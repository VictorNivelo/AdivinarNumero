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


def dibujar_texto(texto, x, y, color=BLANCO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)


def dibujar_caja_entrada(x, y, texto):
    pygame.draw.rect(pantalla, BLANCO, (x - 100, y - 20, 200, 40), 2)
    dibujar_texto(texto, x, y)


def dibujar_fondo():
    pantalla.fill(NEGRO)


def menu_principal():
    seleccion = 0
    opciones = ["Jugar", "Salir"]
    while True:
        dibujar_fondo()
        dibujar_texto("Adivina el Número", ANCHO // 2, ALTO // 4, AMARILLO)
        for i, opcion in enumerate(opciones):
            color = BLANCO if i == seleccion else (150, 150, 150)
            dibujar_texto(opcion, ANCHO // 2, ALTO // 2 + i * 50, color)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if seleccion == 0:
                        return True
                    elif seleccion == 1:
                        pygame.quit()
                        return False
        pygame.display.flip()


def menu_pausa():
    seleccion = 0
    opciones = ["Reanudar", "Reiniciar", "Salir al menú principal"]
    while True:
        dibujar_fondo()
        dibujar_texto("Juego en Pausa", ANCHO // 2, ALTO // 4, AMARILLO)
        for i, opcion in enumerate(opciones):
            color = BLANCO if i == seleccion else (150, 150, 150)
            dibujar_texto(opcion, ANCHO // 2, ALTO // 2 + i * 50, color)
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
                if evento.key == pygame.K_ESCAPE:
                    juego_en_pausa = True
                if evento.key == pygame.K_RETURN and not adivinado:
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
        dibujar_fondo()
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
