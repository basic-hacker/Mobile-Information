import shutil
from colorama import Fore, Style

# Define the ASCII art for the "Basic-Hacker" banner
banner = r"""
 ________  ________  ________  ___  ________                ___  ___  ________  ________  ___  __    _______   ________     
|\   __  \|\   __  \|\   ____\|\  \|\   ____\              |\  \|\  \|\   __  \|\   ____\|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \|\ /\ \  \|\  \ \  \___|\ \  \ \  \___|  ____________\ \  \\\  \ \  \|\  \ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \   __  \ \   __  \ \_____  \ \  \ \  \    |\____________\ \   __  \ \   __  \ \  \    \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \ \  \|____|\  \ \  \ \  \___\|____________|\ \  \ \  \ \  \ \  \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\____\_\  \ \__\ \_______\             \ \__\ \__\ \__\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\_________\|__|\|_______|              \|__|\|__|\|__|\|__|\|_______|\|__| \|__|\|_______|\|__|\|__|
                       \|_________|                                                                                         
"""

# Get the terminal width
terminal_width, _ = shutil.get_terminal_size()

# Define the color for the banner text
color = Fore.GREEN

# Calculate the number of spaces needed to center the banner
num_spaces = (terminal_width - max(len(line) for line in banner.split('\n'))) // 2

# Print the banner with the defined color and centering spaces
for line in banner.split('\n'):
    print(' ' * num_spaces + color + line + Style.RESET_ALL)
