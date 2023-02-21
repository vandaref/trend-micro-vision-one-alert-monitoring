# Alerts Monitoring : Trend Micro Vision One with API, Prometheus and Grafana

Alerts Monitoring : Trend Micro Vision One with API, Prometheus and Grafana sert à obtenir certaines metriques exploitables concernant les events de l'XDR Trend comme le nombre d'events total sur une durée choisie, le lien de l'event, la sevérité, etc. Il est possible par la suite de les intégrer à un outil de monitoring tel que Grafana. 

![](https://github.com/vandaref/trend-micro-vision-one-alert-monitoring/blob/main/grafana_dashboard.PNG)

C'est un projet qui comporte :
  - un script python servant d'exporter et de colleteur Prometheus 
  - un fichier de config qui contient le token
  - un fichier de config prometheus.yml 
  - les requirements

## Prérequis
Installer [Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) (3.10).

Installer [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Créer un fichier **prometheus.yml** vide ou récupérer celui du projet.

Dans Docker Desktop il faut :
  - un container [Prometheus](https://prometheus.io/) (v2.29.2)
  - un container [Grafana](https://grafana.com/) (latest version)

Dans **Windows PowerShell** :
```
docker run -d -p 9090:9090 --name prometheus -v /VOTRECHEMIN/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus:v2.29.2
docker run -d -p 3000:3000 --name grafana grafana/grafana:latest
```
![](https://github.com/vandaref/trend-micro-vision-one-alert-monitoring/blob/main/docker_desktop.PNG)
## Installation

Commencer par installer les libraires et les modules nécessaires.

```bash
pip install -r requirements.txt
```
Il faut modifier le token dans le fichier **config.py** et mettre votre token Trend (droits admin nécessaires).

`token = 'YOURTOKEN'`

Modifier également le fichier de config **prometheus.yml** (/VOTRECHEMIN/prometheus.yml) afin de renseigner votre **IP** dans les jobs. 

```
global:
  scrape_interval: 5s
  external_labels:
    monitor: 'node'
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['YOURIP:9090'] ## IP Address of the localhost. Match the port to your container port
  - job_name: 'vision_one'
    static_configs:
      - targets: ['YOURIP:9400']
```

## Usage
Lancer le container Prometheus et le container Grafana via Docker Desktop puis lancer le script python **api.py** dans une console Windows.

```python
python api.py
```

Pour observer les métrics il faut se rendre à l'adresse : http://YOURIP:9400.

Pour créer votre dashboard il faut se rendre sur : http://YOURIP:3000.

Sur Grafana, renseigner la data source Prometheus avec l'adresse que vous avez attribuée (http://YOURIP:9090). 

## Documentation
[Guide API Trend](https://automation.trendmicro.com/xdr/Guides/First-Steps-Toward-Using-the-APIs)

[API utilisée](https://automation.trendmicro.com/xdr/api-beta)

[Cacher une colonne sur Grafana](https://community.grafana.com/t/hide-column-in-table-in-v8-0/49040/7)

[Faire un exporter Prometheus en Python](https://www.dadall.info/article643/comment-prendre-un-peu-de-python-pour-faire-un-exporter-prometheus)

## Contribution

Toutes les contributions sont les bienvenues.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
