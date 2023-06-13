import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(None, 3),
        pytest.param(3, "1"),
        pytest.param(3, [3]),
    ],
    ids=[
        "You put incorrect function argument",
        "You put incorrect function argument",
        "You put incorrect function argument",
    ]
)
def test_for_correct_type_put_data(cat_age: int,
                                   dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(0, 0, id="Function argument cannot be negative")
    ]
)
def test_get_human_age_with_negative_values(cat_age: int,
                                            dog_age: int) -> None:
    assert cat_age >= 0 and dog_age >= 0


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(14, 0, [0, 0]),
        pytest.param(0, 14, [0, 0]),
        pytest.param(15, 0, [1, 0]),
        pytest.param(23, 0, [1, 0]),
        pytest.param(0, 15, [0, 1]),
        pytest.param(0, 23, [0, 1]),
        pytest.param(24, 0, [2, 0]),
        pytest.param(27, 0, [2, 0]),
        pytest.param(0, 24, [0, 2]),
        pytest.param(0, 28, [0, 2]),
        pytest.param(28, 29, [3, 3])
    ],
    ids=[
        "Human age should be equal to 0 when cat age less 15",
        "Human age should be equal to 0 when dog age less 15",
        "Human age should be equal to 1 when cat age among 15 and 23",
        "Human age should be equal to 1 when cat age among 15 and 23",
        "Human age should be equal to 1 when dog age among 15 and 23",
        "Human age should be equal to 1 when dog age among 15 and 23",
        "Human age should be equal to 2 when cat age among 24 and 27",
        "Human age should be equal to 2 when cat age among 24 and 27",
        "Human age should be equal to 2 when dog age among 24 and 28",
        "Human age should be equal to 2 when dog age among 24 and 28",
        "Human age should be equal to 3 when cat age 28 and dog age 29"
    ]
)
def test_get_human_age_with_positive_values(cat_age: int,
                                            dog_age: int,
                                            expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
