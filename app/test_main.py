from app.main import get_human_age


first_year = 15
second_year = 9
each_year_cat = 4
each_year_dog = 5


def test_should_return_list() -> None:
    cat_age = 20
    dog_age = 20
    check_func_get_human_age = get_human_age(cat_age, dog_age)
    assert isinstance(check_func_get_human_age, list)


def test_should_return_integer_age() -> None:
    cat_age = 20
    dog_age = 20
    check_func_get_human_age = get_human_age(cat_age, dog_age)
    assert all(isinstance(age, int) for age in check_func_get_human_age)


def test_should_checking_for_len_list() -> None:
    cat_age = 20
    dog_age = 20
    check_func_get_human_age = get_human_age(cat_age, dog_age)
    assert len(check_func_get_human_age) == 2


def test_should_checking_for_zero_human_year() -> None:
    cat_age = 14
    dog_age = 14
    check_func_get_human_age = get_human_age(cat_age, dog_age)

    if 0 <= cat_age < first_year:
        assert check_func_get_human_age[0] == 0
    if 0 <= dog_age < first_year:
        assert check_func_get_human_age[1] == 0


def test_should_checking_for_one_human_year() -> None:
    cat_age = 23
    dog_age = 23
    check_func_get_human_age = get_human_age(cat_age, dog_age)

    if first_year <= cat_age < first_year + second_year:
        assert check_func_get_human_age[0] == 1
    if first_year <= dog_age < first_year + second_year:
        assert check_func_get_human_age[1] == 1


def test_should_checking_for_two_human_year() -> None:
    cat_age = 24
    dog_age = 24
    check_func_get_human_age = get_human_age(cat_age, dog_age)

    if (first_year + second_year <= cat_age
            < first_year + second_year + each_year_cat):
        assert check_func_get_human_age[0] == 2
    if (first_year + second_year <= dog_age
            < first_year + second_year + each_year_dog):
        assert check_func_get_human_age[1] == 2


def test_should_checking_for_large_numbers() -> None:
    cat_age = 100
    dog_age = 100
    check_func_get_human_age = get_human_age(cat_age, dog_age)

    if cat_age > first_year + second_year + each_year_cat:
        assert (check_func_get_human_age[0] == 2
                + (cat_age - first_year - second_year) // each_year_cat)

    if dog_age > first_year + second_year + each_year_dog:
        assert (check_func_get_human_age[1] == 2
                + (dog_age - first_year - second_year) // each_year_dog)
