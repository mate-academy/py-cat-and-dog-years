def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    
    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
    
    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years
        
    Returns:
        List with [cat_human_age, dog_human_age]
        
    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    # TODO: Implement this function
    human_years = [0, 0]
    animal_years = [cat_age, dog_age]
    for i in range(len(animal_years)):
        if not isinstance(animal_years[i], int):
            raise TypeError("Only 'int' type as accepted as input")
        if animal_years[i] < 0 or animal_years[i] > 100:
            raise ValueError("Only age between 0 and 100 is accepted")
        if animal_years[i] // 15 > 0:
            human_years[i] += 1
            animal_years[i] -= 15
            if animal_years[i] // 9 > 0:
                human_years[i] += 1
                animal_years[i] -= 9
                human_years[i] += animal_years[i] // (4 + i)

    return human_years
