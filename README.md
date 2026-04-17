# cifrado-cesar

Herramienta en Python para cifrar y descifrar texto con el metodo Cesar. Soporta el alfabeto espanol completo con la letra n, y permite elegir el desplazamiento manualmente.

## Que hace

- Cifra texto dado un desplazamiento
- Descifra texto cifrado dado el mismo desplazamiento
- Soporte de la n (27 letras)
- Opcion de fuerza bruta para probar todos los desplazamientos posibles
- Script directo por consola, sin dependencias externas

## Archivos

```
cifrado-cesar/
├── descifrar_cesar_es.py   # Script principal
├── Como usar cesar.png     # Captura de uso
└── README.md
```

## Como usarlo

```bash
git clone https://github.com/epinki07/cifrado-cesar.git
cd cifrado-cesar
python3 descifrar_cesar_es.py
```

El script pide el texto y el desplazamiento, y devuelve el resultado.

```
Texto: Hola mundo
Desplazamiento: 3
Resultado cifrado: Krrod pxqgr
```

## Tech Stack

Python 3.8+, sin dependencias externas.

## Autor

Diego Ramirez Magana — [LinkedIn](https://www.linkedin.com/in/diego-ramirez-maga%C3%B1a-b15022298/) | [GitHub](https://github.com/epinki07) | dramirezmagana@gmail.com
