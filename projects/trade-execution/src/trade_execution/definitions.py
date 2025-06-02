import trade_execution.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=trade_execution.defs)
