# Places API
- Api service for contains and manipulate places written on DRF

## Installing using GitHub:
 - Open .env.sample and change environment variables on yours !Rename file from .env_sample to .env

```shell
git clone https://github.com/bythewaters/webapp-with-postgis-technologis.git
cd webapp-with-postgis-technologis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run with Docker:
- Docker should be installed
```
- docker-compose build
- docker-compose up
```
- Use the following command to load prepared data from fixture in docker(if you need):
  `docker-compose run --rm app python manage.py loaddata places_fixture.json`

## Getting access:
- via /api/doc/swagger/ --> Detail api documentation by swagger
- via [POST] /api/places/ --> Add new place
- via [GET] /api/places/ --> Places list
- via [GET] /api/places/?coordinate=40.34,30.16 --> Places list nearest to coordinates
- via [GET] /api/places/pk/ --> Place detail information
- via [PUT, PATCH] /api/places/pk/ --> Update place information
- via [DELETE] /api/places/pk/ --> Delete place
