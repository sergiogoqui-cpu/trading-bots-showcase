# DEVLOG

Notas técnicas cortas, de la más reciente a la más antigua. Solo ingeniería: arquitectura, latencia, errores, tooling. Nunca parámetros, umbrales, resultados de estrategias ni credenciales.

Agrega una nota con `python scripts/devlog.py "texto"` (opcional: `--tag ws --tag python`).

<!-- DEVLOG:START -->
## 2026-10-15
- `[alerts]` `[release]` Publicado bot-telegram-alerts 0.1.0: alertas con deduplicacion, limite de frecuencia y reintentos, sin exponer credenciales
- `[metrics]` `[release]` Publicado backtest-metrics 0.1.0: metricas de rendimiento puras (drawdown, CAGR, Sortino) con calendario 24/7 y sin dependencias
- `[http]` `[release]` Publicado http-guard 0.1.0: fetch resiliente en TypeScript con reintentos, backoff con jitter y circuit breaker por host
- `[mt5]` `[release]` Publicado mt5-data-fmt 0.1.0: DataFrames UTC desde MetaTrader 5, flags decodificados, deteccion de huecos y Parquet
- `[logging]` `[python]` Publicado safe-logger 0.1.0: logging que enmascara credenciales y neutraliza inyeccion de logs, sin dependencias
- `[ws]` `[python]` Publicado ws-resilient 0.1.0: cliente WebSocket con backoff y jitter, idle timeout y deteccion de huecos de secuencia
- `[docs]` Primer DEVLOG: separación "framework abierto / estrategia cerrada" y arquitectura de los tres bots publicada.
<!-- DEVLOG:END -->
