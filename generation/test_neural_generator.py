from unittest import IsolatedAsyncioTestCase
from .neural_generator import NeuralDocumentGenerator


class TestNeuralDocumentGenerator(IsolatedAsyncioTestCase):
    def setUp(self):
        self.generator = NeuralDocumentGenerator("Солнечная энергетика")

    async def test_generate_outline(self):
        outline = await self.generator.generate_outline()
        print(outline)
        self.assertGreater(len(outline.split("\n")), 5)

    async def test_generate_paragraph(self):
        self.fail()

    async def test_generate_document(self):
        self.fail()
