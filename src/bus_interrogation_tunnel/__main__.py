from pprint import pp

from requests import get

from . import Auth

response = get(
    "http://hqapp1.bit.edu.cn/vehicle/get-reserved-seats",
    auth=Auth(),
    params={
        "id": "2208639427336042078",
        "date": "2023-03-11",
    },
)
pp(response.json(), compact=True)
