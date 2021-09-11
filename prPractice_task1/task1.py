def find_happy_numbers(num):
    happy_numbers = []
    temp = []
    for i in range(num):
        string_number = str(i)
        if len(temp) != 0:
            happy_numbers.append(int(''.join(temp)))
        for k in range(len(string_number)):
            if string_number[k] == '7' or string_number[k] == '4':
                temp.append(string_number[k])
                continue
            else:
                temp = []
                break
    return happy_numbers


try:
    number = int(input("Enter a number "))
    result = find_happy_numbers(number)
    if len(result) == 0:
        print("Happy numbers weren't found")
    else:
        print(result)
except ValueError:
    print("Invalid type was printed")

