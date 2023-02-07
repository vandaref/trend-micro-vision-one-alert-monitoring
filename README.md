# Alerts Monitoring Trend Micro Vision One with API, Prometheus and Grafana

Alerts Monitoring Trend Micro Vision One with API, Prometheus and Grafana sert à obtenir certaines metrics exploitables concernant les events de l'XDR Trend comme le nombre d'events total sur une durée choisie, le lien de l'event, la sevérité, etc. Il est possible par la suite de les intégrer à un outil de monitoring tel que Grafana. 

C'est un projet qui comporte :
  - un script python servant d'exporter et de colleteur Prometheus 
  - un fichier de config qui contient le token
  - un fichier de config prometheus.yml 
  - les requirements

## Prérequis
Installer [Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) ici 3.10.

Installer [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Dans Docker Desktop il faut :
  - un container [Prometheus](https://prometheus.io/)
  - (un container [Grafana](https://grafana.com/))

## Installation

Commencer par installer les libraires et les modules nécessaires.

```bash
pip install -r requirements.txt
```
Il faut également modifier le token dans le fichier **config.py** et mettre votre token Trend (droits admin nécessaires).

`token = 'YOURTOKEN'`

Modifier le fichier de config **prometheus.yml** afin de renseigner votre **IP** dans les jobs. 

```
- job_name: 'trend'
    static_configs:
      - targets: ['YOURIP:9400']
```

## Usage
Lancer le container Prometheus (et le container Grafana) via Docker Desktop puis lancer le script python **api_v1.0** dans une console Windows.

```python
python api_v1.0
```

Pour observer les résultats il faut se rendre à l'adresse : http://YOURIP:9400 

## Contribution

Toutes les contributions sont les bienvenues.

## License

[MIT](httpschoosealicense.comlicensesmit)
