# System-Konfiguration für PipelineShield
app_name: str = "PiplineShield"
version: float = 1.0
port: int = 8000
is_running: bool = True

# Ausgabe mit modernem f-String
print(f"[{app_name} v{version}] lauscht auf Port {port} - Aktiv: {is_running}")

