import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_paging(memory_manager):
    """Visualizes paging memory allocation."""
    pages = memory_manager.pages
    plt.bar(range(len(pages)), pages, color=['green' if p == 0 else 'red' for p in pages])
    plt.xlabel("Page Number")
    plt.ylabel("Allocation Status")
    plt.title("Memory Paging Visualization")
    plt.show()

def visualize_segmentation(memory_manager):
    """Visualizes segmentation memory allocation."""
    segments = memory_manager.segment_table
    data = np.zeros((1, len(memory_manager.pages)))  # 1 row, multiple columns
    for _, (base, size) in segments.items():
        data[0, base:base+size] = 1  # Mark allocated segments

    sns.heatmap(data, cmap="coolwarm", cbar=False, xticklabels=False, yticklabels=False)
    plt.title("Memory Segmentation")
    plt.show()
