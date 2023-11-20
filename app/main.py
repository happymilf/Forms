import json

from pathlib import Path




from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from database import DataBase, FieldType, Form

BASE_DIR : Path = Path(__name__).resolve().parent



database : DataBase = DataBase(db_name="database")


w_app : FastAPI = FastAPI()
w_app.mount("/static", StaticFiles(directory=f"static"), name="static")


templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@w_app.get("/", response_class=HTMLResponse)
def index(request: Request) -> str:
    return templates.TemplateResponse("index.html", {"request" : request})

@w_app.get("/form/create", name="form_create")
def form_create(request : Request):
    return templates.TemplateResponse("form_create.html", {"request" : request})

@w_app.post("/get_form")
async def get_form(request : Request):
    print((await request.body()))
    search_pattern : dict[str, str] = json.loads((await request.body()))

    result_name : str = ""
    result_json : dict[str, str] = {}
    #database.search(search_pattern)
    
    result_name = database.search(search_pattern)
    print(result_name)
    if result_name:
        result_json["name"] = result_name
    else:
        for key, value in search_pattern.items():
            try:
                FieldType[value.upper()]
            except Exception:
                return {"error_0" : "missmatch field type"}
        return search_pattern

    return result_json

@w_app.post("/form/save")
async def form_save(request : Request):
    form_json : dict[str, str] = json.loads((await request.body()))
    form : Form = Form(form_json["name"])
    form_json.pop("name")

    for field_name in form_json.keys():
        form.set_field(
            field_name=field_name, 
            field_type=FieldType[form_json[field_name].upper()]
            )
    database.insert(form)
    print(form_json)
    


@w_app.get("/form/html", response_class=HTMLResponse)
async def get_html_form(request : Request):
    request_json : dict[str, str] = json.loads((await request.body()))
    if "form_name" in request_json.keys():
        return HTMLResponse(content="", status_code=200)
    elif "form_id" in request_json.keys():
        return HTMLResponse(content="", status_code=200)

