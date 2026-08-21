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

