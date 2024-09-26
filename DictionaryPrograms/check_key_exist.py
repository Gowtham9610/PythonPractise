dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}


def check_in_key(mykey,dic):
    if mykey in dic:
        print("key already in dictionary")
    else:
        print("key not in dictionary")

check_in_key(3,dic1)
