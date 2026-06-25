import os
import subprocess
import time
import sys

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def main_menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    while True:
        limpar_tela()
        print_banner()
        print("\n")
        print("QUICK MENU")
        print("RAG para Compliance - Escolha uma opção:")
        print("\n")
        print("1. RAG Rápido - Código de Ética")
        print("2. RAG Avançado")
        print("3. Sair")
        print("\n")
        time.sleep(1)
        opcao_rapida = input("Escolha a opção (1,2 ou 3): ").strip()
        
        if opcao_rapida == "1":
            return {"tipo": "1"}   
        elif opcao_rapida == "2":
            return {"tipo": "2"}
        elif opcao_rapida == "3":
            print("Saindo do programa")
            sys.exit(0)
        else:
            print("Opção não existente. Saindo do programa")
            sys.exit(0)

def limpar_tela():
    """Limpa a tela do terminal de acordo com o sistema operacional."""
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def print_banner():
    """Exibe o banner decorativo do RAG no terminal."""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
 ╔═══════════════════════════════╗
░█████████     ░███      ░██████   
░██     ░██   ░██░██    ░██   ░██  
░██     ░██  ░██  ░██  ░██         
░█████████  ░█████████ ░██  █████  
░██   ░██   ░██    ░██ ░██     ██  
░██    ░██  ░██    ░██  ░██  ░███  
░██     ░██ ░██    ░██   ░█████░█ {Colors.RESET}"""
    print(banner)

def print_main_menu():
    """Imprime o menu principal de opções de documento."""
    print(f"{Colors.YELLOW}{Colors.BOLD}                   MAIN MENU{Colors.RESET}")
    print(f"{Colors.WHITE}    {'═' * 55}{Colors.RESET}")
    
    menu_items = [
        (1, "Código de Ética", Colors.GREEN),
        (2, "Regulamento da Comissão de Ética", Colors.CYAN),
        (3, "Política de Privacidade", Colors.MAGENTA),
        (4, "LGPD", Colors.BLUE),
        (5, "Sair", Colors.RED)
    ]
    
    for num, text, color in menu_items:
        print(f"{color}       [{num}] {text}{Colors.RESET}")
    
    print(f"{Colors.WHITE}    {'═' * 55}{Colors.RESET}")

def print_second_menu():
    """Imprime um menu secundário de navegação."""
    print(f"{Colors.YELLOW}{Colors.BOLD}                   SECOND MENU{Colors.RESET}")
    print(f"{Colors.WHITE}    {'═' * 55}{Colors.RESET}")
    
    menu_items = [
        (1, "Usar base de dados existente", Colors.GREEN),
        (2, "Criar nova base de dados", Colors.CYAN),
        (3, "Submenu Option 3", Colors.MAGENTA),
        (4, "Voltar ao Menu Principal", Colors.BLUE)
    ]
    
    for num, text, color in menu_items:
        print(f"{color}       [{num}] {text}{Colors.RESET}")
    
    print(f"{Colors.WHITE}    {'═' * 55}{Colors.RESET}")

def segundo_menu():
    """Exibe o submenu e trata a opção escolhida pelo usuário."""
    limpar_tela()
    print_banner()
    print_main_menu()
    try:
        choice = input(f"\n{Colors.WHITE}{Colors.BOLD}   Select an option (1-5): {Colors.YELLOW}")
                
        if choice == "1":
            print(f"\n{Colors.GREEN}🎮 Game starting... Let's go!{Colors.RESET}")
        elif choice == "2":
            print(f"\n{Colors.CYAN}⚙️  Opening Settings...{Colors.RESET}")
        elif choice == "3":
            print(f"\n{Colors.MAGENTA}🏆 Loading High Scores...{Colors.RESET}")
        elif choice == "4":
            print(f"\n{Colors.BLUE}📖 Tutorial would go here!{Colors.RESET}")
        elif choice == "5":
            print(f"\n{Colors.RED}👋 Goodbye! See you next time!{Colors.RESET}")
            time.sleep(1.2)
        else:
            print(f"\n{Colors.RED}Invalid option! Please try again.{Colors.RESET}")
                
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.RESET}")
                
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Program terminated by user.{Colors.RESET}")
    
    except Exception:
        print(f"\n{Colors.RED}An error occurred. Please try again.{Colors.RESET}")
        time.sleep(1)
    return {"tipo": "1"}




