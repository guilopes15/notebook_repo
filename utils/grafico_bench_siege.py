import matplotlib.pyplot as plt
import numpy as np

dados = 'dict do bechmark siege'

fig = plt.figure(figsize=(16, 10))
fig.suptitle('Análise de Performance - Siege Load Test', fontsize=16, fontweight='bold')

ax1 = plt.subplot(2, 3, 1)
transacoes = [dados['successful_transactions'], dados['failed_transactions']]
cores = ['#2ecc71', '#e74c3c']
ax1.pie(transacoes, labels=['Sucesso', 'Falha'], autopct='%1.1f%%', 
        colors=cores, startangle=90)
ax1.set_title(f'Transações Totais: {dados["transactions"]}')

ax2 = plt.subplot(2, 3, 2)
tempos = ['Tempo Médio\nResposta', 'Transação\nMais Longa', 'Transação\nMais Curta']
valores_tempo = [dados['response_time'], dados['longest_transaction'], 
                 dados['shortest_transaction']]
cores_tempo = ['#3498db', '#e67e22', '#1abc9c']
bars = ax2.bar(tempos, valores_tempo, color=cores_tempo, alpha=0.7)
ax2.set_ylabel('Tempo (segundos)')
ax2.set_title('Análise de Tempos de Resposta')
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}s', ha='center', va='bottom')

ax3 = plt.subplot(2, 3, 3)
metricas = ['Taxa de\nTransações', 'Throughput']
valores = [dados['transaction_rate'], dados['throughput']]
cores_metricas = ['#9b59b6', '#34495e']
x = np.arange(len(metricas))
bars = ax3.bar(x, valores, color=cores_metricas, alpha=0.7)
ax3.set_xticks(x)
ax3.set_xticklabels(metricas)
ax3.set_ylabel('Valor')
ax3.set_title('Performance')
for i, bar in enumerate(bars):
    height = bar.get_height()
    unidade = 'trans/s' if i == 0 else 'MB/s'
    ax3.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}\n{unidade}', ha='center', va='bottom')
    
ax4 = plt.subplot(2, 3, 4)
disponibilidade = dados['availability']
ax4.barh(['Disponibilidade'], [disponibilidade], color='#27ae60', alpha=0.7)
ax4.set_xlim([0, 100])
ax4.set_xlabel('Percentual (%)')
ax4.set_title(f'Disponibilidade: {disponibilidade}%')
ax4.text(disponibilidade/2, 0, f'{disponibilidade}%', 
         ha='center', va='center', fontsize=14, fontweight='bold', color='white')

ax5 = plt.subplot(2, 3, 5)
ax5.bar(['Concorrência'], [dados['concurrency']], color='#e74c3c', alpha=0.7)
ax5.set_ylabel('Usuários Simultâneos')
ax5.set_title(f'Concorrência: {dados["concurrency"]:.2f} usuários')
ax5.text(0, dados['concurrency']/2, f'{dados["concurrency"]:.2f}', 
         ha='center', va='center', fontsize=14, fontweight='bold')

ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')
resumo = f"""
RESUMO DO TESTE

Tempo Total: {dados['elapsed_time']:.2f}s
Dados Transferidos: {dados['data_transferred']:.2f} MB

Performance:
• {dados['transaction_rate']:.2f} transações/segundo
• {dados['response_time']:.2f}s tempo médio resposta
• {dados['concurrency']:.2f} usuários concorrentes

Resultado:
✓ {dados['successful_transactions']} transações bem-sucedidas
✗ {dados['failed_transactions']} transações falhadas
✓ {dados['availability']:.2f}% disponibilidade
"""
ax6.text(0.1, 0.5, resumo, fontsize=11, verticalalignment='center',
         family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()

plt.savefig('siege_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico salvo como 'siege_analysis.png' na raiz do projeto")


# plt.show()