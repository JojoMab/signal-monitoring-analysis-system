import os
import tempfile
import unittest

from signal_analyzer.reader import load_signal_data


class ReaderTest(unittest.TestCase):
    def write_temp_csv(self, content):
        temp_file = tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8")
        temp_file.write(content)
        temp_file.close()
        self.addCleanup(lambda: os.path.exists(temp_file.name) and os.remove(temp_file.name))
        return temp_file.name

    def test_load_signal_data_reads_valid_rows(self):
        csv_path = self.write_temp_csv(
            "frequency_mhz,signal_strength_dbm\n"
            "2400,-35\n"
            "2401,-82\n"
        )

        samples = load_signal_data(csv_path)

        self.assertEqual(len(samples), 2)
        self.assertEqual(samples[0].frequency_mhz, 2400)
        self.assertEqual(samples[1].signal_strength_dbm, -82)

    def test_load_signal_data_rejects_missing_columns(self):
        csv_path = self.write_temp_csv("frequency_mhz,value\n2400,-35\n")

        with self.assertRaisesRegex(ValueError, "Missing required CSV column"):
            load_signal_data(csv_path)

    def test_load_signal_data_rejects_invalid_numbers(self):
        csv_path = self.write_temp_csv("frequency_mhz,signal_strength_dbm\n2400,not-a-number\n")

        with self.assertRaisesRegex(ValueError, "Invalid numeric value"):
            load_signal_data(csv_path)


if __name__ == "__main__":
    unittest.main()
