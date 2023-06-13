# -*- coding: utf-8 -*-
from banco_dados import pessoa_dao
from banco_dados import db

db.init()

pessoa_dao.insert(2, "ketlin", "7867634")
