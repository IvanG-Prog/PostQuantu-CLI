import click
from postquantu_cli.apis.decryption_client import decryption_file_client
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    error_operation_menu,
)

# ===========functions of decryption algorithms ===========


@click.command()
@click.pass_context
def kyber_decrypt_function(ctx):
    """Performs Kyber decryption using the API."""
    click.echo("Executing KYBER Decryption Function...")
    from postquantu_cli.cli_menus.decrypt_flow import decryption_sub_menu


    while True:
        file_path = click.prompt("Please write the route to your local file for KYBER decryption")
        private_decryption_key = click.prompt("Please write the route to your PRIVATE DECRYPTION KEY for KYBER decryption")
        save_path = click.prompt("Enter path to save **Decrypted Files** on your local machine")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel" or private_decryption_key.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=kyber_decrypt_function,
                error_message="Operation cancelled by user.",
            )
            return

        try:
            click.echo(f"Attempting to decrypt file: '{file_path}' using KYBER algorithm...")

            success, message, api_response_data = decryption_file_client(
                file_path, private_decryption_key, algo_id="1", save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Decryption successful: {message}", fg="yellow"))
                
                post_operation_menu(
                    ctx,
                    repeat_callback=kyber_decrypt_function,
                    menu_option_text="Go back to Decrypt Menu",
                    menu_callback=decryption_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Decryption failed: {message}", fg="red"))
                error_operation_menu(
                    ctx,
                    repeat_callback=kyber_decrypt_function
                )
                return

        except FileNotFoundError:
            error_operation_menu(
                ctx,
                repeat_callback=kyber_decrypt_function,
                error_message="File not found at the specified path.",
            )
            return
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=kyber_decrypt_function,
                error_message=f"An unexpected error occurred during decryption: {e}",
            )
            return


@click.command()
@click.pass_context
def ntru_decrypt_function(ctx):
    """Performs NTRU decryption using the API."""
    from postquantu_cli.cli_menus.decrypt_flow import decryption_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for NTRU decryption")
        save_path = click.prompt("Enter path to save **Decrypted Files** on your local machine")
        private_decryption_key = click.prompt("Please write the route to your PRIVATE DECRYPTION KEY for NTRU decryption")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel" or private_decryption_key.lower() == "cancel":
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to decrypt file: '{file_path}' using NTRU algorithm...")

            success, message, api_response_data = decryption_file_client(
                file_path, private_decryption_key, algo_id="2", save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Decryption successful: {message}", fg="yellow"))
                
                post_operation_menu(
                    ctx,
                    repeat_callback=ntru_decrypt_function,
                    menu_option_text="Go back to Decrypt Menu",
                    menu_callback=decryption_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Decryption failed: {message}", fg="red"))

                error_operation_menu(
                    ctx, 
                    repeat_callback=ntru_decrypt_function
                )
                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            return
        
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during decryption: {e}", fg="red"))
            return


@click.command()
@click.pass_context
def saber_decrypt_function(ctx):
    """Performs SABER decryption using the API."""
    from postquantu_cli.cli_menus.decrypt_flow import decryption_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for SABER decryption")
        private_decryption_key = click.prompt("Please write the route to your PRIVATE DECRYPTION KEY for SABER decryption")
        save_path = click.prompt("Enter path to save **Decrypted Files** on your local machine")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel":
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to decrypt file: '{file_path}' using SABER algorithm...")

            success, message, api_response_data = decryption_file_client(
                file_path, private_decryption_key, algo_id="3", save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Decryption successful: {message}", fg="yellow"))
                
                post_operation_menu(
                    ctx,
                    repeat_callback=saber_decrypt_function,
                    menu_option_text="Go back to Decrypt Menu",
                    menu_callback=decryption_sub_menu
                )
                return

            else:
                click.echo(click.style(f"❌ Decryption failed: {message}", fg="red"))

                error_operation_menu(
                    ctx, 
                    repeat_callback=saber_decrypt_function
                )
                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            return
        
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during decryption: {e}", fg="red"))
            return
