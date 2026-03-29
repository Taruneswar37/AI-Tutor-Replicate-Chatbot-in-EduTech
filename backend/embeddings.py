from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transcribe import transcribe_m

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def create_chunks(text):
    """Splits the input text into smaller chunks using RecursiveCharacterTextSplitter."""
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=300, 
        chunk_overlap=50
    )
    return splitter.split_text(text)

def create_embeddings(chunks):
    """Generates embeddings for each chunk of text."""
    return embed_model.encode(chunks)

def process(file_path):
    """Main function to process the input file and generate embeddings."""
    text = transcribe_m(file_path)
    chunks = create_chunks(text)
    embeddings = create_embeddings(chunks)
    return chunks, embeddings

if __name__ == "__main__":
    "Example usage"
    file_path = r"D:\Tarun\video text\data\uploads\VID-20250916-WA0017.mp4"
    chunks, embeddings = process(file_path)
    print("\nChunks:\n", chunks)
    print("\nEmbeddings shape:\n", embeddings.shape)