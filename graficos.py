import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar dados
df = pd.read_csv('digital_diet_mental_health.csv')


# =========================================================================
# 1. Histograma — Distribuição das horas totais de tela por dia
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
# Preparação comum: categorias de tempo de tela 
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
# 4. Barra — Tempo Médio de Tela por Finalidade (Trabalho, Lazer, Estudos)
# =========================================================================
media_purpose = {
    'Trabalho': df['work_related_hours'].mean(),
    'Lazer': (df['entertainment_hours'] + df['gaming_hours'] + df['social_media_hours']).mean(),
    'Estudos': (df['laptop_usage_hours'] - df['work_related_hours']).clip(lower=0).mean()
}
plt.figure()
plt.bar(media_purpose.keys(), media_purpose.values())
plt.title('Tempo Médio de Tela por Finalidade')
plt.ylabel('Horas por dia')
plt.tight_layout()
plt.savefig('04_bar_tela_finalidade.png')
plt.close()


# =========================================================================
# 5. Dispersão com linha de tendência - Tempo de tela vs. Saúde Mental
# =========================================================================
plt.figure(figsize=(10,6))
sns.regplot(
    data=df,
    x='daily_screen_time_hours',
    y='mental_health_score',
    scatter_kws={'alpha':0.4, 'color':'#4c72b0'},
    line_kws={'color':'#dd8452', 'lw':2}
)
plt.title('Relação entre Tempo de Tela e Saúde Mental')
plt.xlabel('Horas diárias de tela')
plt.ylabel('Pontuação de Saúde Mental (0-100)')
plt.tight_layout()
plt.savefig('05_dispersao_saude_mental.png')
plt.close()

# =========================================================================
# 6. Barras Agrupadas - Sono e Atividade Física por Faixa de Tela
# =========================================================================
# Calcular médias agrupadas
media_sono_atividade = df.groupby('screen_time_cat').agg({
    'sleep_duration_hours': 'mean',
    'physical_activity_hours_per_week': 'mean'
}).reset_index()

# Configurar o gráfico
plt.figure(figsize=(12, 6))
largura_barra = 0.35
indices = np.arange(len(media_sono_atividade))

# Barras para Sono
plt.bar(
    indices - largura_barra/2,
    media_sono_atividade['sleep_duration_hours'],
    width=largura_barra,
    label='Horas de Sono (média diária)',
    color='#3498db',
    alpha=0.8
)

# Barras para Atividade Física
plt.bar(
    indices + largura_barra/2,
    media_sono_atividade['physical_activity_hours_per_week'],
    width=largura_barra,
    label='Atividade Física (horas/semana)',
    color='#27ae60',
    alpha=0.8
)

# Customização
plt.title('Comparação de Sono e Atividade Física por Faixa de Tempo de Tela')
plt.xlabel('Faixa de Horas Diárias')
plt.ylabel('Horas')
plt.xticks(indices, media_sono_atividade['screen_time_cat'])
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('06_barras_sono_atividade.png')
plt.close()