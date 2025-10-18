
# SPICE Simulation for Lower Nodes and Velocity Saturation Effect

## Objective
- Analyze the behavior of MOSFETs at lower nodes using SPICE simulations.  
- Study **velocity saturation effects** in short-channel devices.  
- Understand **CMOS inverter characteristics** and **MOSFET as a switch**.  

---

## SPICE Simulation for Lower Nodes

- Simulations were carried out for **long-channel and short-channel MOSFETs**.  
- **Long-channel MOSFETs**: Drain current (**Ids**) shows **quadratic dependence** on gate voltage (**Vgs**).  
- **Short-channel MOSFETs**: Ids is **quadratic at low Vgs** and **linear at higher Vgs** due to **velocity saturation**.

---

- Shows how Ids varies with Vgs for both long-channel and short-channel devices.  
- **Long-channel MOSFETs**: Quadratic increase.  
- **Short-channel MOSFETs**: Linear Ids at higher Vgs due to **velocity saturation**.  

![Ids vs Vgs 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20145522.png)  
![Ids vs Vgs 2](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20150029.png)  
![Ids vs Vgs 3](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20151938.png)  
![Ids vs Vgs 4](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20152028.png)  
![Ids vs Vgs 5](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20152240.png)  

**Observation:**  
- Short-channel devices show **early saturation** at higher Vgs.  
- Long-channel devices continue quadratic behavior across the range.

---

- Demonstrates **velocity behavior of carriers** with increasing electric field.  
- **Low electric field:** Linear velocity increase.  
- **High electric field:** Velocity **saturates**, leading to **velocity saturation effects** in short-channel devices.  

![Velocity vs Electric Field 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225306.png)  
![Velocity vs Electric Field 2](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225619.png)  
![Velocity vs Electric Field 3](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20225909.png)  

**Observation:**  
- High field region leads to **Ids saturation** even when Vgs increases.  
- Confirms **velocity saturation effect in short-channel MOSFETs**.

---


- Illustrates **Ids vs Vds** for different Vgs values considering **velocity saturation**.  
- Short-channel devices reach saturation **earlier** than long-channel devices due to **Vdsat effect**.  

![Vdsat Model 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20230441.png)  
![Vdsat Model 2](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231000.png)  
![Vdsat Model 3](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231058.png)  

**Observation:**  
- Saturation occurs when **Vds ≥ Vdsat**.  
- Short-channel MOSFETs show **earlier flattening of Ids**, confirming velocity saturation.

---


- **Linear region (Vds < Vdsat):** Ids increases linearly with Vds.  
- **Saturation region (Vds ≥ Vdsat):** Ids becomes constant.  
- NMOS: Ids depends on **Vgs - Vth**.  
- PMOS: Ids depends on **Vth - Vgs**.  

![Ids vs Vds NMOS 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231106.png)  
![Ids vs Vds PMOS 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231058.png)  
![Ids vs Vds Combined](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20231000.png)  

**Observation:**  
- NMOS and PMOS devices show **expected linear and saturation regions**.  
- Confirms **non-linear resistor behavior** of MOSFETs.

---

- Shows the **switching behavior** of CMOS inverter.  
- **Vout is high** when Vin is low, and **Vout is low** when Vin is high.  
- Transition region defines **switching threshold** where both NMOS and PMOS conduct simultaneously.  

![CMOS VTC 1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20233510.png)  
![CMOS VTC 2](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20233926.png)  
![CMOS VTC 3](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-16%20234037.png)  
**Velocity Saturation Drain Current Model:**  
- **Technology Parameter:** Saturation voltage (**Vdsat**) – the voltage at which carrier velocity saturates, independent of **Vgs** or **Vds**.  
- **Vgt** is minimum → FET is in **saturation region** (both long and short channel).  
- **Vds** is minimum → FET is in **linear region** (both long and short channel).  
- **Vdsat** is minimum → FET velocity **saturates** (**only for short channel**).
 
## **CMOS Voltage Transfer Characteristics (VTC):**  
1. Vout is **high** when Vin is low, and Vout is **low** when Vin is high.  
2. The **transition region** shows a steep drop where both NMOS and PMOS conduct, defining the switching threshold.
#### MOSFET as a switch
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20020006.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20025011.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20031541.png)
**Introduction to Standard MOS Voltage-Current Parameters:**  
In MOS devices, **Rp** (PMOS) and **Rn** (NMOS) act as **non-linear resistors**, where their resistance is a **function of drain current (Ids)**, influenced by gate voltage (Vgs) and drain voltage (Vds).
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day2/Images/Screenshot%202025-10-17%20032017.png)
**PMOS/NMOS Drain Current vs. Drain Voltage:**

1. **Linear Region (Vds < Vdsat):**  
   - Drain current (**Ids**) increases **linearly** with **Vds**.  
   - Device behaves like a **resistor** controlled by Vgs.  

2. **Saturation Region (Vds ≥ Vdsat):**  
   - Drain current (**Ids**) becomes **constant** and independent of Vds.  
   - For **NMOS**, Ids depends on **Vgs - Vth**.  
   - For **PMOS**, Ids depends on **Vth - Vgs**.  
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
