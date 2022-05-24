################################## README ##################################

Jaime Arturo Hurtado Romero   ja.hurtado905@uniandes.edu.co   cod. 201212121

############################################################################

Generalidades:
Se debe de extraer el archivo comprimido "TallerAproximados.zip", dentro de la carpeta encontrará una carpeta denominada source 
en donde encontrará archivos de python con extension ".py"

* main.py           --> (Interface) contiene el fujo 
* graph.py          --> (Grafos) contiene las funciones necesarias para lectura del archivo y creación del grafo.
* generate_file.py  --> (Archivos) Genear archivos con n cantidad de vertices.
* vertex_cover.py   --> (Algotitmos) contiene las funciones necesarias para ejecutar los algoritmos de cubrimiento de vertices.

Para ejecutar el algoritmo deberá ejecutar el archivo main.py desde la terminal al estar ubicado dentro de la carpeta "/source".
La ejecución del programa main.py debe contener el nombre del archivo de entrada, como se muestra en los siguientes ejemplos:

> cd ".\source"                                 <- comando para ubicarse en la carpeta source
> python ".\main.py" -i ".\data\input_100.csv"  <- comando para ejecutar el programa main.py con archivos de entrada

existe un parámetro el cual es requerido:

--input ó -i    <- parámetro que indica la ruta del archivo de entrada.

############################################################################