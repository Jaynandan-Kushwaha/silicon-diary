# 🧩 **1. Static Behavior Evaluation: CMOS Inverter Robustness – Power Supply Variation**

## ⚡ Overview
The **CMOS inverter**—the fundamental building block of digital logic—responds sensitively to its **power supply voltage (VDD)**.  
Adjusting VDD doesn’t simply scale voltage levels; it reshapes the inverter’s **switching behavior, noise margins, and reliability**.  
Understanding these shifts is essential for crafting circuits that balance **power efficiency** with **robust logic performance**.

---

## 🧠 SPICE Simulation Approach
To explore this behavior, SPICE simulations were conducted by sweeping **VDD** across multiple values.  
The analysis focused on:

- 🧭 How the **Voltage Transfer Characteristic (VTC)** shifts with varying VDD  
- ⚖️ Tracking the **switching threshold (VM)** — where input and output voltages intersect  
- 📉 Calculating **noise margins** to assess inverter robustness under real-world variations  

This simulation-based study highlights the **power-performance trade-off** inherent in CMOS design — higher VDD means stronger signals but greater energy cost.

---

## 🔍 Key Insights

### 1. **Behavior at Lower VDD**
- The switching threshold (**VM**) drifts closer to the mid-supply level.  
- **Noise margins** decrease, increasing the inverter’s sensitivity to noise.  
- The inverter remains functional even at **0.8V**, roughly half of the nominal 1.8V, though at the edge of reliable operation.  

### 2. **Switching Threshold Proportionality**
- With a constant transistor ratio (*r*), the **switching threshold (VM)** scales proportionally with **VDD**.  

### 3. **Gain Characteristics**
- The **gain** in the transition region increases as **VDD** decreases, making transitions steeper but potentially less tolerant to variations.  

### 4. **Transition Region Width**
- The **transition width** compresses when VDD is reduced, resulting in sharper transitions but narrower stability margins.  

---
   ![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20160424.png)
   ![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20160432.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20163834.png)

### **Limitations of Operating at Low Supply Voltages**

1. **Performance Degradation:**  
   - Lowering the supply voltage reduces energy dissipation but significantly increases gate transition times, negatively affecting performance.

2. **Parameter Sensitivity:**  
   - At low supply voltages, the DC characteristics become highly sensitive to variations in device parameters, such as transistor threshold voltages.

3. **Reduced Signal Swing:**  
   - Scaling VDD reduces signal swing, lowering internal noise (e.g., crosstalk) but increasing sensitivity to external noise sources, which do not scale proportionally.
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20164240.png)
# 🧠 **2. CMOS Inverter Robustness to Device Variations**

## ⚙️ Overview
Even the most precisely designed CMOS circuits face a harsh truth — **real silicon never behaves exactly as simulated**.  
Variations introduced during fabrication and environmental shifts like temperature changes can subtly, yet significantly, alter circuit performance.  
A robust inverter design must gracefully tolerate these deviations while maintaining reliable logic behavior.

---

## 🔍 Key Observations

### 1. **Design vs. Real Operating Conditions**
- CMOS gates are typically designed under **nominal process, voltage, and temperature (PVT)** assumptions.  
- In practice, **fabrication imperfections** and **temperature fluctuations** cause transistors to deviate from their ideal characteristics.  
- Despite these mismatches, well-balanced CMOS inverters maintain predictable logic levels and switching behavior.

---

### 2. **DC Characteristics Stability**
- The **DC transfer curve** of a CMOS inverter remains fairly **stable** against moderate device variations.  
- This inherent robustness allows the gate to operate correctly across a **wide range of environmental and manufacturing conditions**.  
- Such resilience is a hallmark of CMOS technology, making it ideal for both low-power and high-performance designs.

---

### 3. **Sources of Variation**
- A major source of variability arises during the **etching process** in fabrication, which can slightly alter:  
  - Channel dimensions (W/L ratio)  
  - Threshold voltages  
  - Oxide thickness  
- These small shifts in device parameters can influence switching thresholds, but **the inverter’s complementary structure** helps preserve stable logic operation.

---
   ### SOURCES OF ETCHING PROCESS
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20164934.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20164940.png)
### Sources of variation: Oxide Thickness
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165000.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165039.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165151.png)
![Screenshot 2024-12-14 064317](https://github.com/user-attachments/assets/011ff2a9-1203-4501-a5ca-5c8d8f68d536)
![Screenshot 2024-12-14 064325](https://github.com/user-attachments/assets/f78cebab-3c33-45d5-af1f-7b3d1d6276b1)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165629.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165643.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165652.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165819.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%202025-10-18%20165835.png)

# LABS
## Static behavior evaluation: CMOS inverter robustness, Power supply variation
### Smart SPICE simulation for power supply variations

```
*Model Description
.param temp=27


*Including sky130 library files
.lib "sky130_fd_pr/models/sky130.lib.spice" tt


*Netlist Description


XM1 out in vdd vdd sky130_fd_pr__pfet_01v8 w=1 l=0.15
XM2 out in 0 0 sky130_fd_pr__nfet_01v8 w=0.36 l=0.15


Cload out 0 50fF

Vdd vdd 0 1.8V
Vin in 0 1.8V

.control

let powersupply = 1.8
alter Vdd = powersupply
	let voltagesupplyvariation = 0
	dowhile voltagesupplyvariation < 6
	dc Vin 0 1.8 0.01
	let powersupply = powersupply - 0.2
	alter Vdd = powersupply
	let voltagesupplyvariation = voltagesupplyvariation + 1
      end
 
plot dc1.out vs in dc2.out vs in dc3.out vs in dc4.out vs in dc5.out vs in dc6.out vs in xlabel "input voltage(V)" ylabel "output voltage(V)" title "Inveter dc characteristics as a function of supply voltage"

.endc

```

![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2022-09-24.png)
![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2022-10-46.png)


  
```
*Model Description
.param temp=27


*Including sky130 library files
.lib "sky130_fd_pr/models/sky130.lib.spice" tt


*Netlist Description


XM1 out in vdd vdd sky130_fd_pr__pfet_01v8 w=7 l=0.15
XM2 out in 0 0 sky130_fd_pr__nfet_01v8 w=0.42 l=0.15


Cload out 0 50fF

Vdd vdd 0 1.8V
Vin in 0 1.8V

*simulation commands

.op

.dc Vin 0 1.8 0.01

.control
run
setplot dc1
display
.endc

.end

```

![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2022-11-27.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2022-14-20.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2022-14-28.png)


