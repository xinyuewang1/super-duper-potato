# -*- coding: utf-8 -*-

"""Console script for systeminfo_cookiecutter."""

import click
import platform
import shutil


@click.command()
def main():
    #print(platform.platform())
    #total, used, free = shutil.disk_usage(__file__)
    #print('total, used, free: ', total, used, free)
    a= str('The platform is '+platform.platform())
#    print(type(a))
    return a 


if __name__ == "__main__":
    main()
