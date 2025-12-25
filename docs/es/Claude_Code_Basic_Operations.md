[Inicio](index.html)

# Claude Code: Operaciones Básicas

Aprender a programar con asistencia de IA puede resultar abrumador al principio. Claude Code funciona como un colega experto: usted describe lo que necesita en lenguaje natural y Claude le ayuda a lograrlo. Este tutorial enseña las operaciones esenciales para el uso diario, desde iniciar conversaciones hasta gestionar su espacio de trabajo.

## Conceptos Clave

- **Workspace** - Espacio de trabajo: la carpeta desde donde inicia Claude Code se convierte en el espacio de trabajo de la sesión
- **REPL (Read-Eval-Print Loop)** - Sesión interactiva donde escribe comandos, Claude responde y la conversación continúa hasta que cierra la sesión
- **Contexto** - Cantidad de código e historial que Claude recuerda; funciona como memoria de trabajo que se llena con el tiempo
- **Slash Commands** - Comandos especiales que comienzan con `/` para realizar acciones específicas como limpiar el historial o mostrar ayuda

## Lo Que Necesitará

- Claude Code instalado desde el tutorial de [Windows](Install_CLAUDE_Code_Win.md) o [Mac](Install_Claude_Code_MacOS.md)
- WSL instalado si está usando Windows
- Familiaridad básica con el uso de una terminal o símbolo del sistema
- 15-20 minutos

## Paso 1: Abra Su Terminal

- **Windows**: Presione la tecla Windows, escriba `Ubuntu`, y presione Enter para abrir la terminal WSL
- **Mac**: Presione `Cmd+Space`, escriba `Terminal`, y presione Enter

Se abrirá una ventana de texto donde puede escribir comandos.

## Paso 2: Obtener los Archivos del Proyecto de Demostración

Usaremos un proyecto real de ciencia de datos para explorar las funcionalidades de Claude Code. Puede clonarlo con Git o descargarlo directamente.

**Opción A: Clonar con Git (si tiene Git instalado):**

```
git clone https://github.com/gexijin/data_projects
cd data_projects
```

**Opción B: Descargar sin Git:**

- Visite [https://github.com/gexijin/data_projects](https://github.com/gexijin/data_projects) en su navegador web
- Haga clic en el botón verde **Code** cerca de la parte superior derecha
- Haga clic en **Download ZIP**
- Extraiga el archivo ZIP a una carpeta llamada **data_projects** en la carpeta Descargas.
- En su terminal, navegue a la carpeta extraída:
  - **Windows**: `cd /mnt/c/Users/SuNombre/Downloads/data_projects`
  - **Mac/Linux**: `cd ~/Downloads/data_projects`

Reemplace `SuNombre` con su nombre de usuario real y ajuste la ruta si lo extrajo en otro lugar. Para usuarios de Windows, sus archivos de Windows se acceden desde /mnt/c en el sistema Linux.

## Paso 3: Inicie Claude Code desde la Carpeta

En su terminal (asegúrese de estar dentro de la carpeta data_projects), escriba:

```bash
claude
```

Inicie sesión con su suscripción de Claude siguiendo el [tutorial de instalación](Install_CLAUDE_Code_Win.md). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

Después de iniciar sesión correctamente, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 4: Hacer Preguntas Sobre Su Proyecto

Claude Code lee automáticamente sus archivos cuando es necesario. Pruebe estas preguntas para entender su proyecto:

**Pregunte sobre la estructura de carpetas:**

```
¿Cuál es la estructura de carpetas de este proyecto?
```

**Pregunte sobre tecnologías:**

```
¿Qué tecnologías y bibliotecas usa este proyecto?
```

**Pregunte sobre cambios recientes:**

```
¿Cuál fue el último cambio realizado en este proyecto?
```

Claude verificará el historial de Git (si está disponible) y le informará sobre los commits recientes.

Puede preguntarle a Claude cualquier cosa sobre su código en lenguaje natural. Claude lee los archivos necesarios para responder sus preguntas.

## Paso 5: Slash Commands Esenciales

Escriba `/` y presione Enter para ver todos los comandos disponibles. Estos son los más importantes:

**Ver todos los comandos:**

```
/
```

Esto muestra un menú de todos los slash commands. Use las teclas de flecha para navegar, presione Enter para seleccionar, o presione Esc para cancelar.

**Obtener ayuda:**

```
/help
```
Muestra documentación sobre el uso de Claude Code.



**Verificar el uso de contexto:**
Es importante gestionar el contexto, la "memoria de trabajo" de Claude.

```
/context
```

**Limpiar el historial de conversación:**

Cuando el contexto se llena, inicie una nueva conversación con `/clear`.
```
/clear
```
Elimina la conversación actual y comienza de nuevo. Úselo cuando desee cambiar de tema o cuando la conversación sea demasiado larga. Es esencial para gestionar el contexto.


**Salir de Claude Code:**

```
/exit
```

Finaliza su sesión y regresa al prompt normal de la terminal. También puede presionar **Ctrl + C** dos veces.

## Paso 6: Atajos de Teclado

Estos atajos hacen que trabajar con Claude Code sea más rápido:

- **Shift+Tab** - Cambiar entre modo plan, edición o normal - Planifique primero para tareas complejas
- **Alt+Enter** (Windows/Linux) o **Option+Return** (Mac) - Agregar una nueva línea en su mensaje sin enviarlo
- **Ctrl+C** - Cancelar la operación actual o la respuesta de Claude
- **Ctrl+D** - Aprobar cambios en archivos cuando Claude solicite permiso
- **Esc** - Cerrar menús o cancelar la entrada actual

## Paso 7: Siempre Crear un Archivo CLAUDE.md

El archivo CLAUDE.md es el manual de instrucciones de su proyecto para Claude. Persiste entre sesiones, permitiendo que Claude recuerde el contexto importante de su proyecto.

**Crear el archivo:**

```
/init
```

Claude creará el archivo con un resumen de su proyecto. Este archivo permanece en la raíz de su proyecto y Claude lo lee automáticamente cada vez que inicia una nueva sesión.

Puede editar CLAUDE.md en cualquier momento para agregar instrucciones específicas del proyecto, convenciones de codificación o contexto importante como el propósito de los archivos.

## Paso 8: Referirse a Archivos o Líneas de Código

Puede usar `@` para referirse a un archivo específico:

```
Explica el código en @Visualization/Matplotlib/Nested_Pie_Chart.ipynb
```

Claude leerá el notebook y explicará qué hace, cómo funciona y qué logra el código. Esto efectivamente trae el archivo al contexto.

Si trabaja con Claude Code desde VS Code y tiene la extensión instalada, puede agregar el archivo al contexto simplemente abriéndolo. Verá en la parte inferior derecha de la ventana de comandos `In Nested_Pie_Chart.ipynb`. Así Claude sabe que está hablando de este archivo.

Además, puede seleccionar algunas líneas de código y Claude mostrará **3 lines selected**. Puede pedirle a Claude que haga cambios rápidos a estas líneas o hacer preguntas sobre ellas. Por esto recomendamos usar Claude Code desde VS Code.


## Paso 9: Realizar Acciones con Comandos de Linux

Claude puede realizar acciones ejecutando comandos de Linux de diversas formas.

- Instalar software
  ```
  Instala la biblioteca pandas
  ```

- Iniciar control de versiones
  ```
  Comienza a rastrear cambios usando Git. Mi nombre es James Bond y mi correo es bond@earth.com
  ```
- Confirmar cambios
  ```
  Confirma estos cambios.
  ```
- Encontrar y descargar datos
  ```
  Descarga el dataset de calidad de vino de UCI. Ponlo en una nueva carpeta llamada wine.
  ```

- Ejecutar código
  ```
  Reescribe el código del gráfico circular anidado como un script regular de Python.
  Ejecútalo y guarda el nuevo código y gráficos en la misma carpeta.
  ```

Podemos hacer esta solicitud vaga porque acabamos de pedirle que explique el código. Muchas cosas suceden después de esto. Claude instala software, soluciona errores, resuelve problemas de entornos, todo por su cuenta.

Esencialmente tiene un experto en comandos bash de Linux a su disposición. Mientras gestione los permisos y apruebe las acciones, puede ser muy productivo.

## Próximos Pasos

Ahora que conoce lo básico, pruebe esto por su cuenta:

- Pídale a Claude que explique un algoritmo de aprendizaje automático en una de las carpetas del proyecto
- Solicite modificaciones a un notebook existente (como cambiar colores de gráficos o agregar nuevas características)
- Cree un nuevo script de Python que use datos del proyecto
- Pídale a Claude que compare dos enfoques diferentes en el código base

## Solución de Problemas

- **Error "Command not found"** - Claude Code no está instalado o no está en su PATH. Ejecute `npm install -g @anthropic-ai/claude-code` para instalarlo.
- **Claude proporciona información desactualizada** - Limpie el contexto con `/clear` y pregunte nuevamente. Las conversaciones largas llenan la memoria de Claude.
- **Los cambios en archivos no funcionan** - Asegúrese de tener permisos de escritura en su carpeta de proyecto. Claude solicitará aprobación antes de modificar archivos. Presione Ctrl+D para aprobar.
- **El contexto se llena rápidamente** - Use `/context` para verificar el uso. Cuando esté casi lleno, use `/clear` para iniciar una nueva conversación con contexto limpio.

## Resumen del Flujo de Trabajo

Trabajar con Claude Code sigue este patrón:

- Inicie Claude en su carpeta de proyecto con `claude`
- Haga preguntas en lenguaje natural
- Claude lee archivos según sea necesario y responde
- Solicite cambios en el código—Claude pide permiso antes de modificar archivos
- Use `/clear` al cambiar de tema o cuando el contexto se llene
- Use `/exit` cuando termine

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 14 de diciembre de 2025.
