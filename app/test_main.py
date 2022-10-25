import pytest

from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, cat_to_human, dog_to_human",
        [
            pytest.param(
                1, 14, 0, 0,
                id="return 0 when given years less than 15"
            ),
            pytest.param(
                23, 15, 1, 1,
                id="return 1 when given years less than 24"
            ),
            pytest.param(
                24, 27, 2, 2,
                id="return 2 and more when given years more than 24"
            )
        ]
    )
    def test_convert_age_correctly(
            self, cat_age: int,
            dog_age: int,
            cat_to_human: int,
            dog_to_human: int) -> None:
        assert get_human_age(cat_age, dog_age) == [cat_to_human, dog_to_human]
