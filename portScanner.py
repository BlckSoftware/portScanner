# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:34:28 2023

@author: hkarayazim
"""
import func
import subprocess
import sys

func.welcome_screen("PORT SCANNER",5)
while True:
    ipconfig_output = subprocess.check_output(['ipconfig'])
    
    decoded_data = ipconfig_output.decode('cp857') 
    
    
    decoded_data=decoded_data.replace('\r\n',"\n")
    print("\033[0;33m",decoded_data,"\033[0m\n")
    print("""\033[0;35m
          Yukarıda Bu Cihazın Bütün Network Konfigürasyonunu Görebilirsiniz...
          İsterseniz Uzaktaki Bir Cihazında Portlarını Kontrol Edebilirsiniz.
          İki Aralık Arasındaki Portları da Kontrol Edebilirsiniz.
          Şimdi Lütfen Hedef IP Adresini Yazınız: \033[0m\n\n""")
    ipaddress=input()
    print("\nTarama yapmak istediğiniz portların başlangıcını yazın\n ")
    startPort=input()
    print("\nTarama yapmak istediğiniz portların sonunu yazın\n ")
    endPort=input()
    startPort=int(startPort)
    endPort=int(endPort)
    print("\nPort Scanning İşlemi Başladı Lütfen Bekleyin ...\n")
    func.port_scan(ipaddress,startPort,endPort)
    
    
    cevap = input("\n\nDevam etmek istiyor musunuz? (E/H)")
    if cevap.upper() == "H":
            break   # döngüden çık