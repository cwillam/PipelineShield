# System-Konfiguration für PipelineShield
app_name: str = "PiplineShield"
version: float = 1.0
port: int = 8000
is_running: bool = True

# Ausgabe mit modernem f-String
print(f"[{app_name} v{version}] lauscht auf Port {port} - Aktiv: {is_running}")


# --- Load Distribution & Capacity Metrics ---
total_requests: int = 7
worker_count: int = 2

exact_load: float = total_requests / worker_count
full_batches: int = total_requests // worker_count
remaining_requests: int = total_requests % worker_count

print(f"Floating-Point Division : {total_requests} / {worker_count} = {exact_load} ({type(exact_load).__name__})")
print(f"Integer Floor Division  : {total_requests} // {worker_count} = {full_batches} ({type(full_batches).__name__})")
print(f"Modulo (Remainder)      : {total_requests} % {worker_count} = {remaining_requests} ({type(remaining_requests).__name__})")


# --- Billing & Cost Calculation ---
base_cost: float = 1200.00
discount_percent: float = 15.0

discount_amount: float = base_cost * (discount_percent / 100.0)
final_cost: float = base_cost - discount_amount

print(f"Base License Cost      : {base_cost:.2f} EUR")
print(f"Discount ({discount_percent}%)        : -{discount_amount:.2f} EUR")
print(f"Final Billing Amount   : {final_cost:.2f} EUR")


# --- Safe Metrics Calculation (Zero-Division-Guard) ---
incoming_traffic: int = 500
active_nodes: int = 0 # Simulierter Serverausfall: 0 Knoten verfügbar!

if active_nodes == 0:
    print("Security Alert: Keine aktiven Knoten! Berechnung übersprungen (ZeroDivisionError verhindert).")
    load_per_node: float = 0.0
else:
    load_per_node = incoming_traffic / active_nodes
    print(f"Traffic pro Knoten: {load_per_node:.2f}")
