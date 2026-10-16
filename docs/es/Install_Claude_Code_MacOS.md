---
title: "Instalar Claude Code en Mac"
lang: "es"
---
[Inicio](./)

# Instalar Claude Code en Mac

Claude Code es un asistente de IA que funciona en su Terminal y lo ayuda a escribir, depurar y comprender código. Piénselo como un compañero de programación experto disponible cuando lo necesite. Ya sea principiante o desarrollador experimentado, Claude Code puede acelerar su trabajo y ayudarlo a aprender.

Esta guía lo acompaña paso a paso durante la instalación, con instrucciones detalladas para principiantes.

## Descripción General

- Abrir Terminal
- Instalar Claude Code
- Configurar su conexión API
- Comenzar a usar Claude Code

## Conceptos Clave

- **Terminal**: Aplicación integrada de Mac donde escribe comandos en lugar de hacer clic en botones. Es la forma de interactuar con Claude Code.
- **Claude Code**: Asistente de programación con IA que se ejecuta en Terminal. Puede responder preguntas, escribir código y ayudarlo a comprender proyectos existentes.

## Lo Que Necesitará

- Computadora Mac (macOS 13.0 Ventura o posterior)
- Conexión a Internet
- Suscripción a Claude Pro/Max o clave API
- 5 - 10 minutos

## Paso 1: Abrir Terminal

- Presione **Command (⌘) + Space** para abrir la búsqueda de Spotlight
- Escriba `Terminal`
- Presione **Return** (o haga clic en **Terminal**, un ícono de cuadrado negro, en los resultados)
- Se abrirá una ventana de Terminal con un cursor parpadeante

**Consejo:** Mantenga Terminal abierto para los próximos pasos.

## Paso 2: Instalar Claude Code

En Terminal, copie y pegue este comando, luego presione **Return**:
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Espere a que Claude Code se instale (1-2 minutos)
- Es posible que la ventana no muestre ningún mensaje mientras descarga: esto es normal, solo espere
- Cuando se complete la instalación, cierre y vuelva a abrir Terminal, luego verifique escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code
- Si en su lugar ve `zsh: command not found: claude`, ejecute estas dos líneas (le indican a su Mac dónde encontrar Claude Code) y luego pruebe `claude --version` otra vez:
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

**Alternativa: Instalar con Homebrew**

Si usa Homebrew, puede instalar Claude Code con:
```
brew install --cask claude-code
```

**Consejo:** Ejecute `claude doctor` después de la instalación para verificar que todo esté configurado correctamente.

## Paso 3: Conectarse a Su Cuenta de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En Terminal, escriba:
   ```
   claude
   ```
- Claude intentará abrir un navegador. Si no se abre automáticamente, presione **c** para copiar el enlace de inicio de sesión y luego péguelo en su navegador.
- Inicie sesión en su cuenta de Claude.ai (esto puede ocurrir automáticamente)
- Haga clic en **Authorize**. El navegador debería indicar que ha iniciado sesión, y Terminal muestra un mensaje de éxito.
- Solo si el navegador muestra un código largo en su lugar, haga clic en **Copy Code**, regrese a Terminal, péguelo en **Paste code here if prompted** (presione **Command (⌘) + V**) y presione **Return**.
- Siga las instrucciones para completar la configuración

### Opción B. Usar la clave API de Anthropic

Si tiene una clave API de Anthropic en lugar de una suscripción a Claude:

- Primero, obtenga su clave API de la [Consola de Anthropic](https://console.anthropic.com/)
- En Terminal, escriba:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Reemplace `your-api-key-here` con su clave API real
- Para hacerlo permanente (no tener que configurarlo cada vez), agréguelo a su perfil de shell:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   Reemplace `your-api-key-here` con su clave API real
- Cierre y vuelva a abrir Terminal para que los cambios surtan efecto
- Inicie Claude Code escribiendo `claude`. La primera vez, le pregunta si desea usar la clave API que encontró. Elija **Yes**. (Si elige **No** por error, escriba `/config` y active **Use custom API key**.)

**Nota:** Si usa una Mac más antigua con bash en lugar de zsh, reemplace `~/.zshrc` con `~/.bash_profile` en el comando anterior.

### Opción C. Usar la API de OpenRouter (pago por uso)

OpenRouter es una pasarela de API unificada que proporciona acceso a más de 500 modelos de lenguaje de gran tamaño a través de una única clave API. Esta puede ser una forma económica de usar Claude Code, ya que solo paga por uso y puede elegir entre modelos de varios puntos de precio.

- Regístrese en [openrouter.ai](https://openrouter.ai) e inicie sesión
- Haga clic en **Get API key** y copie la clave en un lugar seguro
- Configure las variables de entorno requeridas antes de iniciar Claude Code:
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="~anthropic/claude-sonnet-latest"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="~anthropic/claude-opus-latest"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="~anthropic/claude-haiku-latest"
   ```
- Inicie Claude Code:
   ```
   claude
   ```
- Verifique la conexión escribiendo `/status` en Claude Code

**Notas:**
- Reemplace `your-openrouter-api-key` con su clave API real de OpenRouter
- `ANTHROPIC_API_KEY` debe establecerse explícitamente como vacío
- Para usar modelos alternativos, deben admitir **capacidades de uso de herramientas**. Puede anular modelos con:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Explore los modelos disponibles en [openrouter.ai/models](https://openrouter.ai/models)
- Los modelos gratuitos (`:free`) están limitados a 50 solicitudes por día, que una sola tarea de Claude Code puede agotar rápidamente
- Los modelos mostrados arriba son de pago: consulte sus precios en [openrouter.ai/models](https://openrouter.ai/models) antes de usarlos
- Solo se garantiza que Claude Code funcione con modelos de Anthropic a través de OpenRouter
- Consulte la [guía oficial de OpenRouter](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration) para más detalles


### Opción D. Usar la API de Anthropic a través de Microsoft Foundry (Azure)

Esta opción es para organizaciones que usan modelos Claude alojados en Azure. En la ventana de Terminal, pegue este código para definir variables de entorno (antes de iniciar Claude):
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Nota:** Reemplace `xxxx-eastus2` con el nombre de su Recurso Foundry (no use la URL base completa). Reemplace `your_api_key` con su clave API completa de su portal de Azure.

Luego inicie Claude Code escribiendo `claude`.

## Paso 4: Probar Claude Code

¡Ya está listo! Así se usa Claude Code:

- En Terminal, escriba:
   ```
   claude
   ```
- Le hará algunas preguntas antes de estar listo para conversar
- Para probar que funciona, haga una pregunta general como "Explain quantum computing."

## Paso 5: Navegar a Su Proyecto

- Si tiene un proyecto en las carpetas de su Mac, puede navegar a él:
   ```
   cd ~/Documents/test_claude
   ```
   Reemplace `test_claude` con el nombre real de su carpeta de proyecto

- Luego inicie Claude:
   ```
   claude
   ```
- Comience pidiéndole a Claude que explique la base de código.
- Puede pedirle a Claude que haga cambios.
- Pruebe su código en su IDE preferido.

**Nota:** Claude opera dentro de una carpeta de proyecto. Define permisos de escritura en la carpeta y guarda la configuración ahí. Es el espacio de trabajo de Claude.

## Paso 6: Actualizar Claude Code

Claude Code instalado mediante el instalador nativo se actualiza automáticamente en segundo plano. También puede activar una actualización manualmente:

- En Terminal, escriba:
   ```
   claude update
   ```
- Claude Code buscará actualizaciones e instalará la versión más reciente

**Nota:** No use `sudo` para ejecutar ni actualizar Claude Code: puede dejar archivos que pertenecen a root en su carpeta `~/.claude`, lo que provoca errores de permisos la próxima vez que ejecute Claude Code normalmente.

**Nota:** Las instalaciones de Homebrew no se actualizan automáticamente. Ejecute `brew upgrade claude-code` periódicamente para obtener la versión más reciente.

## Próximos Pasos
- [Primeros Pasos con VS Code](./VS_Code_Getting_Started.md) - Aprenda a usar VS Code, un editor de código popular
- [Claude Code en VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Ejecute Claude Code dentro de VS Code
- [Escribir un Trabajo de Investigación con Claude Code](./Writing_Research_Paper_Claude_Code.md) - Use Claude Code para escritura académica

## Cómo Abrir Terminal Nuevamente

Después de cerrar Terminal, así se abre de nuevo:

- Presione **Command (⌘) + Space** para abrir la búsqueda de Spotlight
- Escriba `Terminal`
- Presione **Return**
- Se abrirá una ventana de Terminal

## Solución de Problemas

### Primer paso: Ejecutar Claude Doctor
Si algo no funciona, ejecute este comando primero:
```
claude doctor
```
Verifica su instalación e informa cualquier problema.

### El script de instalación falla
- Asegúrese de tener macOS 13.0 o posterior
- Intente la alternativa con Homebrew: `brew install --cask claude-code`
- Verifique su conexión a Internet e intente nuevamente

### Comandos de Claude Code no encontrados
- Cierre Terminal completamente (haga clic en **Terminal** en la barra de menú, luego **Quit Terminal**)
- Abra Terminal nuevamente
- Intente `claude --version` para verificar si está instalado
- Si todavía dice `command not found`, ejecute estas dos líneas y luego pruebe `claude --version` otra vez:
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### La autenticación falla
- Asegúrese de tener una suscripción activa a Claude Pro/Max o una clave API válida
- Intente ejecutar `claude` nuevamente y complete el proceso de inicio de sesión
- Verifique que su navegador abrió la página de autorización correcta

## Consejos para Usuarios de Mac

### Encontrar Rutas de Proyectos
Para encontrar la ruta de una carpeta:
- Abra Finder
- Navegue a su carpeta de proyecto
- Arrastre y suelte la carpeta en Terminal: ¡la ruta completa aparecerá!

### Usar Diferentes Aplicaciones de Terminal
También puede usar otras aplicaciones de terminal:
- iTerm2 (alternativa popular con más funciones)
- Warp (terminal moderna con funciones de IA)
- Hyper (terminal multiplataforma)

¡Claude Code funciona con todas ellas!

## ¿Necesita Ayuda?

- Para problemas con Claude Code: [Claude Code GitHub](https://github.com/anthropics/claude-code)
- Para documentación oficial de configuración: [Guía de Configuración de Claude Code](https://code.claude.com/docs/en/setup)

---

*Última actualización: Febrero 2026*
