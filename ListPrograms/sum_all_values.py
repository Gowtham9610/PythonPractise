new_list = [1,2,3,4,5,]

def list_sum(value):
    total = 0
    for n in value:
        total += int(n)
    return total

print(list_sum(new_list))
user_list =  input("Enter List of values").split(',')
print(user_list)
print(type(user_list))
print(f'Sum of the user list : {list_sum(user_list)}')
