import click 
from pyfiglet import Figlet
from random import randrange

@click.group()
@click.version_option(version='0.01', prog_name='decotext')
def main():
    """DECOTEXT"""
    pass


@main.command()
@click.option('--input', '-i', default="SAURAV GUJJAR", help="give text to decorate.")
def decorate(input):
    """Decorate tour Text"""
    f = Figlet(font='slant')
    color = ''
    if randrange(1,3) == 1:
        color = 'green'
    elif randrange(1,3) == 2:
        color = 'red'
    else:
        color = 'white'
    click.secho(f.renderText(input), fg=color)


if __name__ == "__main__":
    main()