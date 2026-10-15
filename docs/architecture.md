# Arquitectura

## MT5 Runner (forex / oro)

```mermaid
flowchart TB
    subgraph VPS[VPS Windows]
        MT5[MetaTrader 5] <--> RUN[Runner en vivo]
        RUN --> WD[Watchdog + autoactualización]
    end
    API[FastAPI + PostgreSQL] <--> UI[Dashboard Next.js]
    RUN --> API
    RUN --> TG[Alertas Telegram]
    BT[Backtest + optimizador] --> GATE{Compuertas de validación}
    GATE --> RUN
    PAR[Paridad vivo/backtest diaria] --> TG
```

- Optimización y validación offline; el runner solo recibe configuraciones que pasaron todas las compuertas.
- Alarma diaria de paridad entre resultados en vivo y backtest para detectar deriva.

## Solana Bot (memecoins)

```mermaid
flowchart LR
    FEED[Eventos de nuevos pools] --> FIL[Filtros de calidad y seguridad]
    FIL --> SIM[Simulación realista de costos]
    SIM --> PAPER[Paper trading]
    PAPER --> VER{Veredicto live-ready}
    VER -- sí --> LIVE[Ejecución live]
    PAPER --> DASH[Dashboard local solo lectura]
    LIVE --> WD[Runner + watchdog]
```

- Dashboard en `127.0.0.1`, solo lectura.
- Clave de wallet únicamente por entorno; nunca en logs ni en disco versionado.

## Camello (cripto, paper)

```mermaid
flowchart LR
    F[Feeds] --> ST[Snapshot por vela<br/>sin lookahead]
    ST --> J[Modelo por vela]
    J --> DET[Decisión determinista]
    DET --> RG[Risk gate + kill switch]
    RG --> EX[Ejecución paper]
    EX --> JR[(Journal + calibración)]
    JR --> NOC[Revisión nocturna por LLM]
    NOC --> GT{Gate de backtest}
    GT --> DET
```

- El LLM nunca califica su propio backtest ni toca límites de riesgo.
- Test de fuga de datos y fills en la apertura de la vela siguiente.
