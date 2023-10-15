import shutil
from colorama import Fore, Style

# Define the ASCII art for the "Basic-Hacker" banner
banner = r""" 
 __        __     __          
|__)  /\  /__` | /  `    __   
|__) /~~\ .__/ | \__,         
                              
           __        ___  __  
|__|  /\  /  ` |__/ |__  |__) 
|  | /~~\ \__, |  \ |___ |  \ 
                                                                                                        
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
