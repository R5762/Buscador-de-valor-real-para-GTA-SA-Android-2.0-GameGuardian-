print("Buscador de valor real para GTA: SA Android v2...");
print("Atención: Uso exclusivo para la versión 2.0.")

Entero = int(7024640)
Hexadecimal = input("Ingresa el valor hexadecimal que te arrojó GameGuardian aquí: ").strip()

try:
    Hexadecimal_variable = int(Hexadecimal, 16)
except ValueError:
    print("El valor ingresado no es un hexadecimal válido.")
    exit()

Resultado = Entero + Hexadecimal_variable

if Resultado < 0:
    Resultado_hex = "+" + hex(abs(Resultado))[2:]
else:
    Resultado_hex = hex(Resultado)

print(f"Resultado en hexadecimal: {Resultado_hex}")
