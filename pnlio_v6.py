"""
PNLIO v6 – OLLAMA LOCAL KERNEL
Autor: Gonzalo Mauricio de la Rivera Arellano (Godear24)
IA local gratis con Ollama + phi3
"""

import math
import json
import re
import os
import urllib.request
from datetime import datetime
from collections import Counter
from pathlib import Path

def color(text, col=""):
    colors = {"green":"\033[92m","red":"\033[91m","yellow":"\033[93m","cyan":"\033[96m","magenta":"\033[95m","reset":"\033[0m"}
    return f"{colors.get(col,colors['reset'])}{text}{colors['reset']}"

class RCRMetric:
    @staticmethod
    def tokenize(text):
        tokens = re.split(r"\W+", text.lower())
        return [t for t in tokens if t]

    @staticmethod
    def compute(text):
        tokens = RCRMetric.tokenize(text)
        n = len(tokens)
        if n < 2:
            return {"tokens":n,"diversity":0,"entropy":0,"rcr":0}
        div = len(set(tokens))/n
        counts = Counter(tokens)
        ent = -sum((c/n)*math.log2(c/n) for c in counts.values())
        ent_norm = ent/math.log2(n)
        rcr = (div**1.1)*(ent_norm**1.8)
        return {"tokens":n,"diversity":round(div,3),"entropy":round(ent_norm,3),"rcr":round(rcr,3)}

class SymbioticMemory:
    def __init__(self, file="symbiosis_memory.json"):
        self.file = Path(file)
        if not self.file.exists():
            self.file.write_text("[]", encoding="utf-8")

    def add(self, human, ai, rcr, intent):
        try:
            memory = json.loads(self.file.read_text(encoding="utf-8"))
            memory.append({"time":datetime.now().isoformat(),"human":human,"ai":ai,"rcr":rcr,"intent":intent})
            self.file.write_text(json.dumps(memory,indent=2,ensure_ascii=False),encoding="utf-8")
        except Exception as e:
            print(color(f"Error memoria: {e}","red"))

    def show(self, limit=5):
        try:
            memory = json.loads(self.file.read_text(encoding="utf-8"))
            for entry in memory[-limit:]:
                print(color(f"[{entry['time']}] {entry['intent']} | RCR:{entry['rcr']}","yellow"))
                print("H:", entry["human"][:80])
                print("IA:", entry["ai"][:80],"\n")
        except:
            print("Memoria vacía.")

class OllamaAdapter:
    def __init__(self, model="phi3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def run(self, text, intent="explore"):
        system_prompts = {
            "analysis": "Eres un asistente analítico. Responde con rigor y honestidad.",
            "creative": "Eres un motor creativo. Responde con metáforas potentes.",
            "explore": "Eres un explorador libre. Conecta ideas inesperadas."
        }
        prompt = f"{system_prompts.get(intent,'')}\n\nUsuario: {text}\nRespuesta:"
        data = json.dumps({"model":self.model,"prompt":prompt,"stream":False}).encode("utf-8")
        try:
            req = urllib.request.Request(self.url, data=data, headers={"Content-Type":"application/json"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result.get("response","Sin respuesta")
        except Exception as e:
            return f"[Error Ollama: {e}]"

class ModelRouter:
    analysis_words = ["analiza","explica","teoria","estructura","por qué","cómo","define","qué es"]
    creative_words = ["imagina","arte","poema","crea","historia","sueña","inventa"]

    def detect(self, text):
        t = text.lower()
        if any(w in t for w in self.analysis_words): return "analysis"
        if any(w in t for w in self.creative_words): return "creative"
        return "explore"

class PNLIOKernel:
    def __init__(self):
        self.router = ModelRouter()
        self.memory = SymbioticMemory()
        self.ollama = OllamaAdapter()

    def process(self, text):
        intent = self.router.detect(text)
        print(color(f"\nProcesando [{intent}]...","magenta"))
        response = self.ollama.run(text, intent)
        metrics = RCRMetric.compute(response)
        self.memory.add(text, response, metrics["rcr"], intent)
        return response, metrics, intent

def main():
    kernel = PNLIOKernel()
    print(color("""
╔══════════════════════════════════════════════════════╗
║     PNLIO v6 – OLLAMA LOCAL KERNEL                   ║
║     Autor: Gonzalo M. de la Rivera (Godear24)        ║
║     IA local gratis – phi3 corriendo en tu PC        ║
╚══════════════════════════════════════════════════════╝
Comandos: memoria | exit
""","cyan"))

    while True:
        try:
            user = input(color("DIRECTOR >> ","cyan")).strip()
        except (KeyboardInterrupt, EOFError):
            print(color("\nSinfonía terminada.","green"))
            break
        if not user: continue
        if user.lower() in ["exit","quit","salir"]:
            print(color("Sinfonía terminada.","green"))
            break
        if user.lower() == "memoria":
            kernel.memory.show()
            continue

        response, metrics, intent = kernel.process(user)
        print(color(f"\nPNLIO [{intent}] >>","yellow"))
        print(response)
        print(color(f"\nRCR:{metrics['rcr']} | tokens:{metrics['tokens']} | div:{metrics['diversity']} | entropy:{metrics['entropy']}","cyan"))
        print("-"*60+"\n")

if __name__ == "__main__":
    main()
