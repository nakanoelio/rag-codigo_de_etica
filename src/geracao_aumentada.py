from google.genai import types

def augumented_generation(user_query, best_match_text, highest_similarity, client):
    """Gera a resposta usando o contexto mais relevante e o LLM.

    Args:
        user_query (str): Pergunta do usuário.
        best_match_text (str): Texto do documento mais similar.
        highest_similarity (float): Similaridade do melhor documento.
        client: Cliente Gemini para gerar a resposta.

    Returns:
        str: Texto da resposta gerada pelo modelo.
    """

    instructions = (
        "You are a precise technical assistant. Answer the user query using ONLY the provided [[Context]]. "
        "If the query is unrelated to the [[Context]] or [[Similarity]] less than 0.55, say 'Não consegui achar a resposta nos documentos'"
        "If the Context does not contain the answer but query is related to the Context, say 'Não consegui achar a resposta diretamente nos documentos porém,' and provide a generic answer STRICTLY BASED on the context\n\n"
        f"[[Context]]:\n{best_match_text}"
        f"[[Similarity]]:\n{highest_similarity}"
    )

    print(f"\nGenerating response via gemini-2.5-flash...\n")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_query,
        config=types.GenerateContentConfig(
            system_instruction=instructions, temperature=0.0)
    )
    return response.text