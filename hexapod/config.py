import lya
from os.path import expanduser
import sys


config = lya.AttrDict.from_yaml('config_default.yml')
config.update_yaml(expanduser('~/.hexapod.yml'))
