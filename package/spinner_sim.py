from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Create a progress bar
with Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.description]{task.description}")) as progress:
    task = progress.add_task("Processing...", total=1000000)

    while not progress.finished:
        progress.update(task, advance=1)
