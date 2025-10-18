# 🚀 Week 4 — NgspiceSky130 CMOS Simulation & Robustness Evaluation  

Welcome to **Week 4 Research!**  
This week, we dive deeper into the world of **transistor-level simulations** using the **Sky130 PDK** and **Ngspice** — the open-source circuit simulator that forms the foundation of analog and mixed-signal VLSI design.  

If Week 3 was about validating timing at the digital level, Week 4 brings us closer to the **device physics** — understanding how NMOS and PMOS transistors actually behave and how their characteristics impact the overall CMOS performance. ⚙️  

---

## 📘 About Week 4  

This module focuses on building a strong understanding of **MOSFET behavior**, **CMOS inverter design**, and **robustness evaluation** under varying process and environmental conditions.  

Through hands-on Ngspice simulations, we will visualize how transistor parameters affect circuit speed, switching points, and noise margins — critical for ensuring reliable operation before tapeout.  

In this week’s journey, you’ll explore:  
- 📉 **Id–Vds characteristics** of NMOS transistors and how different voltages affect current flow  
- ⚡ **Velocity saturation** and its role in determining switching performance  
- 🔄 **Dynamic simulations** to observe real-time signal transitions  
- 🧩 **Noise margin and robustness** evaluation of CMOS inverters  
- 🔋 **Power supply and variation analysis** for device-level stability  

💡 *If Week 3 gave you timing confidence, Week 4 gives you device-level understanding — the physics behind those transitions.*

---

## 🛠️ Prerequisites  

Before getting started, make sure you’re familiar with the following:  
✅ Basic MOSFET theory (linear and saturation regions)  
✅ CMOS inverter design and operation  
✅ Installed **Ngspice** and **Sky130 PDK**  
✅ Basic command-line usage for simulation runs  

**Recommended Tools**  
- 🧮 Ngspice (for circuit simulations)  
- 🧰 SkyWater 130nm PDK  
- 📊 Python (for plotting and data analysis)  
- 🌊 GTKWave (for transient waveform visualization)

💡 *Tip: Keep your earlier BabySoC and post-synthesis simulation setups handy — they’ll help you relate transistor-level effects to digital timing.*

---

## 📂 Research & Lab Roadmap  

This week’s labs are structured to gradually build your understanding — from transistor fundamentals to full CMOS inverter robustness analysis.  

| 🗓️ Day | 🧠 Focus Area | 🔍 Description |
|:--:|:--|:--|
| **Day 1** | **Basics of NMOS Drain current (Id) vs Drain-to-Source Voltage (Vds)** | Plot Id–Vds curves, understand linear and saturation regions, and study the impact of gate voltage (Vgs). |
| **Day 2** | **Velocity Saturation and Basics of CMOS Inverter VTC** | Learn how velocity saturation affects transistor current and generate the CMOS inverter VTC (Voltage Transfer Characteristic). |
| **Day 3** | **CMOS Switching Threshold and Dynamic Simulations** | Perform transient simulations to observe switching speed, threshold voltage, and propagation delay. |
| **Day 4** | **CMOS Noise Margin Robustness Evaluation** | Analyze noise margins (NMH & NML) and evaluate robustness against variations in process and temperature. |
| **Day 5** | **CMOS Power Supply and Device Variation Robustness Evaluation** | Study how supply voltage and device parameter changes affect inverter performance, delay, and power. |

Each day’s experiment includes:  
✔️ Circuit schematic and SPICE netlist setup  
✔️ DC and transient analysis  
✔️ Waveform and plot observations  
✔️ Key performance and robustness measurements  

---

## 🎯 Learning Outcomes  

By the end of Week 4, you will:  
- 🧠 Understand transistor-level physics and CMOS inverter characteristics  
- 🧩 Analyze Id–Vds behavior and VTC plots using Ngspice  
- ⚙️ Simulate switching thresholds and propagation delays  
- 🔋 Evaluate noise margins and power robustness  
- 📈 Correlate transistor parameters with system-level performance  

💡 *This week bridges the gap between device-level physics and digital logic design — a crucial step toward mastering SoC design and tapeout.*  

---

## 🙏 Acknowledgements  

This research module is part of the **RISC-V Reference SoC Tapeout Program**, developed with the support of the **Open-Source VLSI Design Community**.  

We gratefully acknowledge the contributions of educators, developers, and learners who continue to push open silicon design forward.  

👨‍💻 **Kunal Ghosh (VSDI)**  
🛠️ **Tools Used:** Ngspice, Sky130 PDK, GTKWave, Python  
📘 **Community:** VSDI Learners, Open Hardware Developers, and Contributors  

✨ *“Transistor behavior defines logic precision — mastering devices builds the foundation for mastering systems.”* ✨  

**Author:** *jaynandan-kushwaha*  
---


