import os
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

def dir(app):
    return "%s/%s" % (apps[app]['type'], app)

def make_parent(app):
    if not os.path.exists(apps[app]['type']):
        print "Directory %s doesn't exist. Creating %s..." % (apps[app]['type'], apps[app]['type'])
        os.mkdir(apps[app]['type'])

def run(app, command):
    if os.path.exists(dir(app)):
        remote_app_path = "/vagrant/%s" % dir(app)
        command = "cd %s; %s" % (remote_app_path, command)
        os.system("vagrant ssh -c '%s'" % command)
    else:
        print "App does not exist..."