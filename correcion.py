
import json
import re

PATH_JSON_ORIGINAL = "jsonmovementsfile copy.json"
PATH_JSON_CORREGIDO = "jsonmovementsfile_corregido.json"


def corregir_formato_categorias(path_original, path_corregido):
    with open(path_original, "r", encoding="utf-8") as archivo:
        movimientos = json.load(archivo)

    for movimiento in movimientos:
        categoria = movimiento.get("category")

        # Convertir únicamente las categorías que son texto
        if isinstance(categoria, str):
            coincidencia = re.fullmatch(
                r"\s*Categoría:\s*(.*?)\s*\|\s*Color:\s*(#[0-9A-Fa-f]{6})\s*",
                categoria
            )

            if coincidencia:
                movimiento["category"] = {
                    "name": coincidencia.group(1),
                    "color": coincidencia.group(2)
                }
            else:
                raise ValueError(
                    f"Formato de categoría no válido: {categoria}"
                )

    with open(path_corregido, "w", encoding="utf-8") as archivo:
        json.dump(
            movimientos,
            archivo,
            ensure_ascii=False,
            indent=4
        )

    print(f"Archivo corregido: {path_corregido}")
    print(f"Total de movimientos: {len(movimientos)}")


corregir_formato_categorias(
    PATH_JSON_ORIGINAL,
    PATH_JSON_CORREGIDO
)