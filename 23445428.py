
# Variables y uso de if-elif-else

# Se declara la Variable "moneda" para determinar cual es el tipo de moneda
# luego se usa if-else para que solo se pueda seleccionar los tipos de monedas permitidos.

print("¡Bienvenido al ATM!, Leer cada instrucción para continuar sin ningún tipo de problema")

print("\nPor favor ingresar el tipo de Moneda a solicitar")
print("\n1 Para Bólivares")
print("\n2 Para Dólares")
moneda = int(input())
if moneda == 1 or moneda == 2:
    print("\nResponda lo Siguente")
else:
    print("\n¡Error!: Tipo de moneda no disponible")
    exit()

# la segunda variable declarada es "cuenta", se usa para determinar el tipo de cuenta.
# luego se usa if-else para que solo se pueda seleccionar los tipos de cuentas permitidos.

print("\nPor favor ingresar el tipo de cuenta")
print("\n1 Para Ahorro")
print("\n2 Para Corriente")
cuenta = int(input())
if cuenta == 1 or cuenta == 2:
    print("\nResponda lo Siguiente")
else:
    print("\n¡Error!: Tipo de cuenta no disponible")
    exit()

# Seguimos con la variable "retiro" esta se usa para determinar la cantidad del monto a retirar.
# luego se usa if-elif-else para determinar el limite diario que se puede retirar por el ATM.  

print("\nPor favor ingresar el monto a Retirar")
print("\nSe informa que el limite diario para Bolívares es de 10000 Bs")
print("\nSe informa que el limite diario para Dólares es de 500$")
print("\nRecuerde que los ATM Solo dispensan Billetes con las siguientes denominaciones: 100, 50, 20 y 10")

retiro = int(input())
if moneda == 1 and retiro <= 10000:
    print("\nSu Transacción en Bs se esta procesando")
elif moneda == 2 and retiro <= 500:
    print("\nSu Transacción en $ se esta procesando")
else:
    print("\n¡Transaccion denegana!: Excede limite diario")
    exit()
if retiro % 10 == 0:
    print("\nMonto ingresado valido con las denominaciones disponibles")
else:
    print("\n¡Error: El monto no coincide con las denominaciones disponibles!")
    exit()

# Logica de desglose: Se hace uso del Mod(%) y el Div (//) para calcular la cantidad de billetes que el cajero debe dispensar.

billetes_100 = retiro // 100
resto_1 = retiro % 100
billetes_50 = resto_1 // 50
resto_2 = resto_1 % 50
billetes_20 = resto_2 // 20
resto_3 = resto_2 % 20
billetes_10 = resto_3 // 10
resto_4 = resto_3 % 10

# Variable comision: Se declara la variable comision debido a que si la cuenta es corriente se tiene que agregar una comision extra al debito en la cuenta.
# se le asigna el valor del 5% del monto a retirar.

comision = retiro * 0.05
if cuenta == 1:
    print("\nSe informa que no se Debitará comisión")
else:
    print("\nSe informa que se Debitará un 5%, de comisión al monto a solicitar")

#Salida de datos: Se hace uso del Match-case para determinar cual sera la salida correcta segun el caso dado entre el tipo de moneda y el tipo de cuenta.

match moneda, cuenta:
    case 1, 1:
        print("\nDESGLOSE DE BILLETES Y MONTO TOTAL")
        print(f"Billetes de 100: {billetes_100}")
        print(f"Billetes de 50: {billetes_50}")
        print(f"Billetes de 20: {billetes_20}")
        print(f"Billetes de 10: {billetes_10}")
        print(f"Monto Debitado: {retiro}")
    case 1, 2:
        print("\nDESGLOSE DE BILLETES Y MONTO TOTAL")
        print(f"Billetes de 100: {billetes_100}")
        print(f"Billetes de 50: {billetes_50}")
        print(f"Billetes de 20: {billetes_20}")
        print(f"Billetes de 10: {billetes_10}")
        print(f"Monto Debitado: {retiro + comision}")
    case 2, 1:
        print("\nDESGLOSE DE BILLETES Y MONTO TOTAL")
        print(f"Billetes de 100: {billetes_100}")
        print(f"Billetes de 50: {billetes_50}")
        print(f"Billetes de 20: {billetes_20}")
        print(f"Billetes de 10: {billetes_10}")
        print(f"Monto Debitado: {retiro}")
    case 2, 2:
        print("\nDESGLOSE DE BILLETES Y MONTO TOTAL")
        print(f"Billetes de 100: {billetes_100}")
        print(f"Billetes de 50: {billetes_50}")
        print(f"Billetes de 20: {billetes_20}")
        print(f"Billetes de 10: {billetes_10}")
        print(f"Monto Debitado: {retiro + comision}")
exit("\n¡Gracias por usar nuestro ATM!")
