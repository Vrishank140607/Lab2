def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")


def get_user_input():
    user_input = input()
    string_list = user_input.split(",")

    float_list = []
    for item in string_list:
        float_list.append(float(item))

    return float_list


def calc_average_temperature(temp_list):
    total = sum(temp_list)
    count = len(temp_list)
    return total / count


def calc_min_max_temperature(temp_list):
    minimum = min(temp_list)
    maximum = max(temp_list)
    return [minimum, maximum]


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

    a = get_user_input()
    b = calc_average_temperature(a)
    c = calc_min_max_temperature(a)

    print("Average:", b)
    print("Minimum:", c[0])
    print("Maximum:", c[1])


# Correct syntax:
if __name__ == "__main__":
    main()
