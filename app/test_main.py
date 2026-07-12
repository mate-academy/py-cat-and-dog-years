import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="before first boundary"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="at first boundary"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="before second boundary"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="at second boundary"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="before third boundary"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="at cat third boundary"
        ),
        pytest.param(
            29,
            29,
            [3, 3],
            id="at dog third boundary"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="large numbers"
        ),
    ]
)
def test_convert_age_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param(
            -1,
            10,
            ValueError,
            id="cat negative age"
        ),
        pytest.param(
            10,
            -1,
            ValueError,
            id="dog negative age"
        ),
        pytest.param(
            "15",
            10,
            TypeError,
            id="cat 'str' age type error"
        ),
        pytest.param(
            10,
            15.5,
            TypeError,
            id="dog 'float' age type error"
        ),
        pytest.param(
            [10],
            10,
            TypeError,
            id="cat 'list' age type error"
        ),
        pytest.param(
            10,
            None,
            TypeError,
            id="dog 'None' age type error"
        ),
    ]
)
def test_invalid_input_raises_error(
        cat_age: object,
        dog_age: object,
        expected_exception: type[BaseException]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
