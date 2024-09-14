class Customer: # Este componente se suscribe a un evento que notifica cuando un cliente es agregado
    def __init__(self, event_bus):
        self.customers = [] # Inicializa lista de usuarios
        self.event_bus = event_bus # Instancia el bus de eventos

    def add_customer(self, name, pet_type): # Agrega nuevo cliente y publica evento tipo cliente_agregado
        customer = {'nombre': name, 'tipo_mascota': pet_type} # Diccionario cliente
        self.customers.append(customer) # Agregar cliente
        self.event_bus.publish('cliente_agregado', customer)  # Publica el evento
