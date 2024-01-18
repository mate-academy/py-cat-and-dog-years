from app.main import get_human_age
from pytest import mark, raises, param


@mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
    ],
    ids=[
        "edge case: zero ages",
        "edge case: boundary before conversion changes",
        "boundary age for conversion to 1 human year",
        "boundary age just before next conversion",
        "age at second conversion to human years",
        "age just before uneven conversion for cat and dog",
        "age at uneven conversion for cat and dog",
        "large age numbers",
        "negative ages"
    ]
)
def test_should_return_correct_list(
    cat_age: int,
    dog_age: int,
    expected_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_list


@mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        param(
            "2",
            [2],
            TypeError,
            id="Function should receive integers"
        ),
    ]
)
def test_raising_errors_correctly(
        cat_age: str,
        dog_age: dict,
        expected_exception: Exception
) -> None:
    with raises(TypeError):
        get_human_age(cat_age, dog_age)
