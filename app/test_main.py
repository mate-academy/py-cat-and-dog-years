import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial, expected",
        [
            pytest.param([0, 0], [0, 0], id="test cat/dog 0 years"),
            pytest.param([14, 14], [0, 0], id="test cat/dog 14 years"),
            pytest.param([15, 15], [1, 1], id="test cat/dog 15 years"),
            pytest.param([23, 23], [1, 1], id="test cat/dog 23 years"),
            pytest.param([24, 24], [2, 2], id="test cat/dog 24 years"),
            pytest.param([27, 27], [2, 2], id="test cat/dog 27 years"),
            pytest.param([28, 28], [3, 2], id="test cat(3y)/dog(2) 28 years"),
            pytest.param([28, 29], [3, 3], id="test cat(3y)/dog(3) years"),
            pytest.param([100, 100], [21, 17], id="test cat/dog 100 years"),
            pytest.param([15, 14], [1, 0], id="test different years"),
            pytest.param([28, 23], [3, 1], id="test different years 2"),
            pytest.param([100, 0], [21, 0], id="test different years 3"),
        ]
    )
    def test_boundaries_of_age(self, initial: int, expected: int) -> None:
        cat, dog = initial
        assert get_human_age(cat, dog) == expected


class TestGetHumanAgeErrors:
    @pytest.mark.parametrize(
        "inputs, error",
        [
            pytest.param(
                (None, 1),
                TypeError,
                id="should be integer, not None"
            ),
            pytest.param(
                ("3", 2),
                TypeError,
                id="should be integer, not str"
            ),
            pytest.param(
                (2, 1.5),
                TypeError,
                id="should be integer, not float"
            ),
        ]
    )
    def test_invalid_types_raise_typeerror(
            self,
            inputs: int,
            error: Exception
    ) -> None:
        cat, dog = inputs
        with pytest.raises(error):
            get_human_age(cat, dog)

    @pytest.mark.parametrize(
        "inputs, error",
        [
            pytest.param((-1, 0), ValueError, id="should not be negative"),
            pytest.param((0, -5), ValueError, id="should not be negative2"),
            pytest.param((-3, -4), ValueError, id="should not be negative3"),
        ]
    )
    def test_negative_ages_raise_valueerror(
            self,
            inputs: int,
            error: Exception
    ) -> None:
        cat, dog = inputs
        with pytest.raises(error):
            get_human_age(cat, dog)
