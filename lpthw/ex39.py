"""Dictionaries."""

# create a mapping of states to abbrevation.
states = {
    'Lagos': 'LAG',
    'Kaduna': 'KAD',
    'Abuja': 'ABJ',
    'Ibadan': 'IB',
    'Calabar': 'CAL'
}

# create a basic set of states with cities in them.
cities = {
    'LAG': 'Yaba',
    'ABJ': 'Wuse',
    'KAD': 'Lamba'
}

# add some more cities.
cities['IB'] = 'Lokomba'
cities['CAL'] = 'Canibal'

# print out some cities.
print('-'* 10)
print("Lagos's abbrevation is: ", states['Lagos'])
print("Abuja's abbrevation is: ", states['Abuja'])

# do it using the states then cities dictionary
print("-"* 10)
print("Lagos has: ", cities[states['Lagos']])
print("Abuja has: ", cities[states['Abuja']])

# print every state abbrevation.
print('-'* 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbrevated {abbrev}")

# print every city in state.
print("-"* 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} state has {city} city.")

# print both at the same time.
print("-"* 10)
for stat, abbre in list(states.items()):
    print(f"{stat} is abbrevated {abbre}")
    print(f"and  has {cities[abbre]} city.")

# safely print abbrevation for a state that might not be there.
state = states.get('Cala')

if not state:
    print(f"Sorry, not on dictionary")

# get a city with a default value.
city = cities.get('TX', 'Does not exist.')
print(f"The city for the state 'TX': {city}.")
