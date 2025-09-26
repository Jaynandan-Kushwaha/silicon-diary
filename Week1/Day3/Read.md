
# Day 3 – Combinational and Sequential Optimizations
**Author:** Jaynandan Kushwaha

📌 **Introduction**  
Day 3 focuses on **optimizing digital designs** at both the combinational and sequential levels. Efficient optimization techniques not only improve timing and performance but also reduce area and power consumption.  

We start with an introduction to basic optimization principles, understanding how synthesis tools identify opportunities for improvement. Then, we explore **combinational logic optimizations**, learning strategies to simplify and speed up logic paths. After that, we dive into **sequential logic optimizations**, including efficient flip-flop usage and techniques for handling unused outputs.  

By the end of this day, you will gain practical knowledge of optimization methods that make RTL designs **faster, smaller, and more reliable**, and learn how to apply these techniques during synthesis and simulation.

📚 **Contents**  
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
  <img src="Images/lecture3.png" alt="lecture3.png" width="70%">
</div>
