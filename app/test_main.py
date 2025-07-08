import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="if ages equals zeros"),
        pytest.param(14, 14, [0, 0], id="if ages equals 14"),
        pytest.param(15, 15, [1, 1], id="if ages equals 15"),
        pytest.param(28, 28, [3, 2], id="if ages equals 28"),
        pytest.param(100, 100, [21, 17], id="if ages equals 100")
    ]
)
def test_correct_conversation_ages(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_if_cat_and_dog_ages_is_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 4.5)
