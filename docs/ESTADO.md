# Estado para continuar en local

Actualizado: 12 de noviembre de 2026. Las fuentes/precios del presupuesto conservan el corte indicado en los documentos del 11 de noviembre.

## Completado

- Investigación de experiencia, componentes reutilizables, Hermes y límites de proveedores.
- Roadmap completo de desarrollo y validación: alcance de 24 semanas, dependencias y primeros diez días.
- Modelo de costos con verificación independiente de aritmética y escenarios de 25, 100 y 1,000 usuarios.
- Dirección de diseño elegida: Liquid Glass monocromático; grafito oscuro y plata clara.
- Prototipo HTML navegable, con ocho vistas y estados de error, consentimiento, cotización vencida y resultado pendiente.
- Adaptaciones de cinco patrones de BeautifulUI: tareas desplegables, alternativas, barra de solicitud/contexto, actividad y aprobación explícita.
- Verificación del concepto en Chromium a 320, 390 y 1440 px. Las pruebas son del prototipo, no de una aplicación productiva.

## Todavía no implementado

- Aplicación React/TypeScript y backend de producto.
- Autenticación, base de datos, colas y asociación usuario–VM.
- Aprovisionamiento de VMs reales y conexión al motor Hermes.
- Integraciones reales con Finco, Stripe, comercios, correo o WhatsApp.
- Pago, conciliación, soporte y persistencia de memoria reales.
- Benchmarks pagados de modelos ni despliegue productivo.

## Primer trabajo al volver

1. Convertir el flujo del prototipo en componentes React y fixtures, preservando los estados y la accesibilidad.
2. Fijar herramientas/versiones y documentar arranque, build y pruebas. No instalar dos runtimes de conversación por defecto.
3. Evaluar un adaptador de `assistant-ui` frente a CopilotKit/AG-UI con la misma tarea y stream simulado; elegir una ruta.
4. Preparar dos VMs exclusivas y probar Hermes: aislamiento, herramientas, eventos, reconexión, cancelación y costo.
5. Mantener Quote/Consent/Order/Ledger como contratos del servidor; ninguna aprobación visual por sí sola concede permiso financiero.

No declarar la fase técnica completada por tener la interfaz dibujada. El roadmap contiene las puertas de salida y las pruebas necesarias para cada etapa.

## Abrir y editar el concepto

```sh
python3 prototypes/estela/build.py
```

Después abre `prototypes/estela/index.html` en el navegador. En macOS puedes usar:

```sh
open prototypes/estela/index.html
```

El generador utiliza solo la biblioteca estándar de Python; las fuentes están incluidas. Los datos son ficticios y no se envían a terceros. `build.py` contiene la base visual; `beautifului_adapt.py` aplica las interacciones adaptadas.

Para recalcular el presupuesto:

```sh
python3 docs/cost_model.py
```

Esto verifica los supuestos guardados; no consulta precios vigentes ni ejecuta llamadas a proveedores.

## Evidencia y pendientes

Los JSON de `docs/referencias/validacion-*.json` registran ejecuciones realizadas durante la exploración cloud. No constituyen un pipeline CI de este repositorio. Antes de producción faltan dispositivos reales/Safari, lectores de pantalla, usuarios del perfil, servicios y pruebas financieras.

La web directa de BeautifulUI y algunas fuentes de precios estaban bloqueadas por la red del entorno. BeautifulUI se investigó mediante el repositorio enlazado y archivos fijados por commit; no se afirmó haber revisado su catálogo comercial completo.

Los dominios `beautifului.dev`, `www.beautifului.dev` y `api.github.com` se propusieron en el borrador del entorno. Guardar un borrador no habilita por sí solo el acceso de red. Estas limitaciones del entorno cloud no son requisitos del prototipo local.
