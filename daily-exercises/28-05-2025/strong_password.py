from random import choice 

length = int(input("TAMANHO DA SENHA: "))

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÇç/;,.<>:?[]{}!@#$%¨&*()_+-=§£¢¬\\|'

def strong_password(length):
    return ''.join(choice(chars) for _ in range(length))

print(strong_password(length))