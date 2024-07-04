from app.main import get_human_age
from pytest import mark, param


@mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        param(0, 0, [0, 0],
              id="should return 0 if age equal 0"),
        param(14, 14, [0, 0],
              id="should return 0 if age equal 15"),
        param(15, 15, [1, 1],
              id="should return 1 if age equal 15"),
        param(23, 23, [1, 1],
              id="should return 1 if age equal 23"),
        param(24, 24, [2, 2],
              id="should return 2 if age equal 24"),
        param(27, 27, [2, 2],
              id="should return 2 if age equal 27"),
        param(28, 28, [3, 2],
              id="cat must be elder"),
        param(100, 100, [21, 17],
              id="cat must be much elder")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
