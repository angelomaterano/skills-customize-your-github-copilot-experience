# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você vai construir uma API REST usando o framework FastAPI. O foco é criar rotas, modelos de dados e validação, além de testar os endpoints localmente.

## 📝 Tasks

### 🛠️ Criar API básica com FastAPI

#### Description
Inicialize um projeto FastAPI com uma aplicação mínima e um endpoint de saúde para confirmar que o servidor está funcionando.

#### Requirements
Completed program should:
- Iniciar um app FastAPI com `FastAPI()`
- Expor um endpoint `GET /health` retornando `{ "status": "ok" }`
- Incluir instruções de execução com `uvicorn` (ex.: `uvicorn main:app --reload`)

### 🛠️ Implementar CRUD de recursos

#### Description
Implemente uma API REST para gerenciar um recurso simples (por exemplo, `items`) com operações de criar, listar, obter por id, atualizar e remover.

#### Requirements
Completed program should:
- Definir um `Model` Pydantic (ex.: `Item` com `id`, `name`, `price`)
- Implementar endpoints: `POST /items`, `GET /items`, `GET /items/{id}`, `PUT /items/{id}`, `DELETE /items/{id}`
- Usar armazenamento em memória (lista/dicionário) para persistência simples
- Retornar códigos HTTP apropriados (201, 200, 404, 204)

### 🛠️ Validação e erros

#### Description
Adicione validações nos modelos e trate erros com respostas claras.

#### Requirements
Completed program should:
- Validar campos com tipos e restrições (ex.: `price > 0`)
- Retornar mensagens de erro explicativas para entradas inválidas
- Usar `HTTPException` para erros como recurso não encontrado

