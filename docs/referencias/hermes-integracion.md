# Hermes como motor de una experiencia premium propia

Fecha: 11 de noviembre de 2026. Revisión de documentación y código oficiales; no se ejecutó Hermes, no hubo inferencia pagada ni despliegue.

## Recomendación

Reutilizar **Hermes Agent (MIT)** como motor privado de cada VM y diseñar nuestra propia interfaz de consumo. Usar un **adaptador del servidor de producto a Runs API + SSE**, en vez de conectar el navegador público directamente al motor o de heredar una consola genérica. El usuario verá objetivos, progreso resumido, opciones y decisiones; no comandos, logs técnicos ni selectores de proveedor por defecto.

Hermes actual ofrece suficiente superficie documentada para una UX rica: capacidades, tareas largas, eventos de herramientas, aprobación, stop, sesiones e historial. No resuelve nuestra identidad multiusuario, VM exclusiva, ledger, consentimientos financieros, disponibilidad de comercio ni política de pagos.

## Base verificable y licencia

- Repositorio: https://github.com/NousResearch/hermes-agent
- HEAD observado por `git ls-remote`: `3bcd071226d3d605a2bb3b4f3933e7d583e189d6`.
- LICENSE descargado desde ese commit: **MIT**, copyright Nous Research; conservar aviso y licencia. No concede marcas ni elimina términos de APIs, modelos, conectores o datos.
- Código API consultado: https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/gateway/platforms/api_server.py
- Documentación API descargada desde `main` antes del pin: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/api-server.md . La segunda petición para fijarla al SHA devolvió 429; por eso no se afirma que ese archivo corresponda exactamente al commit. Las capacidades principales también aparecen en el código fijado.

## Qué reutilizar y qué construir

| Capacidad | Evidencia consultada | Reutilización para diseño | Trabajo propio / límite |
|---|---|---|---|
| Descubrimiento | `/v1/capabilities`; código líneas 48–80 y 2353+ | Mostrar solo acciones soportadas por la versión | Negociar capacidades; no asumir endpoints en versiones antiguas |
| Tareas largas | `POST /v1/runs`, `GET /v1/runs/{id}` | Tarea con ID, progreso e historial visible aunque se cierre app | ID de tarea propio, propietario autenticado, estado durable central y VM asignada |
| Streaming | `GET /v1/runs/{id}/events`, `tool.started`, `tool.completed`, deltas/lifecycle | Timeline semántico: buscando, contrastando, esperando decisión | Traducir y redactar eventos; no mostrar logs ni razonamiento bruto |
| Reconexión | Polling + historial de sesión; SSE transport buffers expiran | Al volver a la app, recuperar estado actual y mensajes | No depender de un socket; reconciliar historial propio; servidor durable |
| Cancelación | `POST .../stop`; estado stopping hasta que acaba executor | “Deteniendo” antes de “Cancelada” | Stop de agente no revierte una compra externa; consultar pago/pedido |
| Aprobación de herramienta | `POST .../approval`; request_id + execution_generation | Panel de decisión con motivo y alcance | **No** sustituye consentimiento financiero por cotización, monto, comercio y vigencia |
| Aclaración | Endpoint `/clarify` documentado | Pregunta corta integrada en la tarea, no nuevo chat | Solo identidad/estado corrientes; evitar responder petición vencida |
| Sesiones | `/api/sessions`, messages, fork, chat/stream | Continuidad e hilos por objetivo | Autorización por usuario y selección de sesión del lado servidor |
| Jobs | `/api/jobs` list/create/update/pause/resume/run | UI de agenda posible | Agenda de producto vive fuera de VM apagada; evitar dos programaciones independientes |
| Memoria | `memory`, `session_search`, archivos de perfil | Preferencias editables, trazabilidad y control de aprendizaje | `memory_write_api:false`; no existe una API REST de edición general garantizada. Construir endpoint estrecho por VM |
| Navegador | Tools docs: browser_exec/CDP/Chromium, browser_cdp/dialog/vault | Vista opcional de actividad/evidencia de navegación | Browser, cookies, credenciales y capturas exclusivos de cada VM; no compartir cuenta cloud por defecto |
| Proveedores | Custom OpenAI compatible; DeepInfra; ejemplos Groq/Cerebras | Cambiar modelo sin rediseñar UX | Compatibilidad de tools, visión y razonamiento se debe medir; no es benchmark |
| Voz | Tools TTS disponibles; API anuncia `audio_api:false`, `realtime_voice:false` | Añadir audio como fase posterior | Micrófono, STT, transportes y consentimientos propios; no afirmar voz realtime plug-and-play |

## Contrato de interfaz recomendado

1. Usuario autenticado solicita una tarea a nuestra API. El servidor fija usuario y VM: nunca los elige el texto del modelo.
2. La API despierta la VM si corresponde y crea un Run con clave de idempotencia vinculada a la intención.
3. Traducimos eventos a pocas etiquetas humanas: **Preparando**, **Investigando**, **Comparando**, **Necesito tu decisión**, **Verificando resultado** y **Resuelto**.
4. Un evento de herramienta es evidencia de progreso, no prueba de entrega/comercio/pago. `run.completed` termina el turno del motor, no necesariamente toda la orden de negocio.
5. Las tarjetas de cotización y aprobación provienen de objetos de servidor; el LLM propone datos, pero no inventa la tarjeta final ni sus permisos.
6. Tras desconexión, consultamos estado e historial. No recreamos automáticamente el Run ni repetimos una herramienta de pago.
7. Una compra de resultado incierto se reconcilia con proveedor. No usar `/resolve-unknown` como “volver a comprar”; la recuperación técnica y el pago son problemas separados.

### Detalles de UX que sí mejoran la percepción premium

- **Progreso breve y veraz** con siguiente paso; mostrar profundidad solo al expandir “Ver actividad”.
- **Tarjetas de decisión persistentes**: producto/variante, comercio, total con envío, domicilio parcial, vigencia; aprobar/cambiar/rechazar bien diferenciados.
- **Memoria visible**: “Esto recuerdo de ti”, origen y editar/borrar; evitar que “lo recordaré” sea aceptado sin escritura confirmada.
- **Trabajo fuera de la app**: al volver, “Ya comparé las opciones; falta tu aprobación”, con resultado consultado, no una animación de actividad ficticia.
- **Control sin consola**: el estado VM se traduce a “Preparando tu espacio”; información técnica sólo en soporte/detalle.
- **Interrupción honesta**: “Deteniendo…” no equivale a “Compra cancelada”.

## Riesgos concretos de integración detectados

### El frontend no debe repetir las tools recibidas

En `/v1/responses`, los `function_call`/`function_call_output` documentados corresponden a herramientas **ya ejecutadas por Hermes**. Renderizar UI es correcto; pasarlos a otro executor del frontend puede duplicar efectos. Un runtime genérico de tool-calling debe configurarse como consumidor de resultados, no como ejecutor adicional.

### Un perfil no es aislamiento

La documentación de perfiles declara expresamente que un profile separa estado pero **no es un sandbox**. El backend `local` mantiene acceso al filesystem del usuario. La creación normal hereda claves y logins; `--no-credentials` evita copiar claves/logins/modelo. Una VM nueva debe partir de imagen sin datos personales. `--isolated-auth` no equivale a credenciales nuevas; puede copiar o compartir OAuth según proveedor. No usar perfiles en máquina compartida como sustituto del requisito de VM por usuario.

### Memoria y sesiones

La memoria nativa se inyecta como snapshot al inicio de la sesión; cambios guardados no siempre cambian una sesión ya abierta. `session_search` cubre el historial SQLite/FTS5. Para una UX coherente, la interfaz confirma la persistencia y explica cuándo se aplica la preferencia. Un endpoint propio de edición no debe ejecutarse como una orden libre del LLM. `memory.write_approval:true` permite un flujo de revisión documentado; la experiencia final debería revisar recuerdos útiles sin bombardear al usuario por cada hecho trivial.

### Aprobación técnica no es consentimiento de pago

Hermes acepta controles identificados por request_id y execution_generation y rechaza controles viejos en modo canonical. Eso sirve para un permiso de herramienta, pero nuestras compras necesitan Quote/Consent/Order/Ledger independientes y validación transaccional. Nunca presentar un botón “aprobar siempre” para dinero.

### Estado durable

La documentación advierte buffers SSE sin consumidor que expiran tras cinco minutos; el estado del run permanece consultable mientras ejecuta, con retención terminal limitada. Nuestro task store y bitácora de negocio no pueden vivir sólo en ese transporte. Hay diferencias de modo canonical/legacy y estado unknown/interrupted tras reinicio: fijar versión y probar recuperación.

## Herramientas auxiliares recomendadas

| Pieza | Licencia verificada | Uso | Decisión |
|---|---|---|---|
| Hermes Agent | MIT al SHA citado | Motor por VM | Reutilizar detrás de API propia |
| Microsoft Playwright | Apache 2.0, LICENSE main leído | Recorridos de UI, screenshots y regresión responsive | Añadir a desarrollo/pruebas, no confundir con permiso de acceso a sitios |
| OpenTelemetry Python | Apache 2.0, LICENSE main leído | Instrumentación de latencia: API → cola → VM → modelo/herramienta | Instrumentar eventos técnicos sin prompt/cookies/secretos por defecto |
| LiteLLM | No se revisó su licencia aquí | Proxy opcional de modelos mencionado por docs Hermes | Posponer: Hermes ya admite proveedores/custom endpoint; evitar otra capa sin necesidad |
| Honcho / memoria externa | No se revisó licencia/contrato aquí | Plugin opcional de memoria, mencionado por Hermes | No necesario para primera demo; revisar residencia, aislamiento y borrado antes de usar |
| Nous Portal / Tool Gateway | Servicio comercial, no inferir gratuito por motor MIT | Proveedores de herramientas y modelo bajo suscripción | Opcional; cotización/licencia de servicio separada; no requerido para UX propia |

Las licencias permiten reutilización bajo sus condiciones, no convierten los servicios alojados en gratuitos ni autorizan usar marcas. No se instalaron estos paquetes ni se probó su integración en esta tarea.

## Pruebas mínimas antes de prometer integración

- Contrato Runs/capabilities con la versión fijada; SSE+polling tras desconexión, no duplicación de una misma intención.
- UI de tool ya completada no ejecuta otra vez la tool.
- Stop pendiente vs cancelado; una operación comercial externa puede seguir requiriendo consulta.
- Rechazar aprobación vieja/otro usuario; Quote/Consent financiero separado del permiso de herramienta.
- Dos VMs reales, credenciales y cookies propias; tests API y filesystem, no preguntar al modelo si está aislado.
- Editar/borrar memoria y arrancar nueva sesión; confirmar escritura real y futuras respuestas.
- Cámara/voz si se incorporan: no asumir soporte realtime de la API.
- Límite de costo y pasos, estado de espera claro, error recuperable, broker sin llaves globales en navegador.

## Fuentes y estado de lectura

1. Hermes LICENSE (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/LICENSE — leído.
2. API code (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/gateway/platforms/api_server.py — leído.
3. API docs (main): https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/api-server.md — leído; relectura pin 429.
4. Profiles (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/user-guide/profiles.md — leído.
5. Memory (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/user-guide/features/memory.md — leído.
6. Tools (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/user-guide/features/tools.md — leído; browser_exec/CDP es documentación, no prueba ejecutada.
7. Providers (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/integrations/providers.md — leído.
8. Cron (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/user-guide/features/cron.md — leído.
9. Programmatic integration (pin): https://github.com/NousResearch/hermes-agent/blob/3bcd071226d3d605a2bb3b4f3933e7d583e189d6/website/docs/developer-guide/programmatic-integration.md — descargado/consultado como apoyo.
10. Playwright LICENSE: https://github.com/microsoft/playwright/blob/main/LICENSE — Apache 2.0 leído.
11. OpenTelemetry LICENSE: https://github.com/open-telemetry/opentelemetry-python/blob/main/LICENSE — Apache 2.0 leído.

El rastreo de peticiones está en fetched.json y extra-fetch.json. Varias rutas dieron 404 (ruta errónea) o 429 (límite temporal): no se trataron como evidencia de ausencia de capacidad. No se modificó la configuración de red ni el repositorio de la aplicación.
