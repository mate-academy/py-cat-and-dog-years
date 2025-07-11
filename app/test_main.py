import pytest

from app.main import get_human_age

@pytest.mark.parametrize(
  "cat_age,dog_age,expected_result",
  [
      (-20, -30, [0, 0]),
      (0, 0, [0, 0]),
      (14, 14, [0, 0]),
      (15, 15, [1, 1]),
      (23, 23, [1, 1]),
      (24, 24, [2, 2]),
      (28, 29, [3, 3]),
      (36, 39, [5, 5]),
  ],
  ids=[
      "negative number of years",
      "cat and dog zero years old",
      "cat and dog almost one human year",
      "cat and dog like one human year",
      "cat and dog almost 2 human years",
      "cat and dog like exactly 2 human years",
      "cat and dog like exactly 3 human years",
      "cat and dog like exactly 5 human years",
  ]
)
def test_can_sum(cat_age: int, dog_age: int, expected_result: list) -> None:
  assert get_human_age(cat_age, dog_age) == expected_result
