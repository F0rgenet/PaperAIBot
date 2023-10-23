from abc import ABC, abstractmethod


class DocumentBuilder(ABC):
    @abstractmethod
    def create(self, content: str, filename: str):
        pass

