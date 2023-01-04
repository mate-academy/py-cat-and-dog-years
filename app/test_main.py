import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result_cat, result_dog",
                         [
                             (0, 0, 0, 0),
                             (14, 14, 0, 0),
                             (15, 15, 1, 1),
                             (23, 23, 1, 1),
                             (24, 24, 2, 2),
                             (27, 27, 2, 2),
                             (28, 28, 3, 2),
                             (100, 100, 21, 17),
                             (-34, -23, 0, 0)
                         ]
                         )
def test_output_should_change_with_different_input(
        cat_age: int,
        dog_age: int,
        result_cat: int,
        result_dog: int) -> None:
    assert (get_human_age(cat_age, dog_age) == [result_cat, result_dog]), \
        f"Cat years {cat_age} should be equal to {result_cat}. " \
        f"Dog years {dog_age} should be equal to {result_dog}"


@pytest.mark.parametrize("cat_age, dog_age",
                         [
                             ("14", "25"),
                             ((25,), (57,)),
                             ({47}, {24}),
                             ([35.5], [24])
                         ]
                         )
def test_incorrect_type_input(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

