import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da Rede
v_rms = 220
freq = 60
v_pico = v_rms * np.sqrt(2)

# Parâmetros da Simulação
f_amostragem = 100e3
t_final = 0.05
t = np.arange(0, t_final, 1/f_amostragem)

# Equação da Tensão da Rede
w = 2*np.pi*freq
v_rede = v_pico * np.sin(w*t)

# Plotagem
plt.figure(figsize = (10,4))
plt.plot(t * 1000, v_rede, label = 'Tensão da Rede (220V RMS)')
plt.title('Modelagem da Referência da Rede Elétrica - 60Hz')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.show()

