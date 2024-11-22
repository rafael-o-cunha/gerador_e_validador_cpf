<p align="center">
  <h1>
    Gerador / Validador de CPF (CLI)
  </h1>
</p>

<div style="display: flex; align-items: center; padding: 10px;">
  <span>
    <a href="https://github.com/rocunha09/">
        <img src="https://img.shields.io/badge/-Home-black?style=for-the-badge" alt="Voltar ao Perfil">
    </a>
</span>
</div>

---

<div style="display: flex; align-items: center; padding: 10px;">
  <span>
    <a href="https://github.com/rocunha09/gerador_e_validador_cpf/blob/main/README.md">
      <img src="https://img.shields.io/badge/-Português-green?style=for-the-badge" alt="Português">
    </a>
  </span>

  <span>
    <a href="https://github.com/rocunha09/gerador_e_validador_cpf/blob/main/README_EN.md">
      <img src="https://img.shields.io/badge/-English-blue?style=for-the-badge" alt="English">
    </a>
  </span>

  <span>
    <a href="https://github.com/rocunha09/gerador_e_validador_cpf/blob/main/README_ES.md">
      <img src="https://img.shields.io/badge/-Español-red?style=for-the-badge" alt="Español">
    </a>
  </span>
</div>

---

<div style="display: flex; align-items: center; padding: 10px;">
  <span style="margin-right: 15px">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" />
  </span>
  <span>
  <span style="margin-right: 15px">
    <img src="https://img.shields.io/badge/Obsidian-%23483699.svg?&logo=obsidian&logoColor=white" />
  </span>
</div>

---



## Descrição
O projeto consiste na criação de um gerador e validador de CPF simples que funciona via CLI e tem o objetivo de explorar recursos básicos a nível "Faixa Branca" do Python


## Especificações
    Colete, limpe e valide o dado que representa o cpf, ele deve ter 11 dígitos, exmeplo: CPF 746.824.890-70

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primeira etapa: Calcular o primeiro dígito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Dígitos</strong></td>
      <td>7</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>9</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Multiplicador</strong></td>
      <td>10</td>
      <td>9</td>
      <td>8</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Resultado</strong></td>
      <td>70</td>
      <td>36</td>
      <td>48</td>
      <td>56</td>
      <td>12</td>
      <td>20</td>
      <td>32</td>
      <td>27</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Resultados somados</strong></td>
      <td>301</td>
    </tr>
    <tr>
      <td><strong>Resultado somado multiplicado por 10</strong></td>
      <td>3010</td>
    </tr>
    <tr>
      <td><strong>Resto da divisão por 11</strong></td>
      <td>7</td>
    </tr>
  </tbody>
</table>

Se o resultado da conta for maior que 9 então considerar 0,
se não considerar o valor resultante.


<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primeira etapa: Calcular o primeiro dígito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Dígitos</strong></td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Resultado da conta anterior:</strong></td>
      <td>7</td>
    </tr>
    <tr>
  </tbody>
</table>

Se o valor encontrado bater com o primeiro dígito do complemento então este dígito é válido

## Obs.: Para segunda etapa, basta repetir o cálculo incluindo o primeiro dígito válido:

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Segunda etapa: Calcular o segundo dígito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Dígitos</strong></td>
      <td>7</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>9</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Multiplicador</strong></td>
      <td>11</td>
      <td>10</td>
      <td>9</td>
      <td>8</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Resultado</strong></td>
      <td>77</td>
      <td>40</td>
      <td>54</td>
      <td>64</td>
      <td>14</td>
      <td>24</td>
      <td>40</td>
      <td>36</td>
      <td>0</td>
      <td>14</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Resultados somados</strong></td>
      <td>363</td>
    </tr>
    <tr>
      <td><strong>Resultado somado multiplicado por 10</strong></td>
      <td>3630</td>
    </tr>
    <tr>
      <td><strong>Resto da divisão por 11</strong></td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Se o resultado da conta for maior que 9 então considerar 0,
se não considerar o valor resultante.


<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primeira etapa: Calcular o primeiro dígito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Dígitos</strong></td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Resultado da conta anterior:</strong></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
  </tbody>
</table>

Se o valor encontrado bater com o primeiro dígito do complemento então este dígito é válido


## Etapas e Funcionalidades:

### Funcionalidades

1. Gerar CPF Válido.
2. Validar CPF Existente.

### Etapas

![.](/assets/Diagrama%20Validação%20CPF%20PT.br.png)


## Como utilizar:
1. Clone o projeto para um ambiente que possua o  ![Bash](https://img.shields.io/badge/Python-3.12.3-blue) ou superior instalado.

2. Rode o projeto e siga as instruções que aparecerem.
```bash
> python3 main.py
```
