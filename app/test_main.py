from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected_result",  [
                                                    (-10, 23, [0, 1]),
                                                    (23, -1, [1, 0]),
                                                    (14, 14, [0, 0]),
                                                    (15, 15, [1, 1]),
                                                    (23, 23, [1, 1]),
                                                    (24, 24, [2, 2]),
                                                    (27, 28, [2, 2]),
                                                    (28, 29, [3, 3]),
                                                    (100, 100, [21, 17]),
                                                    ])
def test_should_return_different_ages(cat_age, dog_age, expected_result):
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age, dog_age, expected_exception",  [
                                                    ("28", 29, TypeError),
                                                    (28, "29", TypeError)])
def test_should_return_type_error(cat_age, dog_age, expected_exception):
    with pytest.raises(TypeError):
        assert get_human_age(cat_age, dog_age)
