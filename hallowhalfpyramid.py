N =int(input())
print("* ")
for i in range(N - 2):
    hollow_space = " "*(2*i)
    hollow_line = "* "+ hollow_space + "* "
    print(hollow_line)
star_line = "* " * N
print(star_line)