import sqlite3, shutil, tempfile, time, os

db_src = "./data/Chinook_Sqlite.sqlite"            # original DB
sql = """select c.FirstName || ' ' || c.LastName, t.Name, a.Title
from 
Customer c
join
Invoice on (c.CustomerId || '') = (Invoice.CustomerId || '')
join
InvoiceLine on (Invoice.InvoiceId || '') = (InvoiceLine.InvoiceId || '')
join
Track t on (InvoiceLine.TrackId || '')  = (t.TrackId || '')
join
Album a on (t.AlbumId || '') = (a.AlbumId || '');"""
#params = ("Playlist",)
runs = 10

def checkpoint_and_close(path: str):
    conn = sqlite3.connect(path)
    try:
        conn.execute("PRAGMA wal_checkpoint(FULL);")
        conn.commit()
    finally:
        conn.close()

checkpoint_and_close(db_src)

times: list[float] = []
for i in range(runs):
    tmp = os.path.join(tempfile.gettempdir(), f"db_temp_{i}.sqlite")
    shutil.copy2(db_src, tmp)           # new inode -> reduces kernel reuse
    conn = sqlite3.connect(tmp)         # reopen fresh connection
    cur = conn.cursor()
    t0 = time.perf_counter()
    cur.execute(sql)
    rows = cur.fetchall()               # include fetch cost
    t1 = time.perf_counter()
    conn.close()                        # close after run
    os.remove(tmp)
    times.append(t1 - t0)
    print(f"run {i+1}: {times[-1]:.6f}s, rows={len(rows)}")

print("mean:", sum(times)/len(times))

