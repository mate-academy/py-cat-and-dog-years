import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age: int, dog_age: int, expected: int",
    [
        # --- Casos de Borda: 0 anos humanos ---
        (0, 0, [0, 0]),  # Zero absoluto
        (14, 14, [0, 0]),  # Limite máximo antes de completar 1 ano humano

        # --- Casos de Borda: 1 ano humano ---
        (15, 15, [1, 1]),  # Exatos 15 anos (primeiro ano completo)
        (23, 23, [1, 1]),  # Limite máximo antes de completar 2 anos humanos

        # --- Casos de Borda: 2 anos humanos ---
        (24, 24, [2, 2]),
        # Exatos 24 anos (segundo ano completo)
        (27, 28, [2, 2]),
        # Limite máximo para Gato (27) e Cão (28) antes do 3º ano

        # --- Casos de Borda: 3 anos humanos ---
        (28, 29, [3, 3]),  # Primeiro incremento após os 24 anos

        # --- Casos de Borda: Valores Extremos (Large Numbers) ---
        (100, 100, [21, 17]),  # Verificação de lógica de longo prazo

        # --- Casos de Borda: Números Negativos ---
        (-5, -10, [0, 0]),  # Tratamento de dados fora do range normal
    ],
    ids=[
        "zero_age", "just_before_1_year",
        "exactly_1_year", "just_before_2_years",
        "exactly_2_years", "max_edge_for_2_years",
        "start_of_3_years", "large_numbers",
        "negative_ages"
    ]
)
def test_get_human_age_logic(
        cat_age: int,
        dog_age: int,
        expected: int
) -> None:
    """
    Testa a conversão de idades garantindo que os limites (15, 24, 28/29)
    estão disparando as mudanças corretamente (DRY e Edge Cases).
    """
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
