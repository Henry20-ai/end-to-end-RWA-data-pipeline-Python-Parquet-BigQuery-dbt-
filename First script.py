# Import required libraries
import os
from datetime import datetime, timezone

import pandas as pd
import requests

# ---------------------------
# 1) CoinGecko API configuration
# ---------------------------
url = "https://api.coingecko.com/api/v3/coins/markets"
api_key = os.getenv("COINGECKO_API_KEY")
headers = {"x-cg-demo-api-key": api_key} if api_key else {}
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 200,
    "page": 1,
}

# ---------------------------
# 2) Fetch data from the API
# ---------------------------
response = requests.get(url, headers=headers, params=params, timeout=30)
print("Status Code:", response.status_code)
print("Response Data:", response.text[:300])

if response.status_code != 200:
    raise SystemExit(f"API request failed with status {response.status_code}: {response.text[:500]}")

# ---------------------------
# 3) Validate API response
# ---------------------------
try:
    data = response.json()
except ValueError as exc:
    raise SystemExit(f"API returned invalid JSON: {exc}") from exc

if not isinstance(data, list) or len(data) == 0:
    raise SystemExit("Error: API did not return a valid coin list.")

if len(data) != 200:
    print(f"Warning: expected 200 rows, but received {len(data)} rows.")

# ---------------------------
# 4) Clean and prepare the data
# ---------------------------
df = pd.json_normalize(data)
df["ingested_at"] = datetime.now(timezone.utc)

columns_to_keep = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume",
    "circulating_supply",
    "ingested_at",
]
df_cleaned = df[columns_to_keep]

# ---------------------------
# 5) Save data locally as parquet
# ---------------------------
parquet_filename = "rwa_market_data.parquet"
df_cleaned.to_parquet(
    parquet_filename, engine="pyarrow", compression="snappy"
)
print(f"Successfully saved {len(df_cleaned)} rows to {parquet_filename}")