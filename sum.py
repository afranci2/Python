n=19
if(n%10==0):
    print(True)
elif (n%2==0):
    print(False)
else:
    sum_of_digits=0
    iteration_count=0
    while sum_of_digits != 1:
        number_to_string=str(n)
        for i in range(len(number_to_string)):
            single_digit = int(number_to_string[i])
            sum_of_digits += (single_digit**2)
        if (sum_of_digits==1):
            break
        else: 
            n=sum_of_digits
            iteration_count += 1
        if iteration_count>2^100:
            print(False)
