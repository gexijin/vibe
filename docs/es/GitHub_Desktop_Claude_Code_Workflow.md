[Inicio](index.html)

# Use GitHub Desktop con Claude Code

Está programando con asistencia de IA. Esta hace cambios en sus archivos. A veces los cambios funcionan perfectamente. A veces no. **El control de versiones es como un botón de deshacer para todo su proyecto.** Cada vez que guarda una instantánea (llamada "commit"), crea un punto de restauración. Siempre puede volver atrás.

Cuando combina [GitHub Desktop](https://desktop.github.com) con [Claude Code](https://claude.com/claude-code), obtiene desarrollo a velocidad de IA con control de versiones profesional.

## Conceptos Clave

**Git** rastrea cada cambio en sus archivos en su computadora.

**GitHub** almacena su código en la nube como respaldo.

**GitHub Desktop** hace que Git sea visual - usted hace clic en botones en lugar de escribir comandos.

**Claude Code** es un asistente de programación de IA que escribe código, corrige errores y crea commits por usted.

## Lo Que Hará

Construir una aplicación simple de temporizador con Claude Code y rastrear todos los cambios con GitHub Desktop:
- Crear proyecto y aplicación de temporizador
- Probar y corregir errores
- Hacer commit y push de los cambios
- Descartar cambios malos e intentar de nuevo
- Dejar que Claude automatice los commits

## Lo Que Necesitará

- Haber completado [Instalación de Claude Code en Windows](./Install_CLAUDE_Code_Win) o [Instalación de Claude Code en Mac](./Install_Claude_Code_MacOS)
- Haber completado [Introducción al Control de Versiones](./Github_desktop)
- 20 minutos

## Paso 1: Cree Su Proyecto

- Abra **GitHub Desktop**
- Haga clic en **File** → **New Repository**
- Complete:
  - **Name:** `test_claude`
  - **Description:** `A timer app built with Claude Code`
  - **Local Path:** carpeta Documents
  - **Marque** "Initialize this repository with a README"
- Haga clic en **Create Repository**
- Haga clic en **Publish repository** en la parte superior
- Haga clic en **Publish Repository**

Ahora tiene un proyecto local y un respaldo en la nube en GitHub.

## Paso 2: Solicite a Claude que Cree la Aplicación de Temporizador

- Abra su **terminal**
- Navegue a su proyecto:
  ```
  cd ~/Documents/test_claude
  ```
- Inicie Claude Code:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el tutorial de instalación ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

- Escriba esta solicitud:
  ```
  Crea una aplicación simple de temporizador de cuenta regresiva en un solo archivo llamado timer.html.
  Debe tener:
  - Un campo de entrada para establecer minutos
  - Botones de Iniciar y Detener
  - Una pantalla que muestre el tiempo restante en formato MM:SS
  - Cuando el temporizador llegue a cero, mostrar '¡Se acabó el tiempo!'
  Mantenlo simple con CSS y JavaScript en línea.
  ```

Claude crea el archivo `timer.html` (toma 10-30 segundos).

## Paso 3: Pruebe el Temporizador

- En GitHub Desktop, haga clic en **Repository** → **Show in Finder/Explorer**
- **Haga doble clic** en `timer.html` para abrirlo en su navegador
- Pruebe el temporizador:
  - Escriba `1` en el campo de entrada
  - Haga clic en **Start**
  - Observe la cuenta regresiva

**Si funciona:** Continúe al Paso 5.
**Si algo está roto:** Continúe al Paso 4.

## Paso 4: Corrija Errores (Si Es Necesario)

- Abra la consola del navegador (haga clic derecho en la página → **Inspect** → pestaña **Console**)
- Copie cualquier mensaje de error en rojo
- Regrese a Claude Code en su terminal
- Pegue el error:
  ```
  Veo este error: [pegue el error]. ¿Puedes arreglarlo?
  ```
- Actualice el navegador (haga clic en el botón de recarga o clic derecho → **Reload**) y pruebe nuevamente

## Paso 5: Revise los Cambios

- Cambie a **GitHub Desktop**
- **Panel izquierdo:** Muestra los archivos modificados (`timer.html`)
- **Panel derecho:** Muestra el código (verde = agregado)
- Lea para entender lo que Claude creó

Siempre revise el código generado por IA antes de hacer commit.

## Paso 6: Haga Commit Manualmente

- En la parte inferior izquierda, en el campo **Summary**, escriba:
  ```
  Crear aplicación de temporizador inicial con funcionalidad de inicio/detener
  ```
- Haga clic en **Commit to main**

Ha creado un punto de guardado.

**Buenos mensajes:** "Crear aplicación de temporizador inicial", "Corregir botón de inicio"
**Malos mensajes:** "cambios", "actualizar", "asdf"

## Paso 7: Haga Push a GitHub

- Haga clic en el botón **Push origin** en la parte superior
- Verifique: **Repository** → **View on GitHub** para ver su código en línea

Su código ahora está respaldado en la nube.

## Paso 8: Agregue Notificación de Sonido

- En el terminal de Claude Code:
  ```
  Agrega una notificación de sonido cuando el temporizador llegue a cero. Usa el
  sonido de pitido integrado del navegador o crea una alerta de audio simple.
  ```
- Pruebe: Actualice el navegador, configure el temporizador para 0.1 minutos, haga clic en Start

**Para este tutorial:** Finja que el sonido no funciona bien. No haga commit todavía.

## Paso 9: Descarte los Cambios Malos

Algunas veces la IA nos lleva por el camino equivocado y necesitamos empezar de nuevo desde nuestro último commit (punto de guardado).

- Abra **GitHub Desktop**
- Haga clic en el menú **Branch** → **Discard All Changes**
- Haga clic en **Discard Changes** para confirmar
- Actualice el navegador - el temporizador funciona sin el sonido

Acaba de desechar código que no funcionaba y volvió a su último punto de guardado.

## Paso 10: Rehaga Desde Cero

- En Claude Code:
  ```
  Agrega una notificación de sonido cuando el temporizador llegue a cero. Esta vez, usa un
  elemento de audio HTML5 con un sonido de pitido simple generado por la Web Audio API.
  Asegúrate de que maneje las restricciones de reproducción automática del navegador de forma elegante.
  ```
- Pruebe inmediatamente (actualice el navegador, configure 0.1 minutos, Start)

**Si funciona:** Continúe al Paso 11.
**Si no:** Pegue el error a Claude o intente de nuevo.

## Paso 11: Permita que Claude Haga Commit y Push

- En Claude Code:
  ```
  confirma y envía mis cambios
  ```

Claude verificará los cambios, escribirá un mensaje de commit, hará commit y push (10-20 segundos).

**Cuándo usar:**
- Commits manuales: Cuando está aprendiendo o desea control
- Commits de Claude: Cuando trabaja rápido y desea buenos mensajes

## Paso 12: Solicite a Claude que Resuma los Cambios

- En Claude Code:
  ```
  ¿qué archivos he cambiado?
  ```

Claude explica sus cambios en lenguaje sencillo.

**Intente:** `explica qué hace el código de audio` o `muéstrame los últimos 5 commits`

## Paso 13: Vea el Historial

- En **GitHub Desktop**, haga clic en la pestaña **History**

Verá:
- Initial commit (README)
- Create initial timer app
- Add improved sound notification

Note que el primer intento fallido de sonido no está ahí - lo descartó. Solo el código que funciona llegó a sus commits.

## Desafíos
- Sonido personalizado: Descargue un .mp3 gratuito de [freesound.org](https://freesound.org), póngalo en la carpeta de su proyecto, solicite a Claude que lo use
- Múltiples temporizadores: `Permite a los usuarios crear y ejecutar múltiples temporizadores simultáneamente`
- Barra de progreso: `Agrega una barra de progreso que muestre visualmente cuánto tiempo queda`

**Recuerde:** Pruebe después de cada característica, haga commit después de cada éxito, descarte los fallos.

**Vea su proyecto en GitHub.com:** Haga clic en **Repository** → **View on GitHub** en GitHub Desktop para ver su historial completo de commits y código en línea.

## Solución de Problemas

**"Authentication failed":** GitHub Desktop → File/Preferences → Accounts → cierre sesión y vuelva a iniciar sesión

**Claude dice "not a git repository":** Asegúrese de estar en la carpeta correcta (`cd ~/Documents/test_claude`)

**El temporizador no funciona:** Abra la consola del navegador (clic derecho → **Inspect** → **Console**), copie los errores, péguelos en Claude

**¿Necesita ayuda?** [Documentación de GitHub Desktop](https://docs.github.com/en/desktop) • [Documentación de Claude Code](https://docs.anthropic.com/en/docs/claude-code)

## El Flujo de Trabajo Completo

- Solicite a Claude que haga cambios
- Pruebe en el navegador
- Si funciona → Revise y haga commit
- Si falla → Descarte e intente de nuevo
- Haga push a GitHub
- Repita

Commits manuales cuando desea control. Commits de Claude cuando desea velocidad. Descarte sin miedo - solo haga commit de código que funciona.

## Próximos Pasos

Intente agregar características a su temporizador:

**Victorias rápidas:**
- Botones preestablecidos para 5, 10, 15 minutos: `Agrega tres botones preestablecidos: "5 min", "10 min" y "15 min"`
- Botón de pausa: `Agrega un botón de Pausa/Reanudar que alterne el estado del temporizador`
- Mejor estilo: `Mejora el diseño visual con un esquema de colores moderno`

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
