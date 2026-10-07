with staged as (
    select *
    from {{ ref('stg_rwa_market') }}
),

ranked as (
    select
        token_id,
        symbol,
        name,
        current_price,
        market_cap,
        total_volume,
        circulating_supply,
        ingested_at,
        row_number() over (order by total_volume desc nulls last) as volume_rank
    from staged
)

select
    token_id,
    symbol,
    name,
    current_price,
    market_cap,
    total_volume,
    circulating_supply,
    ingested_at,
    volume_rank
from ranked
order by volume_rank asc
