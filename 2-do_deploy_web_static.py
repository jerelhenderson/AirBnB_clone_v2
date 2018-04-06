#!/usr/bin/python3
"""
Fabric script generates .tgz archive from contents of web_static directory
"""
from fabric.api import local
from datetime import datetime


env.hosts = ['54.152.200.18', '54.224.57.104']


def do_pack():
    """ return archive path if successful """
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(
            cur_time))
        return ("versions/web_static_{}.tgz".format(cur_time))
    except:
        return None

import os


def do_deploy(archive_path):
    """ return `True` if successful """

    if os.path.exists(archive_path):
        return None
    else:
        return False

    try:
        put(archive_path, "/tmp"))
        run("mkdir -p /data/web_static/releases/{}".format())
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format())
        run("rm /tmp/{}".format())
        run("mv /data/web/static/releases/{}".format())
        run("rm -rf /data/web_static/relases/{}".format())
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases{}".format())
        return True
    except:
        return False
