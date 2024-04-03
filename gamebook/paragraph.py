class Paragraph:
    text = ""
    options = []
    id = 0
    is_final = True

    def __init__(self, text: str, options: list, id: int, is_final: bool):
        self.text = text
        self.options = options
        self.id = id
        self.is_final = is_final
    
    def display(self):
        print(f"{self.text}\n")
        cislo = 0
        for opt in self.options:
            pismeno = chr(cislo + 65)
            print(f"{pismeno}) {opt.text}")
            cislo = cislo + 1
        print("Kterou možnost zvolíš?")

class Option:
    text = ""
    target = 0
    id = 0

    def __init__(self, text: str, target: int, id: int):
        self.text = text
        self.target = target
        self.id = id
        pass


par0 = Paragraph(
    text="Nachazis se v konferencni mistnosti Poppy. Co tu budes delat?",
    options=[
        Option(text="Ucit se programovat.", id=1, target=1),
        Option(text="Strihat video.", id = 2, target=2),
        Option(text="Spat.", id = 3, target=2),
        ],
    id=0,
    is_final=False
)

par1 = Paragraph(text="Napsal jsi krasny kod!", is_final=True, options=[], id=1)
par2 = Paragraph(text="Nenaucil ses programovat.", is_final=True, options=[], id=2)

paragraphs = [par0, par1, par2]
paragraphs[0].display()
