import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
    ],
    ids=[
        "0 cat/dog years → 0 human years",
        "14 cat/dog years → 0 human years",
        "15 cat/dog years → 1 human year",
        "23 cat/dog years → 1 human year",
        "24 cat/dog years → 2 human years",
        "27 cat/dog years → 2 human years",
        "28 cat years → 3, 27 dog years → 2",
        "29 cat years → 3, 29 dog years → 3",
    ]
)
def test_get_human_age(a: int, b: int, result: list) -> None:
    assert get_human_age(a, b) == result

# @pytest.mark.parametrize(
#     "a", "b", "result",
#     [
#         (15, 15, [1, 1]),
#         (23, 19, [1, 1]),
#         (21, 20, [1, 1]),
#     ]
# )
# def test_get_human_age_one(a: int, b: int, result: list) -> None:
#     assert get_human_age(a, b) == result
#
# @pytest.mark.parametrize(
#     "a", "b", "result",
#     [
#         (24, 25, [2,2]),
#         (26, 27, [2,2])
#     ]
# )
# def test_get_human_age_two(a: int, b: int, result: list) -> None:
#     assert get_human_age(a, b) == result
#
#
# @pytest.mark.parametrize(
#     "a", "b", "result",
#     [
#         (30, 35, [3, 4]),
#         (39, 45, [5, 6]),
#         (47, 49, [7, 7]),
#         (100, 100, [21, 17]),
#     ]
# )
# def test_get_human_age_three_and_more(a: int, b: int, result: list) -> None:
#     assert get_human_age(a, b) == result