def get_weather_report(temperature):
    # Complete this function
    if temperature < 22:
        report = "Cold"
    elif (temperature >= 22) and (temperature < 35):
        report = "Warm"
    else:
        report = "Hot"
    return report
        

temperature = int(input())
# Call the get_weather_report function
result = get_weather_report(temperature)
print(result)
