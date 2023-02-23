# Сheck Your Code Against the Following Points

## Don't Repeat Yourself

Make sure that your tests don't test the same case few times.

## Clean Code

1. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.

2. Make sure you've tests checks all edged situations such as:
* if output should change with some integer value you should 
check that it is not changed with previous value;
* if function resive data out of normal range, 
such as negative numbers, zero, or realy large numbers;
* if the function receives an incorrect type of data it raises the correct exception.

3. Use ```@pytest.mark.parametrize```
