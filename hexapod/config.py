import lya
from pkg_resources import resource_stream
import os.path


config = lya.AttrDict.from_yaml(
    resource_stream(__name__, 'config_default.yml')
)
_user_path = os.path.expanduser('~/.hexapod.yml')
if os.path.isfile(_user_path):
    config.update_yaml(_user_path)
