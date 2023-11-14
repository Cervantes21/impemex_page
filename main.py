from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configurar las plantillas de Jinja2
templates = Jinja2Templates(directory=".")

# Montar la carpeta "assets" en la ruta "/assets"
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Crear una ruta que devuelva una respuesta HTML usando plantillas Jinja2
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # Puedes pasar datos a la plantilla si es necesario
    data = {"request": request, "page_title": "Tu Título Aquí"}
    # Renderizar la plantilla desde la carpeta raíz
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    data = {"request": request, "page_title": "Acerca de Nosotros"}
    return templates.TemplateResponse("about.html", {"request": request, "data": data})

@app.get("/shop", response_class=HTMLResponse)
async def read_shop(request: Request):
    data = {"request": request, "page_title": "Tienda"}
    return templates.TemplateResponse("shop.html", {"request": request, "data": data})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    data = {"request": request, "page_title": "Contacto"}
    return templates.TemplateResponse("contact.html", {"request": request, "data": data})

@app.get("/shop-single", response_class=HTMLResponse)
async def read_shop_single(request: Request):
    data = {"request": request, "page_title": "Producto Individual"}
    return templates.TemplateResponse("shop-single.html", {"request": request, "data": data})
