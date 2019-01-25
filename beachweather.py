
def beachweather(temperature,precipitation,forecast):
    answer = "no"
    if (len(temperature) > 0 and len(precipitation) > 0 and len(forecast) > 0):
        try:
            temperature = float(temperature[:-1])
            precipitation = float(precipitation[:-1])
            if (temperature >= 21 and (precipitation < 5 or "sun".upper() in forecast.upper())):
                answer = "yes"
        except ValueError:
            answer = "no"
    return answer
