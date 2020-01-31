import pathlib

from environs import Env

BASE_DIR = pathlib.Path(__file__).parent

env = Env()
env.read_env()

SENTRY_DSN = env("SENTRY_DSN")
