[Inicio](index.html)

# Claude Code con control de versiones para Windows

Está trabajando con asistencia de IA. Esta realiza cambios en sus archivos. A veces los cambios son brillantes. A veces no lo son. **El control de versiones es como un botón de deshacer para todo su proyecto.** Cada vez que guarda una instantánea (llamada "commit"), crea un punto de restauración al que siempre puede volver. Lo mejor de todo es que puede hacer esto completamente en su computadora y Claude Code lo hace por usted.

## Conceptos Clave

- **WSL (Windows Subsystem for Linux)** - Ejecuta herramientas de Linux como Git de forma nativa en Windows
- **Git** - Rastrea cada cambio en sus archivos en su computadora, creando puntos de restauración a los que puede volver en cualquier momento
- **Commit** - Una instantánea de su proyecto en un punto específico en el tiempo con una descripción de qué cambió
- **Claude Code** - Asistente de codificación de IA que escribe código, corrige errores y maneja operaciones de Git mediante solicitudes simples

## Lo Que Necesitará

- Haber completado [Instalación de Claude Code en Windows](./Install_CLAUDE_Code_Win)
- WSL y Ubuntu instalados
- 20 minutos

## Paso 1: Abra Ubuntu Terminal

- Haga clic en el menú **Start**
- Escriba `Ubuntu`
- Haga clic en **Ubuntu** para abrir la terminal

Verá un símbolo del sistema que termina con `$`.

## Paso 2: Instale Git

- Escriba este comando y presione Enter:
  ```
  sudo apt-get install git
  ```
- Cuando se le solicite, escriba su contraseña y presione Enter
- Espere a que se complete la instalación (10-30 segundos)
- Verifique que Git esté instalado:
  ```
  git --version
  ```

Debería ver algo como `git version 2.34.1`.

## Paso 3: Configure Git con Su Identidad

Git necesita saber quién es usted para los mensajes de commit.

- Configure su nombre y correo electrónico (pueden ser ficticios)
  ```
  git config --global user.name "Su Nombre"
  git config --global user.email "su.correo@ejemplo.com"
  ```

Usar su nombre y correo electrónico ayuda a identificar quién realizó los cambios cuando varias personas trabajan en el proyecto.

## Paso 4: Navegue a una Carpeta de Windows

WSL puede acceder a sus archivos de Windows a través de `/mnt/c/`.

- Navegue a su carpeta de usuario de Windows:
  ```
  cd /mnt/c/Users/SU_USUARIO/Documents
  ```
  Reemplace `SU_USUARIO` con su nombre de usuario real de Windows.
- Verifique que está en el lugar correcto:
  ```
  pwd
  ```

Debería ver `/mnt/c/Users/SU_USUARIO/Documents`.

## Paso 5: Cree una Carpeta de Proyecto

- Cree una carpeta llamada `test_claude`:
  ```
  mkdir test_claude
  ```
- Navegue hacia ella:
  ```
  cd test_claude
  ```

Aquí es donde vivirá su proyecto.

## Paso 6: Inicie Claude Code

- Inicie Claude Code:
  ```
  claude
  ```

Claude Code se ejecuta y espera su solicitud.

## Paso 7: Solicite a Claude que Inicialice Git

- Escriba esta solicitud:
  ```
  Comienza a rastrear los cambios
  ```

Claude inicializa un repositorio de Git en su carpeta (toma 2-5 segundos). ¡Ahora tiene control de versiones!

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

- Abra Windows File Explorer
- Navegue a `Documents\test_claude`
- Haga doble clic en `timer.html` para abrirlo en su navegador
- Pruebe el temporizador:
  - Escriba `1` en el campo de entrada
  - Haga clic en **Start**
  - Observe la cuenta regresiva

**Si algo está roto:** En Claude Code, describa el error: `Veo este error: [describa lo que pasó]. ¿Puedes corregirlo?`

## Paso 10: Solicite a Claude que Haga un Commit

- En Claude Code, escriba:
  ```
  Guarda estos cambios
  ```

Claude hará lo siguiente:
- Verificar qué archivos cambiaron
- Escribir un mensaje de commit descriptivo
- Crear el commit (toma 5-10 segundos)

¡Ha creado su primer punto de guardado! Siempre puede volver a esta versión funcionando.

## Paso 11: Agregue Botones Predefinidos

- En Claude Code, escriba:
  ```
  Agrega dos botones en la parte superior. Si hago clic en ellos, inician automáticamente temporizadores de 1 y 5 minutos
  ```
- Actualice la pestaña de su navegador
- Pruebe: Haga clic en el botón **5 min**
- Si funciona, haga commit de los cambios:
  ```
  Guarda estos cambios
  ```

Creamos un segundo punto de guardado. Esta versión tiene los dos botones funcionando.


## Paso 12: Agregue Otro Botón

- En Claude Code, escriba:
  ```
  Agrega un botón de 15 minutos
  ```
- Actualice la pestaña de su navegador
- Pruebe: Haga clic en el botón **15 min**

**Para este tutorial:** Pretenda que el botón de 15 minutos no funciona correctamente. No haga commit todavía—practicaremos descartando cambios malos.

## Paso 13: Descarte los Cambios

A veces el código de la IA no funciona y necesita comenzar de nuevo desde su último punto de guardado.

- En Claude Code, escriba:
  ```
  descarta estos cambios
  ```
- Claude le pedirá confirmación
- Escriba `yes` y presione Enter
- Actualice su navegador—el botón de 15 minutos desaparece

Claude descarta los nuevos cambios que no nos gustan. ¡El temporizador funciona nuevamente con solo los botones de 1 y 5 minutos!

## Paso 14: Agregue Notificación de Sonido

- En Claude Code, escriba:
  ```
  Agrega una notificación de sonido cuando el temporizador llegue a cero
  ```
- Actualice el navegador y pruebe después de que Claude termine (configure el temporizador para 0.1 minutos)
- Si funciona, haga commit de los cambios:
  ```
  Guarda estos cambios
  ```

## Paso 15: Agregue un Botón de Posponer

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
- El commit de botones predefinidos (1 min y 5 min)
- El commit de notificación de sonido
- El botón de posponer.

¡Note que el intento del botón de 15 minutos no está ahí—lo descartó!

## Paso 17: Examine el Código

- En el navegador que muestra la aplicación, haga clic derecho y seleccione **View Page Source**
- Puede ver el código fuente.
- En Claude Code, pregunte
  ```
  Explica este código. Solo lo general
  ```

## El Flujo de Trabajo Completo

- Solicite a Claude que realice cambios
- Pruebe
- Si funciona → Solicite a Claude que haga commit
- Si falla → Solicite a Claude que lo corrija.
- Incapaz de corregir → Descarte los cambios e intente nuevamente
- Repita

¡Siempre puede volver a cualquier commit. Descarte sin temor—solo haga commit del código que funciona!

## Próximos Pasos

Intente agregar más características a su temporizador:

- **Botón de 15 minutos:** `Agrega un botón preconfigurado de 15 minutos que funcione` (¡rehaga lo que descartamos!)
- **Botón de pausa:** `Agrega un botón de Pausa/Reanudar que alterne el estado del temporizador`
- **Mejor estilo:** `Mejora el diseño visual con un esquema de colores moderno y fuentes más grandes`
- **Barra de progreso:** `Agrega una barra de progreso visual que muestre el tiempo restante`

Recuerde: Pruebe después de cada característica, haga commit después de cada éxito, descarte los fallos.

## Solución de Problemas

- **Error "not a git repository":** Asegúrese de estar en la carpeta test_claude (`cd /mnt/c/Users/SU_USUARIO/Documents/test_claude`)
- **No puede encontrar timer.html en Windows:** El archivo está en `C:\Users\SU_USUARIO\Documents\test_claude\timer.html`
- **Git solicita contraseña:** Escribió mal la contraseña de `sudo`—intente nuevamente con cuidado
- **El temporizador no funciona:** Abra la consola del navegador (haga clic derecho en la página, seleccione **Inspect**, haga clic en la pestaña **Console**), copie cualquier mensaje de error rojo y péguelo en Claude

## Lo Que Puede Preguntarle a Claude

- `¿qué archivos he cambiado?` - Ver cambios sin hacer commit
- `muéstrame las diferencias` - Ver exactamente qué código cambió
- `explica qué hace el código del temporizador` - Entender la implementación
- `crea una rama llamada experimento` - Probar cambios riesgosos de manera segura
- `vuelve al commit anterior` - Deshacer todo desde el último commit

¡Claude maneja todas las operaciones de Git a través del lenguaje natural—no hay comandos que memorizar!

## Resumen del Flujo de Trabajo

- **Configuración:** Instale Git una vez, configure la identidad una vez
- **Desarrollo:** Claude escribe código, usted prueba en el navegador
- **Control de Versiones:** Claude maneja todas las operaciones de Git mediante solicitudes simples
- **Seguridad:** Descarte cambios malos en cualquier momento, vuelva a cualquier commit anterior
- **Local:** Todo permanece en su computadora, no se requiere cuenta ni internet

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 8 de diciembre de 2025.
