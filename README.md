# ?????? Atleta API

Este projeto oferece uma API robusta para gerenciar informações de atletas, incluindo seus detalhes pessoais, centros de treinamento e categorias associadas. Construído com **FastAPI** e **SQLAlchemy**, ele proporciona uma solução limpa, eficiente e bem estruturada para o backend da sua aplicação de fitness.

-----

## ? Funcionalidades

  * **Gerenciamento de Atletas**: Operações CRUD (Criar, Ler, Atualizar, Deletar) completas para registros de atletas.
  * **Integridade de Dados**: Tratamento robusto da integridade de dados, prevenindo especificamente entradas de CPF duplicadas para atletas.
  * **Parâmetros de Consulta**: ?? Filtre atletas por `nome` e `cpf` para uma recuperação de dados precisa.
  * **Respostas Customizadas**: O endpoint de "listar todos os atletas" fornece uma resposta otimizada, mostrando apenas detalhes essenciais como nome do atleta, nome do centro de treinamento associado e nome da categoria.
  * **Paginação**: ?? Recupere grandes conjuntos de dados de forma eficiente usando os parâmetros de consulta `limit` e `offset`, impulsionado pela biblioteca `fastapi-pagination`.

-----

## ??? Tecnologias Utilizadas

  * **FastAPI**: Um framework web moderno, rápido e de alta performance para construir APIs com Python 3.7+ baseado em type hints padrão do Python.
  * **SQLAlchemy**: O toolkit SQL e Mapeador Objeto-Relacional do Python que oferece aos desenvolvedores o poder e a flexibilidade completos do SQL.
  * **Pydantic**: Validação de dados e gerenciamento de configurações usando type hints do Python.
  * **fastapi-pagination**: Paginação simples e leve para FastAPI.
  * **PostgreSQL**: (Assumido como banco de dados, com base no uso típico de SQLAlchemy e restrições de unicidade como CPF).

-----

## ?? Primeiros Passos

Estas instruções ajudarão você a ter uma cópia do projeto funcionando em sua máquina local para desenvolvimento e testes.

### Pré-requisitos

Antes de começar, certifique-se de ter:

  * Python 3.8+ instalado.
  * Uma instância do banco de dados PostgreSQL rodando e acessível.

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone <url-do-seu-repositorio>
    cd atleta-api # ou o nome do seu diretório de projeto
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    # Se você não tiver um requirements.txt, precisará instalá-los individualmente:
    # pip install fastapi uvicorn sqlalchemy asyncpg pydantic fastapi-pagination[sqlalchemy]
    ```

4.  **Configuração do Banco de Dados:**

      * Configure sua string de conexão com o banco de dados em suas variáveis de ambiente ou em um arquivo de configuração (ex: `.env`). Uma string de conexão SQLAlchemy típica para PostgreSQL se parece com:
        `postgresql+asyncpg://usuario:senha@host:porta/nome_do_banco`

5.  **Execute as Migrações (se aplicável):**

      * Se você estiver usando Alembic ou similar para migrações de banco de dados, execute seus comandos de migração aqui para criar as tabelas necessárias (`atletas`, `categorias`, `centros_treinamento`).

### Executando a Aplicação

Para iniciar a API usando Uvicorn:

```bash
uvicorn main:app --reload
```

Substitua `main:app` pelo caminho real para a sua instância da aplicação FastAPI. A flag `--reload` permite o recarregamento automático durante o desenvolvimento.

-----

## ?? Endpoints da API

Uma vez que a aplicação esteja rodando, você pode acessar a documentação da API em:

  * **Swagger UI**: `http://127.0.0.1:8000/docs` ??
  * **ReDoc**: `http://127.0.0.1:8000/redoc` ??

Aqui está uma visão geral dos principais endpoints:

### Atletas (`/atletas`)

  * **`POST /`**: ? Cria um novo atleta.
      * **Corpo da Requisição**: Schema `AtletaIn` (inclui detalhes do atleta, nome da categoria e nome do centro de treinamento).
      * **Tratamento de Erro**: Retorna `303 See Other` se um CPF já existir.
  * **`GET /`**: ?? Recupera uma lista de todos os atletas com filtros e paginação opcionais.
      * **Parâmetros de Consulta**:
          * `nome` (opcional): Filtra por nome do atleta (correspondência parcial, não sensível a maiúsculas/minúsculas).
          * `cpf` (opcional): Filtra por CPF exato.
          * `limit` (opcional): Número de itens por página (para paginação).
          * `offset` (opcional): Número de itens a serem pulados (para paginação).
      * **Resposta**: Uma lista paginada de objetos `AtletaCustomOut` (nome, nome do centro de treinamento, nome da categoria).
  * **`GET /{id}`**: ?? Recupera um único atleta pelo seu UUID.
      * **Resposta**: Schema `AtletaOut`.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta não for encontrado.
  * **`PATCH /{id}`**: ?? Atualiza os detalhes de um atleta existente pelo seu UUID.
      * **Corpo da Requisição**: Schema `AtletaUpdate` (permite atualizações parciais para nome e idade).
      * **Resposta**: Schema `AtletaOut` com os detalhes atualizados.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta não for encontrado.
  * **`DELETE /{id}`**: ??? Deleta um atleta pelo seu UUID.
      * **Resposta**: `204 No Content` em caso de exclusão bem-sucedida.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta não for encontrado.

-----

## ?? Contribuindo

Contribuições são bem-vindas\! Sinta-se à vontade para abrir issues ou enviar pull requests.

-----

## ?? Licença

Este projeto é de código aberto e está disponível sob a [Licença MIT](https://www.google.com/search?q=LICENSE). (Você deve criar um arquivo `LICENSE` em seu repositório se ainda não o fez).