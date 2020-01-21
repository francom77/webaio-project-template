import pathlib

import yaml
from environs import Env

BASE_DIR = pathlib.Path(__file__).parent
config_path = BASE_DIR / 'config' / 'settings.yml'

env = Env()
env.read_env()

SENTRY_DSN = env("SENTRY_DSN")


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)
