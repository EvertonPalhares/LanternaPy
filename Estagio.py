from time import sleep

resp=input("A lanterna está desligada, deseja começar?:").upper()
bateria = 0
while resp=="S":
    lanterna = input("Você deseja ligar a lanterna?: \n" 
                 "<1> ligar\n" 
                 "<2> desligar")
    if lanterna=="1":
        time.sleep(100000)
        bateria = bateria+1
        if bateria>=100:
            print("A bateria acabou, deseja trocar?:")
        if resp=="S":
            print(lanterna)
        elif:
        exit()

    elif lanterna=="2":
        print("Lanterna desligada")
        exit()
