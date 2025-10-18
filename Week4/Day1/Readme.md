# ⚡ Day 1 — Basics of NMOS Drain Current (Id) vs Drain-to-Source Voltage (Vds)

Welcome to **Day 1** of the NgspiceSky130 module!  
This day marks the starting point of your journey into **transistor-level circuit design and simulation**.  
We begin by understanding the core device that powers all CMOS circuits — the **NMOS transistor** — and explore how its electrical behavior changes with different biasing conditions using **SPICE simulations**.

---

## 🎯 What You’ll Learn

Today’s session is divided into three major parts that together build the foundation for CMOS-level analysis:

### 🧩 1. Introduction to Circuit Design and SPICE Simulations  

We start with the basics — understanding why we need SPICE simulations and how they help in predicting real-world circuit performance before fabrication.  
You’ll also revisit fundamental elements of circuit design, focusing on **NMOS operation**, **threshold voltage**, and how **substrate bias** affects transistor behavior.  

Topics covered:
- Why SPICE simulations are essential  
- Basic elements of circuit design — NMOS  
- Strong inversion and threshold voltage  
- Threshold voltage with positive substrate potential  

---

### ⚙️ 2. NMOS Resistive and Saturation Regions of Operation  

Once we understand the physical structure and basic theory, we move into the **operating regions** of an NMOS transistor.  
Here, we study how the **drain current (Id)** changes with **drain-to-source voltage (Vds)** and **gate-to-source voltage (Vgs)**.  

This section gives you a clear view of how transistors transition from **linear (resistive)** to **saturation** mode — the key to designing amplifiers, switches, and logic gates.

Key concepts:
- Resistive region of operation (small Vds)  
- Drift current theory  
- Drain current model for linear region  
- Pinch-off condition and channel formation  
- Drain current model for saturation region  
- SPICE simulation results for both regions  

By the end of this section, you’ll be able to **plot Id–Vds characteristics** and identify the operating region of a MOSFET from its graph — an essential skill for analog and digital designers alike.

---

### 🧠 3. Introduction to SPICE  

In this final segment, you’ll learn how to bring theory to life through simulation.  
This includes creating your first **SPICE netlist**, defining transistor parameters, and running basic DC analysis using the **Sky130 PDK models**.  

You’ll also understand how each section of the SPICE file works — from defining circuit nodes to specifying transistor models and simulation commands.

You’ll perform:  
- Basic SPICE setup and syntax  
- Writing NMOS circuits using Sky130 models  
- Defining technology parameters (W/L, model names)  
- Running first SPICE simulations  
- Observing Id–Vds behavior through waveform outputs  

---

## 💡 Why Do We Need SPICE Simulations?

SPICE simulations help us **verify a circuit’s behavior** before it’s ever built in hardware.  
In circuit design, logic gates such as **NAND**, **NOR**, and **NOT** are constructed using combinations of **NMOS** and **PMOS** transistors.  

For example, in an **inverter** circuit:
- The **drains** of the PMOS (pull-up) and NMOS (pull-down) connect together at the **output node**, which typically drives a capacitive load.  
- The **gates** of both transistors share the same **input signal**.  
- The **source** of the PMOS is tied to **VDD**, while the NMOS source connects to **GND**.  

This configuration ensures one transistor is ON while the other is OFF, producing a clear logical inversion at the output.  

SPICE simulations allow us to confirm that the circuit operates as expected — verifying **functionality**, **timing**, and **power behavior** before moving to fabrication.  

---

## 🔍 SPICE Simulation  

SPICE acts like a **virtual test lab** for electronic design.  
It enables us to test, analyze, and optimize circuits by simulating how voltages and currents behave over time.  

For example, when we provide an **input waveform** to a circuit, SPICE generates the **output waveform**, allowing us to observe how the circuit responds dynamically.  
From these results, we can measure critical parameters such as:
- **Propagation delay**  
- **Rise and fall times**  
- **Current flow** and **power usage**

By adjusting transistor parameters like **width (W)** and **length (L)**, designers can control the **drain current (Id)**, which directly affects delay and circuit speed.  
This makes SPICE an essential tool for **fine-tuning performance** and ensuring the design behaves efficiently under real-world conditions.

💡 *In short, SPICE bridges the gap between mathematical models and actual hardware — giving us confidence before we ever power on a chip.*

---

## 📈 Outcome  

By completing **Day 1**, you’ll gain a solid understanding of how NMOS transistors behave under various voltage conditions and how SPICE simulations bring theory to life.  
You’ll learn how to interpret transistor characteristics, analyze current-voltage behavior, and generate plots that reveal real design insights.  

This forms the **foundation of all transistor-based design work** — the stepping stone to CMOS logic and full-system chip verification.

✨ *Every silicon chip begins at the transistor level — master this, and you master the heart of digital design.* ✨

