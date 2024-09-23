def list_multiple(values):
    total = int(values[0])
    for i in values[1:]:
        total *=int(i)
    return total


my_list = [2,3,4]
print(list_multiple(my_list))
user_list = input("Enter list of value to multiple").split(',')
print(f"user list mulitple is : {list_multiple(user_list)}")

