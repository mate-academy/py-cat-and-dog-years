import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result",
                         [
                             (14, 14, [0, 0]),
                             (15, 15, [1, 1]),
                             (24, 24, [2, 2]),
                             (28, 28, [3, 2]),
                             (100, 100, [21, 17])
                         ],
                         ids=[
                             "both age less than 15, expect 0 years",
                             "both age equal 15, expect 1 ears",
                             "both age equal 15 + 9, expect 2 years",
                             "both age equal 15 + 9 + 4, expect 3 cat, dog 2",
                             "both age equal 100, expect 21 cat, 17 dog"
                         ])
def test_usual_case(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("cat_age, dog_age",
                         [
                             (0, 0),
                             (-1, -1),
                             (0, 0.2),
                             (0, True)
                         ],
                         ids=[
                             "age equal zeros",
                             "age is negative number",
                             "one of age is float",
                             "one of age is bool"
                         ])
def test_data_out_of_normal_range(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize("cat_age, dog_age, error",
                         [
                             (1, "hh", TypeError),
                             (1, [], TypeError),
                             (2, {}, TypeError),
                             (1, (), TypeError)
                         ],
                         ids=[
                             "wrong type string",
                             "wrong type list",
                             "wrong type dict",
                             "wrong type set"
                         ])
def test_wrong_type(cat_age: int, dog_age: any, error: any) -> None:
    if not isinstance(dog_age, int):
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
