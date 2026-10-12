---
title: "Cree un subagente en Claude Code"
lang: "es"
---
[Inicio](index.html)

# Cree un subagente en Claude Code

Comparar oportunidades de inversión requiere horas de investigación y análisis. Piense en un subagente como contratar a un analista financiero que domina sus herramientas de investigación: usted proporciona nombres de empresas, y él recopila informes, evalúa cada empresa según métricas clave y recomienda la mejor inversión. Una vez que aprenda a construir subagentes, podrá automatizar cualquier flujo de trabajo repetitivo de múltiples pasos. Este tutorial le muestra cómo construir ese analista.

## Conceptos clave

- **Subagente** - Trabajador de IA especializado con objetivo propio, prompt de sistema y herramientas que completa tareas de forma autónoma
- **Contexto aislado** - Un subagente trabaja en su propio espacio de trabajo separado, así que su investigación no satura su conversación principal; solo regresa el resultado final
- **Skill** - Capacidad reutilizable (como generar informes bursátiles) que los subagentes pueden invocar para lograr sus objetivos
- **System Prompt** - Instrucciones que definen qué hace el subagente, cómo evalúa empresas y qué formato devuelve
- **Separación de responsabilidades** - Los skills recopilan datos; los subagentes usan esos datos para tomar decisiones

## Lo que necesitará

- Haber completado el tutorial [Cree su primera Claude Skill](./Create_Your_First_Claude_Skill.md)
- El skill `stock-report` ya instalado (en `.claude/skills/stock-report/`) de ese tutorial
- VS Code u otro editor de texto
- 20-25 minutos

## Paso 1: Abra su carpeta de proyecto e inicie Claude Code

Su skill `stock-report` está en la misma carpeta de proyecto que usó en el tutorial de Skills; vuelva a abrir esa carpeta en lugar de crear una nueva.

**Windows (PowerShell):**
- Haga clic en el **botón Inicio de Windows**, escriba `PowerShell` y ábralo
- Ejecute este comando:
  ```powershell
  cd ~/Documents/test_claude
  ```
- Inicie Claude Code:
  ```
  claude
  ```

**Mac:**
- Abra **Terminal** (Aplicaciones > Utilidades)
- Ejecute este comando:
  ```bash
  cd ~/Documents/test_claude
  ```
- Inicie Claude Code:
  ```
  claude
  ```

Inicie sesión con su suscripción de Claude siguiendo el tutorial de instalación ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 2: Verifique que existe el skill de informe bursátil

Antes de construir su subagente, confirme que el skill está disponible. Escriba:

```
Lista todas las skills disponibles
```

Debería ver `stock-report` en la salida. Este skill investiga empresas y genera informes que cubren noticias de productos, actualizaciones de gestión, desempeño financiero y perspectivas de analistas.

Si no lo ve, los archivos del skill deberían estar en `.claude/skills/stock-report/` (nivel de proyecto). Si la carpeta no existe, vuelva atrás y complete primero el tutorial [Cree su primera Claude Skill](./Create_Your_First_Claude_Skill.md) en esta misma carpeta de proyecto.

## Paso 3: Comprenda la arquitectura de subagente vs skill

Así es como los subagentes y skills trabajan juntos:

| Componente | Propósito | Ejemplo |
|-----------|---------|---------|
| **Skill** | Recopila datos sin procesar sobre una empresa | "Generar informe para Apple: productos, finanzas, gestión, analistas" |
| **Subagente** | Usa datos del skill para lograr un objetivo | "Obtener informes para Apple y Microsoft, evaluar ambos, recomendar en cuál invertir" |

**Diferencia clave:**
- **Skill = herramienta** que realiza investigación
- **Subagente = tomador de decisiones** que usa la herramienta y aplica lógica

Su subagente selector de acciones:
1. Invocará el skill de informe bursátil para cada empresa (2+ veces)
2. Evaluará empresas según categorías (finanzas, crecimiento, gestión, sentimiento)
3. Comparará puntuaciones y recomendará la mejor inversión

## Paso 4: Cree el subagente selector de acciones

Ejecute este comando:

```
/agents
```

Verá la interfaz de agentes de Claude Code mostrando subagentes existentes (si los hay) y opciones para **Crear**, **Editar** o **Eliminar** subagentes.

Ahora cree su subagente:
- Seleccione **Create new subagent**
- Seleccione **Project**
- Seleccione **Generate with Claude (recommended)**
- Pegue las siguientes instrucciones:
  ```
  Crea un archivo markdown para un nuevo subagente llamado stock-picker:
  - Acepta dos o más acciones
  - Usa el skill stock-report para investigar
  - Crea tarjetas de puntuación basadas en las categorías de datos recopilados
  - Proporciona una recomendación final.
  ```
- Presione **Enter** en **[Continue]** para usar **All tools**
- Seleccione **Sonnet** para el modelo
- Presione **Enter** para elegir un color aleatorio

**Qué significa "All tools":** Un subagente puede limitarse solo a las herramientas que necesita, por ejemplo, un agente de solo investigación con únicamente búsqueda web. Este tutorial usa **All tools** porque el stock-picker necesita investigar en línea y puede escribir archivos. Puede restringirlo más adelante editando el archivo del subagente.

## Paso 5: Revise lo que construyó (punto de reflexión)

Para abrir el archivo en VS Code, haga clic en **File > Open File...** y navegue hasta `.claude/agents/stock-picker.md`.

O puede pedirle a Claude:
```
Muéstrame el archivo del subagente stock-picker.
```
Claude mostrará el archivo del subagente ubicado en `.claude/agents/stock-picker.md`. Verá:

Un **YAML frontmatter** en la parte superior:
```
---
name: stock-picker
description: Compara múltiples empresas para decisiones de inversión...
skills: stock-report
---
```

Este frontmatter (la sección entre marcadores `---`) indica a Claude Code cuándo activar este subagente y qué skills puede usar.

Un **System prompt** debajo del frontmatter con su metodología de puntuación.

**Confirme estos elementos clave:**
- El subagente tiene acceso al skill `stock-report`
- El system prompt explica el desglose de puntuación
- El objetivo del subagente es claro: comparar empresas y recomendar una

Puede editar el archivo directamente o pedirle a Claude que lo actualice.

## Paso 6: Pruebe el subagente

Ahora pruebe su subagente con una comparación real. Escriba:

```
¿Qué es mejor inversión: Apple o Google?
```

El subagente se activará automáticamente según su descripción.

## Paso 7: Observe cómo trabaja el subagente

Mientras el subagente se ejecuta, verá que:
1. **Invoca el skill dos veces** - Llama al skill stock-report una vez para Apple y luego para Google
2. **Recopila datos** - Cada llamada al skill busca en la web y genera un informe de empresa
3. **Evalúa empresas** - Aplica la ponderación 40/30/20/10 entre categorías
4. **Genera salida** - Crea tabla de comparación y recomendación

Esto puede tomar 2-3 minutos ya que involucra búsqueda web.

Observe que su conversación principal no se llena con todos los resultados de búsqueda y pasos intermedios: eso es el contexto aislado en acción. El subagente investiga en su propio espacio de trabajo separado y solo le informa lo que ve aquí.

## Paso 8: Revise la salida

El subagente devuelve un análisis detallado que incluye:
- **Informes individuales de empresas** - Actualizaciones de productos, métricas financieras, cambios de gestión y sentimiento de analistas para cada acción
- **Cuadro comparativo de puntuaciones** - Puntuaciones numéricas entre categorías (Salud Financiera, Potencial de Crecimiento, Calidad de Gestión, Sentimiento de Mercado)
- **Recomendación final** - En qué acción invertir y por qué

El subagente puede mostrar esto en el terminal o generar un archivo markdown con el informe completo. Puede editar el archivo del subagente para personalizar las ponderaciones de puntuación o el formato de salida.

## Próximos pasos

Ahora que tiene un subagente selector de acciones funcional, pruebe estas extensiones:

- **Compare 3+ acciones**: "Compara AAPL, MSFT y GOOGL" para ver cómo el subagente maneja más opciones
- **Ajuste ponderaciones de puntuación**: Edite el archivo del subagente para cambiar el desglose 40/30/20/10 (ej., haga que el crecimiento sea 40% si prefiere acciones de crecimiento)
- **Cree otros subagentes**: Construya un subagente "code-reviewer", "bug-hunter" o "document-writer" para diferentes tareas

## Solución de problemas

- **Subagente no se activa**: Asegúrese de que su solicitud mencione comparar empresas o decisiones de inversión. Intente: "Usa el subagente stock-picker para comparar..."
- **Skill no encontrado**: Verifique que `.claude/skills/stock-report/SKILL.md` existe. Reinicie Claude Code si acaba de agregarlo.
- **Puntuaciones incompletas**: Pida al subagente que "continúe" o "explique las puntuaciones de cada categoría con más detalle"
- **Error al crear subagente**: Verifique que la carpeta `.claude/agents/` existe. Claude Code debería crearla automáticamente.

## Resumen del flujo de trabajo

- **Los subagentes automatizan flujos de trabajo de múltiples pasos** - Orquestan skills, aplican lógica y entregan decisiones
- **Los skills son herramientas reutilizables** - Un skill puede ser usado por múltiples subagentes para diferentes objetivos
- **Los system prompts definen el comportamiento** - Instrucciones claras y criterios de puntuación hacen que los subagentes sean confiables
- **Los subagentes mantienen el enfoque** - Cada subagente tiene un propósito único y claro (selección de acciones, revisión de código, etc.)
- **La composición escala** - Construya una biblioteca de skills y subagentes que trabajen juntos

---

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 14 de diciembre de 2025.
