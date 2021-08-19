def message(arg_1, arg_2):
    # Complete this function
    msg = arg_1 + " is " + str(arg_2) + " years old."
    print(msg)

name = input()
age = int(input())
# Call the message function
message(name, age)
