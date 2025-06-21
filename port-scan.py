import socket

TARGET_IP = "your.vps.ip.address"
PORTS = [22, 80, 443, 3306]

def port_scan():
    for port in PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((TARGET_IP, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open")
        else:
            print(f"[CLOSED] Port {port} is closed or filtered")
        sock.close()

if __name__ == "__main__":
    port_scan()
