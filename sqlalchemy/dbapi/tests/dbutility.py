#-*- coding: UTF-8 -*-
from sqlalchemy.dbapi import Scope_session as Session
from sqlalchemy.dbapi.ORMdbAPI import Dbapi

from sqlalchemy.dbapi.tests.mapping_db import JuanZeng


#automap class start
search_clmns = ['xingming']
juanzeng = Dbapi(Session,'xtcs.policy.mapping_db','juanzeng',JuanZeng,"mysql",fullsearch_clmns=search_clmns)
#automap end



    