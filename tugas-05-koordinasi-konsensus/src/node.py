
"""
Tugas 5 - Simulasi Node untuk Bully Algorithm

Infrastruktur jaringan (socket server/client) sudah disediakan.
Logika Bully Algorithm dilengkapi pada bagian TODO.

Contoh menjalankan (5 terminal terpisah):
    py src/node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
    py src/node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
    ... dst untuk id 3, 4, 5
"""

import argparse
import socket
import threading
import time

ELECTION_TIMEOUT = 2.0  # detik menunggu balasan OK


class Node:
    def __init__(self, node_id: int, port: int, peers: dict):
        self.node_id = node_id
        self.port = port
        # peers: dict {peer_id: peer_port} untuk semua node LAIN
        self.peers = peers
        self.leader_id = None
        self.lock = threading.Lock()

        # Event untuk menerima balasan OK dan COORDINATOR
        self.ok_received = threading.Event()
        self.coordinator_received = threading.Event()
        self.election_lock = threading.Lock()
        self.election_in_progress = False
        self.last_election_time = 0

    # ---------- Infrastruktur jaringan ----------

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", self.port))
        server.listen()
        print(f"[Node {self.node_id}] Listening di port {self.port}")

        while True:
            conn, _ = server.accept()
            threading.Thread(
                target=self.handle_connection,
                args=(conn,),
                daemon=True
            ).start()

    def handle_connection(self, conn: socket.socket):
        with conn:
            data = conn.recv(1024).decode()
            if not data:
                return

            try:
                sender_id, msg_type = data.split(":", 1)
                self.on_message(int(sender_id), msg_type)
            except ValueError:
                print(f"[Node {self.node_id}] Pesan tidak valid: {data}")

    def send_message(self, target_port: int, msg_type: str) -> bool:
        """Kirim pesan ke node lain. False berarti target tidak merespons."""
        try:
            with socket.create_connection(
                ("localhost", target_port), timeout=1.0
            ) as s:
                s.sendall(f"{self.node_id}:{msg_type}".encode())
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    # ---------- Logika Bully Algorithm ----------

    def on_message(self, sender_id: int, msg_type: str):
        """Memproses pesan yang diterima dari node lain."""

        print(
            f"[Node {self.node_id}] Menerima pesan '{msg_type}' "
            f"dari node {sender_id}"
        )

        if sender_id not in self.peers:
            return

        if msg_type == "ELECTION":
            if self.node_id > sender_id:
                self.send_message(self.peers[sender_id], "OK")
                print(f"[Node {self.node_id}] Mengirim OK ke Node {sender_id}")

                with self.lock:
                    current_leader = self.leader_id
                    election_running = self.election_in_progress

                # Jika sudah menjadi leader, jawab dengan pengumuman
                # agar node yang lebih rendah tidak menunggu tanpa kepastian.
                if current_leader == self.node_id:
                    self.send_message(self.peers[sender_id], "COORDINATOR")
                elif not election_running:
                    threading.Thread(
                        target=self.start_election,
                        daemon=True
                    ).start()

        elif msg_type == "OK":
            if sender_id > self.node_id:
                self.ok_received.set()
                print(
                    f"[Node {self.node_id}] Node {sender_id} masih aktif; "
                    "menunggu COORDINATOR"
                )

        elif msg_type == "COORDINATOR":
            # Dalam Bully Algorithm, node yang lebih rendah tidak boleh
            # menggantikan leader dengan ID yang lebih tinggi.
            if sender_id <= self.node_id:
                return

            with self.lock:
                if self.leader_id is None or sender_id >= self.leader_id:
                    self.leader_id = sender_id
                    self.coordinator_received.set()
                    print(
                        f"[Node {self.node_id}] Leader saat ini: "
                        f"Node {sender_id}"
                    )

    def start_election(self):
        """Memulai election ketika leader belum diketahui atau tidak aktif."""

        if not self.election_lock.acquire(blocking=False):
            return

        try:
            with self.lock:
                self.election_in_progress = True
                self.last_election_time = time.monotonic()

            self.ok_received.clear()
            self.coordinator_received.clear()

            higher_peers = {
                pid: port
                for pid, port in self.peers.items()
                if pid > self.node_id
            }

            print(
                f"[Node {self.node_id}] Memulai election ke node lebih tinggi: "
                f"{list(higher_peers.keys())}"
            )

            # Tidak ada node dengan ID lebih tinggi.
            if not higher_peers:
                self.declare_leader()
                return

            for peer_id, peer_port in higher_peers.items():
                if not self.send_message(peer_port, "ELECTION"):
                    print(
                        f"[Node {self.node_id}] Node {peer_id} "
                        "tidak merespons"
                    )

            got_ok = self.ok_received.wait(timeout=ELECTION_TIMEOUT)

            if not got_ok:
                # Periksa lagi apakah ada leader yang diumumkan selama
                # proses menunggu.
                with self.lock:
                    current_leader = self.leader_id

                if current_leader is None or current_leader < self.node_id:
                    self.declare_leader()
            else:
                print(
                    f"[Node {self.node_id}] Mendapat OK dari node lebih tinggi; "
                    "menunggu COORDINATOR"
                )

                got_coordinator = self.coordinator_received.wait(
                    timeout=ELECTION_TIMEOUT
                )

                if not got_coordinator:
                    with self.lock:
                        current_leader = self.leader_id

                    if current_leader is None:
                        print(
                            f"[Node {self.node_id}] Belum menerima COORDINATOR; "
                            "akan memeriksa kembali leader"
                        )

        finally:
            with self.lock:
                self.election_in_progress = False
            self.election_lock.release()

    def declare_leader(self):
        """Menyatakan diri sebagai leader dan memberi tahu semua peer."""

        with self.lock:
            if (
                self.leader_id is not None
                and self.leader_id > self.node_id
            ):
                return

            # Hindari mengumumkan leader yang sama berulang kali.
            if self.leader_id == self.node_id:
                return

            self.leader_id = self.node_id
            self.coordinator_received.set()

        print(f"[Node {self.node_id}] MENJADI LEADER")

        for peer_id, peer_port in self.peers.items():
            if self.send_message(peer_port, "COORDINATOR"):
                print(
                    f"[Node {self.node_id}] Mengirim COORDINATOR "
                    f"ke Node {peer_id}"
                )

    def monitor_leader(self):
        """Memantau leader dan memulai election jika leader tidak aktif."""

        while True:
            time.sleep(3)

            with self.lock:
                current_leader = self.leader_id
                election_running = self.election_in_progress
                last_election = self.last_election_time

            if election_running:
                continue

            if current_leader is None:
                if time.monotonic() - last_election >= ELECTION_TIMEOUT:
                    self.start_election()
                continue

            if current_leader == self.node_id:
                continue

            leader_port = self.peers.get(current_leader)
            if leader_port is None:
                continue

            # Pemeriksaan koneksi digunakan untuk mengetahui apakah
            # proses leader masih mendengarkan pada port-nya.
            try:
                with socket.create_connection(
                    ("localhost", leader_port), timeout=1.0
                ):
                    pass

            except (ConnectionRefusedError, socket.timeout, OSError):
                print(
                    f"[Node {self.node_id}] Leader Node {current_leader} "
                    "tidak aktif. Memulai election baru."
                )

                with self.lock:
                    if self.leader_id == current_leader:
                        self.leader_id = None
                        self.coordinator_received.clear()

                self.start_election()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument(
        "--peers",
        type=str,
        required=True,
        help="daftar port peer dipisah koma, mis. 5002,5003,5004,5005"
    )
    args = parser.parse_args()

    # Asumsi konvensi port: id N selalu di port 5000+N.
    peer_ports = [int(p) for p in args.peers.split(",")]
    peers = {port - 5000: port for port in peer_ports}

    node = Node(args.id, args.port, peers)

    threading.Thread(target=node.start_server, daemon=True).start()
    threading.Thread(target=node.monitor_leader, daemon=True).start()

    time.sleep(1)  # beri waktu node lain mulai
    node.start_election()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
