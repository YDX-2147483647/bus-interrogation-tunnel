from __future__ import annotations

from typing import TYPE_CHECKING

from requests import Session

from .util import build_headers

if TYPE_CHECKING:
    from requests import Response


class Bus:
    session: Session
    api_base_url: str

    def __init__(
        self,
        api_base_url="http://hqapp1.bit.edu.cn",
        session: Session | None = None,
        timestamp: int | None = None,
    ) -> None:
        """
        Parameters:

        - `api_base_url`: Base URL of the API without trailing slash.
          Note that the API does not support HTTPS.

        - `session`: A `requests.Session` to replace the default.
          This can be  used to, amongst other things, adjust proxy or SSL certificate
          settings.

        - `timestamp`: Number of milliseconds since the epoch,
          used to mimic as a time traveler.
        """

        self.api_base_url = api_base_url

        self.session = session or Session()
        self.session.headers.update(build_headers(timestamp))

    def request(self, method: str, endpoint: str, **kwargs) -> Response:
        """API request helper

        Parameters:
        - `method`
        - `endpoint`: Endpoint of th API, start with a slash.
        - `kwargs`: Other keyword arguments for `requests`.
        """

        return self.session.request(method, url=self.api_base_url + endpoint, **kwargs)

    def get(self, endpoint: str, **kwargs) -> Response:
        return self.request("get", endpoint, **kwargs)
