from scapy.all import sniff
from datetime import datetime
from database import log_packet

def process_packet(packet):
    try:
        ip_src = packet[0][1].src
        ip_dst = packet[0][1].dst
        protocol = packet.summary()
        timestamp = datetime.now()

        log_packet(ip_src, ip_dst, protocol, timestamp)

    except Exception as e:
        print("Error:", e)

def start_sniffing():
    print("Started Packet Sniffing...")
    sniff(prn=process_packet, store=False)