import pytest

from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(0, 0, [0, 0],
                         id="Human age is zero when pets age are zero"),
            pytest.param(14, 14, [0, 0],
                         id="Human age is zero when pets age < 15"),
            pytest.param(15, 15, [1, 1],
                         id="Human age is 1 when pets age are == 15"),
            pytest.param(23, 23, [1, 1],
                         id="Human age is 1 when pets age == 23"),
            pytest.param(24, 24, [2, 2],
                         id="Human age is 2 when pets age == 24"),
            pytest.param(27, 27, [2, 2],
                         id="Human age is 2 when pets age == 27"),
            pytest.param(28, 28, [3, 2],
                         id="Human age for car is 3 when cat age is 28 and "
                            "human age for dog is 2 when dog age 28"),
            pytest.param(28, 28, [3, 2],
                         id="Human age is 3 when"
                            " cat age is 28 and dog age 29"),
            pytest.param(100, 100, [21, 17],
                         id="100 in Human age when cat is 21 and dog is 17"),
            pytest.param(-1, -1, [0, 0],
                         id="Human age is zero when pets age is negative"),
        ]
    )
    def test_to_age_cat_and_dog_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error_if_age_not_a_number() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", [1])
