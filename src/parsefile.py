import json
import csv

def parse_fixed_width_file(input_file, spec_file, output_file):

    with open(spec_file, 'r') as f:
        spec = json.load(f)

    column_names = spec['ColumnNames']
    offsets = [int(offset) for offset in spec['Offsets']]
    encoding = spec['FixedWidthEncoding']

    with open(input_file, 'rb') as f:
        data = f.read().decode(encoding)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)

        # Split the data into lines
        records = data.strip().splitlines()
        for record in records:
            row = []
            start = 0
            for offset in offsets:
                temp = record[start:start + offset].strip()
                row.append(temp)
                start += offset
            writer.writerow(row)

if __name__ == '__main__':
    input_file = 'fixed_width_file.txt'
    spec_file = 'spec.json'
    output_file = 'output.csv'
    parse_fixed_width_file(input_file, spec_file, output_file)
