import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, extended",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age_parametrize(cat_age, dog_age, extended):
    assert get_human_age(cat_age, dog_age) == extended

def test_get_human_age_negative_value():
    assert get_human_age(-1, -1) == [0, 0]
    assert get_human_age(-5, 10) == [0, 0]
    assert get_human_age(10, -5) == [0, 0] or get_human_age(10, -5) == [0, 0]

def test_get_human_age_zero():
    assert get_human_age(14, 14) ==[0, 0]
    assert get_human_age(15, 15) == [1, 1]

def test_get_human_age_large_numbers():
    result = get_human_age(1000, 1000)
    assert result == [246, 197]  # змінено очікування згідно з логікою
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


def test_get_human_age_type_errors():
    with pytest.raises(TypeError):
        get_human_age(15, None)

    with pytest.raises(TypeError):
        get_human_age(15.5, 20)
