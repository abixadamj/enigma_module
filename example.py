from enigma_module import *

use_these = [("I", "A"), ("II", "B"), ("III", "C")]
machine = Enigma(
    stecker="AQ BJ",
    rotors=use_these,
    reflector="Reflector B",
    operator=True,
    word_length=5,
    stator="military",
)

machine.set_wheels("ABC")
szyfrogram = machine.parse("Zaszyfrowany tekst")
print(szyfrogram)
