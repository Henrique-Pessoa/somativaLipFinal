import os

def cpfVerify(x):
    char = ".-"
    while(x.isalpha()):
        x.isalpha()
        print("O cpf não deve conter letra")
        input("mude o cpf: ")
        os.system("cls") or None
    while(len(x) != 11):
            print("O cpf deve conter 11 digitos")
            x = input("mude o cpf: ")
    for z in char:
        x = x.replace(z,"")
    if(len(x) == 11):
        cpf = '{}.{}.{}-{}'.format(x[:3], x[3:6], x[6:9], x[9:])
        return(cpf)

