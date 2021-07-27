import unittest
from .solution import generate_document


class GenerateDocumentTests(unittest.TestCase):
    def test_basic(self):
        answer = generate_document(
            "Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"
        )
        self.assertEqual(answer, True)

    def test_basic1(self):
        answer = generate_document(
            "Wil", "Will"
        )
        self.assertEqual(answer, False)


if __name__ == "__main__":
    unittest.main()
