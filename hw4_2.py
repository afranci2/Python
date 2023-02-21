def sumDigits(user_number):
    new_number = str(user_number)
    total_sum=0
    for i in range(len(new_number)):
        total_sum += int(new_number[i])
    return(total_sum)