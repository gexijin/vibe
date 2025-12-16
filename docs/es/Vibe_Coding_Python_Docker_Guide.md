[Inicio](index.html)

# Vibe Coding en Python con Claude Code y Docker

Ha escrito código Python línea por línea. Pero ¿qué pasaría si pudiera describir lo que desea en lenguaje natural y ver cómo aparece el código? Vibe coding es como tener una conversación con su computadora: usted describe el resultado, Claude Code lo construye, usted prueba y refina. No es magia; es una nueva forma de trabajar donde usted guía la visión y la IA maneja la implementación. Este tutorial le muestra cómo analizar el conjunto de datos clásico de flores Iris usando únicamente solicitudes en lenguaje natural.

## Conceptos Clave

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - Programar describiendo lo que desea en lenguaje natural, iterando basándose en resultados en lugar de escribir código línea por línea
- **[Claude Code](https://code.claude.com/)** - Asistente de codificación con IA que escribe, depura y refactoriza código a partir de sus solicitudes en lenguaje natural
- **[Iris Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)** - Conjunto de datos clásico con mediciones de 150 flores iris de tres especies
- **Refinamiento iterativo** - El patrón central de vibe coding: describir → probar → refinar → confirmar versiones que funcionen

## Lo Que Necesitará

- Haber completado [Programación en Python con VS Code y Docker](./Python_Coding_Docker_Guide)
- Haber completado [Uso de GitHub Desktop con Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 20-25 minutos

## Paso 1: Crear Nuevo Repositorio en GitHub

- Abra GitHub Desktop
- Haga clic en **File > New Repository**
- Complete los detalles:
  - **Name:** `iris-analysis`
  - **Description:** `Análisis de datos Iris construido con vibe coding`
  - **Local Path:** Elija una ubicación (ej., Documents o carpeta de trabajo)
  - Marque **Initialize this repository with a README**
- Haga clic en **Create Repository**
- Haga clic en **Publish repository** en la parte superior
- Desmarque **Keep this code private** si desea que sea público (opcional)
- Haga clic en **Publish Repository**

Ahora tiene un repositorio Git local y una copia de respaldo en GitHub.

## Paso 2: Copiar Configuración de Docker

Necesita la carpeta `.devcontainer` del proyecto vibe para configurar su entorno Docker.

- Abra File Explorer (Windows) o Finder (Mac)
- Navegue a su carpeta del proyecto vibe (ej., `Documents/vibe`)
- Busque la carpeta `.devcontainer`
- Copie la carpeta completa (contiene `Dockerfile` y `devcontainer.json`)
- Navegue a su nueva carpeta `iris-analysis`
- Pegue la carpeta `.devcontainer` allí

Su carpeta `iris-analysis` ahora debe contener:
- `.devcontainer/` (carpeta que acaba de copiar)
- `README.md` (creado por GitHub Desktop)
- `.git/` (carpeta oculta para control de versiones)

## Paso 3: Abrir Proyecto en Container

- Abra VS Code
- Haga clic en **File > Open Folder**
- Navegue a la carpeta `iris-analysis`
- Haga clic en **Select Folder**
- Aparece una notificación en la parte inferior derecha: **Folder contains a Dev Container configuration file**
- Haga clic en **Reopen in Container**
- Si no ve la notificación, haga clic en el ícono verde en la esquina inferior izquierda y seleccione **Reopen in Container**
- VS Code construye el container de Docker (toma 3-5 minutos la primera vez)
- Observe la notificación de progreso mostrando los pasos de construcción
- Cuando se complete, el ícono verde muestra **Dev Container: Python in Docker**

## Paso 4: Iniciar Claude Code

- En VS Code, haga clic en **Terminal > New Terminal**
- Ahora está dentro del container de Docker
- Escriba este comando para iniciar Claude Code:

```bash
claude
```

- Se abre una ventana del navegador para autenticación
- Haga clic en **Continue with Google** o **Continue with Email**
- Inicie sesión con su cuenta de Claude (o cree una)
- Después de que la autenticación sea exitosa, regrese al terminal de VS Code
- Verá el mensaje de bienvenida de Claude

Claude Code ahora está ejecutándose y listo para sus solicitudes.

## Paso 5: Primer Vibe - Cargar los Datos

Ahora comienza la diversión. En lugar de buscar documentación, simplemente describa lo que desea.

- En el terminal de Claude Code, escriba:

```
Carga el conjunto de datos iris desde scikit-learn. Conviértelo en un dataframe de pandas con los nombres de columnas apropiados. Agrega los nombres de las especies como una columna (no solo números). Muéstrame las primeras 10 filas. Guarda el código en un archivo llamado iris_exploration.py
```

- Presione Enter
- Observe cómo Claude:
  - Escribe código Python para cargar los datos
  - Crea un script con las importaciones apropiadas
  - Ejecuta el código para mostrarle los resultados
- Revise la salida que muestra las mediciones de flores y nombres de especies

¡Acaba de usar vibe coding! Sin buscar documentación, sin ensayo y error—solo describa y pruebe.

Solicite a Claude que confirme usando Git. O hágalo usted mismo desde GitHub Desktop.
```
Confirma estos cambios.
```
## Paso 6: Segundo Vibe - Estadísticas Resumidas

Antes de crear visualizaciones, comprenda qué contienen los datos.

- En el terminal de Claude Code, escriba:

```
Muéstrame estadísticas resumidas de los datos de iris agrupados por especie. Quiero ver la media, mínimo y máximo de cada medición (longitud de sépalo, ancho de sépalo, longitud de pétalo, ancho de pétalo) para cada una de las tres especies. Agrega esto a iris_exploration.py
```

- Presione Enter
- Claude actualiza el script y muestra las estadísticas
- Note cómo cada especie tiene rangos de mediciones diferentes
- Setosa tiene pétalos mucho más pequeños que Virginica

Esta exploración le ayuda a comprender los patrones en los datos.

Solicite a Claude que confirme usando Git. O hágalo usted mismo desde GitHub Desktop.

## Paso 7: Tercer Vibe - Crear un Histograma

Es hora de visualizar los datos.

- En el terminal de Claude Code, escriba:

```
Crea un histograma que muestre la distribución de las longitudes de pétalos para todas las flores. Usa 20 intervalos. Agrega un título y etiquetas de ejes. Guarda el gráfico como petal_length_histogram.png. Agrega este código a iris_exploration.py
```

- Presione Enter
- Claude crea el código de visualización
- Un archivo PNG aparece en su carpeta del proyecto
- Abra `petal_length_histogram.png` para ver el gráfico
- Note los dos picos—esto muestra que las especies tienen longitudes de pétalos diferentes

## Paso 8: Cuarto Vibe - Gráfico de Dispersión

Los gráficos de dispersión muestran relaciones entre dos variables.

- En el terminal de Claude Code, escriba:

```
Crea un gráfico de dispersión con la longitud de pétalo en el eje x y el ancho de pétalo en el eje y. Colorea cada punto por especie usando colores diferentes. Agrega una leyenda que muestre qué color representa cada especie. Guárdalo como petal_scatter.png. Agrega esto a iris_exploration.py
```

- Presione Enter
- Claude crea el gráfico de dispersión
- Abra `petal_scatter.png` para ver el resultado
- Note cómo las tres especies forman grupos distintos
- Setosa (pétalos pequeños) está claramente separada de las demás

Esto es vibe coding en acción: describa la visualización, pruébela e itere.

## Paso 9: Quinto Vibe - Gráfico de Cajas

Los gráficos de cajas son excelentes para comparar distribuciones entre grupos.

- En el terminal de Claude Code, escriba:

```
Crea un gráfico de cajas comparando las longitudes de pétalos entre las tres especies. Coloca las especies en el eje x y la longitud de pétalo en el eje y. Usa colores diferentes para cada especie. Agrega un título. Guárdalo como species_boxplot.png. Agrega esto a iris_exploration.py
```

- Presione Enter
- Claude añade el código del gráfico de cajas
- Abra `species_boxplot.png` para ver la comparación
- Las cajas muestran la mediana y los cuartiles para cada especie
- Puede ver claramente que Virginica tiene los pétalos más largos

## Paso 10: Revisar y Confirmar

Antes de confirmar, revise lo que Claude construyó.

- En VS Code Explorer, haga clic en `iris_exploration.py` para abrirlo
- Revise el código—note las importaciones, carga de datos y secciones de gráficos
- No necesita entender cada línea, pero obtenga una idea de la estructura
- Verifique que todos los archivos PNG fueron creados: `petal_length_histogram.png`, `petal_scatter.png`, `species_boxplot.png`
- Abra GitHub Desktop
- Verá todos los archivos nuevos listados (el script Python y las imágenes PNG)
- En el campo **Summary** en la parte inferior izquierda, escriba:

```
Análisis de datos Iris con histogramas, gráficos de dispersión y gráficos de cajas
```

- Haga clic en **Commit to main**
- Haga clic en **Push origin** para respaldar en GitHub

¡Ha guardado su primer análisis funcional!

## Paso 11: Iterar y Mejorar

Vibe coding brilla cuando usted itera. Intente añadir funciones describiéndolas:

**Ejemplos de solicitudes a Claude:**

- "Agrega un mapa de calor de la matriz de correlación mostrando las relaciones entre las cuatro mediciones"
- "Crea un gráfico de violín comparando el ancho de sépalo entre especies"
- "Calcula y muestra el coeficiente de correlación entre la longitud y el ancho de pétalo"
- "Agrega resultados de pruebas estadísticas comparando especies (ANOVA o prueba t)"
- "Crea un gráfico de pares mostrando todas las relaciones entre variables coloreadas por especie"

Después de cada función exitosa:
- Pruébela ejecutando el script
- Si funciona, confirme con GitHub Desktop
- Si falla, diga a Claude el error y solicite que lo corrija
- Cuando esté corregido, confirme la versión funcional


**Principios clave:**

- **Describa resultados, no implementación** - Diga "muestra un mapa de calor de correlación" no "usa seaborn.heatmap() con df.corr()"
- **Itere rápidamente** - Probar → refinar → probar → refinar
- **Confirme versiones funcionales** - Guarde cada éxito antes de probar nuevas funciones
- **Acepte los fallos** - Si el código de Claude falla, simplemente describa el error y solicite corrección
- **Mantenga el control** - Usted decide las funciones, prioridades y cuándo es suficientemente bueno

Cada vez, siga el patrón: describir → probar → iterar → confirmar.

## Próximos Pasos

- **Pruebe diferentes conjuntos de datos** - Solicite a Claude que use el conjunto de datos wine, digits o cargue un archivo CSV
- **Explore más visualizaciones** - Pruebe mapas de calor, gráficos de pares o gráficos de violín
- **Aprenda preguntando** - Cuando Claude escriba código, pregunte "explica qué hace esta línea" para aprender Python
- **Aplique a sus propios datos** - Use vibe coding para analizar sus datos de investigación o trabajo
- **Lea sobre vibe coding** - Visite [la guía de IBM](https://www.ibm.com/think/topics/vibe-coding) para más información sobre este estilo de codificación

## Solución de Problemas

- **El gráfico no se muestra** - El código guarda los gráficos como archivos PNG. Búsquelos en su carpeta del proyecto y ábralos directamente en VS Code.
- **Errores de importación** - El contenedor de Docker debe tener pandas, matplotlib y scikit-learn preinstalados. Si no, solicite a Claude que los instale con pip.
- **Claude comete errores** - ¡Es normal! Copie el mensaje de error, péguelo a Claude y diga "corrige este error". Vibe coding incluye iteración y depuración.
- **No puede hacer push a GitHub** - Asegúrese de haber iniciado sesión en GitHub Desktop y publicado el repositorio (Paso 1). Verifique su conexión a internet.
- **El contenedor no inicia** - Asegúrese de que Docker Desktop esté ejecutándose (indicador de estado verde). Intente hacer clic en el ícono verde en VS Code y seleccionar **Rebuild Container**.

## Resumen del Flujo de Trabajo

Este tutorial combinó varias tecnologías en un flujo de trabajo:

- **GitHub Desktop** - Control de versiones con interfaz visual (crear repositorios, confirmar, hacer push)
- **Contenedor Docker** - Entorno Python aislado con todas las dependencias preinstaladas
- **VS Code** - Editor de código que se conecta al contenedor de Docker
- **Claude Code** - Asistente con IA que escribe código Python a partir de sus descripciones
- **scikit-learn** - Proporciona el conjunto de datos Iris y herramientas de machine learning
- **pandas** - Manipulación y análisis de datos
- **matplotlib** - Creación de visualizaciones

La magia no está en una sola herramienta—es cómo vibe coding le permite describir lo que desea e iterar rápidamente. Pasó de un proyecto vacío a un análisis de datos completo con múltiples visualizaciones en 20 minutos sin escribir una sola línea de código manualmente.


---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 11 de diciembre de 2025.
