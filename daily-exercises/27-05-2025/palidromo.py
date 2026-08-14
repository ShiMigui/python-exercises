def is_palindromo(frase):
    frase = frase.lower()  
    frase = ''.join(c for c in frase if c.isalnum())  
    return frase == frase[::-1]  

print(is_palindromo("A man, a plan, a canal: Panama"))
print(is_palindromo("Olá mundo"))
