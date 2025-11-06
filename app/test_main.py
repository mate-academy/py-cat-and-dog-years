from app.main import get_human_age
import pytest


def test_correct_results() -> None:
    assert get_human_age(cat_age=15, dog_age=15) == [1, 1]
    assert get_human_age(cat_age=14, dog_age=14) == [0, 0]
    assert get_human_age(cat_age=23, dog_age=23) == [1, 1]
    assert get_human_age(cat_age=24, dog_age=24) == [2, 2]


def test_incorrect_values() -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age=-1, dog_age=-1)

    with pytest.raises(ValueError):
        get_human_age(cat_age=0, dog_age=0)

    with pytest.raises(ValueError):
        get_human_age(cat_age=1000, dog_age=2000)


def test_incorrect_data_types() -> None:

    with pytest.raises(TypeError):
        get_human_age(cat_age="five", dog_age=None)

    with pytest.raises(TypeError):
        get_human_age(cat_age=[5], dog_age={"age": 10})
