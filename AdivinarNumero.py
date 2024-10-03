import pygame
import random

pygame.init()

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 255)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina el Número")
fuente = pygame.font.Font(None, 48)
fuente_ganador = pygame.font.Font(None, 72)

controles = {
    "Jugar": pygame.K_RETURN,
    "Salir": pygame.K_ESCAPE,
    "Pausa": pygame.K_ESCAPE,
}


def dibujar_texto(texto, x, y, color=BLANCO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)


def dibujar_caja_entrada(x, y, texto):
    pygame.draw.rect(pantalla, BLANCO, (x - 100, y - 20, 200, 40), 2)
    dibujar_texto(texto, x, y)


def menu_principal():
    fuente = pygame.font.Font(None, 74)
    fuente_pequeña = pygame.font.Font(None, 36)
    seleccion = 0
    opciones = ["Jugar", "Controles", "Salir"]
    while True:
        pantalla.fill(NEGRO)
        texto_titulo = fuente.render("Adivina el Número", True, BLANCO)
        pantalla.blit(
            texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4)
        )
        for i, opcion in enumerate(opciones):
            color = BLANCO if i == seleccion else (150, 150, 150)
            texto_opcion = fuente_pequeña.render(opcion, True, color)
            pantalla.blit(
                texto_opcion,
                (ANCHO // 2 - texto_opcion.get_width() // 2, ALTO // 2 + i * 50),
            )
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                if evento.key == pygame.K_RETURN:
                    if seleccion == 0:
                        return True
                    elif seleccion == 1:
                        menu_controles()
                    elif seleccion == 2:
                        pygame.quit()
                        return
        pygame.display.flip()


def menu_controles():
    fuente = pygame.font.Font(None, 36)
    fuente_Titulo = pygame.font.Font(None, 46)
    fuente_instrucciones = pygame.font.Font(None, 26)
    controles_orden = ["Jugar", "Salir", "Pausa"]
    seleccion = 0
    esperando_tecla = False
    gris_claro = (200, 200, 200)
    while True:
        pantalla.fill(NEGRO)
        texto_titulo = fuente_Titulo.render("Personalizar Controles", True, BLANCO)
        pantalla.blit(
            texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 6)
        )
        for i, control in enumerate(controles_orden):
            color = AZUL if i == seleccion else BLANCO
            texto = f"{control.capitalize()}: {pygame.key.name(controles[control])}"
            if esperando_tecla and i == seleccion:
                texto = f"{control}: Presiona una tecla..."
            texto_renderizado = fuente.render(texto, True, color)
            pantalla.blit(
                texto_renderizado,
                (ANCHO // 2 - texto_renderizado.get_width() // 2, ALTO // 3 + i * 50),
            )
        texto_instruccion = fuente_instrucciones.render(
            "Presiona ENTER para personalizar", True, gris_claro
        )
        pantalla.blit(
            texto_instruccion,
            (ANCHO // 2 - texto_instruccion.get_width() // 2, ALTO - 100),
        )
        texto_volver = fuente_instrucciones.render(
            "Presiona ESC para volver", True, gris_claro
        )
        pantalla.blit(
            texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 60)
        )
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if esperando_tecla:
                    controles[controles_orden[seleccion]] = evento.key
                    esperando_tecla = False
                else:
                    if evento.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(controles_orden)
                    elif evento.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(controles_orden)
                    elif evento.key == pygame.K_RETURN:
                        esperando_tecla = True
                    elif evento.key == pygame.K_ESCAPE:
                        return
        pygame.display.flip()


def menu_pausa():
    fuente = pygame.font.Font(None, 74)
    fuente_pequeña = pygame.font.Font(None, 36)
    seleccion = 0
    opciones = ["Reanudar", "Reiniciar", "Salir al menú principal"]
    while True:
        pantalla.fill(NEGRO)
        texto_pausa = fuente.render("Pausa", True, BLANCO)
        pantalla.blit(
            texto_pausa, (ANCHO // 2 - texto_pausa.get_width() // 2, ALTO // 4)
        )
        for i, opcion in enumerate(opciones):
            color = BLANCO if i == seleccion else (150, 150, 150)
            texto_opcion = fuente_pequeña.render(opcion, True, color)
            pantalla.blit(
                texto_opcion,
                (ANCHO // 2 - texto_opcion.get_width() // 2, ALTO // 2 + i * 50),
            )
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if seleccion == 0:
                        return "reanudar"
                    elif seleccion == 1:
                        return "reiniciar"
                    elif seleccion == 2:
                        return "menu_principal"
        pygame.display.flip()


def main():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    entrada = ""
    mensaje = "Adivina un número entre 1 y 100"
    ganador = False
    reloj = pygame.time.Clock()
    tiempo_inicial = pygame.time.get_ticks()
    juego_en_pausa = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == controles["Pausa"]:
                    juego_en_pausa = True
                if evento.key == controles["Jugar"] and not adivinado:
                    if entrada:
                        intento = int(entrada)
                        intentos += 1
                        if intento == numero_secreto:
                            mensaje = "¡Correcto!"
                            adivinado = True
                            ganador = True
                        elif intento < numero_secreto:
                            mensaje = "Demasiado bajo. Intenta de nuevo."
                        else:
                            mensaje = "Demasiado alto. Intenta de nuevo."
                        entrada = ""
                elif evento.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                elif evento.unicode.isdigit() and len(entrada) < 3:
                    entrada += evento.unicode
        if juego_en_pausa:
            opcion = menu_pausa()
            if opcion == "menu_principal":
                return
            elif opcion == "reiniciar":
                return main()
            elif opcion == "reanudar":
                juego_en_pausa = False
                continue
        pantalla.fill(NEGRO)
        dibujar_texto(mensaje, ANCHO // 2, 50, VERDE)
        dibujar_texto(f"Intentos: {intentos}", ANCHO // 2, 100, ROJO)
        if adivinado:
            dibujar_texto(f"Número: {numero_secreto}", ANCHO // 2, 150, AMARILLO)
            if ganador:
                dibujar_texto(
                    "¡Ganaste!",
                    ANCHO // 2,
                    ALTO // 2 - 50,
                    VERDE,
                    fuente=fuente_ganador,
                )
        if not adivinado:
            dibujar_caja_entrada(ANCHO // 2, ALTO // 2 + 100, entrada)
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        minutos = tiempo_transcurrido // 60
        segundos = tiempo_transcurrido % 60
        dibujar_texto(
            f"{minutos:02}:{segundos:02}", ANCHO - 80, 30, AZUL, fuente=fuente
        )
        pygame.display.flip()
        reloj.tick(30)


if __name__ == "__main__":
    while menu_principal():
        main()
