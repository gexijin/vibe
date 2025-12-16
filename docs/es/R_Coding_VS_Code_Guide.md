[Inicio](index.html)

# Ejecutar R en VS Code

Quiere escribir código R pero RStudio se siente pesado o prefiere la flexibilidad de VS Code. Piense en VS Code como una navaja suiza: puede manejar R, Python y muchos otros lenguajes en un solo editor liviano. Este tutorial muestra cómo configurar R en VS Code con características inteligentes como finalización de código, gráficos interactivos e incluso aplicaciones Shiny.

## Conceptos Clave

- **[languageserver](https://github.com/REditorSupport/languageserver)** - Paquete de R que habilita finalización de código, verificación de sintaxis y documentación emergente en VS Code
- **[R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - Extensión de VS Code que conecta su editor a R y proporciona resaltado de sintaxis, ejecución de código y depuración
- **[Shiny Extension](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - Extensión de VS Code para crear y ejecutar aplicaciones web Shiny interactivas con recarga automática

## Lo Que Necesitará

- Tutorial [VS Code Basics](./VS_Code_Getting_Started) completado
- Conexión a Internet para descargar R y paquetes
- 10-15 minutos

## Paso 1: Instale o Actualice R

Necesita R versión 4.0 o superior para la mejor compatibilidad.

- **Windows**:
  - Descargue la última versión de R desde [CRAN Windows](https://cran.r-project.org/bin/windows/base/) y ejecute el instalador
  - Durante la instalación, **anote la ruta de instalación** (por ejemplo: `C:\Program Files\R\R-4.5.3`)
  - Si tiene una versión antigua, desinstálela primero mediante Configuración > Aplicaciones

- **macOS**:
  - Descargue desde [CRAN macOS](https://cran.r-project.org/bin/macosx/) y ejecute el instalador .pkg
  - Note si usa Intel (`/Library/Frameworks/R.framework/Resources/bin/R`) o Apple Silicon con Homebrew (`/opt/homebrew/bin/R`)
  - Si está actualizando, la nueva versión reemplazará la antigua

- **Linux**:
  - Use su gestor de paquetes (por ejemplo, `sudo apt install r-base` en Ubuntu)
  - O siga las instrucciones de [CRAN Linux](https://cran.r-project.org/bin/linux/)

Configurará VS Code para encontrar R en el Paso 3, así que no se preocupe si `R --version` aún no funciona en su terminal.

## Paso 2: Instale las Extensiones de R en VS Code

- Abra VS Code
- Haga clic en el ícono de **Extensions** en la barra lateral izquierda
- Busque `REditorSupport.r` y haga clic en **Install** en la extensión R por REditorSupport
- Busque `Posit.shiny` y haga clic en **Install** en la extensión Shiny por Posit

## Paso 3: Encuentre la Ruta de Instalación de R

Antes de configurar VS Code, necesita saber dónde está instalado R en su sistema.

### Para Usuarios de Windows

1. Abra el **Explorador de Archivos**
2. Navegue a `C:\Program Files\R\`
3. Verá una carpeta como `R-4.5.3` (su número de versión puede diferir)
4. Abra esa carpeta → Abra la carpeta `bin`
5. Verá `R.exe` allí
6. La ruta completa es: `C:\Program Files\R\R-4.5.3\bin\R.exe`

**Anote o recuerde su número de versión** (por ejemplo, `R-4.5.3`) - lo necesitará en el Paso 4.

### Para Usuarios de macOS

Su instalación de R típicamente está en una de estas ubicaciones:

- **Instalación estándar (Intel o Apple Silicon)**: `/Library/Frameworks/R.framework/Resources/bin/R`
- **Homebrew en Apple Silicon**: `/opt/homebrew/bin/R`
- **Homebrew en Intel**: `/usr/local/bin/R`

Para verificar qué ruta tiene, abra **Terminal** y escriba:
```bash
which R
```

Esto le mostrará la ruta exacta de su instalación de R.

### Para Usuarios de Linux

R típicamente se instala en: `/usr/bin/R`

Verifique abriendo una terminal y escribiendo:
```bash
which R
```

## Paso 4: Configure VS Code para Encontrar R

- En VS Code, haga clic en el **ícono de engranaje** en la esquina inferior izquierda
- Seleccione **Settings** del menú
- En la barra de búsqueda en la parte superior, escriba `r.rpath.windows` (Windows), `r.rpath.mac` (macOS), o `r.rpath.linux` (Linux)
- Debería ver aparecer la configuración. Haga clic en **Edit in settings.json** debajo de la configuración
- El archivo settings.json se abrirá
- Agregue la configuración apropiada para su plataforma dentro de las llaves `{}`

**Para Windows**, agregue esta línea (reemplace `R-4.5.3` con su versión del Paso 3):

```json
"r.rpath.windows": "C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe",
```

**¿Por qué dos barras invertidas (`\\`)?** En archivos JSON, la barra invertida `\` es un carácter especial (llamado carácter de escape). Para representar una sola barra invertida en la ruta del archivo real, debe escribir dos barras invertidas `\\`. Entonces `C:\Program Files` se convierte en `C:\\Program Files` en settings.json.

**Para macOS**, agregue una de estas líneas:

```json
"r.rpath.mac": "/Library/Frameworks/R.framework/Resources/bin/R",
```

O si instaló R mediante Homebrew en Apple Silicon:

```json
"r.rpath.mac": "/opt/homebrew/bin/R",
```

**Para Linux**, agregue:

```json
"r.rpath.linux": "/usr/bin/R",
```

- Guarde el archivo haciendo clic en **File > Save**
- **Reinicie VS Code** completamente para que los cambios surtan efecto

## Paso 5: Instale los Paquetes de R Requeridos

- En VS Code, haga clic en **View** en el menú superior, luego seleccione **Command Palette**
- Escriba `R: Create R Terminal` y selecciónelo
- Una consola de R aparecerá en el panel de terminal en la parte inferior
  - Debería ver que R se inicia con información de la versión
  - Si obtiene un error, verifique nuevamente su configuración settings.json en el Paso 4 y reinicie VS Code
- Instale los paquetes escribiendo estos comandos uno a la vez:

```r
install.packages("languageserver")
install.packages("shiny")
```

- Espere a que se complete la instalación (puede tomar algunos minutos)
- Escriba `q()` y presione Enter para salir de R
- Escriba `n` cuando se le pregunte sobre guardar el espacio de trabajo

Simplemente escribir `R` en una terminal regular no funcionará a menos que R esté en su PATH del sistema. La extensión R usa su configuración `r.rpath` para encontrar R.

## Paso 6: Cree su Proyecto de R

- Cree una nueva carpeta en su computadora (por ejemplo, `my-r-project`)
- En VS Code, haga clic en **File > Open Folder** y seleccione su nueva carpeta
- Haga clic en **File > New File** en el menú superior
- Guarde el archivo como `analysis.R` haciendo clic en **File > Save**

## Paso 7: Escriba su Primer Script de R

- Escriba este código en `analysis.R`:

```r
# Load the iris dataset
data(iris)

# View the first few rows
head(iris)

# Generate summary statistics
summary(iris)

hist(iris$Sepal.Length)
```

- Guarde el archivo haciendo clic en **File > Save**

## Paso 8: Ejecute Código R Interactivamente

- Con `analysis.R` abierto, seleccione una línea de código y presione `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (Mac) para ejecutarla
- Si no tiene una terminal abierta, el primer `Ctrl+Enter` / `Cmd+Enter` abre una terminal de R. El segundo ejecuta el código.
- Observe cómo la salida aparece en la terminal y el gráfico se abrirá en una ventana separada
- También puede seleccionar todas las líneas y ejecutarlas de la misma manera.

## Paso 9: Cree una Aplicación Shiny Simple

- Cree un nuevo archivo en su carpeta de proyecto: **File > New File**
- Guárdelo como `app.R`
- Escriba este código:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interactive Histogram"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Waiting time (minutes)",
         main = "Distribution of Waiting Times")
  })
}

shinyApp(ui = ui, server = server)
```

- Guarde el archivo
- Note el botón **▶** que aparece en la parte superior derecha del editor
- Haga clic en el menú desplegable para seleccionar **Run Shiny App**
- La aplicación se abre en un navegador o panel de VS Code
- Mueva el deslizador y observe cómo el histograma se actualiza instantáneamente

## Paso 10: Use la Finalización de Código y Ayuda Emergente

- En `analysis.R`, comience a escribir `mea` en una nueva línea
- Aparece un menú desplegable con sugerencias - seleccione `mean()` presionando Enter
- Coloque su mouse sobre la palabra `mean` en su código existente
- Aparece una ventana emergente mostrando la documentación de la función y ejemplos de uso
- Intente colocar el cursor sobre `lm`, `summary`, o `plot` para ver su documentación
- Escriba `data$` y observe cómo VS Code sugiere nombres de columnas (`x` e `y`)

## Paso 11: Pruebe Más Características

- **Integración con Markdown**: Cree un archivo R Markdown (`.Rmd`) para mezclar código, salida y texto
- **Formateo de código**: Haga clic derecho en su script de R y seleccione **Format Document** para formatear automáticamente el código
- **Depuración**: Establezca puntos de interrupción haciendo clic a la izquierda de los números de línea, luego ejecute el código en modo de depuración
- **Integración con Git**: Use las características de Git integradas en VS Code para el control de versiones de sus proyectos de R

## Próximos Pasos

- Cree una aplicación Shiny de múltiples archivos con archivos separados `ui.R` y `server.R`
- Explore [ggplot2](https://ggplot2.tidyverse.org/) para visualización avanzada de datos
- Pruebe los paquetes de [tidyverse](https://www.tidyverse.org/) (`dplyr`, `tidyr`) para manipulación de datos
- Aprenda R Markdown o [Quarto](https://quarto.org/) para crear reportes con código R embebido
- Instale la [R Debugger extension](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) para depuración avanzada

## Solución de Problemas

- **"R is not recognized" en la terminal de VS Code**: VS Code no puede encontrar R. Verifique su settings.json (Paso 4) - confirme que la ruta de R es correcta y apunta a `R.exe` (Windows) o al binario de R (Mac/Linux). Ejemplos de rutas:
  - Windows: `C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe` (ajuste el número de versión)
  - macOS Intel: `/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew: `/opt/homebrew/bin/R`
  - Linux: `/usr/bin/R`
  Después de corregir, reinicie VS Code completamente.

- **Discrepancia de versión de R en la configuración**: Si actualizó R pero VS Code todavía usa la versión antigua, actualice el número de versión en su configuración `r.rpath` de settings.json para que coincida con la nueva instalación de R (vea el Paso 3 para encontrar su ruta de instalación actual).

- **La finalización de código no funciona**: Asegúrese de que languageserver se instaló exitosamente (Paso 5). Reinicie VS Code después de la instalación. Espere 10-20 segundos después de abrir un archivo de R para que el servidor de lenguaje se inicialice. Verifique el panel Output (View > Output > R Language Server) para errores.

- **Los gráficos no aparecen**: Los gráficos se abrirán en ventanas separadas usando el dispositivo gráfico predeterminado de R. Asegúrese de tener un gestor de ventanas disponible. En algunos sistemas, puede necesitar instalar X11 (macOS) o asegurar que el soporte gráfico esté habilitado.

- **La aplicación Shiny no se ejecuta**: Asegúrese de que la extensión Shiny esté instalada (Paso 2), el paquete shiny esté instalado (Paso 5), y su archivo se llame `app.R`. Verifique la terminal para mensajes de error. El botón Run solo aparece cuando VS Code reconoce el archivo como una aplicación Shiny.

## Resumen del Flujo de Trabajo

VS Code proporciona una alternativa moderna y liviana a RStudio con estas ventajas clave:

- **Entorno unificado**: Codifique en R, Python, JavaScript y más en un solo editor
- **Personalizable**: Instale solo las extensiones que necesita para una configuración liviana
- **Terminal integrado**: Ejecute R, Git y comandos de shell juntos
- **Desarrollo Shiny**: Lanzamiento de aplicaciones con un clic y recarga automática
- **Control de versiones**: Integración con Git incorporada sin herramientas externas

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
