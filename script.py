#!/usr/bin/python26
# -*-coding:Latin-1 -*
#importer les modules à utiliser
import nmap
import doNikto

#Afficher le message d'Accueil
print('Bienvenue sur Selfy!')

#Entrer les informations sur la machine à explorer
host = raw_input('Entrer le nom votre serveur: ')
print("le nom de votre hote est ", host)

#Definir les ports
ports="1,1024,1521,1433,80,443,1443,1080,2443,2080,3443,3080,4443,4080,5443,5080,6443,6080,7443,7080,8443,8080,9443,9080,10443,10080,11443,11080,12443,12080,13443,13080,14443,14080,15443,15080,16443,16080,17443,17080,18443,18080,1521,3306,3389,5432,6667,389,110,53,23,25,22,21,3128"
#Definir les options
nmops = "-O -sV -T4"
#Effectuer la recherche de vulnérabilité
nma = nmap.PortScannerAsync()

def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)

nma.scan(hosts='192.168.0.0/30', arguments='-sP', callback=callback_result)

while nma.still_scanning():
    print("Waiting ...")
    nma.wait(2)   # you can do whatever you want but I choose to wait after the end of the scan

if (os.getuid() == 0):
    print('----------------------------------------------------')
    # Os detection (need root privileges)
    nm.scan("127.0.0.1", arguments="-O")
    if 'osmatch' in nm['127.0.0.1']:
        for osmatch in nm['127.0.0.1']['osmatch']:
            print('OsMatch.name : {0}'.format(osmatch['name']))
            print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
            print('OsMatch.line : {0}'.format(osmatch['line']))
            print('')

            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    print('OsClass.type : {0}'.format(osclass['type']))
                    print('OsClass.vendor : {0}'.format(osclass['vendor']))
                    print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                    print('OsClass.osgen : {0}'.format(osclass['osgen']))
                    print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                    print('')


    if 'fingerprint' in nm['127.0.0.1']:
        print('Fingerprint : {0}'.format(nm['127.0.0.1']['fingerprint']))


    # Vendor list for MAC address
    print('scanning localnet')
    nm.scan('192.168.0.0/24', arguments='-O')
    for h in nm.all_hosts():
        print(h)
        if 'mac' in nm[h]['addresses']:
            print(nm[h]['addresses'], nm[h]['vendor'])



print('----------------------------------------------------')
# Read output captured to a file
# Example : nmap -oX - -p 22-443 -sV 127.0.0.1 > nmap_output.xml

with open("./nmap_output.xml", "r") as fd:
    content = fd.read()
    nm.analyse_nmap_xml_scan(content)
    print(nm.csv())



print('----------------------------------------------------')
# Progressive scan with generator
nm = nmap.PortScannerYield()
for progressive_result in nm.scan('127.0.0.1/24', '22-25'):
    print(progressive_result)


# imprimer en format CSV
res=nma.csv()
# Ouverture du fichier destination
fichier=open("resultat1.csv", "w")
fichier.write(res)
