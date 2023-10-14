#!/usr/bin/python3

import os
import sys
from termcolor import cprint
import pyfiglet

# Funciones para verificar si un programa está instalado
def is_program_installed(program_name):
    return os.system(f"which {program_name} > /dev/null 2>&1") == 0

# Funciones para las opciones básicas de UFW
def configure_ufw():
    os.system("sudo ufw enable")

def verify_ufw():
    os.system("sudo ufw status")

def install_ufw():
    os.system("sudo apt-get install ufw")

# Nuevas funciones para las opciones adicionales de UFW
def update_ufw_rules():
    os.system("sudo ufw reload")

def view_ufw_rules():
    os.system("sudo ufw status numbered")

def add_ufw_rule():
    port = input("Introduce el número de puerto para permitir (ej. 80): ")
    os.system(f"sudo ufw allow {port}")

def delete_ufw_rule():
    rule_num = input("Introduce el número de regla a eliminar: ")
    os.system(f"sudo ufw delete {rule_num}")

def ufw_menu():
    while True:
        print("\nSelecciona una acción para UFW:")
        print("1. Configurar UFW")
        print("2. Verificar UFW")
        print("3. Instalar UFW")
        print("4. Volver al menú principal")
        ufw_choice = input("Opción: ")
        
        if ufw_choice == "1":
            while True:
                print("\nSelecciona una opción para configurar UFW:")
                print("1. Agregar regla a UFW")
                print("2. Eliminar regla de UFW")
                print("3. Actualizar reglas de UFW")
                print("4. Ver reglas de UFW")
                print("5. Volver al menú anterior")
                ufw_config_choice = input("Opción: ")
                if ufw_config_choice == "1":
                    print("Agregando regla a UFW...")
                    add_ufw_rule()
                    print("Regla agregada a UFW.")
                elif ufw_config_choice == "2":
                    print("Eliminando regla de UFW...")
                    delete_ufw_rule()
                    print("Regla eliminada de UFW.")
                elif ufw_config_choice == "3":
                    print("Actualizando reglas de UFW...")
                    update_ufw_rules()
                    print("Reglas de UFW actualizadas.")
                elif ufw_config_choice == "4":
                    print("Verificando reglas de UFW...")
                    view_ufw_rules()
                elif ufw_config_choice == "5":
                    break
                else:
                    print("Opción no válida.")

        elif ufw_choice == "2":
            print("Verificando UFW...")
            verify_ufw()
        elif ufw_choice == "3":
            if not is_program_installed("ufw"):
                print("UFW no está instalado. ¿Quieres instalarlo? (y/n)")
                install_choice = input("Opción: ")
                if install_choice.lower() == "y":
                    print("Instalando UFW...")
                    install_ufw()
                    print("UFW instalado correctamente.")
            else:
                print("UFW ya está instalado.")
        elif ufw_choice == "4":
            return
        else:
            print("Opción no válida. Regresando al menú principal.")

# Funciones para las opciones básicas de Firewalld
def configure_firewalld():
    os.system("sudo systemctl enable firewalld")
    os.system("sudo systemctl start firewalld")

def verify_firewalld():
    os.system("sudo firewall-cmd --state")

def install_firewalld():
    os.system("sudo yum install firewalld")

# Nuevas funciones para las opciones adicionales de Firewalld
def add_firewalld_rule():
    port = input("Introduce el número de puerto para permitir (ej. 80): ")
    os.system(f"sudo firewall-cmd --zone=public --add-port={port}/tcp --permanent")
    os.system("sudo firewall-cmd --reload")

def delete_firewalld_rule():
    port = input("Introduce el número de puerto a eliminar (ej. 80): ")
    os.system(f"sudo firewall-cmd --zone=public --remove-port={port}/tcp --permanent")
    os.system("sudo firewall-cmd --reload")

def firewalld_menu():
    while True:
        print("\nSelecciona una acción para Firewalld:")
        print("1. Configurar Firewalld")
        print("2. Verificar Firewalld")
        print("3. Instalar Firewalld")
        print("4. Volver al menú principal")
        firewalld_choice = input("Opción: ")
        
        if firewalld_choice == "1":
            while True:
                print("\nSelecciona una opción para configurar Firewalld:")
                print("1. Agregar regla a Firewalld")
                print("2. Eliminar regla de Firewalld")
                print("3. Volver al menú anterior")
                firewalld_config_choice = input("Opción: ")
                if firewalld_config_choice == "1":
                    print("Agregando regla a Firewalld...")
                    add_firewalld_rule()
                    print("Regla agregada a Firewalld.")
                elif firewalld_config_choice == "2":
                    print("Eliminando regla de Firewalld...")
                    delete_firewalld_rule()
                    print("Regla eliminada de Firewalld.")
                elif firewalld_config_choice == "3":
                    break
                else:
                    print("Opción no válida.")

        elif firewalld_choice == "2":
            print("Verificando Firewalld...")
            verify_firewalld()
        elif firewalld_choice == "3":
            if not is_program_installed("firewalld"):
                print("Firewalld no está instalado. ¿Quieres instalarlo? (y/n)")
                install_choice = input("Opción: ")
                if install_choice.lower() == "y":
                    print("Instalando Firewalld...")
                    install_firewalld()
                    print("Firewalld instalado correctamente.")
            else:
                print("Firewalld ya está instalado.")
        elif firewalld_choice == "4":
            return
        else:
            print("Opción no válida. Regresando al menú principal.")

# Funciones para las opciones básicas de iptables
def configure_iptables():
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -P FORWARD DROP")
    os.system("sudo iptables -P OUTPUT ACCEPT")
    os.system("sudo iptables -F")

def verify_iptables():
    os.system("sudo iptables -L")

# Nuevas funciones para las opciones adicionales de iptables
def add_iptables_rule():
    chain = input("Introduce la cadena en iptables (ej. 'INPUT'): ")
    port = input("Introduce el número de puerto para permitir (ej. 80): ")
    os.system(f"sudo iptables -A {chain} -p tcp --dport {port} -j ACCEPT")

def delete_iptables_rule():
    chain = input("Introduce la cadena en iptables (ej. 'INPUT'): ")
    rule_num = input("Introduce el número de regla a eliminar: ")
    os.system(f"sudo iptables -D {chain} {rule_num}")

def iptables_menu():
    while True:
        print("\nSelecciona una acción para iptables:")
        print("1. Configurar iptables")
        print("2. Verificar iptables")
        print("3. Volver al menú principal")
        iptables_choice = input("Opción: ")
        
        if iptables_choice == "1":
            while True:
                print("\nSelecciona una opción para configurar iptables:")
                print("1. Agregar regla a iptables")
                print("2. Eliminar regla de iptables")
                print("3. Volver al menú anterior")
                iptables_config_choice = input("Opción: ")
                if iptables_config_choice == "1":
                    print("Agregando regla a iptables...")
                    add_iptables_rule()
                    print("Regla agregada a iptables.")
                elif iptables_config_choice == "2":
                    print("Eliminando regla de iptables...")
                    delete_iptables_rule()
                    print("Regla eliminada de iptables.")
                elif iptables_config_choice == "3":
                    break
                else:
                    print("Opción no válida.")

        elif iptables_choice == "2":
            print("Verificando iptables...")
            verify_iptables()
        elif iptables_choice == "3":
            return
        else:
            print("Opción no válida. Regresando al menú principal.")

# El menú principal ahora incluye opciones numéricas y para agregar y eliminar reglas.
def main_menu():
    #cprint("FIREWALLAUT", "red", attrs=["bold"])
    print("BIENVENIDO AL CONFIGURADOR DE FIREWALLS.\n")
    if os.geteuid() != 0:
        print("DEBES EJECUTAR ESTE SCRIPT COMO SUDO.")
        print("POR FAVOR, VUELVE A EJECUTARLO USANDO 'sudo'.")
        sys.exit(1)

    while True:
        print("SELECCIONA UNA OPCIÓN:")
        print("1. UFW")
        print("2. FIREWALLD")
        print("3. IPTABLES")
        print("4. SALIR")
        choice = input("OPCIÓN: ")

        if choice == "1":
            ufw_menu()
        elif choice == "2":
            firewalld_menu()
        elif choice == "3":
            iptables_menu()
        elif choice == "4":
            sys.exit(0)
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("FIREWALLAUT")
    cprint(ascii_banner, "red", attrs=["bold"])
    print("BY JOSH...........v1.0\n")
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nSALIENDO...")

