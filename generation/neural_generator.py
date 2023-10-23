import g4f


class NeuralDocumentGenerator:
    def __init__(self):
        # Initialize the neural network model with the given model_path
        pass

    def generate_document(self, content, filename):
        # Use the neural network model to generate a document from the content
        pass


response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_35_turbo,
    messages=[{"role": "user", "content": f"Тестовое сообщение"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

