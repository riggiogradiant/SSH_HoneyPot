# import os

# log_file_path = "cowrie/var/log/cowrie/cowrie.log"
# output_file_path = "filtered_log.log"

# # Leer el archivo de log
# with open(log_file_path, "r") as file:
#     log_content = file.read()

# # Encontrar el índice del primer salto de línea
# first_newline_index = log_content.find("\n")

# # Obtener las líneas restantes después del primer salto de línea
# remaining_content = log_content[first_newline_index+1:]

# # Filtrar las líneas que contienen las frases deseadas
# filtered_lines = []
# for line in remaining_content.splitlines():
#     if "[HoneyPotSSHTransport,28,127.0.0.1] login attempt" in line or "[HoneyPotSSHTransport,28,127.0.0.1] Command found:" in line:
#         filtered_lines.append(line)

# # Guardar las líneas filtradas en otro archivo
# with open(output_file_path, "w") as file:
#     file.write("\n".join(filtered_lines))

# print("Filtered log lines have been saved to", output_file_path)

import shutil
import os

source_log_path = "cowrie/var/log/cowrie/cowrie.log"

# Leer el contenido del archivo original
with open(source_log_path, "r") as file:
    log_content = file.read()

# Obtener la posición del primer salto de línea
first_newline_index = log_content.find("\n")

# Extraer el contenido después del primer salto de línea
extracted_content = log_content[first_newline_index + 1:]

# Imprimir el contenido extraído en la consola
#print(extracted_content)

# Opcionalmente, puedes escribir el contenido en otro archivo de log
output_log_path = "log_printeado.log"
with open(output_log_path, "w") as file:
    file.write(extracted_content)

print("El contenido del log ha sido impreso.")

