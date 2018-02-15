# -*- coding: utf-8 -*-

"""Console script for systeminfo_cookiecutter."""

import click


@click.command()
def main():
    print(platform.platform())
    total, used, free = shutil.disk_usage(__file__)
    print('total, used, free: ', total, used, free)
    return


if __name__ == "__main__":
    import sys
    sys.exit(main())
