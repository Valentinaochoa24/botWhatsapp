import pyautogui as pt
import time

message = input("Mensaje: ")
limit = input("Cantidad de mensajes: ")

i = 0

time.sleep(3)

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")
    time.sleep(0.5)  # Pausa de 0.5 segundos antes de enviar el siguiente mensaje
    i += 1
