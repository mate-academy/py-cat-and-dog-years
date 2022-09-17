from app.main import get_human_age


def test_equal_right_result():
    args = (
        {"cat_age": 15, "dog_age": 15, "human_age": [1, 1]},
        {"cat_age": 24, "dog_age": 24, "human_age": [2, 2]},
        {"cat_age": 28, "dog_age": 29, "human_age": [3, 3]},
        {"cat_age": 70, "dog_age": 70, "human_age": [13, 11]},
        {"cat_age": 100, "dog_age": 100, "human_age": [21, 17]}
    )
    for i in range(len(args)):
        assert get_human_age(
            args[i]["cat_age"], args[i]["dog_age"]) == args[i]["human_age"]


def test_result_should_is_list():
    assert isinstance(get_human_age(10, 10), list)
