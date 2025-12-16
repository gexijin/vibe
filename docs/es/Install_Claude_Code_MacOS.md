[Inicio](index.html)

# Instalar Claude Code en Mac

Claude Code es un asistente de IA que funciona en su Terminal y lo ayuda a escribir, depurar y comprender código. Piénselo como un compañero de programación experto disponible cuando lo necesite. Ya sea principiante o desarrollador experimentado, Claude Code puede acelerar su trabajo y ayudarlo a aprender.

Esta guía lo acompaña paso a paso durante la instalación, con instrucciones detalladas para principiantes.

## Descripción General

- Descargue e instale Node.js
- Instale Claude Code usando npm
- Configure su clave API
- Comience a usar Claude Code

## Conceptos Clave

- **Terminal**: Aplicación integrada de Mac donde escribe comandos en lugar de hacer clic en botones. Es la forma de interactuar con Claude Code.
- **Node.js**: Software que Claude Code necesita para funcionar. Es como el motor que impulsa Claude Code.
- **Claude Code**: Asistente de programación con IA que se ejecuta en Terminal. Puede responder preguntas, escribir código y ayudarlo a comprender proyectos existentes.

## Lo Que Necesitará

- Computadora Mac (macOS 10.15 Catalina o posterior recomendado)
- Conexión a Internet
- Acceso de administrador en su computadora
- Suscripción a Claude Pro/Max o clave API
- 15-20 minutos

## Paso 1: Descargar Node.js

Claude Code requiere Node.js versión 18 o superior.

**Primero, verifique si Node.js ya está instalado:**

- Haga clic en el icono **Launchpad** en su Dock (el icono con cuadrados de colores)
- Escriba `Terminal` en el cuadro de búsqueda en la parte superior
- Haga clic en **Terminal** (un icono de cuadrado negro)
- En Terminal, escriba:
   ```
   node --version
   ```
- Observe el resultado:
   - **Si ve un número de versión como `v18.x.x` o superior**: ¡Node.js ya está instalado! Vaya al Paso 4.
   - **Si ve "command not found"**: Continúe con la instalación.

**Para descargar Node.js:**

- Abra su navegador web (Safari, Chrome, Firefox, etc.)
- Vaya a:
   ```
   https://nodejs.org/
   ```
- Haga clic en el botón verde **Get Node.js**
- Haga clic en el botón verde **macOS Installer (.pkg)** en el centro de la pantalla
- Se descargará un archivo en su carpeta Descargas (normalmente tarda 30-60 segundos)
   - El archivo se llamará algo como `node-v24.x.x.pkg`

## Paso 2: Instalar Node.js

- Abra **Finder** (icono de cara sonriente azul en su Dock)
- Haga clic en **Descargas** en la barra lateral izquierda
- Encuentre el archivo que descargó (algo como `node-v24.x.x.pkg`)
- Haga doble clic en el archivo
- Aparecerá una ventana de instalación: haga clic en **Continuar**
- Haga clic en **Continuar** nuevamente en la pantalla de Licencia
- Haga clic en **Aceptar** para aceptar la licencia
- Haga clic en **Instalar**
- Escriba la contraseña de su Mac (la que usa para iniciar sesión)
- Haga clic en **Instalar Software**
- Espere a que se complete la instalación (1-2 minutos)
- Haga clic en **Cerrar** cuando vea "La instalación fue exitosa"
- Puede mover el instalador a la Papelera si se le pregunta

## Paso 3: Verificar la Instalación de Node.js

- Haga clic en el icono **Launchpad** en su Dock (icono con cuadrados de colores)
- Escriba `Terminal` en el cuadro de búsqueda
- Haga clic en **Terminal** (icono de cuadrado negro)
- Se abrirá una ventana de Terminal
- Escriba:
   ```
   node --version
   ```
- Debería ver algo como `v24.x.x` (los números exactos pueden variar)
- Si ve un número de versión, ¡excelente! Node.js está instalado correctamente

**Si ve "command not found":**
- Cierre Terminal completamente (**Terminal** en la barra de menú, luego **Salir de Terminal**)
- Abra Terminal de nuevo
- Intente el comando nuevamente

**Consejo:** Mantenga Terminal abierto para los próximos pasos.

## Paso 4: Instalar Claude Code

- En Terminal, escriba:
   ```
   npm install -g @anthropic-ai/claude-code
   ```
- Espere a que Claude Code se instale (2-5 minutos)
- Si ve un error de "permission denied", intente con `sudo`:
   ```
   sudo npm install -g @anthropic-ai/claude-code
   ```
   Ingrese su contraseña de Mac cuando se solicite (no la verá mientras escribe)
- Puede ver algunas advertencias en amarillo o rojo: esto es normal
- Cuando se complete la instalación, verifique escribiendo:
   ```
   claude --version
   ```
- Debería ver el número de versión de Claude Code

## Paso 5: Conectarse a Su Cuenta de Anthropic

### Opción A. Usar su suscripción a Claude Pro o Max

- En Terminal, escriba:
   ```
   claude
   ```
- Claude intentará abrir un navegador. Si no se abre automáticamente, copie la URL mostrada en Terminal y péguela en su navegador.
- Inicie sesión en su cuenta de Claude.ai (esto puede ocurrir automáticamente)
- Haga clic en **Authorize**
- Haga clic en **Copy Code** cuando aparezca un código largo
- Regrese a Terminal
- Para pegar: **Editar** en la barra de menú, luego **Pegar**
- Debería ver un mensaje de éxito
- Siga las instrucciones para completar la configuración

### Opción B. Usar la clave API de Anthropic

Si tiene una clave API de Anthropic en lugar de una suscripción a Claude:

- Primero, obtenga su clave API de la [Consola de Anthropic](https://console.anthropic.com/)
- En Terminal, escriba:
   ```
   export ANTHROPIC_API_KEY="su-clave-api-aqui"
   ```
   Reemplace `su-clave-api-aqui` con su clave API real
- Para hacerlo permanente (no tener que configurarlo cada vez), agréguelo a su perfil de shell:
   ```
   echo 'export ANTHROPIC_API_KEY="su-clave-api-aqui"' >> ~/.zshrc
   ```
   Reemplace `su-clave-api-aqui` con su clave API real
- Cierre y vuelva a abrir Terminal para que los cambios surtan efecto

**Nota:** Si usa una Mac más antigua con bash en lugar de zsh, reemplace `~/.zshrc` con `~/.bash_profile` en el comando anterior.

### Opción C. Usar la API de Anthropic a través de Azure Foundry

Esta opción es para organizaciones que usan modelos Claude alojados en Azure. En Terminal, pegue este código para definir variables de entorno (antes de iniciar Claude):
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

## Paso 6: Comenzar a Usar Claude Code

¡Ya está listo! Así se usa Claude Code:

- En Terminal, escriba:
   ```
   claude
   ```
- Le hará algunas preguntas antes de estar listo para conversar
- Para probar que funciona, haga una pregunta general como "Explica la computación cuántica"

## Paso 7: Navegar a Su Proyecto

- Si tiene un proyecto en las carpetas de su Mac, navegue a él:
   ```
   cd ~/Documents/test_claude
   ```
   Reemplace `test_claude` con el nombre real de su carpeta de proyecto

- Luego inicie Claude:
   ```
   claude
   ```
- Comience pidiéndole a Claude que explique la base de código
- Puede pedirle a Claude que haga cambios
- Pruebe su código en su IDE preferido

**Nota:** Claude opera dentro de una carpeta de proyecto. Define permisos de escritura en la carpeta y guarda la configuración ahí. Es el espacio de trabajo de Claude.

## Próximos Pasos
- [VS Code Getting Started](./VS_Code_Getting_Started.md) - Aprenda a usar VS Code, un editor de código popular
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Ejecute Claude Code dentro de VS Code
- [Writing a Research Paper with Claude Code](./Writing_Research_Paper_Claude_Code.md) - Use Claude Code para escritura académica

## Cómo Abrir Terminal Nuevamente

Después de cerrar Terminal, así se abre de nuevo:

- Haga clic en el icono **Launchpad** en su Dock (icono con cuadrados de colores)
- Escriba `Terminal` en el cuadro de búsqueda
- Haga clic en **Terminal**
- Se abrirá una ventana de Terminal

## Solución de Problemas

### El instalador de Node.js no se abre
- Asegúrese de haber descargado el archivo `.pkg` de nodejs.org
- Intente hacer clic derecho en el archivo y seleccionar **Abrir** en lugar de hacer doble clic
- Vaya a **Configuración del Sistema** > **Privacidad y Seguridad** y haga clic en **Abrir de Todos Modos**

### "node: command not found" después de la instalación
- Cierre Terminal completamente (haga clic en **Terminal** en la barra de menú, luego **Salir de Terminal**)
- Abra Terminal nuevamente
- Intente `node --version` nuevamente
- Si todavía no funciona, reinicie su Mac e intente nuevamente

### La instalación de npm falla con errores de permisos
- Agregue `sudo` antes del comando npm:
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
- Ingrese su contraseña de Mac cuando se le solicite (no la verá mientras escribe)

### Comandos de Claude Code no encontrados
- Asegúrese de que la instalación de npm se completó exitosamente
- Intente cerrar y volver a abrir Terminal
- Verifique si Claude Code está instalado: `npm list -g @anthropic/claude-code`
- Intente instalar nuevamente: `npm install -g @anthropic-ai/claude-code`

### Errores de "Cannot find module"
- Asegúrese de que Node.js esté instalado correctamente: `node --version`
- Intente reinstalar Claude Code: `npm uninstall -g @anthropic/claude-code` luego `npm install -g @anthropic-ai/claude-code`

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

Claude Code funciona con todas ellas.

## ¿Necesita Ayuda?

- Para descargar Node.js: [Sitio Web Oficial de Node.js](https://nodejs.org/)
- Para problemas con Node.js: [Documentación de Node.js](https://nodejs.org/docs/)
- Para problemas con npm: [Documentación de npm](https://docs.npmjs.com/)
- Para problemas con Claude Code: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*Última actualización: Diciembre 2025*
