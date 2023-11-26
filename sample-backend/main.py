from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Material(BaseModel):
    formula: str
    density: float


materials = {}


@app.post("/material/", response_model=str)
def create_material(material: Material):
    material_id = str(uuid4())
    materials[material_id] = material
    return material_id


@app.get("/material/{material_id}", response_model=Material)
def get_material(material_id: str):
    material = materials.get(material_id)
    if material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return material


@app.get("/search/")
def search_materials(
        min_density: Optional[float] = Query(None, alias="min-density"),
        max_density: Optional[float] = Query(None, alias="max-density"),
        include_elements: Optional[List[str]] = Query(None, alias="include-elements"),
        exclude_elements: Optional[List[str]] = Query(None, alias="exclude-elements")
):
    results = []

    for material in materials.values():
        print(material, min_density, max_density, include_elements, exclude_elements)
        if min_density is not None and material.density < min_density:
            continue
        if max_density is not None and material.density > max_density:
            continue
        if include_elements:
            if not all(elem in material.formula for elem in include_elements):
                continue
        if exclude_elements:
            if any(elem in material.formula for elem in exclude_elements):
                continue
        results.append(material)

    return results


