import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(0, 0, [0, 0],
                     id="cat 0 and dog 0 years gives [0, 0]"),
        pytest.param(15, 15, [1, 1],
                     id="cat 15 and dog 15 years gives [1, 1]"),
        pytest.param(24, 24, [2, 2],
                     id="cat 24 and dog 24 years gives [2, 2]"),
        pytest.param(14, 14, [0, 0],
                     id="cat 14 and dog 14 years gives [0, 0]"),
        pytest.param(100, 100, [21, 17],
                     id="cat 100 and dog 100 years  gives [21, 17]"),
        pytest.param(24, 100, [2, 17],
                     id="cat 24 and dog 100 years  gives [2, 17]"),
        pytest.param(100, 28, [21, 2],
                     id="cat 100 and dog 28 years  gives [21, 2]"),
        pytest.param(23, 23, [1, 1],
                     id="cat 23 and dog 23 years  gives [1, 1]"),
        pytest.param(27, 27, [2, 2],
                     id="cat 27 and dog 27 years  gives [2, 2]"),
        pytest.param(28, 28, [3, 2],
                     id="cat 28 and dog 28 years  gives [3, 2]"),
        pytest.param(15, 14, [1, 0],
                     id="cat 15 and dog 14 years  gives [1, 0]"),
        pytest.param(0, 14, [0, 0],
                     id="cat 0 and dog 14 years  gives [0, 0]"),
        pytest.param(24, 10, [2, 0],
                     id="cat 24 and dog 10 years  gives [2, 0]"),
        pytest.param(27, 27, [2, 2],
                     id="cat 27 and dog 27 years  gives [2, 2]"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list
                       ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, \
        "get human age should equal expected result"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(-1, 0),
        pytest.param(1, -1),
        pytest.param(1.1, 2.1),
        pytest.param(None, 1),
        pytest.param("five", 0),
    ]
)
def test_invalid_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
