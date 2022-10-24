from tinydb import TinyDB, Query
import pandas as pd

class Task():
    def __init__(self, informacao) -> None:
        self.informacao=informacao


bd = TinyDB("Task.json")
task = Query()
def inserir(model: Task):
    bd.insert({"task":model.informacao})
def mostrarTodos():
    todos = bd.all()
    return todos

def atualizarPessoa(id: int, model:Usuario):
    if bd.search(Task.informacao==str()):
        bd.remove(Task.informacao==str(id))
        inserir(model)
    else:
        print("Esse usuário não existe")
def buscarPorId(id):
    return bd.search(usuario.id==str(id))
def deletarPessoa(id: int):
    if bd.search(usuario.id==str(id)):
        bd.remove(usuario.id==str(id))
    else:
        print("Usuário não encontrado")