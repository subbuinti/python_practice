N = int(input())
M = int(input())
star_line = "* " * M
print(star_line)
for i in range(N-2):
    hollow_spaces = "  "*(M-2)
    hollw_line = "* " + hollow_spaces + "* "
    print(hollw_line)
print(star_line)