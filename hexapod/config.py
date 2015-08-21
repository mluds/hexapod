import lya
from pkg_resources import resource_stream
from os.path import expanduser


config = lya.AttrDict.from_yaml(
    resource_stream(__name__, 'config_default.yml')
)
config.update_yaml(expanduser('~/.hexapod.yml'))
