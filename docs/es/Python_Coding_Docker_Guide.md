[Inicio](index.html)

# Codificación en Python con VS Code mediante Contenedor Docker

¿Alguna vez intentó compartir su código Python con un colega solo para pasar horas depurando problemas del tipo "funciona en mi máquina"? Los contenedores Docker son como contenedores de envío para código: empaquetan su entorno Python, bibliotecas y dependencias en una caja sellada que funciona igual en todas partes. Además, obtiene acceso a decenas de miles de imágenes preconstruidas en [Docker Hub](https://hub.docker.com/), donde los desarrolladores publican entornos listos para usar, evitando la instalación manual de software. Este tutorial muestra cómo ejecutar Python en un entorno aislado y reproducible usando VS Code y Docker Desktop.

## Conceptos Clave

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Aplicación que ejecuta contenedores en su computadora, administrando entornos aislados
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Función de VS Code que permite codificar dentro de un contenedor Docker con soporte completo del IDE
- **Container Isolation** - Su código se ejecuta en un entorno Linux separado que solo ve su carpeta de proyecto, no toda su computadora
- **[Python Official Images](https://hub.docker.com/_/python)** - Imágenes Docker preconstruidas con Python y herramientas esenciales preinstaladas

## Lo Que Necesitará

- Haber completado [Programación en Python con VS Code](./Python_Coding_VS_Code_Guide)
- 20-25 minutos

## Paso 1: Instalar Docker Desktop

- Visite la [página de descarga de Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Haga clic en **Download for Windows** (o Mac/Linux según su sistema)
- Ejecute el instalador y siga el asistente de instalación
- Cuando se le solicite, habilite WSL 2 (usuarios de Windows) o acepte la configuración predeterminada
- Después de la instalación, inicie Docker Desktop
- Espere a que el motor de Docker se inicie (verá un indicador de estado verde en la esquina inferior izquierda)

## Paso 2: Instalar la Extensión Dev Containers

- Abra VS Code
- Haga clic en el icono **Extensions** en la barra lateral izquierda (o haga clic en **View > Extensions**)
- Escriba `dev containers` en el cuadro de búsqueda
- Encuentre **Dev Containers** de Microsoft
- Haga clic en **Install**

## Paso 3: Crear una Carpeta de Proyecto Python

- Cree una nueva carpeta en su computadora llamada `python-docker-demo`
- Dentro de ella, cree una subcarpeta llamada `.devcontainer`
- Dentro de ella, cree una subcarpeta llamada `python`
- Su estructura debería verse así: `python-docker-demo/.devcontainer/` y `python-docker-demo/python/`

## Paso 4: Crear el Dockerfile

- En VS Code, haga clic en **File > Open Folder**
- Navegue a la carpeta `python-docker-demo` que acaba de crear
- Haga clic en **Select Folder**
- En la barra lateral Explorer, haga clic derecho en la carpeta `.devcontainer`
- Haga clic en **New File**
- Nómbrelo `Dockerfile`
- Pegue el siguiente contenido:

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- Haga clic en **File > Save**

## Paso 5: Crear la Configuración del Dev Container

- En la carpeta `.devcontainer`, cree un nuevo archivo llamado `devcontainer.json`
- Pegue el siguiente contenido:

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- Haga clic en **File > Save**

## Paso 6: Crear un Script de Análisis de Datos en Python

- En la carpeta `python`, cree un nuevo archivo llamado `iris_analysis.py`
- Pegue el siguiente contenido:

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.show()
```

- Haga clic en **File > Save**

## Paso 7: Crear una Aplicación Web Streamlit

- En la carpeta `python`, cree un nuevo archivo llamado `app.py`
- Pegue el siguiente contenido:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- Haga clic en **File > Save**

## Paso 8: Reabrir en Contenedor

- Haga clic en el icono verde en la esquina inferior izquierda de VS Code
- Seleccione **Reopen in Container** del menú
- VS Code construirá el contenedor (esto toma de 5 a 10 minutos la primera vez)
- Verá una notificación de progreso mostrando los pasos de construcción
- Cuando esté completo, el icono verde mostrará **Dev Container: Python in Docker**

## Paso 9: Comprender el Entorno del Contenedor

Ahora está codificando dentro de un contenedor Linux. Exploremos lo que esto significa.

- Haga clic en **Terminal > New Terminal** para abrir una terminal dentro del contenedor
- Verifique su ubicación actual:

```bash
pwd
```

Verá `/workspaces/python-docker-demo` - esta es su carpeta de proyecto dentro del contenedor.

- Liste los archivos:

```bash
ls
```

Verá las carpetas que creó: `.devcontainer/`, `python/`, etc.

- Intente subir un directorio:

```bash
cd ..
ls
```

Solo verá `python-docker-demo/` - el contenedor está aislado. No puede acceder a otras carpetas de su computadora, Escritorio o Documentos. Este aislamiento garantiza que su entorno Python sea limpio y reproducible.

- Regrese a la carpeta del proyecto:

```bash
cd python-docker-demo
```

## Paso 10: Ejecutar Código Python Línea por Línea

El contenedor tiene Python preinstalado con paquetes de ciencia de datos. Ejecutemos el script de análisis.

- En VS Code Explorer, navegue a `python/iris_analysis.py`
- Haga clic para abrir el archivo
- Seleccione la primera línea: `import pandas as pd`
- Presione `Shift+Enter` para ejecutarla en una terminal Python interactiva
- Se abre una terminal Python en la parte inferior
- Continúe ejecutando cada línea o bloque uno a la vez con `Shift+Enter`
- Cuando ejecute `print(df.head())`, verá las primeras 5 filas en la terminal
- Cuando ejecute `print(df.describe())`, verá resúmenes estadísticos
- Cuando ejecute el código del histograma, se abrirá una ventana de gráfico mostrando la visualización

## Paso 11: Ejecutar la Aplicación Streamlit

El proyecto incluye una aplicación Streamlit de demostración que crea un histograma interactivo.

- En VS Code Explorer, navegue a `python/app.py`
- Haga clic para abrir el archivo
- Abra una nueva terminal (**Terminal > New Terminal**)
- Ejecute la aplicación:

```bash
cd python
streamlit run app.py
```

- La aplicación se iniciará y mostrará una URL: `http://localhost:8501`
- Aparece una notificación: **Open in Browser**
- Haga clic en **Open in Browser**
- La aplicación Streamlit se abre en su navegador web
- Mueva el deslizador para cambiar los contenedores del histograma - el gráfico se actualiza en tiempo real

## Paso 12: Hacer un Cambio Sencillo

Modifiquemos la aplicación para ver cómo funciona el desarrollo.

- Mantenga la aplicación ejecutándose
- En VS Code, edite `python/app.py`
- Encuentre la línea 6: `st.title("Old Faithful Geyser Data")`
- Cámbiela a:

```python
st.title("My First Python Docker App")
```

- Haga clic en **File > Save**
- Regrese a su navegador
- Haga clic en **Always rerun** en la esquina superior derecha
- El título ahora muestra su texto personalizado

## Paso 13: Comprender el Dockerfile (Opcional)

- En VS Code Explorer, navegue a `.devcontainer/Dockerfile`
- Haga clic para abrir el archivo
- Verá la configuración completa

**Partes clave:**

- `FROM python:3.12-slim` - Imagen base oficial de Python 3.12 (basada en Debian, ligera)
- `RUN apt-get install` - Bibliotecas del sistema Linux para construir paquetes Python
- `RUN pip install --no-cache-dir ...` - Instala permanentemente paquetes Python
- `RUN curl... && apt-get install -y nodejs` - Instala Node.js, requerido para ejecutar Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Instala Claude Code globalmente para asistencia de IA
- `EXPOSE 8501` - Abre el puerto 8501 para aplicaciones Streamlit

**Otras imágenes Python que puede usar:**

- `python:3.12` - Imagen Python completa con más herramientas (tamaño mayor)
- `python:3.12-slim` - Imagen ligera con Python y pip (la que estamos usando)
- `python:3.12-alpine` - Imagen mínima basada en Alpine Linux (tamaño más pequeño)
- `jupyter/datascience-notebook` - Jupyter preconfigurado con bibliotecas de ciencia de datos

Después de cambiar la imagen base, reconstruya el contenedor para aplicar los cambios.

## Paso 14: Instalar Paquetes Python en la Imagen Docker (Opcional)

Los paquetes instalados mediante pip en la terminal (`pip install package`) son temporales y desaparecen cuando reconstruye el contenedor. Para hacer permanentes los paquetes, agréguelos al Dockerfile.

- En VS Code Explorer, navegue a `.devcontainer/Dockerfile`
- Haga clic para abrir el archivo
- Encuentre la línea 9: `RUN pip install --no-cache-dir ...`
- Agregue `scikit-learn` a la lista:

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- Haga clic en **File > Save**
- Haga clic en el icono verde en la esquina inferior izquierda
- Seleccione **Rebuild Container** del menú
- VS Code reconstruirá el contenedor con su nuevo paquete (esto toma de 2 a 5 minutos)
- Para verificar, abra una terminal Python y escriba:

```python
import sklearn
print(sklearn.__version__)
```

Si muestra la versión sin errores, el paquete está instalado permanentemente.

## Próximos Pasos

- **Crear un nuevo script Python** - Haga un nuevo archivo `.py` en la carpeta `python/`, escriba código de análisis de datos usando conjuntos de datos incorporados o cargue sus propios archivos CSV
- **Instalar paquetes Python** - Agregue los paquetes que necesite editando el Dockerfile (línea 9) y reconstruyendo el contenedor
- **Explorar ciencia de datos** - Pruebe la manipulación de datos con pandas y la visualización con matplotlib o seaborn
- **Construir aplicaciones web** - Cree paneles interactivos con Streamlit o Flask

## Solución de Problemas

- **Docker Desktop no está ejecutándose** - Abra Docker Desktop y espere el indicador de estado verde antes de reabrir el contenedor
- **Falla la construcción del contenedor** - Verifique su conexión a Internet; la primera construcción descarga imágenes y paquetes. Haga clic en **Rebuild Container** para reintentar
- **Puerto 8501 ya en uso** - Detenga otras aplicaciones que usen ese puerto, o cambie el puerto en el Dockerfile y `devcontainer.json`

## Descripción General del Flujo de Trabajo

Esta configuración proporciona un entorno de desarrollo Python profesional:

- **VS Code** proporciona el editor de código con resaltado de sintaxis, IntelliSense y depuración
- **Contenedor Docker** ejecuta un entorno Linux aislado con Python y todas las dependencias
- **Imagen oficial de Python** (`python:3.12-slim`) incluye Python, pip y herramientas esenciales
- **Configuración de Dev Container** (`.devcontainer/`) instala automáticamente extensiones de VS Code para depuración Python y soporte de lenguaje
- **Reenvío de puertos** permite acceder a aplicaciones web (Streamlit, Flask) que se ejecutan dentro del contenedor desde su navegador

## Flujo de Trabajo Diario

Una vez configurado todo, esta es su rutina diaria:

1. **Iniciar Docker Desktop** - Abra la aplicación y espere el indicador de estado verde (Docker debe estar ejecutándose)
2. **Abrir VS Code** - Inicie VS Code y abra su carpeta de proyecto
3. **Reabrir en Contenedor** - Si no está ya en el contenedor, haga clic en el ícono verde (inferior izquierdo) y seleccione **Reopen in Container**
4. **Escribir y ejecutar código** - Edite archivos `.py`, ejecute línea por línea con `Shift+Enter`, o ejecute aplicaciones con `streamlit run app.py`
5. **Guardar su trabajo** - Sus archivos de código (`.py`, `.ipynb`) se guardan en su computadora y persisten entre sesiones
6. **Confirmar y enviar** - Use GitHub Desktop para confirmar sus cambios y enviarlos al repositorio

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 7 de diciembre de 2025.
