import os
import re
import click

from clickutils import click_loader


@click.group()
@click.option('--verbose', '-v', type=bool, is_flag=True, default=False,
    help='Print more verbose output')
def cli(verbose: bool):
    '''click_plugins'''
    click_loader.load_commands_from_directory(plugins_group, 'plugins', verbose=verbose)

@click.group()
def plugins_group():
    '''click_plugins test plugins'''
    pass

cli.add_command(plugins_group, name='plugins')


if __name__ == '__main__':
    cli()