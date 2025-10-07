import random
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

# TODO: Use a while loop to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i = i+1
# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)


# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# Générer un nombre aléatoire entre 1 et 10
nombre_secret = random.randint(1, 10)
# Initialiser la variable de l'utilisateur
guess = None
print(" Bienvenue dans le jeu de devinette !")
print("Devine le nombre (entre 1 et 10) :")

# Tant que la réponse est incorrecte
while guess != nombre_secret:
    # Demander à l'utilisateur de deviner
    guess = int(input("Entre ton nombre : "))

    # Vérifier la réponse
    if guess < nombre_secret:
        print("Trop petit , essaie encore !")
    elif guess > nombre_secret:
        print("Trop grand , réessaie !")
    else:
        print(" Bravo ! Tu as trouvé le nombre :", nombre_secret)

# TODO: Use a while loop to calculate the factorial of a number
n = 5
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("Le factoriel de", n, "est :", fact)

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)
# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)

while True:
    op = input("Choisis une opération (+, -, *, /) ou 0 pour quitter : ")

    if op == "0":
        print(" Fin du programme bye.")
        break  # on sort de la boucle

    n1 = float(input("Donne le 1er nombre : "))
    n2 = float(input("Donne le 2eme nombre : "))

    if op == "+":
        print("Résultat pour addition:", n1 + n2)
    elif op == "-":
        print("Résultat pour soustraction :", n1 - n2)
    elif op == "*":
        print("Résultat pour multiplication :", n1 * n2)
    elif op == "/":
        if n2 != 0:
            print("Résultat pour division :", n1 / n2)
        else:
            print(" Erreur : division par zéro impossible.")
    else:
        print(" Opération invalide, réessaie.")

# TODO: Create a function that counts the occurrence of each vowel in a string
def count_vowel(mot):
    vowel = "aeiuo"
    cpt = {"a": 0, "e": 0, "i": 0, "u": 0, "o": 0}
    mot = mot.lower()
    for char in mot:
        if char in vowel:
            cpt[char] += 1
            
    print(cpt)  
mot = input("donne un mot : ")
count_vowel(mot)
# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome


# Test each function with sample inputs and print the results

