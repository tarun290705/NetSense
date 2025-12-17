from scapy.all import sniff, IP
from capture.flow_tracker import update_flow, finalize_flow
from capture.feature_builder import build_feature_payload
from sender.send_to_backend import send_log
import time

FLOW_TIMEOUT = 10  # seconds

last_seen = {}

def process_packet(packet):
    if not packet.haslayer(IP):
        return

    src = packet[IP].src
    dst = packet[IP].dst
    proto = packet[IP].proto
    length = len(packet)

    key, flow = update_flow(src, dst, proto, length)
    last_seen[key] = time.time()

    # Finalize flow if timeout exceeded
    for k in list(last_seen.keys()):
        if time.time() - last_seen[k] > FLOW_TIMEOUT:
            features = finalize_flow(k)
            payload = build_feature_payload(packet, features)
            send_log(payload)
            del last_seen[k]

def start_sniffing():
    print("🚀 Starting live packet capture...")
    sniff(prn=process_packet, store=False)
