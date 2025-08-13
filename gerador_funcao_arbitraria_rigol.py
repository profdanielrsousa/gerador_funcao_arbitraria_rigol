#  GERADOR DE FORMA DE ONDA ARBITRÁRIA PARA O GERADOR DE FUNÇÃO
#  DOS OSCILOSCÓPIOS RIGOL DHO914S E DHO924S
#  ESTE PROGRAMA GERA UMA FORMA DE ONDA SENOIDAL, PODENDO SER ADAPTADO PARA OUTRAS FORMAS DE ONDA
#  O CÓDIGO FOI BASEADO NO ORIGINAL DE LUIZ FERNANDO PINTO DE OLIVEIRA
#  (https://github.com/LuizFernandoOliveira/RIGOL-data-converter)
#  DANIEL RODRIGUES DE SOUSA 13/08/2025

import numpy as np
import matplotlib.pyplot as plt
import csv

# Parâmetros
N = 8192            # Valor fixo. O período deverá ter 8192 valores 
AMP = 1             # Valor da amplitude em Vpp. Note que este valor deve corresponder
                    # a tensão Vpp da forma de onda gerada
FREQ = 250e3        # Frequência em Hz
PERIOD = 1 / FREQ

# Uma vez carregado o arquivo, no próprio menu do gerador de função você poderá
# alterar a frequência e a amplitude

# Geração da função senoidal
t = np.linspace(0, 1, N)        # Aqui os valores vão de 0 a 1, divididos em 8192 partes.
                                # Dependendo da função implementada, você poderá mudar o range,
                                # desde que o tempo final menos o tempo inicial resulte em 1.
                                # Exemplo: t = np.linspace(-0.5, 0.5, N)
                                
y = 0.5 * np.sin(2 * np.pi * t) # A função, neste caso seno

# Plot do sinal
# Este plot é uma simples conferência. Após fechar a janela, o arquivo é gerado.
plt.plot(t, y)
plt.xlabel('Tempo [s]')
plt.ylabel('Tensão [V]')
plt.title('Sinal Senoidal')
plt.grid(True)
plt.show()

# Escrita no arquivo CSV no formato RIGOL DHO914S / DHO924S
with open('output.csv', 'w') as file:
    # Cabeçalho obrigatório
    file.write('RIGOL:DG1:CSV DATA FILE\n')
    file.write('TYPE:Arb\n')
    file.write(f'AMP:{AMP:.3f} Vpp\n')
    file.write(f'PERIOD:{PERIOD:.3e} S\n')
    file.write('DOTS:8192\n')
    file.write('MODE:Freq\n')
    file.write(f'AFG Frequency:{FREQ:.3f}\n')
    file.write('AWG N:0\n')
    file.write('x,y[V]\n')

    # Dados da função no formato ",valor"
    for value in y:
        file.write(f',{value:.5f}\n')

print("Arquivo 'output.csv' gerado com sucesso.")
