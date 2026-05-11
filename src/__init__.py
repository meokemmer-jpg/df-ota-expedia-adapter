"""df-ota-expedia-adapter [CRUX-MK].

Welle-37 HeyLou-Mosaic-Adapter fuer Expedia OTA (Global Top-2 mit Booking).

LAZY-IMPORT-PATTERN: Module werden bei Bedarf importiert.
"""

from __future__ import annotations

__version__ = "0.1.0-SKELETON"
__df_id__ = "df-ota-expedia-adapter"
__welle__ = "welle-37"


def get_connector():
    from src.expedia_adapter import ExpediaConnector
    return ExpediaConnector


def get_auth_manager():
    from src.expedia_auth import ExpediaAuthManager
    return ExpediaAuthManager


def get_webhook_handler():
    from src.expedia_webhook import ExpediaWebhookHandler
    return ExpediaWebhookHandler


def get_commission_tracker():
    from src.commission_tracker import CommissionTracker
    return CommissionTracker


def get_orchestrator():
    from src.adapter_orchestrator import ExpediaAdapterOrchestrator
    return ExpediaAdapterOrchestrator


def get_audit_logger():
    from src.audit_logger import AuditLogger
    return AuditLogger


__all__ = [
    "__version__",
    "__df_id__",
    "__welle__",
    "get_connector",
    "get_auth_manager",
    "get_webhook_handler",
    "get_commission_tracker",
    "get_orchestrator",
    "get_audit_logger",
]
