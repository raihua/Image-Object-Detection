import click
import sys
import os

# project_root = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(project_root)

from image_search_manager_builder import ImageSearchManagerBuilder
from sqlite_indexing import SQLiteIndexing
from mobile_net_detector import MobileNetDetector
builder = ImageSearchManagerBuilder()
image_search_manager = builder\
    .set_index_strategy(SQLiteIndexing())\
    .set_object_detection_model(MobileNetDetector())\
    .build()


@click.group()
def main():
    pass


#
# Each of the functions below is the entry point of a use case for the command line application.
# Call your code from each of these functions, but do not include all of your code in the functions
# in this file.
#


@main.command()
@click.argument("image_path", type=click.Path(exists=True, dir_okay=False))
def add(image_path):
    print(image_search_manager.add(image_path))


@main.command()
@click.option(
    "--all/--some",
    default=True,
    show_default=True,
    help="List images that match all/some query terms",
)
@click.argument("terms", nargs=-1, required=True)
def search(all, terms):
    print(image_search_manager.search(all, terms))


@main.command()
@click.option(
    "--k",
    default=1,
    type=click.IntRange(1),
    show_default=True,
    help="Number of matches to return",
)
@click.argument("image_path", type=click.Path(exists=True, dir_okay=False))
def similar(k, image_path):
    print(image_search_manager.similar(k, image_path))


@main.command()
def list():
    print(image_search_manager.list())


if __name__ == "__main__":
    main()
