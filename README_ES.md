<p align="center">
  <h1>
    Generador / Validador de CPF (CLI)
  </h1>
</p>

<div style="display: flex; align-items: center; padding: 10px;">
  <span>
    <a href="https://github.com/rafael-o-cunha/rafael-o-cunha/blob/main/README_ES.md">
        <img src="https://img.shields.io/badge/-Home-black?style=for-the-badge" alt="Voltar ao Perfil">
    </a>
</span>
</div>

---

<div style="display: flex; align-items: center; padding: 10px;">
  <span>
    <a href="https://github.com/rafael-o-cunha/gerador_e_validador_cpf/blob/main/README.md">
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



## Descripción
El proyecto consiste en la creación de un generador y validador de CPF simple que funciona vía CLI y tiene el objetivo de explorar recursos básicos a nivel "Cinta Blanca" de Python.


## Especificaciones
  Recolecta, limpia y valida el dato que representa el CPF, debe tener 11 dígitos, ejemplo: CPF 746.824.890-70

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primera etapa: Calcular el primer dígito</th>
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
      <td><strong>Resultados sumados</strong></td>
      <td>301</td>
    </tr>
    <tr>
      <td><strong>Resultado sumado multiplicado por 10</strong></td>
      <td>3010</td>
    </tr>
    <tr>
      <td><strong>Resto de la división por 11</strong></td>
      <td>7</td>
    </tr>
  </tbody>
</table>

Si el resultado del cálculo es mayor que 9, entonces considerar 0,  
si no, considerar el valor resultante.

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primera etapa: Calcular el primer dígito</th>
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
      <td><strong>Resultado del cálculo anterior:</strong></td>
      <td>7</td>
    </tr>
    <tr>
  </tbody>
</table>

Si el valor encontrado coincide con el primer dígito del complemento, entonces este dígito es válido.

## Nota: Para la segunda etapa, basta repetir el cálculo incluyendo el primer dígito válido:

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Segunda etapa: Calcular el segundo dígito</th>
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
      <td><strong>Resultados sumados</strong></td>
      <td>363</td>
    </tr>
    <tr>
      <td><strong>Resultado sumado multiplicado por 10</strong></td>
      <td>3630</td>
    </tr>
    <tr>
      <td><strong>Resto de la división por 11</strong></td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Si el resultado del cálculo es mayor que 9, entonces considerar 0,  
si no, considerar el valor resultante.

<table border="1" style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th colspan="12"  style="text-align:center;">Primera etapa: Calcular el primer dígito</th>
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
      <td><strong>Resultado del cálculo anterior:</strong></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
  </tbody>
</table>

Si el valor encontrado coincide con el primer dígito del complemento, entonces este dígito es válido.

## Etapas y funcionalidades:

### funcionalidades

1. Generar CPF válido. 
2. Validar CPF existente.

### Etapas

![.](/assets/Diagrama%20Validação%20CPF%20ES.png)


## Cómo utilizar:
1. Clona el proyecto en un entorno que tenga instalado Python  ![Bash](https://img.shields.io/badge/Python-3.12.3-blue) o superior.

2. Ejecuta el proyecto y sigue las instrucciones que aparezcan.
```bash
> python3 main.py
```
