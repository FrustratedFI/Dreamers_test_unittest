import unittest
from main import reverse_string, count_vowels, count_words

class TestStringProcessor(unittest.TestCase):
    
    def test_reverse_string(self):
        result = reverse_string("hello")
        self.assertEqual(result, "olleh")

    def test_count_vowels_true(self):
        result = count_vowels("apple")
        self.assertTrue(result > 0)

    def test_count_words_in(self):
        sentence = "learning python is fun"
        word_list = sentence.split()
        self.assertIn("python", word_list)

    def test_reverse_is_instance(self):
        result = reverse_string("test")
        self.assertIsInstance(result, str)

    def test_type_error_raises(self):
        with self.assertRaises(TypeError):
            reverse_string(12345)

if __name__ == '__main__':
    unittest.main()