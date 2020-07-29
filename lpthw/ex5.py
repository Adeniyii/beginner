print()

my_name = "Ekardoo"
my_age = 25  # pumping
my_height = 80  # inches
my_weight = 150  # pounds
my_eyes = "Brown"  # sometimes black
my_teeth = "White"  # sometimes
my_hair = "Brown"  # Also sometimes black

# (f"") -- This is called an f-string and is a method of formatting strings.

print(f"let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the kush.")

# This line is tricky, let's try to get it right
total = my_height + my_weight + my_age
print(f"if i add {my_height} + {my_weight} + {my_age}, i get {total}.")
print()

pounds_to_lbs = round(40/20.4)
print(f"Conversion rate for pound to lbs is {pounds_to_lbs}.")

weight_lbs = my_weight * pounds_to_lbs

print(f"my weight in pounds is {my_weight} and {pounds_to_lbs} * {my_weight} = {weight_lbs} in lbs.")
#  All done shir
