# Informática y programación: Proyecto final de Software

Para el proyecto de la materia con software, se utiliza una interfaz en pygame que simula el entorno del proyecto con arduino. El objetivo es que los estudiantes puedan realizar el proyecto de manera sencilla y didactica, si no se disponen de materiales de hardware.

Las consignas se encuentran el el aula virtual, les deseo suerte con el codigo :)

Para lograrlo, se implemento una clase panel, que tiene un método y un atributo que permiten manejar el panel de manera adecuada y se explica mas abajo:

`PanelLuces` es una clase en Python que implementa un panel gráfico con **tres luces indicadoras** (roja, amarilla y verde) y un **botón interactivo** usando Pygame.  
El objetivo es que otros scripts o hilos puedan **consultar el estado del botón** y **controlar las luces** de manera sencilla, manteniendo la interfaz funcional y responsiva.

---

## Características

- Interfaz gráfica en Pygame con tres luces y un botón.
- Control de luces mediante funciones externas.
- Consulta del estado del botón con un simple booleano.
- Funciona en el hilo principal de Pygame, evitando que la ventana se congele.
- Fácil de integrar en otros scripts o hilos de Python.

---

## Funciones

- panel.encender_luz("color",booleano)
    EJEMPLO: panel.encender_luz("verde",True)
        Resultado: Enciende la luz verde
    EJEMPLO: panel.encender_luz("roja",False)
        Resultado: Apaga la luz roja

- button_pressed devuelve un booleano del estado del boton:
    si el botón esta presionado, button_pressed = True
    si el botón NO esta presionado, button_pressed = False



