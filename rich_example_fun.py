from time import sleep
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

# --- 1. Färgad och stylad text ---
console.print("[bold green]Rich är igång![/bold green]")
console.print("Du kan använda [red]BBCode[/red]-liknande taggar för färg.")


# --- 2. Skapa en tabell ---
table = Table(title="Exempel på tabell")

table.add_column("Namn", style="cyan", no_wrap=True)
table.add_column("Roll", style="magenta")
table.add_column("Poäng", justify="right", style="green")

table.add_row("Alice", "Utvecklare", "92")
table.add_row("Bob", "Analytiker", "85")
table.add_row("Charlie", "Tester", "78")

console.print(table)


# --- 3. Progress bar ---
console.print("\n[bold]Progress Bar-exempel:[/bold]")

with Progress() as progress:
    task = progress.add_task("Bearbetar data...", total=100)

    while not progress.finished:
        sleep(0.03)
        progress.update(task, advance=1)


# from rich.console import Console
# from rich.json import JSON

# console = Console()

# data = {
#     "name": "Test",
#     "version": 1,
#     "features": ["colors", "tables", "progress"]
# }

# console.print(JSON.from_data(data))
