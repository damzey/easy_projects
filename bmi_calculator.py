import time
def delay():
    delay = time.sleep(1)

print('Welcome to a BMI calculator.')
print()

delay()
weight = int(input('Enter your weight in kilograms: '))
height = int(input('Enter your height in centimetres: '))

BMI = weight/ ((height/100) ** 2)
print()
rounded_BMI = round(BMI, 1)
print(rounded_BMI)
print()

while rounded_BMI <=0:
    weight = int(input('Enter your weight in kilograms: '))
    height = int(input('Enter your height in centimetres: '))
delay()
if  rounded_BMI <= 18.4:
    print('You are underweight')
    print('Your health risk is minimal')
elif rounded_BMI <= 25:
    print('You are healthy')
    print('Your health risk is minimal')
elif rounded_BMI <= 29.9:
    print('You are overweight')
    print('Your health risk is increased')
elif rounded_BMI <= 34.9:
    print('You are obse')
    print('Your health risk is high ')
elif rounded_BMI <= 39.9:
    print('You are severly obese')
    print('Your healthhealth risk is very high')
else:
    print('You are over-morbidly obese')

