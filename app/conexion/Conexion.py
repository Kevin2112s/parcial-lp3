import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        # https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn
        dbname = "final-lp3"
        user = "postgres"
        password = "Filter777"
        host = "127.0.0.1"
        port = 5432
        #self.con = psycopg2.connect("dbname=final-lp3 user=postgres host=localhost password=Filter777")
        self.con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con