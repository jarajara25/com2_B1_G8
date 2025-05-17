# Laboratorio 6 - Waveforming con Filtro Coseno Alzado

Este repositorio contiene las evidencias y resultados del **Laboratorio 7** de la asignatura **Comunicaciones II**, centrado en la formación de pulsos (waveforming) utilizando filtros de **coseno alzado** y **raíz de coseno alzado**. Las simulaciones se realizaron en **GNU Radio**, y se analizaron diferentes configuraciones de filtrado con y sin presencia de ruido, incluyendo modulación 16QAM.

## Objetivo del laboratorio

Evaluar el impacto del filtrado sobre señales moduladas, observando el comportamiento del ancho de banda, el fenómeno de interferencia intersimbólica (ISI), y la calidad de la transmisión en distintos escenarios.

## Estructura del repositorio

- `informe/`: Contiene todas las evidencias obtenidas durante el laboratorio, incluyendo capturas del dominio del tiempo, la frecuencia, constelaciones y diagramas de ojo para cada caso simulado.
- `GNURadio/`: Incluye los archivos `.grc` correspondientes a los diagramas de bloques utilizados en GNU Radio para cada experimento.

## Casos estudiados

1. Forma rectangular sin filtrado
2. Forma rectangular con filtrado
3. Filtro de coseno alzado con $\beta = 1$
4. Filtro de coseno alzado con $\beta = 0$
5. Filtro de coseno alzado con $\beta = 0.5$
6. Filtro raíz de coseno alzado con $\beta = 0.5$
7. Todos los casos anteriores aplicados a modulación 16QAM con ruido

## Evidencias registradas

Para cada experimento se documentaron:

- Señal en el dominio del tiempo (envolvente compleja)
- Densidad espectral de potencia (PSD)
- Diagrama de ojo
- Constelación
- Ancho de banda medido

## Autores

- Kevin Rueda – 2214635  
- Juan Jaramillo – 2212273  
- Eduwin Caceres – 2194665

**Universidad Industrial de Santander**  
Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones



