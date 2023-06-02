from pick import pick
from cpfVerify import cpfVerify
from nameVerify import nameVerify
import os
import time
from random import sample
from price import value
numeros = []
sorteados = []
sorteados2 = []
chances = 0

for x in range(1,61):
    numeros.append(x)

nome = input("Coloque o seu nome: ").lower()

nameVerify(nome)



cpf = input("Coloque um cpf valido, exemplo:(12345678900)")

cpf = cpfVerify(cpf)


title = 'Deseja jogar a surpresinha?'
options = numeros
selected = pick(["Sim","Não"], title)

if(selected[0] == "Não"):
    title = 'Quantos volantes deseja jogar?'
    options = numeros
    selected = pick([1,2], title)
    for x in selected:
        volante = selected[0]
        x == False
    if(volante == 1):
        title = 'Escolha no minimo  6 numeros'
        options = numeros
        escolhidos = pick(options, title, multiselect=True, min_selection_count=6)
        volante = volante -1
        for x in escolhidos:
            sorteados.append(x[0])
        while(len(sorteados) > 15):
            sorteados = []
            chances+=1
            os.system("cls") or None
            print("Error, deve ser escolhido no maximo 15 valores")
            time.sleep(4)
            title = 'Escolha no minimo  6 numeros'
            options = numeros
            escolhidos = pick(options, title, multiselect=True, min_selection_count=6)
            os.system("cls")
            for x in escolhidos:
                sorteados.append(x[0])
            if(chances == 3):
                print("acabou as suas chances")
                exit()
    else:
        while(volante != 0):
            volante -=1
            title = 'Escolha no minimo  6 numeros'
            options = numeros
            selected = pick(options, title, multiselect=True, min_selection_count=6)
            if volante == 1:
                for x in selected:
                    sorteados.append(x[0])
            else:
                for x in selected:
                    sorteados2.append(x[0])
            while(len(sorteados2) > 15 or len(sorteados) > 15):
                sorteados2 = []
                sorteados = []
                selected = []
                time.sleep(6)
                chances+=1
                print("Error, deve ser escolhido no maximo 15 valores")
                time.sleep(4)
                title = 'Escolha no minimo  6 numeros'
                options = numeros
                escolhidos = pick(options, title, multiselect=True, min_selection_count=6)
                os.system("cls")
                if volante == 1:
                    for x in selected:
                        sorteados.append(x[0])
                        print(len(sorteados))
                else:
                    for x in selected:
                        sorteados2.append(x[0])
                        print(len(sorteados2))

                if(chances == 3):
                    print("acabou as suas chances")
                    exit()
else:
    title = 'Escolha a quantidade de valores que você deseja jogar'
    options = numeros
    selected = pick([6,7,8,9,10,11,12,13,14,15], title)
    sorteados = sample(range(1, 61),selected[0])



if(len(sorteados2) > 0 ):
    for x in sorteados:
        if x in numeros:
            numeros[numeros.index(x)] = "XXX"
    os.system("cls") or None
    print(nome.title())
    print(f"cpf: {cpf}")
    print("Primeiro volante :")
    print(numeros[0:10])
    print(numeros[10:20])
    print(numeros[20:30])
    print(numeros[30:40])
    print(numeros[40:50])
    print(numeros[50:60])
    time.sleep(4)
    os.system("cls") or None
    for x in sorteados2:
        if x in numeros:
            numeros[numeros.index(x)] = "XXX"
    os.system("cls") or None
    print(nome.title())
    print(f"cpf: {cpf}")
    print(f"Você deve pagar: ${value(sorteados2) + value(sorteados)}")
    print("Segundo volante: ")
    print(numeros[0:10])
    print(numeros[10:20])
    print(numeros[20:30])
    print(numeros[30:40])
    print(numeros[40:50])
    print(numeros[50:60])

else:
    for x in sorteados:
        if x in numeros:
            numeros[numeros.index(x)] = "XXX"
    os.system("cls") or None
    print(nome.title())
    print(f"cpf: {cpf}")
    print(f"Você deve pagar: $ {value(sorteados)}")
    print(numeros[0:10])
    print(numeros[10:20])
    print(numeros[20:30])
    print(numeros[30:40])
    print(numeros[40:50])
    print(numeros[50:60])


