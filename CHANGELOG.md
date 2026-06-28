# Registro de Cambios y Tareas (Calculadora)

Este archivo mantiene un registro de todas las modificaciones y tareas pendientes específicas de la aplicación Calculadora, para asegurar que no se rompe nada y mantener el hilo del desarrollo. Como inteligencia artificial, **siempre leeré este archivo antes de realizar cualquier cambio** en la calculadora.

## Tareas Pendientes (Planificadas)

*(Ninguna tarea pendiente por el momento)*

## Cambios Realizados

- **(2026-06-28) Rediseño de Interfaz:** Se eliminó el encabezado "Calculadora Pro" y se redujo el margen inferior del teclado para evitar cortes en la pantalla. Se incorporó correctamente el logo `EliBi`. El botón de "Colores" se rediseñó con estilo 3D y se reubicó en la misma fila del logo. La paleta de colores ahora se despliega en un pop-up superpuesto en lugar de empujar el contenido.
- **(2026-06-28) Modo Diseño Avanzado (Personalización de Temas):** Se implementó un "Modo Diseño" que permite personalizar los colores de cada elemento individual (pantalla, fondo, números, operadores, botón C, botón calcular, botón EliBi, botones de herramientas y fondos de cajas desplegables).
- **(2026-06-28) Guardado de Temas Personalizados:** Se añadió la capacidad de guardar, borrar, sobreescribir y renombrar diseños personalizados mediante `localStorage`, integrando un menú limpio con opciones de "Nuevo", "Guardar", "Borrar" y "Renombrar".
- **(2026-06-28) Mejoras Visuales y de Usabilidad UI:** Se corrigieron los alineamientos de los botones desplegables de herramientas (Descuento, Aumento, IVA), sus cajas de texto y el botón Calcular, dándoles la proporción y el espaciado ("aire") correctos solicitados por el usuario. Se eliminó la "crucecita" en la paleta de temas y se añadió un pop-up semitransparente que muestra el nombre del tema al mantenerlo pulsado.
- **(2026-06-28) Teclado Nativo Bloqueado:** Se previno que el teclado nativo del móvil aparezca al tocar las cajas de Importe o Porcentaje; en su lugar se adaptó el código para que estas cajas se llenen exclusivamente mediante las teclas integradas en la calculadora.
- **(2026-06-28) Menú Pop-up para Botón de Temas:** Se eliminaron los cuadros de diálogo nativos (`confirm`) del sistema para la edición de colores del botón "Temas", reemplazándolos por un pop-up HTML personalizado más limpio y amigable.
- **(2026-06-28) Lógica de Autocompletado en Selector de Color:** Se programó el selector de color (`<input type="color">`) para que al abrirse en el Modo Diseño lea y parta del color base actual del elemento seleccionado (ya sea un color nativo del tema o uno asignado manualmente).
- **(2026-06-28) Corrección Bug Botón C:** Se solucionó el error de CSS inline que impedía que el color personalizado aplicado al botón C sobrescribiera correctamente la clase global `.calc-key.clear`.
- **(2026-06-28) Soporte Offline (PWA):** Se añadió `manifest.json` y `sw.js` (Service Worker) para que la Calculadora pueda instalarse en la pantalla de inicio del iPhone y usarse sin conexión a internet. Se configuró para usar el logo `icono.png`.
- **(2026-06-28) Creación de App Independiente:** Se extrajo el código de la calculadora (HTML, CSS y JS) desde el proyecto original hacia su propio entorno.
- **(2026-06-28) Pantalla Completa:** Ajuste en el CSS para que la calculadora ocupe de manera óptima el 100vw y 100vh de la pantalla de un iPhone.
- **(2026-06-28) Historial de Operaciones:** Se añadió un sistema de historial tipo "ticket" que se despliega al tocar los resultados. Incluye botones funcionales para borrar el historial y cerrar el menú.
- **(2026-06-28) Creación del Registro:** Se ha creado este archivo `CHANGELOG.md` para hacer seguimiento del progreso futuro.
