# ClickUtils

    Extra utils for click library

# Examples

    Loading click groups and commands from filepath or directory

    Directory structure
    _ cwd
     |_ __init__.py (contains code below)
     |_ plugins/
       |_ group_or_command_folder
         |_ *groups (this folder must exists to find click groups or commands)
           |_ __init__.py (any click groups or commands will be pulled from this location)
       ...
    

```python
import os
import click

from clickutils import click_loader


@click.group()
@click.option('--verbose', '-v', type=bool, is_flag=True, default=False,
    help='Print more verbose output')
def cli(verbose: bool):
    '''click_plugins'''
    click_loader.load(plugins_group, os.path.dirname(os.path.abspath(__file__)), verbose=verbose)

@click.group()
def plugins_group():
    '''click_plugins test plugins'''
    pass

cli.add_command(plugins_group, name='plugins')


if __name__ == '__main__':
    cli()
```


Same example using decorator
```python
import os
import click

from clickutils import click_loader


@click.group()
def cli(verbose: bool):
    '''click_plugins'''

@click_loader.group(os.path.dirname(os.path.abspath(__file__)), name='plugins')
def plugins_group():
    '''click_plugins test plugins'''
    pass

cli.add_command(plugins_group)


if __name__ == '__main__':
    cli()
```

