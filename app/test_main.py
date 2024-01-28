from app.main import get_human_age


# write your code here
def test_both_are_zeros_when_less_than_15():
    assert get_human_age(14, 14) == [0, 0], \
        "Should return zeros when age of both animals is less tha 15"


def test_both_are_ones_when_from_15_to_23():
    assert get_human_age(15, 23) == [1, 1], \
        "Should return ones when age of both animals is from 15 to 23"


def test_cat_is_3_dog_is_2_when_both_are_28():
    assert get_human_age(28, 28) == [3, 2], \
        "Cat is 3 and dog is 2 when both are 28"


def test_cat_is_21_dog_is_17_when_both_are_100():
    assert get_human_age(100, 100) == [21, 17], \
        "Cat is 21 and dog is 17 when both are 100"
