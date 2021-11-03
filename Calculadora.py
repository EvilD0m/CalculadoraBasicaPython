def Calculadora():
    opciones = 0
    while True:
        print(''' 
Calculadora elige que quieres hacer
1: Suma
2: Resta
3: Multiplicacion
4: Division
5: apagar
        ''')
        opciones = int(input('Elige una opcion: '))
        if opciones == 1:
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa otro numero: '))
            resultado = a + b
            print(f'Resultado Suma: {resultado}')
        elif opciones == 2:
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa otro numero: '))
            resultado = a - b
            print(f'Resultado Resta: {resultado}')
        elif opciones == 3:
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa otro numero: '))
            resultado = a * b
            print(f'Resultado Multiplicación: {resultado}')
        elif opciones == 4:
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa otro numero: '))
            resultado = a / b
            print(f'Resultado División: {resultado}')
        elif opciones == 5:
            break
        else:
            print('Elige una opcion correcta')

Calculadora()