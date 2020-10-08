def convert_to_days():
    global hours, minutes, seconds
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    print("The number of days is: ", round(get_days(), 4))
    return get_days()
def get_days():
    number_of_days = float(((seconds/3600)+(minutes/60)+hours)/24)
    return number_of_days
convert_to_days()



