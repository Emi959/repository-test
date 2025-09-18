x= float(input ("what's x?"))
y= float(input ("what's y?"))

z= (x/y, 2)

print(f"{z:.2f}")

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n **2
