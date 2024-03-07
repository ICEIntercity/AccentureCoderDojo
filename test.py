class Paragraph:
    options = []
    text = ""
    id = 0
    is_final = True

    def __init__(self, options: list, text: str, id: int, is_final: bool):
        self.options = options
        self.text = text
        self.id = id
        self.is_final = is_final

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
    text="Nachazis se v konferencni mistnosti Poppy.",
    options=[
        Option(text="Ucit se programovat.", id=1, target=1),
        Option(text="Strihat video.", id = 2, target=2),
        Option(text="Spat.", id = 3, target=2),
        ],
    id=0,
    is_final=False
    )

par1 = Paragraph(text="Napsal jsi krasny kod!", is_final=True, options=[], id=1)
par2 = Paragraph(text="Nenaucil jsi se programovat.", is_final=True, options=[], id=2)



