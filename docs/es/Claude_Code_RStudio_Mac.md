[Inicio](index.html)

# Uso de Claude Code con RStudio en Mac

Tiene RStudio en Mac para ejecutar código R y Claude Code para asistencia de codificación con IA. Este tutorial muestra cómo usar ambas herramientas juntas en los mismos archivos de proyecto. Creará un proyecto R, escribirá código manualmente y luego usará Claude Code desde Terminal para mejorarlo con visualizaciones y análisis, todo mientras RStudio permanece abierto para ejecutar y probar su código.

## Conceptos Clave

- **Terminal** - Interfaz de línea de comandos de Mac donde se ejecuta Claude Code
- **Archivos compartidos** - Tanto RStudio como Claude Code trabajan en los mismos archivos en su carpeta Documentos
- **Flujo de trabajo híbrido** - RStudio ejecuta el código; Claude Code lo escribe y lo mejora

## Lo Que Necesitará

- Guía [Install Claude Code on Mac](./Install_Claude_Code_MacOS) completada
- RStudio instalado en Mac
- 20-30 minutos

## Paso 1: Abrir RStudio en Mac

- Haga clic en **Launchpad** en su Dock (el ícono de cuadrícula de puntos)
- Escriba `RStudio` en el cuadro de búsqueda
- Haga clic en **RStudio** para abrirlo
- La ventana de RStudio se abre con múltiples paneles

## Paso 2: Crear un Nuevo Proyecto R

- En RStudio, haga clic en **File** desde el menú superior
- Haga clic en **New Project...**
- Seleccione **New Directory**
- Seleccione **New Project**
- Para **Directory name**, escriba: `test_claude`
- Haga clic en **Browse** junto a "Create project as subdirectory of:"
- Navegue hasta su carpeta **Documents**
- Haga clic en **Open**
- Haga clic en **Create Project**
- RStudio crea el proyecto y cambia a él

## Paso 3: Crear un Nuevo Script R

- En RStudio, haga clic en **File > New File > R Script**
- Se abre un nuevo script vacío en el panel superior izquierdo
- Haga clic en **File > Save** (o presione **Command (⌘) + S**)
- Nombre el archivo: `iris.R`
- Haga clic en **Save**

## Paso 4: Escribir el Código Inicial Manualmente

Escriba este código en su archivo `iris.R`:

```r
data(iris)
str(iris)
summary(iris)
```

- Haga clic en **File > Save** para guardar sus cambios (o presione **Command (⌘) + S**)
- Para ejecutar el código: resalte todas las líneas, luego haga clic en el botón **Run** (parte superior derecha del panel del script)
- Debería ver resultados en el panel Console mostrando la estructura del conjunto de datos y estadísticas

## Paso 5: Abrir Terminal

- Abra **Finder** y haga clic en **Applications** en la barra lateral izquierda
- Abra la carpeta **Utilities**
- Haga doble clic en **Terminal**
- La ventana de Terminal se abre

## Paso 6: Navegar a su Carpeta de Proyecto

- En Terminal, escriba este comando:
  ```
  cd ~/Documents/test_claude
  ```
- Verifique que está en la ubicación correcta escribiendo:
  ```
  ls
  ```
- Debería ver `iris.R` y `test_claude.Rproj` listados

**Consejo:** Si no está seguro de la ruta exacta, puede arrastrar y soltar la carpeta desde Finder a Terminal y la ruta completa aparecerá automáticamente.

## Paso 7: Iniciar Claude Code

- En Terminal, escriba:
  ```
  claude
  ```
- Claude Code se inicia y muestra un mensaje de bienvenida
- Es posible que necesite autenticarse si esta es su primera sesión
- Ahora está listo para usar asistencia de IA para su proyecto R

## Paso 8: Solicitar a Claude un Gráfico de Dispersión

Si Claude Code es lento o no responde, simplemente espere a que se inicialice. Luego escriba esta solicitud:

```
Agrega código a iris.R para crear un gráfico de dispersión de longitud vs. ancho del sépalo, coloreado por especie. Usa ggplot2.
```
- Claude Code leerá su archivo `iris.R` y agregará el código de visualización
- Cuando se le solicite, otorgue permiso a Claude para editar el archivo iris.R seleccionando la opción apropiada
- Espere a que Claude termine (verá un mensaje de confirmación)


## Paso 9: Ejecutar el Nuevo Código en RStudio

- Cambie de nuevo a RStudio (haga clic en la ventana de RStudio o presione **Command (⌘) + Tab**)
- Puede ver un mensaje diciendo que el archivo ha cambiado - haga clic en **Yes** para recargar
- Si no aparece ningún mensaje, haga clic en **File > Reopen with Encoding > UTF-8**
- Resalte todo el código y haga clic en **Run**
- Un gráfico de dispersión aparece en el panel **Plots** (parte inferior derecha)
- Si obtiene un error sobre ggplot2, instálelo escribiendo `install.packages("ggplot2")` en el panel Console

## Paso 10: Refinar el Gráfico de Dispersión

- Cambie a Terminal (presione **Command (⌘) + Tab** o haga clic en la ventana de Terminal)
- Escriba esta solicitud:
  ```
  Elimina el título. Cambia el tipo de marcador según la especie. Usa el tema clásico.
  ```

## Paso 11: Ver el Gráfico Refinado

- Cambie a RStudio
- Recargue el archivo si se le solicita
- Resalte el código actualizado y haga clic en **Run**
- El gráfico ahora debería mostrarse sin título, con diferentes formas de marcadores para cada especie y usando el tema clásico


## Paso 12: Solicitar a Claude un Gráfico PCA

- Cambie a Terminal
- Escriba esta solicitud:
  ```
  Agrega código para realizar un análisis de componentes principales (PCA) sobre las variables numéricas y graficar las muestras usando los dos primeros componentes principales.
  ```

## Paso 13: Ejecutar el Análisis PCA

- Cambie a RStudio
- Recargue el archivo si se le solicita
- Resalte todo el código y haga clic en **Run**
- Aparece un gráfico PCA mostrando muestras proyectadas en PC1 y PC2, coloreadas por especie

## Paso 14: Solicitar a Claude Revisar y Comentar

- Cambie a Terminal
- Escriba esta solicitud:
  ```
  Revisa todo el script para verificar que esté correcto. Agrega comentarios donde sea necesario.
  ```
- Claude revisará el código y agregará comentarios completos

## Paso 15: Solicitar a Claude Crear R Markdown

- Cambie a Terminal
- Escriba esta solicitud:
  ```
  Crea un nuevo archivo R Markdown para este análisis. Guárdalo como iris_report.Rmd
  ```
- Claude le pedirá permiso para crear este archivo
- Claude creará un nuevo archivo `.Rmd` en su carpeta de proyecto


## Paso 16: Compilar el Archivo R Markdown

- Cambie a RStudio
- Haga clic en **File > Open File...**
- Seleccione `iris_report.Rmd` y haga clic en **Open**
- Haga clic en el botón **Knit** (con un ícono de ovillo de lana) en la parte superior del panel del script
- RStudio generará un reporte HTML
- El reporte se abre en una nueva ventana mostrando su análisis completo con texto narrativo
- El archivo HTML se guarda en su carpeta de proyecto

## Solución de Problemas

- **RStudio no muestra los cambios del archivo** - Haga clic en **File > Reopen with Encoding > UTF-8** para recargar manualmente el archivo, o cierre y vuelva a abrir el archivo.
- **"claude: command not found"** - Asegúrese de haber completado la [guía de instalación](./Install_Claude_Code_MacOS). Intente abrir una nueva ventana de Terminal, o cierre Terminal completamente (**Command (⌘) + Q**) y vuelva a abrirlo.
- **Los gráficos no aparecen** - Asegúrese de que ggplot2 esté instalado. Ejecute `install.packages("ggplot2")` en la consola de RStudio si es necesario.
- **"No such file or directory"** - Verifique que escribió la ruta correctamente en el Paso 6. Intente usar el truco de arrastrar y soltar: arrastre la carpeta test_claude desde Finder a Terminal después de escribir `cd ` (con un espacio).
- **Claude Code es lento en la primera solicitud** - Espere 30-60 segundos para que Claude se inicialice. Las solicitudes posteriores serán más rápidas.

## Atajos de Teclado de Mac

Atajos útiles para cambiar entre aplicaciones:
- **Command (⌘) + Tab** - Cambiar entre aplicaciones abiertas rápidamente
- **Command (⌘) + `** (acento grave) - Cambiar entre ventanas de la misma aplicación
- **Command (⌘) + Space** - Abrir búsqueda Spotlight (para abrir aplicaciones)
- **Command (⌘) + Q** - Salir de una aplicación completamente

## Próximos Pasos

- Pida a Claude que agregue pruebas estadísticas (pruebas t, ANOVA) a su análisis
- Solicite a Claude una **versión Python** de este código y preparar un documento Quarto
- Solicite a Claude crear funciones para tareas repetitivas en sus scripts R
- Use Claude para depurar mensajes de error cuando su código R no funcione
- Pida a Claude que optimice código R lento para mejor rendimiento

## Resumen del Flujo de Trabajo

Esta configuración híbrida combina lo mejor de ambos mundos:

- **RStudio (Mac)** - Consola R interactiva, visualización inmediata de gráficos, interfaz familiar para ejecutar código
- **Claude Code (Terminal)** - Generación, revisión y mejora de código impulsada por IA
- **Archivos compartidos** - Ambas herramientas trabajan en los mismos archivos de su carpeta Documentos
- **Refinamiento iterativo** - Comience con código manual, mejore con Claude, pruebe en RStudio y refine más
- **Documentación** - Claude puede generar reportes y comentarios completos para su análisis

El flujo de trabajo es simple: escriba o edite código con Claude en Terminal, luego pruébelo y ejecútelo inmediatamente en RStudio. No necesita copiar archivos ni sincronización manual: ambas aplicaciones acceden a los mismos archivos sin problemas en su Mac.

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2024.
