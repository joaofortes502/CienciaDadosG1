import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('digital_diet_mental_health.csv')


# 1. Histograma do tempo de tela diário

plt.figure()
plt.hist(df['daily_screen_time_hours'], bins=20)
plt.title('Distribuição do Tempo de Tela Diário')
plt.xlabel('Horas por dia')
plt.ylabel('Número de Participantes')
plt.tight_layout()
plt.savefig('1tempoTelaXnumParticipantes.png')
plt.close()


# 2. Barra: Tempo médio de tela por quartil de ansiedade semanal

df['anxiety_quartile'] = pd.qcut(df['weekly_anxiety_score'], 4, labels=['Q1 (Baixo)', 'Q2', 'Q3', 'Q4 (Alto)'])
mean_screen = df.groupby('anxiety_quartile')['daily_screen_time_hours'].mean().reindex(['Q1 (Baixo)', 'Q2', 'Q3', 'Q4 (Alto)'])
plt.figure()
mean_screen.plot(kind='bar')
plt.title('Tempo Médio de Tela por Quartil de Ansiedade')
plt.xlabel('Quartil de Ansiedade')
plt.ylabel('Horas de Tela por dia')
plt.tight_layout()
plt.savefig('2tempoMedioTelaXquartilAnsiedade.png')
plt.close()


# 3. Barra: Score médio de saúde mental por faixa de tempo de tela

df['screen_time_cat'] = pd.cut(df['daily_screen_time_hours'],
                               bins=[0,2,4,6,8,24],
                               labels=['0-2','2-4','4-6','6-8','8+'],
                               right=False)
avg_mh = df.groupby('screen_time_cat')['mental_health_score'].mean()
plt.figure()
avg_mh.plot(kind='bar')
plt.title('Score Médio de Saúde Mental por Faixa de Tempo de Tela')
plt.xlabel('Tempo de Tela (h/dia)')
plt.ylabel('Score Médio de Saúde Mental')
plt.tight_layout()
plt.savefig('3scoreMedioXtempoTela.png')
plt.close()


# 4. Linha: Idade x Tempo médio de tela

age_screen = df.groupby('age')['daily_screen_time_hours'].mean().sort_index()
plt.figure()
age_screen.plot()
plt.title('Tempo Médio de Tela por Idade')
plt.xlabel('Idade')
plt.ylabel('Horas de Tela por dia')
plt.tight_layout()
plt.savefig('4idadeXtempoMedio.png')
plt.close()


# 5. Pizza: Distribuição percentual das faixas de tempo de tela 

count_cat = df['screen_time_cat'].value_counts().reindex(['0-2','2-4','4-6','6-8','8+'])
plt.figure()
count_cat.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Faixas de Tempo de Tela')
plt.ylabel('')
plt.tight_layout()
plt.savefig('5faixasTempoTela.png')
plt.close()


# 6. Linha: Score médio de saúde mental por Idade

mean_mh_age = df.groupby('age')['mental_health_score'].mean().sort_index()
plt.figure()
mean_mh_age.plot(marker='o')
plt.title('Score Médio de Saúde Mental por Idade')
plt.xlabel('Idade')
plt.ylabel('Score Médio de Saúde Mental')
plt.tight_layout()
plt.savefig('6scoreXidade.png')
plt.close()

