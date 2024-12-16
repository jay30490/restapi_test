import os
import random


def read_var(fld: str) -> str:
    """
    Reading env variable value

    :param fld: env variable name
    :return: env variable value in string format
    """
    return str(os.getenv(fld))


def generate_id():
    """
    Method for generating a random ID in range 1 - 10 000.

    :return: string with generated ID
    """
    return str(random.randrange(0, 10000))


def get_brand_fld(resp_json: list, data: str, key_fld: str, src_fld: str) -> str:
    """
    Get field value from the list of dicts by stating another key: value data

    :param resp_json: list of dicts
    :param data: value of the key in search
    :param key_fld: known item key
    :param src_fld: value of the known item key
    :return:
    """
    get_fld = ''
    for i in resp_json:
        for k, v in i.items():
            if k == key_fld and v == data:
                get_fld = i[src_fld]
                break
    return get_fld
