import click
from methods.bilinear_interp_increase import bilinear_interpolation
from methods.bilinear_interp_decrease import bilinear_interpolation_downscale

from . import __version__

@click.command()
@click.version_option(version=__version__)
#required=True-эта опция обязательна
#exists=True - путь должен существовать
@click.option('--input', '-i', required=True, type=click.Path(exists=True), help='Path to the input image')
@click.option('--output', '-o', required=True, type=click.Path(), help='Path to save the output image')
@click.option('--algorithm', '-a', type=click.Choice(['increase_size', 'decrease_size']), default='increase_size', help='Interpolation algorithm')

def main(input, output, algorithm):
    if algorithm == 'increase_size':
        bilinear_interpolation(input, output)
        click.echo("Image was interpolated")
    elif algorithm == 'decrease_size':
        bilinear_interpolation_downscale(input, output)
        click.echo("Image was interpolated")