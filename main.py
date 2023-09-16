from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.common.result_template import ResResult
from models.users import Users


app = FastAPI()


@app.get("/")
async def hello_world():
    data_hello = {"hello": "world"}

    users: list[Users] = [
        Users(
            name="Jatidthaa",
            surname="sanpimpha",
            age=30,
            height=164,
            weight=65
        ),
        Users(
            name="Mike",
            surname="McDavid",
            age=28,
            height=170,
            weight=57
        )
        ,
        Users(
            name="Rob",
            surname="Richmond",
            age=55,
            height=185,
            weight=70
        )
    ]

    res = ResResult(
        success=True,
        message="success",
        data=users
    )

    return JSONResponse(status_code=status.HTTP_200_OK, content=res.model_dump())
