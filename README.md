# automaticPlagiarism_diplodatos
Repositorio destinado a la propuesta de Mentoría: "Detección Automática de Plagio", para la Diplomatura de Ciencia de Datos, Aprendizaje Automático y sus Aplicaciones, Cohorte 2023

# Intrinsic Plagiarism

Detección Intrínseca de Plagio

## Se debe descargar el dataset para la detección intrínseca de plagio (PAN-PC-2011)

Se descargar el dataset de:

  1. [https://zenodo.org/record/3250095#.YifVtXrMLIU](https://zenodo.org/record/3250095#.YifVtXrMLIU)
  2. Se crea una carpeta denominada "intrinsic", dentro de la carpeta "intrinsic-plagiarism", y se copian (y descomprimen) los archivos en dicha carpeta.
  3. Se crea una carpeta denominada "corpus" dentro de la carpeta "intrinsic-plagiarism".
  4. Luego debemos dirigirnos a la carpeta intrinsic y seguir la siguiente ruta:
	\pan-plagiarism-corpus-2011\intrinsic-detection-corpus\suspicious-document
	
	En dicha carpeta se encuentran carpetas (part1, part2, ..., part_10) con los documentos .txt y sus respectivos .xml.
	Se debe correr el script copiar-corpus.py para copiar todos esos archivos en una misma carpeta (carpeta corpus)