import datetime, random

def getBirthdays(num_of_birthdays):
    birthdays = []
    
    for i in range(num_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        
        random_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_days
        birthdays.append(birthday)
        
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique
    
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a   # Return matching birthday
            
# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
        "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    response = input("How many birthdays shall I generate? (MAX 100)\n> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        number_birthdays = int(response)
        break
    
print()

# Generate and display the birthdays
print(f"Here are {number_birthdays} birthdays:")
birthdays = getBirthdays(number_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    month_name = MONTHS[birthday.month - 1]
    date_text = f"{month_name} {birthday.day}"
    print(date_text, end=" ")
    
print("\n\n")

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display results
print("In this simulation, ", end=" ")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print("multiple people have a birthday on", date_text)
else:
    print("there are no matching birthdays.\n")
    
# Run through simulations
print(f"Generating {number_birthdays} random birthdays 100,000 times...")
input("Press ENTER to begin...")

print("Let\'s run another 100,000 simulations.")
sim_match = 0
for i in range(100000):
    if i % 10000 == 0:
        print(f"{i} simulations run")
    birthdays = getBirthdays(number_birthdays)
    
    if getMatch(birthdays) != None:
        sim_match += 1
        
print("100,000 simulations run.")

# Display simulation results
probability = round(sim_match / 100000 * 100, 2)
print(f"""Out of 100,000 simulations of {number_birthdays} people, there was a
matching birthday in that group {sim_match} times. This means
that {number_birthdays} people have a {probability}% chance of
having a matching birthday in their group.""")
print("That\'s probably more than you would think!")