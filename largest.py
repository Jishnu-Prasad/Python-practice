largest_so_far = None

for num in [9,41,12,3,74,15,110]:
    if largest_so_far is None or num > largest_so_far:
        largest_so_far = num
print("Largest Number is", largest_so_far )


