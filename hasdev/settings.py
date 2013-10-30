from yaml import load
from .helpers import union

apps = load(file('instance/apps.yml', 'r'))
settings = load(file('instance/settings.yml', 'r'))

if 'apps' in settings and isinstance(settings['apps'], dict):
	apps = union(apps, settings['apps'])