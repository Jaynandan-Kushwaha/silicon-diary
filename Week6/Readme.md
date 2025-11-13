
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

### Theory

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
10. Make timing ECO fixes to remove all violations.
11. Replace the old netlist with the new netlist generated after timing ECO fix and implement the floorplan, placement and cts.
12. Post-CTS OpenROAD timing analysis.
13. Explore post-CTS OpenROAD timing analysis by removing 'sky130_fd_sc_hd__clkbuf_1' cell from clock buffer list variable 'CTS_CLK_BUFFER_LIST'.

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

#### 9. Do Post-Synthesis timing analysis with OpenSTA tool.

Since we are having 0 wns after improved timing run we are going to do timing analysis on initial run of synthesis which has lots of violations and no parameters were added to improve timing

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

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Commands run final screenshot

![Screenshot from 2024-03-26 05-52-18](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/790d4852-7f1d-47b5-a64f-5735f6064b61)

Newly created `pre_sta.conf` for STA analysis in `openlane` directory

![Screenshot from 2024-03-26 05-53-06](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/0a02d055-f012-44bd-a750-4508bbfc771e)

Newly created `my_base.sdc` for STA analysis in `openlane/designs/picorv32a/src` directory based on the file `openlane/scripts/base.sdc`

![Screenshot from 2024-03-26 05-55-17](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/8c917d87-5507-4079-ba6b-facbf18c238f)
![Screenshot from 2024-03-26 05-55-38](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/e07d05db-2f06-47ab-bff7-2af88c39d001)

Commands to run STA in another terminal

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Command to invoke OpenSTA tool with script
sta pre_sta.conf
```

Screenshots of commands run

![Screenshot from 2024-03-26 06-04-28](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/32def177-5173-4dd7-ba3b-44e37846644c)
![Screenshot from 2024-03-26 06-05-07](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/d8b8c46a-3a8b-458c-8c75-03f6577f5d17)
![Screenshot from 2024-03-26 06-05-53](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/ab396c91-430f-41ca-b9a4-dda72a91c4d5)
![Screenshot from 2024-03-26 06-08-51](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/aa1d50b0-9cb1-45bf-a641-b64842166b48)

Since more fanout is causing more delay we can add parameter to reduce fanout and do synthesis again

Commands to include new lef and perform synthesis 

```tcl
# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a -tag 25-03_18-52 -overwrite

# Adiitional commands to include newly added lef to openlane flow
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Command to set new value for SYNTH_MAX_FANOUT
set ::env(SYNTH_MAX_FANOUT) 4

# Command to display current value of variable SYNTH_DRIVING_CELL to check whether it's the proper cell or not
echo $::env(SYNTH_DRIVING_CELL)

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Commands run final screenshot

![Screenshot from 2024-03-26 06-20-29](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/c5869cf5-ab95-46f9-9fd1-dc91e92455d8)

Commands to run STA in another terminal

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Command to invoke OpenSTA tool with script
sta pre_sta.conf
```

Screenshots of commands run

![Screenshot from 2024-03-26 06-22-31](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/0f3247fc-aaad-4e98-b23e-bdc9a361d08c)
![Screenshot from 2024-03-26 06-22-41](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/9fcc3975-0e03-4515-aee5-04b7c1c6a315)
![Screenshot from 2024-03-26 06-22-50](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/e19db773-3995-4af4-b0a3-188b02fdf454)
![Screenshot from 2024-03-26 06-23-01](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/c22c85fb-1a94-4639-a731-da4c364d1a78)

#### 10. Make timing ECO fixes to remove all violations.

OR gate of drive strength 2 is driving 4 fanouts

![Screenshot from 2024-03-26 06-55-46](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/73c58332-a212-4a24-b853-e8cae3b385a6)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11672_

# Checking command syntax
help replace_cell

# Replacing cell
replace_cell _14510_ sky130_fd_sc_hd__or3_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced

![Screenshot from 2024-03-26 07-02-44](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/c50c6023-1836-468d-a8c3-955b02e4224c)
![Screenshot from 2024-03-26 07-04-08](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/6059a511-9977-4d9e-8dde-8939f0e1b8f7)
![Screenshot from 2024-03-26 09-42-15](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/df3dba3c-9445-4d51-9842-bf4410f05cf5)
![Screenshot from 2024-03-26 07-07-50](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/f141d1ff-4e21-4f9a-ab47-19579a686ac4)

OR gate of drive strength 2 is driving 4 fanouts

![Screenshot from 2024-03-26 09-46-23](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/3f66eed9-c43d-483e-ab85-21d70452b81f)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11675_

# Replacing cell
replace_cell _14514_ sky130_fd_sc_hd__or3_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced

![Screenshot from 2024-03-26 09-49-29](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/d896c1fa-078e-4fe1-8e4d-60fae870d672)
![Screenshot from 2024-03-26 09-50-13](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/a21abd89-b92a-4d28-b065-6b8b523026de)
![Screenshot from 2024-03-26 09-50-33](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/9b961126-3de7-450e-9789-5009ca7f6a16)

OR gate of drive strength 2 driving OA gate has more delay

![Screenshot from 2024-03-26 10-22-10](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/7669eeef-7b93-4cfd-a152-17eec772496a)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11643_

# Replacing cell
replace_cell _14481_ sky130_fd_sc_hd__or4_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced

![Screenshot from 2024-03-26 10-29-31](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/c63cf6a1-582d-43e5-907f-e292b94cc086)
![Screenshot from 2024-03-26 10-29-55](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/6495c2e8-78c8-41d2-b783-628f36b982c5)

OR gate of drive strength 2 driving OA gate has more delay

![Screenshot from 2024-03-26 10-32-27](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/4185dc98-a065-49d3-a92f-fb4b02f23ee5)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11668_

# Replacing cell
replace_cell _14506_ sky130_fd_sc_hd__or4_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced

![Screenshot from 2024-03-26 10-36-59](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/be71b3a4-efe1-4239-be5a-28ccebd2b7f4)
![Screenshot from 2024-03-26 10-37-14](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/2ae759b3-f9a7-478f-a34a-3f8706347eca)

Commands to verify instance `_14506_`  is replaced with `sky130_fd_sc_hd__or4_4`

```tcl
# Generating custom timing report
report_checks -from _29043_ -to _30440_ -through _14506_
```

Screenshot of replaced instance

![Screenshot from 2024-03-26 10-43-04](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/970b3cb7-fe10-4b5e-99c9-85059714f8f2)

*We started ECO fixes at wns -23.9000 and now we stand at wns -22.6173 we reduced around 1.2827 ns of violation*

#### 11. Replace the old netlist with the new netlist generated after timing ECO fix and implement the floorplan, placement and cts.

Now to insert this updated netlist to PnR flow and we can use `write_verilog` and overwrite the synthesis netlist but before that we are going to make a copy of the old old netlist

Commands to make copy of netlist

```bash
# Change from home directory to synthesis results directory
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/25-03_18-52/results/synthesis/

# List contents of the directory
ls

# Copy and rename the netlist
cp picorv32a.synthesis.v picorv32a.synthesis_old.v

# List contents of the directory
ls
```

Screenshot of commands run

![Screenshot from 2024-03-26 10-54-15](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/90c90853-0664-44d7-8ff2-573621935870)

Commands to write verilog

```tcl
# Check syntax
help write_verilog

# Overwriting current synthesis netlist
write_verilog /home/vsduser/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/25-03_18-52/results/synthesis/picorv32a.synthesis.v

# Exit from OpenSTA since timing analysis is done
exit
```

Screenshot of commands run

![Screenshot from 2024-03-26 11-02-19](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/c6c8ce7f-5219-41bc-a5a8-47b0e1c62c7c)

Verified that the netlist is overwritten by checking that instance `_14506_`  is replaced with `sky130_fd_sc_hd__or4_4`

![Screenshot from 2024-03-26 11-01-25](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/1ddb66da-64cb-426d-8d78-30370c63dacb)

Since we confirmed that netlist is replaced and will be loaded in PnR but since we want to follow up on the earlier 0 violation design we are continuing with the clean design to further stages

Commands load the design and run necessary stages

```tcl
# Now once again we have to prep design so as to update variables
prep -design picorv32a -tag 24-03_10-03 -overwrite

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Follwing commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or

# Now we are ready to run placement
run_placement

# Incase getting error
unset ::env(LIB_CTS)

# With placement done we are now ready to run CTS
run_cts
```

Screenshots of commands run

![Screenshot from 2024-03-26 11-33-14](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/a0f223bc-3cbb-4bb1-8c7e-d800f1a4efd7)
![Screenshot from 2024-03-26 11-33-22](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/9bd610a8-fd5e-452b-94b2-5a5fc76db5e9)
![Screenshot from 2024-03-26 11-35-40](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/283d9b5e-fc48-45a3-8548-c68fc8966f46)
![Screenshot from 2024-03-26 11-36-16](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/af866818-af6f-4bc4-96c0-cf3c99839003)
![Screenshot from 2024-03-26 11-37-36](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/55aa5130-8a9f-48d6-abc8-7aace68b58c8)
![Screenshot from 2024-03-26 11-38-26](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/755fc79a-2a77-402b-aa11-33799e31ee09)
![Screenshot from 2024-03-26 11-39-53](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/45fdc85e-cc32-4b08-954e-bd78dcec0891)
![Screenshot from 2024-03-26 12-00-48](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/5deb6b89-c81e-4b4d-a225-badc1f7c7299)

#### 12. Post-CTS OpenROAD timing analysis.

Commands to be run in OpenLANE flow to do OpenROAD timing analysis with integrated OpenSTA in OpenROAD

```tcl
# Command to run OpenROAD tool
openroad

# Reading lef file
read_lef /openLANE_flow/designs/picorv32a/runs/24-03_10-03/tmp/merged.lef

# Reading def file
read_def /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/cts/picorv32a.cts.def

# Creating an OpenROAD database to work with
write_db pico_cts.db

# Loading the created database in OpenROAD
read_db pico_cts.db

# Read netlist post CTS
read_verilog /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/synthesis/picorv32a.synthesis_cts.v

# Read library for design
read_liberty $::env(LIB_SYNTH_COMPLETE)

# Link design and library
link_design picorv32a

# Read in the custom sdc we created
read_sdc /openLANE_flow/designs/picorv32a/src/my_base.sdc

# Setting all cloks as propagated clocks
set_propagated_clock [all_clocks]

# Check syntax of 'report_checks' command
help report_checks

# Generating custom timing report
report_checks -path_delay min_max -fields {slew trans net cap input_pins} -format full_clock_expanded -digits 4

# Exit to OpenLANE flow
exit
```

Screenshots of commands run and timing report generated

![Screenshot from 2024-03-26 12-55-00](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/ee26dfa7-715a-4df7-97e7-4c6e54d16522)
![Screenshot from 2024-03-26 12-57-40](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/e04a4dfd-000c-406b-bdaa-f5314c4eedef)
![Screenshot from 2024-03-26 12-58-12](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/ac27d567-1b72-444d-a638-9be2db677ae2)
![Screenshot from 2024-03-26 13-09-57](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/e63cac70-072d-4453-992e-076b94f8f1a2)

#### 13. Explore post-CTS OpenROAD timing analysis by removing 'sky130_fd_sc_hd__clkbuf_1' cell from clock buffer list variable 'CTS_CLK_BUFFER_LIST'.

Commands to be run in OpenLANE flow to do OpenROAD timing analysis after changing `CTS_CLK_BUFFER_LIST`

```tcl
# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Removing 'sky130_fd_sc_hd__clkbuf_1' from the list
set ::env(CTS_CLK_BUFFER_LIST) [lreplace $::env(CTS_CLK_BUFFER_LIST) 0 0]

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Checking current value of 'CURRENT_DEF'
echo $::env(CURRENT_DEF)

# Setting def as placement def
set ::env(CURRENT_DEF) /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/placement/picorv32a.placement.def

# Run CTS again
run_cts

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Command to run OpenROAD tool
openroad

# Reading lef file
read_lef /openLANE_flow/designs/picorv32a/runs/24-03_10-03/tmp/merged.lef

# Reading def file
read_def /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/cts/picorv32a.cts.def

# Creating an OpenROAD database to work with
write_db pico_cts1.db

# Loading the created database in OpenROAD
read_db pico_cts.db

# Read netlist post CTS
read_verilog /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/synthesis/picorv32a.synthesis_cts.v

# Read library for design
read_liberty $::env(LIB_SYNTH_COMPLETE)

# Link design and library
link_design picorv32a

# Read in the custom sdc we created
read_sdc /openLANE_flow/designs/picorv32a/src/my_base.sdc

# Setting all cloks as propagated clocks
set_propagated_clock [all_clocks]

# Generating custom timing report
report_checks -path_delay min_max -fields {slew trans net cap input_pins} -format full_clock_expanded -digits 4

# Report hold skew
report_clock_skew -hold

# Report setup skew
report_clock_skew -setup

# Exit to OpenLANE flow
exit

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Inserting 'sky130_fd_sc_hd__clkbuf_1' to first index of list
set ::env(CTS_CLK_BUFFER_LIST) [linsert $::env(CTS_CLK_BUFFER_LIST) 0 sky130_fd_sc_hd__clkbuf_1]

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)
```

Screenshots of commands run and timing report generated

![Screenshot from 2024-03-26 13-42-03](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/2191f13b-ff76-4281-9d3c-52cbf12f9142)
![Screenshot from 2024-03-26 13-45-28](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/3dcd6efe-d31a-4f72-aede-be1cdd7b078f)
![Screenshot from 2024-03-26 13-48-01](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/2cb2c6fd-1e8c-4921-8553-7dcfb51258e5)
![Screenshot from 2024-03-26 13-48-13](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/70353613-86f2-432c-a1d8-821083e8c209)
![Screenshot from 2024-03-26 13-50-12](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/bf6c116b-e31c-4dce-b04f-a75430b1d03b)
![Screenshot from 2024-03-26 13-53-30](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/assets/63997454/a26e9d23-d448-4512-8676-8a2b3fb22572)

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
