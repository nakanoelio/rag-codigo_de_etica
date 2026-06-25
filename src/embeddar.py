import numpy as np

model = "gemini-embedding-001" # Pode-se escolher outros modelos de embedding, porém deve ser consistente com o modelo para a pergunta.

def emb_documentos(documents_text, client):
    """Cria embeddings para cada documento do corpus.

    Args:
        documents_text: Lista de textos dos documentos.
        client: Cliente Gemini usado para gerar embeddings.

    Returns:
        dict: Dicionário com texto e embedding de cada documento.
    """
    vetor_dicionario = {}
    i = 0
    for doc in documents_text:
        embedding_resposta = client.models.embed_content(
            model=model,
            contents=doc
        )
        # Extract vector and convert it immediately into a NumPy array
        vetor_embedding = np.array(embedding_resposta.embeddings[0].values, dtype=np.float32)
        vetor_dicionario[f"{i}"] = {
            "texto": doc,
            "embedding_vetor": vetor_embedding
        }
        i += 1
    return vetor_dicionario

def emb_pergunta(user_query, client):
    """Gera embedding para a pergunta do usuário.

    Args:
        user_query (str): Texto da pergunta do usuário.
        client: Cliente Gemini usado para gerar o embedding.

    Returns:
        numpy.ndarray: Vetor de embedding da pergunta.
    """
    query_response = client.models.embed_content(
        model=model,
        contents=user_query
    )
    query_vector = np.array(query_response.embeddings[0].values, dtype=np.float32)
    return query_vector
