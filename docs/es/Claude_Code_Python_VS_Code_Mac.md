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
- Suscripción Claude Pro/Max o clave API de Anthropic
- 20-30 minutos

## Paso 1: Abra VS Code y Cree un Proyecto Python

- Abra **Visual Studio Code**
- Haga clic en **File** en la barra de menú, luego en **Open Folder**
- Navegue a su carpeta **Documents**
- Haga clic en **New Folder** en la parte inferior del cuadro de diálogo
- Nombre la carpeta `claude_python_test`
- Haga clic en **Open** para abrir la nueva carpeta
- Si se le pregunta "Do you trust the authors?", haga clic en **Yes, I trust the authors**

## Paso 2: Instale e Inicie Sesión en la Extensión Claude Code

- Haga clic en el ícono **Extensions** en la barra lateral izquierda (ícono de cuatro cuadrados)
- En el cuadro de búsqueda, escriba `Claude Code`
- Encuentre **Claude Code** de Anthropic y haga clic en **Install**
- Después de la instalación, aparece un ícono de Claude (chispa) en la barra lateral izquierda
- Haga clic en el ícono de Claude para abrir el panel de chat
- Haga clic en **Sign in to Claude Code** en el panel de chat
- Elija su método de autenticación:
  - **Usuarios de Claude Pro/Max**: Haga clic en **Sign in with Claude.ai**, autorice en el navegador y copie el código de vuelta a VS Code
  - **Usuarios de clave API**: Haga clic en **Use API Key** y pegue su clave API de Anthropic
- Para pasos detallados de autenticación, consulte la guía [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS) (Paso 5)
- Una vez que haya iniciado sesión, verá "Ready to help" en el panel de chat

## Paso 3: Cree un Script Python Inicial Manualmente

- Haga clic en **File > New File** en la barra de menú
- Haga clic en **Select a language** y escriba `Python`, luego seleccione **Python**
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
print(iris_df.info())
print("\nSummary statistics:")
print(iris_df.describe())
```

- Guarde el archivo haciendo clic en **File > Save**
- Abra el terminal de Python: haga clic en **View** en la barra de menú, luego en **Terminal**
- En el terminal, ejecute: `python iris_analysis.py`
- Debería ver la estructura del conjunto de datos y las estadísticas resumidas en el terminal

## Paso 4: Pídale a Claude que Agregue un Gráfico de Dispersión

- Haga clic en el ícono de **Claude** en la barra lateral izquierda para abrir el panel de chat
- En el cuadro de chat en la parte inferior, escriba:

```
Agrega código a iris_analysis.py para crear un gráfico de dispersión del largo vs. ancho del sépalo, coloreado por especie. Usa seaborn.
```

- Presione Enter para enviar
- Claude lee su archivo y propone cambios: verá una diferencia que muestra el código nuevo para agregar
- Haga clic en **Accept** para aplicar los cambios
- El código de seaborn/matplotlib aparece en su archivo
- Si no tiene los paquetes requeridos, ejecute en el terminal:
  ```
  pip install seaborn matplotlib scikit-learn pandas
  ```

## Paso 5: Ejecute el Código Actualizado

- En el terminal, ejecute: `python iris_analysis.py`
- Aparece una ventana con el gráfico de dispersión
- Debería ver puntos coloreados por especie (setosa, versicolor, virginica)
- Cierre la ventana del gráfico para continuar

## Paso 6: Pídale a Claude que Refine el Gráfico

- En el panel de chat de Claude, escriba:

```
Elimina el título. Cambia el tipo de marcador según la especie. Cambia al estilo whitegrid.
```

- Presione Enter
- Claude muestra los cambios de código actualizados
- Haga clic en **Accept**
- Ejecute el código actualizado nuevamente: `python iris_analysis.py` en el terminal
- El gráfico ahora se muestra con diferentes formas de marcador por especie, sin título y con estilo whitegrid
- Cierre la ventana del gráfico para continuar

## Paso 7: Pídale a Claude un Análisis PCA

- En el panel de chat de Claude, escriba:

```
Agrega código para realizar PCA en las variables numéricas y graficar las muestras usando los dos primeros componentes principales.
```

- Presione Enter
- Claude agrega código PCA a su script
- Haga clic en **Accept**
- Ejecute el código: `python iris_analysis.py` en el terminal
- Aparece un gráfico PCA que muestra las muestras proyectadas en PC1 y PC2, coloreadas por especie
- Cierre la ventana del gráfico cuando termine

## Paso 8: Pídale a Claude que Revise y Comente

- En el panel de chat de Claude, escriba:

```
Revisa todo el script para verificar que esté correcto. Agrega comentarios cuando sea necesario.
```

- Presione Enter
- Claude revisa el código y sugiere comentarios que explican cada sección
- Haga clic en **Accept**
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
- **Falló la autenticación** - Verifique que su suscripción Claude Pro/Max esté activa o que su clave API sea válida. Consulte [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS) para solución de problemas de autenticación.
- **Errores de paquete no encontrado** - Instale los paquetes requeridos en el terminal: `pip install seaborn matplotlib scikit-learn pandas`. Espere a que se complete la instalación antes de ejecutar el código.
- **Los cambios de código no se aplican** - Asegúrese de hacer clic en **Accept** en la diferencia. Si no funciona, intente copiar el código sugerido por Claude manualmente.
- **El gráfico no se muestra** - Asegúrese de tener una pantalla. En algunos sistemas puede necesitar agregar `plt.show()` al final o usar `%matplotlib inline` en Jupyter.

## Resumen del Flujo de Trabajo

- **Claude Code Extension** proporciona un asistente de IA directamente en VS Code con panel de chat y ediciones en línea
- **Refinamiento iterativo** - Comience con código básico, pídale a Claude que lo mejore, pruebe inmediatamente y continúe refinando
- **Conciencia del contexto** - Claude lee sus archivos Python y comprende la estructura de su proyecto
- **Edición en línea** - Los cambios propuestos aparecen como diferencias en sus archivos reales, no como respuestas de chat separadas
- **Permanezca en flujo** - No necesita cambiar entre navegador y editor: todo sucede en VS Code

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
