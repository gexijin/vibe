[Inicio](index.html)

# Use Claude Code para R en VS Code en Mac

Ya configuró R en VS Code y puede escribir código manualmente. Ahora quiere que la IA le ayude a escribir, mejorar y depurar su código R mientras se concentra en el análisis. Piense en Claude Code como un compañero de programación dentro de VS Code: describa lo que necesita y él escribe o mejora el código sin salir de su ventana de trabajo.

## Conceptos Clave

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Extensión de VS Code que integra el asistente de IA Claude directamente en su editor con ediciones de código en línea
- **Chat Panel** - Panel lateral en VS Code donde conversa con Claude sobre su código
- **Inline Edits** - Los cambios de código sugeridos por Claude aparecen directamente en sus archivos con diferencias que puede aceptar o rechazar

## Lo Que Necesitará

- Tutorial [R en VS Code](./R_Coding_VS_Code_Guide) completado - R debe funcionar en VS Code
- Tutorial [Instalación de Claude Code en Mac](./Install_Claude_Code_MacOS) completado - Claude Code CLI instalado
- Suscripción a Claude Pro/Max o clave de API de Anthropic
- 20-30 minutos

## Paso 1: Abra VS Code y Cree un Proyecto de R

- Abra **Visual Studio Code**
- Haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue a su carpeta **Documents**
- Haga clic en **New Folder** en la parte inferior del diálogo
- Nombre la carpeta `claude_r_test`
- Haga clic en **Open** para abrir la nueva carpeta
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**

## Paso 2: Instale e Inicie Sesión en la Extensión de Claude Code

- Haga clic en el ícono de **Extensions** en la barra lateral izquierda (ícono de cuatro cuadrados)
- En el cuadro de búsqueda, escriba `Claude Code`
- Encuentre **Claude Code** de Anthropic y haga clic en **Install**
- Después de la instalación, aparece un ícono de Claude (chispa) en la barra lateral izquierda
- Haga clic en el ícono de Claude para abrir el panel de chat
- Haga clic en **Sign in to Claude Code** en el panel de chat
- Elija su método de autenticación:
  - **Usuarios de Claude Pro/Max**: Haga clic en **Sign in with Claude.ai**, autorice en el navegador y copie el código de vuelta a VS Code
  - **Usuarios de clave de API**: Haga clic en **Use API Key** y pegue su clave de API de Anthropic
- Para pasos detallados de autenticación, consulte la guía [Instalación de Claude Code en Mac](./Install_Claude_Code_MacOS) (Paso 5)
- Una vez iniciada la sesión, verá "Ready to help" en el panel de chat

## Paso 3: Cree un Script de R Inicial Manualmente

- Haga clic en **File > New File** en la barra de menú
- Haga clic en **Select a language** y escriba `R`, luego seleccione **R**
- Guarde el archivo haciendo clic en **File > Save**, nómbrelo `iris_analysis.R`
- Escriba este código:

```r
data(iris)
str(iris)
summary(iris)
```

- Guarde el archivo haciendo clic en **File > Save**
- Abra la terminal de R: haga clic en **View** en la barra de menú, luego en **Command Palette**, escriba `R: Create R Terminal`, presione Enter
- Seleccione el código y presione `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (Mac) para ejecutarlo
- Debería ver la estructura del conjunto de datos y las estadísticas resumidas en la terminal

## Paso 4: Pida a Claude que Agregue un Gráfico de Dispersión

- Haga clic en el ícono de **Claude** en la barra lateral izquierda para abrir el panel de chat
- En el cuadro de chat en la parte inferior, escriba:

```
Agrega código a iris_analysis.R para crear un gráfico de dispersión de longitud vs. ancho del sépalo, coloreado por especie. Usa ggplot2.
```

- Presione Enter para enviar
- Claude lee su archivo y propone cambios: verá una diferencia mostrando el nuevo código a agregar
- Haga clic en **Accept** para aplicar los cambios
- El código de ggplot2 aparece en su archivo
- Si no tiene ggplot2 instalado, ejecute `install.packages("ggplot2")` en la terminal de R

## Paso 5: Ejecute el Código Actualizado

- Seleccione todo el código en `iris_analysis.R`
- Presione `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (Mac)
- Aparece un gráfico de dispersión en una ventana de gráficos separada
- Debería ver puntos coloreados por especie (setosa, versicolor, virginica)

## Paso 6: Pida a Claude que Refine el Gráfico

- En el panel de chat de Claude, escriba:

```
Elimina el título. Cambia el tipo de marcador según la especie. Usa el tema clásico.
```

- Presione Enter
- Claude muestra los cambios de código actualizados
- Haga clic en **Accept**
- Ejecute el código actualizado nuevamente: seleccione todo y presione `Ctrl+Enter` / `Cmd+Enter`
- El gráfico ahora muestra diferentes formas de marcadores por especie, sin título y con el tema clásico

## Paso 7: Pida a Claude un Análisis de PCA

- En el panel de chat de Claude, escriba:

```
Agrega código para realizar un análisis de componentes principales (PCA) sobre las variables numéricas y graficar las muestras usando los dos primeros componentes principales.
```

- Presione Enter
- Claude agrega código de PCA a su script
- Haga clic en **Accept**
- Ejecute todo el código: seleccione todo y presione `Ctrl+Enter` / `Cmd+Enter`
- Aparece un gráfico de PCA mostrando las muestras proyectadas en PC1 y PC2, coloreadas por especie

## Paso 8: Pida a Claude que Revise y Comente

- En el panel de chat de Claude, escriba:

```
Revisa todo el script para verificar que esté correcto. Agrega comentarios donde sea necesario.
```

- Presione Enter
- Claude revisa el código y sugiere comentarios explicando cada sección
- Haga clic en **Accept**
- Su script ahora tiene comentarios claros explicando la carga de datos, la visualización y el análisis de PCA

## Próximos Pasos

- Pida a Claude que cree un informe de R Markdown: "Crea un archivo R Markdown para este análisis"
- Use Claude para depurar errores: "Este código da el Error X, ¿puedes arreglarlo?"
- Solicite pruebas estadísticas: "Agrega una prueba t comparando la longitud del sépalo entre setosa y versicolor"
- Pida a Claude que optimice el código: "Haz este bucle más rápido usando vectorización"
- Obtenga ayuda con funciones desconocidas: "Explica qué hace dplyr::mutate"

## Solución de Problemas

- **La extensión de Claude no se muestra** - Reinicie VS Code después de la instalación. Haga clic en **View > Extensions** para verificar que esté instalada.
- **Error "Cannot read R file"** - Asegúrese de haber guardado el archivo con la extensión `.R`. Claude necesita archivos guardados para leerlos.
- **Error de autenticación** - Verifique que su suscripción a Claude Pro/Max esté activa o que su clave de API sea válida. Consulte [Instalación de Claude Code en Mac](./Install_Claude_Code_MacOS) para solucionar problemas de autenticación.
- **ggplot2 no encontrado** - Instálelo en la terminal de R: `install.packages("ggplot2")`. Espere a que se complete la instalación antes de ejecutar el código.
- **Los cambios de código no se aplican** - Asegúrese de hacer clic en **Accept** en la diferencia. Si no funciona, intente copiar manualmente el código sugerido por Claude.

## Resumen del Flujo de Trabajo

- **Claude Code Extension** proporciona un asistente de IA directamente en VS Code con panel de chat y ediciones en línea
- **Refinamiento iterativo** - Comience con código básico, pida a Claude mejoras, pruebe inmediatamente y refine más
- **Comprensión del contexto** - Claude lee sus archivos de R y entiende la estructura de su proyecto
- **Edición en línea** - Los cambios propuestos aparecen como diferencias en sus archivos reales, no como respuestas de chat separadas
- **Flujo continuo** - No necesita cambiar entre el navegador y el editor: todo ocurre en VS Code

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
