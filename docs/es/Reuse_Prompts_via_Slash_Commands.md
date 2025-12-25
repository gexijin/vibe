[Inicio](index.html)

# Crear Comandos Slash Personalizados

¿Cansado de escribir los mismos prompts detallados una y otra vez? Los comandos slash personalizados le permiten guardar instrucciones complejas como atajos reutilizables. Al igual que crear atajos de teclado para sus tareas más frecuentes, los comandos slash transforman prompts extensos en comandos simples como `/stock-report Apple` que generan informes completos al instante.

¿La mejor parte? Usamos Claude para escribir el prompt detallado y crear el comando. Así es, Claude es muy bueno escribiendo prompts para... sí mismo.

## Conceptos Clave

- **Comando slash** - Un prompt reutilizable almacenado como archivo Markdown que Claude Code ejecuta cuando usted escribe `/nombre-comando`
- **Argumentos** - Variables que usted pasa a los comandos (como símbolos bursátiles) usando la palabra clave especial `$ARGUMENTS`
- **Carpeta `.claude/commands/`** - Donde Claude Code automáticamente descubre y carga sus comandos personalizados

## Lo Que Necesitará

- Haber completado [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) o [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- Un tema para investigar (usaremos informes de acciones como ejemplo)
- Un editor de texto como VS Code instalado
- 15-20 minutos

## Paso 1: Crear una Carpeta de Proyecto

**Windows (WSL):**
- Abra **Ubuntu** desde el menú Inicio
- Escriba estos comandos:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir test_claude
  cd test_claude
   ```
  Reemplace `YOUR_USERNAME` con su nombre de usuario de Windows

**Mac:**
- Abra **Terminal** (encuéntrelo en Aplicaciones > Utilidades)
- Escriba estos comandos:
  ```bash
  cd ~/Documents
  mkdir test_claude
  cd test_claude
  ```

## Paso 2: Iniciar Claude Code

**Windows (WSL):**
- Aún en el terminal Ubuntu, escriba:
  ```
  claude
  ```

**Mac:**
- Aún en Terminal, escriba:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el tutorial de instalación ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 3: Pedir a Claude que Cree un Comando Slash

En lugar de crear archivos manualmente, deje que Claude haga el trabajo. Escriba este prompt:

```
Crea un comando slash llamado stock-report que genere informes sobre
desarrollos recientes de una empresa identificada por nombre o símbolo bursátil.
Incluye:
- Noticias de productos o servicios
- Noticias del equipo directivo
- Informes financieros recientes
- Informes de analistas
```
Cuando se le solicite, otorgue a Claude permiso para crear el archivo.
Claude creará un prompt detallado y lo guardará como `stock-report.md` en la carpeta `.claude/commands/`.

**Nota:** Usamos formato Markdown en todo: en prompts, informes y comandos slash. Markdown es compatible con IA y puede editarse fácilmente como archivos de texto plano.

## Paso 4: Revisar el Comando

Use cualquier editor de texto para abrir el archivo `stock-report.md` de la carpeta `.claude/commands/`. Ese es el prompt para el comando slash.

Si tiene VS Code instalado (recomendado):
- Inicie VS Code
- Desde **File**, elija **Open folder**, y seleccione la carpeta del proyecto `Documents/test_claude`
- Desde el explorador de archivos, navegue a `.claude/commands` y haga clic en el archivo `stock-report.md` para abrirlo

Revise el prompt y modifique las instrucciones si lo desea.

**Nota:** Claude es excelente escribiendo prompts. Notará que su prompt está bien estructurado con formato markdown y redactado con claridad. Aprenda a escribir prompts como este. A veces incluso incluye instrucciones para solicitar aclaraciones si el identificador es ambiguo.

## Paso 5: Probar el Comando

Primero **salga** de la sesión actual de Claude Code presionando **Ctrl+C** dos veces. Luego reinicie Claude para que se cargue el nuevo comando slash:
  ```
  claude
  ```
Ahora pruebe su nuevo comando con un símbolo bursátil real:

```
/stock-report Apple
```

Claude busca en la web y genera un informe completo sobre Apple Inc. Esto puede tomar 1-2 minutos.

## Paso 6: Revisar el Informe Generado

Claude crea un informe en la línea de comandos. Revise la salida:

- Verifique que cada sección tenga información relevante y actual
- Verifique que las fuentes sean creíbles y recientes
- Note cómo Claude organizó la información

## Paso 7: Guardar el Informe en un Archivo

Modifiquemos el comando slash para guardar automáticamente los informes como archivos markdown. Agregue esto manualmente al archivo markdown del comando slash.

- Abra el archivo `stock-report.md` de la carpeta `.claude/commands/`
- Agregue esto al final:
  ```
  Guarda el informe como un archivo markdown. El nombre del archivo debe incluir el nombre de la empresa y la fecha.
  ```
- Guarde el archivo.

## Paso 8: Ejecutar el Comando Nuevamente

- Primero **salga** de la sesión actual de Claude Code presionando **Ctrl+C** dos veces. Luego reinicie Claude para que se cargue el nuevo comando slash:
  ```
  claude
  ```
- Ahora pruebe su nuevo comando con un símbolo bursátil real:

  ```
  /stock-report AAPL
  ```
- Abra el informe

Claude genera el informe y lo guarda como un archivo markdown llamado algo como `Apple_2025-12-13.md`. Haga clic en el archivo en VS Code para verlo.

## Paso 9: Modificar el Comando a través de Claude

Puede pedir a Claude que edite los comandos slash:

```
Modifica el comando slash stock-report para que guarde el informe como un archivo html.
```

Claude actualiza el archivo de comando. Puede verificarlo desde el editor.

## Paso 10: Probar el Comando Actualizado

- Primero **salga** de la sesión actual de Claude Code presionando **Ctrl+C** dos veces. Luego reinicie Claude para que se cargue el nuevo comando slash:
  ```
  claude
  ```

- Pruebe el comando mejorado:

  ```
  /stock-report AAPL
  ```

Claude crea un archivo llamado algo como `Apple_2025-12-13.html`. Haga clic en este archivo desde el Explorador de Archivos en Windows o Mac para abrirlo en su navegador predeterminado.

## Paso 11: Reutilizar el Comando Slash (Opcional)

La palabra clave `$ARGUMENTS` en su comando slash funciona como un marcador de posición. Cuando escribe `/stock-report AAPL`, Claude reemplaza `$ARGUMENTS` con `AAPL` antes de ejecutar el prompt.

Pruebe con otro símbolo:

```
/stock-report TSLA
```

La misma estructura de comando ahora investiga Tesla.

## Paso 12: Probar Otro Comando Slash (Opcional)

Si completó el tutorial [Writing Research Paper](./Writing_Research_Paper_Claude_Code.md), debería tener un comando `/research-paper`. Pruébelo con un tema nuevo.

Primero, limpie la memoria de Claude para comenzar de nuevo:

```
/clear
```

Luego ejecute el comando de artículo de investigación:

```
/research-paper AI in schools
```

Dos diferencias clave:
- `/research-paper` se creó al final de una sesión capturando la interacción humana, mientras que `/stock-report` se crea desde cero
- `/research-paper` solicita información de manera interactiva antes de redactar el artículo

## Próximos Pasos

Ahora que comprende los comandos slash, cree más comandos personalizados para sus flujos de trabajo:

- **Revisión de código:** `/review-code` - Analiza código en busca de errores y mejoras
- **Notas de reunión:** `/meeting-summary` - Genera resúmenes estructurados de reuniones
- **Borradores de correo electrónico:** `/email-reply` - Crea respuestas de correo electrónico profesionales

## Solución de Problemas

- **Comando no encontrado:** Reinicie Claude Code para recargar los comandos desde `.claude/commands/`
- **Los argumentos no funcionan:** Verifique que `$ARGUMENTS` esté escrito correctamente en el archivo de comando (distingue mayúsculas y minúsculas)
- **Informe incompleto:** Pida a Claude que "continúe" o "agregue más detalle a la sección [nombre de sección]"

## Resumen del Flujo de Trabajo

- **Los comandos slash personalizados** ahorran tiempo al convertir prompts complejos en atajos simples
- **Los argumentos** hacen que los comandos sean flexibles para diferentes entradas (símbolos bursátiles, temas, archivos)
- **Claude construye comandos** - No necesita escribir archivos Markdown manualmente; solo describa lo que necesita
- **Los comandos son reutilizables** - Una vez creados, úselos en cualquier proyecto y sesión
- **Combine comandos** - Construya una biblioteca de comandos especializados para diferentes tareas

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 13 de diciembre de 2025.
