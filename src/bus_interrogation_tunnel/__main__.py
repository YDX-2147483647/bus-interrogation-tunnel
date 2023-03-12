from __future__ import annotations

from argparse import ArgumentParser
from typing import TYPE_CHECKING

from rich.pretty import pprint

from bus_interrogation_tunnel import Bus

if TYPE_CHECKING:
    from argparse import Namespace


def build_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("endpoint")
    parser.add_argument("params", nargs="+", type=parse_params)
    return parser


def parse_params(raw: str) -> tuple[str, str]:
    key, value = raw.split("==", maxsplit=2)
    return key, value


def main(args: Namespace) -> None:
    api = Bus()
    pprint(args.params)
    response = api.get(args.endpoint, params=dict(args.params))
    pprint(response.json())


if __name__ == "__main__":
    main(build_parser().parse_args())
