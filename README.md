# 📦 Sistema de Controle de Estoque

## 📌 Descrição

Sistema web desenvolvido com **Django** e **Django REST Framework** para gerenciamento de estoque.

O sistema permite cadastrar produtos, categorias e controlar movimentações de entrada e saída, garantindo a consistência dos dados automaticamente.

---

## 🚀 Funcionalidades

### 🌐 Interface Web

* Cadastro, edição e exclusão de produtos
* Cadastro, edição e exclusão de categorias
* Registro de movimentações (entrada e saída)
* Controle automático de estoque
* Interface com Bootstrap

### 🔐 Autenticação

* Login de usuários
* Logout
* Proteção de páginas restritas (CRUD)

### 🧠 Regras de Negócio

* Atualização automática do estoque ao criar movimentações
* Reversão automática ao excluir movimentações
* Atualização correta ao editar movimentações
* Proteção contra exclusão de categorias com produtos vinculados

### 🔌 API REST

* Endpoints para produtos, categorias e movimentações
* API protegida com autenticação

---

## ⚙️ Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* Bootstrap

---

## ▶️ Como executar o projeto

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Criar usuário admin
python manage.py createsuperuser

# Executar servidor
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 🔐 Autenticação na API

A API utiliza autenticação por sessão (login no sistema).

Para acessar:

1. Faça login no sistema web
2. Acesse os endpoints da API

---

## 🔌 Endpoints da API

Base da API:

```
http://127.0.0.1:8000/estoque/api/
```

---

### 📦 Produtos

| Método | URL                           | Descrição         |
| ------ | ----------------------------- | ----------------- |
| GET    | `/estoque/api/produtos/`      | Listar produtos   |
| POST   | `/estoque/api/produtos/`      | Criar produto     |
| GET    | `/estoque/api/produtos/{id}/` | Detalhar produto  |
| PUT    | `/estoque/api/produtos/{id}/` | Atualizar produto |
| DELETE | `/estoque/api/produtos/{id}/` | Excluir produto   |

---

### 🗂️ Categorias

| Método | URL                             | Descrição           |
| ------ | ------------------------------- | ------------------- |
| GET    | `/estoque/api/categorias/`      | Listar categorias   |
| POST   | `/estoque/api/categorias/`      | Criar categoria     |
| GET    | `/estoque/api/categorias/{id}/` | Detalhar categoria  |
| PUT    | `/estoque/api/categorias/{id}/` | Atualizar categoria |
| DELETE | `/estoque/api/categorias/{id}/` | Excluir categoria   |

---

### 🔄 Movimentações

| Método | URL                                | Descrição              |
| ------ | ---------------------------------- | ---------------------- |
| GET    | `/estoque/api/movimentacoes/`      | Listar movimentações   |
| POST   | `/estoque/api/movimentacoes/`      | Criar movimentação     |
| GET    | `/estoque/api/movimentacoes/{id}/` | Detalhar movimentação  |
| PUT    | `/estoque/api/movimentacoes/{id}/` | Atualizar movimentação |
| DELETE | `/estoque/api/movimentacoes/{id}/` | Excluir movimentação   |

---

## 🧠 Regras importantes da API

* 🔐 Todos os endpoints exigem autenticação
* 📈 Movimentações de entrada aumentam o estoque
* 📉 Movimentações de saída diminuem o estoque
* 🔄 Ao editar uma movimentação, o estoque é recalculado
* ❌ Ao excluir uma movimentação, o estoque é revertido
* 🚫 Categorias com produtos não podem ser excluídas

---

## 📁 Organização do Projeto

```
core/        → autenticação e páginas base
estoque/     → lógica principal do sistema
templates/   → arquivos HTML
```

---

## 🏆 Autor

Eric Felipe Santos

---

## 📌 Observação

Este projeto foi desenvolvido como atividade prática para aplicação de conceitos de Django, APIs REST e controle de estoque.
