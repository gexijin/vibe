---
title: "Use Claude Code para Python en VS Code en Mac"
lang: "es"
---
[Inicio](index.html)

# Use Claude Code para Python en VS Code en Mac

Ha configurado Python en VS Code y puede escribir código manualmente. Ahora desea que la IA lo ayude a escribir, mejorar y depurar su código Python mientras se enfoca en el análisis. Piense en Claude Code como un compañero de programación que vive dentro de VS Code: describa lo que desea y Claude Code escribe o mejora el código mientras permanece en la misma ventana.

## Conceptos Clave

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Extensión de VS Code que trae el asistente de IA Claude directamente a su editor con ediciones de código en línea
- **Chat Panel** - Panel lateral en VS Code donde conversa con Claude sobre su código
- **Inline Edits** - Los cambios de código sugeridos por Claude aparecen directamente en sus archivos con diferencias que puede aceptar o rechazar

## Lo Que Necesitará

- Tutorial completado [Programación en Python con VS Code](./Python_Coding_VS_Code_Guide) - Python debe estar funcionando en VS Code
- Tutorial completado [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS) - Claude Code CLI debe estar instalado
- Un plan de pago de Claude (como Pro o Max) o una cuenta de Anthropic Console; el plan gratuito no incluye Claude Code
- 20-30 minutos

## Paso 1: Abra VS Code y Cree un Proyecto Python

- Abra **Visual Studio Code**
- Haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue a su carpeta **Documentos**
- Haga clic en **New Folder** en la parte inferior del cuadro de diálogo
- Nombre la carpeta `claude_python_test`
- Haga clic en **Open** para abrir la nueva carpeta
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**

## Paso 2: Instale e Inicie Sesión en la Extensión Claude Code

- Haga clic en el ícono **Extensions** en la barra lateral izquierda (ícono de cuatro cuadrados)
- En el cuadro de búsqueda, escriba `Claude Code`
- Encuentre **Claude Code for VS Code** de Anthropic y haga clic en **Install**
- Después de la instalación, haga clic en **✻ Claude Code** en la esquina inferior derecha de la ventana de VS Code (la barra de estado) para abrir el panel de Claude
- La primera vez aparece una pantalla de inicio de sesión: haga clic en **Sign in**, apruebe el acceso en su navegador y luego vuelva a VS Code
- Para pasos detallados de autenticación, consulte la guía [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS) (Paso 3)
- Una vez que haya iniciado sesión, verá una lista de verificación **Learn Claude Code** y un cuadro de prompt en la parte inferior del panel

## Paso 3: Cree un Script Python Inicial Manualmente

- Haga clic en **File > New File...** en la barra de menú
- En la lista que aparece en la parte superior de la ventana, elija **Python File**
- Guarde el archivo haciendo clic en **File > Save**, nómbrelo `iris_analysis.py`
- Escriba este código:

```python
from sklearn import datasets
import pandas as pd

# Load iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display structure
iris_df.info()
print("\nSummary statistics:")
print(iris_df.describe())
```

- Guarde el archivo haciendo clic en **File > Save**
- Cree un entorno virtual, como en el Paso 5 de [Programación en Python con VS Code](./Python_Coding_VS_Code_Guide): haga clic en **View > Command Palette**, escriba `Python: Create Environment`, elija **Venv** y luego seleccione su versión de Python
- Espere a que aparezca la carpeta `.venv` en el Explorer
- Abra una terminal: haga clic en **View** en la barra de menú, luego en **Terminal**. Debería ver `(.venv)` al inicio del prompt
- Instale los paquetes que necesita este script:
  ```
  pip install scikit-learn pandas
  ```
- En la terminal, ejecute: `python iris_analysis.py`
- Debería ver la estructura del conjunto de datos y las estadísticas resumidas en la terminal

## Paso 4: Pídale a Claude que Agregue un Gráfico de Dispersión

- Abra el panel de Claude (ícono Spark en la parte superior derecha del archivo abierto, o **✻ Claude Code** en la esquina inferior derecha)
- En el cuadro de chat en la parte inferior, escriba:

```
Agrega código a iris_analysis.py para crear un gráfico de dispersión del largo vs. ancho del sépalo, coloreado por especie. Usa seaborn.
```

- Presione Enter para enviar
- Claude lee su archivo y lo edita: el código nuevo aparece en `iris_analysis.py`
- Si Claude muestra una diferencia y pide permiso, acepte el cambio
- El código de seaborn/matplotlib aparece en su archivo
- Instale los paquetes de gráficos que usa el código de Claude (no se instalaron en el Paso 3). En la terminal (con `(.venv)` visible), ejecute:
  ```
  pip install seaborn matplotlib
  ```

## Paso 5: Ejecute el Código Actualizado

- En la terminal, ejecute: `python iris_analysis.py`
- Aparece una ventana con el gráfico de dispersión
- Debería ver puntos coloreados por especie (setosa, versicolor, virginica)
- Cierre la ventana del gráfico para continuar

## Paso 6: Pídale a Claude que Refine el Gráfico

- En el panel de chat de Claude, escriba:

```
Elimina el título. Cambia el tipo de marcador según la especie. Cambia al estilo whitegrid.
```

- Presione Enter
- Claude actualiza el código
- Si se le pide, acepte el cambio
- Ejecute el código actualizado nuevamente: `python iris_analysis.py` en la terminal
- El gráfico ahora se muestra con diferentes formas de marcador por especie, sin título y con estilo whitegrid
- Cierre la ventana del gráfico para continuar

## Paso 7: Pídale a Claude un Análisis PCA

- En el panel de chat de Claude, escriba:

```
Agrega código para realizar PCA en las variables numéricas y graficar las muestras usando los dos primeros componentes principales.
```

- Presione Enter
- Claude agrega código PCA a su script
- Si se le pide, acepte el cambio
- Ejecute el código: `python iris_analysis.py` en la terminal
- Aparece un gráfico PCA que muestra las muestras proyectadas en PC1 y PC2, coloreadas por especie (si primero se abre la ventana del gráfico de dispersión del Paso 6, ciérrela y a continuación aparecerá el gráfico PCA)
- Cierre la ventana del gráfico cuando termine

## Paso 8: Pídale a Claude que Revise y Comente

- En el panel de chat de Claude, escriba:

```
Revisa todo el script para verificar que esté correcto. Agrega comentarios cuando sea necesario.
```

- Presione Enter
- Claude revisa el código y agrega comentarios que explican cada sección
- Si se le pide, acepte el cambio
- Su script ahora tiene comentarios claros que explican la carga de datos, la visualización y el análisis PCA

## Próximos Pasos

- Pídale a Claude que cree un notebook Jupyter: "Convierte esto a un notebook Jupyter"
- Use Claude para depurar errores: "Este código genera el error X, ¿puedes corregirlo?"
- Solicite pruebas estadísticas: "Agrega una prueba t comparando el largo del sépalo entre setosa y versicolor"
- Pídale a Claude que optimice el código: "Haz este código más eficiente usando vectorización de numpy"
- Obtenga ayuda con funciones desconocidas: "Explica qué hace pandas.groupby"

## Solución de Problemas

- **La extensión Claude no se muestra** - Reinicie VS Code después de la instalación. Haga clic en **View > Extensions** para verificar que esté instalada.
- **Error "Cannot read Python file"** - Asegúrese de haber guardado el archivo con extensión `.py`. Claude necesita archivos guardados para leerlos.
- **Falló la autenticación** - Verifique que su plan de pago de Claude o su cuenta de Anthropic Console esté activa. Consulte [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS) para solución de problemas de autenticación.
- **Errores de paquete no encontrado** o **`command not found: python`** - Asegúrese de que la terminal muestre `(.venv)` (si no, ciérrela y abra una nueva con **View > Terminal**) y luego instale los paquetes requeridos: `pip install seaborn matplotlib scikit-learn pandas`. Espere a que se complete la instalación antes de ejecutar el código.
- **Los cambios de código no se aplican** - Si Claude pidió permiso, asegúrese de haber aceptado el cambio. Si no funciona, intente copiar el código sugerido por Claude manualmente.
- **El gráfico no se muestra** - Asegúrese de tener una pantalla. En algunos sistemas puede necesitar agregar `plt.show()` al final o usar `%matplotlib inline` en Jupyter.

## Resumen del Flujo de Trabajo

- **Claude Code Extension** proporciona un asistente de IA directamente en VS Code con panel de chat y ediciones en línea
- **Refinamiento iterativo** - Comience con código básico, pídale a Claude que lo mejore, pruebe inmediatamente y continúe refinando
- **Conciencia del contexto** - Claude lee sus archivos Python y comprende la estructura de su proyecto
- **Edición en línea** - Los cambios propuestos aparecen como diferencias en sus archivos reales, no como respuestas de chat separadas
- **Permanezca en flujo** - No necesita cambiar entre navegador y editor: todo sucede en VS Code

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2025.
