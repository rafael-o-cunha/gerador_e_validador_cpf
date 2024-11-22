import random
import sys

def cleanDataAndValidateLen(inputUser):
    newData = ''
    for c in inputUser:
        if c.isdigit():
            newData += c
            
    if len(newData) == 11:
        return newData, True
    return newData, False

def validationOfDigits(cpf, digit):
    count = 0
    result = 0
    for c in range(len(cpf) - (1 if digit == 1 else 0), 1, -1):
        part = c * int(cpf[count])
        result += part
        count += 1
    result = (result * 10) % 11
    result = result if result <= 9 else 0
    return True if result == int(cpf[len(cpf) - (2 if digit == 1 else 1)]) else False

def generateRandomValue():
    cpf = ''
    for i in range(11):
        cpf += str(random.randint(0, 9))
    return cpf

def CPFValidate(cpf):
    status = validationOfDigits(cpf, 1) 
    if status == True:
        status = validationOfDigits(cpf, 2)
    
    return status


def main():
    value = ''
    cpf = ''
    result = False
    status = False
    print('-----------------------------------------------------------------------------')
    print('                        Gerador / Validador de CPF')
    print('-----------------------------------------------------------------------------')
    print('Digite a opção desejada: ')
    opt = input('1 Para gerar CPF e 2 apenas para validar um CPF existente:')
    if int(opt) == 1:
        while status == False:
            value = generateRandomValue()
            cpf, status = cleanDataAndValidateLen(value)    
            if status == True:
                status = CPFValidate(cpf)
    
    elif int(opt) == 2:
        value = input('Digite o CPF a ser verificado: ')
        cpf, status = cleanDataAndValidateLen(value) 
        if status == True:
                status = CPFValidate(cpf)  
                if status == False:
                    print(f'\nCPF {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} é inválido') 
                    print('-----------------------------------------------------------------------------')
                    sys.exit()
       
        elif status == False:
            print('\nCPF digitado não possui o tamanho padrão [11 dígitos]')
            print('-----------------------------------------------------------------------------')
            sys.exit()

    if status == True:
            print(f'\nCPF Válido: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}') 
            print('-----------------------------------------------------------------------------')
            sys.exit()

if __name__ == "__main__":
    main()