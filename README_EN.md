<p align="center">
  <h1>
    CPF Generator / Validator(CLI)
  </h1>
</p>

<div style="display: flex; align-items: center; padding: 10px;">
  <span>
    <a href="https://github.com/rafael-o-cunha/rafael-o-cunha/blob/main/README_EN.md">
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
    <a href="https://github.com/rafael-o-cunha/gerador_e_validador_cpf/blob/main/README_EN.md">
      <img src="https://img.shields.io/badge/-English-blue?style=for-the-badge" alt="English">
    </a>
  </span>

  <span>
    <a href="https://github.com/rafael-o-cunha/gerador_e_validador_cpf/blob/main/README_ES.md">
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



## Description
The project consists of creating a simple CPF generator and validator that works via CLI and aims to explore basic "White Belt" level features of Python


## Specifications
  Collect, clean and validate the data that represents the "CPF", it must have 11 digits, example: CPF 746.824.890-70

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">First step: Calculate the first digit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Digits</strong></td>
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
      <td><strong>Multiplier</strong></td>
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
      <td><strong>Result</strong></td>
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
      <td><strong>Sum of results</strong></td>
      <td>301</td>
    </tr>
    <tr>
      <td><strong>Result summed and multiplied by 10</strong></td>
      <td>3010</td>
    </tr>
    <tr>
      <td><strong>Mod of division by 11</strong></td>
      <td>7</td>
    </tr>
  </tbody>
</table>

If the result of the calculation is greater than 9, then consider 0,
if not, consider the resulting value.


<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">First step: Calculate the first digit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Digits</strong></td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Result of previous account:</strong></td>
      <td>7</td>
    </tr>
    <tr>
  </tbody>
</table>

If the value found matches the first digit of the complement then this digit is valid

## Obs.: For the second step, simply repeat the calculation including the first valid digit:

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Second step: Calculate the second digit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Digits</strong></td>
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
      <td><strong>Multiplier</strong></td>
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
      <td><strong>Result</strong></td>
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
      <td><strong>Sum of results</strong></td>
      <td>363</td>
    </tr>
    <tr>
      <td><strong>Result summed and multiplied by 10</strong></td>
      <td>3630</td>
    </tr>
    <tr>
      <td><strong>Resto da divisão por 11</strong></td>
      <td>0</td>
    </tr>
  </tbody>
</table>

If the result of the calculation is greater than 9, then consider 0; otherwise, consider the resulting value.

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">First step: Calculate the first digit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12"  style="text-align:center;"><strong>CPF</strong>: 746.824.890-70</td>
    </tr>
    <tr>
      <td><strong>Digits</strong></td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Result of the previous calculation:</strong></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
  </tbody>
</table>

If the value found matches the first digit of the complement, then this digit is valid.

## Steps and Features:

### Features

1. Generate a valid CPF.
2. Validate an existing CPF.

### Steps

![.](/assets/Diagrama%20Validação%20CPF%20EN.png)


## How to use:
1. Clone the project to an environment that has  ![Bash](https://img.shields.io/badge/Python-3.12.3-blue) or a higher version installed.

2. Run the project and follow the instructions that appear.
```bash
> python3 main.py
```
