from scapy.all import IP, TCP, sr1, conf
from colorama import init, Fore
import argparse, sys, socket

conf.verb = 0
init(autoreset=True)


def banner():
    print(
        Fore.RED
        + """
  ▄████▄   ██░ ██   ▄▄▄       ██▀███   ██▓ ██▓███
▒██▀  ▀█   ▓██░ ██▒▒████▄     ▓██  ▒ ██▒▓██▒▓██░  ██▒
▒▓█     ▄  ▒██▀▀██░▒██   ▀█▄   ▓██  ░▄█  ▒▒██▒▓██░ ██▓▒
▒▓▓▄  ▄██▒░▓█  ░██  ░██▄▄▄▄██  ▒██▀▀█▄   ░██░▒██▄█▓▄  ▀
▒  ▓███▀  ░░▓█▒░██▓  ▓█    ▓██▒░██▓  ▒██▒░██░▒██▒  ░   ▄▄
░  ░▒  ▒   ░  ▒  ░░▒░▒  ▒▒    ▓▒█░░  ▒▓  ░▒▓░░▓   ▒▓▒░  ░   ▒▒
   ░   ▒     ▒  ░▒░  ░   ▒    ▒▒  ░   ░▒  ░  ▒░  ▒  ░░▒  ░    ▒
░          ░   ░░  ░   ░    ▒      ░░    ░   ▒  ░░░    ░  ░
░  ░        ░   ░   ░       ░   ░    ░       ░   ░          ░
░                                        
"""
    )


def resolve(host):
    try:
        return socket.gethostbyname(host)
    except Exception:
        print(Fore.RED + "[!] Host inválido ou offline")
        sys.exit(1)


def scan_port(ip, port):
    pkt = IP(dst=ip) / TCP(dport=port, flags="S")
    resp = sr1(pkt, timeout=0.4, retry=1)
    if resp and resp.haslayer(TCP):
        if resp[TCP].flags == "SA":
            return "open"
        elif resp[TCP].flags == "RA":
            return "closed"
    return "filtered"


def main():
    banner()
    parser = argparse.ArgumentParser(
        description="Escâner de portas TCP rápido e quieto."
    )
    parser.add_argument("target", help="IP ou domínio alvo")
    parser.add_argument(
        "-p", "--ports", default="1-1000", help="Intervalo: 22-80 ou lista: 22,80,443"
    )
    args = parser.parse_args()

    ip = resolve(args.target)
    print(Fore.CYAN + f"[+] Alvo: {ip}")

    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = map(int, args.ports.split(","))

    for port in ports:
        status = scan_port(ip, port)
        if status == "open":
            print(Fore.GREEN + f"[+] {port:5}/tcp open")
        elif status == "closed":
            print(Fore.WHITE + f"[-] {port:5}/tcp closed")
        else:
            print(Fore.YELLOW + f"[?] {port:5}/tcp filtered")
    print(Fore.CYAN + "[+] Varredura finalizada.")


if __name__ == "__main__":
    main()
