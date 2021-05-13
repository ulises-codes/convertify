import csv
import pathlib


def parse_text(text):
    return text.lower().replace(' ', '_')


def main():
    path = pathlib.Path('table.txt')

    with open('src/convertify/resources/data.csv') as csv_file:
        csv_dict = csv.DictReader(csv_file)

        units = []

        headers = ['Unit Type', 'Unit', 'Symbol']
        header = "|" + "|".join(headers) + "|\n"

        divider = "|" + "|".join(['-' * len(h) for h in headers]) + "|\n"

        path.open('a+').write(f'{header}{divider}')

        for row in csv_dict:
            unit = parse_text(row['from'])

            if unit in units:
                continue

            conversion_type = parse_text(row['conversion_type'])
            unit_symbol = parse_text(row['from_symbol'])

            string = f'|{conversion_type}|{unit}|{unit_symbol}|\n'

            path.open('a+').write(string)

            units.append(unit)


if __name__ == "__main__":
    main()
