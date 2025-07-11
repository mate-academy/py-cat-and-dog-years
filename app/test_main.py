from app.main import get_human_age
import pytest


def test_cat_and_dog_ages():
    # Test case 1: 14 years should give 0 human age
    result = get_human_age(14, 14)
    assert result == [0, 0]

    # Test case 2: 15 years should give 1 human age
    result = get_human_age(15, 15)
    assert result == [1, 1]

    # Test case 3: 23 years should give 1 human age
    result = get_human_age(23, 23)
    assert result == [1, 1]

    # Test case 4: 24 years should give 2 human age
    result = get_human_age(24, 24)
    assert result == [2, 2]

    # Test case 5: 27/28 years should give 2 human age
    result = get_human_age(27, 28)
    assert result == [2, 2]

    # Test case 6: 28/29 years should give 3 human age
    result = get_human_age(28, 29)
    assert result == [3, 3]