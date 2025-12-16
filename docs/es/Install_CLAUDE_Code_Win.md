[Inicio](index.html)

# Instalar Claude Code en Windows Usando WSL

Claude Code es un potente asistente de codificación con IA, pero los usuarios de Windows enfrentan un desafío: muchas herramientas de desarrollo funcionan mejor en Linux. ¿La solución? WSL (Windows Subsystem for Linux) le permite ejecutar un entorno Linux completo dentro de Windows, como tener dos computadoras en una. Esta guía lo llevará a través de la configuración completa para que pueda comenzar a programar con Claude en aproximadamente 20 minutos.

## Conceptos Clave

- **WSL (Windows Subsystem for Linux)** - Característica de Windows que ejecuta un sistema Linux real junto con Windows
- **Ubuntu** - Distribución de Linux popular y amigable para principiantes que instalaremos a través de WSL
- **PowerShell** - Herramienta de línea de comandos integrada de Windows, usada aquí para instalar WSL
- **Node.js** - Entorno de ejecución de JavaScript que Claude Code requiere para funcionar
- **Terminal** - Interfaz basada en texto para ejecutar comandos (como la línea de comandos de Ubuntu)

## Lo Que Necesitará

- Computadora con Windows 10 (versión 2004 o superior) o Windows 11
- Acceso de administrador en su computadora
- Suscripción a Claude Pro/Max o clave API a través de Azure Foundry
- 15-20 minutos

## Paso 1: Verificar si la Virtualización está Habilitada

Antes de instalar WSL, necesita verificar que la virtualización esté habilitada en su computadora. Esto es necesario para que WSL funcione.

- **Haga clic derecho** en la barra de tareas (barra en la parte inferior de su pantalla)
- Haga clic en **Administrador de tareas**
- Si se abre en una ventana pequeña, haga clic en **Más detalles** en la parte inferior
- Haga clic en la pestaña **Rendimiento**
- Haga clic en **CPU** en la barra lateral izquierda
- Observe la sección inferior derecha de la ventana
- Encuentre la línea que dice **Virtualización:** y verifique si dice **Habilitado**

**Si dice "Habilitado":** ¡Excelente! Continúe con el Paso 2.

**Si dice "Deshabilitado":** Debe habilitar la virtualización en la configuración del BIOS de su computadora:
- Reinicie su computadora
- Durante el inicio, presione la tecla del BIOS (normalmente **F2**, **F10**, **Del** o **Esc**, depende del fabricante)
- Busque configuraciones relacionadas con "Virtualization Technology", "Intel VT-x", "AMD-V" o "SVM Mode"
- Habilite estas configuraciones
- Guarde y salga del BIOS (normalmente **F10**)
- Su computadora se reiniciará

## Paso 2: Abrir PowerShell como Administrador

- Haga clic en el **botón de Inicio de Windows** (ícono de Windows en la esquina inferior izquierda)
- Escriba `PowerShell` en el cuadro de búsqueda
- Verá **Windows PowerShell** en los resultados
- **Haga clic derecho** en **Windows PowerShell**
- Haga clic en **Ejecutar como administrador**
- Aparecerá una ventana preguntando "¿Desea permitir que esta aplicación haga cambios en su dispositivo?"
- Haga clic en **Sí**

Se abrirá una ventana azul con texto blanco - esto es PowerShell ejecutándose como administrador.

## Paso 3: Instalar WSL

**Primero, verifique si WSL y Ubuntu ya están instalados:**

- En la ventana de PowerShell, escriba:
   ```
   wsl --list --verbose
   ```
- Observe el resultado:
   - **Si ve "Ubuntu" listado** con un STATE de "Running" o "Stopped": ¡WSL y Ubuntu ya están instalados! Vaya directamente al Paso 4.
   - **Si ve un mensaje de error** o "Windows Subsystem for Linux has no installed distributions": Continúe con la instalación.

**Para instalar WSL y Ubuntu:**

- En la ventana de PowerShell, escriba:
   ```
   wsl --install
   ```
- Puede ver mensajes como "Installing: Windows Subsystem for Linux" e "Installing: Ubuntu"
- Cuando vea un mensaje indicando que la instalación está completa, necesita reiniciar su computadora:
   - Haga clic en el **botón de Inicio de Windows**
   - Haga clic en el **ícono de Energía**
   - Haga clic en **Reiniciar**
- Su computadora se reiniciará - esto toma aproximadamente 1-2 minutos

**Por qué es necesario reiniciar:** El reinicio permite que Windows habilite las características de WSL y Virtual Machine Platform que acaba de instalar.

**Nota:** Si obtiene un error indicando que no se reconoce el comando, su versión de Windows puede ser demasiado antigua. Asegúrese de tener Windows 10 versión 2004 o superior, o Windows 11. Ejecute Windows Update para obtener la última versión.

## Paso 4: Configurar Ubuntu (Solo la Primera Vez)

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
- Escriba una contraseña simple (incluso puede usar la misma que el nombre de usuario: `john`)
- No verá los caracteres mientras escribe: esto es normal
- Escriba la misma contraseña nuevamente cuando se le solicite

**Importante:** Recuerde este nombre de usuario y contraseña, los necesitará más adelante.

## Paso 5: Actualizar Ubuntu

- En la ventana de terminal de Ubuntu, escriba:
   ```
   sudo apt update
   ```
- Escriba su contraseña (la que acaba de crear) cuando se le solicite
- A continuación, escriba:
   ```
   sudo apt upgrade -y
   ```
- Espere a que se actualicen todos los paquetes (esto puede tomar 5 minutos)

## Paso 6: Instalar Node.js

Claude Code requiere Node.js versión 18 o superior. Siga estos pasos:

- En la terminal de Ubuntu, copie y pegue estos comandos:

   Primero, descargue el instalador de nvm:
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   cat install.sh | bash
   \. "$HOME/.nvm/nvm.sh"
   nvm install 24
   ```
   Esto descarga el instalador de nvm, lo instala y luego lo usa para instalar Node.js v24.0
- Espere a que se instale Node.js (2-5 minutos)
- Verifique la instalación escribiendo:
   ```
   node --version
   ```
- Debería ver algo como `v24.x.x` (los números exactos pueden variar)

## Paso 7: Instalar Claude Code

- En la terminal de Ubuntu, escriba:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Espere a que se instale Claude Code (2-5 minutos)
- Puede ver algunas advertencias en amarillo o rojo: esto es normal
- Cuando la instalación esté completa, verifíquela escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code

## Paso 8: Configurar su Conexión API de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En la terminal de Ubuntu, escriba:
   ```
   claude
   ```
- Claude intentará abrir un navegador. Si no puede abrirlo automáticamente, mantenga presionado **Ctrl** y haga clic en la URL larga. También puede copiar la URL y pegarla en un navegador.
- Inicie sesión en su cuenta de Claude.ai (esto puede ocurrir automáticamente si usa Chrome)
- Haga clic en **Authorize**
- Haga clic en **Copy Code** cuando aparezca un código largo
- Regrese a la ventana de terminal
- Para pegar: **Haga clic derecho** y seleccione **Paste** (o presione **Ctrl+Shift+V**)
- Debería ver un mensaje de éxito
- Siga las instrucciones para completar la configuración

### Opción B. Usar clave API de Anthropic

Si tiene una clave API de Anthropic en lugar de una suscripción a Claude:

- Primero, obtenga su clave API de la [Consola de Anthropic](https://console.anthropic.com/)
- En la terminal de Ubuntu, escriba:
   ```
   export ANTHROPIC_API_KEY="su-clave-api-aqui"
   ```
   Reemplace `su-clave-api-aqui` con su clave API real
- Para hacerlo permanente (no tener que configurarlo cada vez), agréguelo a su perfil de shell:
   ```
   echo 'export ANTHROPIC_API_KEY="su-clave-api-aqui"' >> ~/.bashrc
   ```
   Reemplace `su-clave-api-aqui` con su clave API real
- Cierre y vuelva a abrir la terminal de Ubuntu para que los cambios surtan efecto
- Ahora debería poder usar Claude Code con su clave API

### Opción C. Usar API de Anthropic a través de Azure Foundry

Antes de iniciar Claude Code, en la terminal de Ubuntu, pegue este código para definir las variables de entorno:
```
# Habilitar integración Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1
# Nombre del recurso Azure
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Configurar modelos según los nombres de implementación de su recurso
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=su_clave_api
```

**Nota:** Reemplace `xxxx-eastus2` con el nombre de su Recurso Foundry (no use la URL base completa). Reemplace `su_clave_api` con su clave API completa de su portal de Azure.

Luego inicie Claude Code:
```
claude
```

Ahora debería poder usar Claude Code con los modelos de Claude implementados en Azure.


## Paso 9: Probar Claude Code

¡Está todo listo! Para ver si funciona, haga una pregunta general como "Explica la computación cuántica"

## Paso 10: Acceder a sus Proyectos de Windows
- Si tiene una carpeta de Windows llamada `test_claude` con archivos de un proyecto, puede acceder a ella:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Reemplace `Username` con su nombre de usuario real de Windows
- Luego inicie Claude:
   ```
   claude
   ```
- Comience pidiéndole a Claude que explique la base de código
- Puede pedirle a Claude que haga cambios
- Pruebe su código en su IDE preferido

**Nota:** Claude opera dentro de una carpeta de proyecto. Guarda la configuración en esa carpeta. Es el espacio de trabajo de Claude.

## Próximos Pasos

- **Configurar VS Code**: Siga la guía [VS Code Getting Started](VS_Code_Getting_Started.md), luego conéctelo a Claude Code con [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win.md)
- **Aprender conceptos básicos de Git**: Agregue control de versiones a sus proyectos con [Claude Code Git on Windows](Claude_Code_Git_Windows.md)
- **Probar un proyecto**: Trabaje con [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code.md) para ver Claude Code en acción

## Solución de Problemas

### Cómo abrir la terminal de Ubuntu después de cerrarla
- Haga clic en el **botón de Inicio de Windows**, escriba `Ubuntu` y haga clic en la aplicación **Ubuntu** (ícono de círculo naranja)

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
Este error significa que la virtualización no está habilitada:
- Regrese al Paso 1 y verifique en el Administrador de tareas si la virtualización está habilitada
- Si está deshabilitada, debe habilitarla en el BIOS de su computadora (vea el Paso 1 para instrucciones)
- Después de habilitar la virtualización, reinicie su computadora e intente `wsl --install` nuevamente

### "wsl --install" no funciona
- Asegúrese de estar ejecutando PowerShell como Administrador
- Asegúrese de tener Windows 10 versión 2004+ o Windows 11
- Intente ejecutar: `wsl --update` primero, luego intente `wsl --install` nuevamente

### La ventana de Ubuntu no se abre después de reiniciar
- Haga clic en el Inicio de Windows
- Escriba `Ubuntu`
- Haga clic en la aplicación Ubuntu para iniciarla manualmente

### "sudo: apt: command not found"
- Su WSL puede no haberse instalado correctamente
- En PowerShell (como Administrador), escriba: `wsl --unregister Ubuntu`
- Luego ejecute `wsl --install` nuevamente

### La instalación de Node.js falla
- Asegúrese de haber ejecutado `sudo apt update` primero
- Intente el comando de instalación nuevamente

### Comandos de Claude Code no encontrados
- Asegúrese de que la instalación se completó exitosamente
- Intente cerrar y volver a abrir la terminal de Ubuntu
- Intente ejecutar el comando de instalación nuevamente: `curl -fsSL https://claude.ai/install.sh | bash`

## ¿Necesita Ayuda?

- Para problemas con WSL: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Para problemas con Claude Code: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
