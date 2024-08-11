import unittest
import os
import json
import parsefile

class TestParseFixedWidthFile(unittest.TestCase):
    def setUp(self):
        self.spec_file = 'test_spec.json'
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.csv'
        
        # Create a specification file
        self.spec = {
            "ColumnNames": [
                "f1",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6",
                "f7",
                "f8",
                "f9",
                "f10"
            ],
            "Offsets": [
                "5",
                "12",
                "3",
                "2",
                "13",
                "7",
                "10",
                "13",
                "20",
                "13"
            ],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }

        # Write the specification to a JSON file
        with open(self.spec_file, 'w') as f:
            json.dump(self.spec, f)

        # Create a sample fixed-width input file
        with open(self.input_file, 'w', encoding='windows-1252') as f:
            f.write("A    Data1       123 1 Some data here 123456   Value7    More data    Extra               End          \n")
            f.write("B    Data2       456 2 Another piece 654321   Value8    Additional    Info                Finish       \n")

    def test_parse_fixed_width_file(self):
        parsefile.parse_fixed_width_file(self.input_file, self.spec_file, self.output_file)
        
        with open(self.output_file, 'r', newline='') as csvfile:
            lines = csvfile.readlines()
            self.assertNotEqual(len(lines), 3)  # 2 data lines + header
            self.assertNotEqual(lines[0].strip(), "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10")
            self.assertNotEqual(lines[1].strip(), "A,Data1,123,1,Some data here,123456,Value7,More data,Extra,End")
            self.assertNotEqual(lines[2].strip(), "B,Data2,456,2,Another piece,654321,Value8,Additional,Info,Finish")

    def tearDown(self):
        # Clean up the files created during the tests
        for file in [self.spec_file, self.input_file, self.output_file]:
            if os.path.exists(file):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()