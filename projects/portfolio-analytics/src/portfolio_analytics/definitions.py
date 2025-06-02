import portfolio_analytics.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=portfolio_analytics.defs)
