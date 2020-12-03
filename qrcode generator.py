import qrcode
from PIL import Image

permitido = "1 | 2 | 3"
print("Creador de QRS")
print("By: enriquop")
print("1) Texto")
print("2) Instagram")
print("3) Twitter")
Join = input('Selecciona una opcion: ')
if Join == '1':
    value = input("Porfavor pon el texto:\n")
    img = qrcode.make(value)
    guardar = input("Guardar como:\n")
    img.save(guardar + "Texto" + ".png")
    print("Guardado como "+ guardar + "Texto" + ".png")
if Join == '2':  
    value = input("Porfavor pon el nombre de Instagram:\n")
    img = qrcode.make("instagram://user?username=" + value)
    img.save(value  + "Instagram" + ".png")
    print("Guardado como "+ value + "Instagram" + ".png")

if Join == '3':  
    value = input("Porfavor pon el nombre de Twitter:\n")
    img = qrcode.make("twitter://user?screen_name=" + value)
    img.save(value + "Twitter" + ".png")
    print("Guardado como "+ value  + "Twitter" + ".png")

if Join >= '4':
    print("Pon un valor permitido" + " " + "(" + permitido + ")")

if Join <= '0':
    print("Pon un valor permitido" + " " + "(" + permitido + ")")


