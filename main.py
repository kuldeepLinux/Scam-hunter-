#!/usr/bin/env python3
"""
ScamHunter v2.0 - OSINT Tool for Scammer Investigation
Author: Kuldeep (CEH)
GitHub: github.com/kuldeepLinux
"""

import sys
import argparse
from colorama import Fore, Style, init

from modules.banner import show_banner, show_menu, show_footer
from modules.phone_lookup import PhoneLookup
from modules.email_lookup import EmailLookup

init(autoreset=True)

__author__ = "Kuldeep"
__version__ = "2.0.0"


def print_result(result):
    """Result को अच्छे format में print करें"""
    if "error" in result:
        print(f"\n{Fore.RED}[✗] Error: {result['error']}")
        return

    print(f"\n{Fore.GREEN}[✓] Lookup Successful!\n")
    for key, val in result.items():
        if key in ("tool", "author", "version", "input", "timestamp", "_meta", "module"):
            continue
        if isinstance(val, dict):
            print(f"  {Fore.YELLOW}{key:15}{Fore.WHITE}:")
            for k, v in val.items():
                print(f"    {Fore.CYAN}{k:15}{Fore.WHITE}: {v}")
        elif isinstance(val, list):
            print(f"  {Fore.YELLOW}{key:15}{Fore.WHITE}: {', '.join(map(str, val))}")
        else:
            print(f"  {Fore.YELLOW}{key:15}{Fore.WHITE}: {val}")


def phone_menu():
    phone = input(f"\n{Fore.CYAN}📱 Enter phone number (e.g., +919876543210): {Fore.WHITE}").strip()
    if not phone:
        print(f"{Fore.RED}[✗] No number entered")
        return

    print(f"\n{Fore.CYAN}[*] Looking up: {phone}")
    tool = PhoneLookup(phone)
    result = tool.run()
    print_result(result)

    path = tool.save()
    print(f"\n{Fore.GREEN}[✓] Report saved: {Fore.WHITE}{path}")


def email_menu():
    email = input(f"\n{Fore.CYAN}📧 Enter email address: {Fore.WHITE}").strip()
    if not email:
        print(f"{Fore.RED}[✗] No email entered")
        return

    print(f"\n{Fore.CYAN}[*] Looking up: {email}")
    tool = EmailLookup(email)
    result = tool.run()
    print_result(result)

    path = tool.save()
    print(f"\n{Fore.GREEN}[✓] Report saved: {Fore.WHITE}{path}")


def coming_soon(name):
    print(f"\n{Fore.YELLOW}[!] {name} module coming soon!")
    print(f"{Fore.CYAN}    Stay tuned: github.com/kuldeepLinux")


def interactive_menu():
    while True:
        show_menu()
        choice = input(f"{Fore.GREEN}Enter your choice [1-6]: {Fore.WHITE}").strip()

        if choice == "1":
            phone_menu()
        elif choice == "2":
            email_menu()
        elif choice == "3":
            coming_soon("Username Search")
        elif choice == "4":
            coming_soon("Domain Lookup")
        elif choice == "5":
            coming_soon("IP Address Lookup")
        elif choice == "6":
            print(f"\n{Fore.CYAN}Thanks for using ScamHunter! Stay safe. 🛡️")
            show_footer()
            break
        else:
            print(f"{Fore.RED}[✗] Invalid choice. Try again.")

        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(
        description=f"ScamHunter v{__version__} - OSINT Tool by {__author__} (CEH)"
    )
    parser.add_argument("-p", "--phone", help="Phone number to lookup")
    parser.add_argument("-e", "--email", help="Email to lookup")
    parser.add_argument("-r", "--region", default="IN", help="Region code (default: IN)")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-v", "--version", action="version",
                        version=f"ScamHunter v{__version__} by {__author__}")
    args = parser.parse_args()

    show_banner()

    # Direct command mode
    if args.phone:
        tool = PhoneLookup(args.phone, args.region)
        result = tool.run()
        print_result(result)
        path = tool.save(args.output) if args.output else tool.save()
        print(f"\n{Fore.GREEN}[✓] Report saved: {Fore.WHITE}{path}")
        show_footer()
        return

    if args.email:
        tool = EmailLookup(args.email)
        result = tool.run()
        print_result(result)
        path = tool.save(args.output) if args.output else tool.save()
        print(f"\n{Fore.GREEN}[✓] Report saved: {Fore.WHITE}{path}")
        show_footer()
        return

    # Interactive menu mode
    interactive_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Exiting...")
        sys.exit(0)
