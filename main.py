import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parâmetros da Rede
v_rms = 220
v_dc = 600
freq = 60
v_pico = v_rms * np.sqrt(2)

# Parâmetros da Simulação
f_amostragem = 100e3
t_final = 0.05
t = np.arange(0, t_final, 1/f_amostragem)

# Equação da Tensão da Rede
w = 2*np.pi*freq
v_rede = v_pico * np.sin(w*t)

# Parâmetros do invertos
freq_sw = 10e3
w_sw = 2* np.pi*freq_sw

# Equação da Onda Portadora Triangular
portadora = signal.sawtooth(freq_sw*t, width=0.5)* (v_dc / 2)

# 3. Lógica do Inversor (Bipolar para começar)
# Se a referência for maior que a portadora, sai +Vdc. Se não, sai -Vdc.
v_ab = np.where(v_rede > portadora, v_dc, -v_dc)

# Parâmetro do filtro
L = 8e-3
R = 0.1
dt = 1/f_amostragem

# Inicialização do array de corrente
i_saida = np.zeros_like(t)

# Simulação dinâmica do inversor
for k in range(1, len(t)):
    # Tensão sobre o indutor = V_inversor - V_rede - Queda na resistência
    v_l = v_ab[k] - v_rede[k] - R*i_saida[k-1]

    i_saida[k] = i_saida[k-1] + (v_l/L)*dt

# Plotagem
plt.figure(figsize = (10,4))
plt.plot(t * 1000, v_rede, label = 'Tensão da Rede (220V RMS)')
plt.plot(t * 1000, portadora, label = 'Portadora')
plt.plot(t * 1000, v_ab, label = 'PWM')
plt.plot(t * 1000, i_saida, label = 'Corrente')
plt.title('Modelagem da Referência da Rede Elétrica - 60Hz')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.show()



