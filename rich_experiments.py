from rich import print
from rich.console import Console

### Console Markup

print("[italic red]Hello[/italic red] World!")
print("[bold red]alert![/bold red] Something happened")
print("[bold italic yellow on red blink]This text is impossible to read") # Supposed to blink?
print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]\n")

### Console API
my_console = Console()
print(my_console.size, my_console.encoding, my_console.is_terminal, my_console.color_system, "\n")

### Color systems
# None Disables color entirely.
# "auto" Will auto-detect the color system.
# "standard" Can display 8 colors, with normal and bright variations, for 16 colors in total.
# "256" Can display the 16 colors from “standard” plus a fixed palette of 240 colors.
# "truecolor" Can display 16.7 million colors, which is likely all the colors your monitor can display.
# "windows" Can display 8 colors in legacy Windows terminal. New Windows terminal can display “truecolor”.

### Logging
my_console.log("Test\n")  # Writes the time on the left and line on the right. Useful for debugging.

### Printing JSON
my_console.print_json('[false, true, null, "foo"]')

### Rules
my_console.rule("[bold red]Chapter 2")
my_console.rule("[bold red]Chapter 3", align="left")
