# BeautifulUI aplicado a Estela — revisión 04

Fuente: [TurboKach/ai-native-react-components](https://github.com/TurboKach/ai-native-react-components/tree/05dab2d2b5f1f3e40029776e339a486d70491079), que enlaza a beautifului.dev. Commit: `05dab2d2b5f1f3e40029776e339a486d70491079`. Licencia MIT, Copyright (c) 2026 Turbo, preservada en el HTML y el paquete. No se afirma que toda la web o un catálogo PRO use esta licencia. La web directa fue bloqueada; se revisó el código del repositorio enlazado.

## Qué se incorporó

| Fuente | Adaptación al prototipo | Valor |
|---|---|---|
| `task-rows.tsx` | Cápsulas desplegables, chevron y detalles accesibles mediante `aria-expanded`, `aria-controls` e `inert`. | Ver estado y contexto sin llenar el inicio. |
| `recommendation-card.tsx` | Alternativas dentro de la tarjeta; seleccionar una actualiza título, total y destino de revisión. | Comparar sin perder el contexto ni confundir selección con autorización. |
| `prompt-bar.tsx` | Contexto adjunto visible, retirada local y atajo Ctrl/Cmd+Enter. Sin Glimm. | Saber qué acompaña la solicitud y enviar con teclado. |
| `tool-chips.tsx` | Actividad compacta con detalle desplegable; el contenido corresponde al escenario y cambia al detenerlo. | Entender preparación, trabajo pendiente y resultado sin consola técnica. |
| `approval-card.tsx` | Etapas Revisar/Autorizar ligadas a la casilla y envío explícito. Sin autoavance ni autoenvío. | Mantener claridad del alcance de compra y evitar confirmaciones accidentales. |

La traducción usa HTML/CSS/JS para mantener el concepto autónomo. Los TSX originales se entregan como fuente de referencia para la fase React; no están instalados como runtime. Se conservan vidrio monocromático, modo claro/oscuro, movimiento reducido y fondos sólidos de respaldo.

## Qué se eliminó de las demos

- Temporizadores que cambian estados a completado o producen eventos de herramientas ficticios.
- Autoenvío de la última respuesta de aprobación.
- Indicadores de confianza prefijados sin evidencia.
- Texto escrito por autoplay, dictado o conexiones ficticias.
- Glimm/WebGL arcoíris y cambios temporales de `Math.random`.

La demo sigue usando datos de ejemplo; no ejecuta tareas, llama al modelo ni compra. En producción los estados y permisos deben venir de nuestro servidor y no de los componentes.

## Reproducción

`python3 prototypes/estela/build.py` invoca `beautifului_adapt.py`, aplica las adaptaciones y preserva avisos de licencia. Los resultados de las comprobaciones del entorno original están en `docs/referencias/validacion-*.json`. Este repositorio todavía no incluye un pipeline CI.
