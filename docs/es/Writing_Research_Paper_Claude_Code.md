[Inicio](index.html)

# Escribir Artículos de Investigación con Claude Code

Aprenda a escribir artículos de investigación utilizando Claude Code como asistente para investigar, generar ideas, planificar, redactar y editar. Automatice el proceso completo creando un slash command reutilizable. Vea un [ejemplo de artículo](./example_paper.md) creado con este flujo de trabajo.

## Conceptos Clave

- **Flujo de trabajo** - Investigación → Lluvia de ideas → Investigación enfocada → Esquema → Borrador → Revisión manual → Pulir con IA → Agregar resumen → Mejorar título → Verificar referencias → Corrección con IA
- **Asistente de IA** - Usted toma las decisiones importantes mientras la IA realiza el trabajo repetitivo
- **Claude Code** - Sistema de IA que busca información en la web, organiza la investigación y redacta contenido mediante instrucciones en lenguaje natural
- **Slash command** - Comando personalizado que puede reutilizarse en Claude Code para automatizar flujos de trabajo

## Lo Que Necesitará

- Haber completado [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win) o [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac)
- 30-40 minutos

## Paso 1: Crear una Carpeta de Proyecto

Cree una carpeta para su artículo de investigación:

- Abra **File Explorer** (Windows) o **Finder** (Mac)
- Navegue a **Documentos**
- Cree una nueva carpeta llamada `test_claude`

Todo el trabajo de este proyecto se realizará en esta carpeta.

## Paso 2: Iniciar VS Code
Para Windows:
- Haga clic en el **botón Inicio de Windows** (esquina inferior izquierda de su pantalla)
- Escriba `Visual Studio Code` o `VS Code` en el cuadro de búsqueda
- Haga clic en **Visual Studio Code** cuando aparezca en los resultados de búsqueda
- VS Code se abre con una pestaña de Bienvenida - puede cerrar esta pestaña
- Mire la esquina inferior izquierda de VS Code - verá un icono azul o verde
- Haga clic en este icono para abrir el menú de conexión remota
- Seleccione **Connect to WSL** del menú
- VS Code se recargará y se conectará a su instalación de Ubuntu
- La esquina inferior izquierda ahora debería mostrar **WSL: Ubuntu**

Para Mac:
- Abra **Finder** y vaya a **Aplicaciones**
- Encuentre **Visual Studio Code** y haga doble clic en él
- Si ve una advertencia "Visual Studio Code es una aplicación descargada de internet", haga clic en **Abrir**
- VS Code se abre con una pestaña de Bienvenida - puede cerrar esta pestaña

## Paso 3: Abrir la Carpeta en VS Code
Para Windows vía WSL:
- En VS Code (todavía conectado a WSL), haga clic en **File** en la barra de menú, luego en **Open Folder**
- Aparece un menú desplegable **Open Folder** en el centro superior
- Encuentre su carpeta escribiendo:
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Reemplace `YOUR_USERNAME` con su nombre de usuario de Windows (por ejemplo, `John.Smith`)
- Haga clic en **OK**. VS Code se recarga con su carpeta `test_claude`


Para Mac:
- En VS Code, haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue y seleccione la carpeta `test_claude`
- Haga clic en **Open** (Mac) o **OK** (Windows)
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**

## Paso 4: Iniciar Claude Code

- Abra un terminal: haga clic en **Terminal** en el menú principal de VS Code, luego en **New Terminal**
- En el panel de terminal, escriba:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el tutorial de instalación ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 5: Investigación Inicial

Pídale a Claude que investigue su tema. Copie y pegue este prompt en Claude Code, reemplazando el tema con el suyo propio:

```
Estoy escribiendo un artículo de investigación de aproximadamente 1,000 palabras sobre la adopción de IA en el lugar de trabajo.
Busca datos recientes (2023-2025) sobre:
- Ganancias de productividad con herramientas de IA
- Preocupaciones sobre desplazamiento laboral y estadísticas
- Casos de estudio reales de empresas

Requisitos:
- Prioriza investigación revisada por pares e informes de la industria confiables
- Evita anécdotas y artículos de opinión
- Lista cada fuente con un resumen de 1-3 oraciones
- Agrupa las fuentes por tema

Guarda como general_research.md
```

Claude buscará en la web y organizará los resultados en un archivo llamado `general_research.md`. Esto puede tardar uno o dos minutos. Cuando termine, solicite un resumen:

```
Dame un resumen breve.
```

Revise el resumen para obtener una visión general rápida del panorama de investigación.

## Paso 6: Leer las Fuentes
Lea el documento de investigación y haga clic en las fuentes originales para verificar la información:

1. Haga clic en `general_research.md` en el panel Explorer a la izquierda
2. Previsualice el documento formateado: haga clic derecho en la pestaña `general_research.md` y seleccione **Open Preview**
3. Haga clic en los enlaces de las fuentes para leer los artículos y estudios originales

## Paso 7: Lluvia de Ideas Sobre Su Enfoque

Pídale a Claude que le ayude a generar ideas:

```
Basándote en esta investigación, sugiere 3-4 enfoques que podría tomar para este artículo.
```

Revise las opciones y elija la que más le interese.

## Paso 8: Investigación Enfocada

Ahora que tiene su enfoque, pídale a Claude una investigación más específica:

```
Quiero enfocarme en [tu enfoque elegido]. Busca datos más específicos
y ejemplos que respalden esta perspectiva. Guarda como focused_research.md
```

Claude encontrará información específica sobre su enfoque.

## Paso 9: Crear Su Plan

Pídale a Claude que cree un esquema basado en su enfoque elegido:

```
Dame 3 opciones de esquema breve para mi artículo basado en la investigación
enfocada y mi enfoque elegido. Usa viñetas para el flujo narrativo.
Guarda como outlines.md
```

Revise el esquema y pídale a Claude que lo ajuste según sea necesario (por ejemplo, "Haz que la sección 2 se enfoque más en casos de estudio" o "Agrega una sección sobre limitaciones").

## Paso 10: Redactar el Artículo

Seleccione su esquema y pídale a Claude que escriba el borrador completo:

```
Me gusta el esquema #2 [tu opción elegida].

Escribe un artículo de investigación de aproximadamente 1,000 palabras basado en el esquema y la investigación.

Estructura:
- Introducción: Gancho, contexto, declaración de tesis
- Cuerpo: 2-3 secciones con argumentos, estadísticas y ejemplos
- Conclusión: Resumen e implicaciones

Estilo:
- Oraciones claras y concisas (promedio de 15-20 palabras)
- Voz activa, tono analítico
- Estadísticas integradas en la prosa (sin listas de viñetas)
- Transiciones suaves entre párrafos

Citas:
- Usa referencias numeradas [1], [2], etc. después de las afirmaciones
- Incluye 5-15 referencias
- Agrega una sección de Referencias al final

Guarda como paper.md
```

Claude escribirá el borrador completo.

## Paso 11: Revisar Manualmente

Abra `paper.md` en su editor de texto. Lea cuidadosamente y haga sus propias revisiones:
- Agregue su voz personal y perspectivas
- Ajuste los argumentos para que coincidan con su pensamiento
- Corrija cualquier redacción incómoda
- Asegúrese de que las citas sean precisas

Guarde sus cambios en el editor.

## Paso 12: Pulir con IA

Pídale a Claude que mejore secciones específicas:

```
Haz la introducción más atractiva con un gancho convincente.
```

## Paso 13: Agregar un Resumen

Pídale a Claude que agregue un resumen breve al principio:

```
Agrega un resumen al inicio del artículo. Escribe 2-3 oraciones cortas
que resuman el artículo.
```

Claude agregará el resumen. Revíselo y edítelo para asegurarse de que capture con precisión la esencia de su artículo.

## Paso 14: Mejorar el Título

Pídale a Claude que le sugiera opciones para el título:

```
Dame varias opciones para el título. Hazlo más atractivo.
```

Seleccione un título y agregue su toque personal:

```
Me gusta la opción #2 [tu elección]. Edita el archivo.
```

## Paso 15: Verificar Referencias (Opcional)
Pídale a Claude que verifique que sus citas sean consistentes y completas:
```
Verifica todas las referencias en mi artículo:
- Verifica que cada número de cita [1], [2], etc. tenga una referencia correspondiente
- Verifica que cada referencia en la lista esté citada en el artículo
- Verifica que los nombres de autores y títulos sean consistentes
- Verifica que los datos y ejemplos citados aparezcan en la fuente
```

Nota: Claude solo puede verificar fuentes de acceso público. Para artículos con acceso restringido, verifique manualmente que sus citas coincidan con lo que leyó.

## Paso 16: Corrección con IA

Pídale a Claude que haga una corrección final:

```
Haz una corrección final del artículo:
- Corrige cualquier error ortográfico y gramatical
- Asegura un formato consistente en todo el documento
- Verifica el flujo y las transiciones
```

Revise los cambios realizados por Claude.

**Exportar a Word:** En VS Code, haga clic derecho en la pestaña `paper.md` y seleccione **Open Preview**. Haga clic dentro del panel de vista previa, luego haga clic en **Edit > Select All** y **Edit > Copy**. Pegue en Microsoft Word—el formato se conservará.

## Paso 17: Crear un Slash Command para Futuros Artículos

Guarde este flujo de trabajo como un slash command reutilizable para sus próximos artículos:

```
Crea un slash command llamado /research-paper que me guíe a través de
todo este flujo de trabajo. Guárdalo para que pueda usarlo en futuros artículos de investigación sobre diversos temas.
```

Claude creará un slash command personalizado en su carpeta `.claude/commands/`. Es un archivo Markdown que contiene un prompt. Podrá comenzar su próximo artículo simplemente escribiendo `/research-paper [tu tema]`.

## Paso 18: Obtener Retroalimentación

Los LLM no tienen memoria permanente. Para cada respuesta, se envía el historial completo de la conversación como contexto. A medida que la interacción se hace más larga, es importante gestionar la longitud del contexto. Limpiar el contexto permite obtener una perspectiva fresca.

Limpie la memoria de Claude para obtener retroalimentación imparcial sobre su artículo:

```
/clear
```

Esto elimina todo el historial de conversación, permitiendo que Claude lea su artículo con una perspectiva fresca. Ahora solicite retroalimentación:

```
Lee paper.md y dame retroalimentación honesta.
```

Claude evaluará su artículo de forma objetiva, sin estar influenciado por haberlo escrito. Realice las revisiones finales según la retroalimentación recibida.


## El Flujo de Trabajo Completo

1. **Crear Carpeta** - Configure su carpeta de proyecto en Documentos
2. **Abrir en VS Code** - Abra la carpeta en VS Code
3. **Iniciar Claude Code** - Lance Claude Code desde el terminal
4. **Investigar** - Claude busca información general sobre su tema
5. **Leer Fuentes** - Revise la investigación en su editor de texto
6. **Lluvia de Ideas** - Elija su enfoque/perspectiva
7. **Investigación Enfocada** - Claude encuentra datos específicos para su enfoque elegido
8. **Planificar** - Claude crea opciones de esquema basadas en su perspectiva
9. **Redactar** - Claude escribe el artículo completo con referencias
10. **Revisar Manualmente** - Usted agrega su voz y hace cambios
11. **Pulir con IA** - Claude mejora secciones específicas
12. **Agregar Resumen** - Claude crea un resumen ejecutivo
13. **Mejorar Título** - Claude sugiere opciones de título, usted personaliza
14. **Verificar Referencias** - (Opcional) Claude verifica todas las citas
15. **Corrección con IA** - Claude corrige errores y mejora el flujo
16. **Crear Slash Command** - Guarde el flujo de trabajo para futuros artículos
17. **Obtener Retroalimentación Fresca** - Limpie la memoria para una crítica imparcial

## Próximos Pasos

Ahora que tiene el slash command `/research-paper`, intente escribir más artículos:

- **Tecnología:** `/research-paper "Impacto de las redes sociales en la salud mental adolescente"`
- **Negocios:** `/research-paper "Productividad del trabajo remoto"`
- **Ciencia:** `/research-paper "Ética de la edición genética CRISPR"`
- **Formato:** Pídale a Claude `Dame el artículo en formato LaTeX`

El slash command lo guiará automáticamente a través de todo el flujo de trabajo. Recuerde limpiar la memoria cuando cambie de tema.

## Solución de Problemas

- **Los resultados de búsqueda parecen desactualizados:** Especifique "busca datos de 2024-2025 sobre [tema]"
- **El borrador es muy largo o corto:** Indique: "Haz que tenga aproximadamente 1,000 palabras"
- **No puede encontrar archivos:** En el terminal, escriba `ls` para listar todos los archivos en la carpeta actual

## Lo Que Puede Pedirle a Claude

- `Busca estadísticas más recientes sobre [tema]` - Encontrar datos actualizados
- `Resume los argumentos clave de este artículo` - Obtener una visión general
- `Haz la conclusión más persuasiva` - Mejorar secciones específicas
- `Cita todas las fuentes en formato APA` - Formatear referencias

Claude maneja la investigación y redacción mediante lenguaje natural. No hay comandos que memorizar.

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 9 de diciembre de 2025.
