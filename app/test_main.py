from app.main import get_human_age

def test_zero_age_cat_dog() -> None:
    cat_age = 0
    dog_age = 0
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]

def test_middle_age_cat_dog()-> None:
    cat_age = 24
    dog_age = 24
    result = get_human_age(cat_age, dog_age)
    assert result == [2, 2]

def test_near_age_cat_dog()-> None:
    cat_age = 14
    dog_age = 14
    result = get_human_age(cat_age, dog_age)
    if cat_age < 15 and dog_age < 15:
        assert result == [0, 0]

def test_different_age_cat_dog()-> None:
    cat_age = 35
    dog_age = 29
    result = get_human_age(cat_age, dog_age)
    if 32 <= cat_age <= 35 and 28 <= dog_age <= 32:
        assert result == [4, 3]


# write your code here
