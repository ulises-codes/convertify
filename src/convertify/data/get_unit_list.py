import csv
import pathlib


csv_file_path = pathlib.Path(__file__).parent.parent.resolve()


def get_units():
    units = {}

    with open(f'{csv_file_path}/resources/data.csv') as unit_file:
        unit_dict = csv.DictReader(unit_file)
        for unit in unit_dict:
            conversion_type = unit['conversion_type'].lower().replace(' ', '_')
            from_symbol = unit['from_symbol'].lower().replace(' ', '_')
            to_symbol = unit['to_symbol'].lower().replace(' ', '_')
            multiply_by = float(unit['multiply_by'])

            if conversion_type in units:
                if from_symbol not in units[conversion_type]:
                    units[conversion_type][from_symbol] = {}
            else:
                units[conversion_type] = {from_symbol: {}}

            units[conversion_type][from_symbol][to_symbol] = {
                **unit, 'multiply_by': multiply_by}

    return units
