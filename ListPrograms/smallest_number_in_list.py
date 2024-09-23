my_list = [5,2,3,4]

print(min(my_list))


def list_min(values):
    x = int(values[0])
    for i in values:
        if int(i) < x:
            x = int(i)
    return x


user_list = input("Enter list of values").split(',')
print(f"min in user list is : {list_min(user_list)}")

#using sort

user_list.sort(reverse=True)
print(user_list[-1])