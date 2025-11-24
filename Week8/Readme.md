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

### vsdbabysoc_post_cts.sdc
Defines:
- 11 ns clock period  
- Clock propagation  
- Post-CTS timing constraints  

### vsdbabysoc.spef
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

## Post-Route Results Summary

The following table represents the worst slack and total negative slack across corners after routing.

*(Insert your extracted table here)*

---

## Comparison Graphs

### Worst Hold Slack (WHS)
An image showing the change in worst hold slack between pre-route and post-route.

### Worst Setup Slack (WSS)
Graph comparing post-synthesis vs post-route setup slacks.

### Worst Negative Slack (WNS)
Graph showing WNS variation across corners before and after routing.

### Total Negative Slack (TNS)
Graph showing TNS differences across all corners.

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

