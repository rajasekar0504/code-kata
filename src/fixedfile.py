import json

def generate_fixed_width_file(spec_file, data, output_file):
    # Parse the JSON specification
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    include_header = spec["IncludeHeader"].lower() == "true"
    
    # Create the header if required
    lines = []
    if include_header:
        header = ''.join(f"{name:<{offsets[i]}}" for i, name in enumerate(column_names))
        lines.append(header)

    # Create the data lines
    for row in data:
        line = ''.join(f"{str(row[name]):<{offsets[i]}}" for i, name in enumerate(column_names))
        lines.append(line)

    # Write to the file with specified encoding
    with open(output_file, 'w', encoding=spec["FixedWidthEncoding"]) as f:
        f.write('\n'.join(lines) + '\n')

if __name__ == '__main__':
# Example usage
    spec_file = 'spec.json'

    data = [
        {"f1": "A", "f2": "Data1", "f3": "123", "f4": "1", "f5": "Some data here", "f6": "123456", "f7": "Value7", "f8": "More data", "f9": "Extra", "f10": "End"},
        {"f1": "B", "f2": "Data2", "f3": "456", "f4": "2", "f5": "Another piece", "f6": "654321", "f7": "Value8", "f8": "Additional", "f9": "Info", "f10": "Finish"}
    ]
    generate_fixed_width_file(spec_file, data, 'fixed_width_file.txt')
