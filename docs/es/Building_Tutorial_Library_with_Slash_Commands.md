# Cómo automaticé la documentación con prompts reutilizables

A mediados de diciembre de 2025, pasé 2 horas tratando de ayudar a mi asistente de investigación a instalar Claude Code por Zoom. Me di cuenta de que alguien como ella necesita instrucciones específicas y prácticas, así que me propuse crear tutoriales completos para Claude Code. Mi objetivo: tutoriales prácticos y enfocados que guíen a principiantes completos a través de tareas reales paso a paso. Sin volcados de teoría. Sin manuales de referencia exhaustivos. Solo "haz esto, después esto, después esto" hasta lograr algo concreto.

Lo que comenzó como unos pocos archivos de documentación rápidamente se convirtió en una plataforma de aprendizaje multilingüe con más de 100 documentos de tutoriales. ¿El secreto? No los escribí todos manualmente. En su lugar, construí un conjunto de comandos slash personalizados (esencialmente, prompts reutilizables) que transformaron Claude Code en una fábrica de documentación automatizada, una que produce consistentemente tutoriales en mi estilo práctico y paso a paso.

## El desafío

Crear tutoriales consume mucho tiempo. Cada uno requiere investigación de las mejores prácticas actuales, escritura estructurada y amigable para principiantes, formato consistente, validación de precisión técnica, traducción a múltiples idiomas y mantenimiento continuo a medida que las herramientas evolucionan. Hacerlo manualmente para más de 20 tutoriales en más de 3 idiomas tomaría semanas.

## La solución: De proceso manual a comandos slash automatizados

Creé cinco comandos slash especializados que manejaron todo el ciclo de vida del tutorial.

### [`/tutorial`](../assets/commands/tutorial.md) - El generador de tutoriales

Creé los primeros tutoriales manualmente a través de prompts interactivos con Claude. Refiné el proceso mediante iteración, y luego le pedí a Claude que codificara el proceso funcional en un comando slash.

Este es exactamente el patrón descrito en mi [tutorial de artículo de investigación](./Writing_Research_Paper_Claude_Code.md): recorrer el flujo de trabajo manualmente y, en el paso final, pedirle a Claude que lo guarde como un comando reutilizable que captura el flujo de trabajo probado:
1. **Investigación**: Claude busca en la web información actual (sin números de versión desactualizados ni métodos obsoletos)
2. **Planificación**: Claude presenta lo que aprendió, recomienda un enfoque y esboza los pasos principales
3. **Iteración**: Reviso el plan y le pido a Claude que lo revise varias veces hasta quedar satisfecho
4. **Escritura**: Tras la aprobación, Claude escribe siguiendo reglas de formato estrictas:
   - Enlace a inicio en la parte superior
   - Gancho atractivo
   - Conceptos clave
   - Instrucciones paso a paso con verbos de acción
   - Sección de solución de problemas
   - Fecha de creación
5. **Prueba**: Pruebo los pasos yo mismo en una terminal separada y reviso si es necesario
6. **Pulido**: A veces edito manualmente, otras veces le pido a Claude que lo haga

El comando impone una estructura consistente en todos los tutoriales. Cada tutorial se siente como si viniera del mismo autor porque siguieron el mismo proceso sistemático. Generé más de 20 tutoriales que abarcan desde operaciones básicas de Git hasta flujos de trabajo avanzados de Docker.

### [`/review-tutorial`](../assets/commands/review-tutorial.md) - El bot de control de calidad

Para este, simplemente le pedí a Claude que "creara un comando slash para revisar tutoriales". Sin especificaciones detalladas. Claude generó un flujo de trabajo completo de tres fases con más de 30 criterios de calidad organizados por categorías:

- **Calidad del contenido**: título, gancho, conceptos clave, prerrequisitos, flujo de pasos, próximos pasos, solución de problemas
- **Estándares de formato**: enlace a inicio, encabezados de pasos, viñetas, negrita/comillas invertidas, bloques de código, párrafos
- **Amigabilidad para principiantes**: instrucciones basadas en menús, diferencias de plataforma, objetivos de clic exactos, sin jerga
- **Precisión técnica**: comandos correctos, interfaz actual, estimaciones de tiempo realistas
- **Calidad de escritura**: gramática, terminología consistente, lenguaje conciso

El comando presenta los hallazgos en un informe estructurado y luego aplica correcciones tras la aprobación. ¿Por qué era necesario? Dos razones: Claude no siempre sigue estrictamente las reglas de `/tutorial`, y el comando `/tutorial` mismo evolucionó mientras construía más tutoriales. El comando de revisión me permite pulir por lotes los tutoriales anteriores para ajustarlos a los últimos estándares.

### [`/translate-chinese`](../assets/commands/translate-chinese.md) & [`/translate-spanish`](../assets/commands/translate-spanish.md) - El motor de localización

Las traducciones al japonés llegaron primero, sin un comando slash. Simplemente le pedí a Claude Code que tradujera todos los tutoriales al japonés en un solo prompt. Claude automáticamente generó 8 subagentes ejecutándose en paralelo, cada uno manejando diferentes tutoriales simultáneamente.

Para idiomas subsiguientes, le pedí a Claude que "creara un comando slash para traducir tutoriales al chino", sin pautas específicas. Claude generó un flujo de trabajo de seis fases con reglas completas:

- **Reglas de traducción**: Mantener bloques de código, términos técnicos (Git, Docker, VS Code), rutas de archivos y URLs en inglés; traducir texto instructivo, encabezados y explicaciones
- **Pautas de idioma**: Reglas de tono y estilo, traducciones técnicas comunes (Click = 点击, Install = 安装), convenciones de tratamiento formal
- **Requisitos de formato**: Enlace a inicio localizado, estructura preservada, puntuación correcta (。，！？ para chino, ¿? ¡! para español)
- **Revisión de calidad**: Lista de verificación de fluidez natural, terminología consistente, uso correcto de caracteres

Con los comandos slash listos, le pedí a Claude Code que tradujera los 25 tutoriales usando subagentes. La traducción completa (50 archivos nuevos en dos idiomas) tomó solo 15 minutos.

El resultado: 81 archivos de tutoriales traducidos en los directorios de chino, español, francés, alemán y japonés, todos manteniendo calidad y estructura consistentes.

### [`/review-translation`](../assets/commands/review-translation.md) - La herramienta de mantenimiento de traducciones

Los tutoriales evolucionan. Los comandos cambian. Se añaden nuevas secciones. Este comando mantiene las traducciones sincronizadas mediante un flujo de trabajo de cuatro fases:

1. **Leer ambas versiones**: Cargar el original en inglés y la traducción lado a lado
2. **Comparar y actualizar**: Identificar secciones faltantes, contenido desactualizado, comandos o URLs modificados
3. **Revisar calidad**: Verificar precisión de traducción, calidad del idioma, consistencia de formato
4. **Informar y corregir**: Presentar hallazgos, obtener aprobación y aplicar actualizaciones

La revisión de calidad es exhaustiva. Para japonés, verifica frases naturales (no palabra por palabra), nivel de cortesía apropiado (forma です/ます), uso correcto de partículas (は/が, を, に, で), y que no haya uso excesivo de katakana antinatural. Cuando actualicé los tutoriales en inglés, pude propagar rápidamente los cambios a todas las traducciones manteniendo la calidad del idioma.

### Puliendo Traducciones para un Flujo Natural

Después de sincronizar las traducciones con los originales en inglés, añadí un paso final de pulido: editar cada documento traducido por sí solo para mejorar la calidad del lenguaje, sin comparar con el inglés. Este paso se enfoca puramente en hacer que el texto suene natural para hablantes nativos.

Usé prompts en el idioma de destino. En lugar de pedirle a Claude en inglés que "pula este documento en japonés", usé ChatGPT para escribir los prompts en japonés, chino o español. Esto pareció producir mejores resultados—Claude parecía pensar más naturalmente en ese idioma cuando las instrucciones también estaban en ese idioma.

Por ejemplo, para pulir documentos en chino, usé: "修改 @docs/zh/ 目录下的中文文档。中文需要流畅、准确、言简意赅。提示词也要用中文。Use subagents." Para español: "Revisa los documentos en @docs/es/. El español debe ser fluido, preciso y conciso. Use subagents." Para japonés: "@docs/ja/ のドキュメントを修正してください。日本語は流暢で正確、簡潔にしてください。Use subagents."

Modelos más potentes como Opus 4.5 también parecen ayudar. Este paso de pulido detectó frases incómodas que no eran técnicamente incorrectas pero no sonaban naturales. Combinado con subagentes, pude pulir los más de 25 documentos en cada idioma en una sola operación por lotes.

## Escalando con subagentes

Para trabajo verdaderamente paralelo, usé la función de subagentes de Claude. Al pulir las traducciones al japonés, lancé múltiples agentes de revisión simultáneamente, procesando 19 archivos con mejoras coordinadas.

La combinación de comandos slash para flujos de trabajo estructurados y subagentes para paralelización creó un pipeline de documentación que escaló mucho más allá de lo que el esfuerzo manual habría logrado.

## Los resultados

En menos de dos semanas, creé más de 20 tutoriales en inglés que cubren temas de principiante a intermedio, 81 tutoriales traducidos en 3 idiomas, calidad consistente mediante procesos de revisión automatizados, y documentación mantenible con herramientas de sincronización para traducciones.

Todos los tutoriales siguen la misma estructura, estilo de escritura y convenciones de formato porque fueron generados por el mismo proceso sistemático.

## Lecciones clave

- **Empieza manual, luego automatiza.** Haz la tarea manualmente primero, refina el proceso y luego pídele a Claude que lo guarde como un comando.
- **Estructura los comandos como flujos de trabajo de múltiples fases.** Dile a Claude cómo pensar el problema, no solo qué hacer.
- **Incorpora el control de calidad en el proceso.** Crea un comando de revisión junto con tu comando de generación.
- **Haz los comandos colaborativos, no autónomos.** Incluye pasos de aprobación. Claude maneja las partes tediosas; tú tomas las decisiones estratégicas.
- **Usa subagentes para procesamiento por lotes.** Al procesar muchos documentos, di explícitamente "Use subagents" en tu prompt. Presiona Shift+Tab primero para habilitar el modo de aceptación automática—los subagentes no pedirán permisos, haciendo el procesamiento paralelo más fluido.

## Conclusión

Construir esta biblioteca de tutoriales me enseñó que la automatización no se trata de eliminar a los humanos del proceso, sino de amplificar el juicio humano. No escribí más de 100 tutoriales manualmente, pero cada uno refleja mis estándares, mi estructura y mi aprobación.

Los comandos slash transformaron Claude Code de un asistente útil en una fábrica de documentación que trabaja bajo mi dirección, mantiene mis estándares y escala al tamaño de proyecto que necesite.

Si tienes tareas de documentación repetitivas, no sigas haciéndolas manualmente. Construye el comando slash una vez y luego despliégalo docenas o cientos de veces.

Ese es el poder de la automatización sistemática.

---

*¿Quieres ver los comandos slash que construí? Revisa la [carpeta de comandos](../assets/commands/). La biblioteca completa de tutoriales está disponible en el [sitio de documentación del proyecto](https://github.com/gexijin/vibe/tree/main/docs).*

---

**P.D.** Esta publicación de blog fue redactada por Claude Code mediante prompts iterativos:
1. "Revisa mi historial de commits y escribe una publicación de blog sobre cómo creé estos tutoriales, enfatizando mi uso de comandos slash para automatizar."
2. "Refleja que el comando /tutorial evolucionó primero a partir de prompts interactivos manuales."
3. "Enfatiza mi estilo de tutorial: práctico, enfocado, paso a paso."
4. "Añade que las traducciones al japonés llegaron primero sin comandos slash, y que Claude usó 8 subagentes en paralelo."
5. "Añade que Claude escribió los comandos slash de traducción sin pautas específicas, y que 25 tutoriales fueron traducidos en 15 minutos usando subagentes."
6. "Añade enlace a los comandos guardados en docs/assets/commands."
7. "Reescribe con menos viñetas."
8. "Lee realmente los comandos slash y añade detalles."
9. "Resume nuestra interacción en cada turno. Añade una P.D. sobre cómo se generó este blog."

Creado por [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) el 15 de diciembre de 2025.
