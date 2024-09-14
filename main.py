from event_bus import EventBus
from customer import Customer
from notification_service import NotificationService

def main():
    event_bus = EventBus() # Instanciación del bus de eventos

    customer_model = Customer(event_bus) # Instanciación de cliente
    notification_service = NotificationService(event_bus) # # Instanciación del servicio de notificaciones

    # Agregar clientes
    customer_model.add_customer("Óscar", "perro")
    customer_model.add_customer("Santiago", "gato")
    customer_model.add_customer("Juan", "perro")

if __name__ == "__main__": # Main. Punto de entrada del programa
    main()
