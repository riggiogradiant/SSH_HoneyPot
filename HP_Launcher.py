import subprocess

# Ejecutar pro1.py
subprocess.run(["python3", "client_HP.py"])

# Ejecutar pro2.py después de que pro1.py haya terminado
subprocess.run(["python3", "filtro.py"])
