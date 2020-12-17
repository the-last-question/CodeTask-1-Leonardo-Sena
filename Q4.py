def palin(word):  return word == word[::-1]

def main():
    word = input("Entrada: ")
    print(word + " É um palindromo") if(palin(word)) else print(word + " Não é um palindromo")
        
if __name__ == "__main__": main()