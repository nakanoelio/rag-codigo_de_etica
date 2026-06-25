import numpy as np

def similaridade_coseno(pergunta_usuario, vetor_dicionario):
    """Calcula a similaridade de cosseno entre a pergunta e cada embedding do corpus.

    Args:
        pergunta_usuario: Embedding da pergunta do usuário.
        vetor_dicionario (dict): Dicionário de embeddings de documentos.

    Returns:
        tuple[str, float]: Texto mais semelhante e o valor da similaridade.
    """
    texto_mais_parecido = None
    maior_similaridade = -1.0

    # Cosine Similarity Formula: (A . B) / (||A|| * ||B||)
    for texto_doc in vetor_dicionario.items():
        vetor_texto = texto_doc[1]["embedding_vetor"]
        
        # Calculate dot product
        dot_product = np.dot(pergunta_usuario, vetor_texto)
        
        # Calculate magnitudes (norms)
        query_norm = np.linalg.norm(pergunta_usuario)
        doc_norm = np.linalg.norm(vetor_texto)
        
        # Compute Cosine Similarity
        similaridade = dot_product / (query_norm * doc_norm)
        
        # Track the document with the highest match score
        if similaridade > maior_similaridade:
            maior_similaridade = similaridade
            texto_mais_parecido = texto_doc[1]["texto"]

    #print(f"Top context retrieved manually (Similarity Score: {maior_similaridade:.4f})")
    return texto_mais_parecido, maior_similaridade