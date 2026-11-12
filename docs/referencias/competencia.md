# Investigación de experiencia competitiva: Muse y agentes personales

Fecha: 11 de noviembre de 2026. Trabajo de descubrimiento; no se utilizó ninguna app comercial ni se hicieron compras, autenticaciones o contactos con proveedores.

## Conclusión

No es responsable afirmar que el concepto supera a Muse a partir de esta sesión: la página oficial de Meta y las webs comerciales devolvieron 403 por política de red. Sí hay una oportunidad de diseño concreta que podemos validar sin copiar: un asistente sereno, centrado en resultados, con decisiones y fuentes claras; continuidad en segundo plano; español y compras mexicanas; y separación visible entre propuesta, autorización, ejecución y resultado confirmado.

La recomendación no es importar una consola open source y cambiarle colores. Es conservar Hermes como motor privado y construir una experiencia de consumo propia sobre componentes reutilizables. Lo premium debe verse en jerarquía, interacción, texto, recuperación y confianza, además del acabado gráfico.

## Evidencia y alcance

| Fuente | Estado de esta sesión | Qué establece | Qué no establece |
|---|---|---|---|
| [Meta: presentación Muse](https://about.fb.com/ltam/news/2026/09/presentamos-muse-el-primer-agente-de-ia-personal-del-mundo-creado-para-todos/) | Bloqueada (403) | El contexto previo aporta anuncio y actualización México 05/11/2026 | No hemos inspeccionado ni la UI ni capacidades actuales; no atribuir pantallas, onboarding, precio o funciones específicas |
| [Manus](https://manus.im/) | Bloqueada (403) | Solo identifica un candidato de comparación | No usar para puntuar calidad, funcionalidad o apariencia |
| [OpenAI Operator](https://openai.com/index/introducing-operator/) | Bloqueada (403) | Candidato de comparación histórica | No implica que el producto actual sea idéntico ni acceso a su UX actual |
| [Microsoft MagenticLite README](https://github.com/microsoft/magentic-ui/blob/main/README.md) | Texto reconsultado | Main se presenta como MagenticLite, sucesor de Magentic-UI; navegador + archivos, dirigir/aprobar/tomar control, VM Quicksand, licencia MIT | No es una prueba de rendimiento ni una app financiera lista; videos oficiales bloqueados |
| [MagenticLite configuración](https://github.com/microsoft/magentic-ui/blob/main/docs/configuration.md) | Texto reconsultado | Onboarding de endpoints; Settings; opciones separadas para detalles de tools/razonamiento; política de aprobación configurable | La configuración interna no es una buena portada de consumo por sí misma |
| [MagenticLite Transparency Note](https://github.com/microsoft/magentic-ui/blob/main/docs/TRANSPARENCY_NOTE.md) | Texto reconsultado | Es prototipo de investigación; sus pruebas dependen de Fara1.5 + MagenticBrain; detección crítica del navegador depende del modelo; limita tareas largas y datos sensibles | Sustituir modelo no conserva garantías. No es aprobación para pagos desatendidos |
| [MagenticLite limitaciones](https://github.com/microsoft/magentic-ui/blob/main/docs/limitations.md) | Texto reconsultado | Declara problemas con resumen, conversaciones largas, steering, archivos grandes, subir archivos e imágenes de entrada | No extrapolar a Hermes ni a todas las apps agentes |
| [Hermes README](https://github.com/NousResearch/hermes-agent/blob/main/README.md) | Texto reconsultado | Memoria, herramientas, automatización, varios canales/proveedores, avisos de licencia MIT; base reutilizable | No documenta aquí una PWA de consumo terminada con nuestros flujos financieros |
| [Browser Use Web UI README](https://github.com/browser-use/web-ui/blob/main/README.md) | Texto reconsultado | UI Gradio, navegador propio, sesiones persistentes, grabación y selección de LLM | Imagen `assets/web-ui.png` inspeccionada: es un logotipo, no screenshot. No se puntuó la apariencia de pantallas |
| [OpenManus README](https://github.com/FoundationAgents/OpenManus/blob/main/README.md) | Texto reconsultado | Agente abierto, integración Browser Use MCP, MIT declarado | No es Manus comercial ni evidencia de equivalencia de calidad/UX |

Se probó por error/candidatura el dominio muse.ai: **no se ha establecido que pertenezca al producto de Meta y no se usa como evidencia**. Los intentos de acceso y documentos leídos se guardan para trazabilidad, no como prueba de contenido que no se pudo abrir.

## Hallazgo de versiones que importa

La rama `main` del repositorio `microsoft/magentic-ui` ahora se presenta como **MagenticLite**, no la versión 0.1 antigua. El README enlaza la rama `magentic-ui-0.1` para el producto previo; el Transparency Note incluso emplea otra grafía para la rama anterior. Usar el README actual como fuente del estado actual, fijar commit antes de reutilizar código y no mezclar capturas de 0.1 con capacidades del main.

El prototipo de Microsoft es una buena fuente conceptual de colaboración humano-agente: steer, approve, take over. Sin embargo, sus salvaguardas de navegador dependen de Fara; no se transfieren automáticamente a Groq/Qwen/Hermes. La aprobación de pagos del proyecto debe seguir siendo determinista y externa al agente.

## Qué significa competir, sin inventar defectos de Muse

Estos son objetivos nuestros, no afirmaciones de que Muse carezca de ellos:

1. **Claridad de ejecución:** poder responder en una mirada qué está haciendo, qué falta y cuándo necesita al usuario.
2. **Control sin fricción:** permitir corregir objetivo, presupuesto, selección o fecha sin reiniciar toda la conversación.
3. **Continuidad:** trabajo en segundo plano y reanudación consistente; la VM es infraestructura, no un estado críptico en la portada.
4. **Resultado utilizable:** una comparación, archivo, pedido, plan o recordatorio, no una pared de texto genérico.
5. **Confianza de compra:** precio total, variante, vendedor, domicilio parcial y vigencia juntos antes de autorizar.
6. **Memoria gobernable:** preferencias editables con origen; no sensación de vigilancia ni magia irreversible.
7. **Recuperación digna:** errores útiles, siguiente paso claro, soporte y estados desconocidos honestos.
8. **Contexto México:** español natural, MXN, envío local, CFDI cuando corresponda y explicación correcta del proveedor financiero.

## Dirección de experiencia premium recomendada

### 1. Inicio: la tarea importante primero

Un saludo breve, campo de intención principal, dos o tres sugerencias contextuales y tarjetas de tareas que necesitan atención. Evitar grillas de 20 botones, métricas sin sentido, selección de modelos o tarjetas de saldo ficticio. El campo permite texto y adjuntos; voz posterior si se valida. Ejemplos de tareas editables, no promesas de acceso a comercios sin convenio.

### 2. Conversación + espacio de trabajo

Conversación concisa como hilo conductor; resultados estructurados en paneles/cards. En desktop, workspace al lado cuando hay algo que comparar o revisar. En móvil, resultado a pantalla completa con volver al contexto; no dos columnas comprimidas.

Muestra estados externos verificables: “Comparando opciones”, “Necesito tu aprobación”, “Verificando el pago”, “Pedido confirmado”. Los detalles de herramientas y eventos pueden desplegarse; no mostrar razonamiento interno como justificación del dinero.

### 3. Bandeja de decisiones

Una vista de lo que requiere intervención, independiente del scroll del chat. Fecha límite, monto y razón de la decisión visibles. Rechazar/cambiar debe sentirse tan legítimo y accesible como aprobar.

### 4. Comparación editorial

Dos o tres opciones; un candidato recomendado con explicación breve y trazable. Propiedades comparables: total, entrega, vendedor, devolución y variante. Señalar cuándo falta dato. Acciones: elegir, preguntar, descartar; no “comprar” antes de la aprobación formal.

### 5. Aprobación sobria

Hoja o panel dedicado con producto/variante, vendedor, total máximo MXN, envío, domicilio parcial, vigencia y permiso. Botón claro “Autorizar hasta $X”, cambiar/rechazar accesibles. Reautenticación cuando el riesgo lo exija. Después mostrar ejecución, no éxito anticipado.

### 6. Memoria y espacio personal

Categorías pequeñas y comprensibles: preferencias, documentos y conexiones. Cada preferencia editable, dato sensible protegido, exportación/revocación a mano. No usar la etiqueta “VM” para información que el consumidor solo necesita como “Tu espacio”; sí explicar persistencia y uso de datos en detalles.

### 7. Historial de resultados

Tarjetas con entregable y estado final, no listas interminables de mensajes. Pedido, seguimiento, recibo, ayuda y devolución próximos entre sí. Cuenta del servicio separada de fondos de compra; marca e identidad legal del proveedor pendientes de Finco.

## Tres tareas iniciales para demostrar valor

- Comparar tres opciones de un artículo para una necesidad concreta, con presupuesto y entrega; terminar en cotización simulada revisable.
- Preparar un plan personal a partir de restricciones y preferencias editables; generar un entregable sin pago.
- Seguir un pedido o pendiente a partir de información suministrada por el usuario; recordatorio y estado visible, sin fingir acceso a un comercio.

## Qué adaptar de los comparables abiertos

| Elemento | Adaptar | No importar sin cambio |
|---|---|---|
| MagenticLite | “Dirigir / aprobar / tomar control”, estado de tarea, sandbox como frontera, revelado progresivo de herramientas | Seguridad dependiente de otro modelo; onboarding de endpoints al usuario final; prototipo de investigación como producto financiero |
| Hermes | Motor, memoria, herramientas y automatización con perímetro privado | Llaves administrativas, skills con autoridad financiera, herencia de sesiones entre usuarios |
| Browser Use | Grabación/reproducción para evidencia, persistencia de navegador, observación del trabajo | Consola de configuraciones como home premium; compartir un contexto de navegador |
| OpenManus | Ideas de composición y protocolo MCP cuando sean útiles | Suponer equivalencia con Manus comercial; introducir segundo orquestador por defecto |

## Pruebas de diseño para esta fase

Propuestas, no ejecutadas:

- Mostrar una tarea en curso durante cinco segundos: al menos 4/5 participantes explican estado y siguiente paso sin ayuda.
- Antes de autorizar, todos identifican total máximo, vendedor y qué cambia si rechazan. Cualquier confusión monetaria exige rediseño.
- Al ver “verificando”, nadie interpreta “pedido confirmado”.
- Corregir presupuesto/variante no requiere volver a redactar todo el objetivo.
- Terminar comparación, revisar aprobación, cancelar y encontrar memoria en móvil con una mano, zoom y teclado.
- Revisar estados vacíos, largos, offline, timeout y error con el mismo nivel de diseño que el caso feliz.

## Limitación material y siguiente evidencia requerida

Para una comparación visual directa con Muse hace falta acceso a su sitio/app oficial o capturas autorizadas y fechadas de onboarding, home, tarea, decisión y resultado. Hasta disponer de ello, usar el lenguaje “dirección para competir” y no “rediseño superior a Muse” o una tabla de funciones inventadas. La investigación de componentes y las maquetas propias sí puede continuar ahora.
