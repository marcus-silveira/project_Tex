## Instalação

Para rodar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/marcus-silveira/project_Tex
    cd project_Tex
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Tabelas

### Gênero

A tabela de gênero contém informações sobre o sexo dos usuários. Os valores possíveis são:

| ID | Gênero   |
| -- | -------- |
| 1  | Masculino |
| 2  | Feminino  |

### Estado Civil

A tabela de estado civil contém os diferentes status que um usuário pode ter. Os valores disponíveis são:

| ID | Status      |
| -- | ----------- |
| 1  | Solteiro    |
| 2  | Casado      |
| 3  | Viúvo       |
| 4  | Divorciado   |

## Observações
- As IDs são usadas para identificar cada gênero e estado civil de forma única.
- Certifique-se de que os dados inseridos correspondem às opções definidas nessas tabelas.

## Endpoints da API

Abaixo estão os principais endpoints disponíveis:

- **GET /users**: Retorna todos os usuários.
- **GET /users/id**: Retorna um usuário específico pelo ID.
- **POST /users**: Cria um novo usuário (os dados devem incluir `name`, `cpf`, `email`, etc.).
- **PUT /users/id**: Atualiza as informações de um usuário específico.
- **DELETE /users/id**: Remove um usuário específico.

### Exemplo de Requisição POST
### Exemplo de Requisição POST

```json
{
    "name": "Marcus Silveira",
    "cpf": "12345678901",
    "rg": "MG1234567",
    "email": "marcus@example.com",
    "address": "123 Main St",
    "state": "MG",
    "city": "Belo Horizonte",
    "birthday": "1990-01-01",
    "cellphone": "31987654321",
    "gender_id": 1,
    "marital_status_id": 1
}
```


### Executando os Testes

Para executar os testes, instale o framework `pytest` e siga os passos abaixo:

1. **Navegue até a raiz do seu projeto** no terminal.

2. **Execute os testes usando o pytest:**

   ```bash
   pytest
   ```

   Isso irá executar todos os testes encontrados no diretório `tests/` e exibir os resultados no terminal.

