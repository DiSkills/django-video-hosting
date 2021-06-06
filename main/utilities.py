from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    """ Filename save """

    return f'{datetime.utcnow().timestamp()}{splitext(filename)[1]}'


def ranged(file, start, end, block_size=8192):
    """ Iterator bytes for FileResponse """

    consumed = 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0:
            break
        data = file.read(data_length)
        if not data:
            break
        consumed += data_length
        yield data

    if hasattr(file, 'close'):
        file.close()
