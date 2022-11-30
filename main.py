# write your code here
favorite_animals = ['dog','cat','monkey','rabbit']
print(favorite_animals[1])
favorite_animals.remove('monkey')
favorite_animals.append('parrot')
for x in favorite_animals:
    print(f"i love {x}")

numbers = [1,2,3,4,5]
number_sum = 0
for number in numbers:
    number_sum += number
print(number_sum)