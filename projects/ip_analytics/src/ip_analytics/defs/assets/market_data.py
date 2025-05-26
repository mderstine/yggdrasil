import dagster as dg
import httpx
import polars as pl


@dg.asset(
        name="SOFR",
        key_prefix=["MarketData"],
        group_name="MarketData",
        description="SOFR (Secured Overnight Financing Rate) data from FRED",
        kinds=["polars"],
        # io_manager_key="polars_io_manager",
        # required_resource_keys={"polars_io_manager"},
        # metadata={
        #     "source": "FRED",
        #     "url": "https://fred.stlouisfed.org/series/SOFR"
        # }
)
def sofr(context: dg.AssetExecutionContext) -> dg.MaterializeResult:

    fred_api_key = "41d1cc1b88629e3431c4d2e39bffc925"
    url = f'https://api.stlouisfed.org/fred/series/observations'
    params = {
        "series_id": "SOFR",
        "api_key": fred_api_key,
        "file_type": "json"
    }

    response = httpx.get(url, params=params)
    data = response.json()["observations"]

    sofr = pl.DataFrame(
        {
            "date": [item["date"] for item in data],
            "value": [
                float(item["value"]) if item["value"] else None for item in data
            ]
        }
    )

    context.log.debug(sofr)

    return dg.MaterializeResult()
