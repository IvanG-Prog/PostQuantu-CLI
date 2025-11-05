# src/postquantu_cli/encrypt_flow.py
import os
import click
from postquantu_cli.apis.sign_encrypt_client import sign_then_encrypt_file_client
from postquantu_cli.algo_functions.encrypt_algos import (
    kyber_function,
    ntru_function,
    saber_function,
)
from postquantu_cli.algo_functions.sign_algos import (
    Dilithium_function,
    falcon_function,
    sphincs_function,
)
from postquantu_cli.algo_functions.utils import (
    post_operation_menu,
    extract_file_id,
    error_operation_menu,
)


# ============ Main Encrypt Menu ============
@click.group()
@click.pass_context
def encrypt(ctx):
    """Handles encryption and signing operations."""
    click.echo("You are in the Encrypt menu.")

    if ctx.invoked_subcommand is None:
        while True:
            click.echo("---")
            click.echo("Which mode do you want to use?")
            click.echo("(1) Sign (DSA)")
            click.echo("(2) Sign and Encrypt (DSA & KEM) ")
            click.echo("(3) Encrypt (KEM)")
            click.echo("(4) Back to Main Menu")
            click.echo("---")

            try:
                choice = click.prompt(
                    "Please, enter the number of your choice", type=int
                )
            except click.exceptions.Abort:
                click.echo("Operation cancelled. Exiting Encrypt menu.")
                return

            if choice == 1:
                click.echo("You have chosen Sign (DSA)")
                ctx.invoke(sign_sub_menu)
                break

            elif choice == 2:
                click.echo("You have chosen Sign and Encrypt (DSA & KEM)")
                ctx.invoke(encrypt_and_sign_sub_menu)
                break

            elif choice == 3:
                click.echo("You have chosen Encrypt (KEM)")
                ctx.invoke(encrypt_sub_menu)
                break

            elif choice == 4:
                click.echo("Returning to Main Menu...")
                from postquantu_cli.cli import main_menu

                ctx.invoke(main_menu)
                return

            else:
                click.echo(
                    click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red")
                )


# ============ submenus and commands for signing ============


@encrypt.group()
@click.pass_context
def sign_sub_menu(ctx):
    """Displays algorithm choices for signing and handles file input."""

    click.echo("---")
    click.echo("Choose Signature (DSA) Algorithm:")
    click.echo("(1) CRYSTALS-DILITHIUM")
    click.echo("(2) FALCON")
    click.echo("(3) SPHINCS+")
    click.echo("(4) Back to Encrypt menu")
    click.echo("---")

    try:
        choice = click.prompt("Please, enter a number of your choice", type=int)
    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Encrypt menu.")
        return

    if choice == 1:
        click.echo("You have chosen Dilithium")
        ctx.invoke(Dilithium_function)
        return

    if choice == 2:
        click.echo("You have chosen FALCON")
        ctx.invoke(falcon_function)
        return

    if choice == 3:
        click.echo("You have chosen SPHINCS")
        ctx.invoke(sphincs_function)
        return

    if choice == 4:
        click.echo("Returning to Encrypt menu")
        ctx.invoke(encrypt)
        return

    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))


pass

sign_sub_menu.add_command(Dilithium_function)
sign_sub_menu.add_command(falcon_function)
sign_sub_menu.add_command(sphincs_function)

# ============ submenus and commands for sign and encrypt ============


@encrypt.group()
@click.pass_context
def encrypt_and_sign_sub_menu(ctx):
    """Signs a file with the selected DSA algorithm, then encrypts the result with the selected encryption algorithm.."""

    click.echo("---")
    click.echo("First, Choose Signature (DSA) Algorithm:")
    click.echo("(1) CRYSTALS-DILITHIUM")
    click.echo("(2) FALCON")
    click.echo("(3) SPHINCS+")
    click.echo("(4) Back to Encrypt Menu")
    click.echo("---")

    try:
        sign_choice = click.prompt("Please, enter the number of your signing algorithm choice", type=int)

    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Sign and Encrypt menu.")
        return

    sign_algo_name = ""
    sign_algo_id = ""

    if sign_choice == 1:
        sign_algo_name = "Dilithium"
        sign_algo_id = "1"

    elif sign_choice == 2:
        sign_algo_name = "FALCON"
        sign_algo_id = "2"

    elif sign_choice == 3:
        sign_algo_name = "SPHINCS"
        sign_algo_id = "3"

    elif sign_choice == 4:
        click.echo("Returning to Encrypt Menu...")
        ctx.invoke(encrypt)
        return
    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

        error_operation_menu(
            ctx, 
            repeat_callback=sign_sub_menu)

    click.echo(f"You have chosen  {sign_algo_name} for signing")

    click.echo("---")
    click.echo("Next, Choose Encryption (KEM) Algorithm:")
    click.echo("(1) CRYSTALS-KYBER")
    click.echo("(2) NTRU")
    click.echo("(3) SABER")
    click.echo("(4) Back to Encrypt Menu")
    click.echo("---")

    try:
        encrypt_choice = click.prompt("Please, enter the number of your encryption algorithm choice", type=int)

    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Sign and Encrypt menu.")
        return

    encrypt_algo_name = ""
    encrypt_algo_id = ""

    if encrypt_choice == 1:
        encrypt_algo_name = "KYBER"
        encrypt_algo_id = "1"

    elif encrypt_choice == 2:
        encrypt_algo_name = "NTRU"
        encrypt_algo_id = "2"

    elif encrypt_choice == 3:
        encrypt_algo_name = "SABER"
        encrypt_algo_id = "3"

    elif encrypt_choice == 4:
        click.echo("Returning to Encrypt Menu...")
        ctx.invoke(encrypt)
        return

    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))

    click.echo(f"You have chosen {encrypt_algo_name} for encryption.")

    file_path = click.prompt("Enter the path to the file to be signed and encrypted on your local computer")
    file_id = click.prompt("Enter the file ID (unique identifier for the file): ")

    #save_path = click.prompt("Enter path to save **Signed and Encrypted Files** on your local machine: ")

    if file_path.lower() == "cancel" :
        click.echo("Operation cancelled by user. Returning to Sign and Encrypt menu.")
        ctx.invoke(encrypt_and_sign_sub_menu)
        return

    #file_id = os.path.splitext(os.path.basename(file_path))[0]

    try:
        click.echo(f"Attempting to sign with {sign_algo_name} and encrypt with {encrypt_algo_name} file: '{file_path}'...")

        success, message, api_response_data = sign_then_encrypt_file_client(
            file_path, file_id, sign_algo_id, encrypt_algo_id
        )

        if success:
            click.echo(click.style(f"✅ Combined operation successful: {message}", fg="yellow"))

            encryption_details = api_response_data.get("Encryption Details", {})
            signing_details = api_response_data.get("Signing Details", {})
            if encryption_details:
                click.echo("===== Encryption Details =====".center(60))
                click.echo(click.style(f"  Encrypted File Name: {encryption_details.get('encrypted_file_name', '')}", fg="yellow"))
                click.echo(click.style(f"  Encrypted File Hash: {encryption_details.get('encrypted_file_hash', '')}", fg="yellow"))
                click.echo(click.style(f"  Private Decryption Key Name: {encryption_details.get('private_decryption_key_name', '')}", fg="yellow"))
                click.echo(click.style(f"  Private Decryption Key Hash: {encryption_details.get('private_decryption_key_hash', '')}", fg="yellow"))

            if signing_details:
                click.echo("===== Signing Details =====".center(60))
                click.echo(click.style(f"  Signature File Name: {signing_details.get('signature_file_name', '')}", fg="yellow"))
                click.echo(click.style(f"  Signature File Hash: {signing_details.get('signature_file_hash', '')}", fg="yellow"))
                click.echo(click.style(f"  Public Verification Key Name: {signing_details.get('public_verification_key_name', '')}", fg="yellow"))
                click.echo(click.style(f"  Public Verification Key Hash: {signing_details.get('public_verification_key_hash', '')}", fg="yellow"))
            
            post_operation_menu(
                ctx,
                repeat_callback=encrypt_and_sign_sub_menu,
                menu_option_text="Go back to Encrypt menu",
                menu_callback=encrypt,
            )

        else:
            click.echo(
                click.style(f"❌ Combined operation failed: {message}", fg="red")
            )
            error_operation_menu(ctx, repeat_callback=encrypt_and_sign_sub_menu)
        return

    except FileNotFoundError:
        click.echo(
            click.style(
                "Error: File not found at the specified path. Please try again.",
                fg="red",
            )
        )
        error_operation_menu(ctx, repeat_callback=encrypt_and_sign_sub_menu)
        return
    except Exception as e:
        click.echo(
            click.style(
                f"An unexpected error occurred during combined operation: {e}", fg="red"
            )
        )
        error_operation_menu(ctx, repeat_callback=encrypt_and_sign_sub_menu)
        file_id = extract_file_id(file_path)
        return


# ============ submenus and commands for encryption ============


@encrypt.group()
@click.pass_context
def encrypt_sub_menu(ctx):
    """Displays KEM algorithm choices for encryption and handles file input."""

    click.echo("---")
    click.echo("Choose Encryption (KEM) Algorithm:")
    click.echo("(1) CRYSTALS-KYBER ")
    click.echo("(2) NTRU")
    click.echo("(3) SABER")
    click.echo("(4) Back to Encrypt Menu")
    click.echo("---")

    try:
        choice = click.prompt("Please, enter the number of your choice", type=int)
    except click.exceptions.Abort:
        click.echo("Operation cancelled. Exiting Encrypt menu.")
        return

    if choice == 1:
        click.echo(" You have chosen KYBER")
        ctx.invoke(kyber_function)

    elif choice == 2:
        click.echo("You have chosen NTRU ")
        ctx.invoke(ntru_function)

    elif choice == 3:
        click.echo("You have chosen SABER")
        ctx.invoke(saber_function)

    elif choice == 4:
        click.echo("Returning to Encrypt Menu...")
        ctx.invoke(encrypt)
        return
    else:
        click.echo(click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red"))


pass


encrypt_sub_menu.add_command(ntru_function)
encrypt_sub_menu.add_command(kyber_function)
encrypt_sub_menu.add_command(saber_function)
