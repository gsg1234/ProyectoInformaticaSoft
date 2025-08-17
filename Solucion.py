import threading
import time
from BotonYLuces import PanelLuces

panel = PanelLuces()

########Espaciio para definir subprogramas##########



####################################################

def control_luces_externo():
    while panel.running:
        ########bucle principal##########
        time.sleep(0.001)

hilo_externo = threading.Thread(target=control_luces_externo, daemon=True)
hilo_externo.start()

panel.run()
