#!/usr/bin/env python
from traitcapture.orm import Accession, User, Species, Plant
from csv import DictReader
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

def main(opts):
    engine = create_engine()
    session = scoped_session(sessionmaker(bind=engine))

    session.flush()
    session.commit()
