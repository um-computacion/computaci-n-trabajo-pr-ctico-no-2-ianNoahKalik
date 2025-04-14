def is_palindrome(world):
    word = word.lower().replace(" ", "").replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("?", "").replace("!", "")
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

word = input("Ingresa una cadena: ")
resultado = is_palindrome(word)
print(f"¿La cadena es un palíndromo?: {resultado}")