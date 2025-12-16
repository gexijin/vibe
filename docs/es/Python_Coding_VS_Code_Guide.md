[Inicio](index.html)

# Programación en Python con VS Code

Desea escribir código Python pero no está seguro de qué editor usar, o busca algo más ligero que PyCharm. Piense en VS Code como una navaja suiza: maneja Python, R, JavaScript y muchos otros lenguajes en un solo editor ligero. Este tutorial muestra cómo configurar Python en VS Code con características inteligentes como autocompletado de código, depuración interactiva y aplicaciones web.

## Conceptos Clave

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Extensión de VS Code desarrollada por Microsoft que proporciona resaltado de sintaxis, depuración, ejecución de código y soporte para notebooks Jupyter
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Servidor de lenguaje que proporciona IntelliSense rápido, verificación de tipos e importaciones automáticas para Python
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - Entorno Python aislado para gestionar paquetes específicos del proyecto sin afectar el Python del sistema
- **[Streamlit](https://streamlit.io/)** - Biblioteca de Python para crear aplicaciones web interactivas con scripts simples de Python

## Lo Que Necesitará

- Tutorial completado [Primeros Pasos con VS Code](./VS_Code_Getting_Started)
- Conexión a Internet para descargar Python y paquetes
- 15-20 minutos

## Paso 1: Instalar Python

Necesita Python 3.8 o superior para la mejor compatibilidad con paquetes modernos.

- **Windows**:
  - Descargue la última versión de Python desde [python.org](https://www.python.org/downloads/)
  - Ejecute el instalador
  - **Marque la casilla "Add python.exe to PATH"** antes de hacer clic en Install Now
  - Anote la ubicación de instalación (típicamente `C:\Users\YourName\AppData\Local\Programs\Python\Python312`)

- **macOS**:
  - Descargue desde [python.org](https://www.python.org/downloads/) y ejecute el instalador
  - O use Homebrew: abra Terminal y escriba `brew install python`
  - Ruta de Homebrew: `/opt/homebrew/bin/python3` (Apple Silicon) o `/usr/local/bin/python3` (Intel)

- **Linux**:
  - Python generalmente viene preinstalado. Verifique la versión con `python3 --version`
  - Si es necesario, instale vía gestor de paquetes: `sudo apt install python3 python3-pip python3-venv` (Ubuntu/Debian)

Verifique la instalación abriendo una terminal y ejecutando `python3 --version` o `python --version`.

## Paso 2: Instalar Extensiones de Python en VS Code

- Abra VS Code
- Haga clic en el ícono **Extensions** en la barra lateral izquierda (o haga clic en **View > Extensions**)
- Busque `ms-python.python` y haga clic en **Install** en la extensión Python de Microsoft
- Pylance debería instalarse automáticamente con la extensión Python. Si no, busque `ms-python.vscode-pylance` e instálela

La extensión Python incluye soporte para depuración, IntelliSense, formateo de código y notebooks Jupyter.

## Paso 3: Crear Su Proyecto Python

- Cree una nueva carpeta en su computadora (por ejemplo, `my-python-project`)
- En VS Code, haga clic en **File > Open Folder** y seleccione su nueva carpeta
- Haga clic en **File > New File** en el menú superior
- Guarde el archivo como `analysis.py` haciendo clic en **File > Save**

## Paso 4: Seleccionar el Intérprete de Python

VS Code necesita saber qué instalación de Python usar.

- Haga clic en **View** en la barra de menú, luego **Command Palette**
- Escriba `Python: Select Interpreter` y selecciónelo
- Elija la versión de Python que instaló (por ejemplo, `Python 3.12.x` o similar)
- El intérprete seleccionado aparece en la esquina inferior derecha de VS Code

Si no ve su instalación de Python, haga clic en **Enter interpreter path** y navegue hasta donde está instalado Python.

## Paso 5: Crear un Entorno Virtual

Los entornos virtuales mantienen aisladas las dependencias de su proyecto.

- Haga clic en **View** en la barra de menú, luego **Command Palette**
- Escriba `Python: Create Environment` y selecciónelo
- Elija **Venv** (entorno virtual integrado)
- Seleccione su intérprete de Python de la lista
- Espere a que VS Code cree el entorno (verá aparecer una carpeta `.venv`)
- VS Code activará automáticamente este entorno para su proyecto

Verá `(.venv)` en el prompt de su terminal cuando el entorno esté activo.

## Paso 6: Instalar Paquetes Requeridos

- Abra una nueva terminal en VS Code haciendo clic en **View > Terminal**
- La terminal debería mostrar `(.venv)` indicando que su entorno virtual está activo
- Instale paquetes escribiendo estos comandos:

```bash
pip install pandas matplotlib streamlit
```

- Espere a que se complete la instalación (puede tomar 1-2 minutos)

Si `(.venv)` no aparece, el entorno no está activo. Haga clic en **View > Command Palette**, ejecute `Python: Select Interpreter`, luego elija el intérprete con `('.venv': venv)` al lado.

## Paso 7: Escribir Su Primer Script de Python

Escriba este código en `analysis.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# View the first few rows
print(iris.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- Guarde el archivo haciendo clic en **File > Save**

## Paso 8: Ejecutar Código Python Interactivamente

- Con `analysis.py` abierto, haga clic en el botón **▶ Run Python File** en la esquina superior derecha
- O haga clic derecho en el editor y seleccione **Run Python File in Terminal**
- Observe la salida en el panel de terminal
- Aparecerá una ventana de histograma mostrando su gráfico
- También puede seleccionar líneas específicas y presionar `Shift+Enter` para ejecutar solo esas líneas en una sesión interactiva de Python

## Paso 9: Crear una Aplicación Simple de Streamlit

- Cree un nuevo archivo: **File > New File**
- Guárdelo como `app.py`
- Escriba este código:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Sidebar slider
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Load data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Create histogram
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Display in Streamlit
st.pyplot(fig)
```

- Guarde el archivo
- Abra la terminal y ejecute:

```bash
streamlit run app.py
```

- La aplicación se abrirá en su navegador (generalmente en `http://localhost:8501`)
- Mueva el control deslizante en la barra lateral y observe la actualización instantánea del histograma
- Presione `Ctrl+C` en la terminal para detener la aplicación

## Paso 10: Usar Autocompletado de Código e IntelliSense

- En `analysis.py`, comience a escribir `iris.` en una nueva línea
- Aparecerá un menú desplegable con todos los métodos y atributos disponibles
- Escriba `iris.gr` y observe la sugerencia de `groupby()`
- Pase el cursor del mouse sobre `pd.read_csv` en su código existente
- Un popup mostrará la firma de la función, parámetros y documentación
- Intente escribir `import ` y observe las sugerencias de nombres de paquetes de VS Code
- Cuando escribe una llamada a función, IntelliSense muestra sugerencias de parámetros

## Paso 11: Probar la Depuración

- En `analysis.py`, haga clic a la izquierda del número de línea 8 (la línea `print(iris.head())`) para establecer un punto de interrupción (aparecerá un punto rojo)
- Haga clic en **Run** en la barra de menú, luego en **Start Debugging**
- Seleccione **Python File** cuando se le solicite
- La ejecución del código se pausará en el punto de interrupción
- Use la barra de herramientas de depuración para avanzar paso a paso por el código, inspeccionar variables y ver la pila de llamadas
- Haga clic en **Run > Continue** para reanudar la ejecución

## Próximos Pasos

- Explore [pandas](https://pandas.pydata.org/) para manipulación y análisis de datos
- Aprenda sobre [notebooks Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) en VS Code para ciencia de datos interactiva
- Pruebe [Flask](https://flask.palletsprojects.com/) o [FastAPI](https://fastapi.tiangolo.com/) para construir APIs web
- Instale [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) para formateo automático de código
- Use [pytest](https://docs.pytest.org/) para escribir y ejecutar pruebas

## Solución de Problemas

- **"Python is not recognized" en la terminal**: Python no está en su PATH del sistema. En Windows, reinstale Python y marque "Add python.exe to PATH". En Mac/Linux, use `python3` en lugar de `python`. Reinicie VS Code después.

- **No se encuentra el intérprete**: Haga clic en el selector de intérprete en la esquina inferior derecha de VS Code, o en **View > Command Palette** y ejecute `Python: Select Interpreter`. Si su instalación de Python no aparece, seleccione **Enter interpreter path** y navegue hasta su ejecutable de Python.

- **El entorno virtual no se activa**: VS Code debería activarlo automáticamente al abrir una terminal. Si no, active manualmente: Windows: `.venv\Scripts\activate`, Mac/Linux: `source .venv/bin/activate`. Verifique viendo `(.venv)` en el prompt de su terminal.

- **IntelliSense no funciona**: Asegúrese de que Pylance esté instalado y habilitado. Verifique que la esquina inferior derecha muestre su intérprete seleccionado. Espere 10-20 segundos después de abrir un archivo para que Pylance se inicialice. Reinicie VS Code si persisten los problemas.

- **pip install falla**: Asegúrese de que su entorno virtual esté activado (busque `(.venv)` en la terminal). En Linux, podría necesitar instalar `python3-venv` primero. En Windows, verifique que el antivirus no bloquee pip.

- **La aplicación Streamlit no se ejecuta**: Verifique que streamlit esté instalado en su entorno virtual (`pip list | grep streamlit`). Revise la terminal para mensajes de error. Asegúrese de que ninguna otra aplicación use el puerto 8501.

## Resumen del Flujo de Trabajo

VS Code proporciona un entorno moderno y ligero para el desarrollo en Python con estas ventajas:

- **Entorno unificado**: Codifique en Python, R, JavaScript y más en un solo editor
- **IntelliSense potente**: Autocompletados inteligentes, verificación de tipos e importaciones automáticas vía Pylance
- **Depuración integrada**: Establezca puntos de interrupción, inspeccione variables y avance paso a paso por el código
- **Soporte Jupyter**: Ejecute notebooks directamente en VS Code sin aplicaciones separadas
- **Control de versiones**: Integración Git incorporada para seguimiento de cambios
- **Ecosistema de extensiones**: Miles de extensiones para pruebas, formateo, linting y más

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
