from app.main import get_human_age
import pytest


class TestGetHumanAge:
    """Testa a conversão de idade de gatos e cachorros para anos humanos"""

    # Testa os exemplos do exercício - são os mais importantes
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ])
    def test_exemplos_oficiais(self, cat_age, dog_age, expected):
        """Testa os casos que vieram no exercício"""
        resultado = get_human_age(cat_age, dog_age)
        assert resultado == expected

    # Testa idades baixas e negativas
    @pytest.mark.parametrize("cat_age, dog_age", [
        (-5, -5),  # Idades negativas
        (-1, -1),  # -1 ano
        (0, 0),  # Zero anos
        (1, 1),  # 1 ano
        (10, 10),  # 10 anos
    ])
    def test_idades_baixas(self, cat_age, dog_age):
        """Testa idades pequenas, zero e negativas"""
        resultado = get_human_age(cat_age, dog_age)
        # Só verifica que não quebra e retorna lista com 2 números
        assert isinstance(resultado, list)
        assert len(resultado) == 2
        assert all(isinstance(idade, int) for idade in resultado)

    # Testa quando só um dos animais tem idade que muda
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (28, 24, [3, 2]),  # Gato muda, cachorro não
        (24, 28, [2, 2]),  # Cachorro não muda ainda em 28
        (29, 29, [3, 3]),  # Ambos mudam
        (100, 50, [21, 7]),  # Idades muito diferentes
    ])
    def test_idades_diferentes(self, cat_age, dog_age, expected):
        """Testa quando gato e cachorro têm idades diferentes"""
        assert get_human_age(cat_age, dog_age) == expected

    # Testa alguns pontos específicos onde a idade muda
    @pytest.mark.parametrize("idade, esperado_gato, esperado_cachorro", [
        (23, 1, 1),  # Antes da segunda mudança
        (24, 2, 2),  # Primeiro ano da segunda fase
        (27, 2, 2),  # Último ano antes da próxima mudança do gato
        (28, 3, 2),  # Gato muda, cachorro não
        (29, 3, 3),  # Cachorro também muda
        (32, 4, 3),  # Gato muda de novo
    ])
    def test_pontos_de_mudanca(self, idade, esperado_gato, esperado_cachorro):
        """Testa os pontos exatos onde a idade humana muda"""
        resultado = get_human_age(idade, idade)
        assert resultado == [esperado_gato, esperado_cachorro]

    # Testa idades altas para ver se o cálculo continua certo
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (40, 40, [6, 5]),
        (50, 50, [8, 7]),
        (60, 60, [11, 9]),
        (80, 80, [16, 13]),
    ])
    def test_idades_altas(self, cat_age, dog_age, expected):
        """Testa com idades mais avançadas"""
        assert get_human_age(cat_age, dog_age) == expected

    # Testa números muito grandes - só verifica que funciona
    @pytest.mark.parametrize("cat_age, dog_age", [
        (10000, 10000),
        (100000, 100000),
    ])
    def test_numeros_grandes(self, cat_age, dog_age):
        """Testa se funciona com números grandes"""
        resultado = get_human_age(cat_age, dog_age)
        # Só verifica que retorna algo razoável
        assert isinstance(resultado, list)
        assert len(resultado) == 2
        assert all(idade >= 0 for idade in resultado)
        # Gato sempre fica mais velho que cachorro na mesma idade
        assert resultado[0] >= resultado[1]


# Testa se a função aceita tipos errados de dados
class TestTiposErrados:
    """Testa o que acontece quando passam tipos de dados errados"""

    @pytest.mark.parametrize("cat_age, dog_age", [
        ("15", 15),  # Texto em vez de número
        (15, "15"),  # Texto no cachorro
        (15.5, 15),  # Número quebrado
        (None, 15),  # Valor vazio
    ])
    def test_tipos_incorretos(self, cat_age, dog_age):
        """Testa se a função lida bem com tipos errados"""
        # A função pode aceitar ou dar erro, qualquer um dos dois está ok
        try:
            resultado = get_human_age(cat_age, dog_age)
            # Se aceitou, verifica que veio algo razoável
            assert isinstance(resultado, list)
            assert len(resultado) == 2
        except (TypeError, ValueError):
            # Se deu erro, também está certo
            pass
