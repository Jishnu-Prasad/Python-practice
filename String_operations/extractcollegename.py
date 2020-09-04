data ="From jishnu.prasad@viit.pune sat jan 5"

spos = data.find('@')
epos = data.find(' ', spos)

college = data[spos+1 : epos]
print(college)