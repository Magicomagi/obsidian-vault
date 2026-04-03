---
tags:
  - AI
  - informatica
date: 2026-04-03
---
[[gemini_key_rotator.py]]


Configurazione OpenClaw
Nelle impostazioni di OpenClaw, sostituisci:

| Campo                   | Valore                                |
| ----------------------- | ------------------------------------- |
| Base URL / API endpoint | `http://127.0.0.1:8080`               |
| API Key                 | qualsiasi stringa (es. `placeholder`) |



## Esecuzione persistente (systemd user)
~/.config/systemd/user/gemini-rotator.service
```
[Unit]
Description=Gemini API Key Rotator

[Service]
ExecStart=/usr/bin/python3 /path/to/gemini_key_rotator.py
Restart=always

[Install]
WantedBy=default.target


systemctl --user enable --now gemini-rotator.service
```
