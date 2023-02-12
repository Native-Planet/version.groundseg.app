import sqlite3, json, logging, os
from datetime import datetime
from pathlib import Path

logging.basicConfig(filename="/data/srv.log", level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(levelname)s:%(message)s')

dbs = ['latest','edge']
for db in dbs:
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    conn.execute('pragma journal_mode=wal;')
    conn.execute('pragma auto_vacuum = FULL;')
    conn.execute('CREATE TABLE IF NOT EXISTS groundseg (uid INTEGER, \
                major TEXT NULL, minor TEXT NULL, patch TEXT NULL, \
                amd64_url TEXT NULL, arm64_url TEXT NULL, checksum TEXT NULL, \
                last_mod TIMESTAMP NULL, PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS vere (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, checksum TEXT NULL \
                last_mod TIMESTAMP NULL, PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS minio (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, checksum TEXT NULL \
                last_mod TIMESTAMP NULL, PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS wireguard (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, checksum TEXT NULL \
                last_mod TIMESTAMP NULL, PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.commit()
    conn.close()

conn = sqlite3.connect(f'/data/content.sq3', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS content (uid INTEGER, \
            content TEXT NULL, last_mod TIMESTAMP NULL, \
            PRIMARY KEY ("uid" AUTOINCREMENT) );')
conn.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_value(db,table,lookup):
    query = f'SELECT {lookup} FROM {table} WHERE uid is 1;'
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    answer_raw = cur.execute(query).fetchall()
    if not answer_raw:
        return None
    else:
        answer_json = json.loads(json.dumps(answer_raw))
        result = answer_json[0][lookup]
        return result

def upd_value(db,table,key,value):
    timestamp = datetime.now()
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    conn.execute('pragma journal_mode=wal;')
    query = f'UPDATE {db} SET \
        {key} = ?, \
        last_mod = "{timestamp}" \
        WHERE uid is 1;'
    logging.info(query)
    cur = conn.cursor()
    cur.execute(f'''{query}''',(str(value),))
    conn.commit()
    generate_content()

def generate_content():
    content = {
        'groundseg': {
            'latest': {
                'groundseg': {
                    'major': int(get_value('latest','groundseg','major')),
                    'minor': int(get_value('latest','groundseg','minor')),
                    'patch': int(get_value('latest','groundseg','patch')),
                    'amd64_url': get_value('latest','groundseg','amd64_url'),
                    'arm64_url': get_value('latest','groundseg','arm64_url'),
                    'checksum': get_value('latest','groundseg','checksum')
                },
                'vere': {
                    'repo': get_value('latest','vere','repo'),
                    'tag': get_value('latest','vere','tag'),
                    'checksum': get_value('latest','vere','checksum')
                },
                'minio': {
                    'repo': get_value('latest','minio','repo'),
                    'tag': get_value('latest','minio','tag'),
                    'checksum': get_value('latest','minio','checksum')
                },
                'wireguard': {
                    'repo': get_value('latest','wireguard','repo'),
                    'tag': get_value('latest','wireguard','tag'),
                    'checksum': get_value('latest','wireguard','checksum')
                }
            },
            'edge': {
                'groundseg': {
                    'major': get_value('edge','groundseg','major'),
                    'minor': get_value('edge','groundseg','minor'),
                    'patch': get_value('edge','groundseg','patch'),
                    'amd64_url': get_value('edge','groundseg','amd64_url'),
                    'arm64_url': get_value('edge','groundseg','arm64_url'),
                    'checksum': get_value('edge','groundseg','checksum')
                },
                'vere': {
                    'repo': get_value('edge','vere','repo'),
                    'tag': get_value('edge','vere','tag'),
                    'checksum': get_value('edge','vere','checksum')
                },
                'minio': {
                    'repo': get_value('edge','minio','repo'),
                    'tag': get_value('edge','minio','tag'),
                    'checksum': get_value('edge','minio','checksum')
                },
                'wireguard': {
                    'repo': get_value('edge','wireguard','repo'),
                    'tag': get_value('edge','wireguard','tag'),
                    'checksum': get_value('edge','wireguard','checksum')
                }
            }
        }
    }
    content = json.loads(content)
    upd_value('content','content','content',content)
    return content