age_list = []
sampled_list = []
age_count = int(input("How many ages have been collected? "))
for i in range(age_count):
    age = int(input("Enter age: "))
    age_list.append(age)

for i in range(len(age_list)):
    if i%3==0:
        sampled_list.append(age_list[i])

print("The sampled list is: " , sampled_list)