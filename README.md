# Learn FastAPI by Coding

Open-source project provided by AppSeed to help beginners accommodate faster with FastAPI. For newcomers, FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 

> **For support and more [Free Samples](https://appseed.us/admin-dashboards/open-source) join [AppSeed](https://appseed.us).**

<br />

## Getting Started with FastAPI

> Create a Virtual Environment

```bash
$ # Virtualenv modules installation (Unix-based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows-based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> Install `FastAPI` and `uvicorn`

```bash
$ pip install fastapi
$ pip install uvicorn
```

<br />

> Edit your first file `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
```

<br />

> Start the app using `uvicorn` 

```bash
$ uvicorn main:app --reload
$ 
$ The project is LIVE - https://localhost:8000 
```

<br />

> Visualize auto-generated docs

- OpenAPI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

<br />

--- 
Learn Django by Coding - Provided and actively supported by AppSeed [App Generator](https://appseed.us)
