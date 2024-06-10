# Play Fast Dice

This is game of dice, under format API.

## Deploy
- `fastapi dev main.py`
- Using Visual Studio Code, play debug mode on `main.py` file

## Request to play

Request:
- `http://0.0.0.0:8000/api/dice/play`

Method:
- `GET`

Header:
- `Accept`: `[application/json]`

Parameters:
- Quantity `[1-5]`
- Face `[4,6,8,10,12,13,14,15,16,17,18,19,20]`

Description:

- `Face` is not required and default value is `6`.
- `Quantity` is not required and default value is `1`.

Response Json to quantity `3`, face `6`:
```
{
    "dice": [
        2,
        4,
        1
    ]
}
```

## Doc
- `http://localhost:8000/docs`

## FAST API
- https://fastapi.tiangolo.com/

## Enable to use with REST Client - see request folder
- Name: REST Client
- Id: humao.rest-client
- Description: REST Client for Visual Studio Code
- Version: 0.25.1
- Publisher: Huachao Mao
- VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
