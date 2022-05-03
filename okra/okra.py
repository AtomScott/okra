import argparse
import logging

from cerberus import Validator
from cerberus.errors import BasicErrorHandler
from omegaconf import OmegaConf
import sys

logger = logging.getLogger(__name__)

LOG_LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
LOG_LEVEL_CHOICE = LOG_LEVELS + list(map(lambda w: w.lower(), LOG_LEVELS))


def _print_message(text):
    print(text)

def _validate_config(config):
    """ Validate the config
    """
    v = Validator(schema, error_handler=BasicErrorHandler(schema))

    if not isinstance(config, dict):
        logger.debug(f'convert config({type(config)}) to dict')
        config = OmegaConf.to_container(config)

    valid = v.validate(config)

    if not valid:
        for i, (key, error) in enumerate(v.errors.items()):
            logger.error(f'({i}), {key}: {error}')
        # raise Exception('config is not valid. See above for details.')
    return True


def load_config(schema_path=None, config_path=None):
    if schema_path is None:
        _print_message('The schema path is not specified.')

    elif config_path is None and len(sys.argv) == 1:
        _print_help
        config_path = sys.argv[1]
    base_config = OmegaConf.load(yaml_path)
    config = OmegaConf.merge(base_config, args)
    _validate_config(config)
    return config


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-yp', '--yaml_path', type=str)
    parser.add_argument('-l', '--log', choices=LOG_LEVEL_CHOICE, help='Set log level.', default='INFO')
    args = vars(parser.parse_args())
    args['numeric_log_level'] = getattr(logging, args['log'].upper(), None)
    return args
