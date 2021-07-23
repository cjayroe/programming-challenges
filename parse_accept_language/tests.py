from parse_accept_language.solution import parse_accept_language
import unittest


class ParseAcceptLanguageTests(unittest.TestCase):
    def test_basic1(self):
        answer = parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"])
        self.assertEqual(answer,["en-US", "fr-FR"])
    
    def test_basic2(self):
        answer = parse_accept_language("en-US", ["fr-FR"])
        self.assertEqual(answer, [])
    
    def test_language_variant(self):
        answer = parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
        self.assertEqual(answer, ["fr-CA", "fr-FR"])

    def test_double_language_variant(self):
        answer = parse_accept_language("fr, en", ["en-US", "fr-CA", "fr-FR"])
        self.assertEqual(answer, ["fr-CA", "fr-FR", "en-US"])

    def test_en_language_variant(self):
        answer = parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
        self.assertEqual(answer, ["en-US"])

    def test_multi_language_variant(self):
        answer = parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
        self.assertEqual(answer, ["fr-FR", "fr-CA"])

    def test_region_specfic_variant_language_variant(self):
        answer = parse_accept_language("fr, fr-FR", ["en-US", "fr-CA", "fr-FR"])
        self.assertEqual(answer, ["fr-CA", "fr-FR"])



if __name__ == '__main__':
    unittest.main()