"""LWH: after changing any file in this repo, run `python3 update-sw-revisions.py`
so installed copies of LWH Draw pick up the change (refreshes the offline cache)."""
import hashlib, json, re, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service-worker.js')
s = open(p).read()
def fix(m):
    entry = json.loads(m.group(0))
    f = os.path.join(os.path.dirname(p), entry['url'])
    if entry.get('revision') and os.path.isfile(f):
        entry['revision'] = hashlib.md5(open(f, 'rb').read()).hexdigest()
    return json.dumps(entry, separators=(',', ':'))
s2, n = re.subn(r'\{"url":"[^"]+","revision":(?:"[^"]*"|null)\}', fix, s)
open(p, 'w').write(s2)
print('updated', n, 'entries')
