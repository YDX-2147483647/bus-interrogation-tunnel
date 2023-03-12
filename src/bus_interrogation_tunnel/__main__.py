from pprint import pp

from bus_interrogation_tunnel import Bus

api = Bus()
response = api.get(
    "/vehicle/get-reserved-seats",
    params={
        "id": "2208639427336042078",
        "date": "2023-03-11",
    },
)
pp(response.json(), compact=True)
