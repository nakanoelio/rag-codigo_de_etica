import pickle
from pathlib import Path

import chunkificador
import embeddar
import extrair_pdf

def gerar_corpus(client, escolha_menu):
    """Gera ou carrega um corpus de embeddings conforme a opção do menu.

    Args:
        client: Cliente Gemini usado para criar embeddings.
        escolha_menu (dict): Dicionário com a opção selecionada pelo usuário.

    Returns:
        dict: Dicionário de embeddings carregados ou gerados.
    """   
    # compute repository-root-relative paths
    repo_root = Path(__file__).resolve().parent.parent
    print(repo_root)
    pkl_path = repo_root / 'context_embeddings' / 'CdE_rag.pkl'
    pdf_path = repo_root / 'pdf' / 'Código_de_Ética_exemplo.pdf'

    if escolha_menu["tipo"] == "2":
        # generate corpus from the source PDF and save embeddings
        existe_pdf = input("Informe o caminho do arquivo em pdf ou aperte Enter se já houver um arquivo: ").strip()
        if existe_pdf == "":
            caminho_do_pdf = str(pdf_path)
        else:
            caminho_do_pdf = existe_pdf
        # se o caminho informado não existir, avisar e usar o padrão
        if not Path(caminho_do_pdf).exists():
            print(f"Aviso: '{caminho_do_pdf}' não encontrado. Usando PDF padrão: {pdf_path}")
            caminho_do_pdf = str(pdf_path)
        corpus_texto = extrair_pdf.create_corpus_from_pdf(caminho_do_pdf)
        chunks = chunkificador.chunkificar(corpus_texto)
        vetor_embeddings = embeddar.emb_documentos(chunks, client)
        pkl_path.parent.mkdir(parents=True, exist_ok=True)
        with open(pkl_path, 'wb') as f:
            pickle.dump(vetor_embeddings, f)
    
    elif escolha_menu["tipo"] == "1":  
        with open(pkl_path, 'rb') as f:
            vetor_embeddings = pickle.load(f)
    
    return vetor_embeddings