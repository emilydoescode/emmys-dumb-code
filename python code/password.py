import random
import string

s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("How many characters do you want in your password? ")

while True:
    try:
        character_number = int(user_input)

        if character_number < 8:
            print("EIGHT CHARACTERS IS THE MINIMUM")
            user_input = input("Input your number, now BIGGER than eight")

        else:
            break

    except:
        print("Please, Enter numbers only.")
 
        user_input = input("How many characters do you want in your password? ")
 
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
 
part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))
 
 
result = []
 
for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
random.shuffle(result)
 

password = "".join(result)
print("Strong Password: ", password)