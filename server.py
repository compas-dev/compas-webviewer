from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import compas
from compas.geometry import Box
from compas.datastructures import Mesh
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


def mesh_to_vertices_edges_triangles(mesh: Mesh) -> MeshOutput:
    vertices, faces = mesh.to_vertices_and_faces()
    triangles = []
    for face in faces:
        if len(face) == 3:
            triangles.append(face)
        elif len(face) == 4:
            triangles.append([face[0], face[1], face[2]])
            triangles.append([face[0], face[2], face[3]])
    edges = list(mesh.edges())
    return MeshOutput(
        vertices=list(flatten(vertices)),
        faces=list(flatten(triangles)),
        edges=list(flatten(edges)),
    )


@app.get("/ping")
async def ping():
    return 1


@app.get("/version")
async def version():
    return compas.__version__


@app.get("/load_tubemesh")
async def load_tubemesh() -> MeshOutput:
    mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
    return mesh_to_vertices_edges_triangles(mesh)


@app.get("/load_bunny")
async def load_bunny() -> MeshOutput:
    mesh = Mesh.from_ply(compas.get("bunny.ply"))
    mesh.rotate(3.14159 / 2, [1, 0, 0])
    mesh.scale(30)
    return mesh_to_vertices_edges_triangles(mesh)


@app.post("/box_to_subdivided_mesh")
async def box_to_subdivided_mesh(boxdata: BoxInput) -> MeshOutput:
    box = Box(boxdata.xsize, boxdata.ysize, boxdata.zsize)
    mesh = box.to_mesh()
    ball = mesh.subdivided(k=3)
    return mesh_to_vertices_edges_triangles(ball)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
