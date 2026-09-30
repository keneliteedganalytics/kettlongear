"""Kettlon metrics refresh helper.
Usage: python ops/refresh_metrics.py set instagram.followers 42
       python ops/refresh_metrics.py append ads.history '{"date":"2026-10-01","spend":30,"link_clicks":12}'
       python ops/refresh_metrics.py log "Text of the day"
Writes data/metrics.json and stamps updated_at. Commit and push afterwards."""
import json, sys, datetime, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "data" / "metrics.json"
d = json.loads(P.read_text())
def path(o, k):
    parts = k.split("."); 
    for p in parts[:-1]: o = o.setdefault(p, {})
    return o, parts[-1]
cmd = sys.argv[1]
if cmd == "set":
    o, k = path(d, sys.argv[2]); v = sys.argv[3]
    try: v = json.loads(v)
    except Exception: pass
    o[k] = v
elif cmd == "append":
    o, k = path(d, sys.argv[2]); o.setdefault(k, []).append(json.loads(sys.argv[3]))
elif cmd == "log":
    d.setdefault("log", []).insert(0, {"date": datetime.date.today().isoformat(), "text": sys.argv[2]}); d["log"] = d["log"][:30]
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4)))
d["updated_at"] = now.isoformat(timespec="minutes"); d["updated_by"] = "Kettlon metrics automation"
P.write_text(json.dumps(d, indent=2)); print("ok", cmd)
