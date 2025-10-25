
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
