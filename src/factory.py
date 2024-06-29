from abc import ABC, abstractmethod

"""
# Factory Pattern

**Purpose:**
Provides an interface for creating objects in a superclass, but allows subclasses to alter the 
type of objects that will be created.

**When to Use:** 
When the exact type of the object cannot be predicted until runtime.

**Advantages:**
Promotes loose coupling.
Adds a level of abstraction to the instantiation process.

**Disadvantages:**
Can increase complexity of the codebase.

**Use-Cases:**
GUI toolkit (creating buttons, textboxes, etc.).
Document reader (reading different file formats).
Shape generator.

Example in Python (Document reader use-case):
"""

# Document Reader base class
class DocumentReader(ABC):
    @abstractmethod
    def read(self, filepath):
        pass

# Concrete Document Readers
class PDFReader(DocumentReader):
    def read(self, filepath):
        return f"Reading PDF file: {filepath}"

class WordReader(DocumentReader):
    def read(self, filepath):
        return f"Reading Word file: {filepath}"

class TextReader(DocumentReader):
    def read(self, filepath):
        return f"Reading Text file: {filepath}"

# Factory class
class DocumentReaderFactory:
    @staticmethod
    def get_document_reader(filetype):
        if filetype == "pdf":
            return PDFReader()
        elif filetype == "word":
            return WordReader()
        elif filetype == "text":
            return TextReader()
        else:
            raise ValueError(f"Unsupported file type: {filetype}")

# Usage
def read_document(filepath, filetype):
    reader = DocumentReaderFactory.get_document_reader(filetype)
    return reader.read(filepath)

if __name__=="__main__":
    try:
        print(read_document("document.pdf", "pdf"))   # Reading PDF file: document.pdf
        print(read_document("document.docx", "word")) # Reading Word file: document.docx
        print(read_document("document.txt", "text"))  # Reading Text file: document.txt
    except ValueError as e:
        print(e)