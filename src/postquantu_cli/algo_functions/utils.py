import click
import sys


def post_operation_menu(
    ctx,
    repeat_callback=None,
    HashToken=None,
    custom_message=None,
    menu_option_text="Go back to Encrypt main menu",
    menu_callback=None,
):

    while True:
        if custom_message:
            click.echo(custom_message)
        else:
            click.echo(
                f"""              


"""
            )

        click.echo("--- Operation Completed ---")
        click.echo("What would you like to do next?")
        click.echo("(1) Perform another operation")
        click.echo(f"(2) {menu_option_text}")
        click.echo("(3) Return to main menu")
        click.echo("(4) Exit the program")
        click.echo("---")

        try:
            next_action_choice = click.prompt(
                "Please, enter the number of your choice", type=int
            )
        except click.exceptions.Abort:
            click.echo("Operation cancelled. Exiting program.")
            ctx.exit()
            return

        if next_action_choice == 1 and repeat_callback:
            click.echo("Returning for another operation...")
            ctx.invoke(repeat_callback)
            return
        elif next_action_choice == 2:
            click.echo(f"Returning to {menu_option_text}...")
            if menu_callback:
                ctx.invoke(menu_callback)
                return
        elif next_action_choice == 3:
            from postquantu_cli.cli import main_menu

            click.echo("Returning to main menu...")
            ctx.invoke(main_menu)
            return
        elif next_action_choice == 4:
            click.echo("Exiting program. Goodbye! 👋")
            sys.exit(0)
            return
        else:
            click.echo(
                click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red")
            )


def error_operation_menu(ctx, repeat_callback=None, error_message="An error occurred."):
    # click.echo(click.style(f"\n❌ {error_message}\n", fg="red"))
    while True:
        click.echo(
            f"""

--- Error Handling ---"""
        )
        click.echo("What would you like to do next?")
        click.echo("(1) Try the operation again")
        click.echo("(2) Go back to previous main menu")
        click.echo("(3) Return to main menu")
        click.echo("(4) Exit the program")
        click.echo("---")
        try:
            next_action_choice = click.prompt(
                "Please, enter the number of your choice", type=int
            )
        except click.exceptions.Abort:
            click.echo("Operation cancelled. Exiting program.")
            ctx.exit()
            return
        if next_action_choice == 1 and repeat_callback:
            click.echo("Trying the operation again...")
            ctx.invoke(repeat_callback)
            return
        elif next_action_choice == 2:
            click.echo("Returning to Encrypt main menu...")
            
        elif next_action_choice == 3:   
            from postquantu_cli.cli import main_menu
            click.echo("Returning to main menu...")
            ctx.invoke(main_menu)
            return
        elif next_action_choice == 4:
            click.echo("Exiting program. Goodbye! 👋")
            ctx.exit()
            return
        else:
            click.echo(
                click.style("Invalid option. Please, enter 1, 2, 3 or 4.", fg="red")
            )


def extract_file_id(file_path):
    import os

    return os.path.splitext(os.path.basename(file_path))[0]
