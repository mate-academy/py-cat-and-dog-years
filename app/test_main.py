from app.main import get_human_age


def test_should_return_zeros_when_ages_equal_0():
    assert [0, 0] == get_human_age(0, 0)


def test_should_return_zeros_when_ages_less_than_15():
    assert [0, 0] == get_human_age(14, 2)


def test_should_return_correct_output_for_different_ages():
    assert [1, 2] == get_human_age(23, 24)


def test_should_return_different_result_for_28_pets_ages():
    assert [3, 2] == get_human_age(28, 28)


def test_for_extra_ages():
    assert [21, 17] == get_human_age(100, 100)


def test_should_return_zeros_for_ages_less_than_0():
    assert [0, 0] == get_human_age(-213, -523423)
