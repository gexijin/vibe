[Inicio](index.html)

# Instalar Claude Code en Windows

Claude Code es un asistente de IA que vive en su terminal y le ayuda a escribir, depurar y comprender código. Esta guía lo lleva a través de la configuración completa: una instalación nativa rápida a través de PowerShell, y luego WSL2 para la experiencia completa con Linux.

## Conceptos Clave

- **WSL (Windows Subsystem for Linux)** - Una característica de Windows que ejecuta un sistema Linux real junto con Windows
- **Ubuntu** - Una distribución de Linux popular y amigable para principiantes que puede instalar a través de WSL
- **PowerShell** - Herramienta de línea de comandos integrada de Windows, usada aquí para instalar Claude Code y WSL

## Lo Que Necesitará

- Una computadora con Windows 10 (versión 2004 o superior) o Windows 11
- Acceso de administrador en su computadora
- Suscripción a Claude Pro/Max o clave API a través de Azure Foundry
- 10 - 15 minutos

## Paso 1: Instalar Claude Code de Forma Nativa en Windows (funciona pero no recomendado)

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

> **Nota:** La instalación nativa en Windows tiene algunas limitaciones:
> - Sin sandboxing de la herramienta Bash (una característica de seguridad solo disponible en WSL2/macOS)
> - Algunas herramientas y flujos de trabajo funcionan mejor en un entorno Linux
>
> Continúe con los pasos siguientes para instalar WSL2 y obtener la experiencia completa.

## Paso 2: Verificar la Virtualización e Instalar WSL

**Primero, verifique si la virtualización está habilitada:**

- **Haga clic derecho** en la barra de tareas (la barra en la parte inferior de su pantalla)
- Haga clic en **Administrador de tareas** en el menú
- Si el Administrador de tareas se abre en una ventana pequeña, haga clic en **Más detalles** en la parte inferior
- Haga clic en la pestaña **Rendimiento** en la parte superior
- Haga clic en **CPU** en la barra lateral izquierda
- Observe la sección inferior derecha de la ventana
- Encuentre la línea que dice **Virtualización:** y verifique si dice **Habilitado**

**Si dice "Habilitado":** ¡Excelente! Continúe abajo.

**Si dice "Deshabilitado":** Necesita habilitar la virtualización en la configuración del BIOS de su computadora:
- Reinicie su computadora
- Durante el inicio, presione la tecla del BIOS (normalmente **F2**, **F10**, **Del** o **Esc**, depende del fabricante de su computadora)
- Busque configuraciones relacionadas con "Virtualization Technology", "Intel VT-x", "AMD-V" o "SVM Mode"
- Habilite estas configuraciones
- Guarde y salga del BIOS (normalmente **F10**)
- Su computadora se reiniciará normalmente

**Ahora instale WSL:**

- Haga clic en el **botón de Inicio de Windows**
- Escriba `PowerShell` en el cuadro de búsqueda
- **Haga clic derecho** en **Windows PowerShell** y haga clic en **Ejecutar como administrador**
- Haga clic en **Sí** cuando se le pregunte "¿Desea permitir que esta aplicación haga cambios en su dispositivo?"

**Verifique si WSL y Ubuntu ya están instalados:**

- En la ventana de PowerShell, escriba:
   ```
   wsl --list --verbose
   ```
- **Si ve "Ubuntu" listado:** ¡WSL ya está instalado! Vaya al Paso 3.
- **Si ve un mensaje de error:** Continúe con la instalación abajo.

**Para instalar WSL y Ubuntu:**

- En la ventana de PowerShell, escriba:
   ```
   wsl --install
   ```
- Puede ver mensajes como "Installing: Windows Subsystem for Linux" e "Installing: Ubuntu"
- Cuando la instalación esté completa, reinicie su computadora:
   - Haga clic en el **botón de Inicio de Windows** → **ícono de Energía** → **Reiniciar**
- Su computadora se reiniciará — esto toma aproximadamente 1-2 minutos

**Nota:** Si obtiene un error indicando que no se reconoce el comando, su versión de Windows puede ser demasiado antigua. Asegúrese de tener Windows 10 versión 2004 o superior, o Windows 11.

## Paso 3: Configurar Ubuntu

Después de que su computadora se reinicie, una ventana de terminal con "Ubuntu" en el título debería abrirse automáticamente en 2-5 minutos.

**Si la ventana de Ubuntu NO se abrió automáticamente:**
- Haga clic en el **botón de Inicio de Windows**
- Escriba `Ubuntu` en el cuadro de búsqueda
- Haga clic en **Ubuntu** (verá un ícono circular naranja)
- La terminal de Ubuntu se abrirá y continuará con la configuración

**Ahora complete la configuración inicial:**

- Espere el mensaje: `Enter new UNIX username:`
- Escriba un nombre de usuario (solo letras minúsculas y números, sin espacios)
   - Ejemplo: `john`
- Verá: `New password:`
- Escriba una contraseña simple (incluso la misma que el nombre de usuario `john`)
- No verá los caracteres mientras escribe — esto es normal
- Escriba la misma contraseña nuevamente cuando se le solicite

**Importante:** Recuerde este nombre de usuario y contraseña — los necesitará más adelante.

## Paso 4: Instalar Claude Code en WSL

- En la terminal de Ubuntu, escriba:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Espere a que se instale Claude Code
- Cuando la instalación esté completa, verifique escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code

## Paso 5: Conectarse a su Cuenta de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En la terminal de Ubuntu, escriba:
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

### Opción B. Usar clave API de Anthropic

Si tiene una clave API de Anthropic en lugar de una suscripción a Claude:

- Primero, obtenga su clave API de la [Consola de Anthropic](https://console.anthropic.com/)
- En la terminal de Ubuntu, escriba:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Reemplace `your-api-key-here` con su clave API real
- Para hacerlo permanente (para no tener que configurarlo cada vez), agréguelo a su perfil de shell:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   Reemplace `your-api-key-here` con su clave API real
- Cierre y vuelva a abrir la terminal de Ubuntu para que los cambios surtan efecto
- Ahora debería poder usar Claude Code con su clave API

### Opción C. Usar API de OpenRouter (¡comienza gratis!)

OpenRouter es una puerta de enlace API unificada que proporciona acceso a más de 500 modelos de lenguaje grandes a través de una sola clave API. Esta puede ser una forma económica de usar Claude Code, ya que solo paga por uso y puede elegir entre modelos de diferentes precios.

- Regístrese en [openrouter.ai](https://openrouter.ai) e inicie sesión
- Haga clic en **Get API key** y copie la clave en un lugar seguro
- Configure las variables de entorno requeridas antes de iniciar Claude Code:
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Inicie Claude Code:
   ```
   claude
   ```
- Verifique la conexión escribiendo `/status` en Claude Code

**Notas:**
- Reemplace `your-openrouter-api-key` con su clave API real de OpenRouter
- `ANTHROPIC_API_KEY` debe establecerse explícitamente como vacío
- Para usar modelos alternativos, deben soportar **capacidades de uso de herramientas**. Puede sobrescribir modelos con:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Explore los modelos disponibles en [openrouter.ai/models](https://openrouter.ai/models)
- El nivel gratuito le da 50 solicitudes API por día
- Consulte la [guía oficial de OpenRouter](https://openrouter.ai/docs/guides/claude-code-integration) para más detalles

### Opción D. Usar API de Anthropic a través de Azure Foundry

Antes de iniciar Claude Code, en la terminal de Ubuntu, pegue este código para definir las variables de entorno:
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Nota:** Reemplace `xxxx-eastus2` con el nombre de su Recurso Foundry (no use la URL base completa). Reemplace `your_api_key` con su clave API completa de su portal de Azure.

Luego inicie Claude Code:
```
claude
```

Ahora debería poder usar Claude Code con los modelos de Claude implementados en Azure.

## Paso 6: Probar Claude Code

¡Está todo listo! Escriba `claude` en la terminal de Ubuntu y haga una pregunta general como "Explica la computación cuántica."

## Paso 7: Acceder a sus Proyectos

**Windows nativo (PowerShell):**
- Si tiene una carpeta de proyecto, navegue hasta ella:
   ```
   cd ~/Documents/test_claude
   ```
- Luego inicie Claude:
   ```
   claude
   ```

**WSL (Ubuntu):**
- Si tiene una carpeta de Windows llamada `test_claude`, puede acceder a ella:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Reemplace `Username` con su nombre de usuario real de Windows.
- Luego inicie Claude:
   ```
   claude
   ```

- Comience pidiéndole a Claude que le explique la base de código.
- Puede pedirle a Claude que haga cambios.
- Pruebe su código en su IDE preferido.

**Nota:** Claude opera dentro de una carpeta de proyecto. Guarda la configuración en esa carpeta. Es el espacio de trabajo de Claude.

## Paso 8: Actualizar Claude Code

Claude Code se actualiza automáticamente, pero puede actualizarlo manualmente en cualquier momento:

**WSL (Ubuntu):**
```
sudo claude update
```

**Windows nativo (PowerShell — ejecutar como administrador):**
```
claude update
```

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
- Regrese al Paso 2 y verifique en el Administrador de tareas si la virtualización está habilitada
- Si está deshabilitada, necesita habilitarla en el BIOS de su computadora (vea el Paso 2 para instrucciones)
- Después de habilitar la virtualización, reinicie su computadora e intente `wsl --install` nuevamente

### "wsl --install" no funciona
- Asegúrese de estar ejecutando PowerShell como Administrador
- Asegúrese de tener Windows 10 versión 2004+ o Windows 11
- Intente ejecutar: `wsl --update` primero, luego intente `wsl --install` nuevamente

### La ventana de Ubuntu no se abre después de reiniciar
- Haga clic en el Inicio de Windows
- Escriba `Ubuntu`
- Haga clic en la aplicación Ubuntu para iniciarla manualmente

### Cómo abrir la terminal de Ubuntu después de cerrarla
- Haga clic en el **botón de Inicio de Windows**, escriba `Ubuntu` y haga clic en la aplicación **Ubuntu** (ícono de círculo naranja)

### Comandos de Claude Code no encontrados (WSL)
- Asegúrese de que la instalación se completó exitosamente
- Intente cerrar y volver a abrir la terminal de Ubuntu
- Intente ejecutar el comando de instalación nuevamente: `curl -fsSL https://claude.ai/install.sh | bash`

## ¿Necesita Ayuda?

- Para problemas con WSL: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Para problemas con Claude Code: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2025. Actualizado en febrero de 2026.
