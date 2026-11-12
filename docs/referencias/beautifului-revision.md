# BeautifulUI: revisión de las piezas reutilizables

Revisión: 11/11/2026. Repositorio leído: `TurboKach/ai-native-react-components`, commit `05dab2d2b5f1f3e40029776e339a486d70491079`. No se instaló ni ejecutó código externo y no se modificó el prototipo.

## Procedencia y alcance de licencia

El README del repositorio dice que sus 19 primitivas están «Sourced from beautifului.dev» y enlaza ese sitio. El archivo LICENSE de **este repositorio** es MIT, copyright 2026 Turbo. Esto permite adaptar el código de estas piezas conservando el aviso; **no demuestra que todo BeautifulUI, su catálogo PRO, marca, imágenes o cualquier asset del sitio sea MIT**.

Archivos, URLs fijadas y hashes: `source_manifest.json`. El README advierte expresamente que los componentes son demostraciones autoanimadas y no APIs terminadas:

> “Treat them as visual references to wire up to real state, not as finished API surfaces.”

Fuentes:
- [README fijado](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/README.md)
- [LICENSE fijada](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/LICENSE)

## Lo más útil para el Liquid Glass monocromo

Prioridad: **task-rows → prompt-bar (solo estructura) → recommendation-card → tool-chips resumido → approval-card rediseñada para consentimiento**. Adoptar la jerarquía, detalles expandibles, sombra fina y transiciones breves; mantener nuestro diseño y fuente de verdad.

| Pieza | Patrón que conviene adaptar | Qué hay que retirar o cambiar |
|---|---|---|
| Task Rows | Filas compactas de tarea, icono de estado, detalle expandible, transición de forma suave | La demo decide Failed/Completed por tiempo. Nuestro estado viene de eventos/acciones explícitas; sin porcentajes, éxitos o reintentos ficticios |
| Prompt Bar | Compositor que crece al escribir, adjuntos visibles, menú contextual y acciones compactas | Autoplay, modelos ficticios, conexión Gmail simulada, dictado simulado, adjuntos de nombres hardcoded y arcoíris WebGL. Enviar debe conservar texto si falla y limpiar solo tras aceptación real |
| Recommendation Card | Recomendación principal y alternativas en un drawer conservando el contexto | “High confidence” y el medidor son valores hardcoded: eliminarlos. La selección prepara una opción; no simula compra ni cambia a “Accepted” sin respuesta válida |
| Tool Chips | Actividad agrupada y detalle bajo demanda; evita una conversación llena de logs | Sustituir “4 tool calls, 2 messages”, comandos y tests inventados por eventos reales. Mostrar resumen legible, no razonamiento privado ni consola obligatoria |
| Approval Card | Un bloque de decisión con opciones y jerarquía clara | Es un cuestionario local, no autorización financiera. Quitar autoadvance/autosubmit, paginador minúsculo y opciones hardcoded; hacer consentimiento explícito ligado a versión, monto y vencimiento |

En un prototipo estático/vanilla pueden adaptarse estos patrones sin introducir React/Next únicamente para usarlos. En la aplicación React futura conviene extraer componentes controlados y tokens propios, no copiar la página showcase completa.

## Revisión concreta de API y comportamiento

### Approval Card

[Fuente](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/components/approval-card.tsx)

- Exporta `ApprovalCard()` sin props de datos ni callback de aprobación. `QUESTIONS` contiene tres preguntas ficticias de helados.
- En `toggle()` las preguntas radio ejecutan `setTimeout(..., 480)`; al elegir la última opción se hace `setSent(true)`. El usuario puede acabar enviando sin una acción final separada.
- La etiqueta “Answers sent” solo depende de estado local. No hay envío API, consentimiento autenticado, versión de quote, idempotencia o expiración.
- El patrón de radio/checkbox usa botones `aria-pressed`; al adaptarlo revisar grupos semánticos, teclado y foco. El paginador tiene puntos de 7–9 px y controles pequeños: ampliar áreas táctiles y no usar esos puntos como confirmación.
- Para dinero: resumen persistente del producto/variante, total máximo MXN, comercio, dirección parcial y vencimiento; botones **Aprobar por hasta MXN… / Cambiar / Rechazar**. Solo el servidor puede pasar a aprobado; “enviando” y “requiere nueva aprobación” son estados distintos.

### Task Rows

[Fuente](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/components/task-rows.tsx)

- Exporta `TaskRows({ variant = "Capsules" })`; no admite lista ni estado externo.
- `useTick(TICKS)` recorre una secuencia con `setTimeout`; no es un proceso de backend. `row2` pasa de pending a failed y luego done según el tick.
- El contenido “Verified vendor records”, “12 suppliers”, “68%” y “Completed” es demostrativo.
- Adaptación: `tasks`, `expandedIds`, `onToggle`, `onOpen`, `onCancel`; cada tarea con ID, título, estado, detalle seguro y marca de actualización. Usar barra indeterminada o texto de etapa si no existe porcentaje medido. El final debe venir de un evento verificable.

### Tool Chips

[Fuente](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/components/tool-chips.tsx)

- Exporta `ToolChips()`; `ROWS` y `DIFFS` son arrays de demo. Cada 700 ms aparece otro paso.
- Incluye “✓ 34 checks passed” y “built in 1.2s” como texto estático. No conservarlos como evidencia.
- Los chips de archivos parecen interactivos por cursor pero no tienen navegación real; “+2 more” no define callback.
- Adaptación: eventos recibidos del servidor, resumidos como “Consultó 3 fuentes” o “Necesita tu autorización” solo si ese conteo/estado está respaldado. Detalles bajo demanda, sin exponer secretos ni cadena de pensamiento.

### Prompt Bar

[Fuente](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/components/prompt-bar.tsx)

- Props: solo `variant`, con estado local para texto, menús, modelo, adjuntos y escucha. No hay `onSubmit` de aplicación.
- `AUTO_STEPS` cicla indefinidamente hasta interacción; altera texto, selección de modelo y `connected`. Puede dar impresión de conexión autorizada sin que exista.
- “Adjuntar” añade nombres de `FILES`, no abre ni valida archivos. “Dictado” espera 2.2 segundos e inserta una frase fija. `send()` borra texto/adjuntos y cierra menús; no envía nada.
- Reutilizar crecimiento de textarea, fichas removibles y navegación de menú; quitar el catálogo técnico de modelos de la vista principal y las integraciones no conectadas. Micrófono solo si está implementado y autorizado.
- API deseada: `value`, `onChange`, `attachments`, `onPickFiles`, `onRemove`, `onSubmit`, `status`, `error`. Mantener borrador al fallar, impedir doble envío y rotular claramente una demo.

### Recommendation Card

[Fuente](https://github.com/TurboKach/ai-native-react-components/blob/05dab2d2b5f1f3e40029776e339a486d70491079/components/recommendation-card.tsx)

- Exporta sin props; tiene `OPTIONS` de demo, medidor `signal` y `accepted` local.
- Elegir alternativa cambia estado local; “Accept” hace `setAccepted(true)`. No hay operación backend ni vinculación de consentimiento.
- Conservar drawer, jerarquía y selección; sustituir medidor por datos comprobables (total, entrega, fuente, fecha). “Elegir opción” prepara cotización; **no** compra. Para ejecutar, pasar por el bloque de autorización.

## Glimm: licencia y por qué omitirlo aquí

El repositorio declara `glimm: ^0.3.0`. Se consultó el paquete exacto **glimm 0.3.0** en npm, se leyó su LICENSE MIT (copyright Noman Ijaz) y README, y se verificó la integridad del tarball contra `dist.integrity`. Evidencia: `glimm_metadata.json`, `glimm_evidence.json`, `glimm_LICENSE`, `glimm_README.md`. Esto no significa que una instalación futura con `^0.3.0` sea idéntica: fijar versión si se usa.

Glimm es un efecto WebGL de barrido de color. No lo necesitamos para este diseño monocromo:

- El Prompt Bar crea un `RAINBOW`, un canvas WebGL y una celebración al cambiar al modelo ficticio “flagship”. Eso añade carga visual sin comunicar progreso real.
- `makeShader()` cambia temporalmente **`Math.random` global a `() => 0`** para fijar el color. Aunque lo restaura en `finally`, copiar este parche global no es apropiado para nuestra app.
- `celebrate()` contempla `prefers-reduced-motion`, y el README de glimm afirma fallback cuando falta WebGL. Las otras secuencias temporizadas de la demo no heredan automáticamente esa protección; revisar todo el componente.
- No copiar el proveedor de transiciones globales ni interceptar toda navegación. Usar CSS/opacidad/transformación breve, sin WebGL, con `prefers-reduced-motion` y sin animación que tape un total o simule actividad.

Fuente npm: https://registry.npmjs.org/glimm/0.3.0

## Tratamiento visual propuesto

- Superficie principal gris/blanca ligeramente translúcida, borde de 1 px y sombra suave; vidrio más evidente en navegación/compositor, menos blur debajo de texto y montos.
- Texto principal 14–16 px, secundario con contraste suficiente. El ejemplo usa muchos textos de 11.5–13 px: no copiar densidad de showcase tal cual para consumidor móvil.
- Neutros para estado, icono y palabras explícitas; no depender solo de verde/rojo. El éxito aparece al concluir de verdad.
- Detalles se expanden con una transición breve; sin expansión automática que mueva el contenido mientras se intenta pulsar.
- CTA negro/blanco sobrio y estable. Acciones destructivas separadas. Preservar foco visible, teclado, lectores y objetivos táctiles amplios.

## Pruebas antes de dar por adaptado

1. Ningún timeout cambia el estado de tarea, conexión, autorización, pedido o pago a éxito.
2. Pausar y rechazar funcionan; el paso terminal viene de eventos/acciones reales. Doble clic no envía dos veces.
3. Cambiar de opción o vencer cotización invalida el consentimiento anterior; aceptar la recomendación no compra.
4. Reducir movimiento detiene loops/transiciones no esenciales; no hay parche global de `Math.random` ni canvas innecesario.
5. Texto largo, precios MXN y teclado móvil no recortan resumen ni CTA; a 320 px sigue usable.
6. Tab, Escape y foco de diálogos/menús funcionan; controles táctiles y contraste medidos.
7. Las capturas de prototipo se rotulan como simulación donde haya fixtures; no muestran “tests passed” o conexiones ficticias como hechos.

Conclusión: usar el repositorio MIT vinculado a BeautifulUI como **fuente de patrones y componentes visuales**, no como flujo de agente terminado. Las mejores ganancias aquí son las filas expandibles, el compositor adaptable y el drawer de alternativas; la autoridad y la verdad de los estados siguen siendo nuestras.
