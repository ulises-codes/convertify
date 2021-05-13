import logging
import argparse
from app.data.convert import UNIT_TYPES, UNIT_MAP, convert

parser = argparse.ArgumentParser(description="Convert commonly used units.")
subparsers = parser.add_subparsers(
    help='sub-command help', title="unit type", dest="unit_type")

unit_parsers = {}

for unit_type in UNIT_TYPES:
    unit_parsers[unit_type] = subparsers.add_parser(
        unit_type,
        description=f"Convert a {unit_type} unit."
    )

    unit_parsers[unit_type].add_argument(
        '--from', '-f',
        dest="from",
        choices=[*UNIT_MAP[unit_type]],
        type=str,
        help="The unit you are converting from.",
        required=True
    )

    unit_parsers[unit_type].add_argument(
        '--to', '-to',
        dest="to",
        choices=[*UNIT_MAP[unit_type]],
        type=str,
        help="The unit you are converting to.",
        required=True
    )

    unit_parsers[unit_type].add_argument(
        '--amount', '-a',
        dest="amount",
        type=float,
        help="The amount to convert.",
        required=True
    )

args = parser.parse_args()


def log_args_to_console(**kwargs):
    print(kwargs)


def validate_args(from_unit=str, to=str):
    if from_unit == to:
        logging.critical(f"Cannot convert from {from_unit} to {to}.")


def cli():
    parsed = {**vars(args)}

    validate_args(from_unit=parsed['from'], to=parsed['to'])

    result = convert(
        unit_type=parsed['unit_type'],
        from_unit=parsed['from'],
        to=parsed['to'],
        amount=parsed['amount']
    )

    print(f"{parsed['amount']} {parsed['from']} = {result} {parsed['to']}.")


if __name__ == "__main__":
    cli()
