import pymysql

class BD (object):
    __instance = None
    __host = None
    __user = None
    __password = None
    __db = None

    def __new__(cls, *args, **kwargs):
        if BD().__instance is None:
            BD().__instance = object.__new__(cls)
        return BD().__instance

    def setConexion(self, host, user, password, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db

    def run(self, query):
        db = pymysql.connect(host = self.__host, user = self.__user, passwd = self.__password, db = self.__db)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)

        db.close()
        return cursor