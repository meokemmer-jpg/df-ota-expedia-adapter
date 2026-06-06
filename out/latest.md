# df-ota-expedia-adapter — Output [CRUX-MK]
*Autonom aktiviert 2026-06-05T15:48:58.998753+00:00 | ollama-local/qwen2.5:14b-instruct*

# df-ota-expedia-adapter [CRUX-MK]

## Zusammenfassung

Der `df-ota-expedia-adapter` ist ein Teil des Kemmer-Systems und dient als 
Connector für die Expedia OTA-APIs. Die Hauptaufgabe dieses Adapters besteh
besteht darin, das Booking-Prozess zu synchronisieren und den Hotellern ein
einen direkten Zugriff auf den Expedia-Markt zu ermöglichen.

## Zweck

Der Adapter stellt folgende Funktionen bereit:
- Verbindung zur Expedia Quick Connect (EQC) API für Inventarabfragen.
- Rate-Push über die Rate Management API.
- Buchungsabfrage und Webhooks für Benachrichtigungen.
- 20%-Kommission-Tracker pro Booking.

## Technische Details

### Module
- `expedia_adapter.py`: Enthält den Hauptcode, der die EQC-API und die Rate
Rate Management-API verwendet. Stellt auch einen Kommissions-Tracker bereit
bereit.
- `expedia_auth.py`: Handhabt das Authentifizierungspattern für SOAP-Token 
und API-Key.
- `expedia_webhook.py`: Empfängt Buchungsbenachrichtigungen über Webhooks u
und verifiziert sie via HMAC-SHA256.
- `commission_tracker.py`: Erstellt Kommissions-Aufzeichnungen und generier
generiert Aggregat-Berichte für die Buchungen.
- `adapter_orchestrator.py`: LaunchAgent-Eingangspunkt für den Adapter.
- `audit_logger.py`: Protokolliert HMAC-SHA256-signed Auditentries (JSONL a
append-only).

### Umgebungsvariablen
- `DF_OTA_EXPEDIA_REAL_ENABLED=false` (Standard): Mock-Daten werden verwend
verwendet. 
- `EXPEDIA_HOTELIER_ID`, `EXPEDIA_API_KEY`: Erforderlich für den realen Mod
Modus.
- `DF_OTA_EXPEDIA_PHRONESIS_TICKET`: Benötigt für Push-Vorgänge im realen M
Modus.

### Tests
Die Testdatei `test_expedia_adapter.py` enthält 27+ Tests, die Adapter-Funk
Adapter-Funktionalität, Authentifizierung, Webhook und Tracker sowie Orches
Orchestrator und AuditLogger abdecken. Der Test kann aus dem Projektordner 
ausgeführt werden:
```bash
PYTHONPATH=. python -m pytest tests/ -v
```

### Verwendung des LaunchAgents
Der LaunchAgent wird via `com.kemmer.df-ota-expedia-adapter.plist` geladen,
geladen, der in den Homeverzeichnis-LaunchAgents kopiert und gestartet wird
wird.

## Compliance

Der Adapter ist gemäß K11-K16 und LC1-LC5 Vorgaben entwickelt:
- **K11:** Cascade-Containment via try/except + LC4 idempotent
- **K12:** Provenance via frozen dataclass + source-tracking
- **K13:** PAV via env_tag + vendor_api anchor
- **K14:** Override via single_command + martin_review weekly
- **K15:** Entropy ~700 LOC mit rho-Justifikation 40k EUR/J
- **K16:** Concurrent-Spawn-Mutex via mkdir-lock + pgrep

## Fazit

Der `df-ota-expedia-adapter` ist ein wesentlicher Bestandteil der Kemmer-Re
Kemmer-Reise-Lösungen, die den Expedia-Markt für Hotellern zugänglich macht
macht und gleichzeitig eine transparente und sichere Kommissionen-Verwaltun
Kommissionen-Verwaltung bietet.