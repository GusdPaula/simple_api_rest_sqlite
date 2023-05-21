TOKEN = 'Bearer '

with open ('token.txt', 'r') as file:
    TOKEN += file.read()
