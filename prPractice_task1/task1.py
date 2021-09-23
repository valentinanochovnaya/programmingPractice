def find_happy_numbers(num, arr):
    happy_numbers = []
    count = 0
    temp = []
    for i in range(num):
       if (len(temp) != 0):
            happy_numbers.append(int(str(''.join(temp))))
            count = 0
       temp = []
       string_number = str(i)
       for k in range(len(string_number)):
           for n in range(len(arr)):
               if string_number[k] == str(arr[n]):
                   count = count + 1
               else:
                   continue
       if count == len(string_number):
            temp.append(string_number)
       else:
           temp = []
           count = 0
    return happy_numbers


try:
    len_ = int(input("Enter a length of control array "))
    control_array = []
    for i in range(len_):
        el = int(input())
        control_array.append(el)
    number = int(input("Enter a number "))
    result = find_happy_numbers(number, control_array)
    if len(result) == 0:
        print("Happy numbers weren't found")
    else:
        print(result)
except ValueError:
    print("Invalid type was printed")

