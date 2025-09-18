def convert(things):
    things.replace(":)", "🙂")
    things.replace(":(", "🙁")
    return things

def main():
    x=input("enter text")
    converted=convert(x)
    print(converted)
main()
