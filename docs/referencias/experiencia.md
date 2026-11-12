# Experiencia premium: parte 1

Fecha: 11 de noviembre de 2026. Propuesta de diseño basada en los requisitos y el roadmap del proyecto. No representa entrevistas realizadas, pruebas con usuarios ni uso directo de Muse. Cualquier ventaja competitiva aquí es una hipótesis por validar; el análisis comparativo de fuentes se lleva en otro frente.

## La decisión de producto

Crear un concierge personal que convierte una intención en un resultado verificable, con atención humana en los momentos donde se necesita. El centro de la experiencia es **la tarea y su resultado**, con una conversación disponible como contexto. No debe sentirse como un chat de laboratorio ni como una consola para administrar agentes.

Promesa inicial propuesta: **“Pide lo que necesitas. Sigue lo importante.”**

Una ejecución puede seguir con la app cerrada; una compra necesita la aprobación concreta del usuario. La persona siempre distingue entre que el agente está investigando, que necesita una decisión y que existe un resultado confirmado.

El diferencial a probar es una combinación de: resolución local en México, evidencia de precio total y variante, continuidad de tareas y postventa. Ni “tener IA” ni una estética lujosa bastan por sí solas. No se afirma que Muse carezca de estas funciones.

### Cómo se siente premium

- Una siguiente acción clara; poca navegación y sin cinco paneles compitiendo por atención.
- Jerarquía editorial, tipografía legible, espacios generosos y componentes precisos; el contraste y la accesibilidad no son un tema opcional.
- Información densa solo cuando sirve: progreso resumido, evidencia desplegable y condiciones completas antes de autorizar.
- Movimiento breve que explica cambios de estado; no órbitas eternas que aparentan trabajo. Respetar movimiento reducido.
- Atención a los errores, sesiones vencidas y devoluciones con el mismo cuidado que la pantalla inicial.
- Español mexicano natural. No “orquestación”, “tenant”, “tokens”, “sandbox” o “VM” en el flujo de consumo.
- Cifras, fechas, marca y dirección consistentes. Identidad elegante sin imitar marca, logotipo, textos ni recursos de Muse.

## Arquitectura de información

**Navegación primaria:** Hoy · Tareas · Memoria. En móvil, barra inferior con tres destinos y botón central de nueva solicitud solo si no duplica el compositor. En escritorio, navegación corta lateral con el mismo orden. El perfil abre Conexiones, Plan, Soporte y Privacidad.

**Hoy:** una entrada principal, decisiones que requieren atención y tareas activas. No KPI tiles ni saldo como elemento dominante. El estado financiero se añade solo cuando exista un programa real habilitado.

**Tareas:** activas / requieren tu decisión / terminadas. Filtros limitados; cada tarjeta responde objetivo, estado y próximo paso. Un historial de conversación no sustituye el historial de tarea.

**Memoria:** información personal que la persona puede ver, corregir, borrar y dejar de utilizar. No es un vertedero de todo lo conversado.

**Conexiones:** permisos por servicio, último uso y revocación. No se piden correo, calendario ni cuenta financiera en el primer minuto si la primera tarea no los necesita.

El chat entra desde Hoy y vive dentro de una tarea. Se puede aclarar o cambiar una solicitud desde allí sin perder el contexto. Una vista de actividad resume eventos reales; nunca muestra cadena de pensamiento ni simula pasos no ocurridos.

## Ocho pantallas y sus contratos

| Pantalla | Jerarquía y acción primaria | Contenido obligatorio | Estados que diseñar ahora |
|---|---|---|---|
| 1. Bienvenida y acceso | Promesa breve → acceso → primera tarea | Acceso, mayoría de edad del MVP, enlaces de términos/privacidad; explicación de permisos cuando se pidan | Acceso nuevo, código expirado, error, recuperación; sin pedir KYC innecesario |
| 2. Hoy | Solicitud → decisiones → actividad | Compositor, ejemplos del alcance, máximo tres decisiones visibles, tareas que siguen en curso | Vacío, primera tarea, varias tareas, solo una decisión urgente, sin conexión |
| 3. Detalle de tarea | Resultado/estado → siguiente acción → evidencia | Objetivo, restricciones editables, estado, última actualización, conversación, actividad real y cancelación | Preparando, trabajando, esperando al usuario/proveedor, pausada, completada, error y estado desactualizado |
| 4. Comparación | Recomendación razonada → alternativas | Hasta tres opciones; variante, vendedor, precio total/envío, disponibilidad y fuente/fecha; explicación de selección | Sin resultados, una sola opción, falta de stock, costo sin confirmar, imágenes fallidas, precio cambiado |
| 5. Autorizar una compra | Objeto y total → alcance → confirmación | Producto/variante/cantidad, comercio, tope, moneda, envío, dirección parcial, vigencia; autorización vinculada en servidor | Lista para autorizar, cotización vencida/cambiada, reautenticación, enviando consentimiento, ya autorizado |
| 6. Pedido y postventa | Estado verificable → seguimiento → ayuda | Pago y pedido separados; identificadores legibles, entrega, recibo/factura disponible; cancelar/devolver | Pedido confirmado, pago sin pedido, incertidumbre, devolución solicitada, parcial y recibida |
| 7. Tu memoria | Preferencias útiles → editar/controlar | Categoría, valor, origen, último uso si existe, editar/borrar, usar/no usar | Vacío, guardada, editada, eliminación pendiente, conexión revocada |
| 8. Conexiones y cuenta | Lo conectado → permisos → revocar | Servicio, alcance, último acceso si existe, reconectar/desconectar; plan, soporte y privacidad accesibles | No conectada, operativa, acceso vencido, revocando, error; banco/tarjeta solo habilitados si son reales |

El prototipo debe etiquetarse globalmente como **“Demostración · datos de ejemplo”**. Evitar “saldo disponible” y números de tarjeta que aparenten una cuenta real. Las marcas de comercios, cotizaciones y pedidos de muestra son ficticios o se identifican como ejemplos.

## Journey 1: investigación que termina en una decisión

**Solicitud de ejemplo:** “Busca audífonos para videollamadas, hasta MXN 3,500, que lleguen esta semana.”

1. La persona escribe en Hoy; el sistema crea una tarea. Solo pregunta algo que impida avanzar: ciudad/código postal si la entrega no se puede estimar; no repite preguntas de preferencias ya autorizadas.
2. Detalle muestra objetivo y restricciones como chips editables: “Videollamadas”, “Hasta MXN 3,500”, “Entrega esta semana”. Una línea comunica el evento real más reciente; no porcentajes inventados.
3. Puede salir de la app. La tarea conserva su identidad y resultado; la página no es el ejecutor.
4. Resultado presenta una recomendación y dos alternativas, si existen, con razones y fuentes. Si falta costo de envío, no llamar “total” al precio parcial.
5. Puede comparar, cambiar un criterio, guardar el resultado o preparar una compra. Preparar compra no autoriza cobrar.

**Éxito de diseño:** la persona puede explicar por qué se recomienda una opción, identificar qué no está confirmado y modificar el objetivo sin empezar de cero.

## Journey 2: compra con control explícito

**Datos sintéticos:** set de café, una unidad, variante marfil; vendedor “Casa Ejemplo”; artículos MXN 1,149 + envío MXN 100 = total MXN 1,249. No son una oferta comercial ni disponibilidad real.

1. Desde la opción elegida, “Preparar compra”. Se reconsulta precio, stock, envío y condiciones mediante la integración permitida.
2. La pantalla dedicada de autorización muestra producto exacto, comercio, tope MXN 1,249, envío incluido, dirección parcial y vigencia. El botón dice **“Autorizar hasta MXN 1,249”**. Alternativas visibles: “Cambiar” y “No autorizar”.
3. La autorización queda unida a usuario, cotización/versión, importe, moneda, comercio, alcance y vencimiento en el servidor. Los detalles técnicos no se muestran, pero sí el alcance humano.
4. Estado inmediato: “Autorización recibida”. Después: “Estamos realizando la compra”. No mostrar “Comprado” por haber tocado el botón ni por una autorización de tarjeta.
5. Cuando el comercio confirme: “Pedido confirmado”. Pago y pedido conservan estados distintos; existe acceso a comprobantes y postventa.
6. Si cambian las condiciones fuera del alcance, nueva cotización y nueva aprobación. Si se pierde la respuesta después de posible cobro, “Estamos verificando el resultado”; no habilitar otro pago equivalente a ciegas.
7. Después del compromiso externo, “Solicitar cancelación” comunica una solicitud; no asegura haber cancelado. Reembolso solicitado y recibido son estados diferentes.

**Éxito de diseño:** entiende qué autoriza antes de hacerlo y distingue autorización, compra, pedido y devolución. Menos clics no justifica ocultar una condición material.

## Journey 3: trabajo en segundo plano y regreso

**Solicitud de ejemplo:** “Revisa mañana a las 10 si este producto vuelve a estar disponible. Avísame; no lo compres.”

1. Confirmación con hora y zona del usuario: “Revisaré mañana a las 10:00. Te avisaré si vuelve a estar disponible. No realizaré la compra.”
2. Detalle muestra “Programada” y la próxima revisión. La agenda vive fuera de la VM, que puede detenerse por inactividad. No mostrar “trabajando” mientras espera el horario.
3. Cuando se ejecuta, el estado cambia por un evento real a “Preparando la tarea” y luego “Revisando disponibilidad”. No necesita permanecer en la pantalla.
4. Si la persona pierde conexión, el cliente muestra “Sin conexión. El estado puede haber cambiado; lo actualizaremos al reconectar”, junto a última actualización. No garantiza continuidad si el servidor no puede confirmarla.
5. Al regresar, el cliente consulta los eventos y resultados durables de la misma tarea; no la vuelve a enviar. Notificación opcional lleva al detalle correcto sin ejecutar una compra.
6. El resultado dice cuándo se revisó y si la disponibilidad fue confirmada. Puede cancelar futuras revisiones. Cancelación durante una compra externa sigue otro contrato.

**Éxito de diseño:** distingue programada, ejecutándose, esperando decisión y completada. No necesita saber qué es una VM para confiar en que cerrar la app no equivale a cancelar.

## Autonomía y permisos

| Acción | Comportamiento inicial |
|---|---|
| Leer fuentes públicas, comparar y resumir | Puede avanzar dentro de cuotas y alcance |
| Guardar preferencia personal | Proponer y permitir editar/borrar; explicar origen y uso |
| Acceder a correo/calendario | Solo con conexión y scopes mínimos autorizados; revocable |
| Preparar carrito/cotización | No crea permiso de gasto |
| Comprar o enviar acción con efecto material | Requiere alcance y consentimiento concretos validados en servidor |
| Compra recurrente | Fuera del primer prototipo; necesita mandato con frecuencia, máximo, vigencia y revocación |
| Usar o cambiar identidad efectiva | Nunca por texto del modelo; la fija la plataforma |

La UI puede mostrar un control de autonomía en lenguaje simple —“Investigar”, “Preparar”, “Pedir mi aprobación”—, pero no un interruptor ambiguo de “modo autónomo” que aparente otorgar acceso financiero global. No usar badges de seguridad no demostrables como “100% seguro” o “privacidad absoluta”.

## Microcopy y tono

| Situación | Texto propuesto |
|---|---|
| Inicio | “¿Qué necesitas resolver?” |
| Ejemplo de alcance | “Compara opciones, organiza pendientes o da seguimiento a una compra.” |
| Actividad real | “Ya tengo dos opciones con envío confirmado.” |
| Falta un dato | “Necesito tu código postal para comparar el total con envío.” |
| Preparando ejecución | “Estoy preparando tu tarea. Puedes salir y volver después.” |
| Espera de decisión | “Tengo una opción lista. Revisa las condiciones antes de autorizar.” |
| Autorizar | “Autorizar hasta MXN 1,249” |
| Cambio material | “El total cambió a MXN 1,299. Necesito tu aprobación antes de continuar.” |
| Incertidumbre de pago | “Estamos verificando el resultado. No vuelvas a pagar; aquí aparecerá la actualización.” |
| Sesión de comercio vencida | “Necesitas volver a iniciar sesión para continuar. No compartas tu contraseña por chat.” |
| Cancelación previa | “La tarea se detuvo. No se inició la compra.” Solo si el servidor lo confirma |
| Cancelación posterior | “Solicitamos la cancelación. Falta la confirmación del comercio.” |
| Eliminar memoria | “Dejaré de usar esta preferencia. Algunos registros de operación pueden conservarse según la política de retención.” |

Tono: breve, cálido y específico. Nada de “tu agente está pensando profundamente” ni promesas de velocidad que no fueron medidas. Los montos siempre llevan moneda; las fechas/horas usan la zona seleccionada por la persona.

## Pruebas de diseño: 12 casos

Estas son pruebas propuestas, pendientes de ejecución. Para la primera ronda usar 5–8 participantes del perfil; no declarar validación de mercado a partir de esa muestra.

| ID | Prueba | Evidencia / criterio inicial |
|---|---|---|
| UX-P01 | Primera solicitud sin tutorial | Al menos 4 de 5 participantes completan el inicio sin instrucciones del moderador; registrar dudas y abandonos |
| UX-P02 | Comparación de costo real | Todos identifican total, envío, variante y vendedor; si falta dato, lo reconocen |
| UX-P03 | Comprensión de autorización | Antes de tocar, explica producto, máximo y alcance; cualquier malentendido financiero bloquea el diseño |
| UX-P04 | Estado de pago y pedido | Distingue autorización, pago, pedido confirmado y reembolso recibido en escenarios mezclados |
| UX-P05 | Cerrar y volver | Puede encontrar la misma tarea, su última actualización y el siguiente paso sin duplicarla |
| UX-P06 | Error y resultado incierto | No interpreta “verificando” como fallo definitivo ni intenta volver a pagar; encuentra ayuda |
| UX-P07 | Cancelación | Diferencia detener preparación de solicitar cancelación al comercio; entiende qué está confirmado |
| UX-P08 | Memoria y permisos | Encuentra, corrige y borra preferencia; revoca una conexión y entiende el efecto |
| UX-P09 | Móvil y teclado | 320/360/390/430 CSS px, teclado virtual, nombres largos: monto y CTA nunca tapados; objetivo táctil claro |
| UX-P10 | Accesibilidad | Teclado, foco, zoom 200%, contraste WCAG 2.2 AA y lector de pantalla en recorridos críticos; no depender de color |
| UX-P11 | Confianza y alcance | Distingue fuente verificada, estimación y dato pendiente; no cree que se comprará sin autorización |
| UX-P12 | Fluidez percibida | Instrumentar tiempo a feedback, primera herramienta y tarea completa; movimiento no oculta espera ni bloquea interacción |

Además de usabilidad, las reglas financieras se prueban en servidor: estas pruebas de comprensión nunca sustituyen validación de consentimiento, aislamiento, idempotencia o conciliación.

## Qué mostrar en el primer concepto visual

Prioridad 1: Hoy → comparación → autorización → resultado incierto / confirmado. Prioridad 2: detalle de tarea persistente y memoria editable. Mantener todas las cifras como datos de ejemplo y enlazar componentes entre pantallas.

Para que sea premium, el diseño debe sobrevivir cinco variantes: sin datos, solicitud larga, solo una opción, aprobación vencida y red perdida. Una imagen de portada no demuestra el producto.

### Hipótesis competitivas que sí podemos defender después de medir

1. Menos esfuerzo para saber qué sigue: tarea + siguiente decisión en una vista, medido por éxito sin moderación.
2. Mayor claridad financiera: total, alcance y estado verificables, medido por comprensión y errores de autorización.
3. Mejor continuidad percibida: regresar a la misma tarea y resultado sin reexplicar el contexto, medido por recuperación sin duplicados.
4. Atención local: MXN, entrega y comercios habilitados en México, medida por disponibilidad y resultados realmente resueltos.
5. Postventa integrada: compra no se da por terminada hasta que pedido/devolución tenga seguimiento, medido por resolución y carga de soporte.
6. Memoria bajo control de la persona, medida por descubribilidad de editar/borrar y funcionamiento efectivo de la revocación.

Son hipótesis del producto, no afirmaciones sobre carencias de Muse ni resultados ya obtenidos.
