import ip_analytics.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=ip_analytics.defs)
