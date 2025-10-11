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

