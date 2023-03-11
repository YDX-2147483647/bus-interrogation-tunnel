from __future__ import annotations

from hashlib import md5
from time import time
from typing import TYPE_CHECKING

from requests.auth import AuthBase

if TYPE_CHECKING:
    from requests import PreparedRequest


def get_timestamp() -> int:
    """Get current timestamp

    Returns the number of milliseconds since the epoch,
    which is defined as the midnight at the beginning of January 1, 1970, UTC.

    Equivalent of `new Date().getTime()` in JavaScript.
    """
    return int(time() * 1000)


_MAGIC = "oVw5lgBQ32mygdfZUvYuKAbYtm7DRN37"


def build_headers(_timestamp: int | None = None) -> dict[str, str]:
    """Build headers for authentication

    :param _timestamp: 仅用于单元测试，一般为`None`
    """

    api_time = str(_timestamp or get_timestamp())
    api_token = md5(md5((_MAGIC + api_time).encode()).hexdigest().encode()).hexdigest()
    return {"apitoken": api_token, "apitime": api_time}


class Auth(AuthBase):
    """Authentication"""

    def __init__(self) -> None:
        pass

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers.update(build_headers())
        return r
