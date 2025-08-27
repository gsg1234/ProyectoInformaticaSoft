import threading
import time
from BotonYLuces import PanelLuces

panel = PanelLuces()

########Espaciio para definir subprogramas##########



####################################################

def control_luces_externo():
    while panel.running:
        ########bucle principal##########
        if panel.button_pressed:
            panel.encender_luz("verde",True)
        else:
            panel.encender_luz("verde",False)
        time.sleep(0.001)

def control_luces_2():
    while panel.running:
        panel.encender_luz("roja",True)
        time.sleep(1)
        panel.encender_luz("roja",False)
        time.sleep(1)

hilo_externo = threading.Thread(target=control_luces_externo, daemon=True)
hilo_externo2 = threading.Thread(target=control_luces_2, daemon=True)
hilo_externo.start()
hilo_externo2.start()

panel.run()
