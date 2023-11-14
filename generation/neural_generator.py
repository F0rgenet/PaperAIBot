from documents import builders, DocumentBuilder
import xml.etree.ElementTree as XMLTree
from g4f.Provider import ChatgptX, NoowAi, GPTalk, GptForLove
from g4f import RetryProvider
import g4f

g4f.debug.logging = True


class NeuralDocumentGenerator:
    def __init__(self, theme: str):
        self.theme = theme

    async def generate_outline(self) -> str:
        tree = XMLTree.parse("generation/prompts.xml")
        root = tree.getroot()
        prompt = root.find(".//outline").text.strip().replace("{theme}", self.theme)
        prompt = "\n".join(line.strip() for line in prompt.split("\n"))

        provider = RetryProvider([GptForLove, ChatgptX, NoowAi, GPTalk, GptForLove])
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            provider=provider,
            messages=[{"role": "user", "content": prompt}],
        )
        return response

    async def generate_paragraph(self):
        pass

    async def generate_document(self, filename: str, builder: DocumentBuilder):
        builder.create(filename, "")


