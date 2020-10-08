def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    print("The number of days is: ", get_days(hours,  minutes, seconds))
    return get_days(hours, minutes, seconds)
def get_days(hours, minutes, seconds):
    number_of_days = float(((seconds/3600)+(minutes/60)+hours)/24)
    return round(number_of_days, 4)
convert_to_days()



