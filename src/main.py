#!/usr/bin/env python3
from google import genai
import menu
import corpus
import embeddar
import recuperacao_rag
import geracao_aumentada

def main():
    """Executa o fluxo principal do RAG.

    Esta função obtém a chave da API, executa o loop de perguntas e respostas,
    processa a pergunta do usuário e exibe a resposta até o usuário decidir sair.
    """
    API_KEY = obter_chave_llm()
    
    while True:
        pergunta_usuario, resposta = funcoes_rag(API_KEY)

        print("\n")
        print(f"A sua pergunta é:\n\n{pergunta_usuario}")
        print("\n")
        print(f"A resposta é:\n\n{resposta}")

        continuar = input(f'\nDeseja fazer uma nova pergunta?: (digite "S" para sim ou "N" para não) ')
        if continuar.upper().strip() == "S":
            continue
        else:
            print("\n")
            print(f'Saindo do RAG!')
            break

def obter_chave_llm() -> str:
    """Solicita a chave de API do Gemini ao usuário.

    Returns:
        str: A chave de API informada pelo usuário, sem espaços em branco extras.
    """
    chave_llm: str = input("Informe a chave API do Gemini: ").strip()
    return chave_llm  

def funcoes_rag(API_KEY):
    """Executa as etapas de recuperação aumentada para uma pergunta do usuário.

    Args:
        API_KEY (str): A chave de API utilizada para criar o cliente Gemini.

    Returns:
        tuple[str, str]: A pergunta do usuário e a resposta gerada pelo RAG.
    """
    client = genai.Client(api_key=API_KEY)
    escolha_menu = menu.main_menu()
    vetor_dicionario = corpus.gerar_corpus(client=client, escolha_menu=escolha_menu)  
    pergunta_usuario = input("Qual é a sua pergunta?: ").strip()
    embedding_pergunta = embeddar.emb_pergunta(pergunta_usuario, client)
    texto_mais_parecido, maior_similaridade = recuperacao_rag.similaridade_coseno(
        embedding_pergunta, vetor_dicionario)   
    resposta = geracao_aumentada.augumented_generation(
        pergunta_usuario, texto_mais_parecido, maior_similaridade, client)
    return pergunta_usuario, resposta

if __name__ == "__main__":
    
    main()
