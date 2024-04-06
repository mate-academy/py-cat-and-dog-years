import pytest


from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age", [(0, 0), (14, 14),
                                             (15, 15), (23, 23)])
def test_return_list(cat_age: int, dog_age: int) -> None:
    assert isinstance(
        get_human_age(cat_age=cat_age, dog_age=dog_age), list
    ), "Function must return list"


@pytest.mark.parametrize("cat_age,dog_age", [(0, 0), (14, 14),
                                             (15, 15), (23, 23)])
def test_return_two_elem(cat_age: int, dog_age: int) -> None:
    assert (
        len(get_human_age(cat_age, dog_age)) == 2
    ), "Function must return list of length two"


@pytest.mark.parametrize("cat_age,dog_age", [(0, 0), (14, 14),
                                             (15, 15), (23, 23)])
def test_contents_of_list(cat_age: int, dog_age: int) -> None:
    check_list = [
        isinstance(x, int)
        for x in get_human_age(cat_age=cat_age, dog_age=dog_age)
    ]
    assert all(check_list), "Result list must contain only integers"


@pytest.mark.parametrize("cat_age,dog_age", [(0, 0), (14, 14),
                                             (15, 15), (22, 22)])
def test_all_elements_are_positive(cat_age: int, dog_age: int) -> None:
    check_list = [
        (elem >= 0) for elem in get_human_age(cat_age=cat_age, dog_age=dog_age)
    ]
    assert all(check_list), "Result list must contain only positive integers"


@pytest.mark.parametrize("cat_age,dog_age", [(0, 0), (14, 14),
                                             (13, 10), (7, 5)])
def test_all_zero_if_age_less_fourteen(cat_age: int,
                                       dog_age: int) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == [
        0,
        0,
    ], "Result list must contain only zeros"


@pytest.mark.parametrize("cat_age,dog_age", [(15, 15), (16, 15),
                                             (23, 20), (23, 23)])
def test_animal_with_one_human_year(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == [
        1,
        1,
    ], "Result list must contain only ones"


@pytest.mark.parametrize("cat_age,dog_age", [("24", "a"), (["a"], {"a" : 1})])
def test_wrong_input(cat_age: int, dog_age: int) -> None:
    try:
        get_human_age(cat_age=cat_age, dog_age=dog_age)
    except TypeError:
        return
    else:
        raise Exception("Function must raise TypeError")


@pytest.mark.parametrize("cat_age,dog_age", [(24, 24), (27, 27),
                                             (26, 27), (25, 27)])
def test_animal_with_two_human_year(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == [
        2,
        2,
    ], "Result list must contain only twos"


@pytest.mark.parametrize("cat_age,dog_age", [(-24, -24), (-2, -3),
                                             (-5, -10), (-7, -8)])
def test_animal_with_negative_age(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == [
        0,
        0,
    ], "Result list must contain only zeros"
