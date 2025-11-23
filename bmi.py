def calculate_bmi(height, weight):
    print("Height =", height)
    print("Weight =", weight)

    # Calculate BMI
    bmi = weight / (height * height)

    # Display calculated BMI
    print("BMI =", bmi)

    # Determine weight classification
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
    elif bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    else:
        print("Weight Classification: Over Weight")


# Test the function
calculate_bmi(weight=57, height=1.73)


