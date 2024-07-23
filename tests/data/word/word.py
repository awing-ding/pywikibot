import unittest
from src.data.word.word import Word


class MyTestCase(unittest.TestCase):
    def test_wikicodeGenerator(self):
        result_protegore = """
[[Category:Word]]
[[Category:Verbe]]
=== Verbe ===
'''protegore''' pʁotɛgoʁɛ
# 

== Étymologie ==

== Traductions ==
protéger

        """.rstrip().lstrip()
        self.assertEqual(Word(("protéger", "protegore", "pʁotɛgoʁɛ", "verbe", None, None, None, None, None))._wikicode, result_protegore)  # add assertion here


if __name__ == '__main__':
    unittest.main()
