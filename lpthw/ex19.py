def cnc(cheese_count, b_of_crackers):
    print(f"you have {cheese_count} cheese.")
    print(f"you have {b_of_crackers} boxes of crackers")

print()
print("we can just give the function arguments directly")
print()
cnc(10,20)
print()
print("or we can use variables from our script.")
cheese = 20
crack = 40
print()
cnc(cheese, crack)
print()
print("and we can combine the two. Variables & math baby")
print()
cnc(cheese + 10, crack + cheese)
