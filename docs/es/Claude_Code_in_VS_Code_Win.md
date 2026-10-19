---
title: "Configure VS Code para Claude Code en Windows"
lang: "es"
---
[Inicio](index.html)

# Configure VS Code para Claude Code en Windows

Ya instaló Claude Code en su máquina Windows, ahora necesita un editor visual para trabajar con su código. VS Code le permite editar archivos visualmente mientras ejecuta Claude Code en la terminal integrada, uno al lado del otro en la misma ventana.

## Conceptos Clave

- **VS Code** - Editor de código gratuito de Microsoft con una terminal integrada
- **Terminal Integrada** - Panel de terminal PowerShell dentro de VS Code, para que no tenga que cambiar de ventana para ejecutar Claude Code
- **Carpeta del espacio de trabajo** - La carpeta que abre en VS Code; Claude Code lee y edita los archivos dentro de ella

## Lo Que Necesitará

- Haber completado [Instalar Claude Code en Windows](./Install_CLAUDE_Code_Win)
- Haber completado [Primeros Pasos con VS Code](./VS_Code_Getting_Started)
- 10-15 minutos

## Paso 1: Cree una Carpeta de Proyecto

- Abra el **Explorador de archivos** (haga clic en el icono de carpeta en su barra de tareas)
- Navegue a **Documentos**
- Haga clic derecho en el espacio vacío, seleccione **New > Folder**
- Nombre la carpeta `test_claude`

## Paso 2: Inicie VS Code

- Haga clic en el **botón de Inicio de Windows** (el logotipo de Windows en su barra de tareas)
- Escriba `Visual Studio Code` o `VS Code` en el cuadro de búsqueda
- Haga clic en **Visual Studio Code** cuando aparezca en los resultados de búsqueda
- VS Code se abre con una pestaña de bienvenida - puede cerrar esta pestaña


## Paso 3: Abra la Carpeta en VS Code

- En VS Code, haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue a **Documentos** y seleccione la carpeta `test_claude`
- Haga clic en **Select Folder** y VS Code se recargará con su carpeta `test_claude`
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**


## Paso 4: Inicie Claude Code

- Después de que VS Code se recargue, abra una nueva terminal: haga clic en **Terminal** en la barra de menú, luego en **New Terminal**
- En el panel de la terminal, escriba:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el [tutorial de instalación](./Install_CLAUDE_Code_Win.md). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 5: Pruebe el Flujo de Trabajo

- En Claude Code, escriba:
```
Escribe un artículo breve explicando por qué a los LLMs les gusta usar el formato Markdown. Guárdalo como article.md
```
- Claude Code crea el archivo y verá aparecer `article.md` en el panel Explorer a la izquierda
- Haga clic en `article.md` en el Explorer para verlo en el editor
- Para previsualizar el artículo formateado: haga clic derecho dentro del editor de `article.md` y seleccione **Markdown Preview Enhanced: Open Preview to the Side** (la extensión de [Primeros Pasos con VS Code](./VS_Code_Getting_Started)). Si no tiene esa extensión, haga clic derecho en la pestaña `article.md` y seleccione **Open Preview** en su lugar
- Verá el Markdown renderizado con encabezados, viñetas y formato adecuados

## Reabrir Claude en VS Code Más Tarde

Después de cerrar VS Code, puede volver a su proyecto de estas formas:

- **Opción A:** Abra VS Code, haga clic en **File > Open Recent** y seleccione `test_claude`
- **Opción B:** Abra el **Explorador de archivos**, haga clic derecho en la carpeta `test_claude` y seleccione **Open with Code** (en Windows 11, haga clic primero en **Mostrar más opciones**). Esta opción solo aparece si se marcó **Add "Open with Code" action** al instalar VS Code; de lo contrario, use la Opción A

## Próximos Pasos

- Pida a Claude Code que explique una base de código existente: "Explica qué hace este proyecto"
- Haga que Claude Code le ayude a escribir nuevas funcionalidades: "Agrega una función que calcule el promedio de una lista"
- Use Claude Code para corregir errores: "Este código da un error, ¿puedes arreglarlo?"
- Pruebe la extensión de Claude Code para obtener un panel de chat visual con diferencias en línea. Ejecutar `claude` en la terminal de VS Code normalmente la instala por usted (si no, busque "Claude Code" en Extensions). Abra cualquier archivo y luego haga clic en el ícono Spark en la parte superior derecha del editor

## Solución de Problemas

- **`claude` no se reconoce** - Cierre VS Code por completo (todas las ventanas) y vuelva a abrirlo; luego abra una terminal nueva y pruebe `claude`. Si sigue fallando, ejecute `claude --version` en una ventana normal de PowerShell; si eso también falla, siga primero el [tutorial de instalación](./Install_CLAUDE_Code_Win.md)
- **¿Usa WSL?** - Si configuró la ruta opcional de WSL/Ubuntu, instale la extensión **WSL** desde la barra lateral Extensions, haga clic en el icono **><** de la esquina inferior izquierda y seleccione **Connect to WSL** antes de abrir la carpeta de su proyecto (accesible en `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude`)

## Resumen del Flujo de Trabajo

- **VS Code** se ejecuta en Windows y proporciona la interfaz del editor visual
- **Terminal Integrada** ejecuta Claude Code directamente dentro de VS Code
- Edite archivos en el editor, converse con Claude Code en la terminal: lo mejor de ambos mundos

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 10 de diciembre de 2025.
