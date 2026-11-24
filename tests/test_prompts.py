import unittest

from prompts import preparar_prompt


class TestPrepararPrompt(unittest.TestCase):

    def test_deve_preparar_prompt_com_chamado_valido(self):
        chamado = "O sistema ERP está sem conexão."

        resultado = preparar_prompt(chamado)

        self.assertIn(chamado, resultado)
        self.assertIn("Categoria:", resultado)
        self.assertIn("Prioridade:", resultado)

    def test_deve_rejeitar_chamado_vazio(self):
        with self.assertRaises(ValueError):
            preparar_prompt("")

    def test_deve_rejeitar_chamado_com_apenas_espacos(self):
        with self.assertRaises(ValueError):
            preparar_prompt("   ")


if __name__ == "__main__":
    unittest.main()
