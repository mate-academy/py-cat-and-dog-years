import pytest
from typing import List, Optional
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age, context",
    [
        (0, 0, [0, 0], None),
        (14, 14, [0, 0], None),
        (15, 15, [1, 1], None),
        (23, 23, [1, 1], None),
        (24, 24, [2, 2], None),
        (27, 28, [2, 2], None),
        (28, 29, [3, 3], None),
        (100, 100, [21, 17], None),
        (-2, -1, [0, 0], None),
        ("a", 4.0, None, pytest.raises(TypeError)),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_human_age: Optional[List[int]],
                       context: Optional[object]
                       ) -> None:
    if context is not None:
        with context:
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected_human_age
