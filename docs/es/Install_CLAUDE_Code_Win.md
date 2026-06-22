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
- La descarga debería comenzar automáticamente — abra el instalador cuando termine
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
- Espere a que se complete la instalación
- Cierre y vuelva a abrir PowerShell, luego verifique escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code

## Paso 3: Conectarse a Su Cuenta de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En la ventana de PowerShell, escriba:
   ```
   claude
   ```
- Claude intentará abrir un navegador. Si no puede abrirlo automáticamente, mantenga presionado **Ctrl** y haga clic en la URL larga para abrirla en un navegador. Alternativamente, copie la URL y péguela en un navegador externo.
- Inicie sesión en su cuenta de Claude.ai (esto puede ocurrir automáticamente si usa Chrome)
- Haga clic en **Authorize**
- Haga clic en **Copy Code** cuando aparezca un código largo
- Regrese a la ventana de terminal
- Para pegar en la terminal: **Haga clic derecho** y seleccione **Paste** (o presione **Ctrl+Shift+V**)
- Debería ver un mensaje de éxito
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

### Opción C. Usar API de OpenRouter (¡comienza gratis!)

OpenRouter es una puerta de enlace de API unificada que da acceso a más de 500 grandes modelos de lenguaje con una sola clave API. Puede ser una forma económica de usar Claude Code, ya que solo paga por lo que usa y puede elegir entre modelos de distintos precios.

- Regístrese en [openrouter.ai](https://openrouter.ai) e inicie sesión
- Haga clic en **Get API key** y copie la clave en un lugar seguro
- En PowerShell, configure las variables de entorno requeridas:
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- Cierre y vuelva a abrir PowerShell, luego inicie Claude Code:
   ```
   claude
   ```
- Verifique la conexión escribiendo `/status` en Claude Code

**Notas:**
- Reemplace `your-openrouter-api-key` con su clave API real de OpenRouter
- `ANTHROPIC_API_KEY` debe establecerse explícitamente como vacío
- Para usar modelos alternativos, deben soportar **capacidades de uso de herramientas**. Puede sobrescribir modelos con:
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- Explore los modelos disponibles en [openrouter.ai/models](https://openrouter.ai/models)
- El nivel gratuito le da 50 solicitudes API por día
- Consulte la [guía oficial de OpenRouter](https://openrouter.ai/docs/guides/claude-code-integration) para más detalles

### Opción D. Usar API de Anthropic a través de Azure Foundry

En PowerShell, pegue este código para definir las variables de entorno:
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**Nota:** Reemplace `xxxx-eastus2` con el nombre de su Recurso Foundry (no use la URL base completa). Reemplace `your_api_key` con su clave API completa de su portal de Azure.

Luego cierre y vuelva a abrir PowerShell, e inicie Claude Code:
```
claude
```

Ahora debería poder usar Claude Code con los modelos de Claude implementados en Azure.

## Paso 4: Probar Claude Code

¡Está todo listo! Escriba `claude` en PowerShell y haga una pregunta general como "Explica la computación cuántica."

## Paso 5: Acceder a sus Proyectos

- Si tiene una carpeta de proyecto, navegue hasta ella en PowerShell:
   ```
   cd ~/Documents/test_claude
   ```
- Luego inicie Claude:
   ```
   claude
   ```
- Comience pidiéndole a Claude que le explique la base de código.
- Puede pedirle a Claude que haga cambios.
- Pruebe su código en su IDE preferido.

**Nota:** Claude opera dentro de una carpeta de proyecto y guarda ahí su configuración. Es su espacio de trabajo.

## Paso 6: (Opcional) Instalar WSL2 para la Experiencia Completa con Linux

Para la mayoría de las personas, la configuración nativa anterior es más que suficiente. Aun así, Claude Code funciona mejor en Linux. WSL2 ejecuta un sistema Linux real dentro de Windows y añade el **sandboxing de la herramienta Bash** (una función de seguridad), además de una mejor compatibilidad con las herramientas de Linux. Configurarlo lleva más tiempo y obliga a reiniciar, así que hágalo solo si quiere la experiencia completa con Linux.

### a) Verificar la virtualización e instalar WSL

**Primero, verifique si la virtualización está habilitada:**

- **Haga clic derecho** en la barra de tareas (la barra en la parte inferior de su pantalla)
- Haga clic en **Administrador de tareas** en el menú
- Si el Administrador de tareas se abre en una ventana pequeña, haga clic en **Más detalles** en la parte inferior
- Haga clic en la pestaña **Rendimiento** en la parte superior
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
- Verifique escribiendo:
   ```
   claude --version
   ```
- Conecte su cuenta escribiendo `claude` en la terminal de Ubuntu y siguiendo el inicio de sesión en el navegador (igual que el Paso 3, Opción A). Si usa una clave API en su lugar, configúrela con `export ANTHROPIC_API_KEY="your-api-key-here"` (WSL usa comandos de Linux, no `setx`)
- Para abrir una carpeta de proyecto de Windows desde WSL:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Reemplace `Username` con su nombre de usuario real de Windows.

## Próximos Pasos

- **Configurar VS Code**: Siga la guía [VS Code Getting Started](VS_Code_Getting_Started), luego conéctelo a Claude Code con [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Aprender conceptos básicos de Git**: Agregue control de versiones a sus proyectos con [Claude Code Git on Windows](Claude_Code_Git_Windows)
- **Probar un proyecto**: Trabaje con [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) para ver Claude Code en acción

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
- Asegúrese de que su PATH incluya el directorio de instalación de Claude

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
