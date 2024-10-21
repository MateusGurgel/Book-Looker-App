# Documentação da API

## Visão Geral

Esta API fornece dois endpoints relacionados a livros e seus registros de log.

## URL Base

---

## Endpoints

### 1. Obter Todos os Livros

**Endpoint**: `/books`

**Método**: `GET`

#### Descrição:
Busca uma lista de todos os livros disponíveis no sistema.

#### Resposta:
- **200 OK**: Retorna uma lista de todos os livros.

**Exemplo de Resposta**:
```json
[
    {
        "id": 1,
        "titulo": "Título do Livro 1",
        "link": "www.amazon.com/exemplo"
    },
    {
        "id": 2,
        "titulo": "Título do Livro 2",
        "link": "www.amazon.com/exemplo2"
    }
]
```

### 2. Obter Os logs dos livros

**Endpoint**: `/books/{id}/logs`

**Método**: `GET`

#### Descrição:
Busca os registros de preços de livros

#### Resposta:
- **200 OK**: Retorna uma lista de preços de determinado livro

**Exemplo de Resposta**:
```json
[
    {
        "id": 1,
        "book_id": 1,
        "price": 80,
        "date": "10/01/2004"
    },
]
```