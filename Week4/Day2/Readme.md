# ⚡ **. SPICE Simulation for Lower Nodes and Velocity Saturation Effect**

## 🎯 Objective
This experiment dives into the **scaling behavior of MOSFETs** as technology nodes shrink — exploring how **short-channel effects** reshape current flow and device performance.  
Through detailed **SPICE simulations**, we analyze:

- The contrast between **long-channel and short-channel MOSFETs**  
- The emergence of **velocity saturation** in modern nanoscale devices  
- The resulting impact on **CMOS inverter behavior** and **MOSFET switching efficiency**

---

## 🧩 SPICE Simulation for Lower Nodes

As transistors scale down to nanometer dimensions, the classic long-channel equations begin to **lose accuracy**.  
SPICE simulations reveal how **carrier transport physics** evolves between the two regimes:

### 🧠 **Long-Channel MOSFETs**
- The drain current (**Ids**) exhibits a **quadratic dependence** on gate voltage (**Vgs**).  
- Follows the textbook equation:  
  \[
  I_{ds} \propto (V_{gs} - V_{th})^2
  \]
- Carriers accelerate freely through the channel — **no velocity saturation** occurs.

---

### ⚙️ **Short-Channel MOSFETs**
- Initially, **Ids** increases quadratically with **Vgs**, similar to long-channel behavior.  
- As **Vgs** rises, **carrier velocity approaches a physical limit** — the **saturation velocity (v_sat)**.  
- Beyond this point, **Ids grows linearly with Vgs**, signaling **velocity saturation dominance**.  
- This effect becomes stronger as device dimensions shrink, limiting drive current and affecting delay performance.

---

## 📊 **Observation Summary**

| Parameter | Long-Channel Device | Short-Channel Device |
|------------|--------------------|----------------------|
| Current–Voltage Relation | Quadratic | Linear (at high Vgs) |
| Dominant Effect | Carrier Mobility | Velocity Saturation |
| Channel Behavior | Gradual Channel Approximation | High Electric Field Limitation |
| Impact on Circuits | Predictable, high gain | Reduced gain, faster switching |

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20145522.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20150029.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20151938.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20152028.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20152240.png)  

## 🔬 **Observation: Velocity Saturation Phenomenon**

### ⚡ **Device Behavior Comparison**
- **Short-channel MOSFETs** exhibit **early current saturation** as **Vgs** increases.  
  - Carriers quickly reach their **maximum drift velocity**, limiting further current growth.  
- **Long-channel MOSFETs**, on the other hand, maintain a **quadratic Ids–Vgs relationship** across the voltage range.  
  - The carriers accelerate smoothly without hitting the velocity ceiling, following the classic MOSFET model.

---

### 🌪️ **Carrier Velocity vs. Electric Field**
SPICE simulations further illustrate how **carrier velocity** evolves with the **applied electric field (E-field):**

| Electric Field Region | Carrier Behavior | Physical Effect |
|------------------------|------------------|-----------------|
| **Low E-field** | Carrier velocity increases **linearly** with E-field | Drift velocity proportional to E |
| **High E-field** | Velocity reaches a **saturation limit** | **Velocity saturation** dominates |

---

### 💡 **Insight**
As the **electric field strength** rises in **short-channel devices**, carriers can no longer accelerate indefinitely — their velocity **flattens out**, leading to **current saturation**.  
This phenomenon marks the **transition from long-channel quadratic behavior** to **short-channel linear characteristics**, a defining trait of modern nanometer-scale transistors.

---

![Vimsge](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225306.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225619.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225909.png)  

## 📈 **Observation: Ids–Vds Characteristics under Velocity Saturation**

### ⚡ **High-Field Behavior**
- In the **high electric field region**, the drain current (**Ids**) enters **saturation** even as **Vgs** continues to increase.  
- This behavior directly **confirms the presence of velocity saturation** in **short-channel MOSFETs**, where carrier drift velocity reaches its physical maximum limit.  

---

### 🧩 **Ids vs. Vds Analysis**
SPICE simulations depicting **Ids–Vds** characteristics for various **Vgs** levels reveal clear distinctions between device scales:

| Device Type | Ids–Vds Behavior | Dominant Effect |
|--------------|------------------|-----------------|
| **Long-Channel MOSFET** | Smooth quadratic rise before saturation | Gradual Channel Approximation |
| **Short-Channel MOSFET** | Rapid early saturation at lower Vds | **Velocity Saturation (Vdsat)** |

---

### 🌪️ **Insight**
Short-channel devices **reach current saturation earlier** because their **Vdsat (saturation voltage)** is significantly lower.  
As carriers hit their **velocity saturation limit**, further increases in **Vds** produce negligible current growth.  
This phenomenon defines the **performance ceiling** in nanoscale transistors — balancing speed, power, and reliability in modern CMOS design.

---

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20230441.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231000.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231058.png)  

## 🔍 **Observation: Ids Behavior in Linear and Saturation Regions**

### ⚡ **Saturation Condition**
- Current **saturation occurs when Vds ≥ Vdsat**, where the channel near the drain is fully pinched off.  
- **Short-channel MOSFETs** exhibit **earlier flattening of Ids**, a clear signature of **velocity saturation** dominating carrier transport.  

---

### 📊 **Region-Wise Behavior**

| Region | Condition | Current Behavior | Dominant Dependence |
|---------|------------|------------------|----------------------|
| **Linear Region** | Vds < Vdsat | **Ids increases linearly** with Vds | Channel behaves resistively |
| **Saturation Region** | Vds ≥ Vdsat | **Ids becomes constant** | Limited by carrier velocity saturation |
| **NMOS** | — | Ids ∝ (Vgs − Vth) | Controlled by gate overdrive |
| **PMOS** | — | Ids ∝ (Vth − Vgs) | Complementary gate control |

---

### 💡 **Insight**
In modern **short-channel devices**, velocity saturation defines the transition from the **linear to the saturation region**.  
As soon as **Vds exceeds Vdsat**, carriers at the drain end reach their **maximum drift velocity**, causing **Ids to plateau**.  
This behavior highlights how **scaling limits** shape transistor dynamics — a crucial concept in understanding **deep submicron MOSFET operation**.

---


![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231106.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231058.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231000.png)  

## ⚙️ **Observation: MOSFET Characteristics and CMOS Inverter Switching**

### 🔋 **MOSFET Behavior**
- Both **NMOS** and **PMOS** devices exhibit the **expected linear and saturation regions** in their I–V characteristics.  
- This confirms the **non-linear resistor nature** of MOSFETs — acting as voltage-controlled current sources rather than simple resistors.  
- The distinction between **linear (ohmic)** and **saturation (constant-current)** operation forms the foundation of transistor-based circuit design.

---

### 🔀 **CMOS Inverter Switching Behavior**
- The **CMOS inverter** demonstrates its classic **complementary switching action**:  
  - **Vout is HIGH** when **Vin is LOW** (PMOS conducts, NMOS off).  
  - **Vout is LOW** when **Vin is HIGH** (NMOS conducts, PMOS off).  
- The **transition region** marks the **switching threshold (VM)** — the point where **both NMOS and PMOS** are partially ON and conduct simultaneously.  

---

### 💡 **Insight**
The combined I–V characteristics of NMOS and PMOS devices define the **Voltage Transfer Characteristic (VTC)** of the inverter.  
This elegant push–pull mechanism ensures **low static power consumption**, **sharp transitions**, and **robust digital logic behavior**, making CMOS the **cornerstone of modern digital electronics**.

---
  

![Images](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20233510.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20233926.png)  
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20234037.png)  
## 🚀 **Velocity Saturation Drain Current Model**

### ⚙️ **Overview**
The **Velocity Saturation Drain Current Model** refines the traditional MOSFET I–V equations to capture **short-channel effects** that dominate in deep-submicron technologies.  
As the **electric field** along the channel intensifies, carriers reach their **maximum drift velocity**, limiting further increase in drain current (**Ids**).

---

### 📐 **Key Technology Parameter**
- **Saturation Voltage (Vdsat):**  
  The voltage at which **carrier velocity saturates**, becoming **independent of Vgs or Vds**.  
  It defines the **boundary** between linear and saturation regions in short-channel devices.

---

### 🔍 **Operating Regions and Conditions**

| Parameter | Device Condition | Region | Description |
|------------|------------------|---------|-------------|
| **Vgt** (Vgs − Vth) → minimum | FET operates in **saturation** | Applies to both **long** and **short channel** devices |
| **Vds** → minimum | FET operates in **linear region** | Applies to both **long** and **short channel** devices |
| **Vdsat** → minimum | **Velocity saturation** occurs | **Only in short-channel** devices |

---

### 💡 **Insight**
At nanoscale dimensions, **Vdsat** becomes a crucial factor in defining MOSFET performance.  
Once carriers reach their **velocity saturation limit**, further increases in **Vds** no longer boost current — resulting in **linear Ids–Vgs dependence** and marking a clear shift from traditional **long-channel behavior**.  
This model forms the basis for accurately predicting device performance in **advanced CMOS technologies**.

---

## ⚡ **CMOS Voltage Transfer Characteristics (VTC)**

### 🔀 **Inverter Behavior**
1. The **CMOS inverter** follows its fundamental switching rule:  
   - **Vout is HIGH** when **Vin is LOW** → PMOS conducts, NMOS is off.  
   - **Vout is LOW** when **Vin is HIGH** → NMOS conducts, PMOS is off.  

2. The **transition region** represents the critical **switching threshold**, where **both NMOS and PMOS** partially conduct.  
   - This region produces a **steep drop in Vout**, showcasing the inverter’s **sharp switching response**.  
   - The point of symmetry in this curve defines the **switching threshold voltage (VM)**.

---

### 💡 **Insight**
The **Voltage Transfer Characteristic (VTC)** elegantly illustrates the inverter’s ability to translate analog input variations into **precise digital logic levels**.  
Its **steep transition slope** ensures **strong noise immunity**, **fast switching**, and **minimal static power consumption** — the hallmarks of efficient CMOS logic design.

---

#### MOSFET as a switch
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20020006.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20025011.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20031541.png)
**Introduction to Standard MOS Voltage-Current Parameters:**  
In MOS devices, **Rp** (PMOS) and **Rn** (NMOS) act as **non-linear resistors**, where their resistance is a **function of drain current (Ids)**, influenced by gate voltage (Vgs) and drain voltage (Vds).
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20032017.png)
## 📊 **PMOS/NMOS Drain Current vs. Drain Voltage**

### ⚡ **Linear Region (Vds < Vdsat)**
- The drain current (**Ids**) increases **linearly** with **Vds**.  
- The MOSFET behaves like a **voltage-controlled resistor**, with **Vgs** governing the slope.  
- This region is often called the **ohmic region**, where the channel is fully formed and carriers accelerate proportionally to the applied drain voltage.

---

### ⚡ **Saturation Region (Vds ≥ Vdsat)**
- The drain current (**Ids**) **flattens** and becomes nearly **independent of Vds**.  
- **NMOS:** Ids ∝ (**Vgs − Vth**) — current controlled by gate overdrive.  
- **PMOS:** Ids ∝ (**Vth − Vgs**) — complementary behavior to NMOS.  
- Saturation occurs because the **channel near the drain is pinched off**, or in short-channel devices, because **carrier velocity saturates**.  

---

### 💡 **Insight**
The **linear and saturation regions** define the fundamental operating modes of MOSFETs.  
Understanding these regions is crucial for **analog circuit design**, **switching applications**, and **predicting CMOS inverter behavior**, ensuring devices operate efficiently across voltage ranges.

---

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20161854.png)
 #### Step1. Convert **PMOS gate-source voltage** to **Vin**.  
 Replace internal node voltages with **Vin**, **Vdd**, **Vss**, and **Vout**.  
 Simulate and plot the **VTC** by varying **Vin** and analyzing **Vout**.
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20162320.png)
**Step 2 & Step 3:**  
- Convert **PMOS** and **NMOS drain-source voltages** to **Vout**.  
- Relate the drain-source voltages of both devices to the output voltage (**Vout**) by considering their respective operating regions (linear or saturation).
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20162543.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20162556.png)
**Step 4:**  
- **Merge the PMOS and NMOS load curves** by combining their drain current (Ids) characteristics with respect to **Vout**.  
- **Plot the Voltage Transfer Characteristic (VTC)** by mapping **Vout** against **Vin**, showing the transition from low to high output voltage.
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-18%20000754.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-18%20195231.png)

# LABS
## SPICE simulation for lower nodes and velocity saturation effect
#### Sky130 Id-Vgs
##### EXAMPLE 1
      *Model Description
      .param temp=27

      *Including sky130 library files
      .lib "sky130_fd_pr/models/sky130.lib.spice" tt

      *Netlist Description
       XM1 Vdd n1 0 0 sky130_fd_pr__nfet_01v8 w=0.39 l=0.15
       R1 n1 in 55
       Vdd vdd 0 1.8V
       Vin in 0 1.8V

      *simulation commands
       .op
       .dc Vdd 0 1.8 0.1 Vin 0 1.8 0.2

       .control

       run
       display
       setplot dc1
       .endc
       .end

#### The plot of Ids vs Vds over constant Vgs:
![Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%20from%202025-10-18%2020-30-24.png)
![Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%20from%202025-10-18%2020-30-46.png)

##### EXAMPLE 2
      *Model Description
       .param temp=27

       *Including sky130 library files
       .lib "sky130_fd_pr/models/sky130.lib.spice" tt

       *Netlist Description
        XM1 Vdd n1 0 0 sky130_fd_pr__nfet_01v8 w=0.39 l=0.15
        R1 n1 in 55
        Vdd vdd 0 1.8V
        Vin in 0 1.8V

        *simulation commands
         .op
        .dc Vin 0 1.8 0.1 

        .control

         run
         display
         setplot dc1
         .endc
         .end
####  The plot of Ids vs Vgs over constant Vds:
![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%20from%202025-10-18%2020-29-39.png)
![ Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%20from%202025-10-18%2020-30-06.png)

---

## 💡 **Conclusion**
The SPICE analysis unveils a **fundamental truth of device scaling** — as MOSFETs shrink, **velocity saturation becomes the new ceiling** for current flow.  
While this limits the maximum drive strength, it also leads to **faster transitions** and **compact, power-efficient designs**.  
Understanding this trade-off is key to mastering **modern CMOS circuit design** at advanced technology nodes.

---
