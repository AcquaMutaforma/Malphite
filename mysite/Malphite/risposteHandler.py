import psycopg2
import logManager as log

dbname = 'postgres'
user = 'postgres'
password = 'alessandro5'
host = "127.0.0.1"
port = "5432"


def get_risposta_by_idr(idrisposta: int):
    connessione = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port).cursor()
    connessione.execute('SELECT * FROM "Malphite_risposta" WHERE idr=%s', str(idrisposta))
    try:
        return connessione.fetchone()
    except ConnectionError as e:
        log.logError(f"[risposteHandler] - connessione DB - {e}")
    except Exception as e:
        log.logError(f"[risposteHandler] - connessione DB - {e}")


def get_idrisposte_con_keyword(keyword: str) -> ():
    connessione = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port).cursor()
    connessione.execute('(SELECT idr FROM "Malphite_risposta" WHERE idr IN ( SELECT idRisposta_id FROM "Malphite_relazione" WHERE idKeyword_id IN ( SELECT id FROM "Malphite_keyword" WHERE keyword = %s)))', (str(keyword),))
    try:
        return connessione.fetchone()
    except ConnectionError as e:
        log.logError(f"[risposteHandler] - connessione DB - {e}")
    except Exception as e:
        log.logError(f"[risposteHandler] - connessione DB - {e}")


"""
INSERT INTO "Malphite_risposta" (idr, nome, "percorsoFile") VALUES (1,'test','/home/rasp/Desktop/')
INSERT INTO "Malphite_keyword" (id, keyword) VALUES (1,'test')
INSERT INTO "Malphite_keyword_idRisposta" (id, keyword_id, risposta_id) VALUES (1, 1, 1)

SELECT idr FROM "Malphite_risposta" WHERE idr IN ( SELECT risposta_id FROM "Malphite_keyword_idRisposta" WHERE keyword_id IN ( SELECT id FROM "Malphite_keyword" WHERE keyword=%s))
"""