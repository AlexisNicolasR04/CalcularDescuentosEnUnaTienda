def aplicar_descuento(monto, es_vip):
    """Calcula el total final aplicando descuentos según el monto y el estado VIP."""
    # Aplicar descuento basado en el monto de la compra
    if monto >= 1000:
        descuento = 0.10  # 10% de descuento
    elif monto >= 500:
        descuento = 0.05  # 5% de descuento
    else:
        descuento = 0.00  # Sin descuento

    # Calcular el monto después del descuento por la compra
    total_con_descuento = monto - (monto * descuento)

    # Aplicar descuento adicional del 5% si es VIP
    if es_vip:
        total_con_descuento -= total_con_descuento * 0.05

    return total_con_descuento, descuento

def main():
    print("Bienvenido a la tienda de ropa")
    
    while True:
        # Solicitar el monto total de la compra
        monto_compra = float(input("Ingresa el monto total de la compra: $"))

        # Preguntar si el cliente es miembro VIP
        es_vip_input = input("¿Es cliente VIP? (sí/no): ").lower()
        es_vip = es_vip_input == "sí" or es_vip_input == "si"

        # Calcular el total final con los descuentos aplicados
        total_final, descuento = aplicar_descuento(monto_compra, es_vip)

        # Mostrar detalles del descuento aplicado
        if descuento == 0.10:
            print("Se ha aplicado un descuento del 10% por una compra mayor a $1,000.")
        elif descuento == 0.05:
            print("Se ha aplicado un descuento del 5% por una compra mayor o igual a $500.")
        else:
            print("No se ha aplicado descuento por la compra menor a $500.")

        # Indicar si es VIP
        if es_vip:
            print("Además, se ha aplicado un 5% adicional por ser cliente VIP.")

        # Mostrar el total final a pagar
        print(f"El total final a pagar después de los descuentos es: ${total_final:.2f}")

        # Preguntar si se desea realizar otra operación
        repetir = input("¿Quieres realizar otra compra? (sí/no): ").lower()
        if repetir != "sí" and repetir != "si":
            print("Gracias por usar el sistema de descuentos. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
