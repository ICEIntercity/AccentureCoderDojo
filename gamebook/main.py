import json

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
        
        if len(self.options) != 0:
            print("Kterou možnost zvolíš?")

def load_paragraphs(file_path):
    paragraphs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            par_options = []
            for opt_str in item['options']:
                opt = Option(
                    text=opt_str['text'],
                    target=opt_str['target'],
                    id=opt_str['id']
                )
                par_options.append(opt)

            par = Paragraph(
                text=item['text'],
                options=par_options,
                id=item['id'],
                is_final=item['is_final']
            )
            paragraphs.insert(par.id, par)

    return paragraphs

class Option:
    text = ""
    target = 0
    id = 0

    def __init__(self, text: str, target: int, id: int):
        self.text = text
        self.target = target
        self.id = id
        pass


paragraphs = load_paragraphs("paragraphs.json")

current_paragraph = paragraphs[0]
current_paragraph.display()

while True:
    choice = input()

    if len(choice) != 1:
        print("Napis to znovu a spravne")
        exit(-1)

    choice_id = ord(choice.upper()) - 65

    try:
        target_paragraph = current_paragraph.options[choice_id].target # target moznosti cislo choice_id v current_paragraph
    except IndexError:
        print("Moznost neexistuje!")
        exit(-2)

    current_paragraph = paragraphs[target_paragraph]
    current_paragraph.display()

    if current_paragraph.is_final:
        exit(0)
        