# File: main.py
# Purpose: install missing packages using the pip command line and 
# sets up the jupyter notebook server for visualization.

from __future__ import annotations
from signal import SIGINT
from signal import signal
from subprocess import CalledProcessError
from subprocess import check_call
from subprocess import run
from sys import executable

# If requirements.txt is updated, please update this list too
PACKAGES = ['jupyter', 'pandas', 'matplotlib', 'd3graph', 'plotly']

def install(package: str) -> None:
    ''' 
    Attempt to install package by creating a subprocess
    to execute a command with the pip command line tool.
    '''
    try:
        check_call([executable, '-m', 'pip', 'install', package])
    except CalledProcessError:
        print(f'Could not install {package}.')
    except:
        print('Something went wrong.')

def installed(package: str, environment: List[str]) -> bool:
    '''
    Return True if the package is installed on the machine.
    '''
    return package in environment

def get_environment() -> List[str]:
    '''
    Return the list of packages that are currently installed by the
    host machine (also known as the environment).
    '''
    environment = []
    result = run(['pip', 'list'], capture_output = True, text = True)
    packages = result.stdout.split('\n')
    packages.pop() # Remove the entry that only contains a newline
    for package in reversed(packages):
        if package[0] == '-': # Stop when at the divider line
            break
        environment.append(package.split(' ')[0])
    return environment

def check_packages() -> None:
    '''
    Check that all required packages are properly installed.
    If a package is not installed, install them.
    '''
    environment = get_environment()
    for package in PACKAGES:
        if not installed(package, environment):
            install(package)

def handler(number, frame) -> None:
    '''
    Handle the SIGINT signal when closing the jupyter notebook.
    '''
    print('[MediaCAT Visualization] Closed notebook')

def start() -> None:
    '''
    Start the Jupyter Notebook Server.
    '''
    run(['jupyter', 'notebook', 'notebooks'])

if __name__ == '__main__':
    signal(SIGINT, handler)
    check_packages()
    start()
