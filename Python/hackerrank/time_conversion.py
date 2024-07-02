
from time import sleep

def statement():
    print('''
Dado um horário no formato de 12 horas AM/PM, converta-o para o horário militar 
(formato de 24 horas).

Nota:
- 12:00:00AM no relógio de 12 horas é 00:00:00 no relógio de 24 horas.
- 12:00:00PM no relógio de 12 horas é 12:00:00 no relógio de 24 horas.

Exemplo:

s = '12:01:PM'
Retorne '12:01:00'.

s = '12:01:00AM'
Retorne '00:01:00'.

Descrição da Função:

Complete a função timeConversion no editor abaixo. Ela deve retornar uma nova 
string representando o horário de entrada no formato de 24 horas.

timeConversion tem o(s) seguinte(s) parâmetro(s):

string s: um horário no formato de 12 horas

Retornos:

string: o horário no formato de 24 horas

Formato de Entrada:

Uma única string, 's', que representa um horário no formato de relógio de 12 
horas (ou seja: hh:mm:ssAM ou hh:mm:ssPM).

Restrições:

Todos os horários de entrada são válidos

Exemplo de Entrada 0:

07:05:45PM

Exemplo de Saída 0:

19:05:45
''')

def timeConversion(s):

    # Verifica se o meridiano é AM ou PM
    meridiano = s[-2:]

    # Extração da hora, minuto e segundo
    hora = s[:2]
    minuto = s[3:5]
    segundo = s[6:8]

    # Se o caso for AM
    if meridiano == "AM":
        if hora == "12":
            hora = "00"

    # Se o caso for PM
    else:
        if hora != "12":
            hora = str(int(hora) + 12)

    # Construção do formato de 24 horas
    resultado = f"{hora}:{minuto}:{segundo}"
    
    return resultado

if __name__ == '__main__':

    statement()
    
    s = input('Digite a hora para efetuar a formatação para 24h: ').upper()

    sleep(2)
    print(timeConversion(s))
