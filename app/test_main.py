from app.main import get_human_age
import pytest
from typing import List, Any


class TestGetHumanAge:
    """Testa a conversão de idade de gatos e cachorros para anos humanos"""

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
    )
    def test_exemplos_oficiais(
        self, cat_age: int, dog_age: int, expected: List[int]
    ) -> None:
        """Testa todos os exemplos fornecidos no exercício"""
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "age_before, age_at, expected_before, expected_at",
        [
            (14, 15, [0, 0], [1, 1]),  # Ambos mudam de 0 para 1
            (23, 24, [1, 1], [2, 2]),  # Ambos mudam de 1 para 2
            (27, 28, [2, 2], [3, 2]),  # Só gato muda
            (28, 29, [3, 2], [3, 3]),  # Só cachorro muda
        ],
    )
    def test_transicoes_de_valor(
        self,
        age_before: int,
        age_at: int,
        expected_before: List[int],
        expected_at: List[int],
    ) -> None:
        """Testa que a saída muda exatamente nos valores de boundary"""
        # Verifica que antes do boundary o valor é o esperado
        assert get_human_age(age_before, age_before) == expected_before
        # Verifica que no boundary o valor muda para o novo esperado
        assert get_human_age(age_at, age_at) == expected_at

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-10, -10),  # Números negativos
            (-1, -1),  # -1
            (0, 0),  # Zero
            (1000000, 1000000),  # Números muito grandes
            (999999999, 999999999),  # Números extremamente grandes
        ],
    )
    def test_dados_fora_faixa_normal(self, cat_age: int, dog_age: int) -> None:
        """Testa dados fora da faixa normal"""
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(x, int) for x in result)
        assert all(x >= 0 for x in result)

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (24, 15, [2, 1]),  # Gato no segundo nível, cachorro no primeiro
            (28, 24, [3, 2]),  # Gato no terceiro nível, cachorro no segundo
            (100, 50, [21, 7]),  # Combinação de idades diferentes
            (32, 34, [4, 4]),  # Diferentes caminhos para mesmo resultado
        ],
    )
    def test_combinacoes_diferentes(
        self, cat_age: int, dog_age: int, expected: List[int]
    ) -> None:
        """Testa combinações onde gato e cachorro têm idades diferentes"""
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "age, expected_cat, expected_dog",
        [
            (15, 1, 1),  # Primeiro threshold
            (23, 1, 1),  # Último ano antes do segundo threshold
            (24, 2, 2),  # Segundo threshold
            (28, 3, 2),  # Gato: (28-24)//4=1 → 3
            (29, 3, 3),  # Gato: 3, Cachorro: 3
            (32, 4, 3),  # Gato: 4, Cachorro: 3
        ],
    )
    def test_padroes_calculo(
        self, age: int, expected_cat: int, expected_dog: int
    ) -> None:
        """Testa padrões específicos de cálculo para verificar a lógica"""
        assert get_human_age(age, age) == [expected_cat, expected_dog]


class TestTiposIncorretos:
    """Testa o comportamento com tipos de dados incorretos"""

    @pytest.mark.parametrize(
        "invalid_cat_age, invalid_dog_age",
        [
            ("15", 15),  # String em vez de int
            (15, "15"),  # String em vez de int
            ("cat", 15),  # String não numérica
            (15.5, 15),  # Float em vez de int
            (15, 15.7),  # Float em vez de int
            (None, 15),  # None value
            ([15], 15),  # Lista em vez de int
            ((15,), 15),  # Tupla em vez de int
        ],
    )
    def test_tipos_incorretos_levantam_excecao(
        self, invalid_cat_age: Any, invalid_dog_age: Any
    ) -> None:
        """Testa que tipos incorretos levantam exceção apropriada"""
        with pytest.raises((TypeError, ValueError)):
            get_human_age(invalid_cat_age, invalid_dog_age)


# Testes de validação de estrutura
@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (15, 15),
        (100, 100),
        (-5, -5),
        (9999, 9999),
    ],
)
def test_estrutura_resultado(cat_age: int, dog_age: int) -> None:
    """Valida que o resultado sempre tem a estrutura correta"""
    result = get_human_age(cat_age, dog_age)

    # Verifica estrutura básica
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)

    # Verifica propriedades lógicas
    assert all(x >= 0 for x in result)
    # Para mesma idade, gato nunca é mais novo que cachorro
    if cat_age == dog_age and cat_age >= 24:
        assert result[0] >= result[1]
