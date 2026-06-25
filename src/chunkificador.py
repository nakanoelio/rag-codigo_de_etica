def chunkificar(text):
    """Divide o texto de entrada em chunks com sobreposição.

    Args:
        text: Lista de palavras ou texto a ser dividido em pedaços.

    Returns:
        list[str]: Lista de strings onde cada elemento é um chunk de texto.
    """
    tamanho_chunk = 150 # Define the desired chunk size (number of words)
    janela_sobreposicao = 15  # Define the window movement (number of words)    
    chunks = []
    for i in range(0, len(text), (tamanho_chunk-janela_sobreposicao)):
        chunk_separado = text[i:i + tamanho_chunk]

        chunk = str(" ".join(chunk_separado).replace("\n", "").strip())
        chunks.append(chunk)
    return chunks

"""Very basic chunkifier, just to split the text into chunks of a certain size
and certain overlap. It can be improved with more advanced techniques like semantic chunking or using 
NLP libraries for better context preservation. """