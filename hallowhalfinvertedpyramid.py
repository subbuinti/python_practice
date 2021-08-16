N = int(input())
star_line = "* " * N
print(star_line)
for row in range(1, N-1):
    hollow_spaces = "  "*(N-row-2)
    hollow_line = "* " + hollow_spaces + "* "
    print(hollow_line)
print("* ")