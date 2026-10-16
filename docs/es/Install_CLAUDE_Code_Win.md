---
title: "Instalar Claude Code en Windows"
lang: "es"
---
[Inicio](index.html)

# Instalar Claude Code en Windows

Claude Code es un asistente de IA que vive en su terminal y le ayuda a escribir, depurar y comprender código. Con esta guía tendrá Claude Code funcionando de forma nativa en Windows en cuestión de minutos. Al final encontrará también WSL2, una configuración opcional más avanzada.

## Conceptos Clave

- **PowerShell** - Herramienta de línea de comandos integrada de Windows, usada aquí para instalar y ejecutar Claude Code
- **Git for Windows** - Una descarga gratuita que agrega **Git Bash**, el shell que Claude Code usa para ejecutar comandos
- **WSL (Windows Subsystem for Linux)** - Una función opcional de Windows que ejecuta un sistema Linux real junto a Windows; se usa en la configuración avanzada del final

## Lo Que Necesitará

- Una computadora con Windows 10 o Windows 11
- Suscripción a Claude Pro/Max, o una clave API
- 5 - 10 minutos

## Paso 1: Instalar Git for Windows (opcional, recomendado)

Git for Windows es **recomendado, pero opcional**. Agrega **Git Bash**, el shell que Claude Code usa para ejecutar comandos. Si omite este paso, Claude Code usará PowerShell en su lugar, así que puede pasar directamente al Paso 2 e instalar Git más adelante si lo prefiere.

- Vaya a [git-scm.com/download/win](https://git-scm.com/download/win)
- Haga clic en **Click here to download** en la parte superior de la página y luego abra el instalador cuando termine
- Haga clic en **Next** para avanzar por el instalador, aceptando las opciones predeterminadas
- Haga clic en **Install**, luego en **Finish**

Eso es todo — Claude Code detectará Git Bash automáticamente al iniciarse.

## Paso 2: Instalar Claude Code

- Haga clic en el **botón de Inicio de Windows**
- Escriba `PowerShell` y haga clic en **Windows PowerShell**
- En la ventana de PowerShell, escriba:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Espere a que se complete la instalación (es posible que la ventana no muestre nada durante un minuto mientras descarga; esto es normal)
- Cierre y vuelva a abrir PowerShell, luego verifique escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code
- Si en su lugar ve `'claude' is not recognized`, ejecute estas dos líneas en PowerShell, luego cierre y vuelva a abrir PowerShell y pruebe `claude --version` otra vez:
   ```
   $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
   [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
   ```

## Paso 3: (Opcional) Abrir Claude Code en VS Code

Omita este paso si todavía no tiene VS Code: puede instalarlo más adelante con [Primeros Pasos con VS Code](VS_Code_Getting_Started.md) y volver aquí.

Ahora que Claude Code está instalado, puede usarlo dentro de VS Code y no solo en la terminal. Esta suele ser la forma más sencilla de trabajar, porque puede leer archivos, editar código y pedir ayuda sin salir de su editor.

Piense en la barra lateral de Claude Code como una ventana de chat dentro de VS Code. Le permite hacer preguntas, pedir explicaciones sobre el código y obtener ayuda mientras trabaja en la misma pantalla.

### Cómo abrir la barra lateral de Claude Code

1. Abra VS Code
2. Mire el extremo izquierdo de la ventana
3. Haga clic en el icono **Extensions** si todavía no ve el panel de Claude Code
4. Busque Claude Code en el marketplace de extensiones
5. Haga clic en **Install** si todavía no está instalada
6. Después de la instalación, busque el icono Spark de Claude Code en la barra lateral izquierda, o haga clic en **✻ Claude Code** en la esquina inferior derecha de la ventana

Si no ve el icono de Claude Code, pruebe lo siguiente:

1. Presione **Ctrl + Shift + P**
2. Escriba: Claude Code: Open in Side Bar
3. Haga clic en la opción correspondiente de la lista

Si aún no aparece, cierre VS Code y vuelva a abrirlo. A veces la extensión necesita reiniciarse antes de que aparezca la barra lateral.

### Para qué sirve la barra lateral

En la barra lateral de Claude Code puede:

- hacer preguntas sobre su proyecto
- obtener ayuda para corregir errores
- pedir explicaciones sobre código que no entiende
- crear o actualizar archivos
- trabajar de forma más visual sin salir de VS Code

Esto es útil porque puede mantener su código abierto en el editor y pedirle ayuda a Claude en la misma ventana.

### Prueba rápida

Cuando se abra la barra lateral:

- escriba: Explícame este proyecto
- presione **Enter**

Si Claude responde, ya está listo para usarlo. La primera vez, es posible que la barra lateral le pida iniciar sesión: siga sus indicaciones, o conecte su cuenta en el Paso 4 más abajo y vuelva a intentarlo.

> Consejo: Si la barra lateral sigue sin aparecer, asegúrese de que la extensión Claude Code esté instalada y de que VS Code se haya reiniciado.

## Paso 4: Conectarse a Su Cuenta de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En la ventana de PowerShell, escriba:
   ```
   claude
   ```
- Claude intentará abrir un navegador. Si no puede abrirlo automáticamente, presione **c** para copiar el enlace de inicio de sesión y luego péguelo en su navegador.
- Inicie sesión en su cuenta de Claude.ai (esto puede ocurrir automáticamente si usa Chrome)
- Haga clic en **Authorize**. El navegador debería indicar que ha iniciado sesión, y PowerShell muestra un mensaje de éxito.
- Solo si el navegador muestra un código largo en su lugar (esto ocurre en WSL/Ubuntu), haga clic en **Copy Code**, regrese a la terminal, péguelo en **Paste code here if prompted** (**clic derecho** o presione **Ctrl+V**) y presione **Enter**.
- Siga las instrucciones para completar la configuración

Las opciones basadas en API de abajo se configuran desde **PowerShell** con el comando `setx`, que guarda los ajustes de forma permanente. Tras ejecutar `setx`, **cierre y vuelva a abrir PowerShell** para aplicar el cambio y luego inicie `claude`.

### Opción B. Usar clave API de Anthropic

Si tiene una clave API de Anthropic en lugar de una suscripción a Claude:

- Obtenga su clave API de la [Consola de Anthropic](https://console.anthropic.com/)
- En PowerShell, escriba:
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   Reemplace `your-api-key-here` con su clave API real
- Cierre y vuelva a abrir PowerShell para que el cambio surta efecto
- Inicie Claude Code:
   ```
   claude
   ```
- La primera vez, Claude Code le pregunta si desea usar la clave API que encontró. Elija **Yes**. (Si elige **No** por error, escriba `/config` y active **Use custom API key**.)

### Opción C. Usar API de OpenRouter (pago por uso)

OpenRouter es una puerta de enlace de API unificada que da acceso a más de 500 grandes modelos de lenguaje con una sola clave API. Puede ser una forma económica de usar Claude Code, ya que solo paga por lo que usa y puede elegir entre modelos de distintos precios.

- Regístrese en [openrouter.ai](https://openrouter.ai) e inicie sesión
- Haga clic en **Get API key** y copie la clave en un lugar seguro
- En PowerShell, configure las variables de entorno requeridas:
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   [Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', $null, 'User')
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "~anthropic/claude-sonnet-latest"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "~anthropic/claude-opus-latest"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "~anthropic/claude-haiku-latest"
   ```
- Cierre y vuelva a abrir PowerShell, luego inicie Claude Code:
   ```
   claude
   ```
- Verifique la conexión escribiendo `/status` en Claude Code

**Notas:**
- Reemplace `your-openrouter-api-key` con su clave API real de OpenRouter
- La línea de `ANTHROPIC_API_KEY` elimina cualquier clave API de Anthropic guardada, que no debe estar configurada cuando usa OpenRouter
- Para usar modelos alternativos, deben soportar **capacidades de uso de herramientas**. Puede sobrescribir modelos con:
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- Explore los modelos disponibles en [openrouter.ai/models](https://openrouter.ai/models)
- Los modelos gratuitos (`:free`) están limitados a 50 solicitudes por día, que una sola tarea de Claude Code puede agotar rápidamente
- Los modelos mostrados arriba son de pago: consulte sus precios en [openrouter.ai/models](https://openrouter.ai/models) antes de usarlos
- Solo se garantiza que Claude Code funcione con modelos de Anthropic a través de OpenRouter
- Consulte la [guía oficial de OpenRouter](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration) para más detalles

### Opción D. Usar API de Anthropic a través de Microsoft Foundry (Azure)

En PowerShell, pegue este código para definir las variables de entorno:
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-8"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**Nota:** Reemplace `xxxx-eastus2` con el nombre de su Recurso Foundry (no use la URL base completa). Reemplace `your_api_key` con su clave API completa de su portal de Azure.

Luego cierre y vuelva a abrir PowerShell, e inicie Claude Code:
```
claude
```

Ahora debería poder usar Claude Code con los modelos de Claude implementados en Azure.

## Paso 5: Probar Claude Code

¡Está todo listo! Escriba `claude` en PowerShell y haga una pregunta general como "Explica la computación cuántica."

## Paso 6: Acceder a sus Proyectos

- Si tiene una carpeta de proyecto, navegue hasta ella en PowerShell:
   ```
   cd ~/Documents/test_claude
   ```
   Reemplace `test_claude` con el nombre real de su carpeta de proyecto. Consejo: escriba `cd ` (con un espacio), arrastre la carpeta desde el Explorador de archivos a la ventana de PowerShell para pegar su ruta completa y presione **Enter**.
- Luego inicie Claude:
   ```
   claude
   ```
- Comience pidiéndole a Claude que le explique la base de código.
- Puede pedirle a Claude que haga cambios.
- Pruebe su código en su IDE preferido.

**Nota:** Claude opera dentro de una carpeta de proyecto y guarda ahí su configuración. Es su espacio de trabajo.

## Paso 7: (Opcional) Instalar WSL2 para la Experiencia Completa con Linux

Para la mayoría de las personas, la configuración nativa anterior es más que suficiente. Aun así, algunas funciones solo están disponibles en Linux. WSL2 ejecuta un sistema Linux real dentro de Windows y añade el **sandboxing de la herramienta Bash** (una función de seguridad), además de una mejor compatibilidad con las herramientas de Linux. Configurarlo lleva más tiempo y obliga a reiniciar, así que hágalo solo si quiere la experiencia completa con Linux.

### a) Verificar la virtualización e instalar WSL

**Primero, verifique si la virtualización está habilitada:**

- **Haga clic derecho** en la barra de tareas (la barra en la parte inferior de su pantalla)
- Haga clic en **Administrador de tareas** en el menú
- Si el Administrador de tareas se abre en una ventana pequeña, haga clic en **Más detalles** en la parte inferior
- Haga clic en **Rendimiento** (una pestaña en la parte superior en Windows 10, o un icono en el menú de la izquierda en Windows 11)
- Haga clic en **CPU** en la barra lateral izquierda
- Encuentre la línea que dice **Virtualización:** y verifique si dice **Habilitado**

**Si dice "Deshabilitado":** Debe habilitar la virtualización en el BIOS de su computadora:
- Reinicie su computadora
- Durante el inicio, presione la tecla del BIOS (normalmente **F2**, **F10**, **Del** o **Esc**, según el fabricante)
- Busque configuraciones relacionadas con "Virtualization Technology", "Intel VT-x", "AMD-V" o "SVM Mode"
- Habilite estas configuraciones
- Guarde y salga del BIOS (normalmente **F10**)

**Ahora instale WSL:**

- Haga clic en el **botón de Inicio de Windows**, escriba `PowerShell`
- **Haga clic derecho** en **Windows PowerShell** y haga clic en **Ejecutar como administrador**
- Haga clic en **Sí** cuando se le pregunte "¿Desea permitir que esta aplicación haga cambios en su dispositivo?"
- En la ventana de PowerShell, escriba:
   ```
   wsl --install
   ```
- Puede ver mensajes como "Installing: Windows Subsystem for Linux" e "Installing: Ubuntu"
- Cuando la instalación esté completa, reinicie su computadora

**Nota:** `wsl --install` requiere Windows 10 versión 2004 o superior, o Windows 11. Si el comando no se reconoce, su versión de Windows puede ser demasiado antigua.

### b) Configurar Ubuntu

Después de que su computadora se reinicie, una ventana de terminal con "Ubuntu" en el título debería abrirse automáticamente en 2-5 minutos. Si no lo hace, haga clic en el **botón de Inicio de Windows**, escriba `Ubuntu` y haga clic en la aplicación **Ubuntu** (ícono de círculo naranja).

- Espere el mensaje: `Enter new UNIX username:`
- Escriba un nombre de usuario (solo letras minúsculas y números, sin espacios) — por ejemplo `john`
- Verá: `New password:`
- Escriba una contraseña simple (no verá los caracteres mientras escribe — esto es normal)
- Escriba la misma contraseña nuevamente cuando se le solicite

**Importante:** Recuerde este nombre de usuario y contraseña — los necesitará más adelante.

### c) Instalar Claude Code en WSL

- En la terminal de Ubuntu, escriba:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Cierre la ventana de Ubuntu, abra **Ubuntu** de nuevo desde el menú Inicio y luego verifique escribiendo:
   ```
   claude --version
   ```
- Si todavía ve `command not found`, ejecute esta línea y luego pruebe `claude --version` otra vez:
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
   ```
- Conecte su cuenta escribiendo `claude` en la terminal de Ubuntu y siguiendo el inicio de sesión en el navegador (igual que el Paso 4, Opción A). Si usa una clave API en su lugar, guárdela con `echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc && source ~/.bashrc` (WSL usa comandos de Linux, no `setx`)
- Para abrir una carpeta de proyecto de Windows desde WSL:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Reemplace `Username` con su nombre de usuario real de Windows.

## Próximos Pasos

- **Configurar VS Code**: Siga la guía [Primeros Pasos con VS Code](VS_Code_Getting_Started), luego conéctelo a Claude Code con [Configure VS Code para Claude Code en Windows](Claude_Code_in_VS_Code_Win)
- **Aprender conceptos básicos de Git**: Agregue control de versiones a sus proyectos con [Claude Code con control de versiones para Windows](Claude_Code_Git_Windows)
- **Probar un proyecto**: Trabaje con [Escribir Artículos de Investigación con Claude Code](Writing_Research_Paper_Claude_Code) para ver Claude Code en acción

## Solución de Problemas

### Primer paso: Ejecutar Claude Doctor

Si algo no funciona, intente ejecutar este comando primero:
```
claude doctor
```
Esta herramienta de diagnóstico integrada verifica su instalación y reporta problemas comunes.

### Comando claude no encontrado (Windows nativo)

- Cierre y vuelva a abrir PowerShell
- Intente ejecutar el comando de instalación nuevamente:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Si ve `'claude' is not recognized`, ejecute estas dos líneas en PowerShell y luego cierre y vuelva a abrir PowerShell:
   ```
   $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
   [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
   ```

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
Este error significa que la virtualización no está habilitada:
- Verifique en el Administrador de tareas si la virtualización está habilitada (vea la sección opcional de WSL arriba)
- Si está deshabilitada, habilítela en el BIOS de su computadora
- Después de habilitar la virtualización, reinicie su computadora e intente `wsl --install` nuevamente

### "wsl --install" no funciona
- Asegúrese de estar ejecutando PowerShell como Administrador
- Asegúrese de tener Windows 10 versión 2004+ o Windows 11
- Ejecute `wsl --update` primero y luego `wsl --install` de nuevo

### La ventana de Ubuntu no se abre después de reiniciar
- Haga clic en el **botón de Inicio de Windows**, escriba `Ubuntu` y haga clic en la aplicación **Ubuntu** para iniciarla manualmente

## ¿Necesita Ayuda?

- Para problemas con WSL: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Para problemas con Claude Code: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2025. Actualizado en junio de 2026.
