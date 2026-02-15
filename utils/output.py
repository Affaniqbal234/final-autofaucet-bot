from rich.console import Console

console = Console()


def print_banner():
    banner_text = """
[bold cyan]╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ███████╗██╗███╗   ██╗ █████╗ ██╗       █████╗ ██╗   ██╗████████╗ ██████╗    ║
║  ██╔════╝██║████╗  ██║██╔══██╗██║      ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗   ║
║  █████╗  ██║██╔██╗ ██║███████║██║      ███████║██║   ██║   ██║   ██║   ██║   ║
║  ██╔══╝  ██║██║╚██╗██║██╔══██║██║      ██╔══██║██║   ██║   ██║   ██║   ██║   ║
║  ██║     ██║██║ ╚████║██║  ██║███████╗ ██║  ██║╚██████╔╝   ██║   ╚██████╔╝   ║
║  ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝    ║
║                                                                              ║ 
║                  ██████╗██╗      █████╗ ██╗███╗   ╔███╗                      ║
║                 ██╔════╝██║     ██╔══██╗██║████╗ ╔████║                      ║
║                 ██║     ██║     ███████║██║██╔═███  ██║                      ║
║                 ██║     ██║     ██╔══██║██║██║      ██║                      ║
║                 ╚██████╗███████╗██║  ██║██║██║      ██║                      ║
║                  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═╝                      ║
║            [bold green]Final Auto Faucet Bot[/bold green] - [bold red]Automate Your Earnings[/bold red]                    ║
║                                 [bold red]v1.0.0[/bold red]                                       ║
║          [bold green]GitHub:[/bold green] [bold red][link=https://github.com/Affaniqbal234/final-autofaucet-bot]github.com/Affaniqbal234/final-autofaucet-bot[/link][/bold red]               ║
║          [bold green]Author:[/bold green] [bold red]Affan[/bold red] (@Affaniqbal234)                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝[/bold cyan]
"""
    console.print(banner_text)


def print_success(message):
    console.print(f"[green]✅ {message}[/green]")


def print_error(message):
    console.print(f"[red]❌ {message}[/red]")


def print_info(message):
    console.print(f"[blue]ℹ️  {message}[/blue]")


def print_section(title):
    console.print(f"\n[bold cyan]{'='*80}[/bold cyan]")
    console.print(f"[bold cyan]{title.center(80)}[/bold cyan]")
    console.print(f"[bold cyan]{'='*80}[/bold cyan]\n")
