from sys import platform
import sys
import click
from postquantu_cli.algo_functions.download_algo import download_encrypted_file_function
from postquantu_cli.cli_menus.encrypt_flow import encrypt
from postquantu_cli.cli_menus.decrypt_flow import decrypt

BANNER = r"""
__        __   _                            _         
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  

               P O S T Q U A N T U
"""


@click.group(invoke_without_command=True)
@click.pass_context
def postquantu(ctx):
    """
    Welcome to PostQuantu CLI.
    This is the main entry point for your post- quantum cryptography operations.
    """

    if ctx.invoked_subcommand is None:
        ctx.invoke(main_menu)


@click.command()
@click.pass_context
def main_menu(ctx):
    """
    Displays the main interactive menu for POSTQUANTU CLI.
    """
    click.echo(click.style(BANNER, fg="yellow"))
    welcome_msg = """
🛡️ **POSTQUANTU CLI: Post-Quantum Security Solution.**
----------------------------------------------------------------------
This Command Line Interface (CLI) is engineered to provide robust, future-proof
security capabilities for mission-critical applications.

**PostQuantu** utilizes leading **NIST-standardized** Post-Quantum Cryptography (PQC) 
algorithms—including **Kyber** (Key Encapsulation) and **Dilithium** (Digital Signatures)—
to ensure comprehensive protection against large-scale quantum computing threats.

**Secure Operations:**
* **Confidentiality:** Utilizing PQC for secure data encryption.
* **Integrity:** Ensuring data authenticity and non-repudiation.
* **Resilience:** Built for deployment into production environments.

For technical documentation and integration support:
---
"""
    click.echo(click.style(welcome_msg, fg="green"))

    while True:
        click.echo("---")
        click.echo("Which main operation do you want to perform?")
        click.echo("(1) 🔐 Encrypt (Sign, Sign & Encrypt, Encrypt)")
        click.echo("(2) 🔓 Decrypt (Verify, Verify & Decrypt, Decrypt)")
        click.echo("(3) 📥 Download files from previous operations.")
        click.echo("(4) ❌ Exit")
        click.echo("---")

        try:
            choice = click.prompt("Please, enter the number of your choice", type=int)
        except click.exceptions.Abort:
            click.echo("\nOperation cancelled. Exiting.")
            return

        if choice == 1:
            click.echo("\nYou have chosen Encrypt. Entering Encrypt menu...")
            ctx.invoke(encrypt)
            break
        elif choice == 2:
            click.echo("\nYou have chosen Decrypt. Entering Decrypt menu...")
            ctx.invoke(decrypt)
            break
        elif choice == 3:
            click.echo("\nYou have chosen Download. Entering Download menu...")
            ctx.invoke(download_encrypted_file_function)
            break
        elif choice == 4:
            click.echo("Exiting POSTQUANTU CLI. Goodbye!")
            sys.exit(0)
        else:
            click.echo(click.style("Invalid option. Please, enter 1, 2, 3, or 4.", fg="red"))


postquantu.add_command(main_menu)
postquantu.add_command(encrypt)
postquantu.add_command(decrypt)

if __name__ == "__main__":
   try:
        postquantu() 
   
   except Exception as e:
       print(f"An unexpected error occurred: {e}", file=sys.stderr)

   finally:
       if len(sys.argv) == 1 and platform.system() == "Windows":
            print("\n-------------------------------------------------------------")
            print("Program finished. Press ENTER to close this window...")
            print("-------------------------------------------------------------")
            input()