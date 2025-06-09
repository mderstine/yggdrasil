import dagster as dg


@dg.asset
def test_asset(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    """
    A test asset that does nothing but return a MaterializeResult.
    This is used to verify that the asset can be created and executed.
    """
    context.log.info("Executing test asset")
    return dg.MaterializeResult()
