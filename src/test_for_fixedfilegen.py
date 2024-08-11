import unittest
import os
import fixedfile

class TestFixedWidthFileGeneration(unittest.TestCase):
    def setUp(self):
        self.json_spec = '''
        {
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
        '''
        self.data = [
            {"f1": "A", "f2": "Data1", "f3": "123", "f4": "1", "f5": "Some data here", "f6": "123456", "f7": "Value7", "f8": "More data", "f9": "Extra", "f10": "End"},
            {"f1": "B", "f2": "Data2", "f3": "456", "f4": "2", "f5": "Another piece", "f6": "654321", "f7": "Value8", "f8": "Additional", "f9": "Info", "f10": "Finish"}
        ]
        self.output_file = 'test_output.txt'

    def test_generate_fixed_width_file(self):
        fixedfile.generate_fixed_width_file(self.json_spec, self.data, self.output_file)
        
        with open(self.output_file, 'r', encoding='windows-1252') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)  # 2 data lines + header
            
            self.assertEqual(lines[0].strip(), "f1   f2          f3 f4 f5             f6      f7        f8           f9                  f10          ")
            self.assertEqual(lines[1].strip(), "A    Data1       123 1 Some data here 123456   Value7    More data    Extra               End          ")
            self.assertEqual(lines[2].strip(), "B    Data2       456 2 Another piece 654321   Value8    Additional    Info                Finish       ")

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()