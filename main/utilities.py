from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    """ Filename save """

    return f'{datetime.utcnow().timestamp()}{splitext(filename)[1]}'
