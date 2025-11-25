# Day0

# /mnt/data/silicon_repo/silicon-diary-main/Day0/README.md

# 🚀 Day 0 – VSD Program Kickoff & Toolchain Setup  

<div align="center">

![Program](https://img.shields.io/badge/VSD-Hardware%20Design-blue?style=for-the-badge&logo=semanticscholar)  
![Track](https://img.shields.io/badge/Track-RTL2GDS-orange?style=for-the-badge)  
![Progress](https://img.shields.io/badge/Progress-Day%200-success?style=for-the-badge)  

</div>  

Welcome to the very first step of my **Silicon Diary** 📝.  
Day 0 was all about **laying the foundation**: 
- Getting started with Digital VLSI SOC Design and Planning
- Creating this GitHub repository to document my journey.  
- Setting up a **Linux-based design environment** and installing essential tools.  

---

## 🎯 Task Breakdown  

| # | Task | Outcome |
|---|------|---------|
| 1️⃣ | **Summarize Getting started with Digital VLSI SOC Design and Planning Video** | Key takeaways captured with screenshot |
| 2️⃣ | **Install Open-Source EDA Tools** | Yosys, Icarus Verilog, GTKWave, Ngspice, Magic VLSI installed & tested |

---

## ![Task 1](https://img.shields.io/badge/Task%201-Video%20Summary-blueviolet?style=for-the-badge)  

The introductory session explained the **SoC design flow** step by step:  

- **Specs (C model)** ➝ High-level system behavior defined in C.  
- **RTL Design (Verilog)** ➝ Hardware description created by RTL architects.  
- **Processor + IPs** ➝ Integration of processor core and peripherals.  
- **Gate-level Netlist** ➝ RTL synthesized into logic gates.  
- **SoC Integration** ➝ Combining macros, analog IPs, and GPIOs.  
- **Floorplanning & GDSII** ➝ Physical design and final tape-out.  

## 📷 **Flow Chart of SoC design flow**
<p align="center">
  <img src="Images/SoC Design Flow.png" alt="SoC Design Flow" width="600">

</p>

<div align="center"></div>

---
## ![Task 2](https://img.shields.io/badge/Task%202-EDA%20Tool%20Setup-green?style=for-the-badge)

Installed all required open-source EDA tools for the RTL2GDS flow using a Linux-based setup.  
This section provides an overview of each tool, its purpose in the design flow, and a snapshot of successful installation.

---

## 🧠 Yosys – RTL Synthesis

- **What is it?**  
  This is a framework for RTL synthesis tools. It currently has extensive Verilog-2005 support and provides a basic set of synthesis algorithms for various application domains.

Yosys can be adapted to perform any synthesis job by combining the existing passes (algorithms) using synthesis scripts and adding additional passes as needed by extending the yosys C++ code base.

---
- **Purpose in Design Flow:**  
Yosys's purpose in a design flow is to act as an open-source logic synthesis tool, taking high-level hardware descriptions in Verilog or other HDLs and converting them into a detailed, optimized gate-level netlist for ASICs or FPGAs. It performs logic optimization and technology mapping to produce efficient designs, and its extensible nature makes it a flexible base for custom synthesis tools within a larger design ecosystem._
---
<summary>📌 <b>Installation Steps</b></summary>  

```bash
Yosys
$ sudo apt-get update
$ git clone https://github.com/YosysHQ/yosys.git
$ cd yosys
$ sudo apt install make (If make is not installed please install it)
$ sudo apt-get install build-essential clang bison flex \
libreadline-dev gawk tcl-dev libffi-dev git \
graphviz xdot pkg-config python3 libboost-system-dev \
libboost-python-dev libboost-filesystem-dev zlib1g-dev
$ make config-gcc
$ make
```

---
- **📸 Tool Installation Verification Image:**  
  ![Yosys](Images/yosys.png)

- **🔗 References:**  
  - [ about Yosys] [https://github.com/YosysHQ/yosys](#)
  - [ For more information ] [https://yosyshq.net/yosys/](#)

---

## ⚙️ Icarus Verilog – HDL Simulation

- **What is it?**  
Icarus Verilog is an implementation of the Verilog hardware description language compiler that generates netlists in the desired format (EDIF) and a simulator. It supports the 1995, 2001 and 2005 versions of the standard, portions of SystemVerilog, and some extensions._
---
- **Purpose in Design Flow:**  
  _
Icarus Verilog serves a crucial purpose in the System-on-Chip (SoC) design flow, primarily as an open-source Verilog simulator and synthesis tool. Its main functions in this context include:

    RTL Simulation and Verification:
        Icarus Verilog compiles and simulates Verilog HDL code, allowing designers to verify the functional correctness of their Register-Transfer Level (RTL) designs.
        It executes the compiled Verilog code, often generating Value Change Dump (VCD) files that capture the signal waveforms over time. These VCD files can then be viewed and analyzed using waveform viewers like GTKWave for debugging and understanding the design's behavior.
        This simulation phase is critical for identifying and correcting design errors early in the flow, before committing to more expensive physical implementation_
---
<summary>📌 <b>Installation Steps</b></summary>  

```bash
Steps to install iverilog
sudo apt-get update
sudo apt-get install iverilog
```

---
- **📸 Tool Installation Verification Image:**  
  ![Icarus Verilog](Images/iverilog.png)

- **🔗 References:**  
  - [ wikipedia] [https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://en.wikipedia.org/wiki/Icarus_Verilog&ved=2ahUKEwjZ1rHFyuWPAxWixDgGHUwQK-gQFnoECBkQAw&usg=AOvVaw22K9glLBZOCY6_iBzqdtT7](#)

---

## 📈 GTKWave – Waveform Viewer

- **What is it?**  
GTKWave has been developed to perform debug tasks on large systems on a chip and has been used in this capacity as an offline replacement for third-party debug tools. It is 64-bit clean and is ready for the largest of designs given that it is run on a workstation with a sufficient amount of physical memory._

---
  **Purpose in Design Flow:**  
  _
  To see the RTL Verilog code simulation waveform to verify the specifications

  ---
<summary>📌 <b>Installation Steps</b></summary>  

```bash
Steps to install gtkwave
sudo apt-get update
sudo apt install gtkwave
```
---
- **📸 Tool Installation Verification Image:**  
  ![GTKWave](Images/GTkWave.png)
---

- **🔗 References:**  
  - [ github] [https://gtkwave.github.io/gtkwave/](#)
  - [ Main site] [https://gtkwave.sourceforge.net/](#)

---

## 🔁 Ngspice – Analog Simulation

- **What is it?**  
ngspice is the open source spice simulator for electric and electronic circuits.
Such a circuit may comprise of JFETs, bipolar and MOS transistors, passive elements like R, L, or C, diodes, transmission lines and other devices, all interconnected in a netlist. Digital circuits are simulated as well, event driven and fast, from single gates to complex circuits. And you may enter the combination of both analog and digital as a mixed-signal circuit._

  --- **Purpose in Design Flow:**  
gspice is a circuit simulator that numerically solves equations describing (electronic) circuits: These are made of passive and active devices. Time varying currents and voltages are simulated as well as noise and small signal behavior.
<summary>📌 <b>Installation Steps</b></summary>  

```bash
After downloading the tarball from https://sourceforge.net/projects/ngspice/files/ to a local
directory, unpack it using:
$ tar -zxvf ngspice-37.tar.gz
$ cd ngspice-37
$ mkdir release
$ cd release
$ ../configure --with-x --with-readline=yes --disable-debug
$ make
$ sudo make install
```
---

- **📸 Tool Installation Verification Image:**  
  ![Ngspice](Images/ngspice.png)

- **🔗 References:**  
  - [ NGSPICE] [https://ngspice.sourceforge.io/](#)
  

---

## 🧱 Magic VLSI – Layout Editor

- **What is it?**  
Magic VLSI is an open-source electronic design automation (EDA) tool for designing and modifying Very Large Scale Integration (VLSI) circuits, also known as integrated circuits (ICs). Created in the 1980s at UC Berkeley, it uses a lambda-based design style with well-thought-out algorithms and a liberal license that makes it popular in universities and smaller companies for its ease of use, advanced features like automatic rule checking, and ability to stay current with fabrication technology_

- **Purpose in Design Flow:**  
The primary purpose of the Magic VLSI tool is to design and edit integrated circuit (IC) layouts by providing a user-friendly, interactive environment for creating the physical structures of electronic circuits_

- **📸 Snapshot:**  
  ![Magic VLSI](Images/magic.png)

- **🔗 References:**  
  - [ Magic] [http://opencircuitdesign.com/magic/](#)

---

# 🚀 Environment Ready for VLSI Design Journey!
---
## 🚀 **VLSI Design Journey – Ready to Begin!**

<div align="center">
  
  ![Repository Badge](https://img.shields.io/badge/Repository-silicon-diary-FF6F61)
  [📂 **Repository:** silicon-diary](https://github.com/Jaynandan-Kushwaha/silicon-diary)

  ![Author Badge](https://img.shields.io/badge/Author-Jaynandan_Kushwaha-42A5F5)
  [👨‍💻 **Author:** Jaynandan Kushwaha](https://github.com/Jaynandan-Kushwaha)

  ![Program Badge](https://img.shields.io/badge/Program-VLSI_System_Design-66BB6A)
  [📚 **Program:** VLSI System Design (VSD)](https://www.vlsi.org/)
</div>



---

# /mnt/data/silicon_repo/silicon-diary-main/Day0/Images/README.md

THis Folder will contain all Day 0 work Images of every task 


# Week1

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Readme.md


# 🚀 RTL Design & Synthesis Workshop — *Sky130 Edition*  

> Dive into the fascinating world of **digital logic design** where every line of Verilog can shape the blueprint of silicon.  
This workshop is not just about coding flip-flops and gates — it’s about **thinking like a chip designer**, simulating your ideas, optimizing them, and finally synthesizing them into something closer to real hardware.  
If you’ve ever wondered how RTL transforms into circuits, or how synthesis tools squeeze out efficiency, you’re in the right place! 🌟  

![GitHub Repo Size](https://img.shields.io/github/repo-size/Jaynandan-Kushwaha/silicon-diary?color=blue&style=flat-square)  
![GitHub Stars](https://img.shields.io/github/stars/Jaynandan-Kushwaha/silicon-diary?style=social)  
![Author: jaynandan-kushwaha](https://img.shields.io/badge/Author-jaynandan--kushwaha-blue)  

---

## 📑 Contents  

- [📘 About the Workshop](#-about-the-workshop)  
- [🛠️ Prerequisites](#️-prerequisites)  
- [📂 Workshop Roadmap](#-workshop-roadmap)  
- [🙏 Acknowledgements](#-acknowledgements)  

---

## 📘 About the Workshop  

This workshop is crafted for **students, hobbyists, and engineers** who want to strengthen their understanding of digital design and RTL flow. You’ll learn to:  

- 🖊️ Write **clean Verilog RTL code**  
- 🧪 Run simulations with **Icarus Verilog + GTKWave**  
- ⚙️ Perform **logic synthesis** with **Yosys + Sky130 PDK**  
- 🧩 Master essential design concepts:  
  - Testbenches  
  - Timing libraries  
  - Flip-flop coding styles  
  - Combinational vs sequential optimization  

By the end, you won’t just know RTL — you’ll know how to make it **efficient, optimized, and hardware-ready**.  

---

## 🛠️ Prerequisites  

Before you begin, make sure you have:  

- Basic knowledge of **digital circuits** (gates, mux, flip-flops)  
- Comfort with **Linux shell commands**  
- Installed tools:  
  - `git`  
  - `iverilog`  
  - `gtkwave`  
  - `yosys`  
  - A text editor (VSCode, Vim, Nano, etc.)  

💡 *Tip: On Windows/macOS, you can use WSL for a Linux environment.*  

---

## 📂 Workshop Roadmap  

This repo is organized into **5 days of learning and labs**:  

| 📅 Day | 📝 Focus Area | 🔗 Link |
|-------|---------------|---------|
| 1️⃣ | Verilog RTL Basics & Synthesis | [Day1](Day1/Read.md) |
| 2️⃣ | Timing Libraries & DFF Coding Styles | [Day2](Day2/Readme.md) |
| 3️⃣ | Combinational + Sequential Optimization | [Day3](Day3/Read.md) |
| 4️⃣ | Gate-Level Simulation & Verilog Nuances | [Day4](Day4/Readme.md) |
| 5️⃣ | Advanced Synthesis Optimization | [Day5](Day5/Readme.md) |  

🔎 Each day includes:  
✔️ Explanations with visuals  
✔️ Hands-on Verilog examples  
✔️ Simulation outputs & screenshots  
✔️ Best practices to avoid common pitfalls  

---

## 🙏 Acknowledgements  

Huge thanks to everyone making open-source VLSI learning possible:  
- 👨‍💻 [Kunal Ghosh](https://www.linkedin.com/in/kunal-ghosh-vlsisystemdesign-com-28084836/)  
- 🛠️ Open-source tool developers: **Yosys**, **Icarus Verilog**, **Sky130 PDK**  

---

✨ *Happy Coding & Chip Designing!* ✨  


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day1/Readme.md

# Day 1 – Introduction to Verilog RTL Design and Synthesis  

Author: **Jaynandan Kushwaha**  

---

## 📌 Introduction  

Welcome to **Day 1** of the **RTL Design and Synthesis Workshop** using **Sky130 PDKs**.  

This session marks the starting point of our digital design journey, where we move from **abstract hardware descriptions** to **practical, synthesizable logic**.  

You will be introduced to:  
- Writing Verilog RTL code and testbenches.  
- Running simulations using **Icarus Verilog (iverilog)**.  
- Visualizing outputs with **GTKWave**.  
- Understanding the basics of **logic synthesis with Yosys**.  
- Mapping RTL to the **Sky130 standard cell libraries**.  

The aim of this day is to build a **strong foundation**. Just as an architect first draws blueprints before construction, we will learn how to **design, simulate, and synthesize** digital logic that can ultimately be realized on silicon.  

By the end of Day 1, you will not only understand the RTL design flow but also **perform your first hands-on simulation and synthesis**. This will set the stage for deeper explorations in the upcoming sessions.  

---
## 📂 Table of Contents  

### 🔹 Basics  
1. [📖 Introduction to Verilog RTL Design and Synthesis](#1-Introduction-to-Verilog-RTl-Design-and-Synthesis)  
2. [⚙️ Introduction to Icarus Verilog (Simulator)](#2-introduction-to-icarus-verilog-simulator)  

### 🔹 Hands-On Labs (Simulation)  
3. [🧪 Lab 1 – Setup Overview](#3-labs-using-icarus-verilog-and-gtkwave)  
4. [🖥️ Lab 2 – Simulation with Icarus Verilog + GTKWave (Part 1)](#3-labs-using-icarus-verilog-and-gtkwave)  
5. [📊 Lab 3 – Simulation with Icarus Verilog + GTKWave (Part 2)](#3-labs-using-icarus-verilog-and-gtkwave)  

### 🔹 Synthesis with Yosys  
6. [⚡ Introduction to Yosys and Logic Synthesis](#4-introduction-to-yosys-and-logic-synthesis)  
7. [🔬 Lab 1 – Synthesis of MUX (Part 1)](#5-labs-using-yosys-and-sky130-pdks)  
8. [🔬 Lab 2 – Synthesis of MUX (Part 2)](#5-labs-using-yosys-and-sky130-pdks)  
9. [🔬 Lab 3 – Synthesis of MUX (Part 3)](#5-labs-using-yosys-and-sky130-pdks)  

### 🔹 References & Summary  
10. [🛠️ Tools Overview](#6-tools-overview)  
11. [⌨️ Common Commands](#7-common-commands)  
12. [🎯 Learning Outcomes](#8-learning-outcomes)  
---
## 🔹Basics. 
 
### 1. Introduction to Verilog RTL Design and Synthesis
In introduction it started with some basic definations which are describe below and its important to know about these terminology before starting it 
#### Simulator
Simulators are essential tools used to model, analyze, and verify the behavior of integrated circuits before physical fabrication, ensuring design accuracy and performance.
<div align="center">
  <img src="Images/Simulator1.png" alt="Simulator" width="70%">
</div>

#### How Simulator Works:

##### 1. Parsing & Compilation
- Reads your code (Verilog/VHDL) and checks syntax.
- Converts design into an internal model.

##### 2. Elaboration
- Resolves module hierarchy and signal connections.
- Sets initial values for all signals.

##### 3. Simulation (Event-Driven)
- Signals are updated only when inputs change.
- Changes propagate through the circuit based on logic and delays.

##### 4. Output & Waveforms
- Records signal values over time.
- Shows results via text or waveform viewer.
<div align="center">
  <img src="Images/Simulator_Working.png" alt="Simulator_Working" width="70%">
</div>
---

#### . Testbench and Its Working

#### What is a Testbench?
- A **testbench** is a simulation environment used to **verify and validate** a design (DUT – Design Under Test).
- It is **not synthesized into hardware**; it only exists for testing in simulation.
- Acts like a **virtual lab**, applying inputs and checking outputs of the design.
<div align="center">
  <img src="Images/Testbench.png" alt="Testbench" width="70%">
</div>
---

#### How a Testbench Works
1. **Instantiate DUT**  
   - The testbench creates an instance of the design module to be tested.

2. **Generate Stimulus (Inputs)**  
   - Provides different input patterns (clock, reset, test signals) to the DUT.

3. **Monitor Outputs**  
   - Captures and observes the DUT outputs for correctness.

4. **Check/Verify Results**  
   - Compares DUT output with the expected output (using assertions or manual checks).

5. **Display Results**  
   - Uses `$display`, `$monitor`, or waveform viewers to show simulation behavior.

## Key Points
- A testbench usually includes **clock generation, reset logic, input stimulus, and output checking**.
- It helps detect errors **early in simulation** before going to hardware.
<div align="center">
  <img src="Images/testbench_Working.png" alt="testbench_Working" width="70%">
</div>
---

#### .Design
I put lecture screenshot for defining Design 
<div align="center">
  <img src="Images/Design.png" alt="Design" width="70%">
</div

----

#### . Iverilog Based simulation Flow
In Iverilog Based simulation flow we provide verilog file and testbench file as a input to a iverilog and it dumped file in vcd and that file we can analyse in gtkwave
<div align="center">
  <img src="Images/Simulation_Flow.png" alt="Design" width="70%">
</div 
---

## Lab Setup 

### Lab1 
Make seprate folder for saving our whole lab work in one folder 
```shell
mkdir VSD/VLSI
```

####  Step 1: Clone the Workshop Repository

```shell
git clone https://github.com/kunalg123/sky130RTLDesignAndSynthesisWorkshop.git
cd sky130RTLDesignAndSynthesisWorkshop/verilog_files
```
####  Step 2: Install Required Tools

install these tool if you didnt install in day 0 work 
if you then ignore this part
```shell
sudo apt install iverilog
sudo apt install gtkwave
```
----

### Lab2 

In lab2 we learn how to operate and what are the command to run iverilog and gtk wave tool with on example 
Here are steps:
we taken exapmle of good_mux verilog file 
1.Compile the design and testbench:
```shell
iverilog good_mux.v tb_good_mux.v
```
2.Run the simulation:

```shell
./a.out
```
3.View the waveform:

```shell
gtkwave tb_good_mux.vcd
```
<div align="center">
  <img src="Images/Good_mux.png" alt="Good_mux" width="70%">
</di
<div align="center">
  <img src="Images/good_mu-GTKwave View.png" alt="GTKWave" width="70%">
</div>
---

 4. Verilog Code Analysis

**The code for the multiplexer (`good_mux.v`):**

```verilog
module good_mux (input i0, input i1, input sel, output reg y);
always @ (*)
begin
    if(sel)
        y <= i1;
    else 
        y <= i0;
end
endmodule
```

####  **How It Works**

- **Inputs:** `i0`, `i1` (data), `sel` (select line)
- **Output:** `y` (registered output)
- **Logic:** If `sel` is 1, `y` gets `i1`; if `sel` is 0, `y` gets `i0`.

---

## . Introduction to Yosys & Gate Libraries

### What is Yosys?
**Yosys** is an open-source tool used for **logic synthesis** of digital circuits.  
It translates Verilog designs into a **gate-level netlist**, which acts like a blueprint of the actual hardware implementation.

#### Key Capabilities of Yosys
- **Logic Synthesis:** Turns HDL code into interconnected logic gates.  
- **Design Optimization:** Refines circuits for better speed, area, or power.  
- **Technology Mapping:** Maps generic logic onto specific hardware library cells.  
- **Formal Verification:** Ensures design correctness through checks.  
- **Flexible Extensions:** Can be integrated into custom flows and EDA tools.  

---

### Why Do Libraries Have Multiple Gate Variants?
Standard cell libraries (`.lib` files) don’t just provide one type of gate—they usually offer **several versions of the same gate** (AND, OR, NOT, etc.) with different characteristics.  

Some factors that distinguish these gate variants include:
- **Speed:** High-performance gates for time-critical paths.  
- **Power Consumption:** Low-power options to save energy.  
- **Area:** Compact cells to minimize chip size.  
- **Drive Strength:** Stronger cells to handle larger loads.  
- **Noise & Integrity:** Special cells to maintain signal quality.  
- **Mapping Flexibility:** Gives synthesis tools options to balance trade-offs.  

---

👉 In short, Yosys performs the **conversion and optimization**, while the gate libraries provide the **building blocks in different “flavors”** to match design needs.

---
### Here are some Golden Key Point About this topic well explained and by Teacher here i am attaching for my revision purpose in future i can refresh my concept

<div align="center">
  <img src="Images/Lecture1.png" alt="Lecture1.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture2.png" alt="Lecture2.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture3.png" alt="Lecture3.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture4.png" alt="Lecture4.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture5.png" alt="Lecture5.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture6.png" alt="Lecture6.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture7.png" alt="Lecture7.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture8.png" alt="Lecture8.png" width="70%">
</div>
<div align="center">
  <img src="Images/Lecture9.png" alt="Lecture9.png" width="70%">
</div>



## . Synthesis Lab with Yosys

Let’s synthesize the `good_mux` design using Yosys!

###  Step-by-Step Yosys Flow


1. **Start Yosys**
   inside your  this adress where we clone our sky130 lab package /home/jaynadan/vsd/VLSI/sky130RTLDesignAndSynthesisWorkshop/verilog_files
   start yosis 
    ```shell
    yosys
    ```

3. **Read the liberty library**
    ```shell
    read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
    ```
    Note:- everyone can have in different folder so check according to that where .lib file existing 

4. **Read the Verilog code**
    ```shell
    read_verilog /home/vsd/VLSI/sky130RTLDesignAndSynthesisWorkshop/verilog_files/good_mux.v
    ```

5. **Synthesize the design**
    ```shell
    synth -top good_mux
    ```

6. **Technology mapping**
    ```shell
    abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
    ```

7. **Visualize the gate-level netlist**
    ```shell
    show
    ```

<div align="center">
  <img src="Images/Good-mux-synthesis.png" alt="Good-mux-synthesis.png" width="70%">
</div>

---
## 7. Summary

- We explored how **simulators** work and why they are essential in testing digital designs.  
- We understood the role of a **testbench** and how it drives and verifies a design in simulation.  
- We performed our **first Verilog simulation** using `iverilog` and observed outputs through waveforms.  
- We broke down the working of a **Good_Mux** and analyzed its Verilog code.  
- We got introduced to **Yosys**, learning how it performs synthesis and how different **gate library flavors** help balance speed, power, and area.
---

#### Thats all what we learned in day 1 

I attended every lecture in time but due to health issues i wasnt able to write github notes on that day itself but i was consistent everyday and did my all task everyday 

---

## A Note of Gratitude 🙏

This journey has been more than just learning Verilog or tools—it’s been about clarity, confidence, and inspiration.  
I’m not worried about rankings like top 50 or top 20, because the knowledge we are receiving here is already a **golden reward** for students like us.  

To our teacher: thank you for simplifying what once felt impossible, and for sharing wisdom with such patience.  
You are truly a **gem for learners**, and words will never be enough to capture our gratitude.  
Once again, thank you, sir! 🌟



---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day1/Images/Read.md


This read me will contain whole lecture and lab picture for Day1 


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day2/Readme.md

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
<div align="center">
  <img src="Images/Lecture2.png" alt="Lecture2.png" width="70%">
</div>
In this lecture they explain about multiple modules and how they work and how they will look after synthesis

#### Here is one exapmle we synthesis multipul module.v file and understand the synthesisation behind the tool

1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog multiple_modules.v
   ```
4. Synthesize:
   ```shell
   synth -top multiple_module
   ```
6. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
7. Visualize the gate-level netlist:
   ```shell
   show multiple_modules
   ```

<div align="center">
  <img src="Images/Multiple_Modules.png" alt="Multiple_Modules.png" width="70%">
</div>
8. for generating heir.v file:

 ```shell
  write_verilog multiple_modules_hier.v
   ```
<div align="center">
  <img src="Images/multiple_module.png" alt="multiple_module.png" width="70%">
</div>
with the help of this file we try to understand what we assumed or design by our logic is that correct or not 
after this we flatten the design and see that design here is output 
<div align="center">
  <img src="Images/multiple_module.png" alt="multiple_module.png" width="70%">
</div>

after comparing this we also see sub_module1 and submodule2 both submodule and see is they synthesise correct as sir explain in class 
<div align="center">
  <img src="Images/submodule1.png" alt="submodule1.png" width="70%">
</div>
<div align="center">
  <img src="Images/submodule2.png" alt="submodule2.png" width="70%">
</div>


## Simulation and Synthesis Workflow

### Icarus Verilog Simulation

dff_asyncres

1. **Compile:**
   ```shell
   iverilog dff_asyncres.v tb_dff_asyncres.v
   ```
2. **Run:**
   ```shell
   ./a.out
   ```
3. **View Waveform:**
   ```shell
   gtkwave tb_dff_asyncres.vcd
   ```
<div align="center">
  <img src="Images/lecture3.png" alt="lecture3.png" width="70%">
</div>
---

dff_asyncres_set

1. **Compile:**
   ```shell
   iverilog dff_asyncres_set.v tb_dff_asyncres_set.v
   ```
2. **Run:**
   ```shell
   ./a.out
   ```
3. **View Waveform:**
   ```shell
   gtkwave tb_dff_asyncres_set.vcd
   ```
<div align="center">
  <img src="Images/lecture3.png" alt="lecture3.png" width="70%">
</div>

dff_synchrous


1. **Compile:**
   ```shell
   iverilog dff_syncres.v tb_dff_syncres.v
   ```
2. **Run:**
   ```shell
   ./a.out
   ```
3. **View Waveform:**
   ```shell
   gtkwave tb_dff_syncres.vcd
   ```
<div align="center">
  <img src="Images/lecture3.png" alt="lecture3.png" width="70%">
</div>
---

### Synthesis with Yosys
dff_asyncres
1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog dff_asyncres.v
   ```
4. Synthesize:
   ```shell
   synth -top dff_asyncres
   ```
5. Map flip-flops:
   ```shell
   dfflibmap -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
6. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
7. Visualize the gate-level netlist:
   ```shell
   show
   ```
<div align="center">
  <img src="Images/synth-assync.png" alt="synth-assync.png" width="70%">
</div> 

---

dff_assyncruns-set

1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog dff_async_set.v
   ```
4. Synthesize:
   ```shell
   synth -top dff_async_set
   ```
5. Map flip-flops:
   ```shell
   dfflibmap -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
6. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
7. Visualize the gate-level netlist:
   ```shell
   show
   ```
<div align="center">
  <img src="Images/synth-assync-set.png" alt="synth-assync-set.png" width="70%">
</div>  

---

dff-

1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog dff_asyncres.v
   ```
4. Synthesize:
   ```shell
   synth -top dff_asyncres
   ```
5. Map flip-flops:
   ```shell
   dfflibmap -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
6. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
7. Visualize the gate-level netlist:
   ```shell
   show
   ```
<div align="center">
  <img src="Images/synth-sync.png" alt="synth-sync.png" width="70%">
</div>  

### Intresting Optimisation
Mul2
1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog mult_2.v
   ```
4. Synthesize:
   ```shell
   synth -top mul2
   ```

5. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
6. Visualize the gate-level netlist:
   ```shell
   show
   ```
<div align="center">
  <img src="Images/mul2.png" alt="mul2.png" width="70%">
</div>  

Mul8
1. Start Yosys:
   ```shell
   yosys
   ```
2. Read Liberty library:
   ```shell
   read_liberty -lib ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
3. Read Verilog code:
   ```shell
   read_verilog mult_8.v
   ```
4. Synthesize:
   ```shell
   synth -top mult8
   ```

5. Technology mapping:
   ```shell
   abc -liberty ../lib/sky130_fd_sc_hd__tt_025C_1v80.lib
   ```
6. Visualize the gate-level netlist:
   ```shell
   show
   ```
<div align="center">
  <img src="Images/mul8.png" alt="mul8.png" width="70%">
</div> 
---

## Summary

This guide has covered key aspects of **RTL design and synthesis**, offering practical insights into **timing libraries, synthesis methodologies, and flip-flop coding styles**.  

- **Timing Libraries:** Understanding different process corners, voltage, and temperature variations helps ensure that your design meets performance and reliability requirements.  
- **Synthesis Strategies:** Hierarchical and flattened synthesis approaches provide flexibility in optimizing design speed, area, and debugability. Choosing the right approach depends on the size and complexity of your design.  
- **Flip-Flop Coding Practices:** Proper coding of asynchronous and synchronous flip-flops ensures predictable behavior, avoids glitches, and supports robust sequential circuit design.

By exploring and experimenting with these concepts, you can **improve your RTL design skills**, write cleaner code, and make your designs more efficient, modular, and easier to debug. This foundation will help you confidently tackle **complex digital systems** and optimize them for real-world applications.



---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day2/Images/Read.md

 this folder for storing images


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day3/Read.md


# Day 3 – Combinational and Sequential Optimizations
**Author:** Jaynandan Kushwaha

## 📌 **Introduction**  

Day 3 focuses on **optimizing digital designs** at both the combinational and sequential levels. Efficient optimization techniques not only improve timing and performance but also reduce area and power consumption.  

We start with an introduction to basic optimization principles, understanding how synthesis tools identify opportunities for improvement. Then, we explore **combinational logic optimizations**, learning strategies to simplify and speed up logic paths. After that, we dive into **sequential logic optimizations**, including efficient flip-flop usage and techniques for handling unused outputs.  

By the end of this day, you will gain practical knowledge of optimization methods that make RTL designs **faster, smaller, and more reliable**, and learn how to apply these techniques during synthesis and simulation.

---

## 📚 **Contents**  
---
🔹 1. Introduction to Optimizations  
🧩 Lecture 1: Introduction to Optimizations – Part 1  
🧩 Lecture 2: Introduction to Optimizations – Part 2  
🧩 Lecture 3: Introduction to Optimizations – Part 3  

🔹 2. Combinational Logic Optimizations  
⚡ Lab 1: Combinational Logic Optimisations – Part 1  
⚡ Lab 2: Combinational Logic Optimisations – Part 2  

🔹 3. Sequential Logic Optimizations  
🔄 Lab 3: Sequential Logic Optimisations – Part 1  
🔄 Lab 4: Sequential Logic Optimisations – Part 2  
🔄 Lab 5: Sequential Logic Optimisations – Part 3  

🔹 4. Sequential Optimizations for Unused Outputs  
✨ Lab 6: Sequential Optimisation for Unused Outputs – Part 1  
✨ Lab 7: Sequential Optimisation for Unused Outputs – Part 2

---

# Introduction about Loguc Optimisation

## Combinational Logic Optimisation

**Overview:**  
Constant propagation is an **optimization technique** used during synthesis where variables assigned a fixed value are directly replaced with that constant. This eliminates unnecessary logic and makes the circuit leaner and more efficient.

**How It Works:**  
The synthesis tool scans the RTL code to detect signals or variables that always hold a **constant value**. Instead of preserving them as separate operations, the tool substitutes the constant directly into the logic. This often leads to removal of redundant gates or even entire portions of unused circuitry.

**Key Benefits:**  
- **Simplified Logic:** Reduces the design complexity by cutting down unnecessary operations.  
- **Performance Gains:** Shorter logic paths result in faster execution and reduced delay.  
- **Resource Efficiency:** Minimizes the number of gates and flip-flops required, saving both area and power.  

Constant propagation is a small optimization step, but it plays a **big role in streamlining designs**, making circuits more compact and improving overall synthesis quality.
<div align="center">
  <img src="Images/Combinational.png" alt="combinational.png" width="70%">
</div> 

### Explanation of type of Combinational logic
#### Constant Propagation in Combinational Optimization

**Concept:**  
In combinational optimization, **constant propagation** is the process of detecting inputs or signals that always evaluate to a fixed value (0 or 1) and replacing them directly in the logic. By doing this, synthesis tools can eliminate unnecessary gates and simplify the overall circuit.

**How It Works:**  
- The synthesis tool scans through combinational logic equations.  
- If a variable or expression is tied to a constant value, that constant is directly substituted.  
- This substitution often leads to removal of redundant gates and collapsing of logic paths.  

<div align="center">
  <img src="Images/Constant-Ex.png" alt="Constant-Ex.png" width="70%">
</div>

---


#### Boolean Simplification in Combinational Optimization

**Concept:**  
Boolean simplification is the process of reducing logic expressions using **Boolean algebra rules** without changing their functionality. The goal is to minimize the number of logic gates, reduce circuit complexity, and improve performance.

**How It Works:**  
- The synthesis tool applies Boolean identities (like absorption, De Morgan’s theorem, distributive law, etc.) to simplify equations.  
- Equivalent but **smaller logic expressions** replace the original design.  
- This leads to fewer gates in the final netlist and optimized timing paths.  
<div align="center">
  <img src="Images/Boolean-EX.png" alt="Constant-Ex.png" width="70%">
</div>

---

## Sequential Optimization

**Concept:**  
Sequential optimization deals with improving circuits that use **storage elements** such as flip-flops and registers. Unlike combinational logic, sequential circuits rely on both current inputs and stored states, so the focus here is on reducing unnecessary registers, improving timing, and making the design more efficient.

**How It Works:**  
- **Redundancy Removal:** Identifies flip-flops or registers that do not contribute to the final output or always hold a constant value, and removes them.  
- **State Minimization:** Simplifies state machines by merging equivalent or unreachable states.  
- **Retiming:** Redistributes flip-flops across the design to balance delay, shorten the critical path, and improve clock speed.  
- **Unused Outputs:** Detects sequential elements whose outputs are never used and eliminates them to save resources.  

**Benefits of Sequential Optimization:**  
- **Reduced Area and Power:** Fewer flip-flops and registers mean smaller designs with lower power consumption.  
- **Improved Performance:** Retiming balances logic delays, enabling higher clock frequencies.  
- **Cleaner Design:** Removes unused or redundant sequential logic, making the design easier to analyze and verify.  

Sequential optimization is especially valuable in **large RTL systems**, where careful management of storage elements can significantly improve both **efficiency and reliability** of the overall design.

<div align="center">
  <img src="Images/Sequantial.png" alt="sequantial.png" width="70%">
</div>

---

Exaple to explain Sequantial 
<div align="center">
  <img src="Images/explanation.png" alt="sequantial.png" width="70%">
</div>
<div align="center">
  <img src="Images/explanation2.png" alt="sequantial.png" width="70%">
</div>

---

## Key Sequential Optimization Techniques

### 1. State Optimization
**Definition:**  
State optimization is the process of reducing the number of states in a **finite state machine (FSM)** without changing its functionality.  

**How it Works:**  
- Identifies **equivalent states** that produce the same outputs and transitions, then merges them.  
- Removes **unreachable states** that cannot be activated under any input condition.  

**Benefits:**  
- Smaller state machines → fewer flip-flops.  
- Reduced complexity → faster synthesis and verification.  
- Lower area and power consumption.

---

### 2. Cloning
**Definition:**  
Cloning is the duplication of a sequential element (like a flip-flop or register) to reduce fanout and improve timing performance.  

**How it Works:**  
- When a single register drives too many loads (high fanout), it causes delay.  
- The tool **duplicates the register** so that loads are distributed across multiple drivers.  

**Benefits:**  
- Reduces load per register.  
- Improves timing closure by shortening critical paths.  
- Ensures more balanced signal distribution.

---

### 3. Retiming
**Definition:**  
Retiming is a technique where flip-flops are **moved across combinational logic** without changing the overall functionality, to balance delay and improve performance.  

**How it Works:**  
- Analyzes logic paths and identifies imbalances in delay.  
- Shifts registers forward or backward across logic gates to reduce the **critical path delay**.  

**Benefits:**  
- Enables higher clock frequencies.  
- Balances timing across pipeline stages.  
- Improves overall circuit performance without changing logic behavior.

## . Labs on Optimization

### Lab 1

Below is the Verilog code for Lab 1:

```verilog
module opt_check (input a , input b , output y);
	assign y = a?b:0;
endmodule
```

**Explanation:**
- `assign y = a ? b : 0;` means:
  - If `a` is true, `y` is assigned the value of `b`.
  - If `a` is false, `y` is 0.
  
#### Output

<div align="center">
  <img src="Images/opt_check.png" width="70%">
</div>

### Lab 2

Verilog code:

```verilog
module opt_check2 (input a , input b , output y);
	assign y = a?1:b;
endmodule
```

**Code Analysis:**
- Acts as a multiplexer:
  - `y = 1` if `a` is true.
  - `y = b` if `a` is false.

<div align="center">
  <img src="Images/opt_check2.png" width="70%">
</div>

### Lab 3

Verilog code:

```verilog
module opt_check2 (input a , input b , output y);
	assign y = a?1:b;
endmodule
```

**Functionality:**  
2-to-1 multiplexer; `y = a ? 1 : b` (outputs `1` when `a` is true, otherwise `b`).
<div align="center">
  <img src="Images/opt_check3.png" width="70%">
</div>

### Lab 4

Verilog code:

```verilog
module opt_check4 (input a , input b , input c , output y);
 assign y = a?(b?(a & c ):c):(!c);
 endmodule
```

**Functionality:**
- Three inputs (`a`, `b`, `c`), output `y`.
- Nested ternary logic:
  - If `a = 1`, `y = c`.
  - If `a = 0`, `y = !c`.
- Logic simplifies to:  
  `y = a ? c : !c`

<div align="center">
  <img src="Images/opt_check4.png" width="70%">
</div>
<div align="center">
  <img src="Images/opt_check4-1.png" width="70%">
</div>

### Lab 5
Verilog code:

```verilog
module multiple_module_opt(input a , input b , input c , input d , output y);
wire n1,n2,n3;

sub_module1 U1 (.a(a) , .b(1'b1) , .y(n1));
sub_module2 U2 (.a(n1), .b(1'b0) , .y(n2));
sub_module2 U3 (.a(b), .b(d) , .y(n3));

assign y = c | (b & n1); 


endmodule
```
<div align="center">
  <img src="Images/multiple_opt.png" width="70%">
</div>

### Lab 6
Verilog code:

```verilog
module sub_module(input a , input b , output y);
 assign y = a & b;
endmodule



module multiple_module_opt2(input a , input b , input c , input d , output y);
wire n1,n2,n3;

sub_module U1 (.a(a) , .b(1'b0) , .y(n1));
sub_module U2 (.a(b), .b(c) , .y(n2));
sub_module U3 (.a(n2), .b(d) , .y(n3));
sub_module U4 (.a(n3), .b(n1) , .y(y));


endmodule
```
<div align="center">
  <img src="Images/multiple_module_opt2.png" width="70%">
</div>
### Lab 7

#### dff-const-1
**Gtk-Wave Output** 

<div align="center">
  <img src="Images/dff_const1-gtk.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/synth-const1.png" width="70%">
</div>

### Lab 8

#### dff-const-2
**Gtk-Wave Output** 

<div align="center">
  <img src="Images/const-2-gtk.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/synth-const-2.png" width="70%">
</div>

### Lab 9

#### dff-const-3
**Gtk-Wave Output** 

<div align="center">
  <img src="Images/const-gtk-3.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/syth-const-3.png" width="70%">
</div>

### Lab 10

#### dff-const-4
**Gtk-Wave Output** 

<div align="center">
  <img src="Images/const4-gtk.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/synth-const-4.png" width="70%">
</div>

### Lab 11

#### dff-const-5
**Gtk-Wave Output** 

<div align="center">
  <img src="Images/gtk-const5.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/synth-const-5.png" width="70%">
</div>

## Sequantial Unused output labs 

### Lab 12

#### COunter-opt
**Sunthesis** 

<div align="center">
  <img src="Images/counter-opt.png" width="70%">
</div>

**Synthesis output**

<div align="center">
  <img src="Images/synth-counter.png" width="70%">
</div>

## Summary 

In this chapter, we explored the powerful techniques of **combinational and sequential optimizations** that help refine RTL designs into more efficient hardware.  

- On the **combinational side**, we looked at methods like **constant propagation** and **Boolean simplification**, which streamline logic expressions, remove redundant gates, and shorten critical paths. These optimizations directly improve circuit speed, reduce area, and lower power usage.  

- On the **sequential side**, we examined techniques such as **state optimization**, **cloning**, and **retiming**. These methods focus on storage elements and timing paths, aiming to reduce unnecessary registers, balance logic delays, and handle high-fanout issues effectively. Sequential optimizations are especially important for large-scale digital systems where timing closure and area efficiency are critical.  

Together, these optimization techniques demonstrate how synthesis tools not only translate RTL into gates but also **reshape and refine the design** to achieve better performance, smaller area, and improved power efficiency.  

This chapter builds the foundation for writing RTL that is not only functionally correct but also **optimized for real-world hardware implementation**.






---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day3/Images/Read.md




---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day4/Readme.md

# Day 4 – Gate-Level Simulation (GLS), Blocking vs Non-Blocking, and Synthesis-Simulation Mismatch  
Author: Jaynandan Kushwaha  

---

## 📌 Introduction  
Day 4 takes us further into **post-synthesis verification** and the importance of writing RTL that works reliably in both simulation and hardware.  

We begin with **Gate-Level Simulation (GLS)**, which validates the netlist generated after synthesis. Then we move to **synthesis-simulation mismatch**, understanding how poor coding styles or tool differences can cause functional issues. Finally, we explore the difference between **blocking and non-blocking assignments in Verilog**, two fundamental concepts that affect whether logic is inferred as **combinational or sequential**.  

By the end of this day, you will understand not only how to simulate at the gate level but also how to write RTL that avoids mismatches and follows best practices.  

---

## 📚 Contents  

🔹 **1. Gate-Level Simulation (GLS)**  
   - Concept and Importance  
   - Why and When to Perform GLS  
   - Functional GLS vs Timing GLS  

🔹 **2. Synthesis-Simulation Mismatch**  
   - Causes and Consequences  
   - Best Practices to Avoid Mismatches  

🔹 **3. Blocking vs Non-Blocking in Verilog**  
   - 3.1 Blocking Assignments  
   - 3.2 Non-Blocking Assignments  
   - 3.3 Comparison Table  

⚙️ **4. Labs**  
   - Lab 1: Gate-Level Simulation Run  
   - Lab 2: Debugging Simulation-Synthesis Mismatches  
   - Lab 3: Exploring Blocking vs Non-Blocking Behavior  

✨ **5. Summary**  

---

## 🔹 1. Gate-Level Simulation (GLS)  

**GLS** verifies the **gate-level netlist** produced after synthesis. Unlike RTL simulation, which runs on high-level code, GLS confirms that the **synthesized hardware representation** behaves as expected.  

### Why GLS?  
- ✅ Ensures that synthesis preserved functional correctness.  
- ✅ Validates timing with real delays from standard delay format (SDF).  
- ✅ Checks test logic such as scan chains.  

### When GLS is Done?  
- After **synthesis**, to confirm the design is correctly mapped.  
- Before **physical design**, to catch issues early.  

### Types of GLS  
- **Functional GLS**: Zero/unit delay simulation for logical correctness.  
- **Timing GLS**: Delay-annotated simulation for realistic timing checks.
<div align="center">
  <img src="Images/gls.png"  width="70%">
</div>
<div align="center">
  <img src="Images/gls_verilog.png"  width="70%">
</div>
<div align="center">
  <img src="Images/Exa.png"  width="70%">
</div>


---

## 🔹 2. Synthesis-Simulation Mismatch / Caveat 

A **synthesis-simulation mismatch** occurs when results from RTL simulation differ from those of gate-level simulation or real silicon.  

### Causes:  
- ❌ Use of **non-synthesizable constructs** (delays, initial blocks, etc.).  
- ❌ **Incomplete coding**, such as missing `else` or incorrect sensitivity lists.  
- ❌ **Ambiguity** in RTL that synthesis and simulation tools interpret differently.  

### Best Practices:  
- Write **synthesizable, tool-friendly RTL**.  
- Avoid constructs that simulators accept but synthesis ignores.  
- Always test with clear, deterministic coding styles.  
<div align="center">
  <img src="Images/Caveats.png"  width="70%">
</div>

---

## 🔹 3. Blocking vs Non-Blocking in Verilog  

Assignments in Verilog fall into two categories:  

### 3.1 Blocking Assignments  
- Executed immediately, in sequential order.  
- Best suited for **combinational logic**.  
- Simple and direct, but can cause incorrect behavior if used in sequential circuits.  

### 3.2 Non-Blocking Assignments  
- Executed concurrently at the end of a time step.  
- Best suited for **sequential logic**, such as registers and flip-flops.  
- Ensures predictable behavior in clocked systems.

  <div align="center">
  <img src="Images/Bloacking.png"  width="70%">
</div>


### 3.3 Comparison Table  

| **Aspect**                     | **Blocking (`=`)**                  | **Non-Blocking (`<=`)**             |
|--------------------------------|--------------------------------------|-------------------------------------|
| Execution Style                | Immediate, sequential               | Concurrent, scheduled               |
| Suitable For                   | Combinational logic                 | Sequential logic                    |
| Update Behavior                | Updates instantly in code order      | Updates applied after the time step |
| Common Use Case                | Temporary variables, calculations   | Registers, pipelines, flip-flops    |

---

## 4. Labs

### Lab 1: Ternary Operator MUX

Verilog code for a simple 2:1 multiplexer using a ternary operator:

```verilog
module ternary_operator_mux (input i0, input i1, input sel, output y);
  assign y = sel ? i1 : i0;
endmodule
```
- **Function:** `y = i1` if `sel = 1`; else `y = i0`.

 <div align="center">
  <img src="Images/ternary.png"  width="70%">
</div>

---

### Lab 2: Synthesis Using Yosys

Synthesize the above MUX using Yosys.  
_Follow the standard Yosys synthesis flow._

 <div align="center">
  <img src="Images/synth-ternary.png"  width="70%">
</div>

---

### Lab 3: Gate-Level Simulation (GLS) of MUX

Run GLS for the synthesized MUX.  
Use this command (adjust paths as needed):

```shell
iverilog /path/to/primitives.v /path/to/sky130_fd_sc_hd.v ternary_operator_mux.v testbench.v
```

 <div align="center">
  <img src="Images/GLS-mux.png"  width="70%">
</div>
---

### Lab 4: Bad MUX Example 

Verilog code with intentional issues:

```verilog
module bad_mux (input i0, input i1, input sel, output reg y);
  always @ (sel) begin
    if (sel)
      y <= i1;
    else 
      y <= i0;
  end
endmodule
```

#### Issues:
- **Incomplete sensitivity list**: Should include `i0`, `i1`, and `sel`.
- **Non-blocking assignment in combinational logic**: Should use blocking assignments (`=`).

**Corrected version:**
```verilog
always @ (*) begin
  if (sel)
    y = i1;
  else
    y = i0;
end
```

 <div align="center">
  <img src="Images/badmux.png"  width="70%">
</div>

---
### Lab 5: Synthesis Using Yosys

Synthesize the above bad MUX using Yosys.  
_Follow the standard Yosys synthesis flow._

 <div align="center">
  <img src="Images/synth-bad.png"  width="70%">
</div>

---

### Lab 6: GLS of Bad MUX

Perform GLS on the `bad_mux`.  
Expect simulation mismatches or warnings due to above issues.

 <div align="center">
  <img src="Images/gls-bad.png"  width="70%">
</div>

---

### Lab 7: Blocking Assignment Caveat

Verilog code:

```verilog
module blocking_caveat (input a, input b, input c, output reg d);
  reg x;
  always @ (*) begin
    d = x & c;
    x = a | b;
  end
endmodule
```

#### What’s wrong?
- The order of assignments causes `d` to use the old value of `x`—not the newly computed value.
- **Best Practice:** Assign intermediate variables before using them.

**Corrected order:**
```verilog
always @ (*) begin
  x = a | b;
  d = x & c;
end
```

 <div align="center">
  <img src="Images/blocking-caveat.png"  width="70%">
</div>

---

### Lab 8: Synthesis of the Blocking Caveat Module

Synthesize the corrected version of the module and observe the results.

 <div align="center">
  <img src="Images/synth-blocking-caveat.png"  width="70%">
</div>

---
### Lab 9: GLS of bloaking-caveat

Perform GLS on the `bad_mux`.  
Expect simulation mismatches or warnings due to above issues.

 <div align="center">
  <img src="Images/gls-caveat.png"  width="70%">
</div>

---

## ✨ Summary  

Day 4 was all about understanding how designs behave after synthesis and ensuring that what you simulate in RTL is the same as what ends up in hardware.  

- We began with **Gate-Level Simulation (GLS)**, a critical step that validates the gate-level netlist produced by synthesis. GLS not only checks functional correctness but also verifies timing (with real delays) and test structures like scan chains, ensuring the design is production-ready.  

- Next, we explored **synthesis-simulation mismatches**, which often arise from non-synthesizable constructs, ambiguous coding styles, or tool interpretation differences. The lesson here was clear: always use clean, synthesizable RTL and follow coding best practices to avoid surprises later in the flow.  

- Finally, we studied **blocking vs non-blocking assignments in Verilog**, two fundamental concepts that directly affect whether hardware is inferred as combinational or sequential. Correct usage of these assignments ensures predictable behavior, especially in clocked designs.  

**Overall takeaway:** Day 4 emphasized the importance of writing RTL that not only functions in simulation but also translates accurately into real hardware. By mastering GLS, avoiding mismatches, and using assignments correctly, you strengthen your ability to design circuits that are both reliable and synthesis-friendly.  


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day4/Images/Readme.md

contain only images


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day5/read.md


# Day 5 – Optimization in Synthesis

**Author:** Jaynandan Kushwaha

## 📌 Introduction

Day 5 focuses on the **optimization phase of synthesis**, where we refine coding techniques to achieve efficient hardware implementation. The day emphasizes how conditional constructs like **if** and **case** statements impact synthesized logic and how incomplete specifications can lead to unintended hardware such as latches.

We then move into the subtleties of **overlapping case constructs**, examining how synthesis tools interpret them and how to avoid mismatches between simulation and implementation. Finally, we explore the use of **for loops and generate statements**, powerful constructs that enhance code reusability and scalability, while also observing how synthesis tools optimize them.

This day is all about writing RTL that is not only functionally correct but also **optimized for synthesis, area, timing, and power**.

---

## 📚 Contents

### 🔹 1. If Case Constructs

* 📖 **Lecture 1:** IF Case Constructs – Part 1
* 📖 **Lecture 2:** IF Case Constructs – Part 2
* 📖 **Lecture 3:** IF Case Constructs – Part 3

### 🔹 2. Incomplete IF Case

* 🧩 **Lab 1:** Incomplete IF – Part 1
* 🧩 **Lab 2:** Incomplete IF – Part 2

### 🔹 3. Incomplete Overlapping Case

* 🧩 **Lab 1:** Incomplete Overlapping Case – Part 1
* 🧩 **Lab 2:** Incomplete Overlapping Case – Part 2
* 🧩 **Lab 3:** Incomplete Overlapping Case – Part 3
* 🧩 **Lab 4:** Incomplete Overlapping Case – Part 4

### 🔹 4. For Loop and For Generate

* 📖 **Lecture 1:** For Loop and For Generate – Part 1
* 📖 **Lecture 2:** For Loop and For Generate – Part 2
* 📖 **Lecture 3:** For Loop and For Generate – Part 3

### 🔹 5. Labs on For Loop and For Generate

* 🧩 **Lab 1:** For Loop and For Generate – Part 1
* 🧩 **Lab 2:** For Loop and For Generate – Part 2
* 🧩 **Lab 3:** For Loop and For Generate – Part 3

---

## ✨ Key Takeaways

* Correct usage of **if** and **case** constructs prevents unintended latch inference.
* Understanding incomplete and overlapping conditions is essential for **simulation-synthesis consistency**.
* **For loops** and **generate statements** improve modularity and reusability, while being efficiently optimized by synthesis tools.
* Optimization is not just about functionality—it’s about writing RTL that is **clean, efficient, and scalable**.

## Labs

### 1 Incomplete_if 

```verilog
module incomp_if (input i0 , input i1 , input i2 , output reg y);
always @ (*)
begin
	if(i0)
		y <= i1;
end
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-incomp-if.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-if.png" width="70%">
</div>

###  2 Incomplete_if2
```verilog
module incomp_if2 (input i0 , input i1 , input i2 , input i3, output reg y);
always @ (*)
begin
	if(i0)
		y <= i1;
	else if (i2)
		y <= i3;

end
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-incom-if2.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-incomp-if2.png" width="70%">
</div>

### 3 Incomp-Case
```verilog
module incomp_case (input i0 , input i1 , input i2 , input [1:0] sel, output reg y);
always @ (*)
begin
	case(sel)
		2'b00 : y = i0;
		2'b01 : y = i1;
	endcase
end
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-incomp-case.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-incomp-case.png" width="70%">
</div>

### 4 Complete_Caase
```verilog
module comp_case (input i0 , input i1 , input i2 , input [1:0] sel, output reg y);
always @ (*)
begin
	case(sel)
		2'b00 : y = i0;
		2'b01 : y = i1;
		default : y = i2;
	endcase
end
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-comp-case.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-comp-case.png" width="70%">
</div>

### 5 Partial Case Assign
```verilog
module partial_case_assign (input i0 , input i1 , input i2 , input [1:0] sel, output reg y , output reg x);
always @ (*)
begin
	case(sel)
		2'b00 : begin
			y = i0;
			x = i2;
			end
		2'b01 : y = i1;
		default : begin
		           x = i1;
			   y = i2;
			  end
	endcase
end
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-partial-case.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-partial-case.png" width="70%">
</div>

### 6 Bad Case

```verilog
module bad_case (input i0 , input i1, input i2, input i3 , input [1:0] sel, output reg y);
always @(*)
begin
	case(sel)
		2'b00: y = i0;
		2'b01: y = i1;
		2'b10: y = i2;
		2'b1?: y = i3;
		//2'b11: y = i3;
	endcase
end

endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-bad-case.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-bad-case.png" width="70%">
</div>

#### .GLS Output 
<div align="center">
  <img src="Images/gls-bad-case.png" width="70%">
</div>

### 7 mux_ Genrated 

```verilog
module mux_generate (input i0 , input i1, input i2 , input i3 , input [1:0] sel  , output reg y);
wire [3:0] i_int;
assign i_int = {i3,i2,i1,i0};
integer k;
always @ (*)
begin
for(k = 0; k < 4; k=k+1) begin
	if(k == sel)
		y = i_int[k];
end
end
endmodule


```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-mux-generate.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-generated-mux.png" width="70%">
</div>

#### .GLS Output 
<div align="center">
  <img src="Images/gls-mux-generated.png" width="70%">
</div>

### 8 demux case

```verilog
module demux_case (output o0 , output o1, output o2 , output o3, output o4, output o5, output o6 , output o7 , input [2:0] sel  , input i);
reg [7:0]y_int;
assign {o7,o6,o5,o4,o3,o2,o1,o0} = y_int;
integer k;
always @ (*)
begin
y_int = 8'b0;
	case(sel)
		3'b000 : y_int[0] = i;
		3'b001 : y_int[1] = i;
		3'b010 : y_int[2] = i;
		3'b011 : y_int[3] = i;
		3'b100 : y_int[4] = i;
		3'b101 : y_int[5] = i;
		3'b110 : y_int[6] = i;
		3'b111 : y_int[7] = i;
	endcase

end
endmodule

```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-demux-case.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-demux-case.png" width="70%">
</div>

#### .GLS Output 
<div align="center">
  <img src="Images/gls-demux-case.png" width="70%">
</div>

### 9 demux generated

```verilog
module demux_generate (output o0 , output o1, output o2 , output o3, output o4, output o5, output o6 , output o7 , input [2:0] sel  , input i);
reg [7:0]y_int;
assign {o7,o6,o5,o4,o3,o2,o1,o0} = y_int;
integer k;
always @ (*)
begin
y_int = 8'b0;
for(k = 0; k < 8; k++) begin
	if(k == sel)
		y_int[k] = i;
end
end
endmodule

```
#### .Gtkwave Output

<div align="center">
  <img src="Images/gtk-demux-generated.png" width="70%">
</div>

#### .Synthesis Output 

<div align="center">
  <img src="Images/synth-demux-generated.png" width="70%">
</div>

#### .GLS Output 
<div align="center">
  <img src="Images/gls-demux-generated.png" width="70%">
</div>

### RCA 

```verilog
FA.v
module fa (input a , input b , input c, output co , output sum);
	assign {co,sum}  = a + b + c ;
endmodule
 RCA.v
module rca (input [7:0] num1 , input [7:0] num2 , output [8:0] sum);
wire [7:0] int_sum;
wire [7:0]int_co;

genvar i;
generate
	for (i = 1 ; i < 8; i=i+1) begin
		fa u_fa_1 (.a(num1[i]),.b(num2[i]),.c(int_co[i-1]),.co(int_co[i]),.sum(int_sum[i]));
	end

endgenerate
fa u_fa_0 (.a(num1[0]),.b(num2[0]),.c(1'b0),.co(int_co[0]),.sum(int_sum[0]));


assign sum[7:0] = int_sum;
assign sum[8] = int_co[7];
endmodule
```
#### .Gtkwave Output

<div align="center">
  <img src="Images/rca.png" width="70%">
</div>

### Note:- All generating steps are in lab1 for how to run yosys iverilog tool i just use them to complete these lab 
for generating gls output we use iverilog tool with special library 
for example generating gls gtkwave for bad_mux :
```command

iverilog ../my_lib/verilog_model/primitive.v ../my_lib/verilog_model/sky130_fd_sc_hd.v bad_mux_net.v tb_bad_mux.v
```
and for writing .net file
when we synthesise before show in yosys we will use command this to generate netlist:
``` command
write_verilog  bad_mux_net.v

```
and it will write netlist and use this netlist file in iverilog for generating gls 


---

# /mnt/data/silicon_repo/silicon-diary-main/Week1/Day5/Images/read.md

this is for images



# Week 2

# /mnt/data/silicon_repo/silicon-diary-main/Week 2/Readme.md


# 🚀 Week 2 — BabySoC Fundamentals & Functional Modelling  

Welcome to **Week 2 Research**!  
This week, we zoom into the **fundamentals of BabySoC design** and explore how **functional modelling** helps us translate theory into working prototypes.  

Think of BabySoC as the “miniature DNA of a chip” — small, simple, yet powerful enough to demonstrate how **processors, memory, and interconnects** interact.  
Here, we’re not just studying block diagrams — we’re building intuition on **how ideas turn into models** and eventually real hardware. 🌟  

---

## 📑 Contents  
📘 About Week 2  
🛠️ Prerequisites  
📂 Research & Lab Roadmap  
🎯 Learning Outcomes  
🙏 Acknowledgements  

---

## 📘 About Week 2  

This module is designed to give you a strong **conceptual foundation** of SoC architecture while teaching you how to **model functionality** step by step.  

You’ll explore:  
- 🔹 **BabySoC architecture basics** (building blocks, data/control flow)  
- 🔹 Abstraction levels in SoC design  
- 🔹 Translating **theory → functional models**  
- 🔹 Applications of functional modelling in **verification and early design exploration**  

---

## 🛠️ Prerequisites  

Before diving in, make sure you’re comfortable with:  
- ✅ Basics of digital logic (mux, flip-flops, datapath control)  
- ✅ Introductory SoC concepts (CPU, memory, I/O)  
- ✅ Installed tools (recommended):  
  - Verilog simulator (Icarus Verilog / Verilator)  
  - Python/Matlab (for high-level modelling)  
  - GTKWave (for visualization)  

💡 *Tip: If Week 1 was about “knowing the language” (RTL), Week 2 is about “thinking in systems.”*  

---

## 📂 Research & Lab Roadmap  

This week is structured in two major parts:  

📅 Part	📝 Focus Area	🔗 Link  
1️⃣	**Theory (Conceptual Understanding)** → BabySoC fundamentals, SoC abstraction levels, mapping specifications to models	`Part1-Theory`  
2️⃣	**Hands-on Functional Modelling** → Building a BabySoC functional model, exploring interactions, running basic experiments	`Part2-FunctionalModelling`  

🔎 Each part includes:  
✔️ Concept notes with clear diagrams  
✔️ Hands-on modelling exercises  
✔️ Step-by-step workflows for BabySoC  
✔️ Reflections connecting **Week 1 RTL basics → Week 2 system-level thinking**  

---

## 🎯 Learning Outcomes  

By the end of Week 2, you will:  
- 🧠 Understand **BabySoC architecture** and its functional layers  
- 🛠️ Model the **behavior of a simplified SoC**  
- 🔄 Bridge the gap between **conceptual theory & implementation**  
- 🚀 Prepare for Week 3, where we move into **deeper RTL integration**  

---

## 🙏 Acknowledgements  

This research builds on the efforts of the **open-source VLSI community**:  

👨‍💻 Kunal Ghosh (VSDI)  
🛠️ Open-source ecosystem: Sky130 PDK, Icarus Verilog, Verilator  
📘 Collaborative learners & contributors shaping BabySoC insights  

✨ *“Every SoC starts as a simple model — mastering functional modelling is your first step to becoming a chip architect.”* ✨  

---

**Author:** *jaynandan-kushwaha*  


---

# /mnt/data/silicon_repo/silicon-diary-main/Week 2/Practical/Readme.md

# 🧪 VSDBabySoC – Lab Process Documentation  

This document captures the **lab workflow** for building, simulating, and analyzing the **VSDBabySoC** project.  
It serves as a guide for students, researchers, and hobbyists who want to practically explore **RISC-V SoC design** with **PLL** and **DAC integration** on **Sky130 open-source PDK**.  

---

## 📌 Objectives  

- Understand the **design flow of an SoC** with digital and analog IPs.  
- Integrate **RVMYTH CPU**, **PLL**, and **DAC** into a single system.  
- Learn how **clock synchronization** and **digital-to-analog conversion** are verified.  
- Perform **simulation, waveform analysis, and output validation**.  

---
## ⚙️ BabySoC Design Modules

The **VSDBabySoC** is built by integrating three open-source IPs into one compact SoC:  
1. A **RISC-V Core (RVMYTH)**  
2. A **Phase-Locked Loop (PLL)**  
3. A **Digital-to-Analog Converter (DAC)**  

Each of these modules plays a crucial role in achieving a fully functional **digital-to-analog educational SoC**.

---

### 🔹 2.1 vsdbabysoc.v (Top-Level SoC Module)

The `vsdbabysoc.v` file is the heart of the design — it brings together the CPU, PLL, and DAC into one top-level system.  
👉 Source: [VSDBabySoC GitHub Repo](https://github.com/manili/VSDBabySoC.git)  

- **Inputs**  
  - `reset`: Resets the RISC-V processor.  
  - `VCO_IN, ENb_CP, ENb_VCO, REF`: Control and reference signals for the PLL.  
  - `VREFH`: Reference voltage for the DAC.  

- **Outputs**  
  - `OUT`: The final analog output from DAC.  

- **Internal Connections**  
  - `RV_TO_DAC`: A 10-bit bus carrying RVMYTH’s output into the DAC.  
  - `CLK`: Stable clock generated by the PLL.  

✨ This is the **integration point** where digital logic meets clock synchronization and analog conversion.  

---

### 🔹 2.2 rvmyth.v (RISC-V Core)

The `rvmyth.v` module is a lightweight, educational **RISC-V CPU core**. It acts as the brain of the BabySoC, processing instructions and producing digital data for the DAC.  
👉 Source: [RVMYTH GitHub Repo](https://github.com/kunalg123/rvmyth/)  

- **Inputs**  
  - `CLK`: Clock input generated by PLL.  
  - `reset`: Resets/initializes the processor.  

- **Outputs**  
  - `OUT`: A 10-bit processed digital value that is fed into the DAC.  

✨ Think of it as the **data generator** — sequential values, instructions, or signals produced by RVMYTH become the basis of the analog waveform at the output.  

---

### 🔹 2.3 avsdpll.v (PLL Module)

The `avsdpll.v` module provides a **stable, synchronized clock** for the entire SoC. Without it, timing mismatches could break communication between the CPU and DAC.  
👉 References: [PLL Intro](https://github.com/ireneann713/PLL.git), [avsdpll Repo](https://github.com/lakshmi-sathi/avsdpll_1v8.git)  

- **Inputs**  
  - `VCO_IN, ENb_CP, ENb_VCO, REF`: Control/reference signals for PLL operation.  

- **Output**  
  - `CLK`: A clean, synchronized system clock.  

✨ The PLL ensures **all blocks work in harmony** by eliminating jitter and aligning phases.  

---

### 🔹 2.4 avsddac.v (DAC Module)

The `avsddac.v` module converts the **10-bit digital stream** from RVMYTH into a continuous **analog output signal**.  
👉 Source: [avsddac Repo](https://github.com/vsdip/rvmyth_avsddac_interface.git)  

- **Inputs**  
  - `D`: 10-bit digital data input from RVMYTH.  
  - `VREFH`: Reference voltage for scaling the DAC output.  

- **Output**  
  - `OUT`: Analog waveform output.  

✨ This is where the magic happens — digital binary values finally become a **real-world analog signal** (for sound, video, etc.).  

---

## 🧪 Testbench  

The `testbench.v` file validates the integration and functionality of the entire BabySoC.  

- **Features**  
  - Initializes signals (reset, clocks, inputs).  
  - Generates reference clock for PLL.  
  - Dumps waveforms for analysis.  

- **Outputs**  
  - `pre_synth_sim.vcd` → Simulation before synthesis.  
  - `post_synth_sim.vcd` → Simulation after synthesis with gate-level netlist.  

✨ Using **GTKWave**, you can visualize:  
- PLL clock stabilization.  
- RVMYTH register updates.  
- DAC output signal evolution.  

---
 


## 🛠️ Tools & Environment  

- **Operating System:** Ubuntu 20.04 / 22.04 (Linux recommended)  
- **Dependencies:**  
  - `make`  
  - `python3`, `pip3`  
  - `git`  
  - `iverilog` (for RTL simulation)  
  - `gtkwave` (for waveform visualization)  
  - `docker` (for reproducible environments)  

## Step by step all simulation process and its outputs 

In this section we will walk through the whole process of modeling the VSDBabySoC in details.

  #### 1. First we need to install some important packages:

  ```
   sudo apt install make python python3 python3-pip git iverilog gtkwave docker.io
   sudo chmod 666 /var/run/docker.sock
   cd ~
   pip3 install pyyaml click sandpiper-saas
  ```

  #### 2. Now we can clone this repository in an directory:
Clone or set up the directory structure as follows:
  ```
   cd ~
   git clone https://github.com/manili/VSDBabySoC.git
  ```
```
VSDBabySoC/
├── src/
│   ├── include/
│   │   ├── sandpiper.vh
│   │   └── other header files...
│   ├── module/
│   │   ├── vsdbabysoc.v      # Top-level module integrating all components
│   │   ├── rvmyth.v          # RISC-V core module
│   │   ├── avsdpll.v         # PLL module
│   │   ├── avsddac.v         # DAC module
│   │   └── testbench.v       # Testbench for simulation
└── output/
└── compiled_tlv/         # Holds compiled intermediate files if needed
```
#### 3. Verify Tool Installation

   ```
   iverilog -v
   gtkwave --version
   ```
#### 4. Pre-Synthesis Simulation
It's time to make the `pre_synth_sim.vcd`:
 ```
  cd VSDBabySoC
  make pre_synth_sim
or
iverilog -o output/pre_synth_sim/pre_synth_sim.out -DPRE_SYNTH_SIM \
    -I src/include -I src/module \
    src/module/testbench.v src/module/vsdbabysoc.v
cd output/pre_synth_sim
./pre_synth_sim.out
  ```
  The result of the simulation (i.e. `pre_synth_sim.vcd`) will be stored in the `output/pre_synth_sim` directory.
We can see the waveforms by following command:

  ```
  $ gtkwave output/pre_synth_sim/pre_synth_sim.vcd
  ```
  
#### 🔎 Simulation Results

During the simulation, two of the most important signals to observe are **`CLK`** and **`OUT`**.  
- The **`CLK`** signal is generated by the **PLL** and serves as the input clock for the RVMYTH core.  
- The **`OUT`** signal is produced by the **DAC**, representing the analog output of the SoC.  

Here is the final waveform result of the modeling process:

![pre_synth_sim](Images/presynth.png)

#### 🧩 Observation from Pre-Synthesis Simulation

The above waveform illustrates the **pre-synthesis simulation** of the `VSDBabySoC` design.  
This simulation is performed before synthesis to verify the logical correctness of the RTL (Register Transfer Level) design.  
It ensures that the Verilog modules for the processor, PLL, and DAC interact correctly before being converted into a gate-level netlist.

---

#### 🔍 Signal Analysis

- **CLK:**  
  Represents the input clock signal driving the system.  
  The waveform shows a uniform and continuous clock pulse, confirming proper clock generation and propagation to all submodules.

- **reset:**  
  Used to initialize the entire SoC into a known state.  
  At the beginning of the simulation, it is asserted high to clear all registers and memory locations. Once de-asserted, normal operation begins.

- **RV_TO_DAC[9:0]:**  
  This 10-bit bus transmits data from the `RVMYTH` processor to the `DAC` module.  
  The changing values in hexadecimal (e.g., 001, 003, 006, 00A, 00F, 015, 01C, etc.) indicate sequential digital output from the RVMYTH register (`x17`), which is continuously updated each clock cycle.  
  This confirms correct data transfer between the processor and DAC.

- **OUT:**  
  Represents the DAC output signal, which models an analog output using a `real` datatype in RTL simulation.  
  Since this is a pre-synthesis run, the analog behavior can still be observed, reflecting how the digital values from `RV_TO_DAC[9:0]` are converted into analog-like waveform responses.

---

#### 💡 Key Insight

From this pre-synthesis simulation:
- The design’s **functional correctness** at the RTL level is verified.  
- The **RVMYTH processor**, **PLL**, and **DAC** modules communicate properly.  
- The **data flow from digital to analog** is clearly visible through the changing `RV_TO_DAC` and `OUT` signals.  
- The **clock and reset behavior** is stable, ensuring reliable synchronization across the SoC.

---

#### ✅ Conclusion

The pre-synthesis simulation confirms that the RTL description of `VSDBabySoC` behaves as expected.  
All functional blocks — including the **RVMYTH core**, **PLL**, and **DAC** — are correctly interconnected and operational.  
This successful simulation establishes a solid foundation for proceeding to the synthesis stage, where the RTL design will be transformed into a gate-level netlist while preserving this verified functionality.

---

#### pre simulation logs

#### **before post synthesis we need to download OpenLane tool** 

this picture will show pre synthesis log of simulation
![pre_log](Images/logpre.png)

---
### OpenLANE installation

The OpenLANE and sky130 installation can be done by following the steps in this repository `https://github.com/nickson-jose/openlane_build_script`.
Comaand to download the openlane tool

  ```
  $ git clone https://github.com/The-OpenROAD-Project/OpenLane.git
  $ cd OpenLane/
  $ make openlane
  $ make pdk
  $ make test
  ```

---

### ⚙️ Synthesis and Post-Synthesis Simulation



The **first step in the design flow** is to synthesize the generated RTL code.  
Once synthesis is complete, we perform **post-synthesis simulation** to verify the correctness of the design.

This step is crucial because it allows us to:  
- Validate that the synthesized netlist behaves the same as the RTL description.  
- Detect any potential mismatches, optimization effects, or bugs introduced during synthesis.  
- Ensure that the design remains functionally consistent before moving to the physical implementation stage.  

Both **pre-synthesis (RTL level)** and **post-synthesis (gate-level)** simulation results should be **identical**.  
If differences appear, it typically indicates either:  
- RTL coding issues (such as uninitialized registers, improper blocking/non-blocking usage), or  
- Constraints not being met during synthesis.  

By confirming identical behavior, we establish confidence that our RTL description is robust and ready for further steps in the SoC design flow.

To run a post-synthesis simulation, use:
```tcl
iverilog -o output/post_synth_sim/post_synth_sim.out -DPOST_SYNTH_SIM \
    -I src/include -I src/module \
    src/module/testbench.v output/synthesized/vsdbabysoc.synth.v
cd output/post_synth_sim
./post_synth_sim.out
```
User could bypass these confusing steps by using our provided Makefile:

  ```
   cd ~/VSDBabySoC
   make post_synth_sim
  ```
The result of the simulation (i.e. `post_synth_sim.vcd`) will be stored in the `output/post_synth_sim` directory and the waveform could be seen by the following command:

  ```
   gtkwave output/post_synth_sim/post_synth_sim.vcd
  ```
Here is the final result:

  ![post_synth_sim](Images/postsynth.png)
  
---

#### 🧩 Observation from Post-Synthesis Simulation

The above waveform represents the **post-synthesis simulation** of the `VSDBabySoC` design, where the synthesized netlist was simulated to verify its behavior.  
The simulation confirms that the synthesized design maintains the same logical behavior as the RTL model, validating the correctness of the synthesis process.

---

#### 🔍 Signal Analysis

- **CLK:**  
  The clock signal generated by the PLL, providing a stable and high-frequency reference to synchronize all modules.  
  The waveform shows a consistent, periodic clock pattern, indicating that the PLL is functioning correctly.

- **reset:**  
  The reset signal initializes the RVMYTH processor.  
  Initially asserted, it ensures all registers and components are set to a known state before normal operation begins.

- **\core.CLK:**  
  This is the clock input of the `RVMYTH` core, derived directly from the PLL output.  
  Its continuous toggling throughout the simulation confirms correct clock distribution within the SoC.

- **OUT (SoC Level):**  
  Represents the DAC’s analog output at the SoC level.  
  In the post-synthesis simulation, it behaves as a digital signal because synthesis tools do not support analog (`real`) datatypes.  
  The waveform transitions indicate that the DAC is correctly receiving digital data from the processor.

- **\core.OUT[9:0]:**  
  This 10-bit bus carries digital data from the RVMYTH core’s register (specifically register `x17`) to the DAC.  
  The hexadecimal values (e.g., 000, 011, 080, 0A8, 0E7, etc.) represent sequential digital outputs, showing how the processor continuously updates data for digital-to-analog conversion.

---

#### 💡 Key Insight

The simulation waveform verifies:
- Proper **clock synchronization** across the entire SoC via the PLL.  
- Successful **data transfer** between the RVMYTH core and the DAC.  
- Correct **digital-to-analog conversion pipeline**, even though the final analog behavior is approximated in digital form due to synthesis constraints.

---

#### ✅ Conclusion

The post-synthesis simulation results confirm the successful integration of all three modules — **RVMYTH**, **PLL**, and **DAC** — within the `VSDBabySoC`.  
The output waveforms demonstrate stable operation, correct timing, and accurate data flow, indicating that the design is ready for further verification and physical implementation stages.

---

### ⚠️ Key Limitation
A critical observation is that **post-synthesis simulations cannot directly handle `real` datatype signals**.  
- Therefore, the `OUT` port at the SoC level is modeled as a digital `wire`.  
- This means that while the DAC’s internal `OUT` shows analog behavior, the top-level SoC output is restricted to a digital approximation.  

---

### Post simulation logs 

yosys simulation logs 
 ![synth_post](Images/logsynthpost.png)

 gtkwave simulation log

  ![post_synth_sim](Images/loggtkpost.png)

  ---

### Yosys synthesis output 

```
13. Printing statistics.

=== vsdbabysoc ===

   Number of wires:               4737
   Number of wire bits:           6211
   Number of public wires:        4737
   Number of public wire bits:    6211
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:               5913
     avsddac                         1
     avsdpll                         1
     sky130_fd_sc_hd__a2111oi_0      5
     sky130_fd_sc_hd__a211oi_1      10
     sky130_fd_sc_hd__a21boi_0       4
     sky130_fd_sc_hd__a21o_2         3
     sky130_fd_sc_hd__a21oi_1      686
     sky130_fd_sc_hd__a221oi_1     168
     sky130_fd_sc_hd__a22o_2         4
     sky130_fd_sc_hd__a22oi_1      137
     sky130_fd_sc_hd__a311oi_1       4
     sky130_fd_sc_hd__a31o_2         1
     sky130_fd_sc_hd__a31oi_1      315
     sky130_fd_sc_hd__a32oi_1        1
     sky130_fd_sc_hd__a41oi_1       17
     sky130_fd_sc_hd__and2_2        12
     sky130_fd_sc_hd__and3_2         1
     sky130_fd_sc_hd__clkinv_1     568
     sky130_fd_sc_hd__dfxtp_1     1144
     sky130_fd_sc_hd__lpflow_inputiso0p_1      1
     sky130_fd_sc_hd__mux2i_1       14
     sky130_fd_sc_hd__nand2_1      852
     sky130_fd_sc_hd__nand3_1      258
     sky130_fd_sc_hd__nand3b_1       1
     sky130_fd_sc_hd__nand4_1       53
     sky130_fd_sc_hd__nor2_1       428
     sky130_fd_sc_hd__nor3_1        42
     sky130_fd_sc_hd__nor4_1         3
     sky130_fd_sc_hd__o2111ai_1     24
     sky130_fd_sc_hd__o211ai_1      62
     sky130_fd_sc_hd__o21a_1        12
     sky130_fd_sc_hd__o21ai_0      856
     sky130_fd_sc_hd__o21bai_1      12
     sky130_fd_sc_hd__o221a_2        1
     sky130_fd_sc_hd__o221ai_1       3
     sky130_fd_sc_hd__o22a_2         1
     sky130_fd_sc_hd__o22ai_1      135
     sky130_fd_sc_hd__o311ai_0       3
     sky130_fd_sc_hd__o31a_2         1
     sky130_fd_sc_hd__o31ai_1        4
     sky130_fd_sc_hd__o32ai_1        1
     sky130_fd_sc_hd__o41ai_1        2
     sky130_fd_sc_hd__or2_2         12
     sky130_fd_sc_hd__xnor2_1       16
     sky130_fd_sc_hd__xor2_1        34

14. Executing Verilog backend.
```

```
.25. Printing statistics.

=== clk_gate ===

   Number of wires:                  5
   Number of wire bits:              5
   Number of public wires:           5
   Number of public wire bits:       5
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  0

=== rvmyth ===

   Number of wires:               3948
   Number of wire bits:           6635
   Number of public wires:         269
   Number of public wire bits:    2941
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:               5165
     $_ANDNOT_                    1412
     $_AND_                        174
     $_DFF_P_                      239
     $_MUX_                        513
     $_NAND_                        42
     $_NOR_                         99
     $_NOT_                         49
     $_ORNOT_                       74
     $_OR_                        1322
     $_SDFFE_PP0P_                 962
     $_SDFFE_PP1P_                  64
     $_SDFF_PP0_                     8
     $_XNOR_                        71
     $_XOR_                        129
     clk_gate                        7

=== vsdbabysoc ===

   Number of wires:                  9
   Number of wire bits:             18
   Number of public wires:           9
   Number of public wire bits:      18
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:                  3
     avsddac                         1
     avsdpll                         1
     rvmyth                          1

=== design hierarchy ===

   vsdbabysoc                        1
     rvmyth                          1
       clk_gate                      7

   Number of wires:               3992
   Number of wire bits:           6688
   Number of public wires:         313
   Number of public wire bits:    2994
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:               5160
     $_ANDNOT_                    1412
     $_AND_                        174
     $_DFF_P_                      239
     $_MUX_                        513
     $_NAND_                        42
     $_NOR_                         99
     $_NOT_                         49
     $_ORNOT_                       74
     $_OR_                        1322
     $_SDFFE_PP0P_                 962
     $_SDFFE_PP1P_                  64
     $_SDFF_PP0_                     8
     $_XNOR_                        71
     $_XOR_                        129
     avsddac                         1
     avsdpll                         1

7.26. Executing CHECK pass (checking for obvious problems).
```

for simulation logs 

---

## 🙏 Acknowledgment

I would like to express my sincere gratitude to the **VLSI System Design (VSD) community** and **Kunal Ghosh** for providing such an insightful and hands-on learning platform.  
The BabySoC project offered me a deep understanding of how a real **System-on-Chip (SoC)** integrates multiple components like **PLL**, **DAC**, and a **RISC-V processor core** into a cohesive hardware system.  

Special thanks to the mentors and open-source contributors whose continuous efforts make advanced semiconductor design accessible to learners worldwide.  
Their guidance and open resources have not only enhanced my technical skills but also strengthened my passion for **VLSI design and research**.

---

## ✍️ Author

**Name:** Jaynandan Kushwaha  
**Domain:** VLSI and Semiconductor Design Enthusiast  
**Focus Areas:** RISC-V, SoC Design, RTL Synthesis, and Digital Circuit Optimization  
**GitHub:** [jaynandan-kushwaha](https://github.com/jaynandan-kushwaha)  

---

## 🌟 Conclusion — End of Week 2

Week 2 marked a significant step forward in understanding the **synthesis and simulation flow** of a real SoC design.  
Through the BabySoC experiment, I explored how RTL design translates into a gate-level representation while maintaining identical functionality between **pre-synthesis** and **post-synthesis** simulations.  

Observing clean and stable waveforms reaffirmed that the design was logically and structurally sound — a crucial validation before moving toward **physical design** and **timing analysis**.  

With this milestone, Week 2 concludes with a sense of accomplishment and curiosity — a reminder that every synthesized signal and simulated waveform brings us one step closer to bridging **digital logic** with **real silicon**.

---

> “Every great chip starts as a few lines of Verilog — and every simulation waveform tells a story of logic coming to life.” 🧠⚙️



---

# /mnt/data/silicon_repo/silicon-diary-main/Week 2/Practical/Images/readme.md

for images


---

# /mnt/data/silicon_repo/silicon-diary-main/Week 2/Theory/Readme.md

# 🚀 BabySoC – Learning SoC Design with RVMYTH, PLL, and DAC

## 📝 Problem Statement  
This project focuses on building a compact, educational **System on Chip (SoC)** based on **RVMYTH**, a simple RISC-V processor core.  
To make it more realistic, BabySoC integrates:  

- **Phase-Locked Loop (PLL)** → For generating stable, high-frequency clocks.  
- **10-bit Digital-to-Analog Converter (DAC)** → To bridge the digital and analog worlds.  

By converting digital signals into analog form, the DAC enables BabySoC to interact with external devices like **monitors, televisions, and mobile systems**, where the outputs could represent **audio or video signals**.  

The design is implemented on **Sky130 technology** and aims to serve as an **open-source, beginner-friendly platform** for students, hobbyists, and engineers exploring **digital–analog integration in chip design**.  

---

## 🔎 1. What is a System on Chip (SoC)?  
A **System on Chip (SoC)** is essentially a **complete computer built on a single chip**.  
Instead of having separate chips for the processor, memory, and peripherals, an SoC brings them all together into a **compact unit**.  

This makes SoCs ideal for modern devices where **performance, power efficiency, and space** are all critical.  
From smartphones to smartwatches and IoT devices, SoCs are the reason our technology is both **powerful and portable**.  

---

## 🧩 2. Key Components of an SoC  

- **CPU (Central Processing Unit)** → The “brain” of the chip; executes instructions, calculations, and controls overall operation.  
- **Memory** →  
  - RAM stores temporary data while programs run.  
  - ROM/Flash provides long-term storage for boot code and essential data.  
- **I/O Interfaces** → Connects the SoC to the outside world (USB, camera, sensors, audio jacks).  
- **GPU (Graphics Processing Unit)** → Handles image and video rendering for displays and games.  
- **DSP (Digital Signal Processor)** → Specialized for tasks like audio processing, filters, and signal enhancement.  
- **Power Management** → Ensures energy efficiency and extends battery life.  
- **Additional Blocks** → Wireless (Wi-Fi, Bluetooth), Security modules, Analog/Mixed-signal interfaces like DACs and ADCs.  

---

## 🏷️ 3. Types of SoCs  

Different SoCs are designed for different applications:  

1. **Microcontroller-based SoCs**  
   - Built around simple CPU cores with memory & peripherals.  
   - Used in IoT, sensors, and embedded systems.  
   - *Example:* ARM Cortex-M, ESP32.  

2. **Microprocessor-based SoCs**  
   - More powerful, capable of running Linux/Android.  
   - Used in smartphones & tablets.  
   - *Example:* Qualcomm Snapdragon, Samsung Exynos.  

3. **Application-Specific SoCs (ASoCs)**  
   - Tailored for high-performance, domain-specific tasks (AI, graphics, networking).  
   - *Example:* Google TPU (AI), NVIDIA Tegra (gaming/graphics).  

4. **Automotive SoCs**  
   - Designed for real-time, reliable operation in vehicles.  
   - *Example:* NVIDIA Drive, Renesas R-Car.  

5. **Multimedia SoCs**  
   - Optimized for audio, video, and display pipelines.  
   - *Example:* MediaTek SoCs in smart TVs.  

👉 **BabySoC** fits into the **Educational/Embedded SoC** category — designed for hands-on learning of CPU cores, clock generation, and digital-to-analog interfacing.  

---

## ⚡ 4. Why SoCs are Important  

- **Compact Design** → Combines multiple functions into one chip, saving board space.  
- **Energy Efficiency** → Reduced power consumption.  
- **Performance Boost** → Faster communication between tightly integrated modules.  
- **Cost-Effective** → Fewer external components reduce manufacturing cost.  
- **Reliability** → Fewer interconnections → fewer chances of failure.  

---

## 🌍 5. Applications of SoCs  

SoCs are used everywhere:  

- **Smartphones & Tablets** → Apple A-series, Qualcomm Snapdragon.  
- **Wearables** → Smartwatches with ultra-low-power SoCs.  
- **IoT Devices** → Smart home sensors & controllers.  
- **Consumer Electronics** → Televisions, gaming consoles, cars.  

---

## 🚧 6. Challenges in SoC Design  

- **Complexity** → Many integrated blocks increase design difficulty.  
- **Thermal Issues** → High integration = heating problems.  
- **Limited Flexibility** → Once fabricated, cannot be easily changed.  

---

## 🎯 In Summary  

A **System on Chip** combines multiple computing and communication blocks into a single silicon platform — making devices **smaller, faster, efficient, and cost-effective**.  

**BabySoC** represents a **learning-friendly SoC** by combining:  

- 🖥️ **RISC-V CPU (RVMYTH)** → Digital computation.  
- ⏱️ **PLL** → Stable high-speed clock management.  
- 🎚️ **DAC** → Digital-to-Analog conversion.  

## SoC Design Flow

<div align="center">
  <img src="Images/soc design flow.webp" alt="Testbench" width="70%">
</div>

# 🌱 VSDBabySoC – A Beginner-Friendly System-on-Chip Journey  

Welcome to **VSDBabySoC** – a compact yet powerful **System on Chip (SoC)** designed not just as a project, but as a **learning adventure** into the world of chip design.  

Built on the open-source **RISC-V architecture**, BabySoC brings together three essential building blocks:  
- 🖥️ **RVMYTH CPU** → the digital brain  
- ⏱️ **Phase-Locked Loop (PLL)** → the clock keeper  
- 🎚️ **10-bit DAC** → the digital-to-analog bridge  

Its primary goal is **simple yet ambitious**: to allow simultaneous testing of three open-source IP cores for the first time, while also calibrating and experimenting with analog components. Think of it as a **mini-laboratory on silicon** where digital logic meets real-world analog signals.  

---

## ✨ Why BabySoC?  
We live in a world where SoCs run **everything** – from smartphones to wearables, from TVs to cars. Yet, understanding how all those moving parts come together can feel overwhelming.  

BabySoC breaks it down into digestible building blocks:  
- A **RISC-V processor** (RVMYTH) for executing instructions and cycling through registers.  
- A **PLL** that generates clean, synchronized clocks to drive the CPU and peripherals.  
- A **DAC** that takes binary data and turns it into smooth analog waveforms (sound, light, video).  

---

## 🧩 BabySoC Components  

### 🔹 RVMYTH (RISC-V CPU)  
The **RVMYTH core** is the heart of BabySoC.  
- Based on the open-source RISC-V ISA.  
- Executes instructions, manages registers, and cycles through data.  
- For this project, values in **register r17** are prepared and sent to the DAC for conversion.  

It represents the **logic and decision-making hub** of the SoC.  

📌 **Block Diagram of CPU Core**  
![RVMYTH CPU Block Diagram](Images/babysoc.jpg)  

---

### 🔹 Phase-Locked Loop (PLL) – *The Clock Keeper*  
A **Phase-Locked Loop (PLL)** is a fundamental circuit in SoCs that ensures everything runs in rhythm.  

#### ⚙️ How PLL Works  
1. **Phase Detector (PD):** Compares the phase of the input clock (reference) with the output clock from the oscillator.  
2. **Loop Filter (LF):** Removes noise from the phase error signal, producing a smooth control voltage.  
3. **Voltage-Controlled Oscillator (VCO):** Adjusts its frequency based on the control voltage, ensuring the output frequency matches the reference.  
4. **Divider (optional):** Generates higher or lower multiples of the reference.  

The PLL works in a feedback loop, “locking” the output frequency and phase to the reference clock.  

📌 **Block Diagram of PLL**  
![PLL Block Diagram](Images/pll.png)  

---

### 🔹 Digital-to-Analog Converter (DAC) – *The Digital–Analog Bridge*  
A **DAC** converts binary values (0s and 1s) into real-world analog signals.  

#### ⚙️ How DAC Works  
1. **Digital Input:** A binary number (10 bits in BabySoC).  
2. **Conversion Circuit:** Uses resistor ladders (R-2R) or weighted resistors.  
3. **Analog Output:** A voltage/current proportional to the input value.  

#### 🔎 DAC Architectures  
- **Weighted Resistor DAC** – each bit has a weighted resistor (simple, but impractical at high resolution).  
- **R-2R Ladder DAC** – uses repeating resistors, scalable and stable.  

📌 **Block Diagram of DAC**  
![DAC Block Diagram](Images/dac.webp)  

---

## ⚙️ How BabySoC Works (Step by Step)  

1. **Initialization & Clocking**  
   - BabySoC receives an input clock.  
   - The **PLL multiplies and stabilizes** it.  
   - The synchronized clock feeds both CPU and DAC.  

2. **Data Processing with RVMYTH**  
   - The CPU executes instructions.  
   - Updates values in register **r17** with new data.  
   - Prepares digital values for conversion.  

3. **Digital-to-Analog Conversion**  
   - The DAC receives the digital values.  
   - Converts them into analog voltages.  
   - Output is written to a file (`OUT`) or connected to external devices.  

📌 **BabySoC Top-Level Block Diagram**  
![BabySoC Block Diagram](Images/topblock.png)  

👉 The end result: **Binary → Instructions → Registers → DAC → Analog Signals** 🎵📺  

---

💡 **BabySoC fits in the Educational/Embedded SoC category** — focused on teaching SoC design fundamentals and experimenting with digital–analog integration.  

---


## 🎯 In Summary  

- **VSDBabySoC** integrates:  
  - 🖥️ **RVMYTH CPU** (logic and control)  
  - ⏱️ **PLL** (stable timing)  
  - 🎚️ **DAC** (analog bridge)  

- It provides a hands-on platform to:  
  - Learn **SoC fundamentals**.  
  - Explore how **digital and analog worlds interact**.  
  - Experiment with **real, open-source IP cores**.  

✨ BabySoC isn’t just a circuit — it’s your **first step into the world of chip design**.  

---

👨‍💻 **Author:** Jaynandan Kushwaha

🔗 **Tech Stack:** RISC-V | Sky130 | PLL | DAC | Open-Source SoC  
📂 **Category:** Educational / Embedded SoC  


---

# /mnt/data/silicon_repo/silicon-diary-main/Week 2/Theory/Images/readme.md




# Week3 

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Readme.md


# 🚀 Week 3 — Post Synthesis GLS & STA Fundamentals

Welcome to **Week 3 Research!**  
This week, we dive into one of the most crucial phases of the VLSI design flow — **Post Synthesis Verification** and **Static Timing Analysis (STA)**.  

If Week 2 was about building functional models and system intuition, Week 3 is where we **validate and time the design** — ensuring that what we built behaves **logically and temporally correct** before tapeout. ⚙️  

We’ll explore how the synthesized netlist behaves through **Gate-Level Simulation (GLS)** and how timing constraints are analyzed and verified using **OpenSTA**.

---

## 📑 Contents
📘 About Week 3  
🛠️ Prerequisites  
📂 Research & Lab Roadmap  
🎯 Learning Outcomes  
🙏 Acknowledgements  

---

## 📘 About Week 3

This module focuses on understanding how **post-synthesis simulations and static timing analysis** form the backbone of reliable chip design.  

Through theory and practical labs, you’ll learn how synthesis transforms RTL into gates and how STA ensures every signal transition happens within timing limits.

You’ll explore:

🔹 What happens after synthesis — logic mapping, optimization, and timing impact  
🔹 Performing **Post Synthesis GLS (Gate-Level Simulation)**  
🔹 Fundamentals of **STA (Static Timing Analysis)**  
🔹 Generating and interpreting **timing graphs** using **OpenSTA**  
🔹 Understanding the link between **timing closure** and **design performance**

💡 *If Week 2 was about thinking in systems, Week 3 is about validating those systems under real hardware constraints.*

---

## 🛠️ Prerequisites

Before diving in, ensure you’re comfortable with:

✅ **Verilog RTL Design & Simulation** (Week 1 & 2 concepts)  
✅ **Synthesis tools** (Yosys or equivalent)  
✅ **Waveform Analysis using GTKWave**  
✅ Installed tools (recommended):
- Icarus Verilog / Verilator  
- Yosys (for synthesis)  
- OpenSTA (for timing analysis)  
- GTKWave (for post-synthesis waveform visualization)

💡 *Tip:* Keep your Week 2 BabySoC models ready — they form the perfect base to analyze post-synthesis behavior this week!

---

## 📂 Research & Lab Roadmap

This week is structured into **three major parts**, combining theory and hands-on exploration:

| 📅 Part | 📝 Focus Area | 🔗 Link |
|:--:|:--|:--|
| 1️⃣ | **Post Synthesis GLS** → Explore gate-level netlist simulation, understand how timing delays impact behavior | Part1-PostSynthesisGLS |
| 2️⃣ | **Fundamentals of STA (Static Timing Analysis)** → Learn how STA checks setup, hold, and path delays to ensure design reliability | Part2-FundamentalsOfSTA |
| 3️⃣ | **Generate Timing Graphs with OpenSTA** → Use OpenSTA to visualize and verify design timing through reports and timing graphs | Part3-TimingGraphsOpenSTA |

Each part includes:  
✔️ Concept walkthroughs  
✔️ Lab exercises with command flow  
✔️ Timing and waveform observations  
✔️ Practical STA checks for design signoff confidence  

---

## 🎯 Learning Outcomes

By the end of Week 3, you will:

🧠 Understand **Post Synthesis GLS flow** and its importance  
📈 Perform **Static Timing Analysis** to verify design timing integrity  
⚙️ Generate and interpret **timing reports** and **graphs** using OpenSTA  
💡 Correlate **synthesis results**, **functional correctness**, and **timing closure**  
🚀 Be ready for **Week 4**, where timing optimization and advanced synthesis techniques come into play  

---

## 🙏 Acknowledgements

This research module builds on the continued efforts of the **Open-Source VLSI Design Community** and contributors to open hardware education.

👨‍💻 **Kunal Ghosh (VSDI)**  
🛠️ Open-source tools: **Yosys**, **OpenSTA**, **GTKWave**, **Icarus Verilog**  
📘 Learners and developers contributing to open silicon design ecosystems  

✨ *“Synthesis gives structure, STA gives confidence — together, they define the readiness of silicon.”* ✨  

**Author:** *jaynandan-kushwah*


---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Images/Readme.md

this folder for part 1 post synthesis gls content by mistekn its creared outside of part 1 folder


---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Part 1 Post Synthesis GLS /Readme.md

# ⚙️ Part 1 — Post Synthesis GLS: “Bringing BabySoC to Life”

Welcome to **Part 1 of Week 3!** 🚀  
Up to now, your BabySoC has lived in the world of RTL — abstract, fast, and ideal.  
But in the real silicon world, wires have delays, gates have timing, and logic must keep up with the clock.  

This is where **Gate-Level Simulation (GLS)** steps in — it’s like giving your design its first **heartbeat** after synthesis.  
We move from ideal logic to the actual gate-level representation, ensuring that every flip-flop and signal transition behaves correctly when timing becomes real. 💡  

---

## 🧠 What Is GLS?

**Gate-Level Simulation (GLS)** is the stage where your synthesized design is tested in its true hardware form.  
After synthesis, your design turns into a **netlist** — a file describing how real logic gates are connected.  
GLS takes this netlist and runs simulations to verify that functionality is preserved **and** that timing behaves as expected.

Unlike RTL simulation:
- GLS includes **propagation delays** from real hardware.
- The testbench remains the same, but the underlying logic now mirrors **post-synthesis reality**.
- It helps detect issues that may not appear at the RTL level.

---

## 🔍 Why BabySoC Needs GLS

Your **BabySoC** integrates multiple modules — the RISC-V core, PLL, DAC, and more.  
Each has its own timing behavior and clock domain. GLS ensures that when these modules talk to each other, they **stay synchronized** and **stable** under real timing constraints.  

Here’s what GLS validates:
- ⏱️ **Timing Consistency:** Signals meet setup and hold times defined in the Standard Delay Format (SDF).  
- ⚡ **Functional Integrity:** The synthesized design still performs the intended operations.  
- 🧩 **Inter-Module Interaction:** No unexpected glitches or metastability during communication between components.

---

## 🧰 Tools You’ll Use

To bring your BabySoC to life at the gate level, you’ll work with:

- 🧠 **Icarus Verilog** — for compiling and simulating the gate-level netlist.  
- 🌈 **GTKWave** — for waveform visualization and debugging timing delays.  
- 📄 **SDF Files** — to inject real-world delay data into your simulations.  

These tools together allow you to view how your design transitions from **“logical correctness”** to **“hardware readiness.”**

---

## 🧭 The Real Purpose

Think of GLS as the **truth test** for synthesis.  
It answers one simple but critical question:

> “Does my design still behave correctly when it becomes hardware?”

When you see your BabySoC waveforms align perfectly under timing delays — that’s your moment of validation. ✨  

---

## 💬 In a Nutshell

> “Gate-Level Simulation is where your SoC stops being an idea and starts acting like a chip —  
> precise, timed, and ready for silicon.” ⚙️  

---

Here is the step-by-step execution plan for running the  commands manually:
---
### **Step 1: Load the Top-Level Design and Supporting Modules**
```bash
yosys
```

![Screenshot from ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/step1.png). 


Inside the Yosys shell, run:
```yosys
read_verilog /home/jaynandan/vsd/VLSI/VSDBabySoC/src/module/vsdbabysoc.v
read_verilog -sv -I /home/jaynandan/vsd/VLSI/VSDBabySoC/src/include /home/jaynandan/vsd/VLSI/VSDBabySoC/src/module/rvmyth.v
read_verilog -I /home/jaynandan/vsd/VLSI/VSDBabySoC/src/include /home/jaynandan/vsd/VLSI/VSDBabySoC/src/module/clk_gate.v

```
![Screenshot from ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/step1.png). 

---

### **Step 2: Load the Liberty Files for Synthesis**
Inside the same Yosys shell, run:
```yosys
read_liberty -lib  /home/jaynandan/vsd/VLSI/VSDBabySoC/src/lib/avsdpll.lib
read_liberty -lib  /home/jaynandan/vsd/VLSI/VSDBabySoC/src/lib/avsddac.lib
read_liberty -lib  /home/jaynandan/vsd/VLSI/VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-13-57.png)

---

### **Step 3: Run Synthesis Targeting `vsdbabysoc`**
```yosys
synth -top vsdbabysoc
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-13-57.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-14-47.png)
![WhatsApp Image )](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-14-55.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-15-02.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-15-10.png)


---

### **Step 4: Map D Flip-Flops to Standard Cells**
```yosys
dfflibmap -liberty /home/jaynandan/vsd/VLSI/VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```
![WhatsApp Image )](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-18-11.png)

---

### **Step 5: Perform Optimization and Technology Mapping**
```yosys
opt
abc -liberty /home/jaynandan/vsd/VLSI/VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -script +strash;scorr;ifraig;retime;{D};strash;dch,-f;map,-M,1,{D}
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-20-01.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-20-10.png)

---

### **Step 6: Perform Final Clean-Up and Renaming**
```yosys
flatten
setundef -zero
clean -purge
rename -enumerate
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-20-35.png)

---

### **Step 7: Check Statistics**
```yosys
stat
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-20-57.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-21-11.png)


---

### **Step 8: Write the Synthesized Netlist**
```yosys
write_verilog -noattr /home/jaynandan/vsd/VLSI/VSDBabySoC/output/post_synth_sim/vsdbabysoc.synth.v
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-22-20.png)

---

## POST_SYNTHESIS SIMULATION AND WAVEFORMS
---

### **Step 1: Compile the Testbench & Run Simulation**
Run the following `iverilog` command to compile the testbench and genrate the .vcd file:
```bash
iverilog -o /home/jaynadan/vsd/VLSI/VSDBabySoC/output/post_synth_sim/post_synth_sim.out \
-DPOST_SYNTH_SIM -DFUNCTIONAL -DUNIT_DELAY=#1 \
-I /home/jaynadan/vsd/VLSI/VSDBabySoC/src/include \
-I /home/jaynadan/vsd/VLSI/VSDBabySoC/src/module \
-I /home/jaynadan/vsd/VLSI/VSDBabySoC/output/synth \
/home/jaynadan/vsd/VLSI/VSDBabySoC/src/module/testbench.v

vvp /home/jaynadan/vsd/VLSI/VSDBabySoC/output/post_synth_sim/post_synth_sim.out

```

---
### **Step 2: View the Waveforms in GTKWave**

```bash
gtkwave post_synth_sim.vcd
```
---

![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-33-15.png)

![WhatsApp Image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-34-18.png)

![WhatsApp Image )](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-36-49.png)

![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Images/Screenshot%20from%202025-10-11%2011-37-15.png)




---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Part 2 Fundamental of STA /Readme.md

# 🧩 Week 3 Task – Post-Synthesis GLS & STA Fundamentals  
### **Part 2 – Fundamentals of Static Timing Analysis (STA)**  

---

## 📘 Objective  
The objective of this week’s task is to **understand and perform Gate-Level Simulation (GLS)** after synthesis, validate functional correctness, and get introduced to the **core concepts of Static Timing Analysis (STA)**.  
Through this part, we aim to understand how STA ensures that a synthesized digital circuit can meet its required timing performance before fabrication.  

---

## 🕓 Introduction to STA  
- **Static Timing Analysis (STA)** is a technique used to verify the timing of a digital circuit **without applying input vectors or running full simulations**.  
- It checks all possible timing paths in the design to ensure data is launched and captured properly within a single clock cycle.  
- Unlike dynamic simulation, which depends on testbench data, STA uses mathematical timing constraints and cell delays to verify design timing exhaustively.  
- STA is a critical part of the **post-synthesis verification flow**, helping designers ensure that the design meets frequency, delay, and timing margin requirements before moving to layout or tape-out.  

---

## 🧠 Core Concepts of STA  

### **Timing Graph Representation**  
- STA represents the circuit as a **timing graph**, consisting of nodes (pins or registers) and edges (delays of logic gates or interconnects).  
- **Startpoints:** These are data launch sources such as flip-flop outputs or primary inputs.  
- **Endpoints:** These are data capture points like flip-flop inputs or primary outputs.  
- The tool calculates two critical parameters for every path:  
  - **Arrival Time (AT):** Actual time when data reaches a node.  
  - **Required Time (RT):** Latest time the data must arrive to satisfy setup or hold constraints.  
- **Slack = Required Time – Arrival Time**  
  - *Positive Slack* → Timing met.  
  - *Negative Slack* → Timing violation.  

This model allows STA to analyze all timing paths quickly and identify critical paths that limit clock frequency.  

---

### **Delays, Setup, and Hold Constraints**  
- **Clock-to-Q Delay:** The time from a clock edge to when valid data appears at a flip-flop output.  
- **Setup Time:** Minimum duration before a clock edge when input data must be stable to be captured correctly.  
- **Hold Time:** Minimum duration after a clock edge during which the data must remain stable.  
- **Clock Skew:** The difference in clock arrival times between source and destination registers. It can either improve or degrade timing margins.  
- **Clock Jitter:** Small, unpredictable variations in clock edge timing caused by noise or power fluctuations.  
- All these timing parameters are stored in **standard cell library (.lib)** files, which STA tools use for accurate delay modeling.  

---

## 🧾 Timing Reports and Slack Interpretation  
- STA tools such as **OpenSTA**, **PrimeTime**, or **Tempus** generate detailed **textual timing reports** that summarize analyzed paths.  
- Each report contains:  
  - Startpoint and endpoint (registers or ports)  
  - Path delay (sum of logic and interconnect delays)  
  - Clock definitions  
  - Setup and hold slack values  
- **Setup Analysis:** Ensures data arrives *before* the active clock edge (maximum delay check).  
- **Hold Analysis:** Ensures data remains stable *after* the clock edge (minimum delay check).  
- The **critical path** is the path with the lowest slack (or highest delay). It determines the maximum operating frequency of the design.  
- When violations occur, designers perform **timing optimization** such as buffering, gate resizing, or path restructuring.  

---

## ⚙️ On-Chip Variation (OCV)  
- **On-Chip Variation (OCV)** refers to timing differences across various parts of the chip due to process, voltage, or temperature (PVT) variations.  
- In reality, not all transistors on a chip behave identically; some are faster, others slower.  
- STA accounts for these uncertainties using **derating factors** that scale timing delays.  
  - Example: A “slow” path may be multiplied by 1.05× delay; a “fast” path by 0.95×.  
- This ensures robust timing closure even under non-uniform manufacturing conditions.  
- Modern STA also includes **Advanced OCV (AOCV)** and **Statistical OCV (SOCV)** for more accurate modeling.  

---

## 🧩 Pessimism and Its Removal in STA  
- STA often makes conservative (worst-case) assumptions, known as **pessimism**, to guarantee safety under all conditions.  
- However, excessive pessimism can lead to unnecessary design over-margining and reduced performance.  
- To address this, tools apply **Pessimism Removal Techniques**:  
  - **Common Clock Path Pessimism Removal (CCPR):** Eliminates redundant delay margins on shared clock paths between launch and capture registers.  
  - **Path-Based Analysis (PBA):** Performs a more precise calculation on selected critical paths, reducing over-conservatism.  
- These methods improve the accuracy of slack results and make timing closure more achievable.  

---

## 🧮 Importance of STA in Design Flow  
- STA serves as a bridge between **functional correctness** and **physical feasibility**.  
- It ensures that every signal transition across the chip meets its timing requirements, independent of simulation test cases.  
- A complete STA sign-off involves analyzing all PVT corners and timing modes (setup, hold, recovery, removal).  
- Reliable STA results enable designers to confidently move forward with place-and-route, sign-off, and tape-out processes.  

---

## ✅ Conclusion  
- **Static Timing Analysis** is the backbone of post-synthesis and post-layout verification in modern VLSI design.  
- It ensures that all data paths meet timing requirements under realistic clock, voltage, and process conditions.  
- Mastery of key STA concepts — **setup and hold checks, slack, skew, jitter, OCV, and pessimism removal** — is essential for achieving timing closure.  
- A strong grasp of STA fundamentals enables engineers to design high-performance, reliable, and timing-clean chips ready for fabrication.  

---

## 🔗 Reference  
🎓 **Free Course:** [STA Fundamentals – Udemy](https://www.udemy.com/course/vlsi-academy-sta-checks/?couponCode=F960AEDD365E0CD12546)  
📘 **Tool Used:** [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA)  

---

### all important concept images are in image folderso you can refre them for better understanding 


---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Part 2 Fundamental of STA /Images/Readme.md




---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Part 3 Generate timing Graph with opensta/Readme.md

# ⚙️ Installation of OpenSTA — “Building Your Timing Analyzer”

Before we begin timing analysis, it’s time to install **OpenSTA (Open Static Timing Analyzer)** — the open-source engine that brings precision to your chip’s performance evaluation. ⚡  

Think of OpenSTA as your **digital stopwatch** 🕒 — it measures how fast signals travel, checks if timing paths are valid, and ensures your BabySoC design can keep up with the clock!

---

## 🧩 Overview

**OpenSTA** is a powerful static timing analysis tool used across open-source ASIC design flows.  
It verifies **setup**, **hold**, and **path delays** without running dynamic simulations.  

To install OpenSTA, we’ll prepare the environment, clone the source, and build it from scratch (or use Docker for simplicity).  

---

## 🧰 Prerequisites

Before installation, make sure your system has the following **build tools and libraries** installed:  

| Tool | Ubuntu Version | macOS Version | Purpose |
|:--|:--:|:--:|:--|
| **OS** | 22.04.2 | 14.5 | – |
| **CMake** | 3.24.2 | 3.29.2 | Build system generator |
| **Clang** | – | 15.0.0 | Compiler (macOS) |
| **GCC** | 11.4.0 | – | Compiler (Linux) |
| **Tcl/Tk** | 8.6 | 8.6.16 | Scripting & GUI library |
| **SWIG** | 4.1.0 | 4.1.1 | Interface generator |
| **Bison** | 3.8.2 | 3.8.2 | Parser generator |
| **Flex** | 2.6.4 | 2.6.4 | Lexical analyzer |

### 📦 External Dependencies

| Library | Ubuntu | Darwin | License | Required |
|:--|:--:|:--:|:--:|:--:|
| **Eigen** | 3.4.0 | 3.4.0 | MPL2 | ✅ Yes |
| **CUDD** | 3.0.0 | 3.0.0 | BSD | ✅ Yes |
| **Tclreadline** | 2.3.8 | 2.3.8 | BSD | ⚙️ Optional |
| **zLib** | 1.2.5 | 1.2.8 | zlib | ⚙️ Optional |

> 💡 *Note:* Other versions may work, but these are the configurations used for official development and testing.

---

## 🧠 Step-by-Step Installation

Follow these commands to build OpenSTA from source:

```bash
# 1️⃣ Clone the OpenSTA Repository
git clone https://github.com/parallaxsw/OpenSTA.git
cd OpenSTA

# 2️⃣ Create a Build Directory
mkdir build
cd build

# 3️⃣ Configure Build with CMake
cmake -DCUDD_DIR=usr/bin/lib ..

# 4️⃣ Compile the Source
make
```
🐳 Docker-Based Installation (Simplified Setup)

Prefer containers? You can use Docker to avoid dependency management.
# Build the Docker Image
```
cd OpenSTA
docker build --file Dockerfile.ubuntu22.04 --tag opensta .

# Run OpenSTA from Docker
docker run -i -v $HOME:/data opensta
```


![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2020-21-52.png)


## Static timing analysis using OpenSTA
#### Timing Ananlysis Using In line Commands
```
 read_liberty examples/nangate45_slow.lib.gz
read_verilog examples/example1.v
link_design top
create_clock -name clk -period 10 {clk1 clk2 clk3}
set_input_delay -clock clk 0 {in1 in2}
report_checks
```
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-27-24.png)


#### VSDBabySoC basic timing analysis

```
# Load Liberty timing models
read_liberty -min /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty -max /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

read_liberty -min /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/avsdpll.lib
read_liberty -max /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/avsdpll.lib

read_liberty -min /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/avsddac.lib
read_liberty -max /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/avsddac.lib


# Read the synthesized Verilog (choose one of the two below)
# If you're analyzing synthesis output:
read_verilog /home/jaynadan/vsd/VLSI/VSDBabySoC/output/synth/vsdbabysoc.synth.v
# Or, if you want to analyze the simulation netlist:
# read_verilog /home/jaynadan/vsd/VLSI/VSDBabySoC/output/post_synth_sim/vsdbabysoc.synth.v


# Link the top-level design
link_design vsdbabysoc


# Read the timing constraints
read_sdc /home/jaynadan/vsd/VLSI/VSDBabySoC/src/sdc/vsdbabysoc_synthesis.sdc


# Generate timing reports
report_checks
report_tns
report_wns
```
     
![WhatsApp Image )](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-46-33.png)
![WhatsApp Image ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-47-22.png)

here slack is positive mean we are in safer side 

### **VSDBabySoC PVT Corner Analysis (Post-Synthesis Timing)**  
STA is performed across all PVT corners to validate that the design meets timing requirements.

The worst max path (Setup-critical) corners in sub-40nm nodes are generally:  
- **ss_LowTemp_LowVolt**  
- **ss_HighTemp_LowVolt** *(Slowest corners)*  

The worst min path (Hold-critical) corners are:  
- **ff_LowTemp_HighVolt**  
- **ff_HighTemp_HighVolt** *(Fastest corners)*  

The following TCL script can be executed to perform STA for the available PVT corners using the Sky130 timing libraries.  
The timing libraries can be downloaded from:  
[https://github.com/efabless/skywater-pdk-libs-sky130_fd_sc_hd/tree/master/timing](https://github.com/efabless/skywater-pdk-libs-sky130_fd_sc_hd/tree/master/timing)  

#### the TCL file is 

```
# ==============================
# VSDBabySoC PVT Corner STA Script (with CSV summary)
# ==============================

# Define list of Sky130 PVT corner libs
set list_of_lib_files {
    sky130_fd_sc_hd__tt_025C_1v80.lib
    sky130_fd_sc_hd__ff_100C_1v65.lib
    sky130_fd_sc_hd__ff_100C_1v95.lib
    sky130_fd_sc_hd__ff_n40C_1v56.lib
    sky130_fd_sc_hd__ff_n40C_1v65.lib
    sky130_fd_sc_hd__ff_n40C_1v76.lib
    sky130_fd_sc_hd__ss_100C_1v40.lib
    sky130_fd_sc_hd__ss_100C_1v60.lib
    sky130_fd_sc_hd__ss_n40C_1v28.lib
    sky130_fd_sc_hd__ss_n40C_1v35.lib
    sky130_fd_sc_hd__ss_n40C_1v40.lib
    sky130_fd_sc_hd__ss_n40C_1v44.lib
    sky130_fd_sc_hd__ss_n40C_1v76.lib
}

# Base paths
set lib_dir /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib
set verilog_file /home/jaynadan/vsd/VLSI/VSDBabySoC/output/synth/vsdbabysoc.synth.v
set sdc_file /home/jaynadan/vsd/VLSI/VSDBabySoC/src/sdc/vsdbabysoc_synthesis.sdc
set output_dir /home/jaynadan/vsd/VLSI/VSDBabySoC/STA_OUTPUT

# Ensure output directory exists
file mkdir $output_dir

# Initialize CSV file
set summary_file "$output_dir/pvt_summary.csv"
set fp [open $summary_file w]
puts $fp "PVT_CORNER,Worst_Setup_Slack,Worst_Hold_Slack,WNS,TNS"
close $fp

# Read additional analog/macro libraries
read_liberty -min $lib_dir/avsdpll.lib
read_liberty -max $lib_dir/avsdpll.lib
read_liberty -min $lib_dir/avsddac.lib
read_liberty -max $lib_dir/avsddac.lib

# Loop through all process-voltage-temperature (PVT) corners
foreach lib_name $list_of_lib_files {
    puts "\n=============================="
    puts "Running STA for $lib_name"
    puts "=============================="

    # Read Liberty library for this corner
    read_liberty -min $lib_dir/$lib_name
    read_liberty -max $lib_dir/$lib_name

    # Read synthesized netlist
    read_verilog $verilog_file

    # Link design
    link_design vsdbabysoc
    current_design

    # Read timing constraints
    read_sdc $sdc_file

    # Run checks
    check_setup -verbose

    # Report results
    set prefix $output_dir/[file rootname $lib_name]
    report_checks -path_delay min_max -fields {nets cap slew input_pins fanout} -digits 4 > ${prefix}_checks.txt

    # Capture key numbers into variables
    set worst_setup_slack [report_worst_slack -max -digits 4]
    set worst_hold_slack [report_worst_slack -min -digits 4]
    set wns [report_wns -digits 4]
    set tns [report_tns -digits 4]

    # Append values to CSV file
    set fp [open $summary_file a]
    puts $fp "$lib_name,$worst_setup_slack,$worst_hold_slack,$wns,$tns"
    close $fp

    # Cleanup before next corner
    reset_design
}

puts "\n=============================="
puts "✅ PVT Corner STA Completed"
puts "Summary CSV generated at: $summary_file"
puts "=============================="

cd /home/jaynadan/vsd/VLSI/VSDBabySoC
sta run_pvt_sta.tcl
```
if you get any error any lib file missing then download by using this python command in your vsdbabysoc path 

````
cd /home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib/

for lib in \
sky130_fd_sc_hd__tt_025C_1v80.lib \
sky130_fd_sc_hd__ff_100C_1v65.lib \
sky130_fd_sc_hd__ff_100C_1v95.lib \
sky130_fd_sc_hd__ff_n40C_1v56.lib \
sky130_fd_sc_hd__ff_n40C_1v65.lib \
sky130_fd_sc_hd__ff_n40C_1v76.lib \
sky130_fd_sc_hd__ss_100C_1v40.lib \
sky130_fd_sc_hd__ss_100C_1v60.lib \
sky130_fd_sc_hd__ss_n40C_1v28.lib \
sky130_fd_sc_hd__ss_n40C_1v35.lib \
sky130_fd_sc_hd__ss_n40C_1v40.lib \
sky130_fd_sc_hd__ss_n40C_1v44.lib \
sky130_fd_sc_hd__ss_n40C_1v76.lib
do
  if [ ! -f "$lib" ]; then
    echo "Downloading missing $lib..."
    wget -q https://raw.githubusercontent.com/efabless/skywater-pdk-libs-sky130_fd_sc_hd/master/timing/$lib
  else
    echo "$lib already exists ✅"
  fi
done
````

output of this tcl file 

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-58-19.png)

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-58-39.png)

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-02.png)

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-12.png)

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-16.png)

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-16.png)

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-20.png)

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-26.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-31.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-34.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-39.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-43.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week3%20/Part%203%20Generate%20timing%20Graph%20with%20opensta/Images/Screenshot%20from%202025-10-11%2019-59-49.png)



---

# /mnt/data/silicon_repo/silicon-diary-main/Week3 /Part 3 Generate timing Graph with opensta/Images/Readme.md




# Week4

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Readme.md

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




---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day1/Readme.md

# ⚡ Day 1 — NMOS Drain Current (Id) vs Drain-to-Source Voltage (Vds)

Welcome to **Day 1** of the **NgspiceSky130 learning series**!  
This day begins your journey into **transistor-level design and SPICE simulation** using the open-source **Sky130 PDK**.  
We’ll explore the electrical behavior of the **NMOS transistor** and understand how **drain current (Id)** varies with **drain-to-source voltage (Vds)** under different gate bias conditions.

---

## 🎯 Learning Objectives

By the end of this session, you will:

- Understand why SPICE simulations are essential in circuit design.  
- Explore NMOS transistor fundamentals and body effect.  
- Analyze **linear (resistive)** and **saturation** regions of NMOS operation.  
- Simulate and plot **Id–Vds characteristics** using Sky130 SPICE models.

---

## 🧩 1. Introduction to Circuit Design and SPICE Simulations  

SPICE (Simulation Program with Integrated Circuit Emphasis) is a powerful tool for **predicting circuit performance** before fabrication.  
It allows us to simulate device behavior, verify electrical parameters, and visualize circuit responses to different inputs.

Key Topics:
- Purpose and advantages of SPICE simulations  
- Basics of NMOS structure and operation  
- Threshold voltage and strong inversion  
- Substrate (body) bias and threshold variation  

---

### 📘 Why SPICE?

In circuit design, SPICE provides a **virtual lab environment** that replicates real-world device behavior.  
For instance, consider a CMOS **inverter**:

- The **PMOS** (pull-up) and **NMOS** (pull-down) share a common output node.  
- Their **gates** receive the same input, ensuring complementary operation.  
- The **output** switches between **VDD** and **GND**, producing logical inversion.

SPICE allows designers to confirm correct switching behavior, analyze **propagation delays**, and study **power consumption** before committing to silicon fabrication.

---

## ⚙️ 2. NMOS Device Fundamentals  

### 🧠 Understanding the NMOS Transistor

An **NMOS transistor** conducts when a **positive gate voltage (Vgs)** exceeds the **threshold voltage (Vt)**.  
This voltage induces a conductive channel between **drain** and **source**, allowing current flow.

![NMOS Structure](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-13%20235455.png)

**Key Parameters:**
- **Vt (Threshold Voltage):** Minimum gate voltage required to form an inversion channel.  
- **Strong Inversion:** Region where the induced channel is fully formed and current flow maximizes.  
- **Body Effect:** Variation of threshold voltage due to substrate potential (Vsb).  

---

### ⚡ Threshold Voltage and Body Effect

The threshold voltage is not constant — it changes with substrate bias (Vsb).  
SPICE models use parameters such as **body-effect coefficient (γ)** and **Fermi potential (ΦF)** to calculate this variation.

| Parameter | Description |
|------------|-------------|
| Vt0 | Threshold voltage when Vsb = 0 |
| γ (Gamma) | Body effect coefficient |
| ΦF | Fermi potential (process-dependent) |

These are foundry-defined parameters embedded in the **Sky130 model files** to ensure simulation accuracy.

![Threshold Variation](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-14%20004240.png)

---

## 📊 3. NMOS Operation Regions  

The NMOS transistor operates in two major regions based on **Vds** and **Vgs**:

---

### 🔹 (a) Resistive / Linear Region

Occurs when **Vds < (Vgs - Vt)**.  
Here, the channel is continuous, and the transistor behaves like a **voltage-controlled resistor**.

![Linear Region](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20004825.png)

**Current Equation:**
\[
I_d = μ_n C_{ox} \frac{W}{L} [(V_{gs} - V_t)V_{ds} - \frac{V_{ds}^2}{2}]
\]

Where:
- **μn:** Electron mobility  
- **Cox:** Oxide capacitance per unit area  
- **W/L:** Width-to-length ratio of the MOSFET  

![Drift-Diffusion Model](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20230408.png)

The **drain current (Id)** increases linearly with **Vds**, forming the initial slope in the Id–Vds plot.

---

**SPICE Observation (Resistive Mode):**  
In simulation, for each **Vgs** value, **Vds** is swept, and Id is plotted.  
As **Vds** approaches **Vgs - Vt**, the linear behavior transitions into saturation.

![Resistive SPICE Curve](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-15%20230740.png)

---

### 🔹 (b) Saturation / Pinch-off Region

Occurs when **Vds ≥ (Vgs - Vt)**.  
The channel pinches off near the drain, and current becomes almost constant.

![Saturation Concept](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20002723.png)

**Current Equation:**
\[
I_d = \frac{1}{2} μ_n C_{ox} \frac{W}{L} (V_{gs} - V_t)^2
\]

Here, **Id** is primarily controlled by **Vgs**, making this region essential for analog amplifiers and current sources.

![Saturation Graphs](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20004407.png)

**SPICE Observation (Saturation Mode):**
- Id saturates with increasing Vds.  
- The saturation level rises with higher Vgs values.  
- The transition point (**Vds = Vgs - Vt**) is clearly visible in the simulated plots.

![SPICE Saturation Curves](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%202025-10-16%20004639.png)

---

## 🧪 4. Introduction to SPICE Simulation Setup  

SPICE simulation bridges **theory** and **practical device behavior**.  
A typical SPICE file contains:

1. **Circuit Elements:** Transistors, voltage sources, and resistors.  
2. **Device Parameters:** Model files (Sky130 NMOS/PMOS) and geometry (W/L).  
3. **Analysis Commands:** `.dc`, `.tran`, `.ac`, etc. for different simulations.  

Example (Conceptual):


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

## 🧾 Summary

| Concept | Description |
|----------|--------------|
| **Resistive Region** | Transistor acts as a resistor; Id ∝ Vds |
| **Saturation Region** | Id becomes constant; controlled by Vgs |
| **Threshold Voltage** | Minimum gate voltage for conduction |
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

## 📈 NMOS Id–Vds Simulation Output

The following plots are obtained from SPICE simulations of an NMOS transistor using **Sky130 models**. They show how the **drain current (Id)** varies with **drain-to-source voltage (Vds)** for different gate voltages (Vgs).

---

### **1️⃣ Id vs Vds for Multiple Gate Voltages**

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2000-51-12.png)

**Description:**
- Shows **Id–Vds characteristics** for several Vgs values.  
- At low Vds, Id increases linearly — the **resistive (linear) region**.  
- At higher Vds, Id flattens — the **saturation region**.  
- Higher Vgs produces higher Id, consistent with NMOS behavior.  
- The transition from linear to saturation occurs approximately at **Vds = Vgs - Vt**.

**Observation:**  
This plot verifies the expected NMOS behavior and clearly distinguishes the linear and saturation regions.

---

### **2️⃣ Zoomed View of Linear Region**

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2000-56-46.png)

**Description:**
- Focused on the **low Vds region** of the NMOS.  
- Illustrates that Id **increases almost linearly with Vds**.  
- Confirms that in the linear region, the transistor behaves like a **voltage-controlled resistor**.  
- The slope of each curve increases with higher Vgs, showing the effect of gate voltage on channel conductance.

**Observation:**  
The linear region is clearly visible, providing insight into how the device will behave in analog circuits or as a switch with small Vds.

---

### **3️⃣ Id vs Vds in Saturation Region**

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day1/Images/Screenshot%20from%202025-10-17%2001-00-05.png)

**Description:**
- Focused on the **high Vds region**, where Id becomes nearly constant.  
- Illustrates the **saturation region (pinch-off)** of the NMOS transistor.  
- Id depends mostly on Vgs and shows minimal variation with further increase in Vds.  
- Confirms the SPICE simulation results match theoretical predictions for the saturation current.

**Observation:**  
This plot helps understand current limiting in NMOS transistors, critical for analog design and current sources.

---

**Summary of Observations:**
- **Linear region:** Id ∝ Vds, slope increases with Vgs.  
- **Saturation region:** Id saturates, controlled mainly by Vgs.  
- **Transition:** Occurs near Vds = Vgs - Vt.  
- SPICE results align well with theoretical NMOS behavior.

## 📈 Outcome  

By completing **Day 1**, you’ll gain a solid understanding of how NMOS transistors behave under various voltage conditions and how SPICE simulations bring theory to life.  
You’ll learn how to interpret transistor characteristics, analyze current-voltage behavior, and generate plots that reveal real design insights.  

This forms the **foundation of all transistor-based design work** — the stepping stone to CMOS logic and full-system chip verification.

✨ *Every silicon chip begins at the transistor level — master this, and you master the heart of digital design.* ✨



---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day1/Images/Readme.md

for images


---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day2/Readme.md

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


---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day2/Images/Readme.md

for images only


---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day3/Readme.md

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


---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day3/Images/Readme.md

only imAGED


---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day4/Readme.md

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




---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day4/Images/Readme.md




---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day5/Readme.md

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
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week4/Day5/Image/Screenshot%20from%202025-10-18%2017-03-19.png)




---

# /mnt/data/silicon_repo/silicon-diary-main/Week4/Day5/Image/Readme.md




# Week5

# /mnt/data/silicon_repo/silicon-diary-main/Week5/Readme.md


# 🚀 OpenROAD Installation Guide

Welcome to the **OpenROAD Project** — an open-source revolution in digital chip design!  
OpenROAD (Open **Real-time Optimized Autonomous Design**) aims to deliver a **24-hour, no-human-in-the-loop RTL-to-GDSII flow**, empowering designers, researchers, and students to explore ASIC physical design freely.  

This guide provides an overview of how to get started with **OpenROAD**, the core physical design tool, and how it relates to **OpenROAD-Flow-Scripts**, the complete flow automation framework.  

Whether you're a researcher tuning placement algorithms or an engineer running a full ASIC flow — OpenROAD gives you the freedom to explore silicon like never before. 🧠💡

---

## ⚖️ OpenROAD vs OpenROAD-Flow-Scripts

| Feature | **OpenROAD** 🧩 | **OpenROAD-Flow-Scripts** 🧱 |
|:--------|:----------------|:-----------------------------|
| **Purpose** | Core engine for digital physical design | Complete RTL-to-GDSII flow automation |
| **Input** | Netlist (post-synthesis) + LEF/DEF + Liberty | RTL (Verilog) + Config files |
| **Output** | DEF, GDS, timing reports | Full ASIC layout, GDSII, logs, and metrics |
| **Functionality** | Placement, routing, optimization, timing | Integrates multiple tools (Yosys, OpenROAD, OpenSTA, Magic, etc.) |
| **Usage** | Interactive or scripted EDA tool | Makefile-based automated design flow |
| **Flexibility** | Ideal for custom research & module-level design | Ideal for running full SoC or block-level flows |
| **Repository** | [github.com/The-OpenROAD-Project/OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | [github.com/The-OpenROAD-Project/OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) |

---

✨ **In short:**  
- **OpenROAD** = the engine 🧠 that powers the flow.  
- **OpenROAD-Flow-Scripts** = the vehicle 🚗 that drives from RTL to GDSII using that engine.  

Together, they make open-source silicon design faster, smarter, and truly accessible. 🌍💻

> Note:- Before installing This Openroad tool make sure you have installed these dependencies otherwise you will may face much problems

### Required Packages
```bash
sudo apt update
sudo apt install -y build-essential cmake clang bison flex libreadline-dev \
                    gawk tcl-dev tk-dev libffi-dev git graphviz xdot \
                    pkg-config python3 python3-dev libboost-system-dev \
                    libboost-python-dev swig libeigen3-dev
```
Install this tool and make
```bash
git clone https://github.com/google/or-tools.git
cd or-tools
mkdir build && cd build
cmake -DBUILD_DEPS=ON -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
sudo make install
```
Inside your temp folder download and extract this file 

Step 1
```bash
cd /tmp
wget https://github.com/google/or-tools/releases/download/v9.6/or-tools_amd64_ubuntu-22.04_cpp_v9.6.2534.tar.gz
tar -xzf or-tools_amd64_ubuntu-22.04_cpp_v9.6.2534.tar.gz
sudo mv or-tools_Ubuntu-22.04-64bit /usr/local/or-tools
```
Step 2 --Set Environment Variables

```bash
export ortools_DIR=/usr/local/or-tools/lib/cmake/ortools
export CMAKE_PREFIX_PATH=/usr/local/or-tools
echo 'export ortools_DIR=/usr/local/or-tools/lib/cmake/ortools' >> ~/.bashrc
echo 'export CMAKE_PREFIX_PATH=/usr/local/or-tools' >> ~/.bashrc
source ~/.bashrc
```
##### If You will not download these dependeices and file you will may get error like this 

Error No. 1 
```bash
root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD# mkdir build && cd build
root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD/build# cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-Wno-error" -DCMAKE_PREFIX_PATH="/usr/local" -DCMAKE_CXX_COMPILER=/usr/bin/g++-9
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:54 (project):
  The CMAKE_CXX_COMPILER:

    /usr/bin/g++-9

  is not a full path to an existing compiler tool.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD/build# 

````
Error No. 2 

```bash
- STA library: /home/jaynadan/vsd/VLSI/OpenROAD/build/libOpenSTA.a
-- STA executable: /home/jaynadan/vsd/VLSI/OpenROAD/build/sta
CMake Error at src/gpl/CMakeLists.txt:12 (find_package):
  By not providing "Findortools.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "ortools", but
  CMake did not find one.

  Could not find a package configuration file provided by "ortools" with any
  of the following names:

    ortoolsConfig.cmake
    ortools-config.cmake

  Add the installation prefix of "ortools" to CMAKE_PREFIX_PATH or set
  "ortools_DIR" to a directory containing one of the above files.  If
  "ortools" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD/build# 

```
and when you will run build command you will get fail here so first sure you download these file and make them first 

### **Steps to Install OpenROAD and Run GUI**  

#### **1. Clone the OpenROAD Repository**  
      git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts
      cd OpenROAD-flow-script
![screensot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-21%2016-24-49.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2001-02-47.png)
#### **2. Run the Setup Script**  
       sudo ./setup.sh
       
![screensot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-23%2021-35-54.png)


#### **3. Build OpenROAD**  

      ./build_openroad.sh --local

If here you not getting error its fine and good you can skip next some part from cloning again OpenRoad repo and installation of it but i also get here build error so i follows next stpes and i think everyone get here almost IN Below image you will get to know about the error if you also get this error worry not we have second option just follow all steps and you will win

![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2000-28-27-1.png)

If you also get something like as above then follow next steps 

Now again Clone repository of OpenRoad and install it by following these steps 
#### **1. Clone the OpenROAD Repository**  
     git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD.git
     cd OpenROAD

#### **Step 2 — Create a Build Directory**  
      mkdir build
      cd build

#### **Step 3 — Configure and Build**  
      cmake .. -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_CXX_FLAGS="-Wno-error" \
      -DCMAKE_PREFIX_PATH="/usr/local" \
       -DCMAKE_CXX_COMPILER=/usr/bin/g++-9

       make -j$(nproc)
       sudo make install
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-56-16.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-56-31.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2013-26-11.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-09-25.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-10-16.png)

#### **Step 4 — Verify Installation**
       ls bin/
       ./bin/openroad -version
✅ You should see version output like:
       v2.0-25739-g7319402f48

![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-13-27.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-16-32.png)
![screeshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-16-51.png)
Now after this go inside your OpenROAD-flow-script directory which we already cloned in 1 step 
```
 cd OpenROAD-flow-script
```
##### **Step 1 - Connect OpenROAD to Flow-Scripts**

       export OPENROAD_EXE=/home/jaynadan/vsd/VLSI/OpenROAD/build/bin/openroad
       echo 'export OPENROAD_EXE=/home/jaynadan/vsd/VLSI/OpenROAD/build/bin/openroad' >> ~/.bashrc
       source ~/.bashrc
       
##### **Step 2 — Source Environment**

           source ./env.sh
          yosys -help  
          openroad -help

You will see like this 

      
       root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD-flow-scripts# source env.sh
       OPENROAD: /home/jaynadan/vsd/VLSI/OpenROAD-flow-scripts/tools/OpenROAD
       root@jaynadan-VMware-Virtual-Platform:/home/jaynadan/vsd/VLSI/OpenROAD-flow-scripts# 

![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-42-09.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-42-15.png)

if you find yosys error the do this step otherwise no need

```
export YOSYS_EXE=/usr/local/bin/yosys
echo 'export YOSYS_EXE=/usr/local/bin/yosys' >> ~/.bashrc
source ~/.bashrc
```

##### ** Step - 3 Run the OpenROAD Flow**

           cd flow
           make
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-53-01.png)

##### ** Step - 4 Launch the graphical user interface (GUI) to visualize the final layout:**

         make gui_final
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-53-47.png)

##### **Directory Structure **

![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week5/Images/Screenshot%20from%202025-10-24%2015-54-43.png)

📘  Notes

Always ```source env.sh ``` before running any flow.
If any dependency fails, rebuild using:

    make clean_all
    make
Logs can be checked under flow/reports/ or flow/logs/.


---

# /mnt/data/silicon_repo/silicon-diary-main/Week5/Images/Readme.md




# Week6

# /mnt/data/silicon_repo/silicon-diary-main/Week6/Readme.md


Day 1:- 
1. Run 'picorv32a' design synthesis using OpenLANE flow and generate necessary outputs.
2. Calculate the flop ratio.

```math
Flop\ Ratio = \frac{Number\ of\ D\ Flip\ Flops}{Total\ Number\ of\ Cells}
```
```math
Percentage\ of\ DFF's = Flop\ Ratio * 100
```

#### 1. Run 'picorv32a' design synthesis using OpenLANE flow and generate necessary outputs.

Commands to invoke the OpenLANE flow and perform synthesis

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```
```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Exit from OpenLANE flow
exit

# Exit from OpenLANE flow docker sub-system
exit
```

Screenshots of running each commands

![1](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2006-54-58.png)
![2](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2007-10-14.png)
![3](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2007-10-21.png)

#### 2. Calculate the flop ratio.

Screenshots of synthesis statistics report file with required values highlighted

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2007-10-14.png)

Calculation of Flop Ratio and DFF % from synthesis statistics report file

```math
Flop\ Ratio = \frac{1613}{14876} = 0.108429685
```
```math
Percentage\ of\ DFF's = 0.108429685 * 100 = 10.84296854\ \%
```

## Day 2 - Good floorplan vs bad floorplan and introduction to library cells 

### Implementation

Section 2 tasks:- 
1. Run 'picorv32a' design floorplan using OpenLANE flow and generate necessary outputs.
2. Calculate the die area in microns from the values in floorplan def.
3. Load generated floorplan def in magic tool and explore the floorplan.
4. Run 'picorv32a' design congestion aware placement using OpenLANE flow and generate necessary outputs.
5. Load generated placement def in magic tool and explore the placement.

```math
Area\ of\ die\ in\ microns = Die\ width\ in\ microns * Die\ height\ in\ microns
```

#### 1. Run 'picorv32a' design floorplan using OpenLANE flow and generate necessary outputs.

Commands to invoke the OpenLANE flow and perform floorplan

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```
```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Now we can run floorplan
run_floorplan
```

Screenshot of floorplan run

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2007-45-24.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-27-12.png)

#### 2. Calculate the die area in microns from the values in floorplan def.

Screenshot of contents of floorplan def

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-37-04.png)

According to floorplan def
```math
1000\ Unit\ Distance = 1\ Micron
```
```math
Die\ width\ in\ unit\ distance = 660685 - 0 = 660685
```
```math
Die\ height\ in\ unit\ distance = 671405 - 0 = 671405
```
```math
Distance\ in\ microns = \frac{Value\ in\ Unit\ Distance}{1000}
```
```math
Die\ width\ in\ microns = \frac{660685}{1000} = 660.685\ Microns
```
```math
Die\ height\ in\ microns = \frac{671405}{1000} = 671.405\ Microns
```
```math
Area\ of\ die\ in\ microns = 660.685 * 671.405 = 443587.212425\ Square\ Microns
```

#### 3. Load generated floorplan def in magic tool and explore the floorplan.

Commands to load floorplan def in magic in another terminal

```bash
# Change directory to path containing generated floorplan def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/17-03_12-06/results/floorplan/

# Command to load the floorplan def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.floorplan.def &
```

Screenshots of floorplan def in magic

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-42-46.png)

Equidistant placement of ports

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-47-19.png)

Port layer as set through config.tcl

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-50-54.png)
![Screenshot 0](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-55-12.png)

Decap Cells and Tap Cells

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2019-57-44.png)


#### 4. Run 'picorv32a' design congestion aware placement using OpenLANE flow and generate necessary outputs.

Command to run placement

```tcl
# Congestion aware placement by default
run_placement
```

Screenshots of placement run

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2020-52-59.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2020-53-35.png)
![screemshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2017-07-22.png)

#### 5. Load generated placement def in magic tool and explore the placement.

Commands to load placement def in magic in another terminal

```bash
# Change directory to path containing generated placement def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/17-03_12-06/results/placement/

# Command to load the placement def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.placement.def &
```

Screenshots of floorplan def in magic

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2020-57-55.png)

Standard cells legally placed 

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-30%2021-01-35.png)

Commands to exit from current run

```tcl
# Exit from OpenLANE flow
exit

# Exit from OpenLANE flow docker sub-system
exit
```

## Day 3 - Design library cell using Magic Layout and ngspice characterization


### Implementation

* Section 3 tasks:-
1. Clone custom inverter standard cell design from github repository: [Standard cell design and characterization using OpenLANE flow](https://github.com/nickson-jose/vsdstdcelldesign).
2. Load the custom inverter layout in magic and explore.
3. Spice extraction of inverter in magic.
4. Editing the spice model file for analysis through simulation.
5. Post-layout ngspice simulations.
6. Find problem in the DRC section of the old magic tech file for the skywater process and fix them.

#### 1. Clone custom inverter standard cell design from github repository

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Clone the repository with custom inverter design
git clone https://github.com/nickson-jose/vsdstdcelldesign

# Change into repository directory
cd vsdstdcelldesign

# Copy magic tech file to the repo directory for easy access
cp /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech .

# Check contents whether everything is present
ls

# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_inv.mag &
```

Screenshot of commands run

![Screenshot from 2024-03-19 00-22-27](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2017-17-12.png)

#### 2. Load the custom inverter layout in magic and explore.

Screenshot of custom inverter layout in magic

![Screenshot from 2024-03-19 00-22-44](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2017-17-05.png)

NMOS and PMOS identified

![Screenshot from 2024-03-19 00-29-14](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2018-46-26.png)

#### 3. Spice extraction of inverter in magic.

Commands for spice extraction of the custom inverter layout to be used in tkcon window of magic

```tcl
# Check current directory
pwd

# Extraction command to extract to .ext format
extract all

# Before converting ext to spice this command enable the parasitic extraction also
ext2spice cthresh 0 rthresh 0

# Converting to ext to spice
ext2spice
```

Screenshot of tkcon window after running above commands

![Screenshot from 2024-03-19 01-24-17](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2018-46-34.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2007-05-28.png)
Screenshot of created spice file

![Screenshot from 2024-03-19 01-27-07](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-10-31%2018-56-57.png)

#### 4. Editing the spice model file for analysis through simulation.

Measuring unit distance in layout grid

![Screenshot from 2024-03-19 01-30-15]()

Final edited spice file ready for ngspice simulation

![Screenshot from 2024-03-19 14-50-54](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2007-54-09.png)

#### 5. Post-layout ngspice simulations.

Commands for ngspice simulation

```bash
# Command to directly load spice file for simulation to ngspice
ngspice sky130_inv.spice

# Now that we have entered ngspice with the simulation spice file loaded we just have to load the plot
plot y vs time a
```

Screenshots of ngspice run

![Screenshot from 2024-03-19 14-56-42](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2007-54-55.png)
![Screenshot from 2024-03-19 14-57-22](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2007-55-38.png)

Rise transition time calculation

```math
Rise\ transition\ time = Time\ taken\ for\ output\ to\ rise\ to\ 80\% - Time\ taken\ for\ output\ to\ rise\ to\ 20\%
```
```math
20\%\ of\ output = 660\ mV
```
```math
80\%\ of\ output = 2.64\ V
```



![Screenshot from 2024-03-19 15-15-02](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2007-59-20.png)
![Screenshot from 2024-03-19 15-20-04](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2008-00-20.png)



```math
Rise\ transition\ time = 2.24638 - 2.18242 = 0.06396\ ns = 63.96\ ps
```

Fall transition time calculation

```math
Fall\ transition\ time = Time\ taken\ for\ output\ to\ fall\ to\ 20\% - Time\ taken\ for\ output\ to\ fall\ to\ 80\%
```
```math
20\%\ of\ output = 660\ mV
```
```math
80\%\ of\ output = 2.64\ V
```


```math
Rise\ Cell\ Delay = 2.21144 - 2.15008 = 0.06136\ ns = 61.36\ ps
```

Fall Cell Delay Calculation

```math
Fall\ Cell\ Delay = Time\ taken\ for\ output\ to\ fall\ to\ 50\% - Time\ taken\ for\ input\ to\ rise\ to\ 50\%
```

#### 6. Find problem in the DRC section of the old magic tech file for the skywater process and fix them.

Link to Sky130 Periphery rules: [https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html](https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html)

Commands to download and view the corrupted skywater process magic tech file and associated files to perform drc corrections

```bash
# Change to home directory
cd

# Command to download the lab files
wget http://opencircuitdesign.com/open_pdks/archive/drc_tests.tgz

# Since lab file is compressed command to extract it
tar xfz drc_tests.tgz

# Change directory into the lab folder
cd drc_tests

# List all files and directories present in the current directory
ls -al

# Command to view .magicrc file
gvim .magicrc

# Command to open magic tool in better graphics
magic -d XR &
```

Screenshots of commands run

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-14-46.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-14-38.png)

Screenshot of .magicrc file

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-14-38.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-17-18.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-17-18.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-39-02.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-39-15.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-50-21.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-50-22.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2015-50-25.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-12-22.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-12-13.png)
![screenshot]()
## Day 4 - Pre-layout timing analysis and importance of good clock tree 

### Implementation

* Section 4 tasks:-
1. Fix up small DRC errors and verify the design is ready to be inserted into our flow.
2. Save the finalized layout with custom name and open it.
3. Generate lef from the layout.
4. Copy the newly generated lef and associated required lib files to 'picorv32a' design 'src' directory.
5. Edit 'config.tcl' to change lib file and add the new extra lef into the openlane flow.
6. Run openlane flow synthesis with newly inserted custom inverter cell.
7. Remove/reduce the newly introduced violations with the introduction of custom inverter cell by modifying design parameters.
8. Once synthesis has accepted our custom inverter we can now run floorplan and placement and verify the cell is accepted in PnR flow.
9. Do Post-Synthesis timing analysis with OpenSTA tool.

#### 1. Fix up small DRC errors and verify the design is ready to be inserted into our flow.

Conditions to be verified before moving forward with custom designed cell layout:
* Condition 1: The input and output ports of the standard cell should lie on the intersection of the vertical and horizontal tracks.
* Condition 2: Width of the standard cell should be odd multiples of the horizontal track pitch.
* Condition 3: Height of the standard cell should be even multiples of the vertical track pitch.

Commands to open the custom inverter layout

```bash
# Change directory to vsdstdcelldesign
cd Desktop/work/tools/openlane_working_dir/openlane/vsdstdcelldesign

# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_inv.mag &
```

Screenshot of tracks.info of sky130_fd_sc_hd

![Screenshot from 2024-03-24 13-38-09](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-43-52.png)

Commands for tkcon window to set grid as tracks of locali layer

```tcl
# Get syntax for grid command
help grid

# Set grid values accordingly
grid 0.46um 0.34um 0.23um 0.17um
```

Screenshot of commands run

![Screenshot from 2024-03-24 13-49-55](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-41-14.png)

Condition 1 verified

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-46-33.png)
![screenshort](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-49-35.png)
Condition 2 verified

```math
Horizontal\ track\ pitch = 0.46\ um
```

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-46-33.png)

```math
Width\ of\ standard\ cell = 1.38\ um = 0.46 * 3
```

Condition 3 verified

```math
Vertical\ track\ pitch = 0.34\ um
```

![Screenshot from 2024-03-24 13-58-32](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-02-20.png)
![screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-52-39.png)
```math
Height\ of\ standard\ cell = 2.72\ um = 0.34 * 8
```

#### 2. Save the finalized layout with custom name and open it.

Command for tkcon window to save the layout with custom name

```tcl
# Command to save as
save sky130_vsdinv.mag
```

Command to open the newly saved layout

```bash
# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_vsdinv.mag &
```

Screenshot of newly saved layout

![Screenshot from 2024-03-24 14-33-20](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2016-41-14.png)

#### 3. Generate lef from the layout.

Command for tkcon window to write lef

```tcl
# lef command
lef write
```

Screenshot of command run

![Screenshot from 2024-03-24 14-35-55](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-04-02.png)

Screenshot of newly created lef file

![Screenshot from 2024-03-24 14-37-19](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-06-04.png)

#### 4. Copy the newly generated lef and associated required lib files to 'picorv32a' design 'src' directory.

Commands to copy necessary files to 'picorv32a' design 'src' directory

```bash
# Copy lef file
cp sky130_vsdinv.lef ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# List and check whether it's copied
ls ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# Copy lib files
cp libs/sky130_fd_sc_hd__* ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# List and check whether it's copied
ls ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/
```

Screenshot of commands run

![Screenshot from 2024-03-24 14-55-23](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-08-12.png)

#### 5. Edit 'config.tcl' to change lib file and add the new extra lef into the openlane flow.

Commands to be added to config.tcl to include our custom cell in the openlane flow

```tcl
set ::env(LIB_SYNTH) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__typical.lib"
set ::env(LIB_FASTEST) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__fast.lib"
set ::env(LIB_SLOWEST) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__slow.lib"
set ::env(LIB_TYPICAL) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__typical.lib"

set ::env(EXTRA_LEFS) [glob $::env(OPENLANE_ROOT)/designs/$::env(DESIGN_NAME)/src/*.lef]
```

Edited config.tcl to include the added lef and change library to ones we added in src directory

![Screenshot from 2024-03-24 15-29-56](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-21-54.png)

#### 6. Run openlane flow synthesis with newly inserted custom inverter cell.

Commands to invoke the OpenLANE flow include new lef and perform synthesis 

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```
```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Adiitional commands to include newly added lef to openlane flow
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Screenshots of commands run

![Screenshot 6](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-29-10.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-32-59.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-50-47.png)

#### 7. Remove/reduce the newly introduced violations with the introduction of custom inverter cell by modifying design parameters.

Noting down current design values generated before modifying parameters to improve timing

![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-32-59.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-50-47.png)

Commands to view and change parameters to improve timing and run synthesis

```tcl
# Now once again we have to prep design so as to update variables
prep -design picorv32a -tag 24-03_10-03 -overwrite

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to display current value of variable SYNTH_STRATEGY
echo $::env(SYNTH_STRATEGY)

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to display current value of variable SYNTH_BUFFERING to check whether it's enabled
echo $::env(SYNTH_BUFFERING)

# Command to display current value of variable SYNTH_SIZING
echo $::env(SYNTH_SIZING)

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Command to display current value of variable SYNTH_DRIVING_CELL to check whether it's the proper cell or not
echo $::env(SYNTH_DRIVING_CELL)

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Screenshot of merged.lef in `tmp` directory with our custom inverter as macro

![Screenshot from 2024-03-24 23-46-25](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-11-07.png)

Screenshots of commands run

![Screenshot from 2024-03-24 17-10-46](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-21-47.png)

Comparing to previously noted run values area has increased and worst negative slack has become 0

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-21-43.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-21-47.png)

#### 8. Once synthesis has accepted our custom inverter we can now run floorplan and placement and verify the cell is accepted in PnR flow.

Now that our custom inverter is properly accepted in synthesis we can now run floorplan using following command

```tcl
# Now we can run floorplan
run_floorplan
```

Screenshots of command run

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-22-36.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-25-05.png)

Since we are facing unexpected un-explainable error while using `run_floorplan` command, we can instead use the following set of commands available based on information from `Desktop/work/tools/openlane_working_dir/openlane/scripts/tcl_commands/floorplan.tcl` and also based on `Floorplan Commands` section in `Desktop/work/tools/openlane_working_dir/openlane/docs/source/OpenLANE_commands.md`

```tcl
# Follwing commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or
```

Screenshots of commands run

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-25-12.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-25-31.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-25-45.png)

Now that floorplan is done we can do placement using following command

```tcl
# Now we are ready to run placement
run_placement
```

Screenshots of command run

![Screenshot from 2024-03-24 23-49-29](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-26-11.png)
![Screenshot from 2024-03-24 23-51-08](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-26-48.png)

Commands to load placement def in magic in another terminal

```bash
# Change directory to path containing generated placement def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/24-03_10-03/results/placement/

# Command to load the placement def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.placement.def &
```

Screenshot of placement def in magic

![Screenshot from 2024-03-25 00-16-54](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-28-28.png)


Command for tkcon window to view internal layers of cells

```tcl
# Command to view internal connectivity layers
expand
```

Abutment of power pins with other cell from library clearly visible

![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-30-19.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2017-30-26.png)


## Day 5 - Final steps for RTL2GDS using tritonRoute and openSTA 
### Implementation

* Section 5 tasks:-
1. Perform generation of Power Distribution Network (PDN) and explore the PDN layout.
2. Perfrom detailed routing using TritonRoute.
3. Post-Route parasitic extraction using SPEF extractor.
4. Post-Route OpenSTA timing analysis with the extracted parasitics of the route.

#### 1. Perform generation of Power Distribution Network (PDN) and explore the PDN layout.

Commands to perform all necessary stages up until now

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```
```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Following commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or

# Now we are ready to run placement
run_placement

# Incase getting error
unset ::env(LIB_CTS)

# With placement done we are now ready to run CTS
run_cts

# Now that CTS is done we can do power distribution network
gen_pdn 
```

Screenshots of power distribution network run

![Screenshot from 2024-03-26 14-22-34](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2018-49-10.png)

Commands to load PDN def in magic in another terminal

```bash
# Change directory to path containing generated PDN def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/26-03_08-45/tmp/floorplan/

# Command to load the PDN def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read 14-pdn.def &
```

Screenshots of PDN def

![Screenshot from 2024-03-26 14-30-52](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2018-53-03.png)
![Screenshot ](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2018-53-46.png)
![Screenshot](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2018-53-50.png)

#### 2. Perfrom detailed routing using TritonRoute and explore the routed layout.

Command to perform routing

```tcl
# Check value of 'CURRENT_DEF'
echo $::env(CURRENT_DEF)

# Check value of 'ROUTING_STRATEGY'
echo $::env(ROUTING_STRATEGY)

# Command for detailed route using TritonRoute
run_routing
```

Screenshots of routing run

![Screenshot from 2024-03-26 15-38-39](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2018-55-30.png)
![Screenshot from 2024-03-26 15-29-38](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week6/Images/Screenshot%20from%202025-11-11%2019-16-12.png)


* [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
* [Nickson P Jose](https://github.com/nickson-jose), Physical Design Engineer, Intel Corporation.
* [R. Timothy Edwards](https://github.com/RTimothyEdwards), Senior Vice President of Analog and Design, efabless Corporation.


---

# /mnt/data/silicon_repo/silicon-diary-main/Week6/Images/Readme.md




# Week7

# /mnt/data/silicon_repo/silicon-diary-main/Week7/Readme.md


**ORFS Directory Structure and File formats**
``` 
├── OpenROAD-flow-scripts             
│   ├── docker           -> It has Docker based installation, run scripts and all saved here
│   ├── docs             -> Documentation for OpenROAD or its flow scripts.  
│   ├── flow             -> Files related to run RTL to GDS flow  
|   ├── jenkins          -> It contains the regression test designed for each build update
│   ├── tools            -> It contains all the required tools to run RTL to GDS flow
│   ├── etc              -> Has the dependency installer script and other things
│   ├── setup_env.sh     -> Its the source file to source all our OpenROAD rules to run the RTL to GDS flow
```
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2002-13-07.png)
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2019-21-00.png)
Now, go to flow directory

``` 
├── flow           
│   ├── design           -> It has built-in examples from RTL to GDS flow across different technology nodes
│   ├── makefile         -> The automated flow runs through makefile setup
│   ├── platform         -> It has different technology note libraries, lef files, GDS etc 
|   ├── tutorials        
│   ├── util            
│   ├── scripts             
```

Automated RTL2GDS Flow for VSDBabySoC:

Initial Steps:

- We need to create a directory `vsdbabysoc` inside `OpenROAD-flow-scripts/flow/designs/sky130hd`
- Now create a directory `vsdbabysoc` inside `OpenROAD-flow-scripts/flow/designs/src` and include all the verilog files here.
- Now copy the folders `gds`, `include`, `lef` and `lib` from the VSDBabySoC folder in your system into this directory.
  - The `gds` folder would contain the files `avsddac.gds` and `avsdpll.gds`
  - The `include` folder would contain the files `sandpiper.vh`, `sandpiper_gen.vh`, `sp_default.vh` and `sp_verilog.vh`
  - The folder would contain the files `avsddac.lef` and `avsdpll.lef`
  - The `lib` folder would contain the files `avsddac.lib` and `avsdpll.lib`
- Now copy the constraints file(`vsdbabysoc_synthesis.sdc`) from the VSDBabySoC folder in your system into this directory.
- Now copy the files(`macro.cfg` and `pin_order.cfg`) from the VSDBabySoC folder in your system into this directory.
- Now, create a `config.mk` file whose contents are shown below:

```
##############################################
#   vsdbabysoc CONFIGURATION (Sky130HD)
##############################################

export DESIGN_NICKNAME = vsdbabysoc
export DESIGN_NAME     = vsdbabysoc
export PLATFORM        = sky130hd

export vsdbabysoc_DIR = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)

##############################################
#   RTL / LIB / LEF INPUTS
##############################################

export VERILOG_FILES = \
    $(vsdbabysoc_DIR)/src/module/vsdbabysoc.v \
    $(vsdbabysoc_DIR)/src/module/rvmyth.v \
    $(vsdbabysoc_DIR)/src/module/clk_gate.v

export VERILOG_INCLUDE_DIRS = $(wildcard $(vsdbabysoc_DIR)/include/)

export SDC_FILE = $(vsdbabysoc_DIR)/vsdbabysoc_synthesis.sdc

export ADDITIONAL_LIBS = \
    $(vsdbabysoc_DIR)/lib/avsddac.lib \
    $(vsdbabysoc_DIR)/lib/avsdpll.lib

# Use TRIMMED LEFs (must be placed inside the LEF folder)
export ADDITIONAL_LEFS = \
    $(vsdbabysoc_DIR)/lef/avsddac.lef \
    $(vsdbabysoc_DIR)/lef/avsdpll.lef

# Optional routing blockages TCL
export ADDITIONAL_ROUTING_BLOCKAGES = $(vsdbabysoc_DIR)/route_blockages.tcl


##############################################
#   DIE / CORE AREA
##############################################

# Increased die size to reduce global route overflow
export DIE_AREA  = 0   0   1800 1800
export CORE_AREA = 20  20  1780 1780


##############################################
#   PLACEMENT PARAMETERS
##############################################

# Useful for lowering density with macros in design
export FP_CORE_UTIL  = 40
export PLACE_DENSITY = 0.30

# Stronger macro halo for easier routing
export MACRO_PLACE_HALO    = 40 40
export MACRO_PLACE_CHANNEL = 40 40

# RTLMP disabled
export RTLMP_FLOW = 0

# External macro placement
export MACRO_PLACEMENT = $(vsdbabysoc_DIR)/macro.cfg


##############################################
#   CLOCK SETTINGS
##############################################

export CLOCK_PORT = CLK
export CLOCK_NET  = CLK

export CTS_BUF_DISTANCE  = 600
export SKIP_GATE_CLONING = 1


##############################################
#   ROUTING (GRT) — FIXES GRT-0116
##############################################

# Allow congestion but continue iterations
export GRT_ALLOW_CONGESTION      = 1
export GRT_SKIP_CONGESTION_CHECK = 0
export GRT_CONGESTION_DRIVEN     = 1

# Stable iteration counts (700 was too high)
export GRT_MAX_ITERATIONS = 150

# Adjust routing resources to ease congestion
export GRT_ADJUSTMENT = 0.25

# Via cost (helps with overflow)
export GRT_VIA_COST_ADJUSTMENT = 2.0

# Allow full runtime
export GRT_MAX_TIME = 3600

# DO NOT STOP on overflow during debug
export GRT_FAIL_ON_OVERFLOW = 0
export GRT_OVERFLOW_ITERS   = 100


##############################################
#   MISC OPTIONS
##############################################

export TNS_END_PERCENT      = 100
export REMOVE_ABC_BUFFERS   = 1
export MAGIC_ZEROIZE_ORIGIN = 0
export MAGIC_EXT_USE_GDS    = 1
export RCX_EXTRACT=1
export RCX_CORNER=typical
export RCX_SPEF_OUTPUT=1

export SPEF_OUTPUT_FILE = $(vsdbabysoc_DIR)/vsdbabysoc.spef
```
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2019-22-42.png)
Now go to terminal and run the following commands:

```
cd OpenROAD-flow-scripts
source env.sh
cd flow
```

Commands for **synthesis**:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk synth
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-22-13.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-22-55.png)

Synthesis netlist:

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-29-54.png)

Synthesis Check:

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-36-14.png)

Synthesis Stats:

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-36-19.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-37-29.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-37-36.png)

Commands for **floorplan**:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk floorplan
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-38-11.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-40-38.png)

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_floorplan
```
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-52-13.png)

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk place
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-52-43.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2022-56-17.png)

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_place
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-04-41.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-05-34.png)

Heatmap:

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-13-25.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-15-55.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-18-01.png)


```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk cts
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-18-39.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-19-16.png)

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_cts
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-21-26.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-25-16.png)



CTS final report:

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-27-39.png)


```

==========================================================================
cts final report_tns
--------------------------------------------------------------------------
tns 0.00

==========================================================================
cts final report_wns
--------------------------------------------------------------------------
wns 0.00

==========================================================================
cts final report_worst_slack
--------------------------------------------------------------------------
worst slack 5.55

==========================================================================
cts final report_clock_skew
--------------------------------------------------------------------------
Clock clk
   0.92 source latency core.CPU_result_a4[0]$_DFF_P_/CLK ^
  -0.82 target latency core.CPU_Dmem_value_a5[0][18]$_SDFFE_PP0P_/CLK ^
   0.55 clock uncertainty
   0.00 CRPR
--------------
   0.65 setup skew


==========================================================================
cts final report_checks -path_delay min
--------------------------------------------------------------------------
Startpoint: core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_src2_value_a3[15]$_DFF_P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: min

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_7_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.20    0.47 ^ clkbuf_3_7_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_7_0_CLK (net)
                  0.06    0.00    0.47 ^ clkbuf_4_14__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    13    0.17    0.18    0.24    0.71 ^ clkbuf_4_14__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_14__leaf_CLK (net)
                  0.18    0.00    0.71 ^ clkbuf_leaf_108_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.04    0.06    0.19    0.90 ^ clkbuf_leaf_108_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_108_CLK (net)
                  0.06    0.00    0.90 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     2    0.01    0.06    0.32    1.22 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_Xreg_value_a4[25][15] (net)
                  0.06    0.00    1.22 ^ _14708_/A1 (sky130_fd_sc_hd__a21oi_1)
     1    0.00    0.04    0.06    1.28 v _14708_/Y (sky130_fd_sc_hd__a21oi_1)
                                         _02012_ (net)
                  0.04    0.00    1.28 v _14712_/A (sky130_fd_sc_hd__nand4_1)
     1    0.01    0.13    0.12    1.40 ^ _14712_/Y (sky130_fd_sc_hd__nand4_1)
                                         _02016_ (net)
                  0.13    0.00    1.40 ^ _14729_/A1 (sky130_fd_sc_hd__o32ai_4)
     1    0.04    0.12    0.18    1.58 v _14729_/Y (sky130_fd_sc_hd__o32ai_4)
                                         _02033_ (net)
                  0.12    0.00    1.59 v _14731_/A2 (sky130_fd_sc_hd__o21ai_0)
     1    0.00    0.06    0.16    1.74 ^ _14731_/Y (sky130_fd_sc_hd__o21ai_0)
                                         core.CPU_src2_value_a2[15] (net)
                  0.06    0.00    1.74 ^ core.CPU_src2_value_a3[15]$_DFF_P_/D (sky130_fd_sc_hd__dfxtp_2)
                                  1.74   data arrival time

                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21    0.47 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00    0.47 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24    0.71 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00    0.71 ^ clkbuf_leaf_70_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.04    0.06    0.18    0.89 ^ clkbuf_leaf_70_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_70_CLK (net)
                  0.06    0.00    0.89 ^ core.CPU_src2_value_a3[15]$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_2)
                          0.88    1.78   clock uncertainty
                          0.00    1.78   clock reconvergence pessimism
                         -0.03    1.74   library hold time
                                  1.74   data required time
-----------------------------------------------------------------------------
                                  1.74   data required time
                                 -1.74   data arrival time
-----------------------------------------------------------------------------
                                  0.00   slack (MET)



==========================================================================
cts final report_checks -path_delay max
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_4_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.07    0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_4_0_CLK (net)
                  0.07    0.00    0.47 ^ clkbuf_4_8__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.15    0.16    0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_8__leaf_CLK (net)
                  0.16    0.00    0.70 ^ clkbuf_leaf_149_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    15    0.04    0.06    0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_149_CLK (net)
                  0.06    0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     1    0.00    0.03    0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_valid_taken_br_a5 (net)
                  0.03    0.00    1.18 v _07913_/A (sky130_fd_sc_hd__or4_4)
    19    0.22    0.35    0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
                                         _02930_ (net)
                  0.35    0.01    2.02 v _07915_/A (sky130_fd_sc_hd__clkinv_16)
    43    0.45    0.31    0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
                                         _02932_ (net)
                  0.31    0.02    2.39 ^ _09981_/C (sky130_fd_sc_hd__nor3_2)
     2    0.02    0.10    0.14    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
                                         _04371_ (net)
                  0.10    0.00    2.53 v _09982_/B1 (sky130_fd_sc_hd__a21oi_4)
     6    0.10    0.70    0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
                                         _04372_ (net)
                  0.70    0.00    3.10 ^ _09988_/A2 (sky130_fd_sc_hd__o21ai_4)
    16    0.12    0.33    0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
                                         _04378_ (net)
                  0.33    0.00    3.48 v _13552_/A (sky130_fd_sc_hd__nor3_4)
    23    0.14    1.37    1.19    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
                                         _07042_ (net)
                  1.37    0.00    4.67 ^ _13572_/B (sky130_fd_sc_hd__nand2_2)
     5    0.03    0.29    0.30    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
                                         _07058_ (net)
                  0.29    0.00    4.98 v _13574_/B1 (sky130_fd_sc_hd__o221ai_1)
     1    0.00    0.20    0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
                                         _01444_ (net)
                  0.20    0.00    5.22 ^ hold2174/A (sky130_fd_sc_hd__dlygate4sd3_1)
     1    0.00    0.05    0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
                                         net2283 (net)
                  0.05    0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
                                  5.79   data arrival time

                         11.05   11.05   clock clk (rise edge)
                          0.00   11.05   clock source latency
     1    0.10    0.00    0.00   11.05 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00   11.05 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00   11.31 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00   11.52 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00   11.76 ^ clkbuf_leaf_90_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.04    0.06    0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_90_CLK (net)
                  0.06    0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
                         -0.55   11.39   clock uncertainty
                          0.00   11.39   clock reconvergence pessimism
                         -0.05   11.34   library setup time
                                 11.34   data required time
-----------------------------------------------------------------------------
                                 11.34   data required time
                                 -5.79   data arrival time
-----------------------------------------------------------------------------
                                  5.55   slack (MET)



==========================================================================
cts final report_checks -unconstrained
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_4_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.07    0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_4_0_CLK (net)
                  0.07    0.00    0.47 ^ clkbuf_4_8__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.15    0.16    0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_8__leaf_CLK (net)
                  0.16    0.00    0.70 ^ clkbuf_leaf_149_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    15    0.04    0.06    0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_149_CLK (net)
                  0.06    0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     1    0.00    0.03    0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_valid_taken_br_a5 (net)
                  0.03    0.00    1.18 v _07913_/A (sky130_fd_sc_hd__or4_4)
    19    0.22    0.35    0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
                                         _02930_ (net)
                  0.35    0.01    2.02 v _07915_/A (sky130_fd_sc_hd__clkinv_16)
    43    0.45    0.31    0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
                                         _02932_ (net)
                  0.31    0.02    2.39 ^ _09981_/C (sky130_fd_sc_hd__nor3_2)
     2    0.02    0.10    0.14    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
                                         _04371_ (net)
                  0.10    0.00    2.53 v _09982_/B1 (sky130_fd_sc_hd__a21oi_4)
     6    0.10    0.70    0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
                                         _04372_ (net)
                  0.70    0.00    3.10 ^ _09988_/A2 (sky130_fd_sc_hd__o21ai_4)
    16    0.12    0.33    0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
                                         _04378_ (net)
                  0.33    0.00    3.48 v _13552_/A (sky130_fd_sc_hd__nor3_4)
    23    0.14    1.37    1.19    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
                                         _07042_ (net)
                  1.37    0.00    4.67 ^ _13572_/B (sky130_fd_sc_hd__nand2_2)
     5    0.03    0.29    0.30    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
                                         _07058_ (net)
                  0.29    0.00    4.98 v _13574_/B1 (sky130_fd_sc_hd__o221ai_1)
     1    0.00    0.20    0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
                                         _01444_ (net)
                  0.20    0.00    5.22 ^ hold2174/A (sky130_fd_sc_hd__dlygate4sd3_1)
     1    0.00    0.05    0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
                                         net2283 (net)
                  0.05    0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
                                  5.79   data arrival time

                         11.05   11.05   clock clk (rise edge)
                          0.00   11.05   clock source latency
     1    0.10    0.00    0.00   11.05 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00   11.05 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00   11.31 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00   11.52 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00   11.76 ^ clkbuf_leaf_90_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.04    0.06    0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_90_CLK (net)
                  0.06    0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
                         -0.55   11.39   clock uncertainty
                          0.00   11.39   clock reconvergence pessimism
                         -0.05   11.34   library setup time
                                 11.34   data required time
-----------------------------------------------------------------------------
                                 11.34   data required time
                                 -5.79   data arrival time
-----------------------------------------------------------------------------
                                  5.55   slack (MET)



==========================================================================
cts final report_check_types -max_slew -max_cap -max_fanout -violators
--------------------------------------------------------------------------
max capacitance

Pin                                    Limit     Cap   Slack
------------------------------------------------------------
_13743_/Y                               0.15    0.15   -0.00 (VIOLATED)
_13455_/Y                               0.15    0.15   -0.00 (VIOLATED)


==========================================================================
cts final max_slew_check_slack
--------------------------------------------------------------------------
0.02021305449306965

==========================================================================
cts final max_slew_check_limit
--------------------------------------------------------------------------
1.4951449632644653

==========================================================================
cts final max_slew_check_slack_limit
--------------------------------------------------------------------------
0.0135

==========================================================================
cts final max_fanout_check_slack
--------------------------------------------------------------------------
1.0000000150474662e+30

==========================================================================
cts final max_fanout_check_limit
--------------------------------------------------------------------------
1.0000000150474662e+30

==========================================================================
cts final max_capacitance_check_slack
--------------------------------------------------------------------------
-0.001024815021082759

==========================================================================
cts final max_capacitance_check_limit
--------------------------------------------------------------------------
0.1538189947605133

==========================================================================
cts final max_capacitance_check_slack_limit
--------------------------------------------------------------------------
-0.0067

==========================================================================
cts final max_slew_violation_count
--------------------------------------------------------------------------
max slew violation count 0

==========================================================================
cts final max_fanout_violation_count
--------------------------------------------------------------------------
max fanout violation count 0

==========================================================================
cts final max_cap_violation_count
--------------------------------------------------------------------------
max cap violation count 2

==========================================================================
cts final setup_violation_count
--------------------------------------------------------------------------
setup violation count 0

==========================================================================
cts final hold_violation_count
--------------------------------------------------------------------------
hold violation count 0

==========================================================================
cts final report_checks -path_delay max reg to reg
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
   0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
   0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
   0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
   0.15    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
   0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
   0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
   1.20    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
   0.31    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
   0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
   0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
   0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
           5.79   data arrival time

  11.05   11.05   clock clk (rise edge)
   0.00   11.05   clock source latency
   0.00   11.05 ^ pll/CLK (avsdpll)
   0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
  -0.55   11.39   clock uncertainty
   0.00   11.39   clock reconvergence pessimism
  -0.05   11.34   library setup time
          11.34   data required time
---------------------------------------------------------
          11.34   data required time
          -5.79   data arrival time
---------------------------------------------------------
           5.55   slack (MET)



==========================================================================
cts final report_checks -path_delay min reg to reg
--------------------------------------------------------------------------
Startpoint: core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_src2_value_a3[15]$_DFF_P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: min

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_7_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24    0.71 ^ clkbuf_4_14__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19    0.90 ^ clkbuf_leaf_108_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.90 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
   0.32    1.22 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/Q (sky130_fd_sc_hd__dfxtp_1)
   0.06    1.28 v _14708_/Y (sky130_fd_sc_hd__a21oi_1)
   0.12    1.40 ^ _14712_/Y (sky130_fd_sc_hd__nand4_1)
   0.18    1.58 v _14729_/Y (sky130_fd_sc_hd__o32ai_4)
   0.16    1.74 ^ _14731_/Y (sky130_fd_sc_hd__o21ai_0)
   0.00    1.74 ^ core.CPU_src2_value_a3[15]$_DFF_P_/D (sky130_fd_sc_hd__dfxtp_2)
           1.74   data arrival time

   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24    0.71 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19    0.89 ^ clkbuf_leaf_70_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.89 ^ core.CPU_src2_value_a3[15]$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_2)
   0.88    1.78   clock uncertainty
   0.00    1.78   clock reconvergence pessimism
  -0.03    1.74   library hold time
           1.74   data required time
---------------------------------------------------------
           1.74   data required time
          -1.74   data arrival time
---------------------------------------------------------
           0.00   slack (MET)



==========================================================================
cts final critical path target clock latency max path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path target clock latency min path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path source clock latency min path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path delay
--------------------------------------------------------------------------
5.7921

==========================================================================
cts final critical path slack
--------------------------------------------------------------------------
5.5454

==========================================================================
cts final slack div critical path delay
--------------------------------------------------------------------------
95.740750

==========================================================================
cts final report_power
--------------------------------------------------------------------------
Group                  Internal  Switching    Leakage      Total
                          Power      Power      Power      Power (Watts)
----------------------------------------------------------------
Sequential             6.95e-03   9.72e-04   1.45e-08   7.92e-03  37.7%
Combinational          2.12e-03   4.52e-03   3.05e-08   6.64e-03  31.6%
Clock                  3.66e-03   2.76e-03   2.96e-09   6.42e-03  30.6%
Macro                  0.00e+00   0.00e+00   0.00e+00   0.00e+00   0.0%
Pad                    0.00e+00   0.00e+00   0.00e+00   0.00e+00   0.0%
----------------------------------------------------------------
Total                  1.27e-02   8.25e-03   4.80e-08   2.10e-02 100.0%
                          60.7%      39.3%       0.0%
```

Route:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk route
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-28-42.png)

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-23%2016-14-12.png)

### For resolving error [ERROR GRT-0116] Global routing finished with congestion

i updated the config.mk which one i already uploaded and alco make cnages inside lef files which is also available in this week repo 

### Extracting SPEF File 

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk final
```

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-24%2023-21-23.png)


---

# /mnt/data/silicon_repo/silicon-diary-main/Week7/Images/Readme.md

**ORFS Directory Structure and File formats**

![image]()


``` 
├── OpenROAD-flow-scripts             
│   ├── docker           -> It has Docker based installation, run scripts and all saved here
│   ├── docs             -> Documentation for OpenROAD or its flow scripts.  
│   ├── flow             -> Files related to run RTL to GDS flow  
|   ├── jenkins          -> It contains the regression test designed for each build update
│   ├── tools            -> It contains all the required tools to run RTL to GDS flow
│   ├── etc              -> Has the dependency installer script and other things
│   ├── setup_env.sh     -> Its the source file to source all our OpenROAD rules to run the RTL to GDS flow
```

Now, go to flow directory

![image]()

``` 
├── flow           
│   ├── design           -> It has built-in examples from RTL to GDS flow across different technology nodes
│   ├── makefile         -> The automated flow runs through makefile setup
│   ├── platform         -> It has different technology note libraries, lef files, GDS etc 
|   ├── tutorials        
│   ├── util            
│   ├── scripts             
```

Automated RTL2GDS Flow for VSDBabySoC:

Initial Steps:

- We need to create a directory `vsdbabysoc` inside `OpenROAD-flow-scripts/flow/designs/sky130hd`
- Now create a directory `vsdbabysoc` inside `OpenROAD-flow-scripts/flow/designs/src` and include all the verilog files here.
- Now copy the folders `gds`, `include`, `lef` and `lib` from the VSDBabySoC folder in your system into this directory.
  - The `gds` folder would contain the files `avsddac.gds` and `avsdpll.gds`
  - The `include` folder would contain the files `sandpiper.vh`, `sandpiper_gen.vh`, `sp_default.vh` and `sp_verilog.vh`
  - The folder would contain the files `avsddac.lef` and `avsdpll.lef`
  - The `lib` folder would contain the files `avsddac.lib` and `avsdpll.lib`
- Now copy the constraints file(`vsdbabysoc_synthesis.sdc`) from the VSDBabySoC folder in your system into this directory.
- Now copy the files(`macro.cfg` and `pin_order.cfg`) from the VSDBabySoC folder in your system into this directory.
- Now, create a `config.mk` file whose contents are shown below:

```
export DESIGN_NICKNAME = vsdbabysoc
export DESIGN_NAME = vsdbabysoc
export PLATFORM    = sky130hd

# export VERILOG_FILES_BLACKBOX = $(DESIGN_HOME)/src/$(DESIGN_NICKNAME)/IPs/*.v
# export VERILOG_FILES = $(sort $(wildcard $(DESIGN_HOME)/src/$(DESIGN_NICKNAME)/*.v))
# Explicitly list the Verilog files for synthesis
export VERILOG_FILES = $(DESIGN_HOME)/src/$(DESIGN_NICKNAME)/vsdbabysoc.v \
                       $(DESIGN_HOME)/src/$(DESIGN_NICKNAME)/rvmyth.v \
                       $(DESIGN_HOME)/src/$(DESIGN_NICKNAME)/clk_gate.v

export SDC_FILE      = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)/vsdbabysoc_synthesis.sdc

export vsdbabysoc_DIR = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)

export VERILOG_INCLUDE_DIRS = $(wildcard $(vsdbabysoc_DIR)/include/)
# export SDC_FILE      = $(wildcard $(vsdbabysoc_DIR)/sdc/*.sdc)
export ADDITIONAL_GDS  = $(wildcard $(vsdbabysoc_DIR)/gds/*.gds.gz)
export ADDITIONAL_LEFS  = $(wildcard $(vsdbabysoc_DIR)/lef/*.lef)
export ADDITIONAL_LIBS = $(wildcard $(vsdbabysoc_DIR)/lib/*.lib)
# export PDN_TCL = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)/pdn.tcl

# Clock Configuration (vsdbabysoc specific)
# export CLOCK_PERIOD = 20.0
export CLOCK_PORT = CLK
export CLOCK_NET = $(CLOCK_PORT)

# Floorplanning Configuration (vsdbabysoc specific)
export FP_PIN_ORDER_CFG = $(wildcard $(DESIGN_DIR)/pin_order.cfg)
# export FP_SIZING = absolute

export DIE_AREA   = 0 0 1600 1600
export CORE_AREA  = 20 20 1590 1590

# Placement Configuration (vsdbabysoc specific)
export MACRO_PLACEMENT_CFG = $(wildcard $(DESIGN_DIR)/macro.cfg)
export PLACE_PINS_ARGS = -exclude left:0-600 -exclude left:1000-1600: -exclude right:* -exclude top:* -exclude bottom:*
# export MACRO_PLACEMENT = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)/macro_placement.cfg

export TNS_END_PERCENT = 100
export REMOVE_ABC_BUFFERS = 1

# Magic Tool Configuration
export MAGIC_ZEROIZE_ORIGIN = 0
export MAGIC_EXT_USE_GDS = 1

# CTS tuning
export CTS_BUF_DISTANCE = 600
export SKIP_GATE_CLONING = 1

# export CORE_UTILIZATION=0.1  # Reduce this value to allow more whitespace for routing.
```

Now go to terminal and run the following commands:

```
cd OpenROAD-flow-scripts
source env.sh
cd flow
```

Commands for **synthesis**:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk synth
```

![image]()

![image]()

Synthesis netlist:

![image]()

Synthesis log:

![image]()

Synthesis Check:

![image]()

Synthesis Stats:

![image]()

![image]()

![image]()

![image]()

Commands for **floorplan**:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk floorplan
```

![image]()

![image]()

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_floorplan
```
![image]()

![image]()

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk place
```

![image]()

![image]()

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_place
```

![image]()

![image]()

Heatmap:

![image]()

![image]()

![image]()


```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk cts
```

![image]()

![image]()

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_cts
```

![image]()

![image]()

![image]()

CTS final report:

![image]()


```

==========================================================================
cts final report_tns
--------------------------------------------------------------------------
tns 0.00

==========================================================================
cts final report_wns
--------------------------------------------------------------------------
wns 0.00

==========================================================================
cts final report_worst_slack
--------------------------------------------------------------------------
worst slack 5.55

==========================================================================
cts final report_clock_skew
--------------------------------------------------------------------------
Clock clk
   0.92 source latency core.CPU_result_a4[0]$_DFF_P_/CLK ^
  -0.82 target latency core.CPU_Dmem_value_a5[0][18]$_SDFFE_PP0P_/CLK ^
   0.55 clock uncertainty
   0.00 CRPR
--------------
   0.65 setup skew


==========================================================================
cts final report_checks -path_delay min
--------------------------------------------------------------------------
Startpoint: core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_src2_value_a3[15]$_DFF_P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: min

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_7_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.20    0.47 ^ clkbuf_3_7_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_7_0_CLK (net)
                  0.06    0.00    0.47 ^ clkbuf_4_14__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    13    0.17    0.18    0.24    0.71 ^ clkbuf_4_14__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_14__leaf_CLK (net)
                  0.18    0.00    0.71 ^ clkbuf_leaf_108_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.04    0.06    0.19    0.90 ^ clkbuf_leaf_108_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_108_CLK (net)
                  0.06    0.00    0.90 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     2    0.01    0.06    0.32    1.22 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_Xreg_value_a4[25][15] (net)
                  0.06    0.00    1.22 ^ _14708_/A1 (sky130_fd_sc_hd__a21oi_1)
     1    0.00    0.04    0.06    1.28 v _14708_/Y (sky130_fd_sc_hd__a21oi_1)
                                         _02012_ (net)
                  0.04    0.00    1.28 v _14712_/A (sky130_fd_sc_hd__nand4_1)
     1    0.01    0.13    0.12    1.40 ^ _14712_/Y (sky130_fd_sc_hd__nand4_1)
                                         _02016_ (net)
                  0.13    0.00    1.40 ^ _14729_/A1 (sky130_fd_sc_hd__o32ai_4)
     1    0.04    0.12    0.18    1.58 v _14729_/Y (sky130_fd_sc_hd__o32ai_4)
                                         _02033_ (net)
                  0.12    0.00    1.59 v _14731_/A2 (sky130_fd_sc_hd__o21ai_0)
     1    0.00    0.06    0.16    1.74 ^ _14731_/Y (sky130_fd_sc_hd__o21ai_0)
                                         core.CPU_src2_value_a2[15] (net)
                  0.06    0.00    1.74 ^ core.CPU_src2_value_a3[15]$_DFF_P_/D (sky130_fd_sc_hd__dfxtp_2)
                                  1.74   data arrival time

                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21    0.47 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00    0.47 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24    0.71 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00    0.71 ^ clkbuf_leaf_70_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.04    0.06    0.18    0.89 ^ clkbuf_leaf_70_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_70_CLK (net)
                  0.06    0.00    0.89 ^ core.CPU_src2_value_a3[15]$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_2)
                          0.88    1.78   clock uncertainty
                          0.00    1.78   clock reconvergence pessimism
                         -0.03    1.74   library hold time
                                  1.74   data required time
-----------------------------------------------------------------------------
                                  1.74   data required time
                                 -1.74   data arrival time
-----------------------------------------------------------------------------
                                  0.00   slack (MET)



==========================================================================
cts final report_checks -path_delay max
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_4_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.07    0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_4_0_CLK (net)
                  0.07    0.00    0.47 ^ clkbuf_4_8__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.15    0.16    0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_8__leaf_CLK (net)
                  0.16    0.00    0.70 ^ clkbuf_leaf_149_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    15    0.04    0.06    0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_149_CLK (net)
                  0.06    0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     1    0.00    0.03    0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_valid_taken_br_a5 (net)
                  0.03    0.00    1.18 v _07913_/A (sky130_fd_sc_hd__or4_4)
    19    0.22    0.35    0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
                                         _02930_ (net)
                  0.35    0.01    2.02 v _07915_/A (sky130_fd_sc_hd__clkinv_16)
    43    0.45    0.31    0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
                                         _02932_ (net)
                  0.31    0.02    2.39 ^ _09981_/C (sky130_fd_sc_hd__nor3_2)
     2    0.02    0.10    0.14    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
                                         _04371_ (net)
                  0.10    0.00    2.53 v _09982_/B1 (sky130_fd_sc_hd__a21oi_4)
     6    0.10    0.70    0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
                                         _04372_ (net)
                  0.70    0.00    3.10 ^ _09988_/A2 (sky130_fd_sc_hd__o21ai_4)
    16    0.12    0.33    0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
                                         _04378_ (net)
                  0.33    0.00    3.48 v _13552_/A (sky130_fd_sc_hd__nor3_4)
    23    0.14    1.37    1.19    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
                                         _07042_ (net)
                  1.37    0.00    4.67 ^ _13572_/B (sky130_fd_sc_hd__nand2_2)
     5    0.03    0.29    0.30    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
                                         _07058_ (net)
                  0.29    0.00    4.98 v _13574_/B1 (sky130_fd_sc_hd__o221ai_1)
     1    0.00    0.20    0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
                                         _01444_ (net)
                  0.20    0.00    5.22 ^ hold2174/A (sky130_fd_sc_hd__dlygate4sd3_1)
     1    0.00    0.05    0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
                                         net2283 (net)
                  0.05    0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
                                  5.79   data arrival time

                         11.05   11.05   clock clk (rise edge)
                          0.00   11.05   clock source latency
     1    0.10    0.00    0.00   11.05 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00   11.05 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00   11.31 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00   11.52 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00   11.76 ^ clkbuf_leaf_90_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.04    0.06    0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_90_CLK (net)
                  0.06    0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
                         -0.55   11.39   clock uncertainty
                          0.00   11.39   clock reconvergence pessimism
                         -0.05   11.34   library setup time
                                 11.34   data required time
-----------------------------------------------------------------------------
                                 11.34   data required time
                                 -5.79   data arrival time
-----------------------------------------------------------------------------
                                  5.55   slack (MET)



==========================================================================
cts final report_checks -unconstrained
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Fanout     Cap    Slew   Delay    Time   Description
-----------------------------------------------------------------------------
                          0.00    0.00   clock clk (rise edge)
                          0.00    0.00   clock source latency
     1    0.10    0.00    0.00    0.00 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00    0.00 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00    0.26 ^ clkbuf_3_4_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.07    0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_4_0_CLK (net)
                  0.07    0.00    0.47 ^ clkbuf_4_8__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.15    0.16    0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_8__leaf_CLK (net)
                  0.16    0.00    0.70 ^ clkbuf_leaf_149_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    15    0.04    0.06    0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_149_CLK (net)
                  0.06    0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
     1    0.00    0.03    0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
                                         core.CPU_valid_taken_br_a5 (net)
                  0.03    0.00    1.18 v _07913_/A (sky130_fd_sc_hd__or4_4)
    19    0.22    0.35    0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
                                         _02930_ (net)
                  0.35    0.01    2.02 v _07915_/A (sky130_fd_sc_hd__clkinv_16)
    43    0.45    0.31    0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
                                         _02932_ (net)
                  0.31    0.02    2.39 ^ _09981_/C (sky130_fd_sc_hd__nor3_2)
     2    0.02    0.10    0.14    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
                                         _04371_ (net)
                  0.10    0.00    2.53 v _09982_/B1 (sky130_fd_sc_hd__a21oi_4)
     6    0.10    0.70    0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
                                         _04372_ (net)
                  0.70    0.00    3.10 ^ _09988_/A2 (sky130_fd_sc_hd__o21ai_4)
    16    0.12    0.33    0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
                                         _04378_ (net)
                  0.33    0.00    3.48 v _13552_/A (sky130_fd_sc_hd__nor3_4)
    23    0.14    1.37    1.19    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
                                         _07042_ (net)
                  1.37    0.00    4.67 ^ _13572_/B (sky130_fd_sc_hd__nand2_2)
     5    0.03    0.29    0.30    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
                                         _07058_ (net)
                  0.29    0.00    4.98 v _13574_/B1 (sky130_fd_sc_hd__o221ai_1)
     1    0.00    0.20    0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
                                         _01444_ (net)
                  0.20    0.00    5.22 ^ hold2174/A (sky130_fd_sc_hd__dlygate4sd3_1)
     1    0.00    0.05    0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
                                         net2283 (net)
                  0.05    0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
                                  5.79   data arrival time

                         11.05   11.05   clock clk (rise edge)
                          0.00   11.05   clock source latency
     1    0.10    0.00    0.00   11.05 ^ pll/CLK (avsdpll)
                                         CLK (net)
                  0.00    0.00   11.05 ^ clkbuf_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     8    0.23    0.24    0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_0_CLK (net)
                  0.24    0.00   11.31 ^ clkbuf_3_6_0_CLK/A (sky130_fd_sc_hd__clkbuf_16)
     2    0.04    0.06    0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_3_6_0_CLK (net)
                  0.06    0.00   11.52 ^ clkbuf_4_13__f_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    12    0.16    0.18    0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_4_13__leaf_CLK (net)
                  0.18    0.00   11.76 ^ clkbuf_leaf_90_CLK/A (sky130_fd_sc_hd__clkbuf_16)
    11    0.04    0.06    0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
                                         clknet_leaf_90_CLK (net)
                  0.06    0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
                         -0.55   11.39   clock uncertainty
                          0.00   11.39   clock reconvergence pessimism
                         -0.05   11.34   library setup time
                                 11.34   data required time
-----------------------------------------------------------------------------
                                 11.34   data required time
                                 -5.79   data arrival time
-----------------------------------------------------------------------------
                                  5.55   slack (MET)



==========================================================================
cts final report_check_types -max_slew -max_cap -max_fanout -violators
--------------------------------------------------------------------------
max capacitance

Pin                                    Limit     Cap   Slack
------------------------------------------------------------
_13743_/Y                               0.15    0.15   -0.00 (VIOLATED)
_13455_/Y                               0.15    0.15   -0.00 (VIOLATED)


==========================================================================
cts final max_slew_check_slack
--------------------------------------------------------------------------
0.02021305449306965

==========================================================================
cts final max_slew_check_limit
--------------------------------------------------------------------------
1.4951449632644653

==========================================================================
cts final max_slew_check_slack_limit
--------------------------------------------------------------------------
0.0135

==========================================================================
cts final max_fanout_check_slack
--------------------------------------------------------------------------
1.0000000150474662e+30

==========================================================================
cts final max_fanout_check_limit
--------------------------------------------------------------------------
1.0000000150474662e+30

==========================================================================
cts final max_capacitance_check_slack
--------------------------------------------------------------------------
-0.001024815021082759

==========================================================================
cts final max_capacitance_check_limit
--------------------------------------------------------------------------
0.1538189947605133

==========================================================================
cts final max_capacitance_check_slack_limit
--------------------------------------------------------------------------
-0.0067

==========================================================================
cts final max_slew_violation_count
--------------------------------------------------------------------------
max slew violation count 0

==========================================================================
cts final max_fanout_violation_count
--------------------------------------------------------------------------
max fanout violation count 0

==========================================================================
cts final max_cap_violation_count
--------------------------------------------------------------------------
max cap violation count 2

==========================================================================
cts final setup_violation_count
--------------------------------------------------------------------------
setup violation count 0

==========================================================================
cts final hold_violation_count
--------------------------------------------------------------------------
hold violation count 0

==========================================================================
cts final report_checks -path_delay max reg to reg
--------------------------------------------------------------------------
Startpoint: core.CPU_valid_taken_br_a5$_DFF_P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_4_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.23    0.70 ^ clkbuf_4_8__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.18    0.88 ^ clkbuf_leaf_149_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.88 ^ core.CPU_valid_taken_br_a5$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_1)
   0.30    1.18 v core.CPU_valid_taken_br_a5$_DFF_P_/Q (sky130_fd_sc_hd__dfxtp_1)
   0.83    2.01 v _07913_/X (sky130_fd_sc_hd__or4_4)
   0.36    2.38 ^ _07915_/Y (sky130_fd_sc_hd__clkinv_16)
   0.15    2.53 v _09981_/Y (sky130_fd_sc_hd__nor3_2)
   0.57    3.10 ^ _09982_/Y (sky130_fd_sc_hd__a21oi_4)
   0.38    3.47 v _09988_/Y (sky130_fd_sc_hd__o21ai_4)
   1.20    4.67 ^ _13552_/Y (sky130_fd_sc_hd__nor3_4)
   0.31    4.98 v _13572_/Y (sky130_fd_sc_hd__nand2_2)
   0.24    5.22 ^ _13574_/Y (sky130_fd_sc_hd__o221ai_1)
   0.57    5.79 ^ hold2174/X (sky130_fd_sc_hd__dlygate4sd3_1)
   0.00    5.79 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/D (sky130_fd_sc_hd__dfxtp_1)
           5.79   data arrival time

  11.05   11.05   clock clk (rise edge)
   0.00   11.05   clock source latency
   0.00   11.05 ^ pll/CLK (avsdpll)
   0.26   11.31 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21   11.52 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24   11.76 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19   11.94 ^ clkbuf_leaf_90_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00   11.94 ^ core.CPU_Xreg_value_a4[7][13]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
  -0.55   11.39   clock uncertainty
   0.00   11.39   clock reconvergence pessimism
  -0.05   11.34   library setup time
          11.34   data required time
---------------------------------------------------------
          11.34   data required time
          -5.79   data arrival time
---------------------------------------------------------
           5.55   slack (MET)



==========================================================================
cts final report_checks -path_delay min reg to reg
--------------------------------------------------------------------------
Startpoint: core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: core.CPU_src2_value_a3[15]$_DFF_P_
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: min

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_7_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24    0.71 ^ clkbuf_4_14__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19    0.90 ^ clkbuf_leaf_108_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.90 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/CLK (sky130_fd_sc_hd__dfxtp_1)
   0.32    1.22 ^ core.CPU_Xreg_value_a4[25][15]$_SDFFE_PP0P_/Q (sky130_fd_sc_hd__dfxtp_1)
   0.06    1.28 v _14708_/Y (sky130_fd_sc_hd__a21oi_1)
   0.12    1.40 ^ _14712_/Y (sky130_fd_sc_hd__nand4_1)
   0.18    1.58 v _14729_/Y (sky130_fd_sc_hd__o32ai_4)
   0.16    1.74 ^ _14731_/Y (sky130_fd_sc_hd__o21ai_0)
   0.00    1.74 ^ core.CPU_src2_value_a3[15]$_DFF_P_/D (sky130_fd_sc_hd__dfxtp_2)
           1.74   data arrival time

   0.00    0.00   clock clk (rise edge)
   0.00    0.00   clock source latency
   0.00    0.00 ^ pll/CLK (avsdpll)
   0.26    0.26 ^ clkbuf_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.21    0.47 ^ clkbuf_3_6_0_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.24    0.71 ^ clkbuf_4_13__f_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.19    0.89 ^ clkbuf_leaf_70_CLK/X (sky130_fd_sc_hd__clkbuf_16)
   0.00    0.89 ^ core.CPU_src2_value_a3[15]$_DFF_P_/CLK (sky130_fd_sc_hd__dfxtp_2)
   0.88    1.78   clock uncertainty
   0.00    1.78   clock reconvergence pessimism
  -0.03    1.74   library hold time
           1.74   data required time
---------------------------------------------------------
           1.74   data required time
          -1.74   data arrival time
---------------------------------------------------------
           0.00   slack (MET)



==========================================================================
cts final critical path target clock latency max path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path target clock latency min path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path source clock latency min path
--------------------------------------------------------------------------
0

==========================================================================
cts final critical path delay
--------------------------------------------------------------------------
5.7921

==========================================================================
cts final critical path slack
--------------------------------------------------------------------------
5.5454

==========================================================================
cts final slack div critical path delay
--------------------------------------------------------------------------
95.740750

==========================================================================
cts final report_power
--------------------------------------------------------------------------
Group                  Internal  Switching    Leakage      Total
                          Power      Power      Power      Power (Watts)
----------------------------------------------------------------
Sequential             6.95e-03   9.72e-04   1.45e-08   7.92e-03  37.7%
Combinational          2.12e-03   4.52e-03   3.05e-08   6.64e-03  31.6%
Clock                  3.66e-03   2.76e-03   2.96e-09   6.42e-03  30.6%
Macro                  0.00e+00   0.00e+00   0.00e+00   0.00e+00   0.0%
Pad                    0.00e+00   0.00e+00   0.00e+00   0.00e+00   0.0%
----------------------------------------------------------------
Total                  1.27e-02   8.25e-03   4.80e-08   2.10e-02 100.0%
                          60.7%      39.3%       0.0%
```

Route:

```
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk route
```

![image]()

![image]()


# Week8

# /mnt/data/silicon_repo/silicon-diary-main/Week8/Readme.md

# VSDBabySoC – Static Timing Analysis (Pre-Route & Post-Route)

## 📚 Contents
- Introduction
- Key Files
- Timing Flow
- Post-Route Results Summary
- Comparison Graphs
- Key Differences: Post-Synthesis vs Post-Route
- Summary

---

## Introduction

This document provides the complete Static Timing Analysis (STA) workflow for the VSDBabySoC design across multiple PVT corners.  
Both pre-route and post-route timing reports are generated to understand the effects of parasitics, routing delays, and clock tree insertion on overall timing performance.

---

## Key Files

### sta_across_pvt_route.tcl
A TCL script used to automate:
- Loading multiple liberty files across corners  
- Reading Verilog netlist  
- Reading post-CTS SDC  
- Loading SPEF parasitics  
- Generating WNS, TNS, setup, and hold slack reports for every PVT corner  

### 6_final.sdc
Defines:
- 11 ns clock period  
- Clock propagation  
- Post-CTS timing constraints  

### 6_final.spef
Provides:
- Post-route extracted parasitics (resistance & capacitance)  
- Accurate interconnect delay modeling  

---

## Timing Flow

1. Load liberty files for all PVT corners  
2. Load synthesized/routed netlist  
3. Apply timing constraints  
4. Load parasitics (post-route only)  
5. Generate complete STA reports:  
   - min/max timing paths  
   - setup & hold analysis  
   - WNS, TNS  
   - Worst slack (min & max)  
6. Collect results inside `STA_OUTPUT/pre/` and `STA_OUTPUT/route/`  


---
### TCL File used

```
# ==============================
# VSDBabySoC PVT STA Script
# ==============================

# List of PVT corner libraries
set list_of_lib_files(1) "sky130_fd_sc_hd__tt_025C_1v80.lib"
set list_of_lib_files(2) "sky130_fd_sc_hd__ff_100C_1v65.lib"
set list_of_lib_files(3) "sky130_fd_sc_hd__ff_100C_1v95.lib"
set list_of_lib_files(4) "sky130_fd_sc_hd__ff_n40C_1v56.lib"
set list_of_lib_files(5) "sky130_fd_sc_hd__ff_n40C_1v65.lib"
set list_of_lib_files(6) "sky130_fd_sc_hd__ff_n40C_1v76.lib"
set list_of_lib_files(7) "sky130_fd_sc_hd__ss_100C_1v40.lib"
set list_of_lib_files(8) "sky130_fd_sc_hd__ss_100C_1v60.lib"
set list_of_lib_files(9) "sky130_fd_sc_hd__ss_n40C_1v28.lib"
set list_of_lib_files(10) "sky130_fd_sc_hd__ss_n40C_1v35.lib"
set list_of_lib_files(11) "sky130_fd_sc_hd__ss_n40C_1v40.lib"
set list_of_lib_files(12) "sky130_fd_sc_hd__ss_n40C_1v44.lib"
set list_of_lib_files(13) "sky130_fd_sc_hd__ss_n40C_1v76.lib"

# -----------------------------
# Your PATHS (updated)
# -----------------------------
set lib_dir "/home/jaynadan/sky130pdk/open_pdks/sky130/sky130A/libs.ref/sky130_fd_sc_hd/lib"

set analog_lib_dir "/home/jaynadan/vsd/VLSI/VSDBabySoC/src/lib"

set netlist_file "/home/jaynadan/vsd/VLSI/OpenROAD-flow-scripts/flow/results/sky130hd/vsdbabysoc/base/6_final.v"

set sdc_file "/home/jaynadanvsd/VLSI/OpenROAD-flow-scripts/flow/results/sky130hd/vsdbabysoc/base/6_final.sdc"

set spef_file "/home/jaynadan/vsd/VLSI/OpenROAD-flow-scripts/flow/results/sky130hd/vsdbabysoc/base/6_final.spef"

set output_dir "/home/jaynadan/vsd/VLSI/VSDBabySoC/STA_OUTPUT/route"

file mkdir $output_dir

# -----------------------------
# Read analog libs (PLL/DAC)
# -----------------------------
read_liberty $analog_lib_dir/avsdpll.lib
read_liberty $analog_lib_dir/avsddac.lib

# -----------------------------
# LOOP Through all PVT corners
# -----------------------------
for {set i 1} {$i <= [array size list_of_lib_files]} {incr i} {

    puts "============================================="
    puts " Running STA for $list_of_lib_files($i)"
    puts "============================================="

    # Load PVT corner liberty
    read_liberty $lib_dir/$list_of_lib_files($i)

    # Load design
    read_verilog $netlist_file
    link_design vsdbabysoc
    current_design

    # Constraints
    read_sdc $sdc_file

    # SPEF (post-route parasitics)
    read_spef $spef_file

    # Run setup check
    check_setup -verbose

    # Reports
    report_checks -path_delay min_max \
        -fields {nets cap slew input_pins fanout} \
        -digits {4} \
        > $output_dir/min_max_$list_of_lib_files($i).txt

    # Worst setup slack
    exec echo "$list_of_lib_files($i)" >> $output_dir/sta_worst_max_slack.txt
    report_worst_slack -max -digits {4} \
        >> $output_dir/sta_worst_max_slack.txt

    # Worst hold slack
    exec echo "$list_of_lib_files($i)" >> $output_dir/sta_worst_min_slack.txt
    report_worst_slack -min -digits {4} \
        >> $output_dir/sta_worst_min_slack.txt

    # TNS
    exec echo "$list_of_lib_files($i)" >> $output_dir/sta_tns.txt
    report_tns -digits {4} \
        >> $output_dir/sta_tns.txt

    # WNS
    exec echo "$list_of_lib_files($i)" >> $output_dir/sta_wns.txt
    report_wns -digits {4} \
        >> $output_dir/sta_wns.txt
}
```
### Terminal picture running above tcl

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%20from%202025-11-24%2018-03-42.png)

### tABLE pICTURE

![IMAGE](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-24%20225759.png)


## Comparison Graphs

### Worst Hold Slack (WHS)
An image showing the change in worst hold slack between pre-route and post-route.
![images](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-25%20172620.png)

### Worst Setup Slack (WSS)
Graph comparing post-synthesis vs post-route setup slacks.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-25%20172637.png)

### Worst Negative Slack (WNS)
Graph showing WNS variation across corners before and after routing.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-25%20172653.png)

### Total Negative Slack (TNS)

Graph showing TNS differences across all corners.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-25%20172706.png)

---

## Key Differences: Post-Synthesis vs Post-Route Timing Analysis

| Aspect             | Post-Synthesis Analysis                            | Post-Route Analysis                                           |
| ------------------ | -------------------------------------------------- | ------------------------------------------------------------- |
| Timing Model       | Wire-load estimated delays                         | RC parasitics from SPEF                                      |
| Clock Network      | Ideal, zero skew                                   | Real CTS clock tree delays                                   |
| Interconnect       | Estimated from fanout tables                       | Actual post-route RC delays                                  |
| Accuracy           | Medium (70–80%)                                     | High (95–98%)                                                 |
| Critical Paths     | Logic-dominant                                     | Physically accurate with routing effects                     |

---

## Summary

- Pre-route STA provides early timing insights.  
- Post-route STA represents physical, real-world behavior after routing and parasitic extraction.  
- Post-route timing results reveal realistic setup/hold violations caused by routing delays, coupling, and skew.  
- Multi-corner STA ensures robustness across process, voltage, and temperature variations.

Due to exam pepration i created file late i completd all labs on time i am just creating github juat one day late i am sorry for creating late github repo



---

# /mnt/data/silicon_repo/silicon-diary-main/Week8/Images/Readme.md




