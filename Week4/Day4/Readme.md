# ⚡ **Static Behavior Evaluation: CMOS Inverter Robustness and Noise Margin**

### 🔹 Understanding Noise Margin
In digital circuits, **noise is inevitable** — small voltage spikes or fluctuations can occur due to **interference, crosstalk, or power supply variations**.  
A CMOS inverter’s **noise margin** defines its ability to **tolerate these disturbances** without misinterpreting a logic level.  

In simple terms, it acts as a **safety buffer**:

- Ensures a **logic '1' remains '1'** and a **logic '0' remains '0'** even in the presence of noise.  
- If the noise amplitude is smaller than the margin, the inverter naturally **filters it out**, allowing clean signals to propagate through multiple logic stages without errors.

---

### 🔹 Why Noise Margin Matters
Noise margin is critical for **robust and reliable digital operation**, especially in circuits with **cascaded gates**:

- **Logic High (≈ VDD):** Small voltage fluctuations must still be recognized as **logic 1**.  
- **Logic Low (≈ 0 V):** Small voltage fluctuations must still be recognized as **logic 0**.  

> Ensuring adequate noise margins allows CMOS circuits to maintain **signal integrity**, prevent **logic corruption**, and operate reliably in complex digital systems.

---


### 🔹 Visualizing Noise Margin with VTC

Consider **two CMOS inverters connected back-to-back**. The **Voltage Transfer Characteristic (VTC)** of the first inverter determines the **input voltage range** over which the second inverter correctly interprets signals.  

- **Ideal VTC:** Exhibits an **extremely sharp transition** from low to high output, providing **maximum noise immunity**.  
- **Piece-wise Linear VTC:** A simplified approximation highlighting **critical switching points**, useful for analytical analysis.  
- **Realistic VTC:** Derived from **simulation or real measurements**, showing **gradual transitions** and **non-ideal effects**, reflecting real-world behavior.

> Observing the VTC visually allows designers to **quantify noise margins** and ensure **robust operation** in cascaded CMOS logic circuits.

---
 

![Noise Margin Illustration](https://github.com/user-attachments/assets/a33b8aeb-ae0d-43d9-ae48-7def565b38a7)

---

### Key Points: VIL and VIH
The **VTC curve** contains critical points, **VIL** (Input Low Voltage) and **VIH** (Input High Voltage), which define the inverter’s **noise tolerance boundaries**:

- **Definition:**  
  - **VIL** and **VIH** are the input voltages where the slope of the VTC equals **-1**, meaning the inverter’s gain magnitude is unity.  
- **Logic Interpretation:**  
  - **Vin ≤ VIL** → Output clearly recognized as **logic 0**.  
  - **Vin ≥ VIH** → Output clearly recognized as **logic 1**.  

> These points effectively separate the **safe regions** from the **undefined zone**, where small input variations can cause output uncertainty.

---

### **Noise Margin: VIL and VIH Points**

- **Definition:**  
  - **VIL** and **VIH** are operational points where the slope of the voltage transfer curve (VTC) is **-1**.  
  - These points correspond to the gain of the inverter being equal to **-1**.  

- **Logic Recognition:**  
  - Input voltage **0 to VIL** → Recognized as **Logic 0**.  
  - Input voltage **VIH to VDD** → Recognized as **Logic 1**.
   ### **Noise Margins in CMOS Logic Gates**

1. **Conditions for Proper Operation:**  
   - The following conditions must hold for a logic gate to function correctly in the presence of noise:  
     ```
     VOL_MAX < VIL_MAX  
     VOH_MIN > VIH_MIN  
     ```  

2. **Behavior in Different Input Ranges:**  
   - **For Vin ≤ VIL**:  
     The inverter gain magnitude is less than unity, resulting in minimal output change for a given input change.  
   - **For Vin ≥ VIH**:  
     The gain magnitude is also less than unity, leading to minimal output change.  
   - **For VIL < Vin < VIH**:  
     The gain magnitude exceeds unity, causing significant output changes. This range is called the **undefined region** because noise signals pushing Vin into this range may introduce errors.  

3. **Noise Margin Equations:**  
   - **Low-Level Noise Margin (NML):**  
     ```
     NML = VIL_MAX - VOL_MAX  
     ```  
   - **High-Level Noise Margin (NMH):**  
     ```
     NMH = VOH_MIN - VIH_MIN  
     ```  
   - **Overall Noise Margin (NM):**  
     ```
     NM = Min(NML, NMH)  
     ```  

These noise margins define the tolerance of a circuit to noise without compromising its logical operation.
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20152738.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20153807.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20154329.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20154336.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20154949.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155008.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155055.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155104.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155111.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155127.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155155.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%202025-10-18%20155206.png)

# LABS
##  Static behavior evaluation: CMOS inverter robustness, Noise margin
##### Noise Margin - sky130 Inverter (Wp/Lp=1u/0.15u, Wn/Ln=0.36u/0.15u)
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

 ![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%20from%202025-10-18%2021-25-36.png)
 ![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day4/Images/Screenshot%20from%202025-10-18%2021-26-24.png)


