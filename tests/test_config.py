import unittest
from unittest.mock import patch

from config import (
    obter_api_key,
    obter_modelo,
    obter_temperatura,
    obter_limite_tokens
)


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

    def test_deve_retornar_temperatura_padrao(self):
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(obter_temperatura(), 0.2)

    def test_deve_retornar_temperatura_configurada(self):
        with patch.dict("os.environ", {
            "GEMINI_TEMPERATURE": "0.7"
        }):
            self.assertEqual(obter_temperatura(), 0.7)

    def test_deve_rejeitar_temperatura_invalida(self):
        with patch.dict("os.environ", {
            "GEMINI_TEMPERATURE": "abc"
        }):
            with self.assertRaises(ValueError):
                obter_temperatura()

    def test_deve_rejeitar_temperatura_fora_do_limite(self):
        with patch.dict("os.environ", {
            "GEMINI_TEMPERATURE": "3"
        }):
            with self.assertRaises(ValueError):
                obter_temperatura()

    def test_deve_retornar_limite_tokens_padrao(self):
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(obter_limite_tokens(), 1024)

    def test_deve_retornar_limite_tokens_configurado(self):
        with patch.dict("os.environ", {
            "GEMINI_MAX_OUTPUT_TOKENS": "2048"
        }):
            self.assertEqual(obter_limite_tokens(), 2048)

    def test_deve_rejeitar_limite_tokens_invalido(self):
        with patch.dict("os.environ", {
            "GEMINI_MAX_OUTPUT_TOKENS": "abc"
        }):
            with self.assertRaises(ValueError):
                obter_limite_tokens()

    def test_deve_rejeitar_limite_tokens_nao_positivo(self):
        with patch.dict("os.environ", {
            "GEMINI_MAX_OUTPUT_TOKENS": "0"
        }):
            with self.assertRaises(ValueError):
                obter_limite_tokens()


if __name__ == "__main__":
    unittest.main()
