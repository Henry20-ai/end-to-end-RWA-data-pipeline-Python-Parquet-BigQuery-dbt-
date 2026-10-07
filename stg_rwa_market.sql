with source as (
    select *
    from {{ source('RWA_dataset', 'stg_rwa_market_data') }}
),

renamed as (
    select
        safe_cast(id as string) as token_id,
        safe_cast(symbol as string) as symbol,
        safe_cast(name as string) as name,
        safe_cast(current_price as numeric) as current_price,
        safe_cast(market_cap as numeric) as market_cap,
        safe_cast(total_volume as numeric) as total_volume,
        safe_cast(circulating_supply as numeric) as circulating_supply,
        safe_cast(ingested_at as timestamp) as ingested_at
    from source
)

select *
from renamed
