# 01 #

idade = int(input("Digite sua idade "))

if idade < 16:
    print("MENOR")
elif 16 <= idade <= 18:
    print("EMANCIPADO")  
elif idade > 18:
    print("MAIOR")    

# 02 #

idade = int(input("Digite a idade do nadador "))

if 5 <= idade <= 7:
    print("Classe Infantil A")
elif 8 <= idade <= 10:
    print("Classe Infantil B")
elif 11 <= idade <= 13:
    print("Classe Juvenil A")
elif 14 <= idade <= 17:
    print("Classe Juvenil B")
