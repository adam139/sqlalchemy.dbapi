#-*- coding: UTF-8 -*-
import sqlalchemy.schema
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

from sqlalchemy.dbapi import ORMBase,engine

# automap
metadata = MetaData()
metadata.reflect(engine, only=['juanzeng'])
AutoBase = automap_base(metadata=metadata)
AutoBase.prepare()
JuanZeng = AutoBase.classes.juanzeng

