import click
import os
from postquantu_cli.algo_functions.utils import post_operation_menu
from postquantu_cli.algo_functions.utils import error_operation_menu
from postquantu_cli.apis.descrypt_verify_client import decrypt_then_verify_file_client
from postquantu_cli.algo_functions.decryption_algos import (
    kyber_decrypt_function,
    ntru_decrypt_function,
    saber_decrypt_function,
)
from postquantu_cli.algo_functions.verify_algos import (
    Dilithium_verify_function,
    falcon_verify_function,
    sphincs_verify_function,
)


# -------------------------------------------------------------------#
# ---             MAIN COMMAND: DECRYPT                            ---#
# -------------------------------------------------------------------#


@click.group()
@click.pass_context
def decrypt(ctx):
    """Handles verification and decryption operations."""
    click.echo("You are in the Decrypt menu.")

    if ctx.invoked_subcommand is None:
        while True:
            click.echo("---")
            click.echo("Which mode do you want to use?")
            click.echo("(1) Decryption")
            click.echo("(2) Verify")
            click.echo("(3) Decryption and Verify")
            click.echo("(4) Back to Main Menu")
            click.echo("---")

            try:
                choice = click.prompt(
                    "Please, enter the number of your choice", type=int
                )
            except click.exceptions.Abort:
                click.echo("\nOperation cancelled. Exiting Decrypt menu.")
                return

            if choice == 1:
                click.echo(" You have chosen Decryption")
                ctx.invoke(decryption_sub_menu)
                break

            elif choice == 2:
                click.echo("You have chosen Verify ")
                ctx.invoke(verify_sub_menu)
                break
            elif choice == 3:
                click.echo("You have chosen Verify and Decryption ")
                ctx.invoke(verify_and_decryption_sub_menu)
                break
            elif choice == 4:
                from postquantu_cli.cli import main_menu
                click.echo("Returning to Main Menu...")
                ctx.invoke(main_menu)
                return
            else:
                click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

                error_operation_menu(
                    ctx,
                    repeat_callback=decryption_sub_menu
                )
                return


# ----------------------------------------------#
# ---     Subgroups and specific commands of DECRYPT          ---#
# ---------------------------------------------------------------#


@decrypt.group()
@click.pass_context
def decryption_sub_menu(ctx):
    """Performs decryption."""

   
    click.echo("---")
    click.echo('Chose Decryption (KEN) Algorithm')
    click.echo("(1) CRYSTALS-KYBER ")
    click.echo("(2) NTRU")
    click.echo("(3) SABER")
    click.echo("(4) Back to Decrypt Menu")
    click.echo("---")

    try:
        choice = click.prompt("Please, enter the number of your choice", type=int)
    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Encrypt menu.")
        return

    if choice == 1:
        click.echo(" You have chosen KYBER")
        ctx.invoke(kyber_decrypt_function)

    elif choice == 2:
        click.echo("You have chosen NTRU ")
        ctx.invoke(ntru_decrypt_function)

    elif choice == 3:
        click.echo("You have chosen SABER")
        ctx.invoke(saber_decrypt_function)

    elif choice == 4:
        click.echo("Returning to Decrypt Menu...")
        ctx.invoke(decrypt)
        return
    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

        error_operation_menu(
            ctx,
            repeat_callback=decryption_sub_menu
        )
        return


pass

decryption_sub_menu.add_command(kyber_decrypt_function)
decryption_sub_menu.add_command(ntru_decrypt_function)
decryption_sub_menu.add_command(saber_decrypt_function)





@decrypt.command()
@click.pass_context
def verify_sub_menu(ctx):
    """Performs verification."""
     
    click.echo("---")
    click.echo('Chose Verification (DAS) Algorithm')
    click.echo("(1) CRYSTALS-Dilithium ")
    click.echo("(2) Falcon")
    click.echo("(3) SPHINCS+")
    click.echo("(4) Back to Decrypt Menu")
    click.echo("---")

    try:
        choice = click.prompt("Please, enter the number of your choice", type=int)
    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting decrypt menu.")
        return

    if choice == 1:
        click.echo(" You have chosen Dilithium")
        ctx.invoke(Dilithium_verify_function)

    elif choice == 2:
        click.echo("You have chosen Falcon ")
        ctx.invoke(falcon_verify_function)

    elif choice == 3:
        click.echo("You have chosen SPHINCS+")
        ctx.invoke(sphincs_verify_function)

    elif choice == 4:
        click.echo("Returning to Verify Menu...")
        ctx.invoke(decrypt)
        return
    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

        error_operation_menu(
            ctx,
            repeat_callback=decryption_sub_menu
        )
        return

pass

decryption_sub_menu.add_command(Dilithium_verify_function)
decryption_sub_menu.add_command(falcon_verify_function)
decryption_sub_menu.add_command(sphincs_verify_function)



@decrypt.command()
@click.pass_context
def verify_and_decryption_sub_menu(ctx):
    """Performs verification and decryption."""

    click.echo("---")
    click.echo("Next, Choose Decryption (KEM) Algorithm:")
    click.echo("(1) CRYSTALS-KYBER")
    click.echo("(2) NTRU")
    click.echo("(3) SABER")
    click.echo("(4) Back to Decrypt Menu")
    click.echo("---")

    try:
        decrypt_choice = click.prompt("Please, enter the number of your decryption algorithm choice", type=int)

    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Sign and Encrypt menu.")
        return

    decrypt_algo_name = ""
    decrypt_algo_id = ""

    if decrypt_choice == 1:
        decrypt_algo_name = "KYBER"
        decrypt_algo_id = "1"

    elif decrypt_choice == 2:
        decrypt_algo_name = "NTRU"
        decrypt_algo_id = "2"

    elif decrypt_choice == 3:
        decrypt_algo_name = "SABER"
        decrypt_algo_id = "3"

    elif decrypt_choice == 4:
        click.echo("Returning to Decrypt Menu...")
        ctx.invoke(decrypt)
        return

    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

        error_operation_menu(
            ctx,
            repeat_callback=decryption_sub_menu
        )
        return

    click.echo(f"You have chosen {decrypt_algo_name} for decryption.")  


    click.echo("---")
    click.echo("First, Choose Signature (DSA) Algorithm:")
    click.echo("(1) CRYSTALS-DILITHIUM")
    click.echo("(2) FALCON")
    click.echo("(3) SPHINCS+")
    click.echo("(4) Back to Decrypt Menu")
    click.echo("---")

    try:
        verify_choice = click.prompt("Please, enter the number of your verification algorithm choice", type=int)

    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Sign and Encrypt menu.")
        return

    verify_algo_name = ""
    verify_algo_id = ""

    if verify_choice == 1:
        verify_algo_name = "Dilithium"
        verify_algo_id = "1"

    elif verify_choice == 2:
        verify_algo_name = "FALCON"
        verify_algo_id = "2"

    elif verify_choice == 3:
        verify_algo_name = "SPHINCS"
        verify_algo_id = "3"

    elif verify_choice == 4:
        click.echo("Returning to Decrypt Menu...")
        ctx.invoke(decrypt)
        return
    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

        error_operation_menu(
            ctx,
            repeat_callback=decryption_sub_menu
        )
        return

    click.echo(f"You have chosen  {verify_algo_name} for verification")


    encrypted_file = click.prompt("Enter the path to the encrypted file on your local computer")
    private_decryption_key = click.prompt("Enter the path to the private decryption key file on your local computer")
    signature_file = click.prompt("Enter the path to the signature file on your local computer")
    public_verification_key = click.prompt("Enter the path to the public verification key file on your local computer")
    file_id = click.prompt("Enter the file ID (unique identifier for the file): ")
    save_path = click.prompt("Enter path to save **Decrypted and Verified File** on your local machine: ")


    if encrypted_file.lower() == "cancel" or signature_file.lower() == "cancel":
        click.echo("Operation cancelled by user. Returning to Sign and Decrypt menu.")
        ctx.invoke(verify_and_decryption_sub_menu)
        return

    if private_decryption_key.lower() == "cancel" or public_verification_key.lower() == "cancel":
        click.echo("Operation cancelled by user. Returning to Sign and Decrypt menu.")
        ctx.invoke(verify_and_decryption_sub_menu)
        return
    
    #file_id = os.path.splitext(os.path.basename(encrypted_file))[0]

    try:
        click.echo(f"Attempting to decrypt with {decrypt_algo_name} and verify with {verify_algo_name} file: '{encrypted_file}'...")

        success, message, api_response_data = decrypt_then_verify_file_client(
            encrypted_file, private_decryption_key, signature_file, 
            public_verification_key, file_id, verify_algo_id, decrypt_algo_id, save_path
        )

        if success:
            click.echo(click.style(f"✅ Combined operation successful: {message}", fg="green"))
            ctx.invoke(post_operation_menu(
                ctx,
                repeat_callback=verify_and_decryption_sub_menu,
                menu_option_text="Go back to Decrypt Menu",
                menu_callback=decrypt
            ))

            # Handle successful response
        else:
            click.echo(click.style(f"❌ Combined operation failed: {message}", fg="red"))
            error_operation_menu(
                ctx,
                repeat_callback=verify_and_decryption_sub_menu
            )
        return
    

    except FileNotFoundError:
        click.echo(
            click.style("Error: File not found at the specified path. Please try again.", fg="red"))
        
        error_operation_menu(
            ctx,
            repeat_callback=verify_and_decryption_sub_menu
        )
        return
    
    except Exception as e:
        click.echo(click.style(f"An unexpected error occurred during combined operation: {e}", fg="red"))
        error_operation_menu(
            ctx,
            repeat_callback=verify_and_decryption_sub_menu
        )
        #file_id = extract_file_id(file_path)
        return
