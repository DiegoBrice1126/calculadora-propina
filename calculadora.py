"""
Calculadora de Propina y División de Cuenta
Integrante: Diego Briceño
Fecha: 15/09/2026 (DD/MM/YYYY)
Buenas Practicas de Desarrollo de Software
"""
 
 
def calcularPropina(montoCuenta, porcentajePropina):
    """Calcula el valor de la propina a partir del monto de la cuenta."""
    if montoCuenta <= 0:
        raise ValueError("El monto de la cuenta debe ser mayor a cero")
    if not (0 <= porcentajePropina <= 100):
        raise ValueError("El porcentaje de propina debe estar entre 0 y 100")
    return montoCuenta * (porcentajePropina / 100)
 
 
if __name__ == "__main__":
    try:
        propina = calcularPropina(80000, 10)
        print(f"Propina calculada: {propina}")
    except ValueError as error:
        print(f"Error: {error}")