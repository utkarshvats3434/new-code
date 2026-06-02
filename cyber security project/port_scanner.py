import socket
import ipaddress  # <--- Naya module jo IP check karega (Public hai ya Private)
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

def scan_ports(target_ip):
    table = Table(title=f"🔍 BreachPoint Scan: {target_ip}", title_style="bold magenta")
    table.add_column("Port Number", justify="center", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Risk Level", justify="center")

    ports_to_check = [21, 22, 23, 25, 53, 80, 443, 3306, 3389, 8080]
    
    with open("scan_report.txt", "a") as report_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_file.write(f"\n--- New Scan Started: {target_ip} at {current_time} ---\n")
        
        with console.status(f"[bold yellow]Target {target_ip} scan ho raha hai...", spinner="dots"):
            for port in ports_to_check:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))
                
                if result == 0:
                    table.add_row(str(port), "[bold red]OPEN[/bold red]", "[bold red]HIGH RISK[/bold red]")
                    report_file.write(f"[WARNING] Port {port} is OPEN on {target_ip}\n")
                else:
                    table.add_row(str(port), "[bold green]CLOSED[/bold green]", "[bold green]SAFE[/bold green]")
                s.close()
                
        report_file.write("--- Scan Completed ---\n")

    console.print(table)
    console.print("[bold green]✅ Scan Report saved in 'scan_report.txt'![/bold green]")


if __name__ == "__main__":
    console.print("\n[bold red]=======================================[/bold red]")
    console.print("[bold red]      🛡️  BREACHPOINT SCANNER  🛡️      [/bold red]")
    console.print("[bold red]=======================================[/bold red]\n")
    
    target_input = console.input("[bold cyan][?] Kisko scan karna hai? (Enter IP): [/bold cyan]")
    target = target_input.strip() 
    
    if target == "":
        console.print("[bold red][!] Error: Target IP khali nahi ho sakta![/bold red]")
    else:
        try:
            # 1. Yeh line input kiye gaye text ko IP object mein badlegi
            ip_obj = ipaddress.ip_address(target)
            
            # 2. Check karein ki IP Private (localhost/LAN) hai ya nahi
            if ip_obj.is_private or ip_obj.is_loopback:
                console.print(f"\n[bold blue][*] Safe Private IP Detected. Scan shuru kiya ja raha hai -> {target}[/bold blue]\n")
                scan_ports(target)
            
            # 3. Agar IP Public (Internet/Google) hai, toh scan nahi hoga
            else:
                console.print(f"\n[bold red][!] WARNING: {target} ek Public IP hai![/bold red]")
                console.print("[bold red][!] Ethics Alert: Bina permission Public IPs ko scan karna allowed nahi hai. Scan Blocked.[/bold red]\n")
                
        except ValueError:
            # Agar user ne galat IP format ya kuch galat text daal diya
            console.print("[bold red][!] Error: Kripya sahi IP address format enter karein (e.g., 127.0.0.1)![/bold red]")