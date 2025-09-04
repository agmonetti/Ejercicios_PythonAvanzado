while True:
    try:
        for i in range(1,100000):
            print(i,end=" ")

    except KeyboardInterrupt:
        print("")
        print("Has presionado para detener el programa")
        a=input("Es lo que quieres haces? (s/n): ")
        if a == "n":
            pass
        else:
            break
        