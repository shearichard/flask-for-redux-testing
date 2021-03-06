# Flask API for Redux Toolkit Testing 
## Summary 

A simple flask app to test the [Redux Toolkit](https://redux-toolkit.js.org/rtk-query/usage-with-typescript).

A number of API end points are provided to interact with a database of movie information.

## Online Documenation (OpenAPI/Swagger)

The API endpoints are documented as part of the project and can be accessed at http://127.0.0.1:5000/swagger and http://127.0.0.1:5000/swagger-ui .

There are some notes about how that was done [here](https://progressstory.com/tech/python/swagger-api-doc-automation-with-flask-restful/).

## Sample API calls

### Movies 

#### ADD a new movie

```
curl -X POST http://127.0.0.1:5000/movies -H 'Content-Type: application/json' -d '{"audience_score_percent": "55", "film": "Test Film 2", "genre": "Comedy", "lead_studio": "Warner Bros.", "profitability": "1.9802064", "rotten_tomatoes_percent": "8", "worldwide_gross_usd": "$69.31 ", "year": "2017"}'

```


### Todos

These Sample API calls have been copied from the [flask-restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html) documentation.

#### GET the list

```
$ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}

GET a single task

$ curl http://localhost:5000/todos/todo3
{"task": "profit!"}
```

#### DELETE a task

```
$ curl http://localhost:5000/todos/todo2 -X DELETE -v

> DELETE /todos/todo2 HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:10:32 GMT
```

#### ADD a new task

```
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v

> POST /todos HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 25
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:12:58 GMT
<
* Closing connection #0
{"task": "something new"}
```

#### UPDATE a task

```
$ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v

> PUT /todos/todo3 HTTP/1.1
> Host: localhost:5000
> Accept: */*
> Content-Length: 20
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.8.3 Python/2.7.3
< Date: Mon, 01 Oct 2012 22:13:00 GMT
<
* Closing connection #0
{"task": "something different"}


```

## TODO
Integrate [flask-restx](https://flask-restx.readthedocs.io/en/latest/) to make use of the [swagger capability](https://flask-restx.readthedocs.io/en/latest/swagger.html).

## Credits
The initial movie data, movie.csv, is from https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea which has no explicit license so I'm assuming is free to use, I'm happy to remove it from the project if anyone wishes to complain.
