from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════╗
║                                                  ║
║   {Fore.YELLOW}███████╗ ██████╗██╗   ██╗███╗   ███╗{Fore.CYAN}          ║
║   {Fore.YELLOW}██╔════╝██╔════╝██║   ██║████╗ ████║{Fore.CYAN}          ║
║   {Fore.YELLOW}███████╗██║     ██║   ██║██╔████╔██║{Fore.CYAN}          ║
║   {Fore.YELLOW}╚════██║██║     ██║   ██║██║╚██╔╝██║{Fore.CYAN}          ║
║   {Fore.YELLOW}███████║╚██████╗╚██████╔╝██║ ╚═╝ ██║{Fore.CYAN}          ║
║   {Fore.YELLOW}╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝{Fore.CYAN}          ║
║                                                  ║
║        {Fore.GREEN}OSINT Tool for Scammer Investigation{Fore.CYAN}     ║
║                                                  ║
║           {Fore.MAGENTA}Made by Kuldeep (CEH){Fore.CYAN}              ║
║        {Fore.WHITE}github.com/kuldeepLinux{Fore.CYAN}              ║
║                                                  ║
╚══════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""

def show_banner():
    print(BANNER)

def show_footer():
    print(f"\n{Fore.CYAN}{'─' * 52}")
    print(f"{Fore.GREEN}  ✓ Tool by {Fore.YELLOW}Kuldeep (CEH){Fore.GREEN} | Happy Ethical Hacking!")
    print(f"{Fore.CYAN}{'─' * 52}{Style.RESET_ALL}\n")
