# 🔐 Cifrado César

Herramienta CLI en **Python** para cifrar y descifrar texto utilizando el método César. Soporta alfabeto español con **ñ**, fuerza bruta y variantes de alfabeto.

## 📋 ¿Qué hace?

- **Cifrado**: Transforma texto usando desplazamiento de caracteres
- **Descifrado**: Revierte el cifrado con la clave correcta
- **Fuerza bruta**: Muestra todas las combinaciones posibles
- **Soporte ñ**: Alfabeto español completo (27 letras)
- **Modo interactivo**: CLI fácil de usar

## 🛠️ Tech Stack

| Lenguaje | Tipo | Librerías |
|----------|------|-----------|
| Python 3.8+ | CLI | argparse |
| | | typing |

## 🚀 Cómo usarlo

### Prerrequisitos

```bash
python3 --version  # Python 3.8+
```

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/epinki07/cifrado-cesar.git
cd cifrado-cesar

# No requiere dependencias externas (stdlib)
```

### Uso

```bash
# Cifrar texto con clave 3
python cifrado.py cifrar "Hola Mundo" --clave 3

# Descifrar texto
python cifrado.py descifrar "Krod Pxqgr" --clave 3

# Fuerza bruta (probar todas las claves)
python cifrado.py fuerza-bruta "Krod Pxqgr"

# Con alfabeto extendido (con ñ)
python cifrado.py cifrar "Niño" --clave 5 --alfabeto-espanol
```

## 📁 Estructura del proyecto

```
cifrado-cesar/
├── cifrado.py          # Lógica principal
├── cli.py              # Interfaz de línea de comandos
├── tests/              # Tests unitarios
│   └── test_cifrado.py
└── README.md
```

## 📖 ¿Cómo funciona?

El cifrado César es un método de sustitución donde cada letra se desplaza una cantidad fija de posiciones en el alfabeto.

**Ejemplo con clave = 3:**
```
A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C
```

**"HOLA"** → **"KROD"** (con clave 3)

## 🧪 Tests

```bash
# Ejecutar tests
python -m pytest tests/

# O con unittest
python -m unittest discover
```

## 💡 Qué aprendí

- **Fundamentos de criptografía**: Cifrados de sustitución
- **Manejo de strings en Python**: Unicode, codificación
- **CLI design**: argparse, UX en terminal
- **Testing**: pytest, casos borde con ñ y caracteres especiales
- **Atención al detalle**: Alfabeto español vs inglés

## 🔮 Mejoras futuras

- [ ] Soporte para archivos de entrada/salida
- [ ] Modo interactivo (REPL)
- [ ] Otros cifrados clásicos (Vigenère, Atbash)
- [ ] Empaquetado como pip installable

## 🤝 Autor

**Diego Ramirez Magaña**

- 📧 dramirezmagana@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/diego-ramirez-maga%C3%B1a-b15022298/)
- 🐙 [GitHub](https://github.com/epinki07)

---

> **Nota**: Proyecto pequeño pero útil para demostrar fundamentos sólidos, manejo de lógica y atención al detalle en implementación.
