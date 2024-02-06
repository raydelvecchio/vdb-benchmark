import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('benchmark.xlsx')

for i, (idx, row) in enumerate(data.iterrows()):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    values = row[1:]
    categories = data.columns[1:]
    x = np.arange(len(values))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(values)))
    
    bars = ax.bar(x, values, color=colors)
    
    for bar, category, value in zip(bars, categories, values):
        text_position = bar.get_height() + 0.003

        if category == "VLite2":
            ax.text(bar.get_x() + bar.get_width() / 2, text_position,
                f'{value:.4f}', ha='center', va='bottom', fontweight='bold')
        else:
            ax.text(bar.get_x() + bar.get_width() / 2, text_position,
                f'{value:.4f}', ha='center', va='bottom')
    
    ax.set_title(f'Benchmark: {row[0]}')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45)
    ax.set_ylabel('Time (s)')
    
    plt.tight_layout()
    plt.savefig(f'./results/benchmark_{i+1}_{row[0]}.png')
