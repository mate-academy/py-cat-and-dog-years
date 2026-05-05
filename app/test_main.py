from app.main import get_human_age

def test_should_return_one_for_first_threshold():
    # Exactly 15 should be 1 year
    assert get_human_age(15, 15) == [1, 1]
    # Up to 23 should still be 1 year
    assert get_human_age(23, 23) == [1, 1]

def test_should_return_two_for_second_threshold():
    # Exactly 24 should be 2 years
    assert get_human_age(24, 24) == [2, 2]
    # Cat: 24 + 3 = 27 (still 2); Dog: 24 + 4 = 28 (still 2)
    assert get_human_age(27, 28) == [2, 2]

def test_should_return_three_for_third_threshold():
    # Cat: 24 + 4 = 28 (should be 3); Dog: 24 + 5 = 29 (should be 3)
    assert get_human_age(28, 29) == [3, 3]

def test_high_ages():
    # Check much older animals to ensure the "every 4/5 years" logic works
    assert get_human_age(100, 100) == [21, 17]