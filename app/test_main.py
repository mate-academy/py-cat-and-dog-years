import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-2, -1, [0, 0], id="cat and dog negative numbers"),
        pytest.param(0, 0, [0, 0], id="cat and dog zero age"),
        pytest.param(14, 14, [0, 0], id="cat and dog 14 age"),
        pytest.param(15, 15, [1, 1], id="cat and dog 15 age"),
        pytest.param(23, 23, [1, 1], id="cat and dog 23 age"),
        pytest.param(24, 24, [2, 2], id="cat and dog 24 age"),
        pytest.param(27, 28, [2, 2], id="cat and dog 27,28 age"),
        pytest.param(28, 29, [3, 3], id="cat and dog 28,29 age"),
        pytest.param(28, 28, [3, 2], id="cat and dog 28 age"),
        pytest.param(100, 100, [21, 17], id="cat and dog 100 age")
    ]
)
def tests_checks_all_edged_situations(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_incorrect_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", [28])
