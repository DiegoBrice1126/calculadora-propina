"""
Calculadora de Propina y División de Cuenta
Integrante: Diego Briceño
Fecha: 15/09/2026 (DD/MM/YYYY)
Buenas Practicas de Desarrollo de Software
"""
 
 
def calcularPropina(montoCuenta, porcentajePropina):
    #Calcula el valor de la propina a partir del monto de la cuenta.
    if montoCuenta <= 0:
        raise ValueError("El monto de la cuenta debe ser mayor a cero")
    if not (0 <= porcentajePropina <= 100):
        raise ValueError("El porcentaje de propina debe estar entre 0 y 100")
    return montoCuenta * (porcentajePropina / 100)
 
def dividirCuenta(montoTotal, numeroPersonas):
    #Divide el monto total en partes iguales entre las personas.
    if numeroPersonas < 1:
        raise ValueError("El número de personas debe ser al menos 1")
    return montoTotal / numeroPersonas
 
 
def mostrarResumen(montoCuenta, porcentaje_propina, numeroPersonas):
    #Muestra el resumen completo: cuenta, propina, total y valor por persona.
    propina = calcularPropina(montoCuenta, porcentaje_propina)
    total = montoCuenta + propina
    por_persona = dividirCuenta(total, numeroPersonas)
    print(f"Cuenta: {montoCuenta}")
    print(f"Propina ({porcentaje_propina}%): {propina}")
    print(f"Total: {total}")
    print(f"Valor por persona ({numeroPersonas}): {por_persona:.2f}")
 
 
if __name__ == "__main__":
    try:
        mostrarResumen(80000, 10, 4)
    except ValueError as error:
        print(f"Error: {error}")