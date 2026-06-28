# Registro de Cambios y Tareas (Calculadora)

Este archivo mantiene un registro de todas las modificaciones y tareas pendientes específicas de la aplicación Calculadora, para asegurar que no se rompe nada y mantener el hilo del desarrollo. Como inteligencia artificial, **siempre leeré este archivo antes de realizar cualquier cambio** en la calculadora.

## Tareas Pendientes (Planificadas)

*(Ninguna tarea pendiente por el momento)*

## Cambios Realizados

- **(2026-06-28) Soporte Offline (PWA):** Se añadió `manifest.json` y `sw.js` (Service Worker) para que la Calculadora pueda instalarse en la pantalla de inicio del iPhone y usarse sin conexión a internet. Se configuró para usar el logo `icono.png`.
- **(2026-06-28) Creación de App Independiente:** Se extrajo el código de la calculadora (HTML, CSS y JS) desde el proyecto original hacia su propio entorno.
- **(2026-06-28) Pantalla Completa:** Ajuste en el CSS para que la calculadora ocupe de manera óptima el 100vw y 100vh de la pantalla de un iPhone.
- **(2026-06-28) Historial de Operaciones:** Se añadió un sistema de historial tipo "ticket" que se despliega al tocar los resultados. Incluye botones funcionales para borrar el historial y cerrar el menú.
- **(2026-06-28) Creación del Registro:** Se ha creado este archivo `CHANGELOG.md` para hacer seguimiento del progreso futuro.
