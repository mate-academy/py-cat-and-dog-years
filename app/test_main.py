import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected_human_age"),
    [
        pytest.param(14, 14, [0, 0],
                     id="14 cat/dog years should convert into 0 human age."),
        pytest.param(15, 15, [1, 1],
                     id="15 cat/dog years should convert into 1 human age."),
        pytest.param(23, 23, [1, 1],
                     id="23 cat/dogs years should converts into 1 human age"),
        pytest.param(24, 24, [2, 2],
                     id="24 cat/dogs years should converts into 2 human age"),
        pytest.param(27, 28, [2, 2],
                     id="27 cats/dogs 28 years \
                     should convert into 2 human age"),
        pytest.param(28, 29, [3, 3],
                     id="28 cats/dogs 29 years \
                     should convert into 3 human age"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_get_humans_age_errors() -> None:
    with pytest.raises(TypeError):
        get_human_age("", "")
