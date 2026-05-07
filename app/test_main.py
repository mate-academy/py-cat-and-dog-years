from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="cat 0, dog 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="cat 14, dog 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="cat 15, dog 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="cat 23, dog 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="cat 24, dog 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="cat 27, dog 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat 28, dog 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="cat 100, dog 100"
            ),
        ],
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        human_age: list[int],
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-1, 5),
            (5, -1),
            (-10, -10),
        ]
    )
    def test_negative_ages_raise_value_error(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("15", 15),   # Cat string
            (15, "15"),   # Dog string
            (15.5, 15),   # Cat float
            (15, 15.5),   # Dog float
            (None, 15),   # Cat None
            (15, None),   # Dog None
        ]
    )
    def test_wrong_types_raise_type_error(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)


def test_large_numbers() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


def test_output_changes_when_input_changes() -> None:
    result1 = get_human_age(14, 14)
    result2 = get_human_age(15, 15)
    assert result1 != result2


def test_zero_and_normal() -> None:
    assert get_human_age(0, 15) == [0, 1]
