# 🚀 Day 0 – VSD Program Kickoff & Toolchain Setup  

<div align="center">

![Program](https://img.shields.io/badge/VSD-Hardware%20Design-blue?style=for-the-badge&logo=semanticscholar)  
![Track](https://img.shields.io/badge/Track-RTL2GDS-orange?style=for-the-badge)  
![Progress](https://img.shields.io/badge/Progress-Day%200-success?style=for-the-badge)  

</div>  

Welcome to the very first step of my **Silicon Diary** 📝.  
Day 0 was all about **laying the foundation**: 
- Getting started with Digital VLSI SOC Design and Planning
- Creating this GitHub repository to document my journey.  
- Setting up a **Linux-based design environment** and installing essential tools.  

---

## 🎯 Task Breakdown  

| # | Task | Outcome |
|---|------|---------|
| 1️⃣ | **Summarize Getting started with Digital VLSI SOC Design and Planning Video** | Key takeaways captured with screenshot |
| 2️⃣ | **Install Open-Source EDA Tools** | Yosys, Icarus Verilog, GTKWave, Ngspice, Magic VLSI installed & tested |

---

## ![Task 1](https://img.shields.io/badge/Task%201-Video%20Summary-blueviolet?style=for-the-badge)  

The introductory session explained the **SoC design flow** step by step:  

- **Specs (C model)** ➝ High-level system behavior defined in C.  
- **RTL Design (Verilog)** ➝ Hardware description created by RTL architects.  
- **Processor + IPs** ➝ Integration of processor core and peripherals.  
- **Gate-level Netlist** ➝ RTL synthesized into logic gates.  
- **SoC Integration** ➝ Combining macros, analog IPs, and GPIOs.  
- **Floorplanning & GDSII** ➝ Physical design and final tape-out.  

## 📷 **Flow Chart of SoC design flow**
<p align="center">
  <img src="Images/SoC Design Flow.png" alt="SoC Design Flow" width="600">

</p>

<div align="center"></div>

---
## ![Task 2](https://img.shields.io/badge/Task%202-EDA%20Tool%20Setup-green?style=for-the-badge)

Installed all required open-source EDA tools for the RTL2GDS flow using a Linux-based setup.  
This section provides an overview of each tool, its purpose in the design flow, and a snapshot of successful installation.

---

## 🧠 Yosys – RTL Synthesis

- **What is it?**  
  _[Add description here]_

- **Purpose in Design Flow:**  
  _[Add purpose here]_
---
<details>
<summary>📌 <b>Installation Steps</b></summary>  

```bash
Yosys
$ sudo apt-get update
$ git clone https://github.com/YosysHQ/yosys.git
$ cd yosys
$ sudo apt install make (If make is not installed please install it)
$ sudo apt-get install build-essential clang bison flex \
libreadline-dev gawk tcl-dev libffi-dev git \
graphviz xdot pkg-config python3 libboost-system-dev \
libboost-python-dev libboost-filesystem-dev zlib1g-dev
$ make config-gcc
$ make
```
</details>
---
- **📸 Snapshot:**  
  ![Yosys](Images/yosys-snapshot.png)

- **🔗 References:**  
  - [ ] [Add Reference 1](#)
  - [ ] [Add Reference 2](#)

---

## ⚙️ Icarus Verilog – HDL Simulation

- **What is it?**  
  _[Add description here]_

- **Purpose in Design Flow:**  
  _[Add purpose here]_
---<details>
<summary>📌 <b>Installation Steps</b></summary>  

```bash
Yosys
$ sudo apt-get update
$ git clone https://github.com/YosysHQ/yosys.git
$ cd yosys
$ sudo apt install make (If make is not installed please install it)
$ sudo apt-get install build-essential clang bison flex \
libreadline-dev gawk tcl-dev libffi-dev git \
graphviz xdot pkg-config python3 libboost-system-dev \
libboost-python-dev libboost-filesystem-dev zlib1g-dev
$ make config-gcc
$ make
```
</details>
---
- **📸 Snapshot:**  
  ![Icarus Verilog](Images/iverilog-snapshot.png)

- **🔗 References:**  
  - [ ] [Add Reference 1](#)
  - [ ] [Add Reference 2](#)

---

## 📈 GTKWave – Waveform Viewer

- **What is it?**  
  _[Add description here]_

- **Purpose in Design Flow:**  
  _[Add purpose here]_

- **📸 Snapshot:**  
  ![GTKWave](Images/gtkwave-snapshot.png)

- **🔗 References:**  
  - [ ] [Add Reference 1](#)
  - [ ] [Add Reference 2](#)

---

## 🔁 Ngspice – Analog Simulation

- **What is it?**  
  _[Add description here]_

- **Purpose in Design Flow:**  
  _[Add purpose here]_

- **📸 Snapshot:**  
  ![Ngspice](Images/ngspice-snapshot.png)

- **🔗 References:**  
  - [ ] [Add Reference 1](#)
  - [ ] [Add Reference 2](#)

---

## 🧱 Magic VLSI – Layout Editor

- **What is it?**  
  _[Add description here]_

- **Purpose in Design Flow:**  
  _[Add purpose here]_

- **📸 Snapshot:**  
  ![Magic VLSI](Images/magic-snapshot.png)

- **🔗 References:**  
  - [ ] [Add Reference 1](#)
  - [ ] [Add Reference 2](#)

---

