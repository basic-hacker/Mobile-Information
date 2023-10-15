import os

def install_required_libraries():
    print("Installing required libraries...")
    os.system("pip install -r requirements.txt")

if __name__ == "__main__":
    # Display the banner
    from banner import display_banner
    display_banner()

    # Install the required libraries
    install_required_libraries()
