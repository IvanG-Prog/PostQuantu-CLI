import click
from postquantu_cli.apis.sign_client import sign_file_client
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    error_operation_menu,
)


# ============functions of sign algorithms ===========


@click.command()
@click.pass_context
def Dilithium_function(ctx):
    """Performs Dilithium sign using the API."""
    click.echo("Executing Dilithium Sign Function...")
    from postquantu_cli.cli_menus.encrypt_flow import sign_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for Dilithium Sign")
        file_id = click.prompt("Please enter a file ID for the Dilithium Sign")
        save_original_file = click.confirm("Do you want to save the original file?", default=True)

        if file_path.lower() == "cancel":
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to sign file: '{file_path}' using Dilithium algorithm...")

            success, message, api_response_data = sign_file_client(
                file_path, algo_id="1", file_id=file_id, save_original_file=save_original_file
            )

            if success:
                click.echo(click.style(f"✅ Sign successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx,
                    repeat_callback=Dilithium_function,
                    menu_option_text="Go back to Signature main menu",
                    menu_callback=sign_sub_menu,
                )
                return
            
            else:
                click.echo(click.style(f"❌ Sign failed: {message}", fg="red"))

                error_operation_menu(
                    ctx, 
                    repeat_callback=Dilithium_function
                    )
                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            error_operation_menu(ctx, repeat_callback=Dilithium_function)
            return
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during Sign: {e}", fg="red"))
            
            error_operation_menu(
                ctx,
                repeat_callback=Dilithium_function
            )
            return


@click.command()
@click.pass_context
def falcon_function(ctx):
    """Performs Falcon sign using the API."""
    click.echo("Executing Falcon Sign Function...")
    from postquantu_cli.cli_menus.encrypt_flow import sign_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for Falcon Sign")
        file_id = click.prompt("Please enter a file ID for the Falcon Sign")
        save_original_file = click.confirm("Do you want to save the original file?", default=True)

        if file_path.lower() == "cancel" :
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to sign file: '{file_path}' using Falcon algorithm...")

            success, message, api_response_data = sign_file_client(
                file_path, algo_id="2", file_id=file_id, save_original_file=save_original_file
            )

            if success:
                click.echo(click.style(f"✅ Sign successful: {message}", fg="yellow"))
                
                post_operation_menu(
                    ctx,
                    repeat_callback=falcon_function,
                    menu_option_text="Go back to Signature main menu",
                    menu_callback=sign_sub_menu,
                )
                return
            else:
                click.echo(click.style(f"❌ Sign failed: {message}", fg="red"))
                error_operation_menu(ctx, repeat_callback=falcon_function)
                return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
            
            error_operation_menu(
                ctx,
                repeat_callback=falcon_function
            )
            return
        
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during Sign: {e}", fg="red"))
            
            error_operation_menu(
                ctx,
                repeat_callback=falcon_function
            )
            return


@click.command()
@click.pass_context
def sphincs_function(ctx):
    """Performs SPHINCS sign using the API."""
    click.echo("Executing SPHINCS Sign Function...")
    from postquantu_cli.cli_menus.encrypt_flow import sign_sub_menu

    while True:
        file_path = click.prompt("Please write the route to your local file for SPHINCS Sign")
        file_id = click.prompt("Please enter a file ID for the SPHINCS Sign")
        save_original_file = click.confirm("Do you want to save the original file?", default=True)

        if file_path.lower() == "cancel" :
            click.echo("Operation cancelled by user. Returning to Encrypt menu.")
            return

        try:
            click.echo(f"Attempting to sign file: '{file_path}' using SPHINCS algorithm...")

            success, message, api_response_data = sign_file_client(
                file_path, algo_id="3", file_id=file_id, save_original_file=save_original_file
            )

            if success:
                click.echo(click.style(f"✅ Sign successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx,
                    repeat_callback=sphincs_function,
                    menu_option_text="Go back to Signature main menu",
                    menu_callback=sign_sub_menu,
                )
                return

            else:
                click.echo(click.style(f"❌ Sign failed: {message}", fg="red"))

                error_operation_menu(
                    ctx, 
                    repeat_callback=sphincs_function
                    )
            return

        except FileNotFoundError:
            click.echo(click.style("Error: File not found at the specified path. Please try again.", fg="red"))
           
            error_operation_menu(
                ctx,
                repeat_callback=sphincs_function
            )
            return
        
        except Exception as e:
            click.echo(click.style(f"An unexpected error occurred during Sign: {e}", fg="red"))
            
            error_operation_menu(
                ctx,
                repeat_callback=sphincs_function
            )
            return
