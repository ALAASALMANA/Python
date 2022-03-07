def checkIntValue(num):
    try:
        num2 = int(num)
        return True
    except ValueError:
        return False


dict = {
    '9661111111': "ALAA",
    '9662222222': "Reemaz",
    '9663333333': "Ali"
}

print("1-Search by number ")
print("2-Search by Name")
print("3-Add new user")
n = int(input("Enter the number  opreation  ="))
if n == 1:
    num = input("Enter the number phone ")
    c = str(num)
    if len(c) == 10:
        for d in dict:
            if c == d:
                print(dict[c])
                break
        else:
            print("Sorry, the number is not found ")
    else:
        print("This is invalid number")

elif n == 2:
     num = raw_input("Enter the Name:")
     for k, d in dict.items():
        if num == d:
             print(k)
        break

     else:
            print("Sorry, the name is not found ")


elif n == 3:
    num = input("Enter the phone number=")
    name = raw_input("Enter the Name=")
    if int (num) == 10:
           dict[num] = name
           print("The added is successfully added")

    else:
           print("This is invalid number")
