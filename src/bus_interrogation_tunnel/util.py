from hashlib import md5
from time import time


def get_timestamp() -> int:
    """Get current timestamp

    Returns the number of milliseconds since the epoch,
    which is defined as the midnight at the beginning of January 1, 1970, UTC.

    Equivalent of `new Date().getTime()` in JavaScript.
    """
    return int(time() * 1000)


_MAGIC = "oVw5lgBQ32mygdfZUvYuKAbYtm7DRN37"


def build_headers(timestamp: int | None = None) -> dict[str, str]:
    """Build headers for authentication

    :param timestamp: 仅用于单元测试，一般为`None`
    """

    api_time = str(timestamp or get_timestamp())
    api_token = md5(md5((_MAGIC + api_time).encode()).hexdigest().encode()).hexdigest()
    return {"apitoken": api_token, "apitime": api_time}
