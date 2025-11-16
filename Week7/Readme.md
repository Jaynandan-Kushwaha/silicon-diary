
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

![image](https://github.com/Jaynandan-Kushwaha/silicon-diary/blob/main/Week7/Images/Screenshot%20from%202025-11-15%2023-29-30.png)

