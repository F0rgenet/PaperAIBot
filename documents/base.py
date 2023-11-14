from abc import ABC, abstractmethod


class DocumentBuilder(ABC):
    @abstractmethod
    def create(self, filename: str, content: str):
        pass

