import arth_temperature.temperature as temperature

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round(temperature.celsius_to_fahrenheit(degree)))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round(temperature.fahrenheit_to_celsius(degree)))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
