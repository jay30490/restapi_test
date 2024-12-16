import yaml

from pathlib import Path


ENDPOINTS = 'endpoints.yml'
ENDPOINTS_PATH = 'cfg/'


def get_config_path(file_name: str = ENDPOINTS,
                    file_path: str = ENDPOINTS_PATH) -> str:
    return Path(__file__).parent.joinpath(f'{file_path}{file_name}')


def read_config_file(file_path: str):
    with open(file_path, 'r') as cfg_file:
        return yaml.load(cfg_file, Loader=yaml.SafeLoader)


config_path = get_config_path()
conf = read_config_file(config_path)
