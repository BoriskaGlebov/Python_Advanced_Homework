import unittest

from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class Decrypt(unittest.TestCase):
    def test_decrypt(self):
        crypt = (
            "абра-кадабра.",
            "абраа..-кадабра",
            "абраа..-.кадабра",
            "абра--..кадабра",
            "абрау...-кадабра",
            "абра........",
            "абр......а.",
            "1..2.3",
            ".",
            "1.......................",
        )
        decrypt_str = (
            "абра-кадабра",
            "абра-кадабра",
            "абра-кадабра",
            "абра-кадабра",
            "абра-кадабра",
            "",
            "а",
            "23",
            "",
            "",
        )
        for num, el in enumerate(crypt):
            with self.subTest(el):
                res = decrypt(el)
                self.assertEqual(res, decrypt_str[num])
