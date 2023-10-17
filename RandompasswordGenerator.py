import time
import random
print("welcome to the random password gerator in line 21-22 you can chance the lenght and amount default is 20,10 in line 10 you can chance whether numbers symbols etc. can be included ")
time.sleep(5)
uppercase_letters = "JHSTAGDWDVGEVCFFGVS"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

lenght = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)
#its not my code i have it from yt (NeutralNine) but i chanced some things
input("")