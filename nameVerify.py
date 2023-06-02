def nameVerify(x):
    import os
    y = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    validation = set((x))
    x.strip()
    while(validation.issubset(y) == False):
        print("Erro, verifique a ortografia!")
        x = input("Coloque o seu nome completo!")
        validation = set((x))
        x.strip()
        os.system("cls") or None