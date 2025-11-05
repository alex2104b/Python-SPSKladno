#na druhý řádek začněte vypracovávat desetiminutovku
věk = int(input("zadejte svůj věk:"))
stat = input("Jsi občan ČR:  (Ano/Ne)")

if věk >= 18 and stat == "Ano":
    podmínka = "můžeš volit"
else:
    podmínka = "nemůžes volit"

print(podmínka)