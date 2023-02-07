# Alertes sécurité Trend sur Grafana

Alertes sécurité Trend sur Grafana sert à mettre en place les alertes de sécurité de Trend sur Grafana.
C'est un projet qui comporte un script python servant d'exporter Prometheus et de colleteur. Il y a également un fichier config et les requirements.

## Prérequis
Il faut un container Prometheus et un Grafana. 

De plus penser à ajouter le job 'trend' au fichier de config prometheus.yml qui écoute sur le port 9400. 

## Installation

Commencer par installer les libraires et les modules nécessaires.

```bash
pip install -r requirements.txt
```
Il faut également modifier le token dans le fichier config.py et mettre votre token Trend admin.

## Usage
Lancer le container Prometheus, le Grafana et le script python.

```python
python api_v1.0
```

## Contribution

Toutes les contributions sont les bienvenues.

## License

[MIT](httpschoosealicense.comlicensesmit)