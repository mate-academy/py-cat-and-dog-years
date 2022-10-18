# Cat and Dog years

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Inside `app/test_main.py`, write tests for `get_human_age` function that 
takes two integers `cat_age` (my cat's age in cat years) and `dog_age` 
(my dog's age in dog years) and returns an array where:

- the first element is my cat's age in human years;
- the second element is my dog's age in human years.

As usually age is a whole number of years (discard the remainder).

Cat years are converted to human years following the next rules:

- first 15 cat years give 1 human year;
- the next 9 cat years give 1 more human year;
- every 4 next cat years give 1 extra human year.

Dog years:

- first 15 dog years give 1 human year;
- the next 9 dog years give 1 more human year;
- every 5 next dog years give 1 extra human year.

**Please note:** you have to use `pytest` for writing tests.

Examples:
```python
get_human_age(0, 0) == [0, 0]
get_human_age(14, 14) == [0, 0]
get_human_age(15, 15) == [1, 1]
get_human_age(23, 23) == [1, 1]
get_human_age(24, 24) == [2, 2]
get_human_age(27, 27) == [2, 2]
get_human_age(28, 28) == [3, 2]
get_human_age(100, 100) == [21, 17]
```

Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.