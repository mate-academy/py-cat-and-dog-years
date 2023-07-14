import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 14, [0, 0]),
        (15, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (-28, 14, [0, 0]),
        (14, -29, [0, 0]),
        (-28, -29, [0, 0])
    ],
    ids=[
        "0 cat age and 14 dog age converted into 0 human years",
        "15 cat age and 23 dog age converted into 1 human years",
        "24 cat and dog age converted into 2 human years",
        "27 cat age and 28 dog age converted into 2 human years",
        "28 cat age and 29 dog age converted into 3 human years",
        "negative cat age are return 0 human years",
        "negative dog age are return 0 human years",
        "negative cat and dog age are return 0 human years"
    ]

)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("14", 14),
        (14, "14"),
        ("14", "14"),
        (14, [14]),
        ([14], 14)
    ]
)
def test_get_human_age_raises_type_error(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
