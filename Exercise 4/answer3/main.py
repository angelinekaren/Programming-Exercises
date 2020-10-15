import calendar


def main():
    the_year = int(input("Enter the year: "))
    the_month = int(input("Enter the month: "))
    print(calendar.month(the_year, the_month, w=0, l=0))

main()