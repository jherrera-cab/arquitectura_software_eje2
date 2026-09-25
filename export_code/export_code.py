import os
from pathlib import Path
from convert import convertir_md_a_pdf
from generate import convert_script_markcdown


scripts = [
    "../config/database.py",
    "../controllers/app_controller.py",
    "../models/empleado_dao.py",
    "../models/product_dao.py",
    "../views/consola_view.py"

]

# Crear directorio de salida si no existe
output_dir = Path(__file__).parent / "code"
output_dir.mkdir(parents=True, exist_ok=True)

path_md = str(output_dir / "Codigo.md")
path_pdf = str(output_dir / "Codigo_PDF.pdf")


convert_script_markcdown(scripts, path_md, title="codigo prueba")
convertir_md_a_pdf(path_md, path_pdf)

