def calculate_bmi(height, weight):
  print("Height = " + str(height))
  print("Weight = " + str(weight))

  bmi = weight/(height*height)

  print("BMI = " + str(bmi))

  if bmi < 18.5:
    print("Under Weight")
    return -1

  elif bmi > 25.0:
    print("Over Weight")
    return 1

  else:
    print("Normal Weight")
    return 0

def main():
  print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
  calculate_bmi(weight=57, height=1.73)

if __name__ == "__main__":
    main()