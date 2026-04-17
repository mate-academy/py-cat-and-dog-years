import pytest


from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="zero ages"),
    pytest.param(14, 14, [0, 0], id="last year before first human year"),
    pytest.param(15, 15, [1, 1], id="first human year"),
    pytest.param(23, 23, [1, 1], id="last year of first human year"),
    pytest.param(24, 24, [2, 2], id="second human year"),
    pytest.param(27, 27, [2, 2], id="last year of second human year"),
    pytest.param(28, 28, [3, 2], id="cat advances dog does not"),
    pytest.param(29, 29, [3, 3], id="dog boundary advances at 29"),
    pytest.param(100, 100, [21, 17], id="old age"),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_validate_input_correctly() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 0)


def test_should_validate_input_type_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age([1, 2, 3], "a")
