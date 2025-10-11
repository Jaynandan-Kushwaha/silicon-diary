
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
