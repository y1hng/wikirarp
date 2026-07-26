import sys
import argparse
from colorama import Fore, Style, init
from wikirarp.scanner import scan, RootPermissionError

# Initialize colorama
init(autoreset=True)

BANNER = f"""{Fore.RED}
 __      __.__ __   .__                            
/  \    /  \__|  | _|__|___________ _____________  
\   \/\/   /  |  |/ /  \_  __ \__  \\_  __ \____ \ 
 \        /|  |    <|  ||  | \// __ \|  | \/  |_> >
  \__/\  / |__|__|_ \__||__|  (____  /__|  |   __/ 
       \/          \/              \/      |__|    
{Fore.CYAN}            [ ARP Network Scanner & Mapper ]
{Style.RESET_ALL}"""

def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description="WikiRarp - Fast & Lightweight ARP Network Scanner"
    )
    parser.add_argument("-r", "--range", required=True, help="Network range to scan (e.g., 192.168.1.0/24)")
    parser.add_argument("-t", "--threads", type=int, default=25, help="Number of threads (default: 25)")

    args = parser.parse_args()

    print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Starting WikiRarp scan on: {Fore.YELLOW}{args.range}{Style.RESET_ALL}\n")

    try:
        results = scan(network=args.range, max_workers=args.threads)
        
        if not results:
            print(f"{Fore.YELLOW}[-]{Style.RESET_ALL} No active hosts found.")
            return

        header = f"{'IP Address':<18} {'MAC Address':<18}"
        print(f"{Fore.GREEN}{header}{Style.RESET_ALL}")
        print("-" * 36)
        
        for device in results:
            print(f"{Fore.CYAN}{device['ip']:<18}{Style.RESET_ALL} {Fore.WHITE}{device['mac']:<18}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} Scan completed. Found {len(results)} host(s).")

    except RootPermissionError as e:
        print(f"{Fore.RED}[!]{Style.RESET_ALL} Error: {e}")
        print(f"{Fore.RED}[!]{Style.RESET_ALL} Please run with sudo.")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[!]{Style.RESET_ALL} Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
