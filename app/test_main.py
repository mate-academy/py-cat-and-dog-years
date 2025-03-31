import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2])
])
def test_excepted_should_be_a_list(cat_age, dog_age, expected) -> None:
    assert isinstance(expected, list)


def test_len_of_expected_is_2():
    expected = get_human_age(19, 19)
    assert len(expected) == 2


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2])
])
def test_should_return_expected_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_should_return_0_when_age_less_15():
    assert get_human_age(8, 8) == [0, 0]
