<!-- ├── └── │ 🔴🟡🟢-->
# HomeLab Monitoring System — TODO

---

## ✅ Erledigt

- [x] DataGrabber: `getContainerId()`, `getContainerData()`, `getServiceName()`
- [x] ContainerStatus Pydantic Model (`cgroup` auskommentiert)
- [x] Severity als echte Enum-Klasse mit 8 journald Priority-Leveln
- [x] UnitFileManager: `loop_unit_file()`, `create_unit_file()`, `write_unit_file()`, `push_unit_file()`

---

## 🔧 Offen

- [ ] Unit-File Template ausarbeiten 🔴
│   ├── [ ] OnFailure= : welcher Service wird getriggert? 🔴
│   ├── [ ] ExecStart= : korrekten Pfad eintragen 🔴
│   ├── [ ] WantedBy= : multi-user.target 🔴
│   └── [ ] Type= : simple/forking je nach Service 🔴
- [ ] UnitFileManager Factory fertigstellen 🟡
│   ├── [ ] Existenzprüfung vor touch 🟡
│   └── [ ] While-Schleife in DataGrabber für neue Services 🟢
- [ ] journalctl -o json Ausgabe analysieren → Felder auf ContainerStatus mappen 🔴
- [ ] Rolling-Snapshot implementieren (alle ~30s überschreiben) 🟡
- [ ] parseServiceData() in ObjManager reparieren (colon-split ist falsch) 🟢
- [ ] MonitoringFactory ausarbeiten 🟢
- [ ] ObjManager verheiraten: MonitoringFactory + DataGrabber → model_validate() 🟡
- [ ] ntfy-Notification implementieren 🟢
- [ ] Eine Website mit Flask-Framework bauen 🟢
│   ├── [ ] Webspace einrichten 🔴
│   ├── [ ] Flask installieren 🟢
│   ├── [ ] Ermmittlung von Methoden für die Live-Überwachung der Container 🟡
│   ├── [ ] GUI für Live-Monitoring ausarbeiten 🟢
│   ├── [ ] Implementierung 🟢
│   └── [ ] Anlegen der TLD und die erweiterte Netzwerkarbeit (cloudflare, Pi-hole, NPMplus, Fritzbox) 🟡

---

## ⏳ Nächste Projekte (parallel, keine Reihenfolge)

- [ ] VPN installieren und konfigurieren
│   └── [ ] https://pve.dara.best hinter einem VPN Handshake verstecken
- [ ] WireGuard VPN für externen Pi-hole Zugriff
- [ ] Pi-hole Android App
- [ ] Netzwerk-Umstrukturierung auf 10.X.Y.Z (nach Monitoring!)
- [ ] Proton Mail Migration
- [ ] Proton Mail Bridge Container für Paperless-ngx


"""
UnitFileManager.py

Zweck:
    Legt automatisch systemd-Unit-Dateien für alle aktiven Services
    pro LXC-Container an und hält diese aktuell.

Ablauf:
    1. Bezieht vmid und targetList aus Class_EndPoints (via Factory)
    2. Prüft pro Service in targetList, ob bereits eine Unit-Datei existiert
    3. Legt fehlende Unit-Dateien neu an, basierend auf einer Vorlage
    4. Unit-Dateien enthalten:
        - Restart=on-failure  (automatischer Neustart bei Absturz)
        - OnFailure=          (Todesschrei — triggert Benachrichtigung)
    5. Läuft in einer While-Schleife (mehrfach pro Minute),
       um neu hinzugekommene Services zu erkennen und abzudecken

Abhängigkeiten:
    - Class_EndPoints.py  (vmid, targetList)
    - Vorlage für Unit-Datei (noch zu definieren)

Offen:
    - Welcher Service wird via OnFailure= getriggert?
    - Pfad der Unit-Dateien innerhalb der LXCs
"""

