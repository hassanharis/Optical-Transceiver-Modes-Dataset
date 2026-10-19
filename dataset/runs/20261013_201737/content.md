## **AFBR-79Q4xZ** 10G QSFP Short Wavelength Transceiver Pluggable, Parallel-Fiber-Optics Modules 

## **Data Sheet** 

## **Description** 

The AFBR-79Q4Z Four-Channel, Pluggable, Parallel-FiberOptics Transceiver is a high performance fiber optics module for short-range parallel multi-lane data communication and interconnect applications. This 4-channel device is capable of 10 Gbps per channel, 40 Gbps aggregate operation. The module is designed to operate over multimode fiber systems using a nominal wavelength of 850 nm.  The electrical interface uses a 38 contact edge type connector.  The optical interface uses a MTP[] (MPO) 1x12 ribbon cable connector.   The module incorporates high performance, highly reliable, short wavelength optical devices coupled with proven circuit technology to provide long life and consistent service. 

## **Part Number Ordering Options** 

QDR 10G Infiniband AFBR-79Q4Z DDR 5G Infiniband AFBR-79Q5Z Evaluation test board - AFBR-79QEKZ 

## **Features** 

- High Channel Capacity: 40 Gbps per module 

- High port density:  21mm horizontal port pitch 

- Proven High Reliability 850nm VCSEL technology 

- Hot pluggable transceiver for servicing and ease of installation 

- Low power consumption:  1.5 watts typical per module 

- Compliant to industry-standard, pluggable, QSFP Multi-Source Agreement 

- Up to 100m links at 10G/channel using OM3 multimode fiber 

- Four independent transmitter channels and 4 independent receiver channels per module 

- Operates up to 10 Gbps with 8b/10b compatible coded data 

- Backwards compatible to 5Gbps DDR IB and 2.5 Gbps SDR IB 

- Two Wire Serial (TWS) interface with maskable interrupt for expanded functionality including: 

   - Individual channel functions: disable, squelch disable 

   - A/D readback: module temperature and supply voltages, per channel laser current and laser power, or received power 

   - Status: per channel Tx fault, electrical (transmitter) or optical (receiver) LOS, and alarm flags 

- 0 to 70°C case temperature operating range 

## **Applications** 

- High Performance and High Productivity computer interconnects 

- InfiniBand QDR (4x10G), DDR (4x 5G), and SDR (4x 2.5G) interconnects 

- High bandwidth backplane extension 

- PCI-Express 

- Datacom switch and router backplane connections 

- Telecom switch and router backplane connections 

- Reach extensions for various protocols including PCI Express, HyperTransport and Serial RapidIO 

Patent - www.avagotech.com/patents 


**----- Start of picture text -----**<br>
TX Input Buffer Laser Driver<br>Din[3:0][p/n] (8)<br>4 Channels 4 Channels<br>SCL<br>SDA<br>Mod Sel<br>LPMode Control Diagnostic<br>Monitors<br>ModPresL<br>ResetL<br>IntL<br>RX Output Buffer TIA<br>Dout[3:0][p/n] (8) 4 Channels 4 Channels<br>1x4 VCSEL Array<br>Electrical Interface Optical Interface<br>1x4 PIN Array<br>**----- End of picture text -----**<br>


**Figure 1. Transceiver Block Diagram** 

## **Transmitter** 

The optical transmitter portion of the transceiver (see Figure 1) incorporates a 4-channel VCSEL (Vertical Cavity Surface Emitting Laser) array, a 4-channel input buffer and laser driver, diagnostic monitors, control and bias blocks. The transmitter is designed for IEC-60825 and CDRH eye safety compliance; Class 1M out of the module.  The Tx Input Buffer provides CML compatible differential inputs presenting a nominal differential input impedance of 100 Ohms.  AC coupling capacitors are located inside the QSFP module and are not required on the host board.  For module control and interrogation, the control interface (LVTTL compatible) incorporates a Two Wire Serial (TWS) interface of clock and data signals.  Diagnostic monitors for VCSEL bias, light output (LOP), temperature, and power supply voltage are implemented and results are available through the TWS interface. 

Alarm thresholds are established for the monitored attributes.  Flags are set and interrupts generated when the attributes are outside the thresholds.  Flags are also set and interrupts generated for loss of input signal (LOS) and transmitter fault conditions.  All flags are latched and will remain set even if the condition initiating the latch clears and operation resumes.  All interrupts can be masked and flags are reset by reading the appropriate flag register. The optical output will squelch for loss of input signal unless squelch is disabled.  Fault detection or channel deactivation through the TWS interface will disable the channel.  Status, alarm and fault information are available via the TWS interface.  To reduce the need for polling, the hardware interrupt signal is provided to inform hosts of an assertion of an alarm, LOS and/or Tx fault. 

## **Receiver** 

The optical receiver portion of the transceiver (see Figure 1) incorporates a 4-channel PIN photodiode array, a 4-channel TIA array, a 4 channel output buffer, diagnostic monitors, control and bias blocks.  The Rx Output Buffer provides CML compatible differential outputs for the high speed electrical interface presenting nominal single-ended output impedances of 50 Ohms to AC ground and 100 Ohms differentially that should be differentially terminated with 100 Ohms.  AC coupling capacitors are located inside the QSFP module and are not required on the host board.  Diagnostic monitors for optical input power, are implemented and results are available through the TWS interface. 

Alarm thresholds are established for the monitored attributes. Flags are set and interrupts generated when the attributes are outside the thresholds. Flags are also set and interrupts generated for loss of optical input signal (LOS). All flags are latched and will remain set even if the condition initiating the latch clears and operation resumes. All interrupts can be masked and flags are reset upon reading the appropriate flag register. The electrical output will squelch for loss of input signal (unless squelch is disabled) and channel de-activation through TWS interface. Status and alarm information are available via the TWS interface. To reduce the need for polling, the hardware interrupt signal is provided to inform hosts of an assertion of an alarm and/or LOS. 

## **High Speed Signal Interface** 

Figure 2 shows the interface between an ASIC/SerDes and the QSFP module. For simplicity, only one channel is shown.  As shown in the Figure 2, the compliance points are on the host board side of the electrical connectors. Unused inputs and outputs should be terminated with 100 Ω differential loads. 

2 


**----- Start of picture text -----**<br>
Host Board<br>(Only one channel shown for simplicity)<br>C<br>Rx 1<br>Rx 2<br>D C' Rx Out p Rx 3<br>Rx Out n Rx Rx 4<br>ASIC (SerDes) QSFP Module<br>Tx In p<br>Tx In n Tx Tx 4<br>Tx 3<br>A B' Tx 2<br>Tx 1<br>B<br>Module Card Edge (Host Interface) (Optical Interface)<br>Optical Connector/Port<br>Host Edge Card Connector<br>**----- End of picture text -----**<br>


**Figure 2. Application Reference Diagram** 

QSFP compliance and reference points are as follows: 

A: Host ASIC transmitter output at ASIC package contact on a DUT board – Reference point 

B: Host ASIC transmitter output across the Host Board and Host Edge Card connector at the Module 

Card Edge interface – Reference point 

B’: Host ASIC transmitter output across the Host Board at Host Edge Card Connector – Compliance point 

- C: QSFP receiver output at the Module Card Edge Interface – Reference point 

C’: QSFP receiver output at Host Edge Card Connector – Compliance point 

D: QSFP receiver output at Host ASIC package receiver input contact on a DUT board – Reference point 

## **Control Signal Interface** 

The module has the following low speed signals for control and status: ModSelL, LP Mode, ResetL, ModPrsL, IntL  In addition, there is an industry standard two wire serial interface scaled for 3.3 volt LVTTL. It is implemented as a slave device. Signal and timing characteristics are further defined in the Control Characteristics and Control Interface & Memory Map sections. The registers of the serial interface memory are defined in the Control Interface & Memory Map section. 

## **Package Outline** 

The module is designed to meet the package outline defined in the QSFP MSA. See the package outline and host board footprint figures (Figures 11 -13) for details. 

## **Handling and Cleaning** 

The transceiver module can be damaged by exposure to current surges and over voltage events. Care should be taken to restrict exposure to the conditions defined in the Absolute Maximum Ratings. Wave soldering, reflow soldering and/or aqueous wash process with the modules on board are not recommended. Normal handling precautions for electrostatic discharge sensitive devices should be observed. 

Each module is supplied with an inserted port plug for protection of the optical ports. This plug should always be in place whenever a fiber cable is not inserted. 

The optical connector includes recessed elements that are exposed whenever a cable or port plug is not inserted. Prior to insertion of a fiber optic cable, it is recommended that the cable end be cleaned to avoid contamination from the cable plug. The port plug ensures the optics remain clean and no addition cleaning should be needed. In the event of contamination, dry nitrogen or clean dry air at less than 20 psi can be used to dislodge the contamination.  The optical port features (e.g. guide pins) preclude use of a solid instrument.  Liquids are also not advised. 

## **Link Model and Reference Channel** 

## **Regulatory & Compliance Issues** 

Various standard and regulations apply to the modules. These include eye-safety, EMC, ESD and RoHS.  See the Regulatory Section for details regarding these and component recognition. Please note the transmitter module is a Class 1M laser product – DO NOT VIEW RADIATION DIRECTLY WITH OPTICAL INSTRUMENTS. See Regulatory Compliance Table for details. When released, the AFBR-79Q4Z and AFBR-79Q5Z will support this table. 

Performance specifications for the AFBR-79Q4Z Transceiver are based on a reference channel model. A reference channel model provides the basis for inter-operability between independently produced transceiver modules. The reference model used for the AFBR-79Q4Z Transceiver is based on the industry standard 10GbE link model (10GEPBud3_1_16a.xls available at the IEEE P802.3ae 10Gb/s Ethernet Task Force Serial PMD Documents website: www.ieee802.org/3/ae/public/adhoc/serial_ pmd/documents/) 

3 

## **Absolute Maximum Ratings** 

Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operation Conditions.  It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently.  Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Reference**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40|100|°C||
|Case Temperature – Operating|TC AMR|0|70|°C|1|
|3.3 V Power Supply Voltage|VCC|-0.5|3.6|V||
|Data Input Voltage – Single Ended||-0.5|VCC+0.5|V||
|Data Input Voltage – Diferential||VDIP- VDIN|||1.0|V|2|
|Control Input Voltage|Vi|-0.5|VCC+0.5, 3.6|V||
|Control Output Current|Io|-20|20|mA||
|Relative Humidity|RH|5|95|%||



1.  The position for case temperature measurement is shown in Figure 5. 

2.  This is the maximum voltage that can be applied across the differential inputs without damaging the input circuitry. The equivalent input differential peak-to-peak voltage is twice this number. 

## **Recommended Operating Conditions** 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted.  Optical and electrical characteristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied and damage to the module may occur for such operation over an extended period of time. 

|extended period of time.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|Case Temperature|Tc|0|40|70|°C|1|
|3.3 V Power Supply Voltage|Vcc|3.135|3.3|3.465|V||
|Signal Rate per Channel||2.5||10.0|GBd|2|
|Control* Input Voltage High|Vih|2||Vcc+.3|V||
|Control* Input Voltage Low|Vil|-0.3||0.8|V||
|Two Wire Serial (TWS) Interface Clock Rate||||400|kHz||
|TWS Write Cycle Time||||40|ms||
|Power Supply Noise||||50|mVpp|3|
|Receiver Diferential Data Output Load|||100||Ohms||
|Fiber Length:  500 MHz∙km 50µm MMF (OM2)||0.5||35|m|4|
|Fiber Length:  2000 MHz∙km 50µm MMF (OM3)||0.5||100|m||



- Control signals, LVTTL (3.3 V) compatible 

1. The position of case temperature measurement is shown in Figure 5. 

2. 8b10b coding is assumed 

3. Power Supply Noise is defined as the peak-to-peak noise amplitude over the frequency range at the host supply side of the recommended power supply filter with the module and recommended filter in place. Voltage levels including peak-to-peak noise are limited to the recommended operating range of the associated power supply. See Figure 6 for recommended power supply filter. 

4. Channel insertion loss includes 3.5 dB/km attenuation, 1.5 dB connector loss and 0.3 dB modal noise penalty allocations. 

4 

## **Transceiver Electrical Characteristics*** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40˚C, Vcc = 3.3 V 

|<br>values are for Tc = 40˚C, Vcc = 3.3 V|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbols**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|10G Transceiver Power Consumption|||1.5|TBD|W||
|5G Transceiver Power Consumption|||1.3|TBD|W||
|10G Transceiver Power Supply Current|||454|TBD|mA||
|5G Transceiver Power Supply Current|||394|TBD|mA||
|Transceiver Power On Initialization Time|tPWR INIT|||2000|ms|1|



1. Power On Initialization Time is the time from when the supply voltages reach and remain above the minimum Recommended Operating Conditions to the time when the module enables TWS access. The module at that point is fully functional. 

## **Transmitter Section Electrical Characteristics*** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40˚C, Vcc = 3.3 V 

|<br>values are for Tc = 40˚C, Vcc = 3.3 V|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbols**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|LOS Assert Threshold:|ΔVdi pp los|||50|mVpp||
|Tx Data Input Diferential|||||||
|Peak-to-Peak Voltage Swing|||||||
|LOS Hysteresis: Tx Data Input||0.5||4|dB|1|
||||||||
|**Test conditions for Optical Tx Characteristics:**|||||||
|Data Input Diferential|ΔVDI pp|175||1600|mVpp|2|
|Peak-to-Peak Voltage Swing|||||||
|Data Input Rise & Fall Times (20% – 80%)||30||48|ps||
|Data Input Deterministic Jitter||||15|ps|3|
|Data Input Total Jitter||||30|ps|4|



- For control signal timing including MODSelL, LPMode, ResetL, ModPrsL, IntL, SCL and SDA see Control Interface and Memory Map. 

1. LOS Hysteresis is defined as 20 Log(LOS De-assert Level / LOS Assert Level). 

2. This is a test condition and is not a required characteristic of the transceiver. It is a Tx Recommended Operating condition. Data inputs are CML compatible. Data Input Differential Peak to Peak Voltage Swing is defined as follows: Δ VDI pp = Δ VDIH – Δ VDIL where Δ VDIH = High State Differential Data Input Voltage and Δ VDIL = Low State Differential Data Input Voltage. 

3. This is a test condition and is not a required characteristic of the transceiver. It is a Tx Recommended Operating condition. Deterministic Jitter, DJ, conforms to the dual-Dirac model where TJ(BER) = DJ + 2Q(BER)RJrms and RJrms is the width of the Gaussian component. Here BER = 10[-12] . DJ is measured with the same conditions as TJ. Effects of impairments in the test signal due to the test system are removed from the measurement. All channels not under test are operating with similar test patterns. 

4. This is a test condition and is not a required characteristic of the transceiver. It is a Tx Recommended Operating condition. Total Jitter, TJ, defined for a BER of 10[-12] , is measured at the 50% signal level using using a 10.0 GBd Pseudo Random Bit Sequence of length 2[7] -1 (PRBS7), or equivalent, test pattern .Effects of impairments in the test signals due to the test system are removed from the measurement. All channels not under test are operating with similar test patterns. 

5 

## **Receiver Section Electrical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40˚C, Vcc = 3.3 V 

|<br>values are for Tc = 40˚C, Vcc = 3.3 V|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|Data Output Diferential Peak-to-Peak Voltage|ΔVDO PP|375||875|mVpp|1|
|Swing (Zero De-emphasis)|||||||
|Output Rise/Fall time (20–80%)||||55|ps|2|
|Reference Link Output Deterministic Jitter||||36|ps|3|
|Reference Link Output Total Jitter||||70|ps|4|
|Reference Link Output Eye Width|tEYE LINK|30|||ps|5|



1. Data outputs are CML compatible. Data Output Differential Peak to Peak Voltage Swing is defined as follows: Δ VDO pp = Δ VDOH - Δ VDOL where Δ VDOH = High State Differential Data Output Voltage and Δ VDOL = Low State Differential Data Output Voltage. Impairments in measurements due to the test system are removed. 

2. These are unfiltered rise and fall times measured between the 20% and 80% levels using a 500 MHz square wave test pattern. Impairments in measurements due to the test system are removed. 

3. Deterministic Jitter, DJ, conforms to the dual-Dirac model where TJ(BER) = DJ + 2Q(BER)RJrms and RJrms is the width of the Gaussian component. Here BER = 10[-12] . DJ is measured with the same conditions as TJ. Effects of impairments in the test signals due to the test system are removed from the measurement. All channels not under test are operating with similar test patterns at an input signal 6 dB above maximum Receiver Sensitivity. 

4. Total Jitter, TJ, defined for a BER of 10[-12] , is measured at the 50% signal level using a 10.0 GBd Pseudo Random Bit Sequence of length 2[7] -1 (PRBS7), or equivalent, test pattern .Effects of impairments in the test signals due to the test system are removed from the measurement. All channels not under test are operating with similar test patterns. 

5. Eye Opening is defined as the unit interval less TJ for the same test pattern and conditions as TJ. 

## **Transmitter Optical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40˚C, Vcc = 3.3 V 

|<br>values are for Tc = 40˚C, Vcc = 3.3 V|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|Output Optical Power: Average|Po ave|||1.0|dBm||
|Output Optical Power: Disabled|Po of|||-30|dBm||
|Extinction Ratio|ER|3|||dB||
|Output OMA: Squelched||||-27|dBm||
|Output OMA||-3|||dBm|Informative|
|Center Wavelength||840||860|nm|1|
|Spectral Width - rms||||0.65|nm||
|Transmitter Eye Mask||||||2|



1. The transmitter launch condition meets the requirements of 10 Gigabit Ethernet multimode fiber as detailed in TIA 492AAC. 

2. The transmitter eye mask test is absolute in terms of eye height (OMA) and relative in terms of time. It represents the minimum 1e-12 TX eye opening required to produce a 0.3 UI eye opening at TP4 of a compliant RX. 

6 



**----- Start of picture text -----**<br>
Mask Coordinates<br>X1=0.223 UI<br>X2=0.360 UI<br>Y1=0.170 mW<br>Y2=1.4<br>**----- End of picture text -----**<br>


**Figure 3. Transmitter Eye Mask – This eye mask is based up on a 5 e-5 hits per sample.** 

## **Receiver Optical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40˚C, Vcc = 3.3 V. 

|<br>values are for Tc = 40˚C, Vcc = 3.3 V.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|Input Optical Power Sensitivity (OMA)||||-9.8|dBm|Informative|
|Input Optical Power Saturation|PSAT AVE|1.0|||dBm||
|Operating Center Wavelength||840||860|nm||
|Return Loss||12|||dB||
|LOS Asserted Threshold – OMA|PLOS OMA|-26|TBD||dBm||
|LOS De-asserted – OMA|||TBD|-10|dBm||
|LOS Hysteresis||0.5|TBD||dB||



7 

Regulatory Compliance Table (When released, the AFBR-79Q4xZ and AFBR-795xZ will support this table.) 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge|JEDEC Human Body Model (HBM)|Transceiver module withstands 2000V|
|(ESD) to the Electrical Contacts|(JESD22-A114-B)||
|||Transceiver module withstands 100V|
||JEDEC Machine Model (MM)||
||(JESD22-A115-A)||
|Electrostatic Discharge (ESD) to|Variation of IEC 61000-4-2|Typically withstands at least 6 kV|
|Optical Connector Receptacle||air discharge with module biased|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022|Typically passes with 10 dB margin.|
||(CISPR 22A) VCCI Class 1|Actual performance dependent on|
|||enclosure design|
|Immunity|Variation of IEC 61000-4-3|Typically minimum efect from a 10V/m<br>feld swept from 80 MHz to 1 GHz applied|
|||to the module without a chassis enclosure|
|Laser Eye Safety and Equipment|IEC 60825-1 Amendment 2|Pout: IEC AEL & US FDA CDRH Class 1M|
|Type Testing|CFR 21 Section 1040||
|Component Recognition|Underwriters Laboratories and|UL File Number: E173874|
||Canadian Standards Association||
||Joint Component Recognition for||
||Information Technology Equipment||
||including Electrical Business Equipment||
|RoHS Compliance||Less than 100 ppm of cadmium, lead,|
|||mercury, hexavalent chromium,|
|||polybrominated biphenyls, and|
|||polybrominated biphenyl esters.|



8 

## **QSFP Transceiver Pad Layout** 


**----- Start of picture text -----**<br>
38 GND<br>GND<br>37 TX1n<br>TX2n<br>36 TX1p<br>35 GND TX2p<br>GND<br>34 TX3n<br>TX4n 5 [4321]<br>3332 TX3pGND TX4p 6<br>GND<br>31 LPMode<br>ModSelL<br>30 Vcc1<br>ResetL<br>29 VccTx<br>VccRx 78910<br>28 IntL<br>SCL 11<br>27 ModPrsL<br>SDA 12<br>26 GND<br>GND 13<br>2524 RX4pRX4n RX3p 14<br>RX3n 15<br>23 GND<br>GND 16<br>2221 RX2pRX2n RX1p 17<br>RX1n 18<br>20 GND<br>GND 19<br>Card Edge<br>**----- End of picture text -----**<br>


## **TOP SIDE** 

## **BOTTOM SIDE** 

|**TOP SIDE**<br>**BOTTOM SIDE**|**TOP SIDE**<br>**BOTTOM SIDE**|**TOP SIDE**<br>**BOTTOM SIDE**|**TOP SIDE**<br>**BOTTOM SIDE**|**TOP SIDE**<br>**BOTTOM SIDE**|**TOP SIDE**<br>**BOTTOM SIDE**|
|---|---|---|---|---|---|
|**VIEWED FROM TOP**<br>**VIEWED FROM BOTTOM**||||||
|**Pin**|**Logic**|**Symbol**|**Description**|**Plug**<br>**Sequence**|**Notes**|
|1||GND|Ground|1|1|
|2|CML-I|Tx2n|Transmitter Inverted Data Input|3||
|3|CML-I|Tx2p|Transmitter Non-Inverted Data Input|3||
|4||GND|Ground|1|1|
|5|CML-I|Tx4n|Transmitter Inverted Data Input|3||
|6|CML-I|Tx4p|Transmitter Non-Inverted Data Input|3||
|7||GND|Ground|1|1|
|8|LVTTL-I|ModSelL|Module Select|3||
|9|LVTTL-I|ResetL|Module Reset|3||
|10||Vcc Rx|+3.3 V Power supplyreceiver|2|2|
|11|LVCMOS-I/O|SCL|2-wire serial interface clock|3||
|12|LVCMOS-I/O|SDA|2-wire serial interface data|3||
|13||GND|Ground|1|1|
|14|CML-O|Rx3p|Receiver Non-Inverted Data Output|3||
|15|CML-O|Rx3n|Receiver Inverted Data Output|3||
|16||GND|Ground|1|1|
|17|CML-O|Rx1p|Receiver Non-Inverted Data Output|3||
|18|CML-O|Rx1n|Receiver Inverted Data Output|3||
|19||GND|Ground|1|1|
|20||GND|Ground|1|1|
|21|CML-O|Rx2n|Receiver Inverted Data Output|3||
|22|CML-O|Rx2p|Receiver Non-Inverted Data Output|3||
|23||GND|Ground|1|1|
|24|CML-O|Rx4n|Receiver Inverted Data Output|3||
|25|CML-O|Rx4p|Receiver Non-Inverted Data Output|3||
|26||GND|Ground|1|1|
|27|LVTTL-O|ModPrsL|Module Present|3||
|28|LVTTL-O|IntL|Interrupt|3||
|29||Vcc Tx|+3.3 V Power supplytransmitter|2|2|
|30||Vcc1|+3.3 V Power Supply|2|2|
|31|LVTTL-I|LPMode|Low Power Mode|3||
|32||GND|Ground|1|1|
|33|CML-I|Tx3p|Transmitter Non-Inverted Data Input|3||
|34|CML-I|Tx3n|Transmitter Inverted Data Input|3||
|35||GND|Ground|1|1|
|36|CML-I|Tx1p|Transmitter Non-Inverted Data Input|3||
|37|CML-I|Tx1n|Transmitter Inverted Data Input|3||
|38||GND|Ground|1|1|
|Note 1: GND is the symbol for signal and supply (power) common for the QSFP module. All are common within the QSFP<br>module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host<br>board signal-commongroundplane.||||||
|Note 2: Vcc Rx, Vcc1 and Vcc Tx are the receiver and transmitter power supplies and shall be applied concurrently.<br>Requirements, defned for the host side of the Host Edge Card Connector, are listed in Table 6. Recommended host board<br>power supply fltering is shown in Figure 4. Vcc Rx,Vcc1and Vcc Tx may be internally connected within the QSFP transceiver<br>module in anycombination. The connectorpins are each rated for a maximum current of 500 mA.||||||



**Figure 4. Host Board Pattern for QSFP Transceiver – Top View** 

9 


**Figure 5. Case Temperature Measurement Point** 


**----- Start of picture text -----**<br>
1uH<br>Vcc Tx<br>0.1 uF 22  uF<br>Vcc_host =<br>GND<br>3.3 Volt<br>1uH<br>Vcc Rx<br>0.1 uF 22  uF 0.1 uF 22 uF<br>GND<br>1uH<br>Vcc1<br>0.1 uF 22  uF<br>GND<br>QSFP Module<br>**----- End of picture text -----**<br>


**Figure 6. Recommended Tx Power Supply Filter** 


**----- Start of picture text -----**<br>
VCC25<br>VCC33<br>50<br>DPx Signal Path (Pos)<br>VCC25<br>VCC33<br>50<br>DNx Signal Path (Neg)<br>**----- End of picture text -----**<br>


**Figure 7. Transmitter Data Input Equivalent Circuit** 

10 


**----- Start of picture text -----**<br>
VCC25 VCC25<br>VCC33<br>50 50<br>Doutp<br>Doutn<br>Signal Path (Neg) Signal Path (Pos)<br>**----- End of picture text -----**<br>


**Figure 8. Receiver Data Output Equivalent Circuit** 


**----- Start of picture text -----**<br>
START ReSTART STOP<br>tLOW tHIGH tF tR<br>SCL<br>tHD,SDA tHD,DAT tSU,DAT tBUF tSU,STO tBUF<br>tSU,SDA tR tF<br>SDA In<br>tAA tDH<br>SDA Out<br>**----- End of picture text -----**<br>


**Figure 9. TWS Interface Bus Timing** 

11 

## **Pack** 

## **Package Outline, Host PCB Footprint and Bezel Design** 


**Figure 10. Mechanical Package Outline** 

12 


**Figure 11. QSFP Host Board Mechanical Footprint** 

13 


**Figure 12. QSFP Host Board Mechanical Footprint Detail** 


**Figure 13. Host Board Bezel Design** 

14 

## **Control Interface & Memory Map** 

The control interface combines dedicated signal lines for ModSelL, LP Mode, ResetL, ModPrsL, IntL with two-wire serial, TWS, interface clock, SCL, and data, SDA, signals to provide users rich functionality over an efficient and easily used interface. The TWS interface is implemented as a slave device and compatible with industry standard two-wire serial protocol. It is scaled for 3.3 volt LVTTL. Outputs are high-z in the high state to support busing of these signals. Signal and timing characteristics are further defined in the Control I/O Characteristics section. In general, TWS bus timing and protocols follow the implementation popularized in Atmel Two-wire Serial EEPROMs. For additional details see, e.g., Atmel AT24C01A. 

## **ModSelL** 

The ModSelL is an inputsignal. When held low by the host, the module responds to 2-wire serial communication commands. The ModSelL allows the use of multiple QSFP modules on a single 2-wire interface bus. When the ModSelL is “High”, the module will not respond to or acknowledge any 2-wire interface communication from the host. ModSelL signal input node is biased to the “High” state in the module. In order to avoid conflicts, the host system shall not attempt 2-wire interface communications within the ModSelL de-assert time after any QSFP modules are deselected. Similarly, the host must wait at least for the period of the ModSelL assert time before communicating with the newly selected module. The assertion and de-asserting periods of different modules may overlap as long as the above timing requirements are met. 

## **ResetL** 

The ResetL signal is pulled to Vcc in the QSFP module. A low level on the ResetL signal for longer than the minimum pulse length (t_Reset_init) initiates a complete module reset, returning all user module settings to their default state. Module Reset Assert Time (t_init) starts on the rising edge after the low level on the ResetL pin is released. During the execution of a reset (t_init) the host shall disregard all status bits until the module inidicates a completion of the reset interrupt. The module indicates this by posting an IntL signal with the Data_Not_Ready bit negated. Note that on power up (including hot insertion) the module will post this completion of reset interrupt without requiring a reset. 

## **LPMode** 

## **ModPrsL** 

ModPrsL is pulled up to Vcc_Host on the host board and grounded in the module. The ModPrsL is asserted “Low” when inserted and deasserted “High” when the module is physically absent from the host connector. 

## **IntL** 

IntL is an output signal. When “Low”, it indicates a possible module operational fault or a status critical to the host system. The host identifies the source of the interrupt using the 2-wire serial interface.The IntL signal is an open collector output and must be pulled to host supply voltage on the host board. 

The user can read the present value of the various diagnostic monitors. For transmitters and receivers, internal module temperature and supply voltages are reported. For transmitters, monitors provide for each channel laser bias current and laser light output power (LOP) information. For receivers, input power (Pave) is monitored for each channel. In addition, elapsed operating time is reported. All monitor items are two-byte fields and to maintain coherency, the host must access these with single two-byte read sequences. For each monitored item, alarm thresholds are established. If an item moves past a threshold, a flag is set, and, provided the item is not masked, IntL is asserted. 

A mask bit that can be set to prevent assertion of IntL for the individual item exists for every LOS, Tx fault and monitor flag. Entries in the mask fields are volatile. 

## **Memory Map Overview** 

The memory is structured as a single address, multiple page approach after that in the XFP MSA. The address is given as A0xh. The structure of the memory is shown in Figure 14. The memory space is arranged into a lower, single page, address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, e.g. Interrupt Flags and Monitors. Less time critical entries, e.g. serial ID information and threshold settings, are available with the Page Select function. For a more detailed description of the QSFP memory map see the QSFP MSA specification revision 1.0. 

15 


**----- Start of picture text -----**<br>
2-wire serial address, 1010000x (A0h)"<br>0 ID and status  3(Bytes)<br>2<br>3 (19 Bytes)<br>Interrupt Flags<br>21<br>22 Module Monitors (12 Bytes)<br>33<br>34 Channel Monitors (48 Bytes)<br>81<br>82 Reserved (4 Bytes)<br>85<br>86 Control (12 Bytes)<br>97<br>98 Reserved (2 Bytes)<br>99<br>100 Module  and Channel Mask (7 Bytes)<br>106<br>107 Reserved (12 Bytes)<br>118<br>119 Password Change Entry  (4 Bytes)<br>122 Area (Optional)<br>123 Password Entry Area  (4 Bytes)<br>126 (Optional)<br>127 (1 Bytes)<br>Page Select Byte<br>127<br>Pag0 e0 Pag0 eO( 1 oitpn)la Page 02 (Optional) Pag0 e3<br>119218 BsasdleiF DI e 6(B 4)sety 112288 C C _APPS B 1()sety 215258 UsE re E PRO D Mata (128 Bytes) 117258 ModT eluserhhdlo 4( 8 Bytes)<br>192 E etxndeDI d (32 Bytes) 129 AS T TaL elbenT( htg)L (1 Bytes) 176 Channel Threshold (48 Bytes)<br>223 129 223<br>224 VendS ro pDI cifice (32 Bytes) 130 ApcilpoitaC n odE e 0 yrtn (2 Bytes) 224 Reserved (2 Bytes)<br>255 131 225<br>133132 Application Code Entry 1 (2 Bytes) 241226 Vendor Specific Channel Controls (16 Bytes)<br>other entries 242 Channel Monitor Masks (12 Bytes)<br>253<br>254 Application Code Entry TL (2 Bytes) 254 Reserved (2 Bytes)<br>255 255<br>**----- End of picture text -----**<br>


**Figure 14. Two-Wire Serial Address A0xh Page Structure** 

16 

## **I/O Timing for Control and Status Functions** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted.  Typical values are for Tc = 40°C, Vcc = 3.3 V 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Reference**|
|---|---|---|---|---|---|---|
|Initialization Time|t_init|||2000||Time from power on, hot plug or rising edge of|
|||||||Reset until the module is fully functional.  This time|
|||||||does not apply to non Power level 0 modules in the|
|||||||Low Power state|
|LPMode Assert Time|ton_LPMode|||100|ms|Time from assertion of LPMode until the module|
|||||||power consumption enterspower level 1|
|Interrupt Assert Time|ton_IntL|||200|ms|Time from occurrence of condition triggering IntL|
|||||||until Vout:IntL=Vol|
|Interrupt De-assert Time|Tof_IntL|||500|µs|Time from clear on read operation of associated fag|
|||||||until Vout:IntL=Voh.  This includes deassert times for|
|||||||RX LOS, TX Fault and other fagbits|
|Reset Init Assert Time|t_reset_init|||2|µs|A Reset is generated by a low level longer than the|
|||||||minimm resetpulse timepresent on the ResetLpin|
|Reset Assert Time|t_reset|||2000|ms|Time from rising edge on the ResetL pin until the|
|||||||module is fullyfunctional|
|Serial Bus Hardware|t_serial|||2000|ms|Time from power on until module responds to data|
|ReadyTime||||||transmission over the 2-wire serial bus|
|Monitor Data Ready Time|t_data|||2000|ms|Time from power on to data not ready, bit 0 of Byte 2,|
|||||||deasserted and IntL asserted|
|RX LOS Assert Time|ton_los|||100|ms|Time from RX LOS state to RX LOS bit set and IntL|
|||||||asserted|
|TX Fault Assert Time|ton_Txfault|||200|ms|Time from TX Fault state to TX fault bit set and IntL|
|||||||asserted|
|Flag Assert Time|ton_Flag|||200|ms|Time from occurrence of condition trigerring fag to<br>associated fagbit set and IntL asserted.|
|Mask Assert Time|ton_Mask|||100|ms|Time from mask bit set until associated IntL assertion|
|||||||is inhibited|
|Mask Deassert TIme|tof_Mask|||100|ms|Time from mask bit cleared until associated IntL|
|||||||operation resumes|
|Rate Select Change Time|t_ratesel|||100|ms|Time from change of state of Rate Select bit until|
|||||||transmitter or receiver bandwidth is in conformance|
|||||||with appropriate specifcation|
|Power Set Assert Time|ton_Pdown|||100|ms|Time from P_Down but set until module power|
|||||||consumption enterspower level 1|
|Power Set Deassert Time|tof_Pdown|||300|ms|Time from P_Down bit cleared until the module is|
|||||||fullyfunctional|
|RX Squelch Assert Time|ton_Rxsq|||80|µs|Time from loss of RX input signal until the squelched|
|||||||output condition is reached|
|RX Squelch Deassert Time|tof_Rxsq|||80|µs|Time from resumption of RX input signals until|
|||||||nornmal RX output condition is reached|
|TX Squelch Assert Time|ton_Txsq|||400|ms|Time from loss of TX input signal until the squelched|
|||||||output condition is reached|
|TX Squelch Deassert Time|tof_Txsq|||400|ms|Time from resumption of TX input signals until|
|||||||nominal TX output condition is reached|
|TX Disable Assert Time|ton_txdis|||100|ms|Time from TX Disable bit set until optical output falls|
|||||||below 10% of nominal|
|TX Disable Deassert Time|tof_txdis|||400|ms|Time from TX Disable bit cleared until optical output|
|||||||rises above 90% of nominal|
|RX Output Disable Assert|ton_rxdis|||100|ms|Time from RX Output Disable bit set until RX output|
|Time||||||falls below 10% of nominal|
|RX Output Disable|tof_rxdis|||100|ms|Time from RX Output Disable bit cleared until RX|
|Deassert Time||||||output rises above 90% of nominal|
|Squelch Disable Assert Time|ton_sqdis|||100|ms|This applies to RX and TX Squelch and is the time from|
|||||||bit set until squelch functionalityis disabled|
|Squelch Disable Deassert|tof_sqdis|||100|ms|This applies to RX and TX Squelch and is the time from|
|Time||||||bit cleared until squelch functionalityis enabled|



17 

## **Memory Map** 

For additional detail see QSFP Transceiver MSA Rev 1.0 

For product information and a complete list of distributors, please go to our web site: **www.avagotech.com** 

Avago, Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change.  Copyright © 2005-2013 Avago Technologies. All rights reserved. AV02-1794EN  -  January 28, 2013 

