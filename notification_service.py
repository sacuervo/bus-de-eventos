class NotificationService:
    def __init__(self, event_bus):
        event_bus.subscribe('cliente_agregado', self.send_welcome_message) # Suscripción al evento cliente agregado por medio de método de bus de eventos

    def send_welcome_message(self, customer):
        print(f"Bienvenidos {customer['nombre']} y {customer['tipo_mascota']}!") # Envía mensaje de bienvenida cada vez que se agrega un cliente
