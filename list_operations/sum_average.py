numlist = list()

while True:
    number = input('Enter number: ')
    if number == 'done':
        break
    numlist.append(float(number))

average =sum(numlist)/len(numlist)

print('Average', average)


