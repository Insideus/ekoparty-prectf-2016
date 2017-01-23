from operator import itemgetter
from PIL import Image

calls = {
    "0x634": ("digitalWrite", ("r24", )),
    "0xd0e": ("delay", ("r22", "r23", "r24", "r25")),
}

registers = {
    "r22": 0x0,
    "r23": 0x0,
    "r24": 0x0,
    "r25": 0x0,
}

MORSE = {
    (0, 150): "-",
    (0, 10): ".",
    (99, 255): " "
}

ALPHABET = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z", "-.--.": "{", "-.--.-": "}", ".-.-.-": ".",
    " ": " "
}


class Plot(object):

    def __init__(self, height=100):
        self._height = height
        self._cursor = (0, height - 1)
        self._img = Image.new('RGB', (6024, height), "black")
        self._pixels = self._img.load()
        self._morse = ""

    def digitalWrite(self, bit):
        x, y = self._cursor
        y_dest = -1 if bit else self._height
        for y in xrange(y, y_dest, -1 if bit else 1):
            self._pixels[x, y] = (0xFF, 0x00, 0x00)
            self._cursor = (x, y)

    def delay(self, ms):
        x, y = self._cursor
        x_dest = x + (ms / 2)

        if (y, ms) in MORSE:
            self._morse += MORSE[(y, ms)]

        for x in xrange(x, x_dest):
            self._pixels[x, y] = (0xFF, 0x00, 0x00)
            self._cursor = (x, y)

    def draw(self):
        self._img.save("whatever.png")

    def morse(self):
        words = map(ALPHABET.__getitem__, self._morse.strip().split(" "))
        return "".join(words)


plot = Plot()
for instruction in open("sequence.asm"):
    opcode, args = instruction.strip().split("\t")
    args = args.split(", ")
    if opcode == "call":
        address = args[0]
        function, arg_regs = calls[address]

        value = 0
        for i, arg_reg in enumerate(arg_regs):
            reg = registers[arg_reg]
            value |= (reg << (i * 8))

        print "Calling %s(%d)" % (function, value)
        getattr(plot, function)(value)

    elif opcode == "ldi":
        register, value = args
        if register not in registers:
            raise ValueError("Invalid register %s" % register)

        registers[register] = int(value[2:], 16)
        print "Assigning %s = %s" % (register, value)

plot.draw()
print "The key is:", plot.morse()
