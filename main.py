# main.py


import typer

app = typer.Typer()


@app.command(name="greetings", help="Greet someone")
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(
    name: str = typer.Argument("typer"),
    formal: bool = typer.Option(False, help="Prefers a formal prefix."),
):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}")


if __name__ == "__main__":
    app()
