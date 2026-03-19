#!/bin/bash
# =========================
# INSTALAR PYTHON
# =========================
sudo apt update
sudo apt install -y python3 python3-pip netcat

# =========================
# PERMISOS
# =========================
chmod +x pnlio_node.py

# =========================
# EJECUTAR
# =========================
echo "PNLIO Node instalado. Ejecuta: python3 pnlio_node.py"
