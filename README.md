# ?????? Atleta API

Este projeto oferece uma API robusta para gerenciar informa��es de atletas, incluindo seus detalhes pessoais, centros de treinamento e categorias associadas. Constru�do com **FastAPI** e **SQLAlchemy**, ele proporciona uma solu��o limpa, eficiente e bem estruturada para o backend da sua aplica��o de fitness.

-----

## ? Funcionalidades

  * **Gerenciamento de Atletas**: Opera��es CRUD (Criar, Ler, Atualizar, Deletar) completas para registros de atletas.
  * **Integridade de Dados**: Tratamento robusto da integridade de dados, prevenindo especificamente entradas de CPF duplicadas para atletas.
  * **Par�metros de Consulta**: ?? Filtre atletas por `nome` e `cpf` para uma recupera��o de dados precisa.
  * **Respostas Customizadas**: O endpoint de "listar todos os atletas" fornece uma resposta otimizada, mostrando apenas detalhes essenciais como nome do atleta, nome do centro de treinamento associado e nome da categoria.
  * **Pagina��o**: ?? Recupere grandes conjuntos de dados de forma eficiente usando os par�metros de consulta `limit` e `offset`, impulsionado pela biblioteca `fastapi-pagination`.

-----

## ??? Tecnologias Utilizadas

  * **FastAPI**: Um framework web moderno, r�pido e de alta performance para construir APIs com Python 3.7+ baseado em type hints padr�o do Python.
  * **SQLAlchemy**: O toolkit SQL e Mapeador Objeto-Relacional do Python que oferece aos desenvolvedores o poder e a flexibilidade completos do SQL.
  * **Pydantic**: Valida��o de dados e gerenciamento de configura��es usando type hints do Python.
  * **fastapi-pagination**: Pagina��o simples e leve para FastAPI.
  * **PostgreSQL**: (Assumido como banco de dados, com base no uso t�pico de SQLAlchemy e restri��es de unicidade como CPF).

-----

## ?? Primeiros Passos

Estas instru��es ajudar�o voc� a ter uma c�pia do projeto funcionando em sua m�quina local para desenvolvimento e testes.

### Pr�-requisitos

Antes de come�ar, certifique-se de ter:

  * Python 3.8+ instalado.
  * Uma inst�ncia do banco de dados PostgreSQL rodando e acess�vel.

### Instala��o

1.  **Clone o reposit�rio:**

    ```bash
    git clone <url-do-seu-repositorio>
    cd atleta-api # ou o nome do seu diret�rio de projeto
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```

3.  **Instale as depend�ncias:**

    ```bash
    pip install -r requirements.txt
    # Se voc� n�o tiver um requirements.txt, precisar� instal�-los individualmente:
    # pip install fastapi uvicorn sqlalchemy asyncpg pydantic fastapi-pagination[sqlalchemy]
    ```

4.  **Configura��o do Banco de Dados:**

      * Configure sua string de conex�o com o banco de dados em suas vari�veis de ambiente ou em um arquivo de configura��o (ex: `.env`). Uma string de conex�o SQLAlchemy t�pica para PostgreSQL se parece com:
        `postgresql+asyncpg://usuario:senha@host:porta/nome_do_banco`

5.  **Execute as Migra��es (se aplic�vel):**

      * Se voc� estiver usando Alembic ou similar para migra��es de banco de dados, execute seus comandos de migra��o aqui para criar as tabelas necess�rias (`atletas`, `categorias`, `centros_treinamento`).

### Executando a Aplica��o

Para iniciar a API usando Uvicorn:

```bash
uvicorn main:app --reload
```

Substitua `main:app` pelo caminho real para a sua inst�ncia da aplica��o FastAPI. A flag `--reload` permite o recarregamento autom�tico durante o desenvolvimento.

-----

## ?? Endpoints da API

Uma vez que a aplica��o esteja rodando, voc� pode acessar a documenta��o da API em:

  * **Swagger UI**: `http://127.0.0.1:8000/docs` ??
  * **ReDoc**: `http://127.0.0.1:8000/redoc` ??

Aqui est� uma vis�o geral dos principais endpoints:

### Atletas (`/atletas`)

  * **`POST /`**: ? Cria um novo atleta.
      * **Corpo da Requisi��o**: Schema `AtletaIn` (inclui detalhes do atleta, nome da categoria e nome do centro de treinamento).
      * **Tratamento de Erro**: Retorna `303 See Other` se um CPF j� existir.
  * **`GET /`**: ?? Recupera uma lista de todos os atletas com filtros e pagina��o opcionais.
      * **Par�metros de Consulta**:
          * `nome` (opcional): Filtra por nome do atleta (correspond�ncia parcial, n�o sens�vel a mai�sculas/min�sculas).
          * `cpf` (opcional): Filtra por CPF exato.
          * `limit` (opcional): N�mero de itens por p�gina (para pagina��o).
          * `offset` (opcional): N�mero de itens a serem pulados (para pagina��o).
      * **Resposta**: Uma lista paginada de objetos `AtletaCustomOut` (nome, nome do centro de treinamento, nome da categoria).
  * **`GET /{id}`**: ?? Recupera um �nico atleta pelo seu UUID.
      * **Resposta**: Schema `AtletaOut`.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta n�o for encontrado.
  * **`PATCH /{id}`**: ?? Atualiza os detalhes de um atleta existente pelo seu UUID.
      * **Corpo da Requisi��o**: Schema `AtletaUpdate` (permite atualiza��es parciais para nome e idade).
      * **Resposta**: Schema `AtletaOut` com os detalhes atualizados.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta n�o for encontrado.
  * **`DELETE /{id}`**: ??? Deleta um atleta pelo seu UUID.
      * **Resposta**: `204 No Content` em caso de exclus�o bem-sucedida.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o ID do atleta n�o for encontrado.

-----

## ?? Contribuindo

Contribui��es s�o bem-vindas\! Sinta-se � vontade para abrir issues ou enviar pull requests.

-----

## ?? Licen�a

Este projeto � de c�digo aberto e est� dispon�vel sob a [Licen�a MIT](https://www.google.com/search?q=LICENSE). (Voc� deve criar um arquivo `LICENSE` em seu reposit�rio se ainda n�o o fez).