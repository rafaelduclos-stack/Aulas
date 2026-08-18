# API Confeitaria

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas
**Desenvolvedor** Rafael Duclos

---

## 📋 Sobre o projeto

Minha API gerencia uma confeitaria. Ela possui as quatro funções do CRUD (Create, Read, Update, Delete). A confeitaria oferece vários tipos de produtos, mas atualmente só existem as tabelas de produtos e bolos.

---

## 🗂️ Tabelas do banco

### Tabela `produtos`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | VARCHAR | Nome do produto|
| preco | DECIMAL | Preço do produto|
| quantidade | INT | Quantidade do produto disponível |
| categoria | VARCHAR | Categoria do produto (Ex.: Bolos)|

### Tabela `bolos`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | VARCHAR | Nome do bolo |
| sabor | VARCHAR | Sabor do bolo |
| tamanho | VARCHAR | Tamanho do bolo |
| produto_id | INTEGER | Chave estrangeira → aponta para produtos(id) |

**Relação:** Cada bolo é um tipo de produto, ou seja, cada bolo pertence a um produto.

---

## 🚀 Como rodar o projeto

```bash
# 1. Instalar o Flask (caso não tenha)
pip install flask

# 2. Rodar a API
python app.py

# 3. A API estará disponível em:
# http://127.0.0.1:5000
```

O banco de dados (`confeitariaferduclos.db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

### Tabela produtos

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/<id>` | Busca um produto pelo id |
| POST | `/produtos` | Cria um novo produto |
| PUT | `/produtos/<id>` | Atualiza um produto |
| DELETE | `/produtos/<id>` | Apaga um produto |

### Tabela bolos

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/bolos` | Lista todos os bolos |
| GET | `/bolos/<id>` | Busca um bolo pelo id
| POST | `/bolos` | Cria um novo bolo |
| PUT | `/bolos/<id>` | Atualiza um bolo |
| DELETE | `/bolos/<id> | Apaga um bolo |

### Rotas especiais

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/produtos/<id>/bolos` | Lista os bolos (filhos) de um produto (pai) (JOIN) |
| GET | `/bolos/busca?nome=` | Filtro por query string com LIKE, buscando por nome |

---

## 🧪 Como testar

Os testes estão no arquivo testesconfeitaria.http

Exemplo de requisição para criar um produto:

```http
POST http://127.0.0.1:5000/autores
Content-Type: application/json

{
    "nome": "Bolo Vulcão",
    "categoria": "Bolos",
    "quantidade": "28",
    "preco": 65.0
    
}
```

---

## 👥 Integrantes

- Rafael Duclos - Tudo
