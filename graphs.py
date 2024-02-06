import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('benchmark.xlsx')

for i, (idx, row) in enumerate(data.iterrows()):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    values = row[1:]
    categories = data.columns[1:]
    x = np.arange(len(values))
    
    bars = ax.bar(x, values)
    
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                f'{value:.4f}', ha='center', va='bottom')
    
    ax.set_title(f'Benchmark: {row[0]}')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45)
    ax.set_ylabel('Time (s)')
    
    plt.tight_layout()
    plt.savefig(f'./results/benchmark_{i+1}_{row[0]}.png')

file_paths = [f'./results/benchmark_{i+1}_{row[0]}.png' for i, row in data.iterrows()]
