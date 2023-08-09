import unittest
from frequency_service import FrequencyService


class TestTextProcessing(unittest.TestCase):
    def test_processing(self):
        input_text = "Hel1o Worl'd to!"
        expected_output = "helo world"
        output_text = FrequencyService.process_text(input_text)
        self.assertEqual(output_text, expected_output)


if __name__ == '__main__':
    unittest.main()
