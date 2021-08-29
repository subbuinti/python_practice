


d, y, w = int(input()), None, None

# d = days
# y = years
# w = weeks

# Conversion of days in to years, weeks and days
y = (int)(d / 365)
w = (int)((d % 365) / 7)
d = (int)((d % 365) % 7)

# Output
print(y, "years", w, "weeks", d, "days\n")