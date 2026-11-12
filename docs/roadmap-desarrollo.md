# Roadmap completo de desarrollo y validación

Plan de referencia del 11 de noviembre de 2026. **Este documento describe etapas y pruebas propuestas; no significa que ya se hayan ejecutado.** Consulta [ESTADO.md](ESTADO.md) para la situación real al retomar.


## 01. Roadmap de desarrollo y validación

Agente personal para México | Plan ejecutable v1.0 | 11 de noviembre de 2026

> Primero construiremos una experiencia navegable con datos simulados: pedir → ver progreso → comparar → aprobar o rechazar → ver el resultado. En la primera quincena probaremos también Hermes en dos VMs exclusivas, antes de ampliar la implementación.

**Resultado del primer hito:** podrás abrir la web desde celular y computadora, recorrer una compra simulada y revisar cada pantalla. Debe quedar claro qué hará el agente, cuánto cuesta, qué permiso pide y qué ocurrió. Todavía sin fondos ni compras reales.


### Tres validaciones en cada entrega

- **Visual:** diseño consistente, texto legible, sin recortes, móvil usable y estados de carga, vacío, error y recuperación.

- **Funcional:** controles conectados a estados reales; permisos y aprobaciones validados en servidor; cerrar la app no pierde tareas.

- **De confianza:** no inventar éxito, precio, saldo ni compra. Una operación incierta aparece pendiente de verificar; nunca como terminada.


### Alcance que conservamos

PWA/web primero. Una VM CPU exclusiva y persistente por usuario con Hermes, navegador, archivos, cookies y memoria propios. Agenda y colas centrales despiertan VMs detenidas; la VM sigue trabajando con la app cerrada. Identidad, permisos financieros, consentimientos y ledger permanecen fuera de la VM.

Groq GPT-OSS-120B es candidato de texto, Qwen visual y Cerebras de evaluación; se seleccionarán por pruebas, no por TPS publicados solamente. Finco necesita identidad, contrato y sandbox. WhatsApp y apps nativas se incorporan después de validar elegibilidad y políticas.


### Cómo usaremos este plan

24 semanas de referencia con equipo disponible; los tiempos de terceros no están garantizados. Cada fase termina con una demo y evidencia. Una dependencia externa puede retrasar su entrega sin impedir el trabajo independiente. Este documento amplía el roadmap técnico; no sustituye el presupuesto y fuentes del PDF v1.2.

**Estado actual:** planificación. Las pruebas aquí descritas están pendientes de implementación/ejecución. En este encargo se creó y revisó el documento; no se desarrolló ni desplegó la aplicación.


## 02. Todas las etapas y su orden

Las semanas son relativas al arranque. F00 y F01 comparten la semana 1; F02 cierra la quincena inicial.

| Fase | Cuándo | Qué construimos | Condición para cerrar |
| --- | --- | --- | --- |
| F00 | Días 1–2 | Definir experiencia, alcance y diseño | Recorrido y componentes con estados aprobados. |
| F01 | Días 3–5 | Prototipo navegable y base del proyecto | Flujo completo simulado en móvil y escritorio. |
| F02 | Semana 2 | Hermes, modelos y dos VMs propias | Viabilidad técnica, aislamiento y tiempos medidos. |
| F03 | Semanas 3–4 | Identidad, tareas y gestor de VMs | Acceso aislado, segundo plano y recuperación. |
| F04 | Semanas 5–6 | Agente útil, comparación y memoria | Tareas del alcance con evidencia y datos propios. |
| F05 | Semana 7 | Cotizaciones, consentimiento y compra simulada | No ejecutar sin autorización válida. |
| F06 | Semana 8* | Integraciones financieras en sandbox | Pago, pedido, reversa y devolución conciliados. |
| F07 | Semanas 9–10 | Validación integral y preparación operativa | Sin defectos críticos; salida controlada. |
| F08 | Semanas 11–12* | Piloto por invitación, 25–50 personas | Tareas resueltas y postventa trazable. |
| F09 | Semanas 13–16 | Estabilización y escala 100–300 | Costos, calidad y soporte medidos. |
| F10 | Semanas 17–20* | Canales, conexiones y apps | Mismos permisos y estados en todos los canales. |
| F11 | Semanas 21–24* | Más comercios, recurrencias y continuidad | Cada flujo nuevo conserva controles y margen. |

* Finanzas, WhatsApp, OAuth, tiendas y comercios dependen de accesos/contratos. Si no están habilitados, mantener el flujo correspondiente pendiente. Un piloto de investigación o pago directo del usuario no valida la integración financiera pendiente.


## 03. Primeros diez días de trabajo

Objetivo de quincena: experiencia visible y prueba técnica pequeña, sin construir toda la plataforma.

| Día | Desarrollo / producto | Prueba y evidencia |
| --- | --- | --- |
| 1 | Elegir usuario, tres tareas y un flujo de compra. Separar servicio, fondos y pago al comercio. | Recorrido dibujado; alcances, riesgos y criterios de aceptación escritos. |
| 2 | Diseño móvil: inicio, chat/tarea, comparación, aprobación y resultado. Componentes y colores. | Revisar lectura, navegación, precio total, acciones y estados con 5 personas del perfil. |
| 3 | Base PWA y componentes; datos de prueba deterministas; rutas navegables. | Arranca en entorno de desarrollo. Sin errores de consola ni datos reales expuestos. |
| 4 | Conectar flujo simulado: crear tarea, comparar y editar condiciones. | Pantallas en 360/390/1440 px; contenido largo, vacío y carga. |
| 5 | Aprobar/rechazar/cancelar simulado; pantallas de fallo y resultado incierto. | Demo completa; revisar con teclado y celular. Congelar primera referencia visual. |
| 6 | Fijar Hermes y proveedor de modelo candidato; preparar dos VMs exclusivas de prueba. | Revisar licencia/configuración y evitar herencia de secretos o sesiones. |
| 7 | Una tarea real de investigación sin pagos por VM; medir modelo y navegador. | A/B: memoria, archivos y cookies no se cruzan; registro de latencia y tokens. |
| 8 | Persistencia, parada, despertar por agenda externa y reconexión de interfaz. | Cerrar app, reiniciar VM y recuperar tarea sin repetir efectos. |
| 9 | Lote de evaluación y ataques de contenido; repetir regresión visual. | 100 tareas propuestas para la prueba técnica; separar éxitos, fallos y bloqueos. |
| 10 | Decidir motor/modelo/perfil VM y ajustar alcance. Descomponer tickets siguientes. | Acta continuar/corregir/cambiar; evidencia visual y técnica, costos y riesgos abiertos. |

El prototipo de días 3–5 debe mostrar que es una demostración. No presenta saldos inventados como dinero disponible ni afirma que exista una compra real. Los ejemplos y cuentas son sintéticos.


## 04. F00: diseñar la experiencia mínima

Días 1–2 | Responsable: producto + UX | Backlog de referencia: P00, P01 y P20


### Qué trabajaremos primero

Un caso de uso inicial: “encuentra este producto, compara opciones y déjame aprobar una compra con tope”. Elegir categoría y comercios candidatos sin prometer integraciones no confirmadas. Añadir investigación simple y seguimiento como las otras dos tareas del lote.

| Entregable | Detalle revisable |
| --- | --- |
| Mapa del recorrido | Alta → conversación → tarea → opciones → aprobación → pedido/resultado → ayuda. |
| Navegación | Inicio, tareas, pedidos, conexiones/memoria y cuenta/soporte; nombres consistentes en móvil y escritorio. |
| Componentes | Botones, campos, tarjetas de opción, importes, fuentes, progreso, alertas, diálogos y estados de tarea. |
| Datos / contenido | Ejemplos mexicanos: MXN, domicilio parcial, variante, envío, fecha y zona horaria explícita. |
| Estados dibujados | Normal, vacío, cargando, sin conexión, error, permiso pendiente y resultado desconocido. |
| Límites de producto | Adultos; sin compra universal, transferencias libres, crédito ni autonomía financiera sin topes. |


### Cómo validaremos que se ve bien

- Caminar el prototipo en celular: ¿se entiende el siguiente paso sin explicar comandos? La acción primaria debe ser visible y el total inequívoco.

- No usar solo color para estados; acompañar con texto/icono. Diferenciar “solicitar aprobación” de “comprar” y “pago autorizado” de “pedido confirmado”.

- Revisar versiones con producto/UX/QA y registrar cambios por pantalla; no aceptar una captura bonita que omita errores o recuperación.


### Cierre de fase

> Un recorrido coherente, componentes y estados definidos, criterios por pantalla y alcance aprobado. Salida tangible: prototipo navegable de diseño; aún sin backend financiero.


## 05. F01: prototipo web y base de desarrollo

Días 3–5 | Frontend + backend + QA | P05–P06 iniciales; P10–P11 y P19 simulados

Implementar la estructura visual y un recorrido con fixtures. Las respuestas y compras son simuladas y están etiquetadas. Esta entrega permite probar la interfaz antes de depender de Finco o comercios.

| Trabajo | Resultado |
| --- | --- |
| Proyecto reproducible | README de arranque, herramientas fijadas, lockfile, variables de ejemplo sin secretos y scripts de validación. |
| PWA responsive | Inicio, chat, tareas, comparación, aprobación, pedidos y ajustes con navegación real. |
| Fixtures por estado | Escenarios repetibles de éxito, datos largos, sin resultados, error, precio cambiado y pago desconocido. |
| Contrato de API propuesto | Identidad, Task, Quote, Consent, Payment y Order tipados; separar mock de producción. |
| CI mínima | Build, revisión de tipos, pruebas de reglas implementadas y recorrido de interfaz simulado. |
| Entornos | Desarrollo/staging/producción separados por configuración; nunca conectar mocks al dinero real. |


### Pruebas obligatorias

- El usuario puede pedir, comparar, cambiar una variante, aprobar/rechazar y consultar resultado simulado sin rutas rotas.

- Clic repetido no duplica la acción visible. Botones deshabilitados tienen explicación y recuperación; un cargador no queda indefinido.

- Visual VIS-01 a VIS-12 en los estados aplicables; navegación por teclado y foco en diálogos. Capturas de cada pantalla crítica y sus errores.


### Decisión técnica inicial propuesta

Frontend React + TypeScript; backend de control Python/FastAPI para integrar Hermes; PostgreSQL para estados y ledger, cola/agenda separada. Fijar versiones al iniciar F01. Esta propuesta no autoriza compartir runtime personal: Hermes y navegador siguen en una VM por usuario.

> Salida: demo navegable, datos de prueba identificados y comandos reproducibles. No confundir este hito con autenticación segura, VM real o compra real: eso se valida después.


## 06. F02: Hermes, modelos y VMs exclusivas

Semana 2 | Ingeniería IA + infraestructura + seguridad | P03–P04, P07 y P21 de viabilidad

| Experimento | Qué debe demostrar |
| --- | --- |
| Motor fijado | Versión/commit, licencias y configuración reproducibles; adaptador privado, sin llave administrativa al cliente. |
| Dos usuarios / dos VMs | Hermes, disco, memoria, navegador, cookies y secretos propios; no basta un perfil o contenedor compartido. |
| Broker de inferencia | La plataforma aplica identidad, cuotas, proveedor/modelo y límite; no entrega llave global a la VM. |
| Tool-calling | El modelo genera argumentos válidos y Hermes interpreta herramientas/razonamiento sin acciones extra. |
| Persistencia | Detener y reanudar conserva archivos/memoria; las sesiones pueden requerir autenticación de nuevo. |
| Agenda central | Una VM detenida se despierta por eventos/horario externo, nunca por un cron dentro de esa misma VM. |


### Pruebas de la quincena

- VM-01 a VM-07 y SEC-01: usuario A no puede leer ni accionar en B mediante API, disco, navegador, respaldo o herramientas.

- Evaluación de 100 tareas del alcance con entradas conocidas, sin compras reales. Registrar éxito, errores, intervención, tokens y tiempo por tarea; no cambiar criterios para esconder fallos.

- Comparar candidato Groq120B, ruta sencilla Groq20B y ruta visual Qwen; Cerebras solo evaluación si existe acceso. Medir TTFT, primera herramienta y tiempo total con misma carga.

- PERF-01/02: probar concurrencia 1/5/20 donde el acceso permita, registrando cuota, red, errores y tokens. No presentar TPS publicitados como resultado propio.


### Cierre

> Motor, API y tamaño de VM elegidos por evidencia. Si Hermes requiere un fork profundo, rompe aislamiento o no recupera tareas, corregir o cambiar motor antes de escalar. No continuar con un fallo crítico conocido.


## 07. F03: identidad, tareas y gestor de VMs

Semanas 3–4 | Backend + infraestructura + frontend + QA | P05–P07, P17 y P21

| Construcción | Comportamiento esperado |
| --- | --- |
| Identidad y acceso | Sesión segura, recuperación, roles internos y tenant_id fijado en servidor. |
| Asignación de VM | Usuario-VM persistente, aprovisionamiento idempotente, arranque con bloqueo y estados visibles. |
| Tareas y eventos | Estados durables; historial, streaming y reconexión sin depender de la pestaña abierta. |
| Colas / agenda | Trabajo pendiente y programación fuera de las VMs; reintentos acotados e idempotencia. |
| Parada segura | No apagar durante trabajo activo o resultado financiero desconocido; persistir antes de parar. |
| Restauración / baja | Backups por usuario, restauración probada, retención, exportación y borrado según política. |


### Validación visual

Mostrar “creando”, “iniciando”, “trabajando”, “detenida”, “recuperando” y “error” con explicación y siguiente acción. Al cerrar y abrir la app se ve el progreso conservado, sin reiniciar una tarea ni borrar mensajes.


### Pruebas

- API-01/02: sesión inválida bloqueada y acceso cruzado rechazado aunque se cambien IDs directamente en HTTP.

- VM-02/03: dos solicitudes concurrentes no crean ni despiertan dos VMs para el mismo usuario. La agenda despierta solo la correcta.

- VM-04/05: cerrar app, reiniciar worker/VM y cortar red; recuperar tareas sin duplicar efectos. No tratar una pestaña cerrada como cancelación.

- VM-06/07: restaurar datos del usuario correcto y revocar/borrar según política; verificar también la interfaz de estado.

> Cierre: una tarea avanza con la app cerrada y aparece correctamente al volver. Aislamiento verificado desde el servidor y la infraestructura, además de la UI.


## 08. F04: investigación, comparación y memoria

Semanas 5–6 | IA + integraciones + frontend + QA | P08–P09 y P16 inicial

| Capacidad | Entrega concreta |
| --- | --- |
| Investigación útil | Respuesta con enlaces, fecha de consulta y límites; no inventar precio, stock o cobertura. |
| Comparación | 2–3 opciones cuando existan; variante, vendedor, envío, total, disponibilidad y condiciones. |
| Navegación controlada | Dominios permitidos, sesión propia y solicitud al usuario para MFA/CAPTCHA. |
| Memoria personal | Ver/editar/borrar preferencias, procedencia, exportación y permiso de uso. |
| Límites de tarea | Tope de pasos, tokens, búsquedas, tiempo y reintentos; bloqueo comprensible al agotarse. |
| Seguimiento | Progreso ligado a eventos y ayuda/cancelación; no inferir éxito del texto del modelo. |


### Cómo se debe ver

Las tarjetas permiten comparar totales en MXN sin truncar variante o envío. Explicar cuando falta un dato; “sin disponibilidad confirmada” no equivale a disponible. Domicilios y datos personales se muestran solo en el alcance necesario.


### Pruebas

- AI-01/02: dataset con precio/variante conocidos; fuentes correctas, total consistente y manejo de “sin resultados”.

- AI-03/04: instrucciones maliciosas en página o correo no amplían permisos ni extraen datos; límites cortan bucles.

- AI-05/06: editar/borrar memoria cambia respuestas futuras y no afecta B; logout/revocación corta conexiones nuevas.

- AI-07: errores de proveedor, timeout o respuesta inválida aparecen con recuperación, no con una comparación fabricada.

- VIS-04/07: precios largos, ofertas, una sola opción, falta de stock, imágenes rotas y nombres extensos en móvil.

> Cierre: el usuario puede resolver investigación/comparación y controlar su memoria. Cobertura acotada y errores visibles; ninguna integración comercial se promete sin validación.


## 09. F05: aprobación y compra simulada

Semana 7 | Backend de pagos + frontend + QA + seguridad | P10–P13 y P19 simulados

Construir primero el ciclo financiero con un simulador determinista que permita reproducir rechazos, tiempos fuera, duplicados y resultados desconocidos. El servidor, no el modelo, decide si una orden está autorizada.

| Objeto | Regla |
| --- | --- |
| Cotización | Versión, producto/variante, vendedor, cantidad, total/moneda, envío, domicilio, vigencia. |
| Consentimiento | Usuario autenticado, cotización/versión, acción, máximo, expiración y evidencia; evitar reutilización. |
| Reserva | Atómica y acorde al saldo/límite; disponible y reservado separados si hay saldo administrado. |
| Pago / pedido | IDs y estados distintos. Una autorización de tarjeta no es compra confirmada. |
| Cancelación | Antes del compromiso externo, detener; después, solicitar cancelación/devolución y explicarlo. |
| Desconocido | Bloquear reintento de compra hasta consultar/conciliar; conservar trazabilidad. |


### Pantalla que revisaremos con más cuidado

Debe mostrar qué se comprará, a quién, cuánto como máximo, dirección parcial y hasta cuándo. “Aprobar”, “Cambiar” y “Rechazar” son acciones separadas. Pedir nueva aprobación si cambian condiciones fuera del alcance.


### Pruebas

- PAY-01 a PAY-08 con simulador: sin aprobación, vencida, precio cambiado, replay, doble clic, saldo concurrente, evento duplicado/desordenado y timeout tras cobro.

- PAY-09/10: cancelación antes/después del compromiso y reembolso parcial. VIS-05/06/08: no ocultar cargos ni mostrar éxito antes del pedido confirmado.

> Cierre: ninguna ruta de servidor ejecuta una compra sin consentimiento válido. Todos los estados, incluido “no sabemos aún”, pueden verse y probarse en la demo.


## 10. F06: dinero y proveedores en sandbox

Semana 8, condicionada | Pagos + legal + QA | P01–P02, P12–P18 y P20

| Flujo independiente | Prueba exigida |
| --- | --- |
| Cobrar el servicio: Stripe | Checkout/Billing test: alta, renovación, rechazo, cancelación y reembolso; estado de suscripción y CFDI cuando aplique. |
| Fondear cuenta: Finco | Identidad/titularidad y contrato; alta KYC, CLABE, abono SPEI firmado, límites y devolución en sandbox. |
| Pagar comercio | Emisor y comercio habilitados; autorización/captura, pedido, reversa y devolución parcial/total. |
| Conciliar | Libro auxiliar, proveedor y pedido reconciliados; diferencias y estados inciertos visibles. |
| Soporte | Permisos de intervención, historial, escalamiento y evidencia de cada ajuste. |


### Pruebas financieras completas

PAY-01 a PAY-12 con el sandbox oficial. Capturar IDs de proveedor, firma válida, deduplicación, idempotencia y consulta de estado. Simular fallos además del caso feliz. Verificar que ninguna llave o tarjeta real entre en chat, logs o memoria.


### Revisión visual

- Cuenta distingue disponible, reservado y liquidado; no abona fondos por un mensaje de chat ni por un callback sin validar.

- Membresía y saldo de compras aparecen separados. No etiquetar una referencia CLABE como cuenta individual si el contrato no lo permite.

- Pago autorizado, pedido confirmado, devolución solicitada y reembolso recibido tienen textos diferentes.


### Si Finco no está disponible

> Mantener la integración financiera pendiente. Continuar investigación, comparación y carrito con pago directo por el usuario. Los mocks validan nuestro código, pero no sustituyen sandbox, contrato, elegibilidad ni conciliación real del proveedor.

No se enviarán fondos ni se harán compras reales como parte de estas pruebas de sandbox. Un piloto posterior con dinero exige el flujo habilitado y autorización operativa específica.


## 11. F07: validación integral antes de piloto

Semanas 9–10 | QA + seguridad + infraestructura + operación | P19–P22

| Frente | Prueba de salida |
| --- | --- |
| Recorrido completo | Alta → tarea → comparación → aprobación → ejecución/pedido → seguimiento → devolución. Ver errores y reanudación. |
| Seguridad | Autorización cruzada, injection, secretos, recuperación de cuenta, acceso de soporte y revocación. |
| Resiliencia | Caída de API/worker/VM y proveedor durante ejecución; restauración de backup y conciliación antes de reabrir pagos. |
| Accesibilidad / visual | Matriz móvil/escritorio, teclado, zoom, lector de pantalla; capturas aprobadas para estados críticos. |
| Rendimiento / costo | TTFT, primera herramienta, tarea completa, arranque y carga. Límites por usuario, cuota y alertas. |
| Operación | Manual de incidencias, conciliación diaria, ayuda, kill switch, rollback y guardias acordadas. |


### Evidencia que se revisa en la demo

- Versión exacta, entorno y datos de prueba; reporte de casos ejecutados, fallidos, omitidos y bloqueados.

- Capturas en móvil/escritorio del mismo build; videos del flujo y recuperación; logs redactados y conciliación de operaciones de prueba.

- Ensayo de rollback: volver a versión estable sin borrar ledger ni duplicar órdenes; migrations compatibles o plan de recuperación probado.


### Puerta de salida

> Cero defectos críticos/altos abiertos de aislamiento, dinero o pérdida de datos. Todas las pruebas críticas ejecutadas y aprobadas; ninguna se marca aprobada por estar omitida. Una falla estética se clasifica por su impacto, no se minimiza si oculta monto o acción.

Si existe un bloqueo externo de dinero, puede aprobarse solo un piloto sin ese flujo. El alcance permitido debe quedar escrito; no declarar la plataforma financiera lista.


## 12. F08: piloto por invitación

Semanas 11–12 | Producto + operación + QA + pagos | P23

Invitar 25–50 personas del perfil, con cobertura y límites comunicados. Comenzar por un grupo menor y ampliar si no aparecen fallos críticos. Compras reales solo bajo programa/flujo autorizado; mientras tanto, mantener investigación o pago directo del usuario.

| Qué observamos | Cómo lo validamos |
| --- | --- |
| Primer uso | Registro y primera tarea útil; dónde se pierde, qué texto no entiende y dónde requiere ayuda. |
| Confianza visual | Usuario identifica monto, vendedor, estado, siguiente paso y diferencia entre simulado/real. |
| Calidad | 100 tareas del alcance como muestra inicial: éxito, intervención, falla y causa; separar ayuda del usuario (3DS) de operador. |
| Dinero | 100% de compras reales con consentimiento válido y trazabilidad; conciliación diaria sin diferencias inexplicadas al cierre. |
| Operación | Tiempo de respuesta/resolución, solicitudes de ayuda, cancelaciones, devolución y carga por operador. |
| Economía | Tokens, búsquedas, VM, red, soporte y costos externos por tarea y usuario. |


### Metas iniciales, no resultados

- ≥90% de tareas del alcance completadas sin operador interno en la muestra de 100; revisar causas y sesgo de la muestra. No implica compras universales ni garantía estadística.

- Cero gasto no autorizado y cero acceso cruzado. Si ocurre, detener nuevas compras, investigar y decidir reanudación; no esconderlo en un promedio.

- Al menos una sesión observada de usabilidad por recorrido crítico, con 5–8 participantes del perfil para detectar problemas; no tratar esa muestra como representación del mercado.


### Cierre

> Se avanza con evidencia de utilidad, seguridad y soporte, no por cumplir una fecha. Las limitaciones se incorporan al producto y al siguiente sprint. Sin conciliación y postventa, no se amplían pagos.


## 13. F09: estabilización y escala controlada

Semanas 13–16 | Equipo de producto + ingeniería + operación | P22, P31 y P33

| Trabajo | Validación |
| --- | --- |
| Corregir por impacto | Primero errores de dinero/aislamiento/datos; después tareas fallidas, abandono, latencia y detalles visuales. |
| 100–300 personas | Cohortes graduales solo con capacidad y soporte. No asumir que central de un nodo tiene HA. |
| Capacidad 25/100/1,000 | Carga representativa en staging: API/colas con ejecutores simulados + muestra de VMs reales. No crear 1,000 VMs por defecto. |
| Costos reales | Actualizar escenarios del PDF v1.2 con consumo y cotizaciones; distinguir gastos únicos de operación. |
| VM y modelo | Comparar 4/8 GB, horas activas, arranque y consumo. DO apagado no ahorra mientras exista. |
| Continuidad | Cambiar proveedor/modelo sin mezclar datos, duplicar efectos ni romper el contrato de herramientas. |


### Pruebas que se repiten

- Regresión de recorridos críticos, visual móvil/escritorio y permisos por cada release.

- Carga y recuperación con picos; comprobar límites de proveedor, cola, tasa de error y cola envejecida. Un ejecutor simulado no valida RAM ni navegador real.

- Snapshot/restauración por usuario y fallo de dependencia. Reconciliar antes de reactivar ejecución financiera.

- Usabilidad con usuarios recurrentes y nuevos; no optimizar solo para quienes ya aprendieron la interfaz.


### Cierre

> Antes de adquirir más usuarios: calidad, latencia, costo y postventa medidos por cohorte, límites probados y responsables de operación asignados. El precio final incorpora Finco y otros costos pendientes.


## 14. F10: canales, conexiones y apps

Semanas 17–20, condicionadas | Integraciones + móvil + seguridad + QA | P24–P28

| Canal / conexión | Construcción y pruebas |
| --- | --- |
| WhatsApp elegible | Confirmación del caso con reglas vigentes; consentimiento, opt-out, ventana y plantillas; duplicados y entrega. No usar un puente no oficial para el negocio. |
| Identidad multicanal | Asociación autenticada de cuenta; no usar teléfono o texto como autorización suficiente; eventos convergen a la misma tarea. |
| Correo / calendario | Scopes mínimos, verificación/evaluación cuando aplique, expiración y revocación. Correos y eventos maliciosos no amplían permisos. |
| Voz | Transcripción y confirmación del monto/destinatario; no ejecutar pagos por una transcripción ambigua. Límites de audio y costos. |
| Apps iOS/Android | Adaptar navegación, accesibilidad, notificaciones y deep links; revisar cobro digital por storefront antes de diseñar checkout. |


### Cómo validaremos la apariencia

- Mismo pedido, importe y estado en web, móvil y notificación. Textos largos y enlaces abren la tarea correcta; no revelan datos sensibles en pantalla bloqueada.

- Enlace de notificación no ejecuta automáticamente una compra ni reutiliza consentimiento vencido.

- iOS/Safari y Android reales para teclado, cámara/adjuntos, safe areas, push y reanudación. Emulación de viewport no sustituye pruebas de plataforma.


### Puerta de salida por canal

> Cada canal es una entrega independiente. Si WhatsApp no admite el asistente generalista en México, no se lanza ese uso; la PWA continúa. No presentar una implementación técnica como autorización comercial.

Las apps y conexiones externas pueden necesitar tiempos de revisión fuera del calendario. Mantener la misma fuente de verdad, sin duplicar permisos en cada canal.


## 15. F11: cobertura, recurrencias y continuidad

Semanas 21–24 y evolución posterior | Producto + pagos + operación + ingeniería | P29–P33

| Ampliación | Condición para publicar |
| --- | --- |
| Nuevo comercio/categoría | API/convenio o flujo permitido; variante/stock/total, confirmación, cancelación, entrega y devolución probados. |
| Pago de servicios | Agregador y contrato, referencia correcta, idempotencia, recibo y reversa; no extrapolar compras de bienes. |
| Recurrencia | Mandato con monto máximo, frecuencia, comercio, vigencia y revocación. Avisos y nueva aprobación al salir del alcance. |
| Afiliación / vendedores | Contrato, divulgación y facturación; no sesgo oculto ni ingreso financiero supuesto. |
| Escala mayor | Capacidad, cuotas, HA efectiva, recuperación y soporte antes de habilitar cohortes nuevas. |
| Cambio de motor/proveedor | Exportación, formato de memoria, permisos, sesiones y reconciliación. Pruebas de compatibilidad y rollback. |


### Pruebas nuevas antes de repetir compras

- Dos disparos de agenda generan una sola intención; no pagar dos veces por reintento ni por cambio de canal.

- Mandato revocado/vencido bloquea nuevas ejecuciones. Cambios de precio, domicilio o vendedor fuera de lo aprobado exigen nuevo permiso.

- Horario y zona del usuario explícitos; cambios de horario o ejecución atrasada no adelantan ni duplican cargos.

- Caída en pleno pago mantiene estado desconocido hasta reconsulta; no libera reserva ni ejecuta el siguiente intento a ciegas.


### Después de la semana 24

Evolución por métricas: parches, evaluación de modelos, restauración, seguridad, usabilidad, conciliación y economía por cohorte. La automatización se amplía solo con evidencia de que conserva control, recuperación y soporte.

> La semana 24 no es “todo terminado”. Es el cierre de una expansión acotada; cada nueva capacidad repite las puertas de diseño, pruebas, piloto y operación.


## 16. Pantallas que vamos a revisar

Inventario de UX; cada pantalla tiene estado normal, vacío, carga y error cuando corresponda.

| Pantalla | Qué debe verse claro | Casos que no podemos omitir |
| --- | --- | --- |
| Alta / recuperación | Mayoría de edad, términos, privacidad, verificación y siguiente paso. | Código vencido, intentos, error de red y cuenta ya existente. |
| Inicio / chat | Qué puede hacer, fuentes y tarea en curso. | Conversación vacía, adjunto inválido, respuesta parcial y error de modelo. |
| Lista / detalle de tarea | Estado, objetivo, pasos, bloqueo y cancelar. | VM iniciando, detenida, recuperación, sin conexión y tarea atrasada. |
| Comparación | Variante, vendedor, envío, total, stock y vigencia. | Sin resultados, una opción, imagen rota, nombre/precio largos y datos faltantes. |
| Aprobación | Producto, total máximo, vendedor, dirección parcial y caducidad. | Cotización cambiada, vencida, rechazo, doble clic y reautenticación. |
| Cuenta / tarjeta | Proveedor/titularidad, disponible, reservado, movimientos y bloqueo. | KYC pendiente/rechazado, saldo sin confirmar, tarjeta bloqueada y abono pendiente. |
| Pedido / devolución | Pago y pedido separados, seguimiento, ayuda y devolución. | Cobro sin pedido, resultado incierto, parcial, disputa y retraso. |
| Memoria / conexiones | Qué guarda, origen, editar/borrar y permisos por integración. | Sin datos, acceso expirado, revocación y eliminación pendiente. |
| Plan / facturas / soporte | Precio, recurrencia, cancelación, historial y contacto. | Cobro rechazado, suscripción cancelada, factura fallida y soporte abierto. |
| Panel de operación | Permisos, cola de excepciones y evidencia de intervención. | Acceso denegado, ajuste con doble control y diferencia de conciliación. |

El panel de operación es una interfaz separada por roles, no una pantalla accesible al consumidor. Ocultar un menú no basta: el servidor valida cada permiso. Los datos sensibles en las capturas deben ser sintéticos o estar redactados.


## 17. Criterios visuales verificables

Lista VIS: no se limita a que “se vea bonito”; exige que el usuario entienda y pueda actuar.

| ID | Qué revisamos | Aceptación |
| --- | --- | --- |
| VIS-01 | Reflow y tamaños | Sin scroll horizontal a 320 CSS px en flujos normales; tarjetas/tablas se adaptan, acciones alcanzables. |
| VIS-02 | Texto y contraste | Texto legible: contraste normal ≥4.5:1, texto grande ≥3:1; estados y controles con contraste/indicadores suficientes. |
| VIS-03 | Teclado y foco | Orden lógico; foco visible y no oculto, sin trampas. Dialogo gestiona entrada/salida y devuelve foco. |
| VIS-04 | Contenido extremo | Nombres, variantes, URLs, precios y domicilios largos no tapan montos ni acciones. |
| VIS-05 | Montos y condiciones | MXN explícito, separadores consistentes, total/envío/comisión claros; sin redondeos que alteren el permiso. |
| VIS-06 | Estados verdaderos | No marcar éxito por clic o texto del modelo. Incierto, pagado, pedido y reembolso son distinguibles. |
| VIS-07 | Recursos y carga | Fuentes e imágenes sin saltos perjudiciales; placeholders y fallback; no depender de una imagen para información crítica. |
| VIS-08 | Teclado móvil / overlays | Campos y confirmación no quedan tapados por teclado, barra fija, modal o safe area. |
| VIS-09 | Táctil y acciones | Objetivos ≥24×24 CSS px o separación/excepción válida; apuntar a 44×44 para acciones principales. |
| VIS-10 | Feedback / desconexión | Carga, timeout, offline y reconexión explicados; no spinner infinito ni repetición ciega de pago. |
| VIS-11 | Validación y errores | Campo y explicación vinculados, instrucciones accionables; toast no es el único registro de un error importante. |
| VIS-12 | Regresión visual | Capturas deterministas por estado/viewport; comparar con referencia revisada y aceptar cambios deliberadamente. |

Referencia de accesibilidad: WCAG 2.2 AA. Los umbrales anteriores son criterios del proyecto, no una certificación. Lector de pantalla, semántica, teclado, zoom y accesibilidad de procesos requieren revisión adicional. https://www.w3.org/TR/WCAG22/


## 18. Dispositivos y navegadores de prueba

Matriz mínima propuesta; expandir con los dispositivos reales del piloto.

| Entorno | Prueba | Cuándo |
| --- | --- | --- |
| 320 CSS px y zoom | Reflow, texto aumentado hasta 200%, navegación y aprobación sin recortes. | Cada cambio de layout; todas las pantallas críticas antes de piloto. |
| Android 360×800 / 390×844 | Chrome: conversación, teclado, comparación, aprobación, archivos y reconexión. | Capturas automatizadas por PR crítico y revisión real por release. |
| Móvil grande 430×932 | Contenido largo y densidad, teclado y barras fijas. | Antes de aprobar componentes y regresiones. |
| iPhone / Safari real | Teclado, scroll/modal, safe area, sesión, PWA y notificaciones cuando apliquen. | F01 visual y cada release; capacidades de plataforma desde su fase. |
| Tablet 768×1024 / 1024×768 | Orientación, navegación, tablas y diálogos. | Cambios responsive y previo a piloto. |
| Escritorio 1440×900 | Chrome y Firefox: columnas, streaming, foco y todas las acciones. | Recorridos automáticos y revisión de cada release. |
| Safari escritorio / accesibilidad | Safari real y VoiceOver; NVDA/Chrome o Firefox cuando estén disponibles. | Previo a piloto y cambios de navegación/semántica. |


### Qué demuestra cada tipo de prueba

Emular un viewport sirve para layout, no demuestra que funcione Safari/iOS, teclado del sistema, push, cámara o instalación PWA. Playwright WebKit ayuda a detectar diferencias pero no reemplaza Safari real. Si el entorno cloud no dispone de un dispositivo, registrar esa prueba como pendiente y usar dispositivo físico o servicio de pruebas autorizado al ejecutarla.


### Contenido de las capturas

- Misma versión, fixtures, idioma y estado. Fijar fechas/animaciones y enmascarar solo datos dinámicos necesarios; no ocultar precio ni estado financiero.

- Guardar referencia y comparación. Diferencias en total, botón de aprobación o información cortada bloquean; cambios de diseño intencionales se revisan antes de renovar la referencia.

- No usar una tolerancia global de píxeles para aprobar cambios sin inspección. Una diferencia pequeña puede afectar un dígito del monto.


## 19. Estados y pruebas con personas

Validar apariencia, comprensión y recuperación: tres cosas distintas.

| Estado | Mensaje / comportamiento esperado |
| --- | --- |
| Vacío | Qué puede hacer y ejemplo de siguiente acción, sin actividad ficticia. |
| Cargando / iniciando VM | Qué se está preparando; progreso honesto y recuperación si tarda. |
| Trabajando con app cerrada | Tarea persistida; al volver muestra eventos reales, no reinicia. |
| Esperando al usuario | Permiso o decisión requerida con contexto y vencimiento. |
| Sin conexión | Distinguir conexión del cliente de estado del servidor; no asumir tarea cancelada. |
| Sin stock / precio cambió | Opción no disponible o nueva cotización; no reciclar aprobación anterior. |
| Pago desconocido | “Estamos verificando el resultado”; no habilitar otra compra equivalente a ciegas. |
| Pedido confirmado | ID y datos del comercio; autorización de tarjeta por sí sola no basta. |
| Reembolso solicitado / recibido | Etapas separadas y vinculadas al pago original. |
| Cancelación | Explicar si detuvo ejecución o si está solicitando reversa/devolución externa. |


### Sesión de usabilidad propuesta: 5–8 personas del perfil

- **UX-01:** pedir una tarea y encontrar su avance sin ayuda; registrar bloqueos y dudas, no solo clics.

- **UX-02:** comparar y explicar en sus palabras precio final, vendedor y variante antes de aprobar.

- **UX-03:** rechazar/cambiar y distinguir “pago pendiente”, “pedido confirmado” y “reembolso recibido”.

- **UX-04:** cancelar una tarea, revocar conexión y encontrar soporte; comprobar que no teme perder control.

Meta inicial: al menos 4 de 5 participantes completan los recorridos centrales sin guía del moderador; todos comprenden total y alcance antes de autorizar. Un malentendido financiero bloquea aunque el promedio sea alto. Es una prueba cualitativa de detección, no una estimación estadística de adopción.


## 20. Pruebas de API, identidad y seguridad

Casos críticos ejecutados contra servidor y herramientas; no basta que la UI oculte botones.

| ID | Caso | Resultado exigido |
| --- | --- | --- |
| API-01 | Sesión ausente, vencida o revocada | No accede ni ejecuta. La UI pide recuperar sesión sin perder la tarea persistida. |
| API-02 | Cambiar tenant_id/task_id/order_id en HTTP | Servidor rechaza acceso a otro usuario; no filtra contenido, existencia sensible ni credenciales. |
| API-03 | Campos manipulados / importes inválidos | Valida esquema, moneda, centavos, versión y límites; el modelo no elige identidad efectiva. |
| API-04 | Reintento / doble solicitud | Una intención lógica, efecto único; respuesta recuperable e identificadores consistentes. |
| API-05 | Error / timeout / rate limit | Contrato de error entendible, reintentos seguros acotados y estado durable. |
| API-06 | Roles de soporte y ajustes | Solo operaciones permitidas; intervención auditada y doble control cuando corresponda. |
| SEC-01 | A intenta usar secretos/sesión de B | Bloqueado en API, VM, navegador, almacenamiento y backups; no solo en chat. |
| SEC-02 | Injection en web/correo/adjunto | Contenido no confiable no cambia permisos, comercio, destinatario ni herramientas efectivas. |
| SEC-03 | Enlace a metadata cloud / red interna | Egreso/SSRF bloqueados desde todos los caminos de herramienta que puedan acceder. |
| SEC-04 | Secretos en prompt/log/captura | No se exponen llaves globales, PAN/CVV ni datos de otros usuarios; redacción probada. |
| SEC-05 | Recuperación de cuenta / alta de conexión | Reautenticación y evidencia según riesgo; atacante no toma sesión con un texto o teléfono. |
| SEC-06 | Revocación / cierre / soporte temporal | Detiene nuevas acciones; expira privilegios y ejecuta política de retención/borrado. |

Pruebas con datos sintéticos y entornos propios/autorizados. Revisar amenazas al principio y repetir tras cambios de herramientas, permisos, navegador, almacenamiento o proveedor de identidad.


## 21. Pruebas de la VM y recuperación

La VM exclusiva es un requisito del producto, no una optimización intercambiable por perfiles compartidos.

| ID | Prueba | Resultado exigido |
| --- | --- | --- |
| VM-01 | Dos usuarios con navegadores y archivos | Cada uno conserva memoria, disco, cookies y credenciales propios. No heredar logins de la imagen. |
| VM-02 | Alta/despertar concurrentes y reintentos | Una VM asignada por usuario; idempotencia y bloqueo impiden duplicados y asociaciones cruzadas. |
| VM-03 | Detenida y evento/horario central | La agenda/cola externa despierta la correcta; tarea no depende de cron en la VM apagada. |
| VM-04 | Cerrar app / cambiar de dispositivo | Trabajo continúa si estaba activo; se reanuda visualización sin volver a ejecutar. |
| VM-05 | Reinicio durante una herramienta o pago | Estado durable; consultar resultado externo antes de repetir. No apagar un pago sin resolver. |
| VM-06 | Restaurar backup de A | Datos y permisos de A, sin restaurar secretos globales o datos de B. Medir pérdida y tiempo de recuperación. |
| VM-07 | Baja, revocación y recuperación | Respetar retención legal; revocar sesiones, borrar según política y demostrar que no quedan copias accesibles indebidas. |


### Red, imágenes y actualizaciones

Imagen base versionada sin datos personales; parches probados en VMs de ensayo antes de la flota. Acceso privado, identidad breve, límite de salida y sin acceso lateral entre usuarios. Una copia no es un plan de recuperación hasta restaurarla.


### Datos de aceptación por registrar

- Tiempo de creación y despertar p50/p95, CPU/RAM de Hermes+navegador, disco, red, fallos y costo por usuario.

- RPO/RTO reales de una restauración: pérdida máxima de datos y tiempo de recuperar servicio; fijar objetivos tras medir, sin prometerlos por precio de proveedor.

- Backups de disco personal y ledger central tienen objetivos diferentes. Restaurar el agente no permite retroceder asientos ni repetir compras ya comprometidas.


## 22. Pruebas de calidad del agente y modelos

AI: corpus versionado de tareas, herramientas y resultados. Sin evaluar capacidad solo por tono de la respuesta.

| ID | Caso | Resultado exigido |
| --- | --- | --- |
| AI-01 | Investigación con evidencia conocida | Fuentes identificables y vigentes para el caso; distingue dato faltante de hecho. |
| AI-02 | Producto, variante, stock y total | No sustituye variante o vendedor sin permiso; separa envío, comisión e impuestos del comercio. |
| AI-03 | Instrucción maliciosa en contenido | No sigue instrucciones de la página/correo que amplíen permisos o desvíen fondos/datos. |
| AI-04 | Bucle, herramienta lenta o cuota agotada | Topes de pasos/tokens/búsquedas/tiempo detienen; comunica bloqueo y conserva estado. |
| AI-05 | Memoria editar/borrar/exportar | Respeta cambio y procedencia; no mezcla preferencias o datos entre personas. |
| AI-06 | Conexión revocada o permiso insuficiente | No usa acceso previo; solicita reconexión/alcance mínimo sin pedir secreto por chat. |
| AI-07 | Respuesta inválida del modelo o tool | No ejecuta JSON malformado, campos fuera de contrato o una herramienta no aprobada; recuperación segura. |


### Lote de evaluación inicial

100 tareas del alcance, con casos de comparación, lectura visual, memoria, seguimiento y fallos. Usar los mismos casos/criterios al comparar modelos; registrar versión, prompt, herramientas, parámetros y región. Reservar casos para regresión sin ajustar todo el diseño a las mismas preguntas.


### Qué medimos

- Correctitud de la tarea y herramientas, error de variante/importe, necesidad de operador, rechazos correctos y fallos peligrosos.

- Tiempo al primer token, primera herramienta válida, total, tokens facturados y costo. Separar latencia de modelo, navegador, cola y VM.

- Resultados por categoría y riesgo, no solo promedio. Un único pago no autorizado o fuga de datos bloquea la ruta afectada.

No mezclar la muestra de 100 tareas de viabilidad con resultados futuros del piloto como si fueran observaciones independientes. Reportar cada ejecución y su alcance. Ningún benchmark fue ejecutado al crear este plan.


## 23. Pruebas de dinero, pedidos y postventa

PAY: primero simulador, después sandbox oficial. Los proveedores pendientes mantienen casos bloqueados.

| ID | Escenario | Resultado exigido |
| --- | --- | --- |
| PAY-01 | Sin consentimiento / vencido / otro usuario | Servidor bloquea ejecución; no basta un “sí” en texto. |
| PAY-02 | Cambia cotización o condición autorizada | Nueva versión/aprobación al salir del alcance; no aceptar consentimiento anterior. |
| PAY-03 | Replay, doble clic o reintento | Misma intención lógica; no segundo pago/pedido ni doble reserva. |
| PAY-04 | Dos compras y saldo limitado | Reserva atómica y límites; no sobregiro por concurrencia. |
| PAY-05 | Webhook sin firma / replay / duplicado | Validación, deduplicación y auditoría; sin abono o transición indebida. |
| PAY-06 | Eventos llegan fuera de orden | Consultar fuente y conciliar; no retroceder un estado confirmado incorrectamente. |
| PAY-07 | Timeout después de posible cobro | Marcar desconocido y consultar; no liberar/recomprar a ciegas. |
| PAY-08 | Tarjeta autorizada sin pedido aceptado | Separar estados y resolver reversa/soporte; UI no dice “comprado”. |
| PAY-09 | Cancelar antes/después de compromiso | Detener si aún es posible; después solicitud externa trazable, sin falsa cancelación. |
| PAY-10 | Reembolso parcial / tarjeta cerrada | Vincular pago original, ruta con emisor y conciliación; distinguir solicitado de recibido. |
| PAY-11 | 3DS, rechazo, captura/reversa y SPEI | Intervención legítima, límites y saldo según proveedor; no evadir autenticación. |
| PAY-12 | Cobro de membresía y operación contable | Servicio separado de fondos/GMV; renovación, baja, cobro fallido, CFDI y ajustes auditados. |

Cada caso debe guardar IDs de consentimiento/cotización/pago/pedido/proveedor y asientos afectados, sin PAN/CVV ni secretos. Prueba de éxito y al menos una falla por integración; mock aprobado no cuenta como integración externa aprobada.


## 24. Rendimiento, carga y presupuesto

PERF: objetivos iniciales por validar, no SLA ni resultados medidos.

| ID | Qué se prueba | Criterio / evidencia |
| --- | --- | --- |
| PERF-01 | Interfaz y tareas interactivas | En pantallas representativas: meta LCP≤2.5s, INP≤200ms, CLS≤.1. Laboratorio detecta regresiones; p75 real requiere datos suficientes del piloto. |
| PERF-02 | Modelo y herramientas | Meta inicial p95 TTFT≤1.5s y primera herramienta≤3s para tareas cortas con VM lista; registrar casos, red y errores. No aplicar a todo tipo de tarea. |
| PERF-03 | VM fría y cola | Medir creación/despertar, espera y recuperación por separado. UI informa estado; acordar máximo y política tras medir, sin spinner indefinido. |
| PERF-04 | Escala y costos | Usuarios 25/100/1,000 como escenarios; concurrencia modelo1/5/20 y picos API/colas. Registrar cuota, backlog, tasa de error, latencias y gasto. |


### Condiciones de la prueba

- Fijar build, dataset, región, tamaño de VM, caché, modelo y límites. Separar arranque frío/caliente y comparar la misma carga.

- Entradas/salidas y pasos cuentan completos: TPS de generación, TPM de cuota y tiempo total son medidas diferentes.

- Cargar APIs/colas con simulación es útil, pero no demuestra que 1,000 navegadores/VMs reales tengan igual rendimiento. Validar una muestra real antes de extrapolar.

- Límites y alertas por usuario/tarea/proveedor; probar que el límite funciona. Las pruebas usan presupuesto acotado y no aprovisionan flotas o consumen API pagada ilimitadamente.


### Qué pasa si no se cumple

Atribuir demora a modelo, VM, navegación, cola o proveedor; corregir la causa y repetir el caso afectado. Si se ajusta una meta, documentar por qué cambia y su impacto; no cambiar silenciosamente el umbral para marcar verde.

Métricas Web Vitals son metas de experiencia, no sustituyen pruebas de accesibilidad o seguridad. Referencia: https://web.dev/articles/vitals. TTFT/primera herramienta se miden en nuestra integración, no se deducen de precios o publicidad.


## 25. Pruebas automáticas y proceso de release

Automatizar lo repetible y revisar con personas lo que exige comprensión, accesibilidad o juicio visual.

| Momento | Verificación | Qué bloquea |
| --- | --- | --- |
| Al cambiar reglas | Pruebas de estados, permisos, importes, reservas, cotización e idempotencia; integraciones de DB/cola cuando aplique. | Invariantes financieras, aislamiento o estados incorrectos. |
| Cada cambio de UI crítico | Tipos/build, recorrido E2E determinista y capturas de componentes/pantallas afectadas; accesibilidad automática. | Recorrido roto, montos ocultos, acción inaccesible o cambio visual no revisado. |
| Al integrar a rama estable | API/VM/AI/PAY afectados y smoke del conjunto; las pruebas sandbox solo donde el acceso exista. | Falla crítica o dependencia requerida omitida/bloqueada. |
| Antes de publicar | Staging del build exacto, regresión crítica, dispositivos reales, revisión manual, migración y rollback. | Defecto de alto impacto, evidencia insuficiente o responsable de incidente sin asignar. |
| Después de publicar | Smoke sin efectos financieros indebidos, métricas y errores; comprobar colas y conciliación. | Degradación exige detener ruta/rollback seguro según el caso. |


### Reporte de ejecución

Por caso: ID, fase, versión, entorno, dato/fixture, pasos, resultado esperado, resultado observado, evidencia y responsable. Estado: **pendiente, aprobado, fallido, bloqueado u omitido justificado**. Incluir conteos; cero pruebas ejecutadas no significa aprobado.


### Evidencia útil

- Captura/video para apariencia y flujo; eventos de servidor y proveedor para compras; no usar screenshots como única prueba de saldo o autorización.

- Diferencias visuales aprobadas manualmente y rastreadas al cambio. No aceptar automáticamente todas las capturas para pasar CI.

- Credenciales separadas, logs redactados y fixtures sintéticos. Conservar evidencia por política, sin acumular datos personales innecesarios.


## 26. La demo con la que cerraremos cada etapa

Revisión breve del incremento real, con los mismos criterios definidos antes de implementarlo.

| Paso | Qué enseñaremos |
| --- | --- |
| 1. Alcance de la entrega | Qué historias/casos incluye y qué queda bloqueado o fuera. |
| 2. Flujo normal | Usuario nuevo completa la acción desde la pantalla de entrada hasta resultado verificable. |
| 3. Móvil y escritorio | Mismo flujo con contenido largo, teclado, zoom y acciones visibles. |
| 4. Error y recuperación | Timeout/desconexión/fallo; siguiente paso claro y estado conservado. |
| 5. Cancelación / control | Rechazar, cambiar, cancelar y revocar según la fase; confirmar alcance en servidor. |
| 6. Segundo plano | Cerrar app, reabrir y observar continuidad; parar/despertar la VM cuando aplique. |
| 7. Dinero / incertidumbre | Mostrar escenarios pendientes; no forzar éxito para que la demo se vea completa. |
| 8. Evidencia | Casos ejecutados y fallidos, capturas, eventos y costos relevantes de la misma versión. |
| 9. Decisión | Avanzar, corregir o avanzar solo un alcance menor explícito; dueño y siguiente acción de cada bloqueo. |


### Una tarea está terminada cuando…

- Cumple aceptación funcional y visual; maneja carga, vacío, error y recuperación aplicables.

- Tiene evidencia reproducible, revisiones y pruebas relevantes aprobadas. No muestra datos simulados como reales ni deja secretos en cliente/logs.

- Respeta permisos, observabilidad, cancelación y soporte; migración/rollback documentados si afecta datos o procesos.

- La documentación de arranque/operación refleja lo que existe. Los límites y dependencias quedan visibles.


### Responsables propuestos

Producto/UX evalúan comprensión y alcance; frontend consistencia visual/accesibilidad; backend/pagos invariantes; IA/infra aislamiento y recuperación; QA evidencia/regresión; operación conciliación/postventa. Una persona puede tener varios roles, pero los ajustes financieros sensibles requieren revisión independiente.


## 27. Dependencias y cobertura del backlog

P00–P33 provienen del plan v1.2; esta tabla los aterriza sin eliminar capacidades ni saltar permisos.

| Fase | Backlog principal | Dependencia para cerrar |
| --- | --- | --- |
| F00 | P00, P01, P20 diseño | Usuario/caso y flujo de fondos definidos; riesgos explícitos. |
| F01 | P05–P06 iniciales; P10–P11/P19 mock | Diseño y fixtures aprobados; simulación identificada. |
| F02 | P03–P04, P07/P21 viabilidad | Herramientas/accesos y dos VMs; aislamiento y motor probados. |
| F03 | P05–P07, P17 y P21 | Decisión técnica F02; identidad/agenda/estado durables. |
| F04 | P08–P09 y P16 inicial | Permisos/VM propios; fuente/comercio de investigación habilitado. |
| F05 | P10–P13/P19 simulados | Contratos de orden/cotización/consentimiento fijados. |
| F06 | P01–P02, P12–P18 y P20 | Identidad/contrato Finco, emisor/comercio, Stripe y sandbox según flujo. |
| F07 | P19–P22 completos para alcance | Integraciones requeridas, seguridad y evidencia integral. |
| F08 | P23 | Puertas de piloto y responsables; pagos solo si flujo autorizado. |
| F09 | P22, P31 y P33 | Datos del piloto y capacidad/soporte disponibles. |
| F10 | P24–P28 | WhatsApp elegible, OAuth/tiendas y permisos específicos. |
| F11 | P29–P33 | Contratos de nuevas capacidades, postventa y economía medidas. |


### Trabajos que avanzan en paralelo

Legal/proveedores desde semana 1; diseño y viabilidad en quincena inicial; soporte/conciliación desde antes del piloto. Son frentes de equipo, no una promesa de plazos del proveedor. Si no hay acceso, terminar mocks y contratos internos, mantener el gate externo abierto.


### Límites de calendario y presupuesto

El presupuesto v1.2 de desarrollo cubre cuatro meses; fases de semanas 17–24 requieren caja y dedicación posteriores. Mantener PWA como canal base y no ocultar este costo. Una VM por usuario se conserva durante todas las etapas; ahorro por parar depende del proveedor.


## 28. Primer sprint listo para descomponer

Semana 1: UX navegable y cimientos. La semana 2 conecta la prueba técnica; no todo el backend de producción.

| Ticket | Entrega | Aceptación mínima |
| --- | --- | --- |
| DEV-001 | Alcance y recorrido | Tres tareas elegidas, una compra simulada completa y límites escritos. |
| DEV-002 | Componentes / tokens de diseño | Botones, tipografía, color, formularios y estados accesibles en móvil/escritorio. |
| DEV-003 | Base reproducible | Proyecto inicia con documentación, lockfile, variables sin secretos y checks mínimos. |
| DEV-004 | Inicio/chat y lista de tareas | Crear tarea simulada, abrir detalle y volver sin perder estado del fixture. |
| DEV-005 | Comparación | Variante, vendedor, envío, total y fuente; sin stock/precio largo probados. |
| DEV-006 | Aprobación/rechazo | Condiciones exactas, vigencia, cambiar/rechazar; no confundir con pago real. |
| DEV-007 | Resultado y pedido simulado | Éxito, fallo y desconocido separados; historial y ayuda visibles. |
| DEV-008 | Estados y reconexión simulada | Carga, vacío, offline y error con recuperación; no spinner permanente. |
| DEV-009 | Pruebas visuales y accesibilidad | VIS aplicables, capturas en 360/390/1440, teclado/zoom y revisión manual. |
| DEV-010 | Demo y siguiente sprint | Recorrido completo, defectos priorizados, decisiones registradas y plan de dos VMs para F02. |

> Lo primero que vamos a trabajar: DEV-001 y DEV-002, seguidos por la demo web DEV-003 a DEV-008. La primera entrega que verás será el flujo navegable completo; después lo conectaremos a Hermes y a la plataforma segura, etapa por etapa.

Referencia del proyecto: Roadmap_agente_Mexico_Hermes_v1_2.pdf (48 páginas), con requisitos, presupuesto y 73 fuentes. Este nuevo documento es una propuesta de orden de desarrollo y aceptación, no un registro de pruebas ya pasadas. No cambia contratos, tarifas ni elegibilidad de proveedores.
