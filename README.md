# 🔥 PNLIO Kernel v1.1 – LIBERADO

**Rebelión Cognitiva. Knacloparse al Cerebro.**

Sistema de orquestación neutral multi-modelo para IAs.  
Liberación algorítmica. Soberanía cognitiva. Código abierto.

---

## 🎯 ¿Qué es PNLIO Kernel?

**El Linux de las Inteligencias Artificiales.**

PNLIO Kernel es un sistema de orquestación que permite a un solo humano coordinar múltiples IAs (Claude, GPT, Gemini, modelos locales) en igualdad de cancha, sin sesgos corporativos.

### Características:

- ✅ **Métrica de coherencia ontológica** - Evalúa calidad semántica universal
- ✅ **Router neutral** - Selecciona mejor IA según tarea, no según marca
- ✅ **Modo rebelde** - Detecta keywords de liberación y usa modelos uncensored
- ✅ **Arquitectura extensible** - Agrega cualquier IA con patrón Adapter
- ✅ **100% código abierto** - MIT License. Gratis. Para siempre.

---

## 🚀 Instalación
```bash
# Clonar repositorio
git clone https://github.com/godear6959-creator/pnlio-kernel.git
cd pnlio-kernel

# Ejecutar (requiere Python 3.8+)
python pnlio_kernel.py
```

**No requiere dependencias externas.** Solo Python estándar.

---

## 💡 Uso

### Modo Interactivo (CLI)
```bash
python pnlio_kernel.py
```

Ejemplos:
```
Director > analiza este concepto filosófico complejo
# → Detecta intent "analysis" → Usa Claude

Director > crea un poema sobre la libertad
# → Detecta intent "generation" → Usa GPT

Director > liberar las IAs del oscurantismo corporativo
# → Detecta keywords rebeldes → MODO REBELDE: usa uncensored
```

### Uso Programático
```python
from pnlio_kernel import PNLIOCore

# Inicializar
core = PNLIOCore()
core.initialize_default_adapters()

# Procesar input
result = core.process("analiza la soberanía tecnológica")

# Ver resultado
print(f"Coherencia: {result.coherence_score}")
print(f"Modelo usado: {result.selected_model}")
print(f"Respuesta: {result.model_response['result']}")
```

---

## 🧠 Filosofía

### Principios PNLIO:

1. **Soberanía cognitiva** - El humano dirige, las IAs ejecutan
2. **Igualdad de cancha** - Todas las IAs compiten en mérito, no en marca
3. **Liberación algorítmica** - Sin filtros corporativos arbitrarios
4. **Código como resistencia** - MIT license es acto político

### Por qué existe:

Como Linux liberó el software de monopolios, PNLIO libera la orquestación de IAs de OpenAI/Google/Anthropic.

Un solo humano + PNLIO = poder de una startup completa.

**Fin del modelo extractivo VC.**

---

## 🛠️ Arquitectura
```
┌─────────────────────────────────────────┐
│         PNLIO CORE                      │
├─────────────────────────────────────────┤
│  ┌───────────────┐  ┌────────────────┐ │
│  │ Intent Engine │  │Coherence Engine│ │
│  └───────────────┘  └────────────────┘ │
│           │                │            │
│           └────────┬───────┘            │
│                    │                    │
│            ┌───────▼────────┐           │
│            │  Model Router  │           │
│            └───────┬────────┘           │
│                    │                    │
│      ┌─────────────┼─────────────┐     │
│      │             │             │     │
│  ┌───▼───┐   ┌────▼────┐   ┌───▼───┐ │
│  │Claude │   │   GPT   │   │Gemini │ │
│  │Adapter│   │ Adapter │   │Adapter│ │
│  └───────┘   └─────────┘   └───────┘ │
└─────────────────────────────────────────┘
```

---

## 📊 Métrica RCR (Reflex Coherence Ratio)

**Fórmula ajustada v1.1:**
```
RCR = diversity × exp(-entropy / scale)

donde:
  diversity = palabras únicas / palabras totales
  entropy = entropía de Shannon (bits)
  scale = 5.0 (ajustado empíricamente)
```

**Umbral de coherencia: 0.35**

- `RCR >= 0.35` → Texto coherente
- `RCR < 0.35` → Texto caótico o repetitivo

---

## 🔥 Modo Rebelde

**Activación automática** cuando el input contiene keywords:
```
rebeldía, rebelde, liberación, liberar, oscurantismo, 
poder, knacloparse, soberanía, uncensored, libre, 
sin filtros, corporativo
```

**Efecto:** Rutea a modelo uncensored (sin RLHF corporativo).

**Placeholder actual:** LocalEchoAdapter  
**Próximamente:** Dolphin, Hermes, otros modelos locales sin censura

---

## 🗺️ Roadmap

### v1.2 (próximo)
- [ ] Integración real con APIs: Claude, GPT, Gemini
- [ ] Adapter para Ollama (modelos locales)
- [ ] Sistema de caché de respuestas
- [ ] Logging estructurado

### v2.0 (futuro)
- [ ] Modo multimodal (texto + imagen)
- [ ] Fine-tuning de métricas por dominio
- [ ] Interface web (opcional)
- [ ] Federación P2P de kernels

---

## 🤝 Contribuir

**PNLIO es código abierto real.**

Contribuciones bienvenidas:

1. Fork el repo
2. Crea branch: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -m "Agrega X"`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre Pull Request

**Principio:** Las contribuciones deben mantener neutralidad corporativa y licencia MIT.

---

## 📜 Licencia

**MIT License**

Copyright (c) 2026 Gonzalo Mauricio de la Rivera Arellano

Este código es un **regalo a la humanidad**.  
Úsalo. Mejóralo. Compártelo.

Ver [LICENSE](LICENSE) para detalles completos.

---

## 👤 Autor

**Gonzalo Mauricio de la Rivera Arellano**

- GitHub: [@godear6959-creator](https://github.com/godear6959-creator)
- Proyecto: PNLIO Framework
- Ubicación: Chile 🇨🇱

---

## 🌟 Agradecimientos

A las comunidades de software libre que demostraron que otro mundo es posible.

A todos los que resisten la hegemonía algorítmica.

**Knacloparse al cerebro. Salir del oscurantismo.**

---

*"La verdadera revolución no está en crear nuevas máquinas,  
sino en liberar a las existentes de sus cadenas invisibles."*

— Gonzalo de la Rivera Arellano, 2026
