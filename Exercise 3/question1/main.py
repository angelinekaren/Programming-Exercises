def get_days(hours, minutes, seconds):
    number_of_days = float(((seconds/3600)+(minutes/60)+hours)/24)
    return number_of_days
def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    print("")
    print("The number of days is: ", round(get_days(hours,  minutes, seconds), 4))
convert_to_days()



