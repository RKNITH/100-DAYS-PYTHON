


# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"


height =float(input('eneter your height in meter '))
weight =float(input('enetr your weight in kg '))

BMI = weight/(height ** 2)

if BMI < 18.5:
    print(f'Your Bmi is {BMI}, you are underweight')
elif BMI <25:
    print(f'Your Bmi is {BMI}, you are normal')

else:
    print(f'Your Bmi is {BMI}, you are overweight')






