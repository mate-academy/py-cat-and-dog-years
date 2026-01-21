import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_ages,dog_ages,human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_converter_age_from_human_to_animal(cat_ages: int,
                                            dog_ages: int,
                                            human_ages: list) -> None:
    assert get_human_age(cat_ages, dog_ages) == human_ages


def test_for_data_type() -> None:
    if type(get_human_age(5, 5)) != list:
        raise Exception("The function get_human_age "
                        "should return list type of data")
    else:
        assert type(get_human_age(5, 5)) == list
