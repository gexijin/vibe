[Inicio](index.html)

# Claude Code con control de versiones local para Mac

Está programando con asistencia de IA. Esta hace cambios en sus archivos. A veces los cambios funcionan perfectamente. A veces no. **El control de versiones es como un botón de deshacer para todo su proyecto.** Cada vez que guarda una instantánea (llamada "commit"), crea un punto de restauración al que siempre puede volver. Lo mejor de todo es que puede hacer esto completamente en su computadora y Claude Code lo hace por usted.

## Conceptos Clave

- **Terminal** - Interfaz de línea de comandos integrada de Mac para ejecutar comandos
- **Git** - Rastrea cada cambio en sus archivos en su computadora, creando puntos de restauración a los que puede volver en cualquier momento
- **Commit** - Una instantánea de su proyecto en un momento específico con una descripción de lo que cambió
- **Claude Code** - Asistente de codificación AI que escribe código, corrige errores y maneja operaciones de Git mediante solicitudes simples

## Lo Que Necesitará

- Haber completado [Installing Claude Code on Mac](./Install_Claude_Code_MacOS)
- 30 minutos

## Paso 1: Abra Terminal

Elija uno de estos métodos:

- **Spotlight:** Presione `Command (⌘) + Space`, escriba `Terminal`, presione Enter
- **Finder:** Abra **Applications** > **Utilities** > **Terminal**
- **Launchpad:** Haga clic en **Launchpad** en el Dock, busque `Terminal`

Verá un prompt de comando que termina con `$` o `%`.

## Paso 2: Instale Git

Mac a menudo tiene Git preinstalado. Verifiquemos:

- Escriba este comando y presione Enter:
  ```
  git --version
  ```

**Si ve un número de versión** (como `git version 2.39.0`), Git ya está instalado—pase al Paso 3.

**Si ve "command not found"** o un popup solicitando instalar herramientas de desarrollador:
- Haga clic en **Install** en el popup, o ejecute:
  ```
  xcode-select --install
  ```
- Espere a que se complete la instalación (1-5 minutos)
- Verifique que Git esté instalado:
  ```
  git --version
  ```

Debería ver algo como `git version 2.39.0`.

## Paso 3: Configure Git con Su Identidad

Git necesita saber quién es usted para los mensajes de commit.

- Establezca su nombre y correo electrónico (pueden ser ficticios):
  ```
  git config --global user.name "Su Nombre"
  git config --global user.email "su.correo@ejemplo.com"
  ```

Usar su nombre y correo electrónico ayuda a identificar quién hizo cambios cuando varias personas trabajan en el proyecto.

## Paso 4: Navegue a Su Carpeta de Documentos

- Navegue a su carpeta Documents:
  ```
  cd ~/Documents
  ```
- Verifique que esté en el lugar correcto:
  ```
  pwd
  ```

Debería ver `/Users/SU_USUARIO/Documents`.

## Paso 5: Cree la Carpeta del Proyecto

- Cree una carpeta llamada `test_claude`:
  ```
  mkdir test_claude
  ```
- Navegue dentro de ella:
  ```
  cd test_claude
  ```

Aquí es donde vivirá su proyecto.

## Paso 6: Inicie Claude Code

- Inicie Claude Code:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el [tutorial de instalación](./Install_Claude_Code_MacOS.md). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 7: Pida a Claude que Inicialice Git

- Escriba esta solicitud:
  ```
  Comienza a rastrear los cambios
  ```

Claude inicializa un repositorio Git en su carpeta (toma 2-5 segundos). ¡Ahora tiene control de versiones!

## Paso 8: Construya la Aplicación de Temporizador

- En Claude Code, escriba:
  ```
  Crea una aplicación simple de temporizador en un solo archivo llamado timer.html.
  Debe tener:
  - Un campo de entrada para establecer minutos
  - Botones de Iniciar y Detener
  - Una pantalla que muestre el tiempo restante en formato MM:SS
  ```

Claude crea `timer.html` (toma 10-30 segundos) con el código CSS y JavaScript.

## Paso 9: Pruebe el Temporizador

- Abra Finder
- Navegue a **Documents** > **test_claude**
- Haga doble clic en `timer.html` para abrirlo en su navegador
- Pruebe el temporizador:
  - Escriba `1` en el campo de entrada
  - Haga clic en **Start**
  - Observe la cuenta regresiva

**Si algo no funciona:** En Claude Code, describa el error: `Veo este error: [describa lo que pasó]. ¿Puedes corregirlo?`

## Paso 10: Pida a Claude que Haga Commit

- En Claude Code, escriba:
  ```
  Guarda estos cambios.
  ```

Claude:
- Verificará qué archivos cambiaron
- Escribirá un mensaje de commit descriptivo
- Creará el commit (toma 5-10 segundos)

¡Ha creado su primer punto de guardado! Siempre puede volver a esta versión funcional.

## Paso 11: Agregue Botones Predefinidos

- En Claude Code, escriba:
  ```
  Agrega dos botones en la parte superior. Si hago clic en ellos, inician automáticamente temporizadores de 1 y 5 minutos.
  ```
- Actualice la pestaña de su navegador (o presione `Command (⌘) + R`)
- Pruebe: Haga clic en el botón **5 min**
- Si funciona, haga commit de los cambios:
  ```
  Guarda estos cambios.
  ```

Creamos un segundo punto de guardado. Esta versión tiene los dos botones funcionando.

## Paso 12: Agregue Otro Botón

- En Claude Code, escriba:
  ```
  Agrega un botón de 15 minutos.
  ```
- Actualice la pestaña de su navegador (presione `Command (⌘) + R`)
- Pruebe: Haga clic en el botón **15 min**

**Para este tutorial:** Pretenda que el botón de 15 minutos no funciona correctamente. No haga commit todavía—practicaremos descartando cambios malos.

## Paso 13: Descarte los Cambios

A veces el código de IA no funciona y necesita volver a empezar desde su último punto de guardado.

- En Claude Code, escriba:
  ```
  descarta estos cambios
  ```
- Claude pedirá confirmación
- Escriba `yes` y presione Enter
- Actualice su navegador—el botón de 15 minutos desaparece

Claude descarta los nuevos cambios que no nos gustan. ¡El temporizador funciona de nuevo con solo los botones de 1 y 5 minutos!

## Paso 14: Agregue Notificación de Sonido

- En Claude Code, escriba:
  ```
  Agrega una notificación de sonido cuando se acabe el tiempo
  ```
- Actualice el navegador y pruebe después de que Claude termine (configure el temporizador para 0.1 minutos)
- Si funciona, haga commit de los cambios:
  ```
  Guarda estos cambios
  ```

## Paso 15: Agregue el Botón de Repetición

- En Claude Code, escriba:
  ```
  El sonido debe continuar hasta que haga clic en un botón para posponerlo
  ```
- Actualice el navegador y pruebe después de que Claude termine (configure el temporizador para 0.1 minutos)
- Si funciona, haga commit de los cambios:
  ```
  Guarda estos cambios
  ```

## Paso 16: Vea Su Historial de Commits

- En Claude Code, escriba:
  ```
  muestra mi historial de cambios
  ```

Claude muestra sus commits en un formato legible. Verá:
- Su commit inicial de la aplicación de temporizador
- El commit de los botones predefinidos (1-min y 5-min)
- El commit de la notificación de sonido
- El commit del botón de repetición

¡Note que el intento del botón de 15 minutos no está ahí—lo descartó!

## Paso 17: Examine el Código

- En el navegador que muestra la aplicación, haga clic derecho y seleccione **View Page Source** (o presione `Option (⌥) + Command (⌘) + U`)
- Puede ver el código fuente.
- En Claude Code, pregunte:
  ```
  Explica este código. Solo lo general
  ```

## El Flujo de Trabajo Completo

- Pida a Claude que haga cambios
- Pruebe
- Si funciona → Pida a Claude que haga commit
- Si falla → Pida a Claude que lo corrija.
- Imposible de corregir → Descarte los cambios e intente de nuevo
- Repita

¡Siempre puede volver a cualquier commit. Descarte sin miedo—solo haga commit del código que funciona!

## Próximos Pasos

Intente agregar más características a su temporizador:

- **Botón de 15 minutos:** `Agrega un botón preconfigurado de 15 minutos que funcione` (¡rehaga lo que descartamos!)
- **Botón de pausa:** `Agrega un botón de Pausa/Reanudar que alterne el estado del temporizador`
- **Mejor estilo:** `Mejora el diseño visual con un esquema de colores moderno y fuentes más grandes`
- **Barra de progreso:** `Agrega una barra de progreso visual que muestre el tiempo restante`

Recuerde: Pruebe después de cada característica, haga commit después de cada éxito, descarte los fallos.

## Solución de Problemas

- **Error "not a git repository":** Asegúrese de estar en la carpeta test_claude (`cd ~/Documents/test_claude`)
- **No puede encontrar timer.html en Finder:** El archivo está en `/Users/SU_USUARIO/Documents/test_claude/timer.html`
- **Los comandos de Git no funcionan:** Asegúrese de haber completado el Paso 2 e instalado Git
- **El temporizador no funciona:** Abra la consola del navegador (haga clic derecho en la página, seleccione **Inspect**, luego haga clic en la pestaña **Console**), copie cualquier mensaje de error en rojo y péguelo en Claude

## Lo Que Puede Pedirle a Claude

- `¿qué archivos he cambiado?` - Ver cambios sin commit
- `muéstrame las diferencias` - Ver exactamente qué código cambió
- `explica qué hace el código del temporizador` - Entender la implementación
- `crea una rama llamada experimento` - Probar cambios arriesgados de forma segura
- `vuelve al commit anterior` - Deshacer todo desde el último commit

¡Claude maneja todas las operaciones de Git mediante lenguaje natural—no hay comandos que memorizar!

## Resumen del Flujo de Trabajo

- **Configuración:** Instale Git una vez, configure la identidad una vez
- **Desarrollo:** Claude escribe código, usted prueba en el navegador
- **Control de Versiones:** Claude maneja todas las operaciones de Git mediante solicitudes simples
- **Seguridad:** Descarte cambios malos en cualquier momento, vuelva a cualquier commit anterior
- **Local:** Todo permanece en su computadora, no se requiere cuenta ni internet

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 8 de diciembre de 2025.
