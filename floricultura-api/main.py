from fastapi import FastAPI
from pydantic import BaseModel
import asyncpg

app = FastAPI()



# models

class Flor(BaseModel):
    nome: str
    preco: float
    estoque: int


class Cliente(BaseModel):
    nome: str
    telefone: str
    email: str


class Pedido(BaseModel):
    cliente_id: int
    flor_id: int
    quantidade: int
    data_pedido: str


# conexão com o banco

async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="668474541",
        database="floricultura",
        host="localhost"
    )


# crud flores

@app.post("/flores")
async def criar_flor(flor: Flor):
    conn = await get_db_connection()

    await conn.execute(
        """
        INSERT INTO flores (nome, preco, estoque)
        VALUES ($1, $2, $3)
        """,
        flor.nome,
        flor.preco,
        flor.estoque
    )

    await conn.close()
    return {"message": "Flor criada com sucesso!"}


@app.get("/flores")
async def listar_flores():
    conn = await get_db_connection()

    flores = await conn.fetch("SELECT * FROM flores")

    await conn.close()
    return [dict(flor) for flor in flores]


@app.get("/flores/{id}")
async def buscar_flor(id: int):
    conn = await get_db_connection()

    flor = await conn.fetchrow(
        "SELECT * FROM flores WHERE id = $1",
        id
    )

    await conn.close()

    if flor:
        return dict(flor)

    return {"message": "Flor não encontrada"}


@app.put("/flores/{id}")
async def atualizar_flor(id: int, flor: Flor):
    conn = await get_db_connection()

    await conn.execute(
        """
        UPDATE flores
        SET nome = $1,
            preco = $2,
            estoque = $3
        WHERE id = $4
        """,
        flor.nome,
        flor.preco,
        flor.estoque,
        id
    )

    await conn.close()

    return {"message": "Flor atualizada com sucesso!"}


@app.delete("/flores/{id}")
async def deletar_flor(id: int):
    conn = await get_db_connection()

    await conn.execute(
        """
        DELETE FROM flores
        WHERE id = $1
        """,
        id
    )

    await conn.close()

    return {"message": "Flor deletada com sucesso!"}


# crud clientes

@app.post("/clientes")
async def criar_cliente(cliente: Cliente):
    conn = await get_db_connection()

    await conn.execute(
        """
        INSERT INTO clientes (nome, telefone, email)
        VALUES ($1, $2, $3)
        """,
        cliente.nome,
        cliente.telefone,
        cliente.email
    )

    await conn.close()

    return {"message": "Cliente criado com sucesso!"}


@app.get("/clientes")
async def listar_clientes():
    conn = await get_db_connection()

    clientes = await conn.fetch("SELECT * FROM clientes")

    await conn.close()

    return [dict(cliente) for cliente in clientes]


@app.get("/clientes/{id}")
async def buscar_cliente(id: int):
    conn = await get_db_connection()

    cliente = await conn.fetchrow(
        "SELECT * FROM clientes WHERE id = $1",
        id
    )

    await conn.close()

    if cliente:
        return dict(cliente)

    return {"message": "Cliente não encontrado"}


@app.put("/clientes/{id}")
async def atualizar_cliente(id: int, cliente: Cliente):
    conn = await get_db_connection()

    await conn.execute(
        """
        UPDATE clientes
        SET nome = $1,
            telefone = $2,
            email = $3
        WHERE id = $4
        """,
        cliente.nome,
        cliente.telefone,
        cliente.email,
        id
    )

    await conn.close()

    return {"message": "Cliente atualizado com sucesso!"}


@app.delete("/clientes/{id}")
async def deletar_cliente(id: int):
    conn = await get_db_connection()

    await conn.execute(
        """
        DELETE FROM clientes
        WHERE id = $1
        """,
        id
    )

    await conn.close()

    return {"message": "Cliente deletado com sucesso!"}


# crud pedidos 

@app.post("/pedidos")
async def criar_pedido(pedido: Pedido):
    conn = await get_db_connection()

    await conn.execute(
        """
        INSERT INTO pedidos
        (cliente_id, flor_id, quantidade, data_pedido)
        VALUES ($1, $2, $3, $4)
        """,
        pedido.cliente_id,
        pedido.flor_id,
        pedido.quantidade,
        pedido.data_pedido
    )

    await conn.close()

    return {"message": "Pedido criado com sucesso!"}


@app.get("/pedidos")
async def listar_pedidos():
    conn = await get_db_connection()

    pedidos = await conn.fetch(
        "SELECT * FROM pedidos"
    )

    await conn.close()

    return [dict(pedido) for pedido in pedidos]


@app.get("/pedidos/{id}")
async def buscar_pedido(id: int):
    conn = await get_db_connection()

    pedido = await conn.fetchrow(
        "SELECT * FROM pedidos WHERE id = $1",
        id
    )

    await conn.close()

    if pedido:
        return dict(pedido)

    return {"message": "Pedido não encontrado"}


@app.put("/pedidos/{id}")
async def atualizar_pedido(id: int, pedido: Pedido):
    conn = await get_db_connection()

    await conn.execute(
        """
        UPDATE pedidos
        SET cliente_id = $1,
            flor_id = $2,
            quantidade = $3,
            data_pedido = $4
        WHERE id = $5
        """,
        pedido.cliente_id,
        pedido.flor_id,
        pedido.quantidade,
        pedido.data_pedido,
        id
    )

    await conn.close()

    return {"message": "Pedido atualizado com sucesso!"}


@app.delete("/pedidos/{id}")
async def deletar_pedido(id: int):
    conn = await get_db_connection()

    await conn.execute(
        """
        DELETE FROM pedidos
        WHERE id = $1
        """,
        id
    )

    await conn.close()

    return {"message": "Pedido deletado com sucesso!"}