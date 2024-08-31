# BMI CALCULATOR
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

# bmi is equal to the person's weight divided by the person's height squared.

height =input('Enter your height in meter ')
weight =input('Enter your weight in kg ')

# ONE IMPORTAONT THINGS NOTICE THAT INPUT ALWAYS RETURN STRING

BMI =float(float(weight)/(float(height)**2))
print(BMI)