---
title: "Vibe Coding de un Control de Presupuesto en Excel con Claude Code"
lang: "es"
---
[Inicio](./)

# Vibe Coding de un Control de Presupuesto en Excel con Claude Code

Vibe coding es como tener una conversación con su computadora: usted describe el resultado, Claude Code lo construye, usted prueba y refina. No es magia; es una nueva forma de trabajar donde usted guía la visión y la IA se encarga de la mecánica de la hoja de cálculo: fórmulas, formato y gráficos. Este tutorial le guía en la creación de un control de presupuesto real con varias hojas usando únicamente solicitudes en lenguaje natural.

## Conceptos Clave

- **[Claude Code](https://code.claude.com/)** - Asistente de codificación con IA que escribe, edita y corrige archivos a partir de sus solicitudes en lenguaje natural
- **Libro con varias hojas** - Un único archivo `.xlsx` con varias pestañas (Ingresos, Gastos, Resumen) que se referencian entre sí mediante fórmulas
- **Refinamiento iterativo** - El patrón central de vibe coding: describir → probar → refinar → confirmar versiones que funcionen

## Lo Que Necesitará

- Haber completado [Use Claude Code con Excel en VS Code](./Excel_Coding_VS_Code_Guide)
- Haber completado [Use GitHub Desktop con Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 25-30 minutos

## Paso 1: Crear Nuevo Repositorio en GitHub

- Abra GitHub Desktop
- Haga clic en **File > New Repository**
- Complete los detalles:
  - **Name:** `budget-dashboard`
  - **Description:** `Control de presupuesto personal construido con vibe coding`
  - **Local Path:** Elija una ubicación (por ejemplo, Documents o una carpeta de trabajo)
  - Marque **Initialize this repository with a README**
- Haga clic en **Create Repository**
- Haga clic en **Publish repository** en la parte superior
- Desmarque **Keep this code private** si desea que sea público (opcional)
- Haga clic en **Publish Repository**

Ahora tiene un repositorio Git local y una copia de respaldo en GitHub.

## Paso 2: Abrir el Proyecto en VS Code

- Abra VS Code
- Haga clic en **File > Open Folder**
- Seleccione su carpeta `budget-dashboard`
- Haga clic en **Select Folder** (Windows) u **Open** (Mac)
- Si aún no lo ha hecho, instale la extensión **Spreadsheet Viewer** de MESCIUS (antes llamada **Excel Viewer** de GrapeCity) para poder ver hojas de cálculo sin salir de VS Code. Busque su ID, `GrapeCity.gc-excelviewer`, en el panel Extensions para encontrar la correcta

## Paso 3: Iniciar Claude Code

- Haga clic en **Terminal > New Terminal**
- Escriba este comando para iniciar Claude Code:

```bash
claude
```

- Inicie sesión si se le solicita y luego espere el mensaje de bienvenida de Claude

Claude Code ya está en ejecución y listo para sus solicitudes.

## Paso 4: Primer Vibe - Crear las Hojas de Ingresos y Gastos

En lugar de construir una hoja de cálculo celda por celda, simplemente describa lo que desea.

- En la terminal de Claude Code, escriba:

```
Crea una hoja de cálculo llamada budget.xlsx con dos hojas: "Ingresos" y "Gastos". Ingresos debe tener columnas para Fuente, Mes y Monto, con 3 fuentes de ingresos de ejemplo durante 2 meses. Gastos debe tener columnas para Categoría, Mes y Monto, con 6 categorías de ejemplo (como Alquiler, Supermercado, Transporte, Servicios, Entretenimiento, Ahorro) durante los mismos 2 meses. Agrega una fila Total al final de cada hoja usando fórmulas SUM.
```

- Presione Enter
- Observe cómo Claude escribe y ejecuta un script de Python que construye el libro y luego lo vuelve a calcular para que los totales muestren números reales
- Abra `budget.xlsx` en la pestaña de Spreadsheet Viewer y revise ambas hojas

**Guarde su progreso:** Pídale a Claude que confirme los cambios usando Git, o hágalo usted mismo desde GitHub Desktop:
```
Confirma estos cambios.
```

## Paso 5: Segundo Vibe - Agregar una Hoja de Resumen

Antes de crear gráficos, conecte las dos hojas.

- En la terminal de Claude Code, escriba:

```
Agrega una tercera hoja llamada "Resumen" a budget.xlsx. Debe mostrar Ingresos Totales, Gastos Totales y Ahorro Neto (Ingresos menos Gastos), cada uno calculado con fórmulas que hagan referencia a las hojas Ingresos y Gastos, no con números fijos.
```

- Presione Enter
- Claude actualiza el libro y lo vuelve a calcular
- Abra la pestaña **Resumen** y haga clic en la celda Ahorro Neto para confirmar que es una fórmula que hace referencia a las otras hojas

**Guarde su progreso:** Pídale a Claude que confirme los cambios, o use GitHub Desktop.

## Paso 6: Tercer Vibe - Agregar Gráficos

Los números son útiles, pero los gráficos cuentan la historia de un vistazo.

- En la terminal de Claude Code, escriba:

```
Agrega un gráfico circular a la hoja Gastos que muestre la proporción total de cada categoría en el gasto. Agrega un gráfico de barras a la hoja Resumen que compare Ingresos Totales frente a Gastos Totales para cada mes.
```

- Presione Enter
- Claude agrega ambos gráficos y vuelve a calcular el archivo
- Vuelva a abrir `budget.xlsx` en Spreadsheet Viewer (o actualice la pestaña) y revise ambas hojas para ver los nuevos gráficos

## Paso 7: Cuarto Vibe - Resaltar las Categorías que Superan el Presupuesto

Haga visibles los problemas de un vistazo en lugar de buscarlos entre los números.

- En la terminal de Claude Code, escriba:

```
En la hoja Gastos, agrega formato condicional para que cualquier gasto de más de $500 en un solo mes se resalte en rojo, y cualquier gasto de menos de $100 se resalte en verde.
```

- Presione Enter
- Vuelva a abrir el archivo y revise la hoja Gastos: las celdas ahora deberían tener colores según su valor

Si algo no se ve bien, copie lo que ve y descríbaselo a Claude para que lo corrija.

## Paso 8: Quinto Vibe - Agregar una Lista Desplegable de Categorías

Facilite ampliar la hoja sin errores de escritura.

- En la terminal de Claude Code, escriba:

```
Agrega validación de datos a la columna Categoría de la hoja Gastos para que solo acepte valores de una lista desplegable con las categorías existentes, más "Otro". Agrega dos filas vacías al final listas para nuevas entradas.
```

- Presione Enter
- Abra el archivo, haga clic en una de las celdas vacías de Categoría y confirme que aparece una flecha desplegable con su lista de categorías

## Paso 9: Revisar y Confirmar

Antes de confirmar, revise lo que Claude construyó.

- En Spreadsheet Viewer, revise las tres hojas: Ingresos, Gastos y Resumen
- No necesita entender cada fórmula, pero hágase una idea de la estructura
- Abra GitHub Desktop
- Verá `budget.xlsx` listado como archivo modificado
- En el campo **Summary** en la parte inferior izquierda, escriba:

```
Agregar gráficos, formato condicional y lista desplegable de categorías al control de presupuesto
```

- Haga clic en **Commit to main**
- Haga clic en **Push origin** para respaldar en GitHub

¡Ha guardado una versión completa y funcional de su control de presupuesto!

## Paso 10: Iterar y Mejorar

Vibe coding brilla cuando usted itera. Pruebe agregar funciones describiéndolas:

**Ejemplos de solicitudes a Claude:**

- "Agrega una fila Meta de Ahorro a la hoja Resumen que muestre el progreso hacia una meta de ahorro de $500/mes"
- "Agrega una cuarta hoja que muestre una comparación año contra año cuando agregue más meses de datos"
- "Cambia los colores del gráfico circular a un tema azul y gris"
- "Agrega una nota que explique cada fórmula para que pueda aprender qué hace"
- "Crea un segundo libro llamado household_budget.xlsx para una familia de cuatro personas con más categorías"

Después de cada función exitosa:
- Abra el archivo y revíselo en Spreadsheet Viewer
- Si funciona, confirme los cambios con GitHub Desktop
- Si algo se ve mal, descríbaselo a Claude y pídale que lo corrija
- Cuando esté corregido, confirme la versión que funciona

**Principios clave:**

- **Describa resultados, no la implementación** - Diga "resalta los gastos de más de $500", no "usa formato condicional con un CellIsRule"
- **Itere rápidamente** - Probar → refinar → probar → refinar
- **Confirme versiones que funcionen** - Guarde cada éxito antes de probar nuevas funciones
- **Acepte los errores** - Si una fórmula o un gráfico no sale bien, simplemente describa el problema y pídale a Claude que lo corrija
- **Mantenga el control** - Usted decide qué debe mostrar el control de presupuesto y cuándo es suficientemente bueno

Cada vez, siga el patrón: describir → revisar el archivo → iterar → confirmar.

## Próximos Pasos

- **Aplíquelo a sus propias finanzas** - Pídale a Claude que reconstruya el control de presupuesto con sus categorías reales de ingresos y gastos
- **Importe datos reales** - Coloque un CSV de su estado de cuenta bancario en su carpeta de proyecto y pídale a Claude que lo incorpore al control de presupuesto
- **Aprenda preguntando** - Cuando Claude escriba una fórmula, pregunte "explica qué hace esta fórmula" para aprender Excel
- **Comparta su control de presupuesto** - Haga push del archivo terminado a GitHub para que usted (o sus familiares) puedan obtener la versión más reciente
- **Lea sobre vibe coding** - Visite la [guía de IBM](https://www.ibm.com/think/topics/vibe-coding) para aprender más sobre este estilo de programación

## Solución de Problemas

- **Una celda con fórmula aparece vacía o muestra `None`** - El archivo necesita volver a calcularse después de las ediciones. Pídale a Claude: "Vuelve a calcular budget.xlsx y confirma que no haya errores en las fórmulas."
- **El gráfico no se actualiza después de cambiar los datos** - Vuelva a abrir la pestaña en VS Code (ciérrela y haga clic de nuevo en el archivo) para obligar a Spreadsheet Viewer a actualizarse.
- **Claude comete un error** - ¡Es normal! Describa lo que se ve mal y pídale a Claude que lo corrija. Vibe coding incluye iteración y depuración.
- **No puede hacer push a GitHub** - Asegúrese de haber iniciado sesión en GitHub Desktop y de haber publicado el repositorio (Paso 1). Revise su conexión a internet.
- **La lista desplegable no aparece** - La validación de datos solo se muestra en aplicaciones de hojas de cálculo reales (Excel, LibreOffice, Google Sheets), no siempre en visores ligeros. Abra el archivo en Excel o LibreOffice Calc para probarla.

## Resumen del Flujo de Trabajo

Este tutorial combinó varias herramientas en un solo flujo de trabajo:

- **GitHub Desktop** - Control de versiones con interfaz visual (crear repositorios, confirmar, hacer push)
- **VS Code** - Editor con la extensión Spreadsheet Viewer para vistas previas rápidas
- **Claude Code** - Asistente con IA que crea y edita archivos `.xlsx` reales a partir de sus descripciones
- **openpyxl (tras bastidores)** - El motor que Claude usa para escribir fórmulas, formato y gráficos en el archivo

La magia no está en una sola herramienta: es cómo vibe coding le permite describir lo que desea e iterar rápidamente. Pasó de una carpeta vacía a un control de presupuesto funcional y lleno de gráficos sin escribir una sola fórmula a mano.

## Flujo de Trabajo Diario

Después de esta configuración inicial, su rutina diaria de vibe coding será:

1. **Abra VS Code** - Abra su carpeta de proyecto
2. **Inicie Claude Code** - Escriba `claude` en la terminal
3. **Describa su objetivo** - "Agrega una función que..." o "Corrige la fila donde..."
4. **Revise el archivo** - Ábralo en Spreadsheet Viewer o en Excel/LibreOffice
5. **Itere o confirme** - Si algo no está bien, describa la corrección; si funciona, confirme los cambios con GitHub Desktop
6. **Haga push con regularidad** - Haga clic en **Push origin** para respaldar en GitHub

Cuanto más practique, mejor describirá lo que desea. Vibe coding es una habilidad: usted aprende qué tipo de descripciones funcionan mejor y cómo dividir grandes ideas de hojas de cálculo en partes que se puedan probar.

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 21 de septiembre de 2026.
