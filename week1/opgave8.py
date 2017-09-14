def opgave8():
    running = True
    while running:
        try:

            T =(input("Wat is de temperatuur"))
            B = (input("wat is de windsnelheid?"))
            G = 13 + 0.62 * int(T) - 14 * int(B) ** 0.24 + 0.47 * int(T) * int(B) ** 0.24
            print(G)
            running = False

        except Exception as e:
            print(e, ' ' , "input moeten int type zijn")

opgave8()
