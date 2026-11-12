# Código abierto para una experiencia propia y premium

Fecha de lectura: 11 de noviembre de 2026. Alcance: 7 opciones agrupadas, 10 repositorios oficiales. Se leyeron 34 archivos de documentación, manifiestos y licencias; se guardaron copias fijadas al commit y SHA-256. No se instaló, ejecutó ni modificó ningún producto. Las capacidades son documentación publicada, no pruebas de integración con Hermes.

## Recomendación

Construir la interfaz de marca propia con **shadcn/ui + Radix** para controles, diálogos y accesibilidad, y **assistant-ui** para streaming, compositor y representaciones de herramientas. Nuestro producto conserva la navegación, tablero de tareas, estados, tarjetas de comparación, consentimiento de compra y conexión a la VM. No mostrar un selector de modelos como centro de la experiencia de consumo.

**CopilotKit + AG-UI** es una alternativa razonable si el centro de gravedad será interacción compleja con herramientas y estado compartido; probarla contra assistant-ui antes de elegir, no apilar dos runtimes de chat. **AI SDK** puede ser una capa de transporte/proveedor si aporta valor; el backend Hermes puede integrarse mediante un adaptador propio y no requiere reescribir el agente en TypeScript.

No elegir un fork completo de Open WebUI o LibreChat como primera interfaz pública premium: obliga a recortar una consola de IA de propósito general, arrastra decisiones de producto y aumenta mantenimiento. Open WebUI añade además una restricción actual de branding. OpenBot merece estudiar sus patrones, pero no satisface automáticamente VM exclusiva ni operación libre de servicios comerciales.

## Matriz de adaptación

Las estimaciones indican un spike de evaluación/adaptación de UI, en días-persona de ingeniería, no una cotización ni el plazo completo de producción.

| Opción | Licencia comprobada | Lo que sí reutilizaríamos | Integración / límite | Evaluación inicial propuesta |
|---|---|---|---|---|
| shadcn/ui + Radix Primitives | MIT en ambos repos | Botones, diálogo, sheet, tabs, menús, formularios; controles estilables y base accesible | No incluyen lógica de agente o pagos. Cambiar tokens, composición, tipografía y densidad; no confundir la estética predeterminada con diseño final. Radix reduce trabajo de interacción pero no certifica accesibilidad de nuestra pantalla | 2–4 días-persona para catálogo mínimo y dos pantallas |
| assistant-ui | MIT | Streaming, autoscroll, retries, adjuntos, markdown, atajos, compositor y UI de herramientas/aprobaciones inline | React/TypeScript; admite custom runtime/backend. El consentimiento visual debe llamar a nuestro servidor, que revalida cotización e identidad. `assistant-cloud` es servicio aparte, no requisito inevitable del componente | 2–5 días-persona para chat + tarjeta + stream ficticio y adaptador mínimo |
| CopilotKit + AG-UI | MIT en core y protocolo | UI generativa, pausas para intervención humana, estado compartido y componentes headless; flujo de eventos hacia agentes | Más capa de runtime/protocolo; el soporte genérico a frameworks no demuestra compatibilidad Hermes. CopilotKit Intelligence y Soar no son sinónimos del core MIT | 3–6 días-persona para un recorrido con tools, pausa/reanudación y recuperación |
| Vercel AI SDK / AI Elements | Apache-2.0 en repos leídos | Hooks de streaming/proveedores, UI de mensajes y herramientas. AI Elements copia componentes editables al proyecto | AI SDK admite proveedores directos; Gateway no es obligación. **AI Elements avisa migración y deprecación del repo actual a fin de noviembre 2026**. No iniciar una dependencia rígida sobre el repo viejo | 1–3 días-persona para un componente puntual y prueba de transporte; revisar destino de migración |
| OpenBot | Aplicación MIT; **Intelligence separado** | Referencias concretas de vista del computador, toma de control, rutinas, políticas y aprobaciones. React/Vite; backend Hono/Bun | Despliegue documentado requiere Intelligence licenciado; default da un **contenedor** por persona, no VM. Conectar Hermes/VM y sustituir/contratar servicios exige trabajo; no es drop-in | 2–4 días-persona de revisión de arquitectura/UX; no estimar fork completo sin spike |
| LibreChat | LICENSE raíz MIT; manifiestos inspeccionados declaran ISC | Referencia de adjuntos, historial, streams reanudables y gestión de conexiones/agentes | React + Express/Mongo/Redis y muchos módulos; manifiesto v0.8.9-rc1, workspaces descritos como altamente experimentales. Reconciliar alcance de licencias por subárbol antes de extraer código | 1–2 días-persona de referencia; costo de fork completo aún no estimable |
| Open WebUI | **Open WebUI License**, con licencias históricas por commit | Referencia de interfaz multiproveedor y manejo de archivos | Branding no se puede retirar por defecto fuera de excepciones. Stack Svelte/Python y producto amplio: mala base para nuestra marca React nueva. No describirlo como MIT sin matices | Descartar como base pública; revisar patrones sin copiar marca |

## Tres hallazgos que cambian la decisión

### 1. AI Elements está migrando ahora

Cita exacta del README:

> “This project will be deprecated at the end of November 2026 and replaced by”

El texto enlaza al nuevo AI Elements de shadcn/ui y recomienda esa versión para proyectos nuevos cuando esté disponible. La lectura no verificó aún la disponibilidad del destino. El código actual sigue siendo Apache-2.0; la advertencia es de continuidad/mantenimiento, no una prohibición de uso.

Fuente fijada: https://github.com/vercel/ai-elements/blob/ca8be600bfd01b3131f9bf6134b51602a71f4374/README.md#L4

### 2. Open WebUI no es white-label ilimitado

Cita exacta relevante de LICENSE:

> “licensees are strictly prohibited from altering, removing, obscuring, or replacing any "Open WebUI" branding”

La misma cláusula exceptúa despliegues con no más de 50 personas usuarias dentro de 30 días móviles, permiso escrito previo o licencia enterprise que lo permita. Los materiales anteriores conservan su licencia según `LICENSE_HISTORY`; esto no autoriza mezclar código actual y anunciar todo el producto como MIT.

Fuente fijada: https://github.com/open-webui/open-webui/blob/b0e6098e940942281d9c83f3529ea117287a3a22/LICENSE#L20-L37

### 3. OpenBot se parece a nuestro producto, con dos diferencias decisivas

Cita exacta del requisito de producción:

> “Requires a production Intelligence license beyond evaluation.”

Cita exacta sobre el computador:

> “the supervisor gives each person their own container”

MIT permite adaptar el template, pero la instalación documentada usa Intelligence licenciado. Su computadora personal es contenedor por defecto. Puede inspirar takeover, timeline y decisiones; no sustituye la VM exclusiva acordada ni prueba que el ledger o los controles financieros de México ya estén hechos.

Fuentes fijadas:
- https://github.com/CopilotKit/OpenBot/blob/b01ac8c7cfcca170b097c07cb4c2f331934fa0c2/README.md#L107-L115
- https://github.com/CopilotKit/OpenBot/blob/b01ac8c7cfcca170b097c07cb4c2f331934fa0c2/README.md#L379

## Qué significa “premium” al adaptar estas piezas

1. **Una tarea, una historia visual.** Conversación concisa a la izquierda o arriba; resultados/tarea a su lado. No obligar a leer logs, tokens, modelo o razonamiento interno para entender progreso.
2. **Componentes de resultados propios.** Comparación de opciones con total en MXN, fuente, disponibilidad y vigencia; no tablas JSON o bloques de consola.
3. **Permisos explicables.** Tarjeta de aprobación con importe máximo, vendedor, variante, domicilio parcial y expiración. Acción principal y alternativa claras. El modelo no renderiza permisos arbitrarios.
4. **Continuidad tranquila.** “Lo estoy resolviendo”, avance real, pendientes y retoma; evitar cadenas de spinners o mensajes técnicos de VM. Computador/navegador bajo “Ver actividad” y “Necesito tu ayuda”, no como escritorio remoto obligatorio.
5. **Prueba antes de integración.** Fixture con stream parcial, error, ausencia de stock, cotización vencida, pago desconocido y reconexión; después conectar a Hermes manteniendo el mismo contrato.

Los estados visuales informan, pero no conceden autoridad. Servidor autentica, liga consentimiento a una versión de cotización y ejecuta pagos fuera de la VM. No reutilizar componentes de “approve tool” como aprobación financiera universal.

## Spike de elección de librería (sin servicios pagados)

- Construir la misma tarjeta de comparación y aprobación con un stream ficticio en assistant-ui y CopilotKit; revisar interacción, código propio y tamaño de la capa necesaria.
- Probar interrupción/reconexión, scroll que respeta al usuario, adjunto inválido y pausa para aprobación.
- Verificar React/TypeScript, accesibilidad con teclado y lector, CSS encapsulado, y servidor como única fuente de estados efectivos.
- Elegir una sola capa de runtime de conversación. Mantener catálogo de componentes propio y tokens de diseño desacoplados.
- Fijar commit/versiones y revisar licencias de subpaquetes, iconos, fuentes, ejemplos y dependencias al incorporar código. Conservar avisos MIT/Apache, cambios y NOTICE cuando aplique. La licencia de código no concede derecho a usar nombres, logos, fotografías ni marca ajena.

## Fuentes exactas y límites

Se verificaron archivos oficiales mediante GitHub/raw con TLS, y `git ls-remote` de solo lectura para fijar commits. No se usó popularidad/estrellas como sustituto de calidad. Los hashes y URLs fijadas están en `evidence/pinned_manifest.json`; los commits en `evidence/heads.json`. No se instalaron paquetes ni se ejecutaron pruebas funcionales. La compatibilidad de Hermes, desempeño real, accesibilidad del producto final, servicios y cotizaciones siguen requiriendo validación.

| Repositorio | Commit leído | Licencia exacta |
|---|---|---|
| assistant-ui/assistant-ui | 437b410726e283798ff3b61b0f4209129225e2fa | https://github.com/assistant-ui/assistant-ui/blob/437b410726e283798ff3b61b0f4209129225e2fa/LICENSE |
| CopilotKit/CopilotKit | 5f6d9ba912b67415799be8cc1e18019eb337e636 | https://github.com/CopilotKit/CopilotKit/blob/5f6d9ba912b67415799be8cc1e18019eb337e636/LICENSE |
| vercel/ai | 70e45d5878494be4b66e325187f865951025059e | https://github.com/vercel/ai/blob/70e45d5878494be4b66e325187f865951025059e/LICENSE |
| vercel/ai-elements | ca8be600bfd01b3131f9bf6134b51602a71f4374 | https://github.com/vercel/ai-elements/blob/ca8be600bfd01b3131f9bf6134b51602a71f4374/LICENSE |
| shadcn-ui/ui | dd41d19e2f80ff6891951f7ced74c2c9a650b065 | https://github.com/shadcn-ui/ui/blob/dd41d19e2f80ff6891951f7ced74c2c9a650b065/LICENSE.md |
| radix-ui/primitives | eb3a2b7091293e27df8f9ba906632d8daa3d81a3 | https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/LICENSE |
| open-webui/open-webui | b0e6098e940942281d9c83f3529ea117287a3a22 | https://github.com/open-webui/open-webui/blob/b0e6098e940942281d9c83f3529ea117287a3a22/LICENSE |
| danny-avila/LibreChat | e6567c7a681ce67869dce31486a21d3a25d6931b | https://github.com/danny-avila/LibreChat/blob/e6567c7a681ce67869dce31486a21d3a25d6931b/LICENSE |
| CopilotKit/OpenBot | b01ac8c7cfcca170b097c07cb4c2f331934fa0c2 | https://github.com/CopilotKit/OpenBot/blob/b01ac8c7cfcca170b097c07cb4c2f331934fa0c2/LICENSE |
| ag-ui-protocol/ag-ui | deefd3833c15b353348ba90eae0fad6113021759 | https://github.com/ag-ui-protocol/ag-ui/blob/deefd3833c15b353348ba90eae0fad6113021759/LICENSE |
