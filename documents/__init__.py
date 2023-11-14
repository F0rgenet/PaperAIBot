from .docx import DocumentBuilder as DOCXBuilder
from .pdf import DocumentBuilder as PDFBuilder
from .base import DocumentBuilder

builders = [DOCXBuilder, PDFBuilder]
