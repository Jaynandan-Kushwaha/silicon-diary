# 1. Voltage Transfer Characteristics: SPICE Simulations

To explore the behavior of a **CMOS inverter** in SPICE, careful attention to circuit setup and parameters is essential. Think of it as **building a miniature digital world**, where every connection and value matters:

- **Connecting Components:** Ensure that **PMOS, NMOS, Vdd, Vss, Vin, and Vout** are correctly wired, so the inverter performs its switching magic.  
- **Defining Component Values:** Set the stage with accurate parameters — include **transistor sizes, threshold voltages (Vth), and supply voltage (Vdd)** — to make the simulation reflect real-world behavior.  
- **Identifying Nodes:** Map out every electrical node, such as **input (Vin), output (Vout), drain, source, and bulk terminals**, so you know exactly where the action is happening.  
- **Naming Nodes:** Give every node a clear, descriptive name (like **Vout** for the output) to make analysis intuitive and tracking results effortless.  

> By thoughtfully connecting and naming every piece of the circuit, SPICE becomes a powerful microscope to visualize how the inverter switches between logic states.

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20000754.png)
![SCREESHOT](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20000852.png)
### SPICE simulation for CMOS inverter
SPICE Netlist for CMOS Inverter
A **SPICE netlist** for a CMOS inverter includes transistor models, power supply connections, input voltage source, transistor specifications (PMOS and NMOS), and simulation commands (e.g., `.tran` for transient analysis).
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20001827.png)
Same Wn/Ln = Wp/Lp = 1.5. Plot out vs in:
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002106.png)
Now, Wn/Ln = 1.5 and Wp/Lp = 3.75. Plot out vs in:
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002106.png)
![screen](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002117.png)
## **Static Behavior Evaluation: CMOS Inverter Robustness and Switching Threshold (Vm)**  
The **switching threshold (Vm)** is the point where **Vin = Vout**, and both transistors are in saturation (since **Vds = Vgs**). At **Vm**, maximum power is drawn due to large current, and it can be graphically found at the intersection of the **VTC** with the **Vin = Vout** line. The analytical expression for **Vm** is obtained by equating the drain currents of PMOS and NMOS (**IDSn = IDSp**).
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20002354.png)


In the **velocity-saturated** case, the **switching threshold (Vm)** is the point where both **NMOS** and **PMOS** transistors are in saturation, and the drain currents are equal. This occurs when the **VDS** of both devices is less than the saturation voltage, i.e., **VDSAT < (Vm − VT)**. The threshold voltage **Vm** can be derived by equating the drain currents of both transistors, with the device widths and lengths (W/L ratios) playing a key role in determining the point where both transistors conduct equally.
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20004503.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20004736.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005910.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005923.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20005956.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20010341.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day3/Images/Screenshot%202025-10-18%20040029.png)


---

## Velocity Saturation and Switching Threshold (Vm) Analysis

- **Case 1: Velocity Saturation Occurs**  
  - Happens in short-channel devices or high supply voltage.  
  - Switching threshold **Vm** occurs when currents of PMOS and NMOS transistors are equal.  
  - The ratio **r** (PMOS to NMOS strength) influences **Vm**.  
  - For **Vm ≈ VDD/2**, **r ≈ 1**.  
  - **Vm** can be adjusted by changing the PMOS or NMOS width:  
    - Increase PMOS width → shift **Vm** upwards.  
    - Increase NMOS width → shift **Vm** downwards.  

- **Case 2: Velocity Saturation Does Not Occur**  
  - Applies to long-channel devices or low supply voltage.  
  - The switching threshold **Vm** is still affected by **r** but with a simpler formula.  
  - If **r ≈ 1**, **Vm** is near **VDD/2**.

- **PMOS Width Effect on VTC**  
  - Increasing PMOS width shifts **Vm** upwards.  
  - Increasing NMOS width shifts **Vm** downwards.  
  - **Vm** is relatively stable with small variations in transistor ratios.

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
