# count-web-app

[Components and Sequence UML diagrams](https://viewer.diagrams.net/?page-id=kQxDTNGZS0dU6C5CenBT&highlight=0000ff&edit=_blank&layers=1&nav=1#G1i6e1X1B5qNN8GDrz3-xgTLZgqF5JNlaj)

### Sample request:
```code
  POST http://127.0.0.1/count/increase HTTP/1.1
  content-type: application/json

  {"num" : 3}
```

### Possible responses:
```code
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 25

{
  "increased_num": 4
}
```

```code
HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Content-Length: 38

{
  "error": "3 exists in database"
}
```
```code
HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Content-Length: 40

{
  "error": "3+1 exists in database"
}
```

### Responses for erroneous data
```code
POST http://127.0.0.1/count/increase HTTP/1.1

HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Content-Length: 31

{
  "error": "Expected json"
}
```
```code
POST http://127.0.0.1/count/increase HTTP/1.1
content-type: application/json

{"num" : "str"}

HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Content-Length: 57

{
  "error": "Expected \"num\" to be a natural number"
}
```
