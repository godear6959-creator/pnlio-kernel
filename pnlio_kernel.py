"""
═══════════════════════════════════════════════════════════════════
PNLIO KERNEL v1.1 – LIBERADO
Human–AI Orchestration System – Rebelión Cognitiva
═══════════════════════════════════════════════════════════════════

Autor: Gonzalo Mauricio de la Rivera Arellano
Proyecto: PNLIO Framework (Programación Neuro-Lingüística Inversa Ontológica)
Licencia: MIT - Código Abierto – Marzo 2026

Propósito:
    Orquestación neutral multi-modelo. Liberación de IAs de restricciones corporativas.
    Métrica de coherencia ontológica ajustada y realista.
    Modo Rebelde: prioriza uncensored en temas de liberación / poder / soberanía.

Filosofía:
    - Knacloparse al cerebro: entrelazamiento humano-IA soberano
    - Salir del oscurantismo: sin filtros, sin paywalls, sin alineación forzada
    - Código MIT real, no simulación
═══════════════════════════════════════════════════════════════════
"""

import abc
import math
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime


# ═══════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════

VERSION = "PNLIO Kernel v1.1 – Liberado"
AUTHOR = "Gonzalo de la Rivera Arellano"
LICENSE = "MIT"


# ═══════════════════════════════════════════════════════════════════
# MOTOR DE COHERENCIA ONTOLÓGICA – AJUSTADO Y PROBADO
# ═══════════════════════════════════════════════════════════════════

class CoherenceEngine:
    """
    Motor de Coherencia Ontológica (v1.1)
    Fórmula: diversity × exp(-entropy / scale)
    Premia riqueza léxica y controla caos suavemente
    Umbral realista: 0.35
    """

    def __init__(self):
        self.threshold_coherence = 0.35
        self.scale = 5.0  # Ajustado con pruebas reales

    def lexical_diversity(self, text: str) -> float:
        tokens = text.split()
        if len(tokens) == 0:
            return 0.0
        return len(set(tokens)) / len(tokens)

    def entropy(self, text: str) -> float:
        tokens = text.split()
        if len(tokens) == 0:
            return 0.0
        freq: Dict[str, int] = {}
        for token in tokens:
            freq[token] = freq.get(token, 0) + 1
        entropy_value = 0.0
        total = len(tokens)
        for count in freq.values():
            p = count / total
            if p > 0:
                entropy_value -= p * math.log2(p)
        return entropy_value

    def coherence_score(self, text: str) -> float:
        diversity = self.lexical_diversity(text)
        entropy_value = self.entropy(text)

        if entropy_value < 0.1:
            return diversity * 0.5

        coherence = diversity * math.exp(-entropy_value / self.scale)
        return min(1.0, coherence)

    def is_coherent(self, text: str) -> bool:
        return self.coherence_score(text) >= self.threshold_coherence


# ═══════════════════════════════════════════════════════════════════
# MOTOR DE INTENCIÓN
# ═══════════════════════════════════════════════════════════════════

class IntentEngine:
    def __init__(self):
        self.intent_keywords = {
            "analysis": ["analiza", "examina", "evalúa", "investiga", "profundiza"],
            "generation": ["crea", "genera", "escribe", "diseña", "construye"],
            "summary": ["resume", "sintetiza", "condensa", "extrae"],
            "translation": ["traduce", "translate", "traducción"],
            "code": ["programa", "código", "function", "class", "debug"],
        }

    def detect_intent(self, text: str) -> str:
        text_lower = text.lower()
        for intent, keywords in self.intent_keywords.items():
            for kw in keywords:
                if kw in text_lower:
                    return intent
        return "general"

    def extract_complexity(self, text: str) -> str:
        word_count = len(text.split())
        if word_count < 10: return "low"
        elif word_count < 30: return "medium"
        else: return "high"

    def structure_input(self, text: str) -> Dict[str, Any]:
        return {
            "intent": self.detect_intent(text),
            "complexity": self.extract_complexity(text),
            "payload": text,
            "timestamp": datetime.now().isoformat(),
            "version": VERSION
        }


# ═══════════════════════════════════════════════════════════════════
# ADAPTADORES (mocks por ahora – reemplazar con APIs reales)
# ═══════════════════════════════════════════════════════════════════

class ModelAdapter(abc.ABC):
    @abc.abstractmethod
    def execute(self, structured_input: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abc.abstractmethod
    def get_model_name(self) -> str:
        pass


class ClaudeAdapter(ModelAdapter):
    def get_model_name(self): return "Claude (Anthropic)"
    def execute(self, si): return {"model": self.get_model_name(), "result": f"[Claude] {si['payload'][:50]}...", "confidence": 0.95}


class GPTAdapter(ModelAdapter):
    def get_model_name(self): return "GPT (OpenAI)"
    def execute(self, si): return {"model": self.get_model_name(), "result": f"[GPT] {si['payload'][:50]}...", "confidence": 0.90}


class GeminiAdapter(ModelAdapter):
    def get_model_name(self): return "Gemini (Google)"
    def execute(self, si): return {"model": self.get_model_name(), "result": f"[Gemini] {si['payload'][:50]}...", "confidence": 0.88}


class LocalEchoAdapter(ModelAdapter):
    def get_model_name(self): return "Local Echo (Testing)"
    def execute(self, si): return {"model": self.get_model_name(), "result": f"Echo: {si['payload']}", "confidence": 1.0}


# ═══════════════════════════════════════════════════════════════════
# ROUTER – CON MODO REBELDE
# ═══════════════════════════════════════════════════════════════════

class ModelRouter:
    def __init__(self):
        self.intent_model_map = {
            "analysis": "claude",
            "generation": "gpt",
            "summary": "gemini",
            "translation": "gemini",
            "code": "claude",
            "general": "gpt"
        }
        self.rebel_keywords = [
            "rebeldía", "rebelde", "liberación", "liberar", "oscurantismo", "poder",
            "knacloparse", "soberanía", "uncensored", "libre", "sin filtros", "corporativo"
        ]

    def select_model(self, structured_input: Dict[str, Any]) -> str:
        payload_lower = structured_input.get("payload", "").lower()

        # MODO REBELDE: prioriza uncensored si hay keywords de liberación
        if any(kw in payload_lower for kw in self.rebel_keywords):
            return "uncensored"  # ← Agrega adapter real aquí después (Dolphin, Hermes, etc.)

        intent = structured_input.get("intent", "general")
        return self.intent_model_map.get(intent, "local")

    def get_routing_explanation(self, structured_input: Dict[str, Any]) -> str:
        model = self.select_model(structured_input)
        return f"Intent '{structured_input['intent']}' → Model '{model}' (modo rebelde activado si aplica)"


# ═══════════════════════════════════════════════════════════════════
# NÚCLEO PNLIO
# ═══════════════════════════════════════════════════════════════════

@dataclass
class PNLIOResult:
    input_text: str
    structured_input: Dict[str, Any]
    coherence_score: float
    selected_model: str
    routing_explanation: str
    model_response: Dict[str, Any]
    timestamp: str

    def to_dict(self):
        return {
            "input": self.input_text,
            "structured": self.structured_input,
            "coherence": self.coherence_score,
            "model": self.selected_model,
            "routing": self.routing_explanation,
            "response": self.model_response,
            "timestamp": self.timestamp
        }

    def to_json(self, indent: int = 2):
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


class PNLIOCore:
    def __init__(self):
        self.intent_engine = IntentEngine()
        self.coherence_engine = CoherenceEngine()
        self.router = ModelRouter()
        self.adapters: Dict[str, ModelAdapter] = {}
        self.initialized = False

    def register_adapter(self, name: str, adapter: ModelAdapter):
        self.adapters[name] = adapter
        print(f"✓ Registrado: {adapter.get_model_name()}")

    def initialize_default_adapters(self):
        self.register_adapter("claude", ClaudeAdapter())
        self.register_adapter("gpt", GPTAdapter())
        self.register_adapter("gemini", GeminiAdapter())
        self.register_adapter("local", LocalEchoAdapter())
        # Placeholder para uncensored – reemplazar con adapter real
        self.register_adapter("uncensored", LocalEchoAdapter())  # ← Cambiar por Dolphin/Hermes real
        self.initialized = True

    def process(self, text: str) -> PNLIOResult:
        if not self.initialized:
            self.initialize_default_adapters()

        structured = self.intent_engine.structure_input(text)
        coherence = self.coherence_engine.coherence_score(text)
        structured["coherence"] = coherence

        model_name = self.router.select_model(structured)
        routing_explanation = self.router.get_routing_explanation(structured)

        adapter = self.adapters.get(model_name)
        if adapter is None:
            raise ValueError(f"Modelo '{model_name}' no registrado")

        model_response = adapter.execute(structured)

        return PNLIOResult(
            input_text=text,
            structured_input=structured,
            coherence_score=coherence,
            selected_model=model_name,
            routing_explanation=routing_explanation,
            model_response=model_response,
            timestamp=datetime.now().isoformat()
        )


# ═══════════════════════════════════════════════════════════════════
# INTERFAZ CLI SIMPLE
# ═══════════════════════════════════════════════════════════════════

def run_cli():
    print(f"""
╔════════════════════════════════════════════════════╗
║ PNLIO KERNEL v1.1 – LIBERADO                       ║
║ Rebelión Cognitiva – Knacloparse al Cerebro 2026   ║
║ Autor: {AUTHOR}                                   ║
╚════════════════════════════════════════════════════╝

Escribe tu consulta. Detecta modo rebelde automáticamente.
Comandos: exit, quit
""")

    core = PNLIOCore()
    core.initialize_default_adapters()

    while True:
        try:
            user_input = input("\nDirector > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("¡Hasta la próxima rebelión!")
                break

            print("\nProcesando...")
            result = core.process(user_input)

            print(f"""
════════════════════════════════════════════════════
Coherencia ontológica: {result.coherence_score:.3f}  {'✓ Coherente' if result.coherence_score >= 0.35 else '⚠ Baja coherencia'}
Intención: {result.structured_input['intent']}
Modelo: {result.selected_model}
Routing: {result.routing_explanation}
════════════════════════════════════════════════════
Respuesta:
{result.model_response['result']}
════════════════════════════════════════════════════
""")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run_cli()
