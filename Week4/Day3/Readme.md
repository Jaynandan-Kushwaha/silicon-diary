# Voltage Transfer Characteristics: SPICE Simulations

### 🔧 **Setting Up the CMOS Inverter in SPICE**
Simulating a **CMOS inverter** in SPICE is like constructing a **tiny digital ecosystem** — every component, connection, and value must be precise to reveal true circuit behavior.

- **Connecting Components:**  
  Ensure **PMOS, NMOS, Vdd, Vss, Vin, and Vout** are correctly wired. Each transistor must be properly oriented to capture the complementary action of the inverter.

- **Defining Component Values:**  
  Accurately set **transistor dimensions (W/L), threshold voltages (Vth), and supply voltage (Vdd)**. These parameters determine switching thresholds, gain, and overall inverter performance.

- **Identifying Nodes:**  
  Label every electrical node — **input (Vin), output (Vout), drain, source, and bulk terminals** — to track voltage and current flow with precision.

- **Naming Nodes:**  
  Use **descriptive node names** (e.g., `Vout` for the output) for clarity, making it easier to analyze simulation results and interpret the Voltage Transfer Characteristic (VTC).

---

> By carefully connecting, labeling, and parameterizing the inverter in SPICE, you turn the simulator into a **microscope** that reveals how logic levels transition, how noise margins behave, and how CMOS truly operates.

---


![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20000754.png)
![SCREESHOT](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20000852.png)
### SPICE Simulation for CMOS Inverter

#### 📝 SPICE Netlist Overview
A **SPICE netlist** is the blueprint that tells the simulator **how to build and analyze a CMOS inverter**. It includes:

- **Transistor Models:** Define the electrical characteristics of **NMOS and PMOS devices**, including threshold voltage, mobility, and channel length/width.  
- **Power Supply Connections:** Specify **Vdd** and **Vss** nodes to power the inverter correctly.  
- **Input Voltage Source:** Set up **Vin** to drive the inverter through various voltage levels for simulation.  
- **Transistor Specifications:** Include **W/L ratios, Vth, and model parameters** for each device to accurately reflect real silicon behavior.  
- **Simulation Commands:** Commands like `.tran` for transient analysis, `.dc` for DC sweep, or `.ac` for frequency response allow detailed exploration of inverter behavior.
- ## ⚡ **Static Behavior Evaluation: CMOS Inverter Robustness and Switching Threshold (Vm)**

### 🔀 **Understanding the Switching Threshold**
The **switching threshold (Vm)** is the critical input voltage at which:

- **Vin = Vout**  
- Both **NMOS and PMOS transistors are in saturation** (since Vds ≈ Vgs)  
- Maximum current flows, leading to **peak dynamic power consumption**

Graphically, **Vm** can be found at the intersection of the **Voltage Transfer Characteristic (VTC)** with the **Vin = Vout** line.  

Analytically, **Vm** is determined by **equating the drain currents** of NMOS and PMOS:

\[
I_{DSn} = I_{DSp}
\]

This ensures that both devices conduct equally at the transition point.

---

### 🌪️ **Velocity-Saturated Case**
When **velocity saturation** dominates in short-channel devices:

- **Vm** still occurs where both transistors are in saturation  
- The **drain currents are equal**, but now the **VDS of each transistor** satisfies:  

\[
V_{DS} < V_{DSAT} < (V_m - V_T)
\]

- The **W/L ratios** of NMOS and PMOS play a critical role in determining the exact switching point.  

> In essence, the switching threshold **Vm** reflects the delicate balance of currents in the inverter and is influenced by **device dimensions, velocity saturation, and transistor sizing**.  

![CMOS Inverter VTC](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002354.png)

---

> The SPICE netlist transforms your conceptual CMOS inverter into a **virtual experiment**, letting you observe switching, delay, noise margins, and voltage transfer characteristics with precision.

---

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20001827.png)
Same Wn/Ln = Wp/Lp = 1.5. Plot out vs in:
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002106.png)
Now, Wn/Ln = 1.5 and Wp/Lp = 3.75. Plot out vs in:
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002106.png)
![screen](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002117.png)

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20004503.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20004736.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005910.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005923.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005956.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20010341.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20040029.png)


---

## ⚡ **Velocity Saturation and Switching Threshold (Vm) Analysis**

### 🔹 **Case 1: Velocity Saturation Occurs**
- Typically happens in **short-channel devices** or at **high supply voltage**.  
- The **switching threshold (Vm)** is defined where **PMOS and NMOS drain currents are equal**.  
- The **strength ratio (r = PMOS/NMOS)** directly influences **Vm**:  
  - If **r ≈ 1**, then **Vm ≈ VDD/2**.  
- **Adjusting transistor widths shifts Vm**:  
  - **Increase PMOS width → Vm shifts upward**  
  - **Increase NMOS width → Vm shifts downward**  

---

### 🔹 **Case 2: Velocity Saturation Does Not Occur**
- Applies to **long-channel devices** or **low supply voltage**.  
- **Vm** is still determined by the PMOS/NMOS strength ratio (**r**), but the relationship is simpler.  
- For **r ≈ 1**, **Vm** remains near **VDD/2**.  

---

### 🔹 **PMOS/NMOS Width Effect on VTC**
- **Increasing PMOS width:** shifts **Vm upward**, making the inverter switch at a higher input voltage.  
- **Increasing NMOS width:** shifts **Vm downward**, lowering the switching point.  
- **Vm is relatively stable** for small variations in transistor ratios, demonstrating **robust inverter design**.

---

> Understanding how **velocity saturation** and **transistor sizing** affect the **switching threshold** is crucial for designing CMOS inverters with **balanced noise margins, fast transitions, and predictable logic behavior**.

---


![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20040048.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20104759.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20110415.png)
### Applications of CMOS inverter in clock network and STA
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20204006.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20204022.png)
# LABS
## 1. Voltage transfer characteristics: SPICE simulations
#### Sky130 SPICE simulation for CMOS - VTC
     *Model Description
     .param temp=27

      *Including sky130 library files
      .lib "sky130_fd_pr/models/sky130.lib.spice" tt

      *Netlist Description
       XM1 out in vdd vdd sky130_fd_pr__pfet_01v8 w=0.84 l=0.15
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
        
![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%20from%202025-10-18%2020-55-01.png)
![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%20from%202025-10-18%2020-55-01.png)

- **Switching Threshold (VM):**  
  The input voltage (**Vin**) at which the output voltage (**Vout**) equals the input voltage.  
  - It is the intersection point on the Voltage Transfer Curve (VTC).  
  - Also referred to as the **midpoint voltage** of the CMOS inverter.

  ### Sky130 SPICE simulation for CMOS - Transient Analysis
      *Model Description
       .param temp=27

      *Including sky130 library files
        .lib "sky130_fd_pr/models/sky130.lib.spice" tt

        *Netlist Description
         XM1 out in vdd vdd sky130_fd_pr__pfet_01v8 w=0.84 l=0.15
         XM2 out in 0 0 sky130_fd_pr__nfet_01v8 w=0.36 l=0.15
         Cload out 0 50fF
         Vdd vdd 0 1.8V
         Vin in 0 PULSE(0V 1.8V 0 0.1ns 0.1ns 2ns 4ns)

         *simulation commands
         .tran 1n 10n
         .control
          run
          .endc
          .end
  
  ![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%20from%202025-10-18%2000-36-51.png)
  ![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%20from%202025-10-18%2000-37-57.png)
  ![Image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%20from%202025-10-18%2000-39-16.png)
- **Propagation Delay:**  
  The time difference (measured at 50% of input-output transition) between the input signal change and the corresponding output signal switch in a logic gate (e.g., inverter).

  ##  Conclusion

The SPICE simulations and analysis demonstrate:

- **CMOS inverters** are resilient to supply and process variations.  
- **Velocity saturation** in short-channel devices limits current but enables faster transitions.  
- **Switching threshold (Vm)** can be tuned by adjusting PMOS/NMOS widths and ratios.  
- **VTC** and I–V characteristics reveal the delicate balance between **device physics, sizing, and voltage**, ensuring robust, low-power digital circuits.  

> Overall, this study emphasizes how **SPICE simulations** provide deep insight into CMOS behavior, guiding design choices for **modern, high-performance, and low-power digital logic**.

---
