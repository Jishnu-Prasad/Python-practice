fhand = open('myfile.txt')

#reading the whole file
# inp = fhand.read()
# print(len(inp))


#count total lines
count = 0
for eachline in fhand:
    count = count + 1
    print(eachline)
print('Total lines',count)

#search through lines
for eachline in fhand:
    eachline = eachline.rstrip()
    if eachline.startswith('C'):
        print(eachline)
