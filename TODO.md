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

