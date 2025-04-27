# Q10) append,insert,remove,pop,copy
my_list = list(input("make a list"))
function = input("what function do u want to perform?: Append,insert,pop,copy,remove")
if function == "append":
    my_list.append("computer")
    print(my_list)
elif function == "insert":
    w = int(input("enter the index"))
    x = input("enter the value")
    my_list.insert(w,x)
    print(my_list)
elif function == "remove":
    y = input("enter the element that you wish to remove")
    my_list.remove(y)
    print(my_list)
elif function == "pop":
    z = int(input("enter the index"))
    my_list.pop(z)
    print(my_list)
elif funtion == "copy":
    my_list.copy()
    print(my_list)
