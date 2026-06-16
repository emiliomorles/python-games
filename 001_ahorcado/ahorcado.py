import random

# Dibujos del ahorcado
dibujos = [
    """
      +---+
      |   |
          |
          |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========= """
]

def jugar_ahorcado():
    palabras = ["python", "computadora", "ahorcado", "programacion", "desarrollador", 
                "teclado", "monitor", "internet", "celular", "elefante", "jirafa", 
                "dinosaurio", "ventana", "tecnologia"]

    palabra = random.choice(palabras).upper()
    letras_adivinadas = set()
    vidas = 6
    
    print("¡Bienvenido al juego del Ahorcado!")
    print("Tienes 6 vidas. ¡Buena suerte!\n")
    
    while vidas > 0:
        # Mostrar la palabra
        palabra_mostrada = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
        
        print("\n" + "="*50)
        print(dibujos[6 - vidas])
        print(f"Palabra: {palabra_mostrada}")
        print(f"Vidas restantes: {vidas}")
        
        # Pedir letra
        letra = input("\nIngresa una letra: ").upper().strip()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa solo una letra.")
            continue
            
        if letra in letras_adivinadas:
            print("Ya habías usado esa letra.")
            continue
            
        letras_adivinadas.add(letra)
        
        # === CHEQUEO DE VICTORIA DESPUÉS DE INGRESAR LA LETRA ===
        if set(palabra) == letras_adivinadas:
            print("\n" + "="*50)
            print("🎉 ¡FELICIDADES! ¡GANASTE! 🎉")
            print(f"La palabra era: {palabra}")
            return
        
        if letra not in palabra:
            vidas -= 1
            print(f"¡La letra '{letra}' no está en la palabra!")
    
    # Si llega aquí es porque perdió
    print("\n" + "="*50)
    print(dibujos[6])
    print(f"¡Perdiste! La palabra era: {palabra}")

# Iniciar el juego
jugar_ahorcado()