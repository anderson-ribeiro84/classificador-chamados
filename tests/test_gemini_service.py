
import unittest
from unittest.mock import patch, MagicMock

import httpx2

from google.genai import errors

from services.gemini_service import consultar_gemini


class TestGeminiService(unittest.TestCase):

    def setUp(self):
        """
        Prepara simulações para os testes locais.
        """
        self.patcher_cliente = patch(
            "services.gemini_service.obter_cliente"
        )
        self.patcher_modelo = patch(
            "services.gemini_service.obter_modelo",
            return_value="modelo_teste"
        )
        self.patcher_temperatura = patch(
            "services.gemini_service.obter_temperatura",
            return_value=0.2
        )
        self.patcher_limite_tokens = patch(
            "services.gemini_service.obter_limite_tokens",
            return_value=1024
        )

        self.mock_cliente = self.patcher_cliente.start()
        self.patcher_modelo.start()
        self.patcher_temperatura.start()
        self.patcher_limite_tokens.start()

        self.addCleanup(self.patcher_cliente.stop)
        self.addCleanup(self.patcher_modelo.stop)
        self.addCleanup(self.patcher_temperatura.stop)
        self.addCleanup(self.patcher_limite_tokens.stop)

        self.cliente = MagicMock()
        self.mock_cliente.return_value = self.cliente

    def test_deve_retornar_resposta_com_sucesso(self):
        self.cliente.models.generate_content.return_value.text = (
            "Categoria: Software"
        )

        resultado = consultar_gemini("Problema no sistema ERP")

        self.assertEqual(resultado, "Categoria: Software")

        self.cliente.models.generate_content.assert_called_once_with(
            model="modelo_teste",
            contents="Problema no sistema ERP",
            config={
                "temperature": 0.2,
                "max_output_tokens": 1024,
                "http_options": {
                    "timeout": 30000
                }
            }
        )

    def test_deve_rejeitar_texto_vazio(self):
        with self.assertRaises(ValueError):
            consultar_gemini("")

    def test_deve_rejeitar_resposta_vazia(self):
        self.cliente.models.generate_content.return_value.text = ""

        with self.assertRaises(ValueError):
            consultar_gemini("Problema no sistema ERP")

    def test_deve_tratar_chave_api_invalida(self):
        self.cliente.models.generate_content.side_effect = (
            errors.APIError(
                401,
                {
                    "error": {
                        "message": "Chave inválida",
                        "status": "UNAUTHENTICATED"
                    }
                }
            )
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "Falha de autenticação"
        ):
            consultar_gemini("Problema no sistema ERP")

    def test_deve_tratar_servico_indisponivel(self):
        self.cliente.models.generate_content.side_effect = (
            errors.APIError(
                503,
                {
                    "error": {
                        "message": "Serviço indisponível",
                        "status": "UNAVAILABLE"
                    }
                }
            )
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "temporariamente indisponível"
        ):
            consultar_gemini("Problema no sistema ERP")

    def test_deve_tratar_timeout(self):
        self.cliente.models.generate_content.side_effect = (
            httpx2.TimeoutException("Tempo excedido")
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "tempo limite de comunicação"
        ):
            consultar_gemini("Problema no sistema ERP")

    def test_deve_tratar_falha_de_conexao(self):
        self.cliente.models.generate_content.side_effect = (
            httpx2.ConnectError("Falha de conexão")
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "Não foi possível estabelecer conexão"
        ):
            consultar_gemini("Problema no sistema ERP")


if __name__ == "__main__":
    unittest.main()
