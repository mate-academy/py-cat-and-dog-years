from app.main import get_human_age


def test_get_human_age_cat_and_dog_young() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_cat_and_dog_just_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_cat_and_dog_still_one_year() -> None:
    # 23 cat/dog years: still only 1 human year because second threshold is 24
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_cat_and_dog_two_years() -> None:
    # 24 cat/dog years: crosses into 2 human years
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_cat_extra_years() -> None:
    # 27 cat years: (15 + 9 = 24 used) 27-24 = 3 left; 3 // 4 = 0 extra years
    # 28 dog years: (15 + 9 = 24 used) 28-24 = 4 left; 4 // 5 = 0 extra years
    assert get_human_age(27, 28) == [2, 2]


def test_get_human_age_dog_extra_years() -> None:
    # 28 cat years: (15+9=24 used) 28-24 = 4 left; 4 // 4 = 1 extra y → 2+1=3
    # 29 dog years: (15+9=24 used) 29-24 = 5 left; 5 // 5 = 1 extra y → 2+1=3
    assert get_human_age(28, 29) == [3, 3]
