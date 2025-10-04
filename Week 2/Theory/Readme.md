# 🚀 BabySoC – Learning SoC Design with RVMYTH, PLL, and DAC

## 📝 Problem Statement  
This project focuses on building a compact, educational **System on Chip (SoC)** based on **RVMYTH**, a simple RISC-V processor core.  
To make it more realistic, BabySoC integrates:  

- **Phase-Locked Loop (PLL)** → For generating stable, high-frequency clocks.  
- **10-bit Digital-to-Analog Converter (DAC)** → To bridge the digital and analog worlds.  

By converting digital signals into analog form, the DAC enables BabySoC to interact with external devices like **monitors, televisions, and mobile systems**, where the outputs could represent **audio or video signals**.  

The design is implemented on **Sky130 technology** and aims to serve as an **open-source, beginner-friendly platform** for students, hobbyists, and engineers exploring **digital–analog integration in chip design**.  

---

## 🔎 1. What is a System on Chip (SoC)?  
A **System on Chip (SoC)** is essentially a **complete computer built on a single chip**.  
Instead of having separate chips for the processor, memory, and peripherals, an SoC brings them all together into a **compact unit**.  

This makes SoCs ideal for modern devices where **performance, power efficiency, and space** are all critical.  
From smartphones to smartwatches and IoT devices, SoCs are the reason our technology is both **powerful and portable**.  

---

## 🧩 2. Key Components of an SoC  

- **CPU (Central Processing Unit)** → The “brain” of the chip; executes instructions, calculations, and controls overall operation.  
- **Memory** →  
  - RAM stores temporary data while programs run.  
  - ROM/Flash provides long-term storage for boot code and essential data.  
- **I/O Interfaces** → Connects the SoC to the outside world (USB, camera, sensors, audio jacks).  
- **GPU (Graphics Processing Unit)** → Handles image and video rendering for displays and games.  
- **DSP (Digital Signal Processor)** → Specialized for tasks like audio processing, filters, and signal enhancement.  
- **Power Management** → Ensures energy efficiency and extends battery life.  
- **Additional Blocks** → Wireless (Wi-Fi, Bluetooth), Security modules, Analog/Mixed-signal interfaces like DACs and ADCs.  

---

## 🏷️ 3. Types of SoCs  

Different SoCs are designed for different applications:  

1. **Microcontroller-based SoCs**  
   - Built around simple CPU cores with memory & peripherals.  
   - Used in IoT, sensors, and embedded systems.  
   - *Example:* ARM Cortex-M, ESP32.  

2. **Microprocessor-based SoCs**  
   - More powerful, capable of running Linux/Android.  
   - Used in smartphones & tablets.  
   - *Example:* Qualcomm Snapdragon, Samsung Exynos.  

3. **Application-Specific SoCs (ASoCs)**  
   - Tailored for high-performance, domain-specific tasks (AI, graphics, networking).  
   - *Example:* Google TPU (AI), NVIDIA Tegra (gaming/graphics).  

4. **Automotive SoCs**  
   - Designed for real-time, reliable operation in vehicles.  
   - *Example:* NVIDIA Drive, Renesas R-Car.  

5. **Multimedia SoCs**  
   - Optimized for audio, video, and display pipelines.  
   - *Example:* MediaTek SoCs in smart TVs.  

👉 **BabySoC** fits into the **Educational/Embedded SoC** category — designed for hands-on learning of CPU cores, clock generation, and digital-to-analog interfacing.  

---

## ⚡ 4. Why SoCs are Important  

- **Compact Design** → Combines multiple functions into one chip, saving board space.  
- **Energy Efficiency** → Reduced power consumption.  
- **Performance Boost** → Faster communication between tightly integrated modules.  
- **Cost-Effective** → Fewer external components reduce manufacturing cost.  
- **Reliability** → Fewer interconnections → fewer chances of failure.  

---

## 🌍 5. Applications of SoCs  

SoCs are used everywhere:  

- **Smartphones & Tablets** → Apple A-series, Qualcomm Snapdragon.  
- **Wearables** → Smartwatches with ultra-low-power SoCs.  
- **IoT Devices** → Smart home sensors & controllers.  
- **Consumer Electronics** → Televisions, gaming consoles, cars.  

---

## 🚧 6. Challenges in SoC Design  

- **Complexity** → Many integrated blocks increase design difficulty.  
- **Thermal Issues** → High integration = heating problems.  
- **Limited Flexibility** → Once fabricated, cannot be easily changed.  

---

## 🎯 In Summary  

A **System on Chip** combines multiple computing and communication blocks into a single silicon platform — making devices **smaller, faster, efficient, and cost-effective**.  

**BabySoC** represents a **learning-friendly SoC** by combining:  

- 🖥️ **RISC-V CPU (RVMYTH)** → Digital computation.  
- ⏱️ **PLL** → Stable high-speed clock management.  
- 🎚️ **DAC** → Digital-to-Analog conversion.  

## SoC Design Flow

<div align="center">
  <img src="Images/soc design flow.webp" alt="Testbench" width="70%">
</div>

# 🌱 VSDBabySoC – A Beginner-Friendly System-on-Chip Journey  

Welcome to **VSDBabySoC** – a compact yet powerful **System on Chip (SoC)** designed not just as a project, but as a **learning adventure** into the world of chip design.  

Built on the open-source **RISC-V architecture**, BabySoC brings together three essential building blocks:  
- 🖥️ **RVMYTH CPU** → the digital brain  
- ⏱️ **Phase-Locked Loop (PLL)** → the clock keeper  
- 🎚️ **10-bit DAC** → the digital-to-analog bridge  

Its primary goal is **simple yet ambitious**: to allow simultaneous testing of three open-source IP cores for the first time, while also calibrating and experimenting with analog components. Think of it as a **mini-laboratory on silicon** where digital logic meets real-world analog signals.  

---

## ✨ Why BabySoC?  
We live in a world where SoCs run **everything** – from smartphones to wearables, from TVs to cars. Yet, understanding how all those moving parts come together can feel overwhelming.  

BabySoC breaks it down into digestible building blocks:  
- A **RISC-V processor** (RVMYTH) for executing instructions and cycling through registers.  
- A **PLL** that generates clean, synchronized clocks to drive the CPU and peripherals.  
- A **DAC** that takes binary data and turns it into smooth analog waveforms (sound, light, video).  

---

## 🧩 BabySoC Components  

### 🔹 RVMYTH (RISC-V CPU)  
The **RVMYTH core** is the heart of BabySoC.  
- Based on the open-source RISC-V ISA.  
- Executes instructions, manages registers, and cycles through data.  
- For this project, values in **register r17** are prepared and sent to the DAC for conversion.  

It represents the **logic and decision-making hub** of the SoC.  

📌 **Block Diagram of CPU Core (Placeholder)**  
![RVMYTH CPU Block Diagram](images/rvmyth_cpu.png)  

---

### 🔹 Phase-Locked Loop (PLL) – *The Clock Keeper*  
A **Phase-Locked Loop (PLL)** is a fundamental circuit in SoCs that ensures everything runs in rhythm.  

#### ⚙️ How PLL Works  
1. **Phase Detector (PD):** Compares the phase of the input clock (reference) with the output clock from the oscillator.  
2. **Loop Filter (LF):** Removes noise from the phase error signal, producing a smooth control voltage.  
3. **Voltage-Controlled Oscillator (VCO):** Adjusts its frequency based on the control voltage, ensuring the output frequency matches the reference.  
4. **Divider (optional):** Generates higher or lower multiples of the reference.  

The PLL works in a feedback loop, “locking” the output frequency and phase to the reference clock.  

📌 **Block Diagram of PLL (Placeholder)**  
![PLL Block Diagram](images/pll_block.png)  

---

### 🔹 Digital-to-Analog Converter (DAC) – *The Digital–Analog Bridge*  
A **DAC** converts binary values (0s and 1s) into real-world analog signals.  

#### ⚙️ How DAC Works  
1. **Digital Input:** A binary number (10 bits in BabySoC).  
2. **Conversion Circuit:** Uses resistor ladders (R-2R) or weighted resistors.  
3. **Analog Output:** A voltage/current proportional to the input value.  

#### 🔎 DAC Architectures  
- **Weighted Resistor DAC** – each bit has a weighted resistor (simple, but impractical at high resolution).  
- **R-2R Ladder DAC** – uses repeating resistors, scalable and stable.  

📌 **Block Diagram of DAC (Placeholder)**  
![DAC Block Diagram](images/dac_block.png)  

---

## ⚙️ How BabySoC Works (Step by Step)  

1. **Initialization & Clocking**  
   - BabySoC receives an input clock.  
   - The **PLL multiplies and stabilizes** it.  
   - The synchronized clock feeds both CPU and DAC.  

2. **Data Processing with RVMYTH**  
   - The CPU executes instructions.  
   - Updates values in register **r17** with new data.  
   - Prepares digital values for conversion.  

3. **Digital-to-Analog Conversion**  
   - The DAC receives the digital values.  
   - Converts them into analog voltages.  
   - Output is written to a file (`OUT`) or connected to external devices.  

📌 **BabySoC Top-Level Block Diagram (Placeholder)**  
![BabySoC Block Diagram](images/babysoc_block.png)  

👉 The end result: **Binary → Instructions → Registers → DAC → Analog Signals** 🎵📺  

---

💡 **BabySoC fits in the Educational/Embedded SoC category** — focused on teaching SoC design fundamentals and experimenting with digital–analog integration.  

---


## 🎯 In Summary  

- **VSDBabySoC** integrates:  
  - 🖥️ **RVMYTH CPU** (logic and control)  
  - ⏱️ **PLL** (stable timing)  
  - 🎚️ **DAC** (analog bridge)  

- It provides a hands-on platform to:  
  - Learn **SoC fundamentals**.  
  - Explore how **digital and analog worlds interact**.  
  - Experiment with **real, open-source IP cores**.  

✨ BabySoC isn’t just a circuit — it’s your **first step into the world of chip design**.  

---

👨‍💻 **Author:** Your Name  
🔗 **Tech Stack:** RISC-V | Sky130 | PLL | DAC | Open-Source SoC  
📂 **Category:** Educational / Embedded SoC  
