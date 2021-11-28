import json
import logging
from redis import StrictRedis
from redis.exceptions import ConnectionError, ResponseError


def redis_client(host: str = 'redis', port: int = 6379, database: int = None, timeout: int = None):
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
    except ConnectionError as ex:
        return ex, 500

    return client


def set_redis(key: str = None, value: dict = None, client: StrictRedis = None):
    """
    Update an key/value store
    """
    response = None
    if key and value:
        try:
            response = client.execute_command('JSON.SET', key, '.', json.dumps(value))
        except ResponseError as e:
            logging.error(e)

    return response


def get_redis(key: str = None, client: StrictRedis = None):
    """
    Update an key/value store
    """
    response = None
    if key:
        try:
            response = json.loads(client.execute_command('JSON.SET', key))
        except ResponseError as e:
            logging.error(e)
    return response
