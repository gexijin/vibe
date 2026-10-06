---
title: "Use Claude Code con Excel en VS Code"
lang: "es"
---
[Inicio](./)

# Use Claude Code con Excel en VS Code

Necesita una hoja de cálculo con fórmulas, formato y quizás un gráfico, pero no quiere pelearse con los menús de Excel. Piense en Claude Code como un asistente que conoce Excel a la perfección: usted describe lo que desea en lenguaje natural y él crea un archivo `.xlsx` real con fórmulas que funcionan. Este tutorial le muestra cómo preparar una carpeta de proyecto en VS Code y pedirle a Claude Code que cree y edite hojas de cálculo de Excel por usted.

## Conceptos Clave

- **Habilidad xlsx** - Capacidad de Claude Code para crear y editar hojas de cálculo `.xlsx` con fórmulas reales, formato y gráficos. Viene incluida automáticamente cuando inicia sesión con su cuenta de Claude. Internamente, Claude la usa para escribir y ejecutar pequeños programas de Python que construyen el archivo
- **[Extensión Spreadsheet Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)** (antes llamada Excel Viewer) - Extensión de VS Code que le permite revisar rápidamente los números de una hoja de cálculo sin salir del editor. No muestra gráficos
- **Fórmulas frente a números fijos** - Claude Code escribe fórmulas reales de Excel (como `=SUM(B2:B9)`), así su hoja se vuelve a calcular cuando usted cambia los datos. Si su Excel o LibreOffice está en español, verá la misma fórmula como `=SUMA(B2:B9)`; es normal, el programa traduce los nombres de las fórmulas automáticamente

## Lo Que Necesitará

- Haber completado [Primeros Pasos con VS Code](./VS_Code_Getting_Started)
- Claude Code instalado y funcionando (consulte [Instalar Claude Code en Windows](./Install_CLAUDE_Code_Win) o [Instalar Claude Code en Mac](./Install_Claude_Code_MacOS))
- Microsoft Excel, [LibreOffice Calc](https://es.libreoffice.org/descarga/) (gratuito) o Google Sheets (gratuito en su navegador web) para ver los gráficos
- 20-25 minutos

## Paso 1: Instalar Python

Claude crea las hojas de cálculo escribiendo pequeños programas de Python, así que su computadora necesita tener Python. Usted no tendrá que escribir nada de Python.

- **Windows**:
  - Vaya a [python.org/downloads/windows](https://www.python.org/downloads/windows/) (la página está en inglés)
  - Debajo de la versión más reciente de Python 3, haga clic en **Windows installer (64-bit)**
  - Ejecute el archivo descargado
  - **Marque la casilla "Add python.exe to PATH"** en la parte inferior de la primera pantalla y luego haga clic en **Install Now**
- **Mac**:
  - Vaya a [python.org/downloads](https://www.python.org/downloads/) y haga clic en el botón amarillo **Download Python**
  - Abra el archivo descargado y siga el instalador, haciendo clic en **Continuar** e **Instalar**

Si VS Code ya está abierto, ciérrelo y vuelva a abrirlo para que pueda encontrar Python.

## Paso 2: Instalar la Extensión Spreadsheet Viewer en VS Code

- Abra VS Code
- Haga clic en el icono **Extensions** en la barra lateral izquierda (o haga clic en **View > Extensions**)
- Busque `GrapeCity.gc-excelviewer`
- Haga clic en **Install** en **Spreadsheet Viewer** de **MESCIUS**

**Nota:** Esta extensión antes se llamaba **Excel Viewer** de **GrapeCity**, y es posible que guías y videos antiguos todavía usen ese nombre. Si busca "Excel Viewer" ahora aparecen varias extensiones distintas, así que busque por el ID indicado arriba para encontrar la correcta. El ID todavía empieza por `GrapeCity`; eso es normal.

Esto le permite hacer clic en cualquier archivo `.xlsx` y ver sus hojas, números y fórmulas directamente dentro de VS Code. Es ideal para revisiones rápidas, pero no puede mostrar gráficos, celdas resaltadas con colores ni listas desplegables. Para eso, abra el archivo en Excel, LibreOffice Calc o Google Sheets.

## Paso 3: Crear Su Carpeta de Proyecto

- Cree una carpeta nueva en su computadora (por ejemplo, `my-excel-project`)
- En VS Code, haga clic en **File > Open Folder** y seleccione su nueva carpeta
- Haga clic en **Select Folder** (Windows) u **Open** (Mac)

## Paso 4: Iniciar Claude Code

- Haga clic en **Terminal > New Terminal** en VS Code
- Escriba este comando y presione Enter:

```bash
claude
```

- Si es la primera vez, se abrirá una ventana del navegador para la autenticación: inicie sesión con su cuenta de Claude
- Vuelva a VS Code cuando vea el mensaje de bienvenida de Claude en la terminal

## Paso 5: Crear Su Primera Hoja de Cálculo

- En la terminal de Claude Code, escriba:

```
Crea una hoja de cálculo llamada budget.xlsx con columnas para Categoría, Monto Mensual y Notas. Agrega 6 categorías de gastos de ejemplo como Alquiler, Supermercado y Servicios con montos realistas. Agrega una fila Total al final que sume la columna Monto Mensual usando una fórmula.
```

- Presione Enter
- Observe cómo Claude escribe un script de Python, lo ejecuta y genera `budget.xlsx` en su carpeta de proyecto
- Claude le pedirá permiso antes de ejecutar comandos o instalar herramientas auxiliares (como `openpyxl`, un complemento de Python para hojas de cálculo): elija **Yes** para que continúe
- Si Claude dice que Python no está instalado o que no lo encuentra, vuelva al Paso 1 y luego cierre y vuelva a abrir VS Code

## Paso 6: Ver el Resultado

- En el panel Explorer de VS Code (lado izquierdo), haga clic en `budget.xlsx`
- La extensión Spreadsheet Viewer abre el archivo como una hoja de cálculo
- Si en su lugar ve texto y símbolos ilegibles, VS Code abrió el archivo como texto plano: consulte la sección Solución de Problemas más abajo
- Haga clic en la celda **Total** al final: observe que es una fórmula, no un número escrito a mano
- Si tiene Excel o LibreOffice Calc instalado, también puede hacer doble clic en el archivo en el Explorador de archivos (Windows) o en Finder (Mac) para abrirlo allí

## Paso 7: Pedirle a Claude que Agregue un Gráfico

- De vuelta en la terminal de Claude Code, escriba:

```
Agrega un gráfico circular a budget.xlsx que muestre la proporción de cada categoría en el gasto mensual total.
```

- Presione Enter
- Para ver el gráfico, abra `budget.xlsx` en Excel o LibreOffice Calc (haga doble clic en él en el Explorador de archivos o en Finder), o súbalo a Google Sheets
- Spreadsheet Viewer en VS Code no mostrará el gráfico; es lo esperado, el gráfico sigue estando en el archivo

## Paso 8: Editar los Datos y Pedirle a Claude que los Actualice

- En Excel o LibreOffice Calc, cambie uno de los montos (por ejemplo, duplique el valor de Alquiler)
- Guarde el archivo y ciérrelo
- No haga este cambio en Spreadsheet Viewer: al guardar desde ahí, el gráfico puede borrarse del archivo
- En la terminal de Claude Code, escriba:

```
Cambié algunos números en budget.xlsx. Vuelve a calcular los totales y asegúrate de que el gráfico siga coincidiendo con los datos.
```

- Presione Enter
- Claude lee sus cambios, revisa las fórmulas y confirma que todo cuadra

**¿No tiene Excel ni LibreOffice?** Omita el cambio manual y pídaselo a Claude: "Duplica el monto de Alquiler en budget.xlsx."

Este es el flujo de trabajo principal: describa lo que desea, deje que Claude lo construya, revise el resultado y pida cambios en lenguaje natural.

## Paso 9: Pedirle a Claude que Limpie Datos Desordenados

Claude Code también es útil para arreglar hojas de cálculo que ya están desordenadas.

- Escriba:

```
Crea un archivo messy_sales.csv con 15 filas de datos de ventas que tenga algunos problemas: algunas celdas vacías, formatos de fecha inconsistentes y una fila duplicada. Luego crea una versión limpia llamada sales_clean.xlsx que corrija estos problemas y explica qué corregiste.
```

- Presione Enter
- Revise el resumen que Claude le da de lo que encontró y corrigió
- Abra `sales_clean.xlsx` para confirmar que los datos se ven bien

## Próximos Pasos

- Pídale a Claude que cree una hoja de cálculo a partir de un archivo CSV que ya tenga (primero arrástrelo a su carpeta de proyecto)
- Pruebe solicitudes más avanzadas: "agrega formato condicional para que cualquier categoría de más de $500 se ponga en rojo"
- Pídale a Claude que agregue una segunda hoja que resuma los datos de la primera
- Combine esto con [Use GitHub Desktop con Claude Code](./GitHub_Desktop_Claude_Code_Workflow) para guardar versiones de sus hojas de cálculo a medida que avanza
- Continúe con [Vibe Coding de un Control de Presupuesto en Excel](./Vibe_Coding_Excel_Guide) para crear un proyecto completo con varias hojas

## Solución de Problemas

- **`budget.xlsx` se abre como texto y símbolos ilegibles (empezando por `PK`)**: VS Code muestra el archivo sin procesar porque ningún visor de hojas de cálculo se encargó de abrirlo. El archivo en sí está bien: un `.xlsx` es un paquete comprimido, no texto plano. Compruebe que **Spreadsheet Viewer** de MESCIUS (`GrapeCity.gc-excelviewer`) esté instalado y habilitado; luego cierre la pestaña, haga clic derecho en `budget.xlsx` en el panel Explorer, elija **Open With...** y seleccione **Excel Editor** (el editor de Spreadsheet Viewer para archivos `.xlsx`). Si también tiene instalada otra extensión de hojas de cálculo, elija **Configure default editor for '*.xlsx'...** en la misma lista y seleccione **Excel Editor** para que, de ahora en adelante, al hacer un solo clic en el archivo se use ese editor.
- **Spreadsheet Viewer muestra una vista previa en blanco o dañada**: Cierre la pestaña y vuelva a abrir el archivo. Si sigue fallando, abra el archivo en Excel, LibreOffice Calc o Google Sheets: el archivo en sí está bien, es solo un fallo de la vista previa.
- **Las celdas con fórmulas aparecen vacías en lugar de mostrar un número**: Esto suele significar que el archivo no se volvió a calcular después de escribirse. Pídale a Claude: "Vuelve a calcular budget.xlsx y confirma que no haya errores en las fórmulas."
- **Los cambios de Claude no aparecen**: Asegúrese de estar viendo el mismo archivo que Claude editó (revise el nombre de archivo que menciona). Cierre y vuelva a abrir la pestaña en VS Code para forzar una actualización.
- **"claude is not recognized" o "El término 'claude' no se reconoce" en la terminal**: Claude Code no está instalado correctamente. Vuelva a revisar la guía de instalación para [Windows](./Install_CLAUDE_Code_Win) o [Mac](./Install_Claude_Code_MacOS).
- **Falta el gráfico**: Spreadsheet Viewer no puede mostrar gráficos. Abra el archivo en Excel, LibreOffice Calc o Google Sheets. Si el gráfico tampoco aparece ahí, pídale a Claude: "Falta el gráfico circular en budget.xlsx, vuelve a agregarlo."

## Resumen del Flujo de Trabajo

- **VS Code** - Su carpeta de proyecto y un lugar para ver las hojas de cálculo con la extensión Spreadsheet Viewer
- **Claude Code** - Escribe y edita archivos `.xlsx` reales con fórmulas que funcionan, a partir de sus solicitudes en lenguaje natural
- **Excel / LibreOffice / Google Sheets** - Para ver los gráficos y ajustar manualmente los archivos que crea Claude
- **Itere** - Describa lo que desea, revise el resultado, describa el siguiente cambio

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 21 de septiembre de 2026.
