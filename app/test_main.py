from app.main import get_human_age

# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_calculated_independently():
    # Cat and dog have different conversion rules after 24 years
    assert get_human_age(28, 29) == [3, 3]


def test_large_values():
    assert get_human_age(1000, 1000) == [
        2 + (1000 - 24) // 4,
        2 + (1000 - 24) // 5,
    ]
