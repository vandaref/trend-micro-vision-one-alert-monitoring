import requests                                                                       
import config                                       
# pour utiliser les requests
# pour utiliser le token

from prometheus_client import start_http_server, REGISTRY 
from prometheus_client.core import GaugeMetricFamily
# pour lancer le serveur et faire un registry 
# pour utiliser les metrics de prometheus

from time import sleep                              
from datetime import datetime, timedelta           
# pour mettre un sleep
# pouvoir utiliser la datetime et le timedelta

nb_jours = 1                                        
now =  datetime.today()                             
start = now - timedelta(days=nb_jours, hours=+1)    
# nombre de jours pour le début de la collecte d'events
# date de maintenant                                                    
# date de début (+ une heure pour les résultats exacts)

nowstr = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')     
startstr = start.strftime('%Y-%m-%dT%H:%M:%S.000Z') 
# "maintenant" en format string (cf. doc api trend plus haut), depuis un format ISO 8601
# date de debut dans le format string correspondant (se réferrer à la docde l'api trend), depuis un format ISO 8601

class Collector(object):           
 # on crée un objet                        
    def __init__(self):                                     
        pass
    # initiation de l'objet

    def collect(self):                                      
    # collecte des données que l'on veut exploiter

        url_base = 'https://api.eu.xdr.trendmicro.com'      
        url_path = '/beta/siem/events'    
        token = config.token                                
        # (mon) token d'authentification récupéré via trend, il faut un compte admin, sans ça on ne peut pas exploiter l'api

        query_params = {'startDateTime': startstr, 'endDateTime' : nowstr, 'sortBy' : 'score'} 
        # parametres à prendre en compte pour le résultat souhaité

        # autres params possibles :
        # 'source': 'YOUR_SOURCE (string)',
        # 'startDateTime': 'YOUR_STARTDATETIME (string)',
        # 'endDateTime': 'YOUR_ENDDATETIME (string)',
        # 'investigationStatus': 'YOUR_INVESTIGATIONSTATUS (string)',
        # 'sortBy': 'YOUR_SORTBY (string)',
        # 'queryTimeField': 'YOUR_QUERYTIMEFIELD (string)',
        # 'offset': 'YOUR_OFFSET (integer)',
        # 'limit': 'YOUR_LIMIT (integer)'

        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json;charset=utf-8'}
        # ce que contient les headers, ici le tocker et le type de contenu

        r = requests.get(url_base + url_path, params=query_params, headers=headers)
        # la requete avec tous les éléments
        
        records = r.json()['data']['workbenchRecords']      
        totalCount = r.json()['data']['totalCount']         
        # cela prend en compte tout ce qu'il y a dans les workbenchRecords (plusieurs résultats)
        # cela prend en compte le nombre total d'event (un seul résultat)

        metric_total_event = GaugeMetricFamily('total_event', "Nombre d'events au cours des dernières 24h", labels=['nombre_event'])    
        metric_priority_event = GaugeMetricFamily('priority_event', "Les priorités des derniers events (+ nom, severité et lien)", labels=['workbenchName', 'severity', 'workbenchLink'])   
        # on crée la métric pour le nombre d'event
        # metric pour les infos supplémentaires
                                                                                                                                       
        metric_total_event.add_metric(labels=["24h"], value=totalCount) 
        # on ajoute la metric total_event

        for record in records:  
        # on parcourt tous les éléments dans les workbenchRecords

            metric_priority_event.add_metric(labels=[record['workbenchName'], record["severity"], record["workbenchLink"]], value=record['priorityScore']) 
            # pour chaque event on ajoute les informations voulues
                                                                                                        
        yield metric_total_event        
        yield metric_priority_event 
        # on yield les deux metrics pour retourner les valeurs

if __name__ == "__main__":      
    start_http_server(9400)     
    REGISTRY.register(Collector())
    while True: sleep(10)
    # on lance le serveur sur le port 9400
