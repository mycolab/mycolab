import json
import logging
from redis import StrictRedis
from redis.exceptions import ConnectionError, ResponseError


def redis_client(host: str = 'redis', port: int = 6379, database: int = None, timeout: int = None) -> StrictRedis:
    """
    Redis client
    :return: client
    """
    try:
        client = StrictRedis(
            host=host,
            port=port,
            db=database,
            socket_timeout=timeout
        )
    except ConnectionError as e:
        logging.error(e)
        client = None

    return client


def set_value(key: str = None, value: dict = None, client: StrictRedis = None):
    """
    Set a value at key
    """
    response = None
    if key and value:
        try:
            response = client.execute_command('JSON.SET', key, '.', json.dumps(value))
        except ResponseError as e:
            logging.error(e)

    return response


def get_value(key: str = None, client: StrictRedis = None):
    """
    Get a value by key
    """
    response = None
    if key:
        try:
            response = json.loads(client.execute_command('JSON.SET', key))
        except ResponseError as e:
            logging.error(e)
    return response
