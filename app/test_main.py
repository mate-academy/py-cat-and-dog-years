from app.main import get_human_age

def test_cat_and_dog_age_under_15_should_return_0():
    tests = get_human_age(14,14)
    assert tests[0] == 0
    assert tests[1] == 0

def test_cat_and_dog_age_equal_15_should_return_1():
    tests = get_human_age(15,15)
    assert tests[0] == 1
    assert tests[1] == 1

def test_cat_and_dog_age_higher_15_should_return_1():
    tests = get_human_age(23,23)
    assert tests[0] == 1
    assert tests[1] == 1

def test_cat_and_dog_age_higher_23_should_return_1():
    tests = get_human_age(24,24)
    assert tests[0] == 2
    assert tests[1] == 2

def test_cat_and_dog_age_equal_24_should_return_1():
    tests = get_human_age(24,24)
    assert tests[0] == 2
    assert tests[1] == 2

def test_cat_and_dog_age_higher_26_should_return_1():
    tests = get_human_age(27,27)
    assert tests[0] == 2
    assert tests[1] == 2

def test_cat_and_dog_age_equal_28_should_return_1():
    tests = get_human_age(28,28)
    assert tests[0] == 3
    assert tests[1] == 2

def test_cat_and_dog_age_equal_100_should_return_1():
    tests = get_human_age(100,100)
    assert tests[0] == 21
    assert tests[1] == 17