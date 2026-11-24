import unittest
from unittest.mock import patch

from config import obter_api_key, obter_modelo


class TestConfiguracoes(unittest.TestCase):

    def test_deve_retornar_chave_configurada(self):
        with patch.dict("os.environ", {
            "GEMINI_API_KEY": "chave_teste"
        }):
            self.assertEqual(obter_api_key(), "chave_teste")

    def test_deve_rejeitar_chave_ausente(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                obter_api_key()

    def test_deve_retornar_modelo_padrao(self):
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(
                obter_modelo(),
                "gemini-3.5-flash-lite"
            )

    def test_deve_retornar_modelo_configurado(self):
        with patch.dict("os.environ", {
            "GEMINI_MODEL": "modelo_teste"
        }):
            self.assertEqual(obter_modelo(), "modelo_teste")


if __name__ == "__main__":
    unittest.main()
