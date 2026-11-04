---
title: "Use Claude Code desde VS Code en Mac"
lang: "es"
---
[Inicio](index.html)

# Use Claude Code desde VS Code en Mac

Ya instaló Claude Code en su Mac, ahora necesita un editor visual para trabajar con su código. VS Code le permite editar archivos visualmente mientras ejecuta Claude Code en la terminal integrada. Es como tener su editor de código y asistente de IA lado a lado en una sola ventana.

## Conceptos Clave

- **VS Code** - Editor de código gratuito de Microsoft para Mac
- **Terminal Integrada** - Panel de terminal dentro de VS Code donde ejecuta Claude Code
- **Panel Explorer** - Navegador de archivos en el lado izquierdo de VS Code

## Lo Que Necesitará

- Haber completado [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS)
- Haber completado [Primeros Pasos con VS Code](./VS_Code_Getting_Started)
- 10-15 minutos

## Paso 1: Inicie VS Code

- Abra **Finder** y vaya a **Aplicaciones**
- Encuentre **Visual Studio Code** y haga doble clic en él
- Si ve una advertencia de que "Visual Studio Code" es una app descargada de Internet, haga clic en **Abrir** (Open)
- VS Code se abre con una pestaña de bienvenida - puede cerrar esta pestaña

**Consejo:** Haga clic derecho en VS Code en el Dock y seleccione **Opciones > Mantener en el Dock** para un acceso fácil más adelante.

## Paso 2: Cree una Carpeta de Proyecto

- Abra **Finder**
- Haga clic en **Documentos** en la barra lateral izquierda
- Haga clic en **File** en la barra de menú, luego en **New Folder**
- Nombre la carpeta `test_claude`

## Paso 3: Abra la Carpeta en VS Code

- En VS Code, haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue a **Documentos** y seleccione la carpeta `test_claude` que creó
- Haga clic en **Open**
- Si se le pregunta "Do you trust the authors of the files in this folder?", haga clic en **Yes, I trust the authors**

Ahora debería ver `TEST_CLAUDE` en el panel Explorer del lado izquierdo.

## Paso 4: Inicie Claude Code e Inicie Sesión

- Abra una nueva terminal: haga clic en **Terminal** en la barra de menú, luego en **New Terminal**
- Aparece un panel de terminal en la parte inferior de VS Code
- En la terminal, escriba:
  ```
  claude
  ```
- Si Claude Code le pide que inicie sesión, siga los pasos de inicio de sesión del [tutorial de instalación](./Install_Claude_Code_MacOS). Claude Code requiere un plan de pago de Claude (como Pro o Max) o una cuenta de Anthropic Console; el plan gratuito no lo incluye.
- Verá un mensaje de bienvenida y el prompt de Claude Code
- Ahora puede usar Claude Code mientras edita archivos en VS Code

**Nota:** Solo necesita iniciar sesión una vez: en las próximas sesiones pasará directamente al mensaje de bienvenida.

## Paso 5: Pruebe el Flujo de Trabajo

- En Claude Code, escriba:
```
Escribe un artículo breve explicando por qué a los LLMs les gusta usar el formato Markdown. Guárdalo como article.md
```
- Claude Code crea el archivo y verá que `article.md` aparece en el panel Explorer a la izquierda
- Haga clic en `article.md` en el Explorer para verlo en el editor
- Para previsualizar el artículo formateado: haga clic derecho dentro del editor de `article.md` y seleccione **Markdown Preview Enhanced: Open Preview to the Side** (la extensión de [Primeros Pasos con VS Code](./VS_Code_Getting_Started)). Si no tiene esa extensión, haga clic derecho en la pestaña `article.md` y seleccione **Open Preview** en su lugar
- Verá el Markdown renderizado con encabezados, viñetas y formato apropiados

## Reabrir Claude en VS Code Más Tarde

Después de cerrar VS Code, puede volver a su proyecto de estas formas:

- **Opción A:** Abra VS Code, haga clic en **File > Open Recent**, y seleccione `test_claude`
- **Opción B:** Abra Terminal, navegue a su proyecto con `cd ~/Documents/test_claude`, y escriba `code .`

VS Code recuerda sus carpetas recientes, por lo que la Opción A con Open Recent suele ser la más rápida.

## Próximos Pasos

- Pida a Claude Code que explique una base de código existente: "Explica qué hace este proyecto"
- Haga que Claude Code le ayude a escribir nuevas funcionalidades: "Agrega una función que calcule el promedio de una lista"
- Use Claude Code para corregir errores: "Este código da un error, ¿puedes arreglarlo?"
- Pruebe la extensión de Claude Code para obtener un panel de chat visual con diffs en línea. Ejecutar `claude` en la terminal de VS Code normalmente la instala por usted (si no, busque "Claude Code" en Extensions). Abra cualquier archivo y luego haga clic en el ícono Spark en la parte superior derecha del editor

## Solución de Problemas

- **La terminal muestra "zsh" pero Claude Code no se inicia** - Asegúrese de que Claude Code esté instalado correctamente; ejecute `claude --version` para verificar
- **Comando "code" no encontrado en Terminal** - En VS Code, haga clic en **View** en la barra de menú, luego en **Command Palette**, escriba "shell command", y seleccione **Shell Command: Install 'code' command in PATH**
- **VS Code no se abre porque es de un desarrollador no identificado** - Vaya a **Ajustes del Sistema > Privacidad y seguridad** y haga clic en **Abrir igualmente** (Open Anyway)

## Resumen del Flujo de Trabajo

- **VS Code** proporciona la interfaz del editor visual
- **Terminal Integrada** ejecuta Claude Code dentro de VS Code
- Sus archivos permanecen en su carpeta Documents (o donde elija)
- Edite archivos en el editor, converse con Claude Code en la terminal: lo mejor de ambos mundos

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 10 de diciembre de 2025.
