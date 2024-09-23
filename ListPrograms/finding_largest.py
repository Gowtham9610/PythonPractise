my_list = [5,2,3,4]

print(max(my_list))

def list_max(values):
    max = 0
    for i in values:
        if int(i) > max:
            max = int(i)
    return max

user_list = input("Enter list of values").split(',')
print(f"Max of the user list is : {list_max(user_list)}")

#using sort

user_list.sort()
print(f"using sort {user_list[-1]}")