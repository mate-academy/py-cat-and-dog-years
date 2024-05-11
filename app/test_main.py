from app.main import get_human_age


def test_cat_dog_age_must_be_0_when_under_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat_dog_age_must_be_1_when_under_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cat_age_must_be_2_when_26() -> None:
    assert get_human_age(26, 0) == [2, 0]


def test_dog_age_must_be_2_when_29() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_cat_dog_age_must_be_3_when_33_and_35() -> None:
    assert get_human_age(33, 35) == [4, 4]


def test_cat_age_must_be_4_when_40() -> None:
    assert get_human_age(40, 0) == [6, 0]


def test_dog_age_must_be_4_when_45() -> None:
    assert get_human_age(0, 45) == [0, 6]


def test_cat_dog_age_must_be_5_when_48_and_50() -> None:
    assert get_human_age(48, 50) == [8, 7]
