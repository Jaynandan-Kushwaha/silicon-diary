
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
  <img src="" 
       alt="SoC Design Flow" width="600"/>
</p>

<div align="center">


---

## ![Task 2](https://img.shields.io/badge/Task%202-EDA%20Tool%20Setup-green?style=for-the-badge)  

### 🧠 Yosys – RTL Synthesis  

<details>
<summary>📌 <b>Installation Steps</b></summary>  

```bash
sudo apt-get update
sudo apt-get install yosys
