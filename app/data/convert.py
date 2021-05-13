from fractions import Fraction
from app.data.get_unit_list import get_units

UNIT_MAP = get_units()

UNIT_TYPES = [*UNIT_MAP]


def convert(unit_type=str, from_unit=str, to=str, amount=float):
    multiplier = UNIT_MAP[unit_type][from_unit][to]['multiply_by']
    fraction = Fraction(multiplier)

    return amount * fraction.numerator / fraction.denominator
