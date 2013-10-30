from yaml import load
from copy import deepcopy

def union(a, b):
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.iteritems():
        if k in result and isinstance(result[k], dict):
            result[k] = union(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result

apps = load(file('instance/apps.yml', 'r'))
settings = load(file('instance/settings.yml', 'r'))

if 'apps' in settings and isinstance(settings['apps'], dict):
	apps = union(apps, settings['apps'])