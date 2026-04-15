#!/usr/bin/env python3
"""Cifra y descifra textos con Cesar en variantes del alfabeto espanol."""

from __future__ import annotations

VARIANTES = [
    {
        "nombre": "Solo letras",
        "descripcion": "Usa el alfabeto espanol de 27 letras, incluida la ñ.",
        "alfabeto": "abcdefghijklmnñopqrstuvwxyz",
    },
    {
        "nombre": "Letras y espacio",
        "descripcion": "Usa el alfabeto espanol y tambien desplaza el espacio.",
        "alfabeto": " abcdefghijklmnñopqrstuvwxyz",
    },
]


def crear_indices(alfabeto: str) -> dict[str, int]:
    return {simbolo: indice for indice, simbolo in enumerate(alfabeto)}


def transformar_con_clave(
    texto: str, clave: int, alfabeto: str, direccion: int
) -> str:
    indices = crear_indices(alfabeto)
    longitud_alfabeto = len(alfabeto)
    resultado = []

    for caracter in texto:
        minuscula = caracter.lower()

        if minuscula not in indices:
            resultado.append(caracter)
            continue

        indice_original = indices[minuscula]
        indice_transformado = (indice_original + (direccion * clave)) % longitud_alfabeto
        letra = alfabeto[indice_transformado]

        if caracter.isupper() and letra.isalpha():
            letra = letra.upper()

        resultado.append(letra)

    return "".join(resultado)


def cifrar_con_clave(texto: str, clave: int, alfabeto: str) -> str:
    return transformar_con_clave(texto, clave, alfabeto, direccion=1)


def descifrar_con_clave(texto: str, clave: int, alfabeto: str) -> str:
    return transformar_con_clave(texto, clave, alfabeto, direccion=-1)


def mostrar_introduccion() -> None:
    print("Herramienta de Cesar para el alfabeto espanol.")
    print()
    print("Como usarlo:")
    print("- Elige si quieres cifrar, descifrar con clave o probar todas las claves.")
    print("- Escribe o pega uno o varios textos.")
    print("- Presiona Enter en una linea vacia para procesarlos.")
    print("- El programa usa estas dos variantes de Cesar:")
    print("  1. Solo letras: abcdefghijklmnñopqrstuvwxyz")
    print("  2. Letras y espacio: ' abcdefghijklmnñopqrstuvwxyz'")
    print()
    print("Como leer la salida:")
    print("- 'Cifrar con clave' mueve cada letra hacia adelante.")
    print("- 'Descifrar con clave' mueve cada letra hacia atras.")
    print("- 'Probar todas las claves' muestra todas las posibilidades para ayudarte a hallar el mensaje.")
    print("- Si quieres mover tambien los espacios, usa la variante 'Letras y espacio'.")
    print()


def obtener_accion() -> str:
    print("Elige una accion:")
    print("1. Cifrar con clave")
    print("2. Descifrar con clave")
    print("3. Probar todas las claves")

    opciones = {
        "1": "cifrar",
        "c": "cifrar",
        "cifrar": "cifrar",
        "2": "descifrar",
        "d": "descifrar",
        "descifrar": "descifrar",
        "3": "probar",
        "p": "probar",
        "probar": "probar",
    }

    while True:
        respuesta = input("Opcion: ").strip().lower()
        accion = opciones.get(respuesta)
        if accion is not None:
            return accion
        print("Opcion no valida. Elige 1, 2 o 3.")


def obtener_textos() -> list[str]:
    textos = []

    print("Ingresa el texto. Usa una linea vacia para terminar:")
    while True:
        linea = input("> ")
        if linea == "":
            break
        textos.append(linea)

    return textos


def obtener_variante() -> dict[str, str]:
    print()
    print("Elige la variante del alfabeto:")
    for indice, variante in enumerate(VARIANTES, start=1):
        print(f"{indice}. {variante['nombre']}: {variante['descripcion']}")

    while True:
        respuesta = input("Opcion: ").strip()
        if respuesta in {"1", "2"}:
            return VARIANTES[int(respuesta) - 1]
        print("Opcion no valida. Elige 1 o 2.")


def obtener_clave(longitud_alfabeto: int) -> int:
    while True:
        respuesta = input(f"Clave: ").strip()
        try:
            clave = int(respuesta)
        except ValueError:
            print("La clave debe ser un numero entero.")
            continue

        clave_normalizada = clave % longitud_alfabeto
        if clave_normalizada != clave:
            print(
                f"Se usara la clave {clave_normalizada} dentro del alfabeto de {longitud_alfabeto} simbolos."
            )
        return clave_normalizada


def mostrar_resultados_con_clave(
    textos: list[str], accion: str, variante: dict[str, str], clave: int
) -> None:
    alfabeto = variante["alfabeto"]
    transformador = cifrar_con_clave if accion == "cifrar" else descifrar_con_clave
    etiqueta = "Texto cifrado" if accion == "cifrar" else "Texto descifrado"

    print()
    print(f"Variante: {variante['nombre']}")
    print(f"Clave usada: {clave}")

    for numero, texto in enumerate(textos, start=1):
        resultado = transformador(texto, clave, alfabeto)
        print()
        print(f"Texto {numero}: {texto}")
        print(f"{etiqueta}: {resultado}")


def mostrar_resultados_fuerza_bruta(textos_cifrados: list[str]) -> None:
    for numero, texto_cifrado in enumerate(textos_cifrados, start=1):
        print()
        print(f"Texto {numero}: {texto_cifrado}")
        for variante in VARIANTES:
            nombre = variante["nombre"]
            descripcion = variante["descripcion"]
            alfabeto = variante["alfabeto"]

            print()
            print(f"{nombre}:")
            print(f"  {descripcion}")
            for clave in range(len(alfabeto)):
                texto_descifrado = descifrar_con_clave(texto_cifrado, clave, alfabeto)
                print(f"  Clave {clave:2}: {texto_descifrado}")


def preguntar_si_continuar() -> bool:
    respuesta = input("\nQuieres procesar mas textos? (s/n): ").strip().lower()
    return respuesta in {"s", "si", "y", "yes"}


def main() -> None:
    mostrar_introduccion()

    while True:
        accion = obtener_accion()
        print()
        textos = obtener_textos()

        if not textos:
            print("\nNo se ingreso ningun texto.")
        elif accion == "probar":
            mostrar_resultados_fuerza_bruta(textos)
        else:
            variante = obtener_variante()
            clave = obtener_clave(len(variante["alfabeto"]))
            mostrar_resultados_con_clave(textos, accion, variante, clave)

        if not preguntar_si_continuar():
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    main()
