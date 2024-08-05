import os

GREETINGS = {
    "SPANISH": "¡Hola!",
    "ENGLISH": "Hello!",
    "ROMANSH": "Allegra!",
    "KLINGON": "nukneH!"
}

def greet():
    language = os.environ.get("LOCAL_LANGUAGE", "ROMANSH").upper()
    if language not in GREETINGS:
        language = "ROMANSH"
    greeting = GREETINGS[language]
    print(greeting)

if __name__ == "__main__":
    greet()
    