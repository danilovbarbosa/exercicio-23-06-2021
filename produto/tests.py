from django.test import TestCase

from produto.models import Produto
from produto.serializers import ProdutoSerializer


class TestProdutoSerializer(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.atributos = {
            "nome": "teste 1",
            "preco": 100,
            "marca": "teste 1",
            "descricao": "teste 1",
        }

        self.serializer_data = {
            "nome": "teste 1",
            "preco": 100,
            "marca": "teste 1",
            "descricao": "teste 1",
        }

        self.objeto = Produto.objects.create(**self.atributos)
        self.objeto_serializer = ProdutoSerializer(instance=self.objeto)

    def test_contains_expected_fields(self):
        data = self.objeto_serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "nome",
                    "preco",
                    "marca",
                    "descricao",
                ]
            ),
        )
