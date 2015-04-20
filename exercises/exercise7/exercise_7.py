import tempconvert


def main():
    unit = ""
    other_unit = ""
    original_temp = 0.0
    converted_temp = 0.0
    city_temps = {"Boston": "0 C", "Boise": "48 F", "Phoenix": "85 F", "Miami": "40 C", "Riverside": "30 C",
                  "Baltimore": "32 F"}
    for city, temp in city_temps.items():
        u = temp.split()[1].lower()
        original_temp = float(temp.split()[0])
        if u == 'c':
            unit = "Celsius"
            other_unit = "Fahrenheit"
            converted_temp = tempconvert.c2f(original_temp)
            print("In %s it is %s degrees %s, which is equivalent to %s degrees %s." %
                  (city, original_temp, unit, converted_temp, other_unit))
        elif u == 'f':
            unit = "Fahrenheit"
            other_unit = "Celsius"
            converted_temp = tempconvert.f2c(original_temp)
            print("In %s it is %s degrees %s, which is equivalent to %s degrees %s." %
                  (city, original_temp, unit, converted_temp, other_unit))
        else:
            print("Something went wrong...")


if __name__ == "__main__":
    main()
