import csv

def validator(number):
    num_list = list(number)
    num_list = [int(num) for num in num_list]
    poped_element = num_list.pop()
    num_list.reverse()
    for i in range(len(num_list)):
        if i%2 == 0:
            num_list[i] = num_list[i] * 2
            if num_list[i] > 9:
                num_list[i] = num_list[i] - 9
        else:
            num_list[i] = num_list[i]
    total = sum(num_list) + poped_element
    if total%10==0:
        status = "Valid, Total is {0}".format(total)
    else:
        status = "Invalid, Total is {0}".format(total)
    return status

if __name__ == "__main__":
    with open("samples.csv") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            print(validator(row[0]))
