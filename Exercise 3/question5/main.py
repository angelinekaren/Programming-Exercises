def convert_temp():
    global temp_fahrenheit
    temp_fahrenheit = int(input("Enter a temperature in Fahrenheit:"))
    def convert_to_celcius():
        global temp_celcius
        temp_celcius = 5*(temp_fahrenheit-32)/9
        return temp_celcius
    print("The temperature in Fahrenheit is:", temp_fahrenheit)
    print("The temperature in Celcius is:", convert_to_celcius())
    def convert_to_kelvin():
        temp_kelvin = temp_celcius+273.15
        return temp_kelvin
    print("The temperature in Kelvin is:", convert_to_kelvin())

convert_temp()



