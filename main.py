import pandas as pd
import matplotlib.pyplot as plt

# Suponha que seu DataFrame tenha essas colunas
# 'acceleration' e 'brake' variam entre 0 e 100%
data = pd.read_csv('telemetry_data.csv')

# Configurando bins (faixas de intensidade)
bins = [0, 25, 50, 75, 100]

# Histograma para aceleração
plt.hist(data['acceleration'], bins=bins, alpha=0.5, label='Aceleração', color='green')

# Histograma para frenagem
plt.hist(data['brake'], bins=bins, alpha=0.5, label='Frenagem', color='red')

# Configuração do gráfico
plt.xlabel('Intensidade (%)')
plt.ylabel('Frequência')
plt.title('Histograma de Frenagem e Aceleração')
plt.legend(loc='upper right')

# Exibir o gráfico
plt.show()
