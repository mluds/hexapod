import yaml
from os.path import expanduser


def _merge(default, update):
    pass


def _load_config():
    config = {}
    with open('config_default.yml') as default:
        with open(expanduser('~/.hexapod.yml')) as user:
            config = _merge(default, user)
    return config


config = _load_config()
