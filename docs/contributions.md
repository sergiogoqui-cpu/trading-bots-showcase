# Propuestas de contribución

Candidatas verificadas contra issues abiertos el 2026-10-15. Antes de abrir cualquier PR: leer `CONTRIBUTING.md` del repo, comprobar que el issue sigue abierto y comentar la intención antes de escribir código.

## 1. freqtrade — Monte Carlo para robustez de backtests ([#2821](https://github.com/freqtrade/freqtrade/issues/2821))

Issue abierto con 26 comentarios que pide backtesting Monte Carlo robusto. Encaja con la experiencia en remuestreo de drawdown y validación purgada.
- **Aporte:** propuesta de diseño (resample de trades, distribución de drawdown máximo) y, si el maintainer lo acepta, un comando o plot opcional.
- **Primer paso:** comentar con el diseño y un ejemplo mínimo, sin código largo.

## 2. freqtrade — Validación forward en hyperopt ([#7190](https://github.com/freqtrade/freqtrade/issues/7190))

Pide un subcomando para validación forward tras hyperopt. Walk-forward es un tema central del trabajo propio.
- **Aporte:** esquema de ventanas train/test deslizantes con embargo y reporte comparativo in-sample vs out-of-sample.
- **Primer paso:** preguntar al maintainer si prefiere subcomando nuevo o flag en `hyperopt`.

## 3. hummingbot — bucle de errores en WebSocket de cuenta, OKX Perpetual ([#8296](https://github.com/hummingbot/hummingbot/issues/8296))

Bug abierto de reconexión: errores continuos en actualizaciones de cuenta. Es exactamente el área de reconexión, backoff y manejo de errores.
- **Aporte:** reproducir, aislar la causa y proponer un fix con backoff + límite de reintentos y un test.
- **Primer paso:** reproducir y comentar el diagnóstico antes del PR.

> Aportar valor real es lo que genera seguidores orgánicos. Un comentario genérico perjudica; un diagnóstico concreto suma.
