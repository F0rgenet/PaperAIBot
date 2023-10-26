import g4f


class NeuralDocumentGenerator:
    def __init__(self, theme: str):
        self.theme = theme

    def generate_outline(self):
        pass

    def generate_paragraph(self):
        pass

    def generate_document(self, content, filename):
        pass


response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_35_turbo,
    messages=[{"role": "user", "content": f"Тестовое сообщение"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

