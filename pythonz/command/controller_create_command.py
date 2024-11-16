import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='controller:create'
)
def controller_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    controller_name = click.prompt('Enter the name of the controller es. PostController')
    pythonz_manager.generate_class(controller_name, 'controller')
    click.echo('Created controller successfully')
