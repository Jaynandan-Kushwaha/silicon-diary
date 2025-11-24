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
## Comparison Graphs

### Worst Hold Slack (WHS)
An image showing the change in worst hold slack between pre-route and post-route.
![images](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-24%20231116.png)

### Worst Setup Slack (WSS)
Graph comparing post-synthesis vs post-route setup slacks.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-24%20231206.png)

### Worst Negative Slack (WNS)
Graph showing WNS variation across corners before and after routing.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-24%20231249.png)

### Total Negative Slack (TNS)

Graph showing TNS differences across all corners.
![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week8/Images/Screenshot%202025-11-24%20231329.png)

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

This README documents the complete STA workflow and post-route analysis for the VSDBabySoC design.

