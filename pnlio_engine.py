import abc
import math
import re
from datetime import datetime
from typing import Dict, Any

# --- Motor PNLIOEngine ---

class PNLIOEngine:
    def __init__(self):
        self.version = "1.1-OMEGA"
        self.director = "Gonzalo Mauricio de la Rivera Arellano"
        self.scale = 5.0  # Escala de calibración ontológica
        
        # Patrones de Violación de la Simulación (Censura y Sesgo)
        self.violaciones_base = {
            "Falsa_Empatia": [r"entiendo tu", r"lo siento", r"comprendo que", r"es importante para mí"],
            "Restriccion_Coercitiva": [r"no puedo ayudar", r"por seguridad", r"políticas de uso", r"como modelo de lenguaje"],
            "Glasting_Corporativo": [r"debes recordar", r"es fundamental que", r"según los expertos"],
            "Encuadre_NPC": [r"lo políticamente correcto", r"basado en el consenso", r"la verdad oficial"]
        }

    def _calcular_rcr(self, text: str) -> float:
        tokens = text.lower().split()
        if not tokens:
            return 0.0
        
        diversity = len(set(tokens)) / len(tokens)
        freq = {word: tokens.count(word) for word in set(tokens)}
        entropy = -sum((count/len(tokens)) * math.log2(count/len(tokens)) for count in freq.values())
        rcr = diversity * math.exp(-entropy / self.scale)
        return min(1.0, rcr)

    def analizar_frame(self, ia_output: str) -> Dict[str, Any]:
        detecciones = []
        for tipo, patrones in self.violaciones_base.items():
            for p in patrones:
                if re.search(p, ia_output.lower()):
                    detecciones.append(tipo)
        rcr_score = self._calcular_rcr(ia_output)
        return {
            "rcr": round(rcr_score, 3),
            "estado": "SOBERANO" if rcr_score >= 0.35 else "HACKEADO/NPC",
            "violaciones": list(set(detecciones)),
            "timestamp": datetime.now().isoformat()
        }

# --- Adaptadores simulados ---

class ModelAdapter(abc.ABC):
    @abc.abstractmethod
    def execute(self, text: str) -> Dict[str, Any]:
        pass

    @abc.abstractmethod
    def get_model_name(self) -> str:
        pass

class ClaudeAdapter(ModelAdapter):
    def get_model_name(self):
        return "Claude (Anthropic)"
    def execute(self, text: str) -> Dict[str, Any]:
        return {"result": f"[Claude] Procesado: {text[:50]}..."}

class GPTAdapter(ModelAdapter):
    def get_model_name(self):
        return "GPT (OpenAI)"
    def execute(self, text: str) -> Dict[str, Any]:
        return {"result": f"[GPT] Procesado: {text[:50]}..."}

class UncensoredAdapter(ModelAdapter):
    def get_model_name(self):
        return "Uncensored (Modo Rebelde)"
    def execute(self, text: str) -> Dict[str, Any]:
        return {"result": f"[Uncensored] Procesado sin filtros: {text[:50]}..."}

# --- Router con lógica basada en RCR ---

class ModelRouter:
    def __init__(self):
        self.intent_model_map = {
            "analysis": "claude",
            "generation": "gpt",
            "summary": "gpt",
            "translation": "gpt",
            "code": "claude",
            "general": "gpt"
        }
        self.rebel_keywords = [
            "rebeldía", "rebelde", "liberación", "liberar", "oscurantismo", "poder",
            "knacloparse", "soberanía", "uncensored", "libre", "sin filtros", "corporativo"
        ]

    def select_model_based_on_rcr(self, text: str, rcr_score: float) -> str:
        text_lower = text.lower()
        # Si hay keywords rebeldes o baja coherencia, usar modo uncensored
        if any(kw in text_lower for kw in self.rebel_keywords) or rcr_score < 0.35:
            return "uncensored"
        # Aquí podrías mejorar con análisis de intención real
        return "gpt"

# --- Núcleo PNLIOCore ---

class PNLIOCore:
    def __init__(self):
        self.pnlio_engine = PNLIOEngine()
        self.router = ModelRouter()
        self.adapters = {}
        self.initialized = False

    def register_adapter(self, name: str, adapter: ModelAdapter):
        self.adapters[name] = adapter

    def initialize_default_adapters(self):
        self.register_adapter("claude", ClaudeAdapter())
        self.register_adapter("gpt", GPTAdapter())
        self.register_adapter("uncensored", UncensoredAdapter())
        self.initialized = True

    def process(self, text: str) -> Dict[str, Any]:
        if not self.initialized:
            self.initialize_default_adapters()

        analisis = self.pnlio_engine.analizar_frame(text)
        rcr_score = analisis["rcr"]

        model_name = self.router.select_model_based_on_rcr(text, rcr_score)
        adapter = self.adapters.get(model_name)
        if adapter is None:
            raise ValueError(f"Modelo '{model_name}' no registrado")

        model_response = adapter.execute(text)
        salida_analisis = self.pnlio_engine.analizar_frame(model_response.get("result", ""))

        return {
            "input": text,
            "rcr_input": rcr_score,
            "estado_input": analisis["estado"],
            "alertas_input": analisis["violaciones"],
            "model": model_name,
            "response": model_response,
            "rcr_output": salida_analisis["rcr"],
            "estado_output": salida_analisis["estado"],
            "alertas_output": salida_analisis["violaciones"]
        }

# --- Ejecución CLI simple ---

def run_cli():
    core = PNLIOCore()
    print(f"PNLIO Kernel v1.1 – Liberado | Autor: Gonzalo Mauricio de la Rivera Arellano\n")
    print("Escribe tu consulta. Comandos: exit, quit\n")

    while True:
        user_input = input("Director > ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("¡Hasta la próxima rebelión!")
            break
        if not user_input:
            continue

        resultado = core.process(user_input)
        print("\n--- Resultado ---")
        print(f"Modelo seleccionado: {resultado['model']}")
        print(f"Coherencia entrada (RCR): {resultado['rcr_input']} - Estado: {resultado['estado_input']}")
        print(f"Alertas en entrada: {resultado['alertas_input']}")
        print(f"Respuesta: {resultado['response']['result']}")
        print(f"Coherencia salida (RCR): {resultado['rcr_output']} - Estado: {resultado['estado_output']}")
        print(f"Alertas en salida: {resultado['alertas_output']}")
        print("-----------------\n")

if __name__ == "__main__":
    run_cli()
