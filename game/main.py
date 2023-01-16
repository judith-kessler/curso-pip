# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 07:52:55 2022

@author: Judith
"""
import random 
opciones=("piedra", "papel", "tijera")
c_c=0
c_u=0
r=1

while True:
    print("*"*20)
    print("Ronda "+ str(r))
    print("*"*20)
    print("compu: "+ str(c_c) + " vos: "+ str(c_u))
    si=False
    while si==False:
        opcion_u=(input("piedra, papel o tijera: ")).lower()
        if not opcion_u  in opciones:
            si=False
            print(opcion_u + " no es válido")
        else:
            si=True
        
    opcion_c=random.choice(opciones)

    print("elegiste: ", opcion_u)
    print("la compu eligió: ", opcion_c)

    if opcion_u==opcion_c:
        print("empate!")
    elif opcion_u=="piedra":
        if opcion_c=="papel":
            print("papel envuelve a piedra")
            print("perdiste!")
            c_c+=1
        else:
            print("piedra rompe a tijera")
            print("ganaste")
            c_u+=1
        
    elif opcion_u=="papel":
        if opcion_c=="piedra":
            print("papel envuelve a piedra")
            print("ganaste!")
            c_u+=1
        else:
            print("tijera corta a papel")
            print("perdiste")
            c_c+=1
    elif opcion_u=="tijera":
        if opcion_c=="piedra":
            print("piedra rompe a tijera")
            print("perdiste!")
            c_c+=1
        else:
            print("tijera corta a papel")
            print("ganaste")
            c_u+=1
    
    r+=1
    
    if c_c == 2:
        print("ganó la compu")
        break
    
    if c_u == 2:
        print("ganaste")
        break