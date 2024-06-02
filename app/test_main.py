from app.main import get_human_age


def test_get_human_age() -> None:
    # Test case 1: both cats and dogs are zero years old
    assert get_human_age(0, 0) == [0, 0]

    # Test case 2: cat is 14 years old, dog is 14 years old
    assert get_human_age(14, 14) == [0, 0]

    # Test case 3: cat is 15 years old, dog is 15 years old
    assert get_human_age(15, 15) == [1, 1]

    # Test case 4: cat is 23 years old, dog is 23 years old
    assert get_human_age(23, 23) == [1, 1]

    # Test case 5: cat is 24 years old, dog is 24 years old
    assert get_human_age(24, 24) == [2, 2]

    # Test case 6: cat is 27 years old, dog is 27 years old
    assert get_human_age(27, 27) == [2, 2]

    # Test case 7: cat is 28 years old, dog is 28 years old
    assert get_human_age(28, 28) == [3, 2]

    # Test case 8: cat is 100 years old, dog is 100 years old
    assert get_human_age(100, 100) == [21, 17]
