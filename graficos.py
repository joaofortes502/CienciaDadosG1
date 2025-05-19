import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('digital_diet_mental_health.csv')


# =========================================================================
# 1. Histograma — Distribuição das horas totais de tela por dia
#    (abre a apresentação mostrando de que escala estamos falando)
# =========================================================================
plt.figure()
plt.hist(df['daily_screen_time_hours'], bins=20)
plt.title('Distribuição do Tempo de Tela Diário')
plt.xlabel('Horas por dia')
plt.ylabel('Número de Participantes')
plt.tight_layout()
plt.savefig('01_hist_tempo_tela.png')
plt.close()

# -------------------------------------------------------------------------
# Preparação comum: categorias de tempo de tela (usaremos em vários gráficos)
# -------------------------------------------------------------------------
df['screen_time_cat'] = pd.cut(
    df['daily_screen_time_hours'],
    bins=[0,2,4,6,8,24],
    labels=['0‑2h','2‑4h','4‑6h','6‑8h','8h+'],
    right=False)

# =========================================================================
# 2. Pizza — Percentual de participantes em cada faixa de tempo de tela
# =========================================================================
count_cat = df['screen_time_cat'].value_counts().reindex(['0‑2h','2‑4h','4‑6h','6‑8h','8h+'])
plt.figure()
count_cat.plot(kind='pie', autopct='%1.1f%%', startangle=90, pctdistance=0.8)
plt.title('Distribuição das Faixas de Tempo de Tela')
plt.ylabel('')
plt.tight_layout()
plt.savefig('02_pizza_tela.png')
plt.close()

# =========================================================================
# 3. Barra — Como o TEMPO TOTAL de tela se divide por tipo de dispositivo
# =========================================================================
# Somar horas por tipo e normalizar por participantes para média
media_dispositivos = {
    'Telefone': df['phone_usage_hours'].mean(),
    'Laptop/PC': df['laptop_usage_hours'].mean(),
    'Tablet': df['tablet_usage_hours'].mean(),
    'TV/Streaming': df['tv_usage_hours'].mean()
}
plt.figure()
plt.bar(media_dispositivos.keys(), media_dispositivos.values())
plt.title('Tempo Médio de Tela por Tipo de Dispositivo')
plt.ylabel('Horas por dia')
plt.tight_layout()
plt.savefig('03_bar_dispositivos.png')
plt.close()

# =========================================================================
# 4. Linha — Duração média de sono vs. faixas de tempo de tela
# =========================================================================
mean_sleep = df.groupby('screen_time_cat')['sleep_duration_hours'].mean()
plt.figure()
mean_sleep.plot(marker='o')
plt.title('Sono Médio por Faixa de Tempo de Tela')
plt.xlabel('Faixa de Tempo de Tela')
plt.ylabel('Horas de Sono por Noite')
plt.tight_layout()
plt.savefig('04_line_sono_tela.png')
plt.close()

# =========================================================================
# 5. Barra — Stress médio por faixa de tempo de tela
# =========================================================================
mean_stress = df.groupby('screen_time_cat')['stress_level'].mean()
plt.figure()
mean_stress.plot(kind='bar')
plt.title('Stress Médio por Faixa de Tempo de Tela')
plt.xlabel('Faixa de Tempo de Tela')
plt.ylabel('Score Médio de Stress (1‑10)')
plt.tight_layout()
plt.savefig('05_bar_stress_tela.png')
plt.close()

# =========================================================================
# 6. Linha — Score médio de saúde mental por Idade
# =========================================================================
mean_mh_age = df.groupby('age')['mental_health_score'].mean().sort_index()
plt.figure()
mean_mh_age.plot(marker='o')
plt.title('Score Médio de Saúde Mental por Idade')
plt.xlabel('Idade')
plt.ylabel('Score Médio de Saúde Mental')
plt.tight_layout()
plt.savefig('06_line_saude_idade.png')
plt.close()
