class EventBus:
    def __init__(self):
        self.subscribers = {} # Diccionario que contiene lista de suscriptores para cada evento

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers: # Permite que clientes se suscriban a un tipo de evento específico
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type, data):
        if event_type in self.subscribers: # Publica evento llamando a todos los suscriptores registrados
            for callback in self.subscribers[event_type]:
                callback(data)
