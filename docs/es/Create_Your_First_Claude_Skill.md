[Inicio](index.html)

# Cree su primera Claude Skill

Ha estado escribiendo manualmente `/stock-report AAPL` para generar informes. ¿Y si Claude pudiera decidir automáticamente cuándo crear un informe bursátil según su conversación? Ese es el poder de las Skills: es como cambiar de una transmisión manual a una automática que cambia de marcha cuando es necesario.

## Conceptos clave

- **Skill** - Capacidad almacenada en `.claude/skills/` que Claude activa automáticamente según el contexto
- **Invocación por modelo** - Claude decide cuándo usar la Skill leyendo su descripción, sin necesidad de escribir un comando
- **SKILL.md** - Archivo principal que contiene metadatos YAML e instrucciones para Claude

## Lo que necesitará

- Haber completado: [Crear Comandos Slash Personalizados](./Reuse_Prompts_via_Slash_Commands.md)
- Comando slash `stock-report` de ese tutorial
- VS Code instalado
- 10-15 minutos

## Paso 1: Navegue hasta la carpeta del proyecto

**Windows (WSL):**
- Abra **Ubuntu** desde el menú Inicio
- Ejecute:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Reemplace `YOUR_USERNAME` con su nombre de usuario de Windows

  Si la carpeta no existe, créela primero:
  ```bash
  mkdir -p /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```

**Mac:**
- Abra **Terminal** (Aplicaciones > Utilidades)
- Ejecute:
  ```bash
  cd ~/Documents/test_claude
  ```

  Si la carpeta no existe, créela primero:
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## Paso 2: Inicie Claude Code

Ejecute:
```
claude
```

Inicie sesión con su suscripción de Claude siguiendo el tutorial de instalación ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Después de iniciar sesión, verá un mensaje de bienvenida y el prompt de Claude Code.

## Paso 3: Active la aprobación automática de ediciones

Presione `Ctrl+E` (Windows/Linux) o `Cmd+E` (Mac) para habilitar el modo de aprobación automática.

Esto permite que Claude cree y modifique archivos sin solicitar permiso cada vez.

## Paso 4: Pídale a Claude que convierta el comando slash

Escriba este prompt:
```
Convierte mi comando slash stock-report en una Skill llamada generate-stock-reports.
La Skill debe activarse automáticamente cuando pregunte sobre empresas o acciones.
```

Claude analiza su comando slash existente y lo convierte en una Skill en `.claude/skills/stock-report/`.

**Lo que sucede:** Claude crea una nueva estructura de carpetas con `SKILL.md` que contiene metadatos YAML que indican a Claude cuándo usar esta Skill automáticamente.

## Paso 5: Revise la estructura de la Skill

Abra VS Code y vea el proyecto:
- Haga clic en **File > Open Folder**
- Seleccione `Documents/test_claude`
- En el explorador de archivos, navegue hasta `.claude/skills/stock-report/`
- Haga clic en `SKILL.md` para abrirlo

Observe la estructura:
```yaml
---
name: stock-report
description: Genera informes sobre empresas... Usar cuando los usuarios pregunten sobre acciones, empresas o símbolos bursátiles.
---

[Resto de las instrucciones]
```

El campo `description` es clave: le indica a Claude exactamente cuándo activar esta Skill automáticamente.

## Paso 6: Pruebe la Skill (sin escribir un comando)

En lugar de escribir `/stock-report AAPL`, simplemente haga una pregunta natural:
```
¿Qué está pasando con Apple últimamente?
```

**La diferencia clave:** No escribió un comando. Claude lee su pregunta, reconoce que está preguntando sobre una empresa, revisa las descripciones de las Skills y decide automáticamente usar la Skill stock-report.

Observe cómo trabaja Claude: debería generar el mismo informe completo que vio antes.

## Paso 7: Compare los dos enfoques

**Comando Slash (manual):**
```
/stock-report AAPL
```
- Usted le dice explícitamente a Claude qué hacer
- Siempre funciona igual
- Útil para tareas repetitivas y predecibles

**Skill (automática):**
```
Cuéntame sobre los desarrollos recientes de Tesla
```
o
```
Estoy pensando en invertir en Microsoft
```
o
```
¿Qué está haciendo NVIDIA?
```
- Claude decide si usar la Skill
- Conversación más natural
- Útil para flujos de trabajo complejos que Claude administra por usted

## Paso 8: Pruebe casos límite

Pruebe preguntas que NO deberían activar la Skill de informe bursátil:
```
¿Cómo instalo Python?
```

Claude responde normalmente sin invocar la Skill.

Ahora pruebe una pregunta que SÍ debería activarla:
```
Compara Google y Meta
```

Claude debería usar la Skill dos veces: una para Google y otra para Meta.

## Paso 9: Modifique la descripción de la Skill (opcional)

Hagamos que la Skill sea más selectiva. Pídale a Claude:
```
Actualiza la Skill stock-report para que solo se active cuando mencione explícitamente
"analizar" o "informe" junto con el nombre de una empresa.
```

Claude actualiza el campo `description` en `SKILL.md`. Pruebe la diferencia:
```
¿Qué está haciendo Apple?
```
(Puede que no active la Skill ahora)

```
Analiza Apple
```
(Debería activar la Skill)

## Próximos pasos

Ahora que comprende las Skills, cree más para sus flujos de trabajo:

- **Research Skill** - Se activa automáticamente cuando hace preguntas que requieren búsqueda web
- **Code Review Skill** - Se activa cuando menciona errores o problemas de código
- **Meeting Notes Skill** - Se activa cuando pega transcripciones de reuniones o menciona resúmenes

El patrón: defina cuándo Claude debe ayudar automáticamente, no solo atajos que usted activa manualmente.

## Solución de problemas

- **La Skill no se activa:** Verifique el campo `description` en `SKILL.md`: debe incluir palabras clave relacionadas con su pregunta
- **La Skill se activa con demasiada frecuencia:** Haga la descripción más específica sobre cuándo usarla
- **No encuentra la carpeta de la Skill:** Las Skills están en `.claude/skills/` (carpeta oculta: habilite "Mostrar archivos ocultos" en su explorador de archivos)
- **Los cambios en SKILL.md no funcionan:** Las Skills se cargan automáticamente al modificarse: no es necesario reiniciar. Si persiste el problema, verifique el formato YAML

## Resumen del flujo de trabajo

- **Los comandos slash** son atajos que usted escribe manualmente (como marcadores)
- **Las Skills** son capacidades que Claude descubre y usa automáticamente (como un asistente que conoce sus preferencias)
- **Las descripciones de Skills** actúan como instrucciones que indican a Claude: "Úsame cuando el usuario diga X"
- **Ambos pueden coexistir** - Use comandos slash para tareas rápidas y repetitivas; use Skills para flujos de trabajo complejos
- **Las Skills escalan mejor** - No necesita recordar nombres de comandos; Claude decide según el contexto

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 13, 2025.
