import requests
from rich.console import Console
from rich.table import Table

console = Console()

def check_subdomains(target_domain):
    # A small sample list of common subdomains to check
    common_subdomains = ["admin", "dev", "mail", "api", "test", "staging"]
    
    # Create a beautiful terminal table using the 'rich' library
    table = Table(title=f"🔍 BreachPoint Scan Results for: {target_domain}")
    table.add_column("Subdomain", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("URL", style="magneta")

    console.print(f"[bold yellow]Starting reconnaissance on {target_domain}...[/bold yellow]\n")

    for sub in common_subdomains:
        url = f"http://{sub}.{target_domain}"
        try:
            # Send a quick request to see if the website responds
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                table.add_row(f"{sub}.{target_domain}", "ONLINE (200 OK)", url)
        except requests.ConnectionError:
            # If the subdomain doesn't exist, it throws an error; we just skip it
            continue

    console.print(table)

# Run the scanner on a safe target
if __name__ == "__main__":
    # Use a safe, open domain for testing, or your own local setups
    check_subdomains("google.com")