rooms = {1: "Работа", 2: "Хобби"}

input_room_message = "Выберите номер комнаты:\n"
input_room_message += "".join([f"{id} - {name}\n" for id, name in rooms.items()])
