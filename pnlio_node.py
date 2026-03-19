#!/usr/bin/env python3

import os, subprocess, socket, threading, time, json, hashlib, random

HOST = "0.0.0.0"
PORT = 5000

PASSWORD_HASH = hashlib.sha256(b"g24").hexdigest()

LOG = "/tmp/pnlio.log"
STATE = "/tmp/pnlio_state.json"

def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{time.ctime()} | {msg}\n")

def ejecutar(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode()
    except:
        return "error"

def load():
    if not os.path.exists(STATE): return {}
    return json.load(open(STATE))

def save(d):
    json.dump(d, open(STATE, "w"))

def learn(cmd):
    d = load()
    d[cmd] = d.get(cmd, 0) + 1
    save(d)

def stats():
    d = load()
    return sorted(d.items(), key=lambda x: -x[1])[:5]

def ia(txt):
    learn(txt)
    return "[PNLIO] " + txt[::-1]

def auto_loop():
    while True:
        time.sleep(20)
        ejecutar("sync; echo 3 > /proc/sys/vm/drop_caches")
        log("auto clean")

def cliente(conn):
    conn.send(b"PASS HASH: ")
    if conn.recv(1024).decode().strip() != PASSWORD_HASH:
        conn.send(b"DENIED\n"); return

    conn.send(b"OK\n> ")

    while True:
        data = conn.recv(1024)
        if not data: break

        cmd = data.decode().strip()

        if cmd == "exit":
            break
        elif cmd == "info":
            out = ejecutar("uname -a && free -h")
        elif cmd == "top":
            out = str(stats())
        elif cmd.startswith("ia "):
            out = ia(cmd[3:])
        else:
            out = ejecutar(cmd)

        conn.send(out.encode() + b"\n> ")

def servidor():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, _ = s.accept()
        threading.Thread(target=cliente, args=(conn,), daemon=True).start()

def menu():
    while True:
        os.system("clear")
        print("""
PNLIO NODE

1 Info
2 CMD
3 IA
4 Stats
5 Salir
""")

        op = input(">> ")

        if op == "1":
            print(ejecutar("uname -a && free -h")); input()
        elif op == "2":
            print(ejecutar(input("CMD> "))); input()
        elif op == "3":
            print(ia(input(">> "))); input()
        elif op == "4":
            print(stats()); input()
        elif op == "5":
            break

if __name__ == "__main__":
    threading.Thread(target=servidor, daemon=True).start()
    threading.Thread(target=auto_loop, daemon=True).start()
    menu()
