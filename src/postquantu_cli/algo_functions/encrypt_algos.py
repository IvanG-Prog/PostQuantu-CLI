import click
from postquantu_cli.apis.encryption_client import encrypt_file_client
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    error_operation_menu,
)

# ===========functions of encryption algorithms ===========


@click.command()
@click.pass_context
def kyber_function(ctx):
    """Performs Kyber encryption using the API."""
    click.echo("Executing KYBER Encryption Function...")
    from postquantu_cli.cli_menus.encrypt_flow import encrypt_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for KYBER encryption")
        file_id = click.prompt("Please provide a file ID (optional)")
        #save_path = click.prompt("Enter path to save **Encrypted Files** on your local machine")

        if file_path.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=kyber_function,
                error_message="Operation cancelled by user.",
            )
            return

        try:
            click.echo(f"Attempting to encrypt file: '{file_path}' using KYBER algorithm...")

            success, message, api_response_data = encrypt_file_client(
                file_path, file_id, algo_id="1"
            )

            if success:
                click.echo(click.style(f"✅ Encryption successful: {message}", fg="yellow"))

                post_operation_menu(ctx, repeat_callback=kyber_function, menu_callback=encrypt_sub_menu)
                return
            else:
                click.echo(click.style(f"❌ Encryption failed: {message}", fg="red"))
                error_operation_menu(
                    ctx,
                    repeat_callback=kyber_function
                )
                return

        except FileNotFoundError:
            error_operation_menu(
                ctx,
                repeat_callback=kyber_function,
                error_message="File not found at the specified path.",
            )
            return
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=kyber_function,
                error_message=f"An unexpected error occurred during encryption: {e}",
            )
            return


@click.command()
@click.pass_context
def ntru_function(ctx):
    """Performs NTRU encryption using the API."""
    from postquantu_cli.cli_menus.encrypt_flow import encrypt_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for NTRU encryption")
        file_id = click.prompt("Please provide a file ID (optional)")

        #save_path = click.prompt("Enter path to save **Encrypted Files** on your local machine")

        if file_path.lower() == "cancel":
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to encrypt file: '{file_path}' using NTRU algorithm...")

            success, message, api_response_data = encrypt_file_client(
                file_path, file_id, algo_id="2"
            )

            if success:
                click.echo(click.style(f"✅ Encryption successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx, repeat_callback=ntru_function, menu_callback=encrypt_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Encryption failed: {message}", fg="red"))
                
                error_operation_menu(
                    ctx,
                    repeat_callback=ntru_function
                )
                return

                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            return
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during encryption: {e}", fg="red"))
            return


@click.command()
@click.pass_context
def saber_function(ctx):
    """Performs SABER encryption using the API."""
    from postquantu_cli.cli_menus.encrypt_flow import encrypt_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for SABER encryption")
        file_id = click.prompt("Please provide a file ID (optional)")
        #save_path = click.prompt("Enter path to save **Encrypted Files** on your local machine")

        if file_path.lower() == "cancel":
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to encrypt file: '{file_path}' using SABER algorithm...")

            success, message, api_response_data = encrypt_file_client(
                file_path, file_id, algo_id="3"
            )

            if success:
                click.echo(click.style(f"✅ Encryption successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx, repeat_callback=saber_function, menu_callback=encrypt_sub_menu
                )
                return

            else:
                click.echo(click.style(f"❌ Encryption failed: {message}", fg="red"))

                error_operation_menu(
                    ctx,
                    repeat_callback=saber_function
                )
                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            return
        
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during encryption: {e}", fg="red"))
            return
