# 🧠 Real-Time Memory Allocation Tracker

A visual and interactive Python-based tool that simulates and tracks memory allocation in real-time using **Paging** and **Segmentation** techniques.

## 📌 Project Overview

This tool helps visualize how memory is allocated to processes in an operating system using real-time updates. It is designed with a user-friendly GUI and provides memory tracking from a user's perspective — not just a developer's.

---

## 🎯 Features

### 🔹 GUI Module
- Intuitive interface built using **Tkinter**
- Easy input of process ID, page count, and segment info
- Interactive buttons to trigger memory allocation, deallocation, and visualization

### 🔹 Memory Management Module
- Implements **Paging and Segmentation**
- Supports allocation algorithms like:
  - First Fit
  - Best Fit
  - Worst Fit
- Performs defragmentation and memory optimization

### 🔹 Visualization Module
- Real-time heatmap of memory blocks using **Seaborn/Matplotlib**
- Separate color blocks per process
- Displays:
  - Page usage % (used vs empty)
  - Legends showing process IDs and segments
  - User-friendly memory insights (not technical-only)

---

## 🛠️ Technologies Used

| Component | Technology |
|----------|------------|
| Language | Python 3.x |
| GUI      | Tkinter |
| Visualization | Matplotlib, Seaborn |
| Backend Logic | Custom `MemoryManager` class |
| Git | Version control |
| Platform Tested | macOS |

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/memory-tracker.git
   cd memory-tracker
