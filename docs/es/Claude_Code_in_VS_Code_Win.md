[Inicio](index.html)

# Configure VS Code para Claude Code en WSL

Ya instaló WSL y Claude Code en su máquina Windows, ahora necesita un editor visual para trabajar con su código. VS Code conecta Windows con su entorno Linux, permitiéndole editar archivos visualmente mientras ejecuta Claude Code en el terminal integrado. Piense en VS Code como una ventana a su mundo Linux.

## Conceptos Clave

- **VS Code** - Editor de código gratuito de Microsoft que se ejecuta en Windows pero puede conectarse a WSL
- **Extensión WSL** - Conecta VS Code a su entorno Linux para ejecutar herramientas Linux como Claude Code
- **Terminal Integrado** - Panel de terminal dentro de VS Code que se ejecuta en su entorno WSL (Linux)
- **/mnt/c/** - Forma en que WSL accede a sus archivos de Windows (ej: `/mnt/c/Users/...` = `C:\Users\...`)

## Lo Que Necesitará

- Haber completado [Instalar Claude Code en Windows](./Install_CLAUDE_Code_Win)
- Haber completado [Conceptos Básicos de VS Code](./VS_Code_Getting_Started)
- 10-15 minutos

## Paso 1: Cree una Carpeta de Proyecto

- Abra **File Explorer** (haga clic en el icono de carpeta en su barra de tareas)
- Navegue a **Documents**
- Haga clic derecho en el espacio vacío, seleccione **New > Folder**
- Nombre la carpeta `test_claude`

## Paso 2: Inicie VS Code

- Haga clic en el **botón de Inicio de Windows** (esquina inferior izquierda de su pantalla)
- Escriba `Visual Studio Code` o `VS Code` en el cuadro de búsqueda
- Haga clic en **Visual Studio Code** cuando aparezca en los resultados de búsqueda
- VS Code se abre con una pestaña de bienvenida - puede cerrar esta pestaña


## Paso 3: Instale la Extensión WSL

- En VS Code, haga clic en el icono **Extensions** en la barra lateral izquierda (icono de cuatro cuadrados)
- Escriba `WSL` en el cuadro de búsqueda
- Encuentre **WSL** de Microsoft (debería ser el primer resultado)
- Haga clic en el botón azul **Install**
- Espere unos segundos a que se complete la instalación

## Paso 4: Conecte VS Code a WSL

- Observe la esquina inferior izquierda de VS Code - verá un icono azul o verde
- Haga clic en este icono para abrir el menú de conexión remota
- Seleccione **Connect to WSL** del menú
- VS Code se recargará y se conectará a su instalación de Ubuntu
- La esquina inferior izquierda ahora debería mostrar **WSL: Ubuntu**

La primera vez que se conecta, VS Code instala un pequeño servidor en WSL. Esto toma alrededor de 30 segundos.

## Paso 5: Abra la Carpeta en VS Code

- En VS Code (todavía conectado a WSL), haga clic en **File** en la barra de menú, luego en **Open Folder**
- Aparece un menú desplegable **Open Folder** en la parte superior central
- Encuentre su carpeta escribiendo:
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Reemplace `YOUR_USERNAME` con su nombre de usuario de Windows (por ejemplo, `John.Smith`)
- Haga clic en **OK** y VS Code se recargará con su carpeta `test_claude`
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**


## Paso 6: Inicie Claude Code

- Después de que VS Code se recargue, abra un nuevo terminal: haga clic en **Terminal** en la barra de menú, luego en **New Terminal**
- En el panel del terminal, escriba:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el [tutorial de instalación](./Install_CLAUDE_Code_Win.md). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 7: Pruebe el Flujo de Trabajo

- En Claude Code, escriba:
```
Escribe un artículo breve explicando por qué a los LLMs les gusta usar el formato Markdown. Guárdalo como article.md
```
- Claude Code crea el archivo y verá aparecer `article.md` en el panel Explorer a la izquierda
- Haga clic en `article.md` en el Explorer para verlo en el editor
- Para previsualizar el artículo formateado: haga clic derecho en la pestaña `article.md` y seleccione **Open Preview**
- Verá el Markdown renderizado con encabezados, viñetas y formato adecuados

## Reabrir Claude en VS Code Más Tarde

Después de cerrar VS Code, puede volver a sus proyectos de WSL de estas formas:

- **Opción A:** Abra VS Code, haga clic en la esquina inferior izquierda, seleccione **Connect to WSL**, luego **File > Open Recent**. Seleccione `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude [WSL: Ubuntu]`
- **Opción B:** Abra la aplicación Ubuntu desde Windows, navegue a su proyecto en el terminal y escriba `code .`

VS Code recuerda sus carpetas recientes, por lo que la Opción A con Open Recent suele ser la más rápida.

## Próximos Pasos

- Pida a Claude Code que explique una base de código existente: "Explica qué hace este proyecto"
- Haga que Claude Code le ayude a escribir nuevas funcionalidades: "Agrega una función que calcule el promedio de una lista"
- Use Claude Code para corregir errores: "Este código da un error, ¿puedes arreglarlo?"
- Pruebe la extensión de VS Code de Claude Code para una interfaz visual con diferencias en línea (busque "Claude Code" en Extensions)
- Para manejar archivos más grandes de manera más eficiente, cree una carpeta en el sistema de archivos de WSL (`/home/user/`). Desde Windows, busque el icono de Linux en la parte inferior de la barra lateral en File Explorer o ingrese `\\wsl.localhost\` en la barra de direcciones

## Solución de Problemas

- **"WSL: Ubuntu" no aparece en la esquina inferior izquierda** - Asegúrese de que WSL esté instalado correctamente; intente abrir el terminal de Ubuntu primero para verificar que funcione
- **El Terminal muestra PowerShell en lugar de Linux** - Haga clic en la flecha desplegable junto al símbolo **+** en el panel del terminal y seleccione **Ubuntu (WSL)**
- **Comando `claude` no encontrado** - Ejecute `claude --version` para verificar si Claude Code está instalado; si no está, siga primero el tutorial de instalación de WSL

## Resumen del Flujo de Trabajo

- **VS Code** se ejecuta en Windows y proporciona la interfaz del editor visual
- **Extensión WSL** conecta VS Code a Ubuntu para ejecutar herramientas Linux
- **Terminal Integrado** ejecuta Claude Code dentro de WSL
- Sus archivos permanecen en Windows (carpeta Documents) y WSL accede a ellos a través de `/mnt/c/`
- Edite archivos en el editor, converse con Claude Code en el terminal: lo mejor de ambos mundos

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 10 de diciembre de 2025.
