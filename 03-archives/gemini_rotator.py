#!/usr/bin/env python3
"""
Gemini API Key Rotator + Browser Dashboard
Proxy:     http://127.0.0.1:8080
Dashboard: http://127.0.0.1:8080/dashboard
Status:    http://127.0.0.1:8080/status  (JSON)
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request, urllib.parse, urllib.error
import sys, threading, datetime, json, collections
import zoneinfo

LISTEN_PORT = 8080
GEMINI_BASE = "https://generativelanguage.googleapis.com"

API_KEYS = [
    "AIzaSyA3WGbixiv9y8zLfugoPDnhi7jmjAyKdB0",
    "AIzaSyDvB9DZZtZts39tOlcBbW56aHBbJ8jMvfs",
    "AIzaSyDt6Xd2fpBd40fS0jzQ8OO5LJgnOcX7egE",
    "AIzaSyAoxITqqg9s0s5b1k2Hw0OilsAp49qiCb4",
]

# --- State ---
current_index = 0
exhausted = set()
lock = threading.Lock()
rotation_log = collections.deque(maxlen=50)
request_counts = [0] * len(API_KEYS)
start_time = datetime.datetime.now()


def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    entry = {"ts": ts, "msg": msg}
    rotation_log.appendleft(entry)
    print(f"[{ts}] {msg}", file=sys.stderr)


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
        log("RESET — tutte le chiavi ripristinate (mezzanotte Pacific Time)")


threading.Thread(target=reset_keys, daemon=True).start()

# --- Dashboard HTML ---
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GEMINI KEY ROTATOR</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow:wght@300;600&display=swap');

  :root {
    --bg:       #09090b;
    --surface:  #111114;
    --border:   #27272a;
    --dim:      #3f3f46;
    --fg:       #e4e4e7;
    --muted:    #71717a;
    --green:    #4ade80;
    --red:      #f87171;
    --amber:    #fbbf24;
    --blue:     #60a5fa;
    --glow-g:   #4ade8033;
    --glow-r:   #f8717133;
    --mono:     'Share Tech Mono', monospace;
    --sans:     'Barlow', sans-serif;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--fg);
    font-family: var(--sans);
    font-weight: 300;
    min-height: 100vh;
    padding: 24px 16px;
  }

  /* Scanline overlay */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,.07) 2px,
      rgba(0,0,0,.07) 4px
    );
    pointer-events: none;
    z-index: 999;
  }

  header {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 32px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 16px;
  }

  header h1 {
    font-family: var(--mono);
    font-size: clamp(1rem, 4vw, 1.4rem);
    letter-spacing: .15em;
    color: var(--green);
    text-shadow: 0 0 18px var(--glow-g);
  }

  header .sub {
    font-family: var(--mono);
    font-size: .7rem;
    color: var(--muted);
    letter-spacing: .1em;
  }

  .ping {
    margin-left: auto;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 10px var(--green);
    animation: pulse 1.6s ease-in-out infinite;
  }

  @keyframes pulse {
    0%,100% { opacity: 1; }
    50%      { opacity: .3; }
  }

  /* Grid layout */
  .grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
    max-width: 860px;
    margin: 0 auto;
  }

  @media (min-width: 600px) {
    .grid { grid-template-columns: 1fr 1fr; }
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 18px 20px;
  }

  .card.wide { grid-column: 1 / -1; }

  .card-label {
    font-family: var(--mono);
    font-size: .65rem;
    letter-spacing: .2em;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 14px;
  }

  /* Stats */
  .stat-val {
    font-family: var(--mono);
    font-size: 2rem;
    color: var(--green);
    text-shadow: 0 0 14px var(--glow-g);
  }

  .stat-sub {
    font-size: .75rem;
    color: var(--muted);
    margin-top: 4px;
  }

  /* Countdown */
  #countdown {
    font-family: var(--mono);
    font-size: 1.5rem;
    color: var(--amber);
    letter-spacing: .08em;
  }

  /* Key list */
  .key-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 0;
    border-bottom: 1px solid var(--border);
    transition: background .15s;
  }

  .key-row:last-child { border-bottom: none; }

  .key-index {
    font-family: var(--mono);
    font-size: .7rem;
    color: var(--dim);
    width: 20px;
    flex-shrink: 0;
  }

  .key-id {
    font-family: var(--mono);
    font-size: .78rem;
    color: var(--muted);
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .key-count {
    font-family: var(--mono);
    font-size: .7rem;
    color: var(--dim);
    width: 48px;
    text-align: right;
  }

  .badge {
    font-family: var(--mono);
    font-size: .6rem;
    letter-spacing: .1em;
    padding: 2px 7px;
    border-radius: 3px;
    text-transform: uppercase;
    flex-shrink: 0;
  }

  .badge-active {
    background: var(--glow-g);
    color: var(--green);
    border: 1px solid var(--green);
    box-shadow: 0 0 8px var(--glow-g);
    animation: pulse 1.6s ease-in-out infinite;
  }

  .badge-ok {
    background: transparent;
    color: var(--blue);
    border: 1px solid #60a5fa44;
  }

  .badge-exhausted {
    background: var(--glow-r);
    color: var(--red);
    border: 1px solid var(--red);
  }

  /* Log */
  #log-list {
    list-style: none;
    max-height: 220px;
    overflow-y: auto;
  }

  #log-list::-webkit-scrollbar { width: 4px; }
  #log-list::-webkit-scrollbar-thumb { background: var(--dim); border-radius: 2px; }

  #log-list li {
    font-family: var(--mono);
    font-size: .72rem;
    padding: 5px 0;
    border-bottom: 1px solid #1a1a1d;
    display: flex;
    gap: 10px;
    color: var(--muted);
  }

  #log-list li:first-child { color: var(--fg); }

  .log-ts {
    color: var(--dim);
    flex-shrink: 0;
  }

  /* Reset button */
  .btn-reset {
    font-family: var(--mono);
    font-size: .7rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    background: transparent;
    color: var(--amber);
    border: 1px solid var(--amber);
    border-radius: 4px;
    padding: 7px 16px;
    cursor: pointer;
    transition: background .15s, box-shadow .15s;
    margin-top: 12px;
    width: 100%;
  }

  .btn-reset:hover {
    background: #fbbf2420;
    box-shadow: 0 0 10px #fbbf2440;
  }

  .btn-reset:active {
    background: #fbbf2440;
  }

  .btn-reset:disabled {
    opacity: .4;
    cursor: not-allowed;
  }

  /* Footer */
  footer {
    margin-top: 28px;
    text-align: center;
    font-family: var(--mono);
    font-size: .62rem;
    color: var(--dim);
    letter-spacing: .1em;
  }
</style>
</head>
<body>

<header>
  <h1>GEMINI KEY ROTATOR</h1>
  <span class="sub">localhost:8080</span>
  <div class="ping"></div>
</header>

<div class="grid">

  <div class="card">
    <div class="card-label">Chiave attiva</div>
    <div class="stat-val" id="active-idx">–</div>
    <div class="stat-sub" id="active-mask"></div>
  </div>

  <div class="card">
    <div class="card-label">Reset (mezzanotte PT)</div>
    <div id="countdown">–</div>
    <div class="stat-sub" id="reset-abs"></div>
    <button class="btn-reset" id="btn-reset" onclick="manualReset()">RESET MANUALE CHIAVI</button>
  </div>

  <div class="card">
    <div class="card-label">Chiavi disponibili</div>
    <div class="stat-val" id="available-count">–</div>
    <div class="stat-sub">su <span id="total-count">–</span> totali</div>
  </div>

  <div class="card">
    <div class="card-label">Richieste totali</div>
    <div class="stat-val" id="total-req">–</div>
    <div class="stat-sub">da avvio proxy</div>
  </div>

  <div class="card wide">
    <div class="card-label">Stato chiavi</div>
    <div id="key-list"></div>
  </div>

  <div class="card wide">
    <div class="card-label">Log rotazioni</div>
    <ul id="log-list"></ul>
  </div>

</div>

<footer>aggiornamento ogni 3s &nbsp;|&nbsp; gemini_rotator.py</footer>

<script>
let resetEpoch = null;

function mask(key) {
  if (key.length <= 8) return key;
  return key.slice(0, 6) + '···' + key.slice(-4);
}

function fmtCountdown(secs) {
  const h = Math.floor(secs / 3600);
  const m = Math.floor((secs % 3600) / 60);
  const s = Math.floor(secs % 60);
  return `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}

async function poll() {
  try {
    const r = await fetch('/status');
    const d = await r.json();

    document.getElementById('active-idx').textContent = `KEY ${d.current_index + 1}`;
    document.getElementById('active-mask').textContent = mask(d.keys[d.current_index] || '');
    document.getElementById('available-count').textContent = d.available;
    document.getElementById('total-count').textContent = d.total;
    document.getElementById('total-req').textContent = d.total_requests.toLocaleString('it');
    resetEpoch = d.reset_epoch;
    document.getElementById('reset-abs').textContent =
      new Date(d.reset_epoch * 1000).toLocaleString('it', {timeZone:'America/Los_Angeles'}) + ' PT';

    // Key list
    const kl = document.getElementById('key-list');
    kl.innerHTML = '';
    d.keys.forEach((k, i) => {
      const isActive = i === d.current_index;
      const isEx = d.exhausted.includes(i);
      const row = document.createElement('div');
      row.className = 'key-row';
      row.innerHTML = `
        <span class="key-index">${i+1}</span>
        <span class="key-id">${mask(k)}</span>
        <span class="key-count">${d.request_counts[i]} req</span>
        <span class="badge ${isActive ? 'badge-active' : isEx ? 'badge-exhausted' : 'badge-ok'}">
          ${isActive ? 'ACTIVE' : isEx ? 'EXHAUSTED' : 'READY'}
        </span>
      `;
      kl.appendChild(row);
    });

    // Log
    const ll = document.getElementById('log-list');
    ll.innerHTML = '';
    d.log.forEach(e => {
      const li = document.createElement('li');
      li.innerHTML = `<span class="log-ts">${e.ts}</span><span>${e.msg}</span>`;
      ll.appendChild(li);
    });

  } catch(e) {
    console.warn('poll failed', e);
  }
}

function tickCountdown() {
  if (!resetEpoch) return;
  const secs = Math.max(0, resetEpoch - Date.now() / 1000);
  document.getElementById('countdown').textContent = fmtCountdown(secs);
}

async function manualReset() {
  const btn = document.getElementById('btn-reset');
  btn.disabled = true;
  btn.textContent = 'RESET IN CORSO...';
  try {
    await fetch('/reset', { method: 'POST' });
    await poll();
    btn.textContent = 'RESET OK';
    setTimeout(() => { btn.textContent = 'RESET MANUALE CHIAVI'; btn.disabled = false; }, 1500);
  } catch(e) {
    btn.textContent = 'ERRORE';
    setTimeout(() => { btn.textContent = 'RESET MANUALE CHIAVI'; btn.disabled = false; }, 2000);
  }
}

poll();
setInterval(poll, 3000);
setInterval(tickCountdown, 1000);
</script>
</body>
</html>
"""


class ProxyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/dashboard":
            self._serve_dashboard()
        elif self.path == "/status":
            self._serve_status()
        else:
            self._proxy("GET")

    def do_POST(self):
        if self.path == "/reset":
            self._manual_reset()
            return
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n) if n else None
        self._proxy("POST", body)

    def _manual_reset(self):
        global current_index, exhausted
        with lock:
            current_index = 0
            exhausted.clear()
        log("RESET MANUALE — tutte le chiavi ripristinate dalla dashboard")
        data = b'{"ok":true}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _serve_dashboard(self):
        data = DASHBOARD_HTML.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _serve_status(self):
        pt = zoneinfo.ZoneInfo("America/Los_Angeles")
        now_pt = datetime.datetime.now(pt)
        midnight_pt = (now_pt + datetime.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        reset_epoch = midnight_pt.timestamp()

        with lock:
            payload = {
                "current_index": current_index,
                "exhausted": list(exhausted),
                "available": len(API_KEYS) - len(exhausted),
                "total": len(API_KEYS),
                "keys": API_KEYS,
                "request_counts": list(request_counts),
                "total_requests": sum(request_counts),
                "reset_epoch": reset_epoch,
                "log": list(rotation_log),
            }

        data = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _proxy(self, method, body=None):
        global current_index
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        params.pop("key", None)

        with lock:
            available = [i for i in range(len(API_KEYS)) if i not in exhausted]

        if not available:
            msg = b'{"error":"all keys exhausted until midnight PT"}'
            self.send_response(429)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(msg)
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
                    with lock:
                        request_counts[idx] += 1
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
                    log(f"Key {idx+1} esaurita (HTTP {e.code}) → {'Key ' + str(current_index+1) if remaining else 'NESSUNA disponibile'}")
                    if not remaining:
                        msg = b'{"error":"all keys exhausted until midnight PT"}'
                        self.send_response(429)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(msg)
                        return
                else:
                    body_err = e.read()
                    self.send_response(e.code)
                    self.end_headers()
                    self.wfile.write(body_err)
                    return

    def log_message(self, fmt, *args):
        # silenzia i log HTTP di default, usa il nostro log() solo per eventi proxy
        pass


if __name__ == "__main__":
    srv = HTTPServer(("127.0.0.1", LISTEN_PORT), ProxyHandler)
    log(f"Proxy avviato su http://127.0.0.1:{LISTEN_PORT} — {len(API_KEYS)} chiavi")
    log(f"Dashboard: http://127.0.0.1:{LISTEN_PORT}/dashboard")
    srv.serve_forever()
