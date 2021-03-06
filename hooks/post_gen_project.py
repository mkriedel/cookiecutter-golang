"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function
import os
import shutil
import shlex
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


def remove_docker_files():
    """
    Removes files needed for docker if it isn't going to be used
    """
    for filename in ["Dockerfile",]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

def remove_viper_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "config"
    ))

def remove_logrus_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "log"
    ))

def remove_cobra_files():
    """
    Remove files needed for cobra utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "cmd"
    ))

def run_gofmt():
    """
    Cleans up go code
    """
    args = shlex.split("gofmt -w %s" % PROJECT_DIRECTORY)
    p = Popen(args)
    p.wait()
    if p.returncode != 0:
        raise OSError

# 1. Remove Dockerfiles if docker is not going to be used
if '{{ cookiecutter.use_docker }}'.lower() != 'y':
    remove_docker_files()

# 2. Remove viper config if not seleted
if '{{ cookiecutter.use_viper_config }}'.lower() != 'y':
    remove_viper_files()

# 3. Remove logrus utils if not seleted
if '{{ cookiecutter.use_logrus_logging }}'.lower() != 'y':
    remove_logrus_files()

# 4. Remove unused ci choice
if '{{ cookiecutter.use_ci}}'.lower() == 'travis':
    remove_file("circle.yml")
elif '{{ cookiecutter.use_ci}}'.lower() == 'circle':
    remove_file(".travis.yml")
else:
    remove_file(".travis.yml")
    remove_file("circle.yml")

# 5. Remove unused cobra if not selected
if '{{ cookiecutter.use_cobra }}' != 'y':
    remove_cobra_files()

# 6. Run gofmt
run_gofmt()

# 7. Initialize Git (should be run after all file have been modified or deleted)
if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file(".gitignore")
