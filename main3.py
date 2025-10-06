print("------------------ MODULE 3 -------------------------------- \n")
print("------------------ Exercice 1 -------------------------------- \n")
# TODO: Create a string variable with a sentence
phrase = "Je fais mon demenagement today"
print(phrase)
# TODO: Convert the string to uppercase
print("Masjucule ->", phrase.upper())
# TODO: Convert the string to lowercase
print("Minuscule ->", phrase.lower())
# TODO: Capitalize the first letter of each word
print("Capitalize ->", phrase.title())
# TODO: Replace a word in the string
new_phrase = phrase.replace("today", "aujourd'hui")
print("Avant : ", phrase)
print("Apres :", new_phrase)
# TODO: Split the string into a list of words
split_phrase = phrase.split()
print(split_phrase)

# TODO: Join the list of words back into a string using a different separator
join_phrase = " ".join(split_phrase)
print(join_phrase)

# TODO: Find the position of a specific word in the string
indexMot = join_phrase.rindex("fais")
print(indexMot)
# TODO: Check if the string starts with a specific word
mot = "today"
if phrase.index(mot) == 0:
    print(" oui La phrase commence par", mot)
else:
    print(" NON La phrase ne commence pas par", mot)

# TODO: Remove leading and trailing whitespace from a string
iphrase = "  Je......fais...vuf....mon/demenagement..today  "
remove_Wspace = iphrase.strip(".vuf/")
print("Avant -> ", iphrase)
print("apres -> ", remove_Wspace)

# Print the results of each operation
print(" \n------------------ End 1 -------------------------------- \n")

print("------------------ Exercice 2 -------------------------------- \n")
# TODO: Create variables for name, age, and height
name = "Ali"
age = 25
height = 183


# TODO: Use the .format() method to create a sentence with these variables
sentence = "Je m'appelle {}, j'ai {} ans et je mesure {} cm.".format(name, age, height)

print("option 1 avec format->", sentence)
# TODO: Use f-strings to create the same sentence
sentence2 = f"Je m'appelle {name}, j'ai {age} ans et je mesure {height} cm."
print("option 2-> avec f", sentence2)
# TODO: Use the % operator for string formatting
sentence3 = "Je m'appelle %s, j'ai %d ans et je mesure %d cm." % (name, age, height)
print("option 3-> avec %", sentence3)


# TODO: Format a float number to display only two decimal places

# TODO: Create a table-like output using string formatting

# Print all formatted strings
print("\n------------------- End 2 ------------------------------------- \n")

# TODO: Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

# TODO: Use a for loop to print each number in the list
for x in numbers:
    print(x)

# TODO: Use a for loop with enumerate() to print both index and value
fruits = ["pomme", "banane", "orange"]

# TODO: Use a for loop with enumerate() to print both index and value
for index, fruit in enumerate(fruits):
    print("Index:", index, "-> Fruit:", fruit)


# TODO: Create a dictionary and use a for loop to print all keys and values
personne = {"nom": "Ali", "âge": 25, "ville": "Toulouse"}

for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")

# TODO: Use a for loop with range() to print numbers from 1 to 10

# TODO: Use a for loop with range() to print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# TODO: Use a nested for loop to create a multiplication table (up to 5x5)
# TODO: Use a nested for loop to create a multiplication table (up to 5x5)
for i in range(1, 6):           # ligne (1 à 5)
    for j in range(1, 6):       # colonne (1 à 5)
        print(f"{i} x {j} = {i * j}")
    print("------")             # séparation entre chaque table
