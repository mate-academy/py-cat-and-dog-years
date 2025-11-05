import pytest
from app.main import get_human_age

@pytest.mark.parametrize("cat_in, dog_in, expected_cat, expected_dog", [
    # Testy diagnostyczne i graniczne
    (2, 3, 0, 0),       # poniżej progu
    (14, 14, 0, 0),     # tuż przed progiem
    (15, 15, 1, 1),     # dokładnie na progu
    (16, 16, 1, 1),     # tuż po progu
    (23, 23, 1, 1),     # górna granica drugiego etapu
    (24, 24, 2, 2),     # początek trzeciego etapu
    (27, 27, 2, 2),
    (28, 28, 3, 2),
    (29, 29, 3, 3),
    (33, 33, 4, 3),
    (37, 37, 5, 4),
    (41, 41, 6, 5),
    (45, 45, 7, 6),
    (49, 49, 8, 7),
    (53, 53, 9, 7),
    (57, 57, 10, 8),
    (61, 61, 11, 9),
    (65, 65, 12, 10),
    (100, 100, 21, 17),
])
def test_get_human_age(cat_in, dog_in, expected_cat, expected_dog):
    result = get_human_age(cat_in, dog_in)
    assert result[0] == expected_cat, f"Wiek Kota: Oczekiwano {expected_cat}, otrzymano {result[0]} dla wejścia {cat_in}"
    assert result[1] == expected_dog, f"Wiek Psa: Oczekiwano {expected_dog}, otrzymano {result[1]} dla wejścia {dog_in}"
