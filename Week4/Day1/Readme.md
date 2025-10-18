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

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-13%20234135.png)

---

## ⚙️ Introduction to Basic Circuit Element — NMOS Transistor

**NMOS Transistor:**  
An N-type Metal-Oxide-Semiconductor that conducts when a **positive voltage** is applied to its **gate**, allowing current to flow from **drain to source**.

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-13%20235455.png)

### Key Parameters:
- **Threshold Voltage (Vt):** The voltage at which the transistor begins to conduct current.  
- **Strong Inversion:** When the channel forms fully and allows maximum current flow.  
- **Body Effect:** The variation of threshold voltage due to changes in substrate potential.  

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20000529.png)

#### Considering Potential to Body Terminal

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20001859.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20002358.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20002532.png)

- **Threshold Voltage at Vsb = 0:** The threshold when the source-to-body voltage is zero.  
- **Body Effect Coefficient and Fermi Potential:** Parameters defined by the foundry and used in SPICE models to simulate accurate transistor characteristics.  

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20004240.png)

---

## 📊 NMOS Resistive and Saturation Regions of Operation  

**Resistive Region (Linear Mode):**  
Occurs when **Vds** is small and the channel is uniformly formed — the transistor behaves like a resistor.  

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20004825.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20005943.png)

**Key Concepts:**
- **Drift Current:** Caused by the electric field across the device.  
- **Diffusion Current:** Due to carrier concentration differences.  
- **Cox:** Oxide capacitance value provided by the foundry.  



### Drain Current Model (Linear Region)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20230408.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20230740.png)

**SPICE Conclusion for Resistive Region:**  
SPICE sweeps **Vds** for each **Vgs** value to calculate **Id** until **Vds = Vgs - Vt**.  
The resulting **Id–Vds** plots help visualize linear behavior and identify the transition to saturation.

---

### Saturation (Pinch-off) Region  

In the **saturation region**, the transistor channel is pinched off near the drain, and **Id** becomes nearly constant, depending only on **Vgs**.  
This condition is met when **Vds ≥ Vgs - Vt**.  

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20002723.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20003014.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20003228.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20004407.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20004639.png)



---

## 🧩 SPICE Netlist Example or Spice setup

Below is an example SPICE netlist used to simulate NMOS characteristics.

```spice
* Model Description
.param temp=27

* Include Sky130 Library
.lib "sky130_fd_pr/models/sky130.lib.spice" tt

* Netlist Description
XM1 vdd n1 0 0 sky130_fd_pr__nfet_01v8 w=5 l=2
R1 n1 in 55
Vdd vdd 0 1.8V
Vin in 0 1.8V

* Simulation Commands
.op
.dc Vdd 0 1.8 0.1 Vin 0 1.8 0.2

.control
run
display
setplot dc1
.endc
.end
```

## 🔍 Explanation

**Circuit Description:**

M1 vdd n1 0 0 nmos W=1.8u L=1.2u
R1 in n1 55
Vdd vdd 0 2.5
Vin in 0 2.5


- **M1 vdd n1 0 0 nmos W=1.8u L=1.2u** — Defines an **NMOS transistor** with the given **width** and **length**.  
- **R1 in n1 55** — Represents a **55Ω resistor** between nodes `in` and `n1`.  
- **Vdd vdd 0 2.5** — Provides a **2.5V supply voltage**.  
- **Vin in 0 2.5** — Acts as the **input voltage source**.  

This circuit defines all the essential components, parameters, and node connections required for a **SPICE simulation**.
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20111443.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20111756.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20112124.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20112844.png)

---

## 🧪 LABS

### 1️⃣ Introduction to SPICE
**SPICE** (Simulation Program with Integrated Circuit Emphasis) is a powerful software tool used to **simulate and validate circuit performance**.  
It allows designers to analyze **voltage**, **current**, and **power behavior** before the actual hardware is fabricated.

---

### 2️⃣ SPICE with Sky130 Models

To run SPICE simulations using the **Sky130 PDK**, clone the official workshop repository:

```bash
git clone https://github.com/kunalg123/sky130CircuitDesignWorkshop.git
```


**3 Important Files in the Repo**:

1. **`/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice`**  
   This file contains the SPICE model for the **NFET (N-channel MOSFET)** in the Sky130 process at typical (tt) conditions.

2. **`/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.corner.spice`**  
   This file provides the corner model for the **NFET**, used for simulating different process variations.

3. **`/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models/sky130.lib.pm3.spice`**  
   This library file contains all the **SPICE models** for components in the Sky130 process node.

You can download ngspice for Windows from the official source using the following link:

[ngspice Downloads - SourceForge](http://ngspice.sourceforge.net/download.html)

### To plot the waveforms in ngspice
    ngspice day1_nfet_idvds_L2_W5.spice
    plot -vdd#branch

### output 

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2000-51-12.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2000-56-46.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2001-00-05.png)

## 📈 Outcome  

By completing **Day 1**, you’ll gain a solid understanding of how NMOS transistors behave under various voltage conditions and how SPICE simulations bring theory to life.  
You’ll learn how to interpret transistor characteristics, analyze current-voltage behavior, and generate plots that reveal real design insights.  

This forms the **foundation of all transistor-based design work** — the stepping stone to CMOS logic and full-system chip verification.

✨ *Every silicon chip begins at the transistor level — master this, and you master the heart of digital design.* ✨

