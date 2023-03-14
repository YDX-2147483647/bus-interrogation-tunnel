from argparse import ArgumentParser

from rich.pretty import pprint

from bus_interrogation_tunnel import Bus


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="BIT 班车查询接口")
    parser.add_argument("endpoint", help="要询问的结点，例如 /vehicle/get-list")
    parser.add_argument(
        "params", nargs="*", type=parse_params, help="URL 参数，例如 date==2023-03-13，可多个"
    )
    return parser


def parse_params(raw: str) -> tuple[str, str]:
    key, value = raw.split("==", maxsplit=2)
    return key, value


def main() -> None:
    args = build_parser().parse_args()
    api = Bus()
    response = api.get(args.endpoint, params=dict(args.params))
    pprint(response.json())


if __name__ == "__main__":
    main()
