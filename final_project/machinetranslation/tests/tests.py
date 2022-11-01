import unittest
from translator import french_to_english, english_to_french

class Test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), ' ')
        #self.assertEqual(french_to_english('Merci'),'Thank you')

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), ' ')
        #self.assertEqual(english_to_french('Thanks'), 'Merci')
    

unittest.main()