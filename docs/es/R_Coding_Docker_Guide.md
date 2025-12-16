[Inicio](index.html)

# Programación en R en VS Code a través de Docker Container

¿Alguna vez intentó compartir su código R con un colega, solo para pasar horas depurando problemas de "pero funciona en mi máquina"? Los contenedores Docker son como contenedores de envío para código: empaquetan su entorno R, bibliotecas y dependencias en una caja sellada que funciona igual en todas partes. Además, tiene acceso a decenas de miles de imágenes preconstruidas en [Docker Hub](https://hub.docker.com/), donde los desarrolladores publican entornos listos para usar, evitando la instalación manual de software. Este tutorial muestra cómo ejecutar R en un entorno aislado y reproducible usando VS Code y Docker Desktop.

## Conceptos Clave

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Aplicación que ejecuta contenedores en su computadora, gestionando entornos aislados
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Función de VS Code que le permite programar dentro de un contenedor Docker con soporte completo del IDE
- **Container Isolation** - Su código se ejecuta en un entorno Linux separado que solo ve su carpeta de proyecto, no toda su computadora
- **[Rocker](https://rocker-project.org/)** - Imágenes Docker preconstruidas diseñadas específicamente para desarrollo en R

## Lo Que Necesitará

- Tutorial [R Coding in VS Code](./R_Coding_VS_Code_Guide) completado
- Tutorial [GitHub Desktop Basics](./Github_desktop) completado
- 20-25 minutos

## Paso 1: Instalar Docker Desktop

- Visite la [página de descarga de Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Haga clic en **Download for Windows** (o Mac/Linux según su sistema)
- Ejecute el instalador y siga el asistente de instalación
- Cuando se le solicite, habilite WSL 2 (usuarios de Windows) o acepte la configuración predeterminada
- Después de la instalación, inicie Docker Desktop
- Espere a que el motor de Docker se inicie (verá un indicador de estado verde en la parte inferior izquierda)

## Paso 2: Instalar la Extensión Dev Containers

- Abra VS Code
- Haga clic en el icono de **Extensions** en la barra lateral izquierda (o haga clic en **View > Extensions**)
- Escriba `dev containers` en el cuadro de búsqueda
- Encuentre **Dev Containers** de Microsoft
- Haga clic en **Install**

## Paso 3: Clonar el Proyecto Vibe con GitHub Desktop

- Abra GitHub Desktop
- Haga clic en **File > Clone repository**
- Haga clic en la pestaña **URL**
- En el campo **Repository URL**, pegue: `https://github.com/gexijin/vibe`
- Elija dónde guardar el proyecto (el campo **Local Path**)
- Haga clic en **Clone**
- GitHub Desktop descargará el proyecto en la ubicación elegida

## Paso 4: Abrir el Proyecto en VS Code

- En VS Code, haga clic en **File > Open Folder**
- Navegue hasta la carpeta `vibe` que acaba de clonar
- Haga clic en **Select Folder**
- Verá los archivos del proyecto en la barra lateral del Explorer

## Paso 5: Reabrir en Contenedor

- Busque una notificación en la parte inferior derecha: **Folder contains a Dev Container configuration file**
- Haga clic en **Reopen in Container**
- Si no ve la notificación, haga clic en el icono verde en la esquina inferior izquierda
- Seleccione **Reopen in Container** del menú
- VS Code construirá el contenedor (esto toma 5-10 minutos la primera vez)
- Verá una notificación de progreso mostrando los pasos de construcción
- Cuando se complete, el icono verde mostrará **Dev Container: R in Docker**

**Nota:** El contenedor incluye automáticamente la extensión R y el paquete languageserver. El Dockerfile y devcontainer.json se encargan de esto por usted.

## Paso 6: Comprender el Entorno del Contenedor

Ahora está programando dentro de un contenedor Linux. Exploremos qué significa esto.

- Haga clic en **Terminal > New Terminal** para abrir una terminal dentro del contenedor
- Verifique su ubicación actual:

```bash
pwd
```

Verá `/workspaces/vibe` - esta es su carpeta de proyecto dentro del contenedor.

- Liste los archivos:

```bash
ls
```

Verá los mismos archivos del proyecto: `R/`, `.devcontainer/`, `README.md`, etc.

- Intente subir un directorio:

```bash
cd ..
ls
```

Solo verá `vibe/` - el contenedor está aislado. No puede acceder a otras carpetas de su computadora, Escritorio o Documentos. Este aislamiento garantiza que su entorno R sea limpio y reproducible.

- Regrese a la carpeta del proyecto:

```bash
cd vibe
```

## Paso 7: Ejecutar Código R Línea por Línea

El contenedor tiene R preinstalado con paquetes comunes. Ejecutemos un script simple de análisis de datos.

- En VS Code Explorer, navegue hasta `R/iris_analysis.R`
- Haga clic para abrir el archivo
- Verá código R que analiza el conjunto de datos iris
- Seleccione la primera línea: `data(iris)`
- Presione `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (Mac) para ejecutarla
- Si no tiene una terminal R abierta, la primera vez crea una, la segunda vez ejecuta el código
- Continue ejecutando cada línea una a la vez
- Cuando ejecute `head(iris)`, verá las primeras 6 filas en la terminal
- Cuando ejecute `summary(iris)`, verá resúmenes estadísticos
- Cuando ejecute los comandos `hist()`, se abrirán gráficos de histograma en ventanas separadas
- También puede seleccionar múltiples líneas y ejecutarlas juntas con `Ctrl+Enter` o `Cmd+Enter`

## Paso 8: Ejecutar la Aplicación

El proyecto incluye una aplicación Shiny de demostración que crea un histograma interactivo.

- En VS Code Explorer, navegue hasta `R/app.R`
- Haga clic para abrir el archivo
- Verá código para una aplicación web Shiny
- Busque en la parte superior derecha de la ventana del editor un botón **▶**
- Haga clic en la flecha desplegable junto a él y seleccione **Run Shiny App**
- La aplicación se iniciará y VS Code reenviará automáticamente el puerto 3838
- Aparece una notificación: **Open in Browser**
- Haga clic en **Open in Browser**
- La aplicación Shiny se abre en su navegador web
- Mueva el control deslizante para cambiar los intervalos del histograma - el gráfico se actualiza en tiempo real

## Paso 9: Hacer un Cambio Simple

Modifiquemos la aplicación para ver cómo funciona el desarrollo.

- Mantenga la aplicación en ejecución
- En VS Code, edite `R/app.R`
- Encuentre la línea 16: `titlePanel("Old Faithful Geyser Data")`
- Cámbiela a:

```r
titlePanel("My First R Docker App")
```

- Guarde el archivo (**File > Save**)
- La extensión Shiny recargará automáticamente la aplicación
- Actualice su navegador (o puede actualizarse automáticamente)
- El título ahora muestra su texto personalizado

## Paso 10: Comprender el Dockerfile (Opcional)

- En VS Code Explorer, navegue hasta `.devcontainer/Dockerfile`
- Haga clic para abrir el archivo
- Verá la configuración completa:

```dockerfile
# choose a Dockerhub base image
FROM rocker/shiny-verse:latest

# 1. System deps commonly needed by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. R packages for VS Code integration: language server + debugger
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Shiny server port
EXPOSE 3838
```

**Partes clave:**

- `FROM rocker/shiny-verse:latest` - Imagen base con R, Shiny y tidyverse preinstalados
- `RUN apt-get install` - Bibliotecas del sistema Linux para paquetes R
- `RUN R -q -e 'install.packages(...)'` - Instala paquetes R permanentemente
- `RUN curl... && apt-get install -y nodejs` - Instala Node.js, necesario para ejecutar Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Instala Claude Code globalmente para asistencia con IA
- `EXPOSE 3838` - Abre el puerto 3838 para aplicaciones Shiny

**Otras imágenes Rocker que puede usar:**

- `rocker/r-ver:4.5.3` - Solo R (versión específica)
- `rocker/rstudio:latest` - R con RStudio Server
- `rocker/tidyverse:latest` - R con paquetes tidyverse
- `rocker/shiny-verse:latest` - R con Shiny y tidyverse (el que estamos usando)

Después de cambiar la imagen base, reconstruya el contenedor para aplicar los cambios.

## Paso 11: Instalar Paquetes R en la Imagen Docker (Opcional)

Los paquetes instalados mediante la consola R (`install.packages()`) son temporales y desaparecen cuando reconstruye el contenedor. Para hacer los paquetes permanentes, agréguelos al Dockerfile.

- En VS Code Explorer, navegue hasta `.devcontainer/Dockerfile`
- Haga clic para abrir el archivo
- Agregue una nueva línea debajo de otras líneas 'install.packages' para instalar el paquete `data.table`:
```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- Guarde el archivo (**File > Save**)
- Haga clic en el icono verde en la esquina inferior izquierda
- Seleccione **Rebuild Container** del menú
- VS Code reconstruirá el contenedor con su nuevo paquete (toma 2-5 minutos)
- Para verificar, abra una terminal R y escriba:

```r
library(data.table)
```

Si se carga sin errores, el paquete está instalado permanentemente.

## Próximos Pasos

- **Crear un nuevo script R** - Haga un nuevo archivo `.R` en la carpeta `R/`, escriba código de análisis de datos usando conjuntos de datos integrados como `mtcars` o `iris`
- **Instalar paquetes R** - Agregue los paquetes que necesite editando el Dockerfile y reconstruyendo el contenedor
- **Explorar tidyverse** - Pruebe la manipulación de datos con `dplyr` y visualización con `ggplot2` usando conjuntos de datos de ejemplo

## Solución de Problemas

- **Docker Desktop no está en ejecución** - Abra Docker Desktop y espere el indicador de estado verde antes de reabrir el contenedor
- **La construcción del contenedor falla** - Verifique su conexión a internet; la primera construcción descarga ~2GB. Haga clic en **Rebuild Container** para reintentar
- **El puerto 3838 ya está en uso** - Detenga otras aplicaciones que usen ese puerto, o cambie el puerto en `.devcontainer/devcontainer.json`

## Resumen del Flujo de Trabajo

Esta configuración proporciona un entorno profesional de desarrollo en R:

- **VS Code** proporciona el editor de código con resaltado de sintaxis e IntelliSense
- **Docker container** ejecuta un entorno Linux aislado con R y todas las dependencias
- **Rocker image** (`rocker/shiny-verse`) incluye R, Shiny, tidyverse y herramientas de desarrollo
- **Dev Container config** (`.devcontainer/`) instala automáticamente extensiones de VS Code para depuración de R y soporte de lenguaje
- **Port forwarding** permite acceder a la aplicación Shiny que se ejecuta dentro del contenedor desde su navegador

## Flujo de Trabajo Diario

Una vez que todo esté configurado, aquí está su rutina diaria:

1. **Iniciar Docker Desktop** - Abra la aplicación y espere el indicador de estado verde (Docker debe estar en ejecución)
2. **Abrir VS Code** - Inicie VS Code y abra su carpeta de proyecto
3. **Reabrir en Contenedor** - Si aún no está en el contenedor, haga clic en el icono verde (inferior izquierdo) y seleccione **Reopen in Container**
4. **Escribir y ejecutar código** - Edite archivos `.R`, ejecute línea por línea con `Ctrl+Enter`/`Cmd+Enter`, o ejecute aplicaciones Shiny con el botón **▶ Run Shiny App**
5. **Guardar su trabajo** - Sus archivos de código (`.R`, `.Rmd`) se guardan en su computadora y persisten entre sesiones
6. **Hacer commit y push** - Use GitHub Desktop para hacer commit de sus cambios y hacer push al repositorio

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
