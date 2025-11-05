import os
import click
from postquantu_cli.apis.verify_client import verify_file_client
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    error_operation_menu,
)

# ===========functions of verification algorithms ===========


@click.command()
@click.pass_context
def Dilithium_verify_function(ctx):
    """Performs Dilithium verification using the API."""
    click.echo("Executing DILITHIUM Verification Function...")
    from postquantu_cli.cli_menus.decrypt_flow import verify_sub_menu


    while True:
        file_path = click.prompt("Please write the route to your local signature file for DILITHIUM verification")
        public_key_path = click.prompt("Please write the route to your PUBLIC KEY for DILITHIUM verification")
        file_id = click.prompt("Please enter the file ID used during signing")
        original_file = click.prompt("Please write the route to your ORIGINAL if it has not been saved", default="", show_default=False)
        if not original_file.strip():
            original_file = None
        save_path = click.prompt("Enter path to save **Verified Files** on your local machine")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel" or public_key_path.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=Dilithium_verify_function,
                error_message="Operation cancelled by user.",
            )
            return

        try:
            click.echo(f"Attempting to verify file: '{file_path}' using Dilithium algorithm...")

            success, message, api_response_data = verify_file_client(
                 file_path=file_path, public_verification_key=public_key_path,file_id=file_id, 
                 algo_id="1", original_file=original_file, save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Verification successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx,
                    repeat_callback=Dilithium_verify_function,
                    menu_option_text="Go back to Verify Menu",  
                    menu_callback=verify_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Verification failed: {message}", fg="red"))
                error_operation_menu(
                    ctx,
                    repeat_callback=Dilithium_verify_function
                )
                return

        except FileNotFoundError:
            error_operation_menu(
                ctx,
                repeat_callback=Dilithium_verify_function,
                error_message="File not found at the specified path.",
            )
            return
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=Dilithium_verify_function,
                error_message=f"An unexpected error occurred during Verification: {e}",
            )
            return


@click.command()
@click.pass_context
def falcon_verify_function(ctx):
    """Performs Falcon verification using the API."""
    click.echo("Executing FALCON Verification Function...")
    from postquantu_cli.cli_menus.decrypt_flow import verify_sub_menu


    while True:
        file_path = click.prompt("Please write the route to your local signature file for FALCON verification")
        public_key_path = click.prompt("Please write the route to your PUBLIC KEY for FALCON verification")
        file_id = click.prompt("Please enter the file ID used during signing")
        original_file = click.prompt("Please write the route to your ORIGINAL file if it has been saved", default="", show_default=False)
        if not original_file.strip():
            original_file = None
        save_path = click.prompt("Enter path to save **Verified Files** on your local machine")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel" or public_key_path.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=falcon_verify_function,
                error_message="Operation cancelled by user.",
            )
            return

        try:
            click.echo(f"Attempting to decrypt file: '{file_path}' using FALCON algorithm...")

            success, message, api_response_data = verify_file_client(
                file_path,public_key_path,file_id,
                  algo_id="2", original_file=original_file, save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Verification successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx,
                    repeat_callback=falcon_verify_function,
                    menu_option_text="Go back to Verify Menu",
                    menu_callback=verify_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Verification failed: {message}", fg="red"))
                error_operation_menu(
                    ctx,
                    repeat_callback=falcon_verify_function
                )
                return

        except FileNotFoundError:
            error_operation_menu(
                ctx,
                repeat_callback=falcon_verify_function,
                error_message="File not found at the specified path.",
            )
            return
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=falcon_verify_function,
                error_message=f"An unexpected error occurred during Verification: {e}",
            )
            return



@click.command()
@click.pass_context
def sphincs_verify_function(ctx):
    """Performs SPhincs verification using the API."""
    click.echo("Executing SPHINCS Verification Function...")
    from postquantu_cli.cli_menus.decrypt_flow import verify_sub_menu


    while True:
        file_path = click.prompt("Please write the route to your local signature file for SPHINCS verification")
        public_key_path = click.prompt("Please write the route to your PUBLIC KEY for SPHINCS verification")
        file_id = click.prompt("Please enter the file ID used during signing")
        original_file = click.prompt("Please write the route to your ORIGINAL file if it has been saved", default="", show_default=False)
        if not original_file.strip():
            original_file = None
        save_path = click.prompt("Enter path to save **Verified Files** on your local machine")

        if file_path.lower() == "cancel" or save_path.lower() == "cancel" or public_key_path.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=falcon_verify_function,
                error_message="Operation cancelled by user.",
            )
            return
        try:
            click.echo(f"Attempting to decrypt file: '{file_path}' using SPHINCS algorithm...")

            success, message, api_response_data = verify_file_client(
                file_path, public_key_path, file_id,
                algo_id="3", original_file=original_file, save_path=save_path
            )

            if success:
                click.echo(click.style(f"✅ Verification successful: {message}", fg="yellow"))

                post_operation_menu(
                    ctx,
                    repeat_callback=sphincs_verify_function,
                    menu_option_text="Go back to Verify Menu",
                    menu_callback=verify_sub_menu
                )
                return
            else:
                click.echo(click.style(f"❌ Verification failed: {message}", fg="red"))
                error_operation_menu(
                    ctx,
                    repeat_callback=sphincs_verify_function
                )
                return

        except FileNotFoundError:
            error_operation_menu(
                ctx,
                repeat_callback=sphincs_verify_function,
                error_message="File not found at the specified path.",
            )
            return
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=sphincs_verify_function,
                error_message=f"An unexpected error occurred during Verification: {e}",
            )
            return
