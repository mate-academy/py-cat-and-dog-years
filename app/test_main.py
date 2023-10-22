import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Age of 0 should be equal to zero"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Age of 14 should be equal to zero"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Age of 15 should be equal to 1"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Age of 23 should be equal to 1"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Age of 24 should be equal to 2"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Age of 27 should be equal to 3"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Age of 100 should return correct values"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="Negative age should return zero"
        )
    ]
)
def test_should_return_correct_values(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ([1], [1]),
        ((1,), (1,)),
        ({1}, {1}),
        ("1", "1"),
        (None, None)
    ]
)
def test_raise_errors_for_incorrect_type_of_age(
        cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
