[Inicio](index.html)

# Primeros Pasos con VS Code

Quiere escribir código, pero Notepad o TextEdit le resulta muy limitante. Necesita algo que le ayude a codificar más rápido, con resaltado de sintaxis, autocompletado y herramientas integradas. **VS Code es como un cuaderno inteligente para código**: entiende lo que escribe y le ayuda en el proceso. [Visual Studio Code](https://code.visualstudio.com) es gratuito, funciona en cualquier sistema operativo y millones de desarrolladores lo utilizan.

## Conceptos Clave

- **Editor** - Área principal donde escribe código
- **Explorer** - Barra lateral que muestra sus archivos y carpetas
- **Extensions** - Complementos que agregan nuevas funciones a VS Code
- **Terminal Integrado** - Línea de comandos integrada en VS Code

## Lo Que Necesitará

- Computadora con Windows, macOS o Linux
- Conexión a Internet
- ~500 MB de espacio en disco
- 20-25 minutos

## Paso 1: Descargue e Instale VS Code

- Vaya a [code.visualstudio.com](https://code.visualstudio.com)
- Haga clic en el botón **Download** (detecta su sistema operativo automáticamente)
- Ejecute el instalador:
   - **Windows:** Haga doble clic en el archivo `.exe`, haga clic en **Next** en las indicaciones
   - **Mac:** Abra el archivo `.dmg`, arrastre VS Code a **Applications**
   - **Linux:** Siga las instrucciones para su gestor de paquetes
- Inicie VS Code

Verá una pestaña de bienvenida con opciones para comenzar.

## Paso 2: Recorra la Interfaz

VS Code tiene cinco áreas principales:

- **Barra de Actividad** (borde izquierdo) - Iconos para Explorer, Search, Git, Extensions, etc.
- **Barra Lateral** - Muestra el contenido de la actividad seleccionada (archivos, resultados de búsqueda)
- **Editor** (centro) - Donde escribe código
- **Panel** (parte inferior) - Terminal, Problems, Output
- **Barra de Estado** (borde inferior) - Información sobre su archivo y proyecto

Haga clic en el icono **Explorer** (parte superior de la Barra de Actividad) para ver el navegador de archivos.

## Paso 3: Abra una Carpeta y Explore

- Haga clic en **File** → **Open Folder**
- Navegue a cualquier carpeta existente en su computadora (por ejemplo, Documents)
- Haga clic en **Open** (o **Select Folder**)
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**

La barra lateral Explorer ahora muestra los archivos de su carpeta:

- Haga clic en una carpeta para expandirla
- Haga clic en cualquier archivo para abrirlo en el editor
- Haga clic en el icono **Search** en el Activity Bar (lupa) para buscar en todos los archivos

## Paso 4: Cree un Archivo Markdown

- En Explorer, haga clic en el icono **New File** (página con +)
- Nómbrelo `README.md`
- Agregue este contenido:

```
# Mi Proyecto

Este es un **proyecto de demostración** para aprender VS Code.

## Características
- Fácil de editar
- Formato Markdown
- Vista previa en vivo

## Próximos Pasos
1. Agregar más contenido
2. Probar otros tipos de archivos
3. Explorar extensiones
```
- Haga clic en **File** → **Save** para guardar

Markdown es un formato de texto simple que usa símbolos como `#` para encabezados, `**` para negrita y `-` para listas. Se usa ampliamente para documentación y para comunicarse con LLMs como ChatGPT y Claude.

## Paso 5: Instale la Extensión Markdown Preview

- Haga clic en el icono **Extensions** en el Activity Bar (el icono de cuadrados)
- Escriba `Markdown Preview Enhanced` en el cuadro de búsqueda
- Encuentre **Markdown Preview Enhanced** en los resultados
- Haga clic en **Install**

## Paso 6: Previsualice Su Archivo Markdown

- Abra `README.md` si aún no está abierto
- Haga clic derecho en el editor y seleccione **Markdown Preview Enhanced: Open Preview to the Side**

Se abre un panel de vista previa que muestra su Markdown formateado: edite a la izquierda y vea los cambios a la derecha en tiempo real.

## Paso 7: Use el Terminal Integrado

- Haga clic en **Terminal** → **New Terminal**
- Pruebe estos comandos:

**Listar archivos:**
```
ls
```
(En Windows Command Prompt, use `dir`)

**Mostrar directorio de trabajo:**
```
pwd
```
(En Windows Command Prompt, use `cd`)

**Crear una carpeta nueva:**
```
mkdir notes
```

Revise Explorer: aparece la carpeta `notes`. El terminal se ejecuta en su carpeta de proyecto, por lo que los comandos afectan directamente su proyecto.

## Paso 8: Use Agentes de IA en VS Code (Opcional)

VS Code incluye [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat), un asistente de IA que puede explicar, escribir y depurar código.

- Abra el archivo `README.md` (o cualquier otro archivo en su proyecto)
- Haga clic en **Chat** → **Open Chat** en la barra de título (o presione `Ctrl+Alt+I` en Windows/Linux, `Ctrl+Cmd+I` en Mac)
- Si se le solicita, inicie sesión con su cuenta de **GitHub** (hay un plan gratuito disponible)
- En el panel de chat que se abre, escriba: "Explica este archivo"
- Presione **Enter**

GitHub Copilot analizará su archivo y explicará qué hace. Puede pedirle que escriba código nuevo, corrija errores o responda preguntas como "¿Cómo agrego más características?"

**Consejo:** Para [edición en línea](https://code.visualstudio.com/docs/copilot/copilot-chat), resalte código en cualquier archivo y presione `Ctrl+I` (Windows/Linux) o `Cmd+I` (Mac) para pedirle a Copilot que modifique, corrija o explique solo esa sección.

## Cómo Reabrir Su Proyecto

- Abra VS Code desde el menú Start (Windows), Spotlight (Mac) o Applications (Linux)
- Haga clic en **File** → **Open Recent** → seleccione su carpeta
- O haga clic en **File** → **Open Folder** y navegue hasta ella

## Solución de Problemas

- **La vista previa no se muestra:** Asegúrese de que la extensión Markdown Preview Enhanced esté instalada y que tenga un archivo `.md` abierto
- **El terminal muestra el directorio incorrecto:** Haga clic en el icono de papelera en el panel del terminal, luego en **Terminal** → **New Terminal**
- **El menú Chat no es visible:** Es posible que necesite instalar GitHub Copilot Chat: haga clic en el icono **Extensions**, busque "GitHub Copilot Chat" e instálelo
- **Las extensiones no funcionan:** Haga clic en **View** → **Command Palette**, escriba "reload window" y seleccione **Developer: Reload Window**

## Flujo de Trabajo Completo

1. Abra una carpeta en VS Code
2. Cree y edite archivos
3. Use extensiones para previsualizar
4. Use el terminal para ejecutar comandos
5. Use IA para entender y mejorar el código
6. Guarde y repita

## Próximos Pasos

- **Pruebe otros tipos de archivos:** Cree archivos `.html`, `.css`, `.js` o `.py` y vea el resaltado de sintaxis de VS Code
- **Explore las funciones de IA:** Pídale a la IA que escriba código, corrija errores o sugiera mejoras para sus proyectos
- **Instale más extensiones:** Pruebe "Prettier" para formato automático o "GitLens" para funciones de Git
- **Aprenda atajos:** Haga clic en **Help** → **Keyboard Shortcuts Reference** para acelerar su flujo de trabajo

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
