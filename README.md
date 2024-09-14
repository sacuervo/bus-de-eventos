# Bus de eventos - Guardería de mascotas
- Muestra implementación del patrón de bus de eventos mediante la notificación de un evento de creación de cliente a otros clientes suscritos

## `event_bus.py`

### Constructor
- Contiene una lista de suscriptores para cada evento

### `subscribe()`
- Permite que clientes se suscriban a un tipo de evento específico

### `publish()`
- Publica evento notificando a todos los suscriptores registrados


## `customer.py`
- Este componente en su totalidad se suscrribe a un evento específico con intermediación del bus de eventos

### Constructor
- Inicializa instancia del componente con una lista de usuarios y una instanciación del bus de eventos

### `add_customer()`
- Agrega nuevo cliente y publica evento tipo "cliente_agregado"

## `notification_service.py`

### Constructor
- Inicializa la instancia con una suscripción y al evento y el envío de un mensaje de notificación

### send_welcome_message()
- Envía mensaje de bienvenida cada vez que se agrega un cliente