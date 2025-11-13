
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
