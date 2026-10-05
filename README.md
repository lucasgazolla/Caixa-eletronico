# Sistema Bancário em Python

Projeto desenvolvido em **Python** que simula operações básicas de um caixa eletrônico, permitindo ao usuário consultar o saldo, realizar saques e sair do sistema.

## Funcionalidades

O sistema possui as seguintes opções:

* **Consultar saldo**
* **Realizar saque**
* **Sair do sistema**

Durante o saque, o sistema também realiza algumas validações:

* Limite máximo de saque de **R$ 2.000,00**
* O valor não pode ser **zero ou negativo**
* O valor sacado deve ser **múltiplo de R$ 10,00**
* O usuário não pode sacar um valor maior que o saldo disponível
* É cobrada uma **taxa de serviço de R$ 2,50** por saque realizado

## Saldo inicial

O sistema começa com um saldo de:

```text
R$ 1.000,00
```

Após um saque válido, o valor sacado e a taxa de R$ 2,50 são descontados do saldo.

### Exemplo

Se o usuário sacar **R$ 100,00**:

```text
Saldo inicial: R$ 1.000,00
Saque:         R$ 100,00
Taxa:          R$ 2,50
-----------------------
Saldo final:   R$ 897,50
```

## Tecnologias utilizadas

* **Python**
* Biblioteca `os`
* Biblioteca `time`

## Como executar

### 1. Instale o Python

Certifique-se de ter o Python instalado no computador.

### 2. Clone o projeto

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 3. Acesse a pasta do projeto

```bash
cd nome-do-projeto
```

### 4. Execute o programa

```bash
python nome_do_arquivo.py
```

## Menu do sistema

Ao executar o programa, será apresentado o seguinte menu:

```text
Seu saldo atual é de 1000

Digite a operação desejada -
[1] Sacar
[2] Sair
[3] Consultar Saldo
```

### Opção 1 — Sacar

Solicita o valor que o usuário deseja sacar e verifica se a operação atende às regras estabelecidas.

### Opção 2 — Sair

Encerra o sistema.

### Opção 3 — Consultar saldo

Exibe o saldo disponível na conta sem realizar nenhuma alteração.

## Objetivo do projeto

O projeto foi desenvolvido com o objetivo de praticar conceitos básicos de programação em Python, como:

* Variáveis
* Estruturas condicionais (`if`, `elif`, `else`)
* Estrutura de repetição (`while`)
* Entrada de dados com `input()`
* Conversão de tipos (`int()` e `float()`)
* Operadores matemáticos e lógicos
* Uso de bibliotecas (`os` e `time`)
* Controle de fluxo do programa

## Autor

**Lucas Gazolla**

Estudante de Ciência da Computação.
