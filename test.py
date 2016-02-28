#!/usr/bin/python26
# -*-coding:Latin-1 -*
#importer les modules à utiliser
import nmap
import sys
import os


#Afficher le message d'Accueil
print('Bienvenue sur Selfy!')

#Entrer les informations sur la machine à explorer
host = raw_input('Entrer le nom votre serveur: ')
print("le nom de votre hote est ", host)
print('Traitement en cours, Veuillez patienter s \'il vous plait!')
nm = nmap.PortScanner()
nm.scan(host,'22-443')
nm.command_line()                   # Obtenir la ligne de commande utiliser pour le scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo()                       # Obtenir les informations du scan {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()                      # Obtenir la liste de tous les hotes scannés
nm[host].hostname()          # Obtenir le nom de l'hote scannée
nm[host].hostnames()         # Obtenir la liste des hotes scannées et les rendre sous la forme [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
nm[host].state()             # Obtenir le statut des ports scannées (up|down|unknown|skipped) 
nm[host].all_protocols()     # Obtenir la liste de tous les protocoles scannées ['tcp', 'udp'] in (ip|tcp|udp|sctp)
if ('tcp' in nm[host]):
    list(nm[host]['tcp'].keys()) # Obtenir la liste de tous les ports scannés pour le protocole tcp

nm.nmap_version()
nm[host].all_tcp()           # Obtenir la liste de tous les ports pour le protocole tcp
nm[host].all_udp()           # Obtenir la liste de tous les ports pour le protocole udp
nm[host].all_ip()            # Obtenir la liste de tous les ports pour le protocole ip
nm[host].all_sctp()          # Obtenir la liste de tous les ports pour le protocole sctp
if nm[host].has_tcp(22):     # Toutes les informations consernant le port 22/tcp 
    nm[host]['tcp'][22]          # Obtenir les infos sur le port 22/tcp consernant l'hote scannée
    nm[host].tcp(22)             # Obtenir les infos sur le port 22/tcp consernant l'hote scannée
    nm[host]['tcp'][22]['state'] # Obtenir le statut sur le port 22/tcp consernant l'hote scannée

###################################################################################################
# Detecttion du Système d'exploitation (Avoir les droits Super Administrateur)"
    nm.scan(host, arguments="-O")
    if 'osmatch' in nm[host]:
        for osmatch in nm[host]['osmatch']:
            os1=('OsMatch.name : {0}'.format(osmatch['name']))
            os2=('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
            os3=('OsMatch.line : {0}'.format(osmatch['line']))
            os4=('')

            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    os5=('OsClass.type : {0}'.format(osclass['type']))
                    os6=('OsClass.vendor : {0}'.format(osclass['vendor']))
                    os7=('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                    os8=('OsClass.osgen : {0}'.format(osclass['osgen']))
                    os9=('OsClass.accuracy : {0}'.format(osclass['accuracy']))
#                    
###################################################################################################


#Impression des resultats:
#for host in nm.all_hosts():
#    print('----------------------------------------------------')
#    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
#    print('State : {0}'.format(nm[host].state()))
#
#    for proto in nm[host].all_protocols():
#        print('----------')
#        print('Protocol : {0}'.format(proto))
#
#        lport = list(nm[host][proto].keys())
#        lport.sort()
#        for port in lport:
#            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
#
#print('----------------------------------------------------')

# imprimer en format CSV
res=nm.csv()
# Ouverture du fichier destination
fichier=open("resultat2.csv", "w")
fichier.write(res)
# Fermeture du fichier destination
fichier.close()
#fichier=open("os.csv", "w")
#fichier.write(os1)
#fichier.write("\n")
#fichier.write(os2)
#fichier.write("\n")
#fichier.write(os3)
#fichier.write("\n")
#fichier.write(os4)
#fichier.write("\n")
#fichier.write(os5)
#fichier.write("\n")
#fichier.write(os6)
#fichier.write("\n")
#fichier.write(os7)
#fichier.write("\n")
#fichier.write(os8)
#fichier.close()


