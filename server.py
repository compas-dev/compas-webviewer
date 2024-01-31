from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import compas
from compas.geometry import Box
from compas.utilities import flatten


app = FastAPI()


class BoxInput(BaseModel):
    xsize: float
    ysize: float
    zsize: float


class MeshOutput(BaseModel):
    vertices: List[float]
    faces: List[int]
    edges: List[int]


@app.get("/ping")
async def ping():
    return 1


@app.get("/version")
async def version():
    return compas.__version__


@app.post("/box_to_subdivided_mesh")
async def box_to_subdivided_mesh(boxdata: BoxInput) -> MeshOutput:
    box = Box(boxdata.xsize, boxdata.ysize, boxdata.zsize)
    mesh = box.to_mesh()
    ball = mesh.subdivided(k=3)
    vertices, faces = ball.to_vertices_and_faces()
    triangles = []
    for face in faces:
        triangles.append([face[0], face[1], face[2]])
        triangles.append([face[0], face[2], face[3]])
    edges = list(ball.edges())
    return MeshOutput(
        vertices=list(flatten(vertices)),
        faces=list(flatten(triangles)),
        edges=list(flatten(edges)),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
