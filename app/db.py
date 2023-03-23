import sqlite3, json, logging, os
from datetime import datetime
from pathlib import Path

logging.basicConfig(filename="/data/srv.log", level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(levelname)s:%(message)s')

# create DB if it doesnt exist
dbs = ['latest','edge','canary']
for db in dbs:
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    conn.execute('pragma journal_mode=wal;')
    conn.execute('pragma auto_vacuum = FULL;')
    conn.execute('CREATE TABLE IF NOT EXISTS groundseg (uid INTEGER, \
                major TEXT NULL, minor TEXT NULL, patch TEXT NULL, \
                amd64_url TEXT NULL, arm64_url TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS webui (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS vere (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS minio (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS miniomc (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS netdata (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
    conn.execute('CREATE TABLE IF NOT EXISTS wireguard (uid INTEGER, \
                repo TEXT NULL, tag TEXT NULL, amd64_sha256 TEXT NULL, \
                arm64_sha256 TEXT NULL, last_mod TIMESTAMP NULL, \
                PRIMARY KEY ("uid" AUTOINCREMENT) );')
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

# look up value in db
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

# update value in db
def upd_value(db,table,key,value):
    timestamp = datetime.now()
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    conn.execute('pragma journal_mode=wal;')
    query = f'UPDATE {table} SET \
        {key} = ?, \
        last_mod = "{timestamp}";'
    logging.info(f'UPDATE {db}/{table}: {key}={value}')
    cur = conn.cursor()
    cur.execute(f'''{query}''',(str(value),))
    conn.commit()

# insert blank row in table
def insert_row(db,table):
    timestamp = datetime.now()
    conn = sqlite3.connect(f'/data/{db}.sq3', isolation_level=None)
    query = f'INSERT INTO {table} (uid) VALUES(1);'
    logging.info(f'Inserting {db}:{table}')
    cur = conn.cursor()
    cur.execute(query)
    conn.commit

# generate version object and cache in db
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
                    'amd64_sha256': get_value('latest','groundseg','amd64_sha256'),
                    'arm64_sha256': get_value('latest','groundseg','arm64_sha256')
                },
                'webui': {
                    'repo': get_value('latest','webui','repo'),
                    'tag': get_value('latest','webui','tag'),
                    'amd64_sha256': get_value('latest','webui','amd64_sha256'),
                    'arm64_sha256': get_value('latest','webui','arm64_sha256')
                },
                'vere': {
                    'repo': get_value('latest','vere','repo'),
                    'tag': get_value('latest','vere','tag'),
                    'amd64_sha256': get_value('latest','vere','amd64_sha256'),
                    'arm64_sha256': get_value('latest','vere','arm64_sha256')
                },
                'minio': {
                    'repo': get_value('latest','minio','repo'),
                    'tag': get_value('latest','minio','tag'),
                    'amd64_sha256': get_value('latest','minio','amd64_sha256'),
                    'arm64_sha256': get_value('latest','minio','arm64_sha256')
                },
                'miniomc': {
                    'repo': get_value('latest','miniomc','repo'),
                    'tag': get_value('latest','miniomc','tag'),
                    'amd64_sha256': get_value('latest','miniomc','amd64_sha256'),
                    'arm64_sha256': get_value('latest','miniomc','arm64_sha256')
                },
                'netdata': {
                    'repo': get_value('latest','netdata','repo'),
                    'tag': get_value('latest','netdata','tag'),
                    'amd64_sha256': get_value('latest','netdata','amd64_sha256'),
                    'arm64_sha256': get_value('latest','netdata','arm64_sha256')
                },
                'wireguard': {
                    'repo': get_value('latest','wireguard','repo'),
                    'tag': get_value('latest','wireguard','tag'),
                    'amd64_sha256': get_value('latest','wireguard','amd64_sha256'),
                    'arm64_sha256': get_value('latest','wireguard','arm64_sha256')
                }
            },
            'edge': {
                'groundseg': {
                    'major': int(get_value('edge','groundseg','major')),
                    'minor': int(get_value('edge','groundseg','minor')),
                    'patch': int(get_value('edge','groundseg','patch')),
                    'amd64_url': get_value('edge','groundseg','amd64_url'),
                    'arm64_url': get_value('edge','groundseg','arm64_url'),
                    'amd64_sha256': get_value('edge','groundseg','amd64_sha256'),
                    'arm64_sha256': get_value('edge','groundseg','arm64_sha256')
                },
                'webui': {
                    'repo': get_value('edge','webui','repo'),
                    'tag': get_value('edge','webui','tag'),
                    'amd64_sha256': get_value('edge','webui','amd64_sha256'),
                    'arm64_sha256': get_value('edge','webui','arm64_sha256')
                },
                'vere': {
                    'repo': get_value('edge','vere','repo'),
                    'tag': get_value('edge','vere','tag'),
                    'amd64_sha256': get_value('edge','vere','amd64_sha256'),
                    'arm64_sha256': get_value('edge','vere','arm64_sha256')
                },
                'minio': {
                    'repo': get_value('edge','minio','repo'),
                    'tag': get_value('edge','minio','tag'),
                    'amd64_sha256': get_value('edge','minio','amd64_sha256'),
                    'arm64_sha256': get_value('edge','minio','arm64_sha256')
                },
                'miniomc': {
                    'repo': get_value('edge','miniomc','repo'),
                    'tag': get_value('edge','miniomc','tag'),
                    'amd64_sha256': get_value('edge','miniomc','amd64_sha256'),
                    'arm64_sha256': get_value('edge','miniomc','arm64_sha256')
                },
                'netdata': {
                    'repo': get_value('edge','netdata','repo'),
                    'tag': get_value('edge','netdata','tag'),
                    'amd64_sha256': get_value('edge','netdata','amd64_sha256'),
                    'arm64_sha256': get_value('edge','netdata','arm64_sha256')
                },
                'wireguard': {
                    'repo': get_value('edge','wireguard','repo'),
                    'tag': get_value('edge','wireguard','tag'),
                    'amd64_sha256': get_value('edge','wireguard','amd64_sha256'),
                    'arm64_sha256': get_value('edge','wireguard','arm64_sha256')
                }
            },
            'canary': {
                'groundseg': {
                    'major': int(get_value('canary','groundseg','major')),
                    'minor': int(get_value('canary','groundseg','minor')),
                    'patch': int(get_value('canary','groundseg','patch')),
                    'amd64_url': get_value('canary','groundseg','amd64_url'),
                    'arm64_url': get_value('canary','groundseg','arm64_url'),
                    'amd64_sha256': get_value('canary','groundseg','amd64_sha256'),
                    'arm64_sha256': get_value('canary','groundseg','arm64_sha256')
                },
                'webui': {
                    'repo': get_value('canary','webui','repo'),
                    'tag': get_value('canary','webui','tag'),
                    'amd64_sha256': get_value('canary','webui','amd64_sha256'),
                    'arm64_sha256': get_value('canary','webui','arm64_sha256')
                },
                'vere': {
                    'repo': get_value('canary','vere','repo'),
                    'tag': get_value('canary','vere','tag'),
                    'amd64_sha256': get_value('canary','vere','amd64_sha256'),
                    'arm64_sha256': get_value('canary','vere','arm64_sha256')
                },
                'minio': {
                    'repo': get_value('canary','minio','repo'),
                    'tag': get_value('canary','minio','tag'),
                    'amd64_sha256': get_value('canary','minio','amd64_sha256'),
                    'arm64_sha256': get_value('canary','minio','arm64_sha256')
                },
                'miniomc': {
                    'repo': get_value('canary','miniomc','repo'),
                    'tag': get_value('canary','miniomc','tag'),
                    'amd64_sha256': get_value('canary','miniomc','amd64_sha256'),
                    'arm64_sha256': get_value('canary','miniomc','arm64_sha256')
                },
                'netdata': {
                    'repo': get_value('canary','netdata','repo'),
                    'tag': get_value('canary','netdata','tag'),
                    'amd64_sha256': get_value('canary','netdata','amd64_sha256'),
                    'arm64_sha256': get_value('canary','netdata','arm64_sha256')
                },
                'wireguard': {
                    'repo': get_value('canary','wireguard','repo'),
                    'tag': get_value('canary','wireguard','tag'),
                    'amd64_sha256': get_value('canary','wireguard','amd64_sha256'),
                    'arm64_sha256': get_value('canary','wireguard','arm64_sha256')
                }
            }
        }
    }
    content = json.dumps(content)
    upd_value('content','content','content',content)
    return content

# populate db with values in default_vals.json
def default_vals():
    f = open('/app/default_vals.json')
    d = json.load(f)['groundseg']
    channels = ['latest', 'edge']
    for channel in channels:
        for obj in d[channel]: # gs, vere, minio
            for item in d[channel][obj]: # repo, tag, sha256
                val = d[channel][obj][item]
                upd_value(f'{channel}',f'{obj}',f'{item}',f'{val}')
    generate_content()

# Create rows if empty db
# if extending schema, change to new table name
nullcheck = get_value('canary','netdata','uid')
if nullcheck == None:
    f = open('/app/default_vals.json')
    d = json.load(f)
    channels = ['latest', 'edge', 'canary']
    for channel in channels:
        for table in d['groundseg'][channel]:
            logging.info(f'Creating {channel} {table} table')
            nullcheck = get_value(channel,table,'uid')
            if nullcheck == None:
                insert_row('edge',table)
                insert_row('latest',table)
                insert_row('canary',table)
    nullcheck = get_value('content','content','uid')
    if nullcheck == None:
        insert_row('content','content')
    default_vals()