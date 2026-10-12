---
title: "Uso de Claude Code con RStudio en Windows"
lang: "es"
---
[Inicio](index.html)

# Uso de Claude Code con RStudio en Windows

Tiene RStudio en Windows para ejecutar código R y Claude Code para asistencia de programación con IA. Este tutorial le muestra cómo usar ambas herramientas juntas con los mismos archivos de proyecto. Creará un proyecto R, escribirá código manualmente y luego usará Claude Code desde PowerShell para mejorarlo con visualizaciones y análisis, todo mientras RStudio permanece abierto para ejecutar y probar su código.

## Conceptos Clave

- **PowerShell** - Herramienta de línea de comandos integrada en Windows, que aquí se usa para ejecutar Claude Code junto a RStudio
- **Flujo de trabajo híbrido** - RStudio ejecuta y muestra el código; Claude Code lo escribe y mejora
- **Archivos compartidos** - Ambas herramientas trabajan en la misma carpeta de proyecto, así que los cambios hechos en una aparecen en la otra

## Lo Que Necesitará

- Haber completado la guía [Install Claude Code on Windows](./Install_CLAUDE_Code_Win)
- RStudio instalado en Windows
- 20-30 minutos

## Paso 1: Abrir RStudio en Windows

- Haga clic en el **botón Inicio de Windows**
- Escriba `RStudio` en el cuadro de búsqueda
- Haga clic en **RStudio** para abrirlo
- La ventana de RStudio se abre con múltiples paneles

## Paso 2: Crear un Nuevo Proyecto R

- En RStudio, haga clic en **File** del menú superior
- Haga clic en **New Project...**
- Seleccione **New Directory**
- Seleccione **New Project**
- Para **Directory name**, escriba: `test_claude`
- Haga clic en **Browse** junto a "Create project as subdirectory of:"
- Navegue a su carpeta **Documents**
- Haga clic en **Select Folder**
- Haga clic en **Create Project**
- RStudio crea el proyecto y cambia a él

## Paso 3: Crear un Nuevo Script R

- En RStudio, haga clic en **File > New File > R Script**
- Se abre un nuevo script vacío en el panel superior izquierdo
- Haga clic en **File > Save** (o el icono de guardar)
- Asigne al archivo el nombre: `iris.R`
- Haga clic en **Save**

## Paso 4: Escribir el Código Inicial Manualmente

Escriba este código en su archivo `iris.R`:

```r
data(iris)
str(iris)
summary(iris)
```

- Haga clic en **File > Save** para guardar sus cambios
- Para ejecutar el código: resalte todas las líneas, luego haga clic en el botón **Run** (superior derecho del panel de script)
- Debería ver la salida en el panel Console mostrando la estructura del conjunto de datos y las estadísticas

## Paso 5: Abrir PowerShell

- Haga clic en el **botón Inicio de Windows**
- Escriba `PowerShell` en el cuadro de búsqueda
- Haga clic en **Windows PowerShell** para abrirlo

## Paso 6: Navegar a Su Carpeta de Proyecto

- En PowerShell, escriba:
  ```
  cd ~\Documents\test_claude
  ```
- Verifique que está en la ubicación correcta escribiendo:
  ```
  dir
  ```
- Debería ver `iris.R` y `test_claude.Rproj` listados

## Paso 7: Iniciar Claude Code

- En PowerShell, escriba:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el [tutorial de instalación](./Install_CLAUDE_Code_Win.md). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 8: Solicitar a Claude un Gráfico de Dispersión

Si Claude Code es lento o no responde, simplemente espere a que se inicialice. Luego escriba esta solicitud:

```
Agrega código a iris.R para crear un gráfico de dispersión de longitud de sépalo vs. ancho, coloreado por especie. Usa ggplot2.
```
- Claude Code leerá su archivo `iris.R` y agregará el código de visualización
- Cuando se le solicite, otorgue permiso a Claude para editar el archivo iris.R seleccionando la opción apropiada
- Espere a que Claude termine (verá un mensaje de confirmación)


## Paso 9: Ejecutar el Nuevo Código en RStudio

- Vuelva a RStudio (haga clic en la ventana de RStudio)
- Es posible que vea un aviso indicando que el archivo ha cambiado - haga clic en **Yes** para recargarlo
- Si no aparece ningún aviso, haga clic en **File > Reopen with Encoding > UTF-8**
- Resalte todo el código y haga clic en **Run**
- Aparece un gráfico de dispersión en el panel **Plots** (inferior derecho)
- Si obtiene un error sobre ggplot2, instálelo escribiendo `install.packages("ggplot2")` en el panel Console

## Paso 10: Refinar el Gráfico de Dispersión

- Vuelva a PowerShell
- Escriba esta solicitud:
  ```
  Elimina el título. Cambia el tipo de marcador por especie. Cambia al tema clásico.
  ```

## Paso 11: Ver el Gráfico Refinado

- Vuelva a RStudio
- Recargue el archivo si se le solicita
- Resalte el código actualizado y haga clic en **Run**
- El gráfico ahora debería mostrarse sin título, con formas de marcador diferentes para cada especie y usando el tema clásico


## Paso 12: Solicitar a Claude un Gráfico PCA

- Vuelva a PowerShell
- Escriba esta solicitud:
  ```
  Agrega código para realizar PCA en las variables numéricas y graficar las muestras usando los dos primeros componentes principales.
  ```

## Paso 13: Ejecutar el Análisis PCA

- Vuelva a RStudio
- Recargue el archivo si se le solicita
- Resalte todo el código y haga clic en **Run**
- Aparece un gráfico PCA mostrando las muestras proyectadas en PC1 y PC2, coloreadas por especie

## Paso 14: Solicitar a Claude que Revise y Comente

- Vuelva a PowerShell
- Escriba esta solicitud:
  ```
  Revisa todo el script para verificar que sea correcto. Agrega comentarios cuando sea necesario.
  ```
- Claude revisará el código y agregará comentarios detallados

## Paso 15: Solicitar a Claude que Cree R Markdown

- Vuelva a PowerShell
- Escriba esta solicitud:
  ```
  Crea un nuevo archivo R Markdown para este análisis. Guárdalo como iris_report.Rmd
  ```
- Claude le pedirá permiso para crear este archivo
- Claude creará un nuevo archivo `.Rmd` en su carpeta de proyecto


## Paso 16: Compilar el Archivo R Markdown

- Vuelva a RStudio
- Haga clic en **File > Open File...**
- Seleccione `iris_report.Rmd` y haga clic en **Open**
- Haga clic en el botón **Knit** (con un icono de ovillo de lana) en la parte superior del panel de script
- RStudio generará un informe HTML
- El informe se abre en una nueva ventana mostrando su análisis completo con texto narrativo
- El archivo HTML se guarda en su carpeta de proyecto

## Solución de Problemas

- **RStudio no muestra los cambios en el archivo** - Haga clic en **File > Reopen with Encoding > UTF-8** para recargar el archivo manualmente.
- **"claude: command not found"** - Asegúrese de haber completado la guía de instalación. Intente abrir una nueva ventana de PowerShell.
- **Los gráficos no aparecen** - Asegúrese de que ggplot2 esté instalado. Ejecute `install.packages("ggplot2")` en la Console de RStudio si es necesario.
- **Error: "cannot change working directory"** - Su ruta de Windows contiene espacios. En el Paso 6, envuelva la ruta entre comillas: `cd "~\Documents\Su Nombre\test_claude"`
- **Claude Code es lento en la primera solicitud** - Espere 30-60 segundos para que Claude se inicialice. Las solicitudes posteriores serán más rápidas.
- **¿Usa WSL?** - Si configuró la ruta opcional de WSL/Ubuntu, abra la aplicación **Ubuntu** en lugar de PowerShell en los Pasos 5-16 y navegue a su proyecto con `cd /mnt/c/Users/SuNombreDeUsuario/Documents/test_claude`

## Próximos Pasos

- Intente solicitar a Claude que agregue pruebas estadísticas (pruebas t, ANOVA) a su análisis
- Solicite a Claude que cree una **versión Python** de este código y prepare un documento Quarto
- Solicite a Claude que cree funciones para tareas repetitivas en sus scripts R
- Use Claude para depurar mensajes de error cuando su código R no funcione
- Explore solicitar a Claude que optimice código R lento para mejorar el rendimiento

## Resumen del Flujo de Trabajo

Esta configuración híbrida combina lo mejor de ambos mundos:

- **RStudio** - Consola R interactiva, visualización inmediata de gráficos, interfaz gráfica familiar para ejecutar código
- **Claude Code (PowerShell)** - Generación de código con IA, revisión y mejora
- **Archivos compartidos** - Ambas herramientas trabajan directamente en la misma carpeta de proyecto
- **Refinamiento iterativo** - Comience con código manual, mejore con Claude, pruebe en RStudio y refine más
- **Documentación** - Claude puede generar informes detallados y comentarios para su análisis

El flujo de trabajo es simple: escriba o edite código con Claude en PowerShell, luego pruébelo y ejecútelo inmediatamente en RStudio. No necesita copiar archivos ni sincronización manual: ambas herramientas comparten los mismos archivos.

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2025.
