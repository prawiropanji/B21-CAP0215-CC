# Users API

This API allow to get user infromation

## Endpoint

---

### Create new user

POST `/users`

Example

```
{
    "age": 21,
    "name": "Lisa",
    "sex": "f"
}
```

Output

```
{
    "age": 21,
    "id": 2,
    "name": "Lisa",
    "sex": "f",
    "skin_type": null
}
```

### List all users

GET `/users`

Output

```
[
    {
        "age": 25,
        "id": 1,
        "name": "max",
        "sex": "m",
        "skin_type": null
    },
    {
        "age": 21,
        "id": 2,
        "name": "Lisa",
        "sex": "f",
        "skin_type": null
    }
]
```

### Get single user

GET `/users/:user_id`

Example

```
GET /users/2
```

Output

```
{
    "age": 21,
    "id": 2,
    "name": "Lisa",
    "sex": "f",
    "skin_type": null
}
```

### Update user

PUT `/users/:user_id`

Example

```
PUT /users/2
```

```
{
    "age" : 24
}
```

Output

```
{
    "age": 24,
    "id": 2,
    "name": "Lisa",
    "sex": "f",
    "skin_type": null
}
```

### Delete user

DELETE `users/:user_id`

Example

```
DELETE users/2
```

Output

```
{
    "age": 24,
    "id": 2,
    "name": "Lisa",
    "sex": "f",
    "skin_type": null
}
```
