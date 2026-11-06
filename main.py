# System-Konfiguration für PipelineShield
app_name: str = "PipelineShield"
version: float = 1.0
port: int = 8000
is_running: bool = True

print("=" * 70)
print(f"[{app_name} v{version}] Central Authentication & Security Service")
print(f"Status: Aktiv | Port: {port} | Environment: Development")
print("=" * 70)


# --- Load Distribution & Capacity Metrics ---
print("\n--- [01] Load Distribution & Capacity Metrics ---")
total_requests: int = 7
worker_count: int = 2

exact_load: float = total_requests / worker_count
full_batches: int = total_requests // worker_count
remaining_requests: int = total_requests % worker_count

print(f"Floating-Point Division : {total_requests} / {worker_count} = {exact_load} ({type(exact_load).__name__})")
print(f"Integer Floor Division  : {total_requests} // {worker_count} = {full_batches} ({type(full_batches).__name__})")
print(f"Modulo (Remainder)      : {total_requests} % {worker_count} = {remaining_requests} ({type(remaining_requests).__name__})")


# --- Billing & Cost Calculation ---
print("\n--- [02] Billing & Cost Calculation ---")
base_cost: float = 1200.00
discount_percent: float = 15.0

discount_amount: float = base_cost * (discount_percent / 100.0)
final_cost: float = base_cost - discount_amount

print(f"Base License Cost       : {base_cost:.2f} EUR")
print(f"Discount ({discount_percent}%)        : -{discount_amount:.2f} EUR")
print(f"Final Billing Amount    : {final_cost:.2f} EUR")


# --- Safe Metrics Calculation (Zero-Division-Guard) ---
print("\n--- [03] Zero-Division Protection ---")
incoming_traffic: int = 500
active_nodes: int = 0  # Simulierter Serverausfall: 0 Knoten verfügbar!

if active_nodes == 0:
    print("Security Alert          : Keine aktiven Knoten! Berechnung übersprungen (ZeroDivisionError verhindert).")
    load_per_node: float = 0.0
else:
    load_per_node = incoming_traffic / active_nodes
    print(f"Traffic pro Knoten      : {load_per_node:.2f}")


# --- Authentication & Role-Based Access Control ---
print("\n--- [04] Access Control (RBAC) ---")
user_role: str = "security_officer"
failed_login_attempts: int = 2
is_account_locked: bool = False

if is_account_locked or failed_login_attempts >= 5:
    print("Access Check            : Access Denied (Account is locked due to security policy).")
elif user_role == "admin" or user_role == "security_officer":
    print(f"Access Check            : Access Granted (Elevated privileges for '{user_role}').")
elif user_role == "user" and not is_account_locked:
    print("Access Check            : Access Granted (Standard user access).")
else:
    print("Access Check            : Access Denied (Unknown role or insufficient permissions).")


# --- Token Presence Check (Truthy & Falsy) ---
print("\n--- [05] Token Verification (Truthy & Falsy) ---")
raw_magic_token: str = ""  # Leerer String ist "Falsy"!

if not raw_magic_token:
    print("Token Status            : Warning: Kein Authentifizierungs-Token übergeben (Falsy erkannt).")
else:
    print(f"Token Status            : Token empfangen: {raw_magic_token} (Truthy erkannt).")


# --- Token Validation Function (Guard Clause Pattern) ---
print("\n--- [06] Guard Clause Function Validation ---")


def validate_magic_token(token: str, min_length: int = 16) -> bool:
    # Guard 1: Ist das Token leer oder None? (Falsy-Check)
    if not token:
        return False

    # Guard 2: Erfüllt das Token die Mindestlänge?
    if len(token) < min_length:
        return False

    # Wenn alle Wächter passiert wurden:
    return True


# Testaufrufe der Funktion mit Argumenten:
test_token_invalid: str = "short-token"
test_token_valid: str = "secure-magic-link-token-998877"

print(f"Check '{test_token_invalid}' -> Gültig? {validate_magic_token(test_token_invalid)}")
print(f"Check '{test_token_valid}'   -> Gültig? {validate_magic_token(test_token_valid)}")


# --- Service Connection Retry Loop (for-in-range & break) ---
print("\n--- [07] Connection Manager (Retry Loop) ---")
max_retries: int = 3
service_connected: bool = False

for attempt in range(1, max_retries + 1):
    print(f"Verbindungsversuch {attempt} von {max_retries}...")

    # Wir simulieren: Beim 2. Versuch ist die Verbindung erfolgreich!
    if attempt == 2:
        service_connected = True
        print("-> Verbindung erfolgreich hergestellt! (Schleife per 'break' beendet)")
        break
else:
    print("Alert                   : Alle Verbindungsversuche fehlgeschlagen!")

print(f"Verbindungsstatus       : Verbunden = {service_connected}")


# --- Event Queue Processing (while-loop & continue) ---
print("\n--- [08] Event Processor (Queue Handling) ---")
queue_length: int = 4

while queue_length > 0:
    current_event_id: int = queue_length
    queue_length -= 1  # Zähler verringern

    # Event 2 ist nur ein Netzwerk-Ping -> Überspringen mit continue!
    if current_event_id == 2:
        print(f"Event #{current_event_id}                : Harmloser Heartbeat-Ping -> Übersprungen mit 'continue'.")
        continue

    print(f"Event #{current_event_id}                : Kritisches Auth-Event analysiert und gespeichert.")

print("Queue-Status            : Warteschlange komplett abgearbeitet.")


# --- Security Collections: Lists & Indexing ---
print("\n--- [09] Firewall IP Collections ---")
blocked_ips: list[str] = ["192.168.1.50", "10.0.0.99", "172.16.0.23"]
blocked_ips.append("192.168.1.105")

print(f"Gesamtzahl gesperrter IPs: {len(blocked_ips)}")
print(f"Erste gesperrte IP [0]   : {blocked_ips[0]}")
print(f"Zuletzt gesperrte IP [-1]: {blocked_ips[-1]}")


# --- Security Sessions: Dictionaries & Safe Access ---
print("\n--- [10] Session Manager (Dictionary) ---")
auth_session: dict[str, str] = {
    "session_id": "sess-9912-xyz",
    "username": "lead_developer",
    "mfa_status": "verified",
}
auth_session["client_ip"] = "192.168.1.105"

print(f"Aktiver Benutzer        : {auth_session['username']}")
print(f"MFA-Status              : {auth_session['mfa_status']}")
print(f"Client-IP               : {auth_session['client_ip']}")
print(f"Sicherer Zugriff (.get) : {auth_session.get('scope')} (Kein Absturz dank .get!)")


# --- Memory References: The Mutability Trap ---
print("\n--- [11] Memory Mutability Trap ---")
primary_whitelist: list[str] = ["admin-pc", "gateway-01"]

# Falsche Kopie (Referenz teilt sich denselben Speicherbereich!):
mirrored_whitelist: list[str] = primary_whitelist
mirrored_whitelist.append("hacker-laptop")

print(f"Mirrored Whitelist      : {mirrored_whitelist}")
print(f"Primary Whitelist       : {primary_whitelist}  <-- Ungewollt manipuliert!")

# Echte Kopie (Unabhängiger Speicherplatz mit .copy()):
safe_whitelist: list[str] = primary_whitelist.copy()
safe_whitelist.append("new-secure-node")

print(f"Safe Whitelist          : {safe_whitelist}")
print(f"Primary Whitelist       : {primary_whitelist}  <-- Bleibt sauber geschuetzt!")
print("=" * 70)
