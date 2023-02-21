import pytest

from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(0, 0, [0, 0],
                         id="must return 0"),
            pytest.param(14, 14, [0, 0],
                         id="must return 0"),
            pytest.param(15, 15, [1, 1],
                         id="must return 1 for cat, 1 for dog"),
            pytest.param(23, 23, [1, 1],
                         id="must return 1 for cat, 1 for dog"),
            pytest.param(24, 24, [2, 2],
                         id="must return 2 for cat, 2 for dog"),
            pytest.param(27, 27, [2, 2],
                         id="must return 2 for cat, 2 for dog"),
            pytest.param(28, 28, [3, 2],
                         id="must return 3 for cat, 2 for dog"),
            pytest.param(100, 100, [21, 17],
                         id="must return 0"),
            pytest.param(-1, -1, [0, 0],
                         id="must return 0"),
        ]
    )
    def test_to_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error_if_age_not_a_number() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", [1])
