
# importing pyspatialite
from pyspatialite import dbapi2 as db

# creating/connecting in memory db
with db.connect(':memory:') as conn:
    conn.enable_load_extension(True)
    # creating a Cursor
    cur = conn.cursor()
    rs = cur.execute('SELECT sqlite_version(), spatialite_version()')
    for row in rs:
        msg = "> SQLite v%s Spatialite v%s" % (row[0], row[1])
        print(msg)

