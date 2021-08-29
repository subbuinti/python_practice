x =  input()


def calc(t):
    temp = float(t[:-1])
    scale = t[-1]
    if(scale=="C" or scale=="c"):
        print("{:}C".format(temp))
        print("{:}F".format((temp * 9/5) + 32))
        print("{:}K".format(temp+273))
    elif (scale=="F" or scale=="f"):
        print("{:.2f}C".format((temp - 32) * 5/9))
        print("{:}F".format(temp))
        print("{:.2f}K".format((temp - 32) * 5/9 + 273))
    elif(scale=="K" or scale=="k"):
        print("{:}C".format(temp-273))
        print("{:}F".format((temp - 273) * 9/5 + 32))
        print("{:}K".format(temp))
    
calc(x)