def foodtime():
    time_str = (input("What time is it?"))
    hours = (convert(time_str))
    if (hours) >= (7):
        if (hours) <= (8):
                print ("breakfast time")
    if (hours) >= (12):
        if (hours) <= (13):
                print ("lunch time")
    if (hours) >= (18):
        if (hours) <= (19):
                print ("dinner time")
def convert(time_str):
    time_list = time_str.split(":")
    hours_str, minutes_str = time_list
    return float(hours_str) + float(minutes_str)/60

foodtime()


