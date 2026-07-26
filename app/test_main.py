from app import main


# write your code here
def test_get_human_age() -> None:
    assert main.get_human_age(10, 10) == [1, 1]


def test_get_human_age_cat_and_dog_between_15_and_24() -> None:
    assert main.get_human_age(16, 16) == [2, 2]


def test_get_human_age_cat_and_dog_between_25_and_29() -> None:
    assert main.get_human_age(26, 26) == [3, 3]


def test_get_human_age_cat_and_dog_between_30_and_34() -> None:
    assert main.get_human_age(31, 31) == [4, 4]
