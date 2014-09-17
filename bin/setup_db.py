#!/usr/bin/env python

CLI_DOC = """
USAGE:
    python setup_db.py SQL_URI
"""
from traitcapture import orm
from sqlalchemy import create_engine

def main(uri):
    # create tables in sqlite
    engine = create_engine(uri)
    orm.TableBase.metadata.create_all(engine)

if __name__ == "__main__":
    from sys import argv
    if not len(argv) == 2:
        print CLI_DOC
    else:
        main(argv[1])
