This is a crud person mini-api using django, djangorestframework and postgresql

Funcioons

- PersonDeleteView
- PersonListCreateView
- PersonDetailView
- AllPersonListView
- PresonUpdateView

linux

```
source venv/bin/actiave
```
windows



```
./venv/Scripts/activate
```
[https://docs.docker.com/engine/install/ubuntu/
](https://docs.docker.com/engine/install/)

Run the postgres database

```
docker run --name postgres-db -p 5432:5432 -e POSTGRES_DB=root -e POSTGRES_USER=root -e POSTGRES_PASSWORD=123 -d postgres
```


