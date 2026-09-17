#!/usr/bin/env python3
"""ScamHunter - OSINT Tool | Author: Kuldeep (CEH)"""

import argparse
import sys
from modules.banner import show_banner, show_footer, Fore
from modules.phone_lookup import PhoneLookup

__author__ = "Kuldeep"
__version__ = "1.0.0"

def main():
    show_banner()
    parser = argparse.ArgumentParser(
        description=f"ScamHunter v{__version__} - Made by {__author__}"
    )
    parser.add_argument("-p", "--phone", help="Phone number to lookup")
    parser.add_argument("-r", "--region", default="IN", help="Region code")
    parser.add_argument("-o", "--output", default="report.json", help="Output file")
    parser.add_argument("-v", "--version", action="version",
                        version=f"ScamHunter v{__version__} by {__author__}")
    args = parser.parse_args()

    if not args.phone:
        parser.print_help()
        show_footer()
        sys.exit(1)

    print(f"{Fore.CYAN}[*] Looking up:{Fore.WHITE} {args.phone}")
    print(f"{Fore.CYAN}[*] Tool by:{Fore.YELLOW} {__author__} (CEH)\n")

    tool = PhoneLookup(args.phone, args.region)
    result = tool.run()

    if "error" in result:
        print(f"{Fore.RED}[✗] Error: {result['error']}")
    else:
        print(f"{Fore.GREEN}[✓] Lookup Successful!\n")
        for key, val in result.items():
            if key not in ("input", "timestamp", "tool", "author", "version"):
                print(f"  {Fore.YELLOW}{key:15}{Fore.WHITE}: {val}")

    path = tool.save(args.output)
    print(f"\n{Fore.GREEN}[✓] Report saved: {Fore.WHITE}{path}")
    show_footer()

if __name__ == "__main__":
    main()
