---
tags:
  - informatica
  - AI
date: 2026-04-03
---
```python
#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error, sys, threading, datetime
import zoneinfo

LISTEN_PORT = 8080
GEMINI_BASE = "https://generativelanguage.googleapis.com"

API_KEYS = [
    "AIzaSyA3WGbixiv9y8zLfugoPDnhi7jmjAyKdB0",
    "AIzaSyDvB9DZZtZts39tOlcBbW56aHBbJ8jMvfs",
    "AIzaSyDt6Xd2fpBd40fS0jzQ8OO5LJgnOcX7egE",
    "AIzaSyAoxITqqg9s0s5b1k2Hw0OilsAp49qiCb4",
    "AIza_ACCOUNT_5",
    "AIza_ACCOUNT_6",
]

current_index = 0
exhausted = set()
lock = threading.Lock()


def seconds_until_midnight_pacific():
    pt = zoneinfo.ZoneInfo("America/Los_Angeles")
    now = datetime.datetime.now(pt)
    midnight = (now + datetime.timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    return (midnight - now).total_seconds()


def reset_keys():
    global current_index, exhausted
    while True:
        wait = seconds_until_midnight_pacific()
        threading.Event().wait(wait)
        with lock:
            current_index = 0
            exhausted.clear()
        print("[rotator] RESET: tutte le chiavi ripristinate (mezzanotte Pacific)", file=sys.stderr)


threading.Thread(target=reset_keys, daemon=True).start()


class ProxyHandler(__import__("http.server").server.BaseHTTPRequestHandler):

    def proxy(self, method, body=None):
        global current_index
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        params.pop("key", None)

        with lock:
            available = [i for i in range(len(API_KEYS)) if i not in exhausted]

        if not available:
            self.send_response(429)
            self.end_headers()
            self.wfile.write(b'{"error":"all keys exhausted until midnight PT"}')
            return

        for _ in range(len(available)):
            with lock:
                idx = current_index

            params["key"] = [API_KEYS[idx]]
            query = urllib.parse.urlencode(params, doseq=True)
            url = f"{GEMINI_BASE}{parsed.path}?{query}"

            hdrs = {k: v for k, v in self.headers.items()
                    if k.lower() not in ("host", "content-length")}
            req = urllib.request.Request(url, data=body, headers=hdrs, method=method)

            try:
                with urllib.request.urlopen(req) as r:
                    data = r.read()
                    self.send_response(r.status)
                    for k, v in r.getheaders():
                        if k.lower() != "transfer-encoding":
                            self.send_header(k, v)
                    self.end_headers()
                    self.wfile.write(data)
                    return
            except urllib.error.HTTPError as e:
                if e.code in (429, 403):
                    with lock:
                        exhausted.add(idx)
                        remaining = [i for i in range(len(API_KEYS)) if i not in exhausted]
                        if remaining:
                            current_index = remaining[0]
                    print(f"[rotator] Key {idx} esaurita → {current_index if remaining else 'NESSUNA'}", file=sys.stderr)
                    if not remaining:
                        self.send_response(429)
                        self.end_headers()
                        self.wfile.write(b'{"error":"all keys exhausted until midnight PT"}')
                        return
                else:
                    self.send_response(e.code)
                    self.end_headers()
                    self.wfile.write(e.read())
                    return

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        self.proxy("POST", self.rfile.read(n) if n else None)

    def do_GET(self):
        self.proxy("GET")

    def log_message(self, fmt, *args):
        print(f"[rotator] {fmt % args}", file=sys.stderr)


if __name__ == "__main__":
    from http.server import HTTPServer
    srv = HTTPServer(("127.0.0.1", LISTEN_PORT), ProxyHandler)
    print(f"[rotator] in ascolto su http://127.0.0.1:{LISTEN_PORT} — {len(API_KEYS)} chiavi")
    srv.serve_forever()

```
