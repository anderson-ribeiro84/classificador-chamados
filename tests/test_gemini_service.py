
import unittest
from unittest.mock import patch, MagicMock

import httpx2

from google.genai import errors

from services.gemini_service import consultar_gemini


class TestGeminiService(unittest.TestCase):

    @patch("services.gemini_service.obter_modelo")
    @patch("services.gemini_service.obter_cliente")
    def test_deve_retornar_resposta_com_sucesso(
        self, mock_cliente, mock_modelo
    ):
        cliente = MagicMock()

        cliente.models.generate_content.return_value.text = (
            "Categoria: Software"
        )

        mock_cliente.return_value = cliente
        mock_modelo.return_value = "modelo_teste"

        resultado = consultar_gemini("Problema no sistema ERP")

        self.assertEqual(resultado, "Categoria: Software")
        cliente.models.generate_content.assert_called_once()

    def test_deve_rejeitar_texto_vazio(self):
        with self.assertRaises(ValueError):
            consultar_gemini("")

    @patch("services.gemini_service.obter_cliente")
    def test_deve_rejeitar_resposta_vazia(self, mock_cliente):
        cliente = MagicMock()

        cliente.models.generate_content.return_value.text = ""

        mock_cliente.return_value = cliente

        with patch(
            "services.gemini_service.obter_modelo",
            return_value="modelo_teste"
        ):
            with self.assertRaises(ValueError):
                consultar_gemini("Problema no sistema ERP")

    @patch("services.gemini_service.obter_modelo")
    @patch("services.gemini_service.obter_cliente")
    def test_deve_tratar_chave_api_invalida(
        self, mock_cliente, mock_modelo
    ):
        cliente = MagicMock()

        cliente.models.generate_content.side_effect = (
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

        mock_cliente.return_value = cliente
        mock_modelo.return_value = "modelo_teste"

        with self.assertRaisesRegex(
            RuntimeError,
            "Falha de autenticação"
        ):
            consultar_gemini("Problema no sistema ERP")

    @patch("services.gemini_service.obter_modelo")
    @patch("services.gemini_service.obter_cliente")
    def test_deve_tratar_servico_indisponivel(
        self, mock_cliente, mock_modelo
    ):
        cliente = MagicMock()

        cliente.models.generate_content.side_effect = (
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

        mock_cliente.return_value = cliente
        mock_modelo.return_value = "modelo_teste"

        with self.assertRaisesRegex(
            RuntimeError,
            "temporariamente indisponível"
        ):
            consultar_gemini("Problema no sistema ERP")

    @patch("services.gemini_service.obter_modelo")
    @patch("services.gemini_service.obter_cliente")
    def test_deve_tratar_timeout(
        self, mock_cliente, mock_modelo
    ):
        cliente = MagicMock()

        cliente.models.generate_content.side_effect = (
            httpx2.TimeoutException("Tempo excedido")
        )

        mock_cliente.return_value = cliente
        mock_modelo.return_value = "modelo_teste"

        with self.assertRaisesRegex(
            RuntimeError,
            "tempo limite de comunicação"
        ):
            consultar_gemini("Problema no sistema ERP")

    @patch("services.gemini_service.obter_modelo")
    @patch("services.gemini_service.obter_cliente")
    def test_deve_tratar_falha_de_conexao(
        self, mock_cliente, mock_modelo
    ):
        cliente = MagicMock()

        cliente.models.generate_content.side_effect = (
            httpx2.ConnectError("Falha de conexão")
        )

        mock_cliente.return_value = cliente
        mock_modelo.return_value = "modelo_teste"

        with self.assertRaisesRegex(
            RuntimeError,
            "Não foi possível estabelecer conexão"
        ):
            consultar_gemini("Problema no sistema ERP")


if __name__ == "__main__":
    unittest.main()
