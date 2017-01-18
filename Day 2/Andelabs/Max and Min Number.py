def find_max_min(numbers): #define the function that takes an argument
    min_max = []           #assign variables to the max and min
    max_num = max(numbers)
    min_num = min(numbers)

    if isinstance(numbers, list):    #Identify the max and min numbers of the list
        if max_num==min_num:
            min_max.append(max_num)
            return min_max
        else:
            min_max.append(min_num)
            min_max.append(max_num)
            return min_max

    else:
        return None
