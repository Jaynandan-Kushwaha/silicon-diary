# Day 2 – Timing Libraries, Hierarchical vs Flat Synthesis, and Efficient Flop Coding Styles
Author: Jaynandan Kushwaha  
 ---- 

## 📌Introduction
Day 2 takes us deeper into the practical aspects of synthesis and optimization.  
We begin by understanding **timing libraries** and how they shape the translation of RTL into gate-level designs.  
Next, we explore the differences between **hierarchical and flat synthesis**, examining how design structure impacts performance and optimization.  
Finally, we dive into **flop coding styles** and learn how subtle changes in coding can lead to big differences in **timing, power, and area efficiency**.  

This day is all about gaining insights into the “behind-the-scenes” mechanisms that guide synthesis tools and learning how to write RTL that works *with* the tools, not against them.

---

## 📚 Contents

### 🔹 1. Introduction to Timing Libraries
- 🧩 **Lab 1:** Exploring `.lib` Files – Part 1  
- 🧩 **Lab 2:** Diving Deeper into `.lib` Files – Part 2  
- 🧩 **Lab 3:** Advanced View of `.lib` Files – Part 3  

### 🔹 2. Hierarchical vs Flat Synthesis
- 🏗️ **Lab 4:** Understanding Hierarchical vs Flat Synthesis – Part 1  
- 🏗️ **Lab 5:** Comparing Hierarchical vs Flat Approaches – Part 2  

### 🔹 3. Flop Coding Styles & Optimization
- 🔄 **Lecture 1:** Why Flops Matter – Coding Styles (Part 1)  
- 🔄 **Lecture 2:** Flop Coding Styles in Depth (Part 2)  
- ⚙️ **Lab 6:** Flop Synthesis Simulations – Part 1  
- ⚙️ **Lab 7:** Flop Synthesis Simulations – Part 2  
- ✨ **Lecture 3:** Interesting Optimizations – Part 1  
- ✨ **Lecture 4:** Interesting Optimizations – Part 2  
---

## Introductio To Timing Libraries
In lab1, Lab2, Lab3 we understand the sky130 and explore it 
### SKY130 PDK Overview
The **SKY130 PDK** is an open-source Process Design Kit developed around SkyWater’s 130nm CMOS technology.  
It serves as the foundation for digital design, offering a collection of **standard cell libraries, device models, and timing information**.  
These libraries provide critical data such as **propagation delay, power consumption, capacitance, and process variation details**, which are required by synthesis and simulation tools to accurately represent real hardware behavior.  

In short, without timing libraries, the synthesis tool would not know how fast a gate is, how much power it consumes, or how it behaves under different voltage and temperature conditions.  

---

### Decoding `tt_025C_1v80` in SKY130 PDK
A common naming format you’ll see in library files is something like `tt_025C_1v80`. Let’s break it down:  

- **tt** → “Typical-Typical” process corner (standard transistor behavior).  
- **025C** → Temperature = 25°C, representing nominal operating temperature.  
- **1v80** → Core voltage of 1.8V, which is the nominal supply voltage for standard cells.  

This label tells us the **process, voltage, and temperature (PVT) conditions** under which the library data was characterized.  

---

### Why Different PVT Corners Matter
Real silicon doesn’t always behave the same. Manufacturing variations, supply fluctuations, and temperature changes can alter timing.  
That’s why libraries include multiple PVT corners, such as:  
- **ss_100C_1v60** → Slow process, 100°C, 1.6V (worst-case delay, high temp, low voltage).  
- **ff_n40C_1v95** → Fast process, -40°C, 1.95V (best-case delay, low temp, high voltage).  

By using different libraries, designers can **test robustness**, ensuring the chip works reliably across all real-world conditions.  

<div align="center">
  <img src="Images/Lib-file.png" alt="Lib-file.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture1.png" alt="Lecture1.png" width="70%">
</div>
In this lecture they explain about Process Voltage and temprature how on these terms are important in silicon design work and this PVT tell how fast and slow our silicon will work 
---

In part 2 and 3 we discuss about verious information stored in .lib file technology used, volatge power leakage in cells and many more thing specially area how it differs on increasing cells in combinational ckt and about power leakage 

---

## Hierarchical vs Flat Synthesis

### Hierarchical Synthesis

**Overview:**  
Hierarchical synthesis is a design strategy where each module in the RTL is **synthesized individually**, maintaining the original hierarchy rather than flattening the design into a single block.

**Workflow:**  
Tools like **Yosys** handle each module separately. Using commands like `hierarchy`, the tool **maps out the structure of the design**, ensuring that module boundaries are preserved throughout the synthesis process.

**Benefits:**  
- **Speeds up synthesis** for large-scale designs by processing modules independently.  
- **Simplifies debugging**, as issues can be traced within individual modules.  
- **Supports modular design**, making it easier to integrate with other tools or IP blocks.

**Drawbacks:**  
- **Cross-module optimizations are limited**, which might reduce overall performance.  
- **Reports may require extra setup**, since hierarchical structures are not always captured automatically.

#### Here is one exapmle we synthesis multipul module.v file and understand the synthesisation behind the tool




