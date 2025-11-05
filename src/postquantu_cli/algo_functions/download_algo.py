import click
from postquantu_cli.apis.download_client import download_encrypted_file
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    error_operation_menu,
)

@click.command()
@click.pass_context
def download_encrypted_file_function(ctx):
    """Downloads an encrypted file from the API."""
    click.echo("Executing Download Encrypted File Function...")

    while True:
        file_path = click.prompt("Enter the name of the  file to download")
        #file_name = click.prompt("Enter the name to save the downloaded file as")
        save_path = click.prompt("Enter the folder to save the downloaded file")


        '''if file_name.lower() == "cancel" or save_path.lower() == "cancel":
            error_operation_menu(
                ctx,
                repeat_callback=download_encrypted_file_function,
                error_message="Operation cancelled by user.",
            )
            return'''

        try:
            success, message = download_encrypted_file(file_path, save_path)
            if success:
                click.echo(click.style(f"✅ Download successful: {message}", fg="yellow"))
                post_operation_menu(
                    ctx, 
                    repeat_callback=download_encrypted_file_function,
                    menu_option_text="Go back to main menu",
                    menu_callback=None  
                )
                return
            
            else:
                click.echo(click.style(f"❌ Download failed: {message}", fg="red"))
                error_operation_menu(
                    ctx, 
                    repeat_callback=download_encrypted_file_function)
                return
            
        except Exception as e:
            error_operation_menu(
                ctx,
                repeat_callback=download_encrypted_file_function,
                error_message=f"An unexpected error occurred during download: {e}",
            )
            return