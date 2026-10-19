**Data Sheet** 

## **AFBR-57H5MZ** 

**64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G** 


## **Description** 

The Broadcom[®] AFBR-57H5MZ optical transceiver supports high-speed serial links over multi-mode optical fiber at signaling rates up to 57.8 Gb/s PAM4 (the serial line rate of 64GFC). The product is compliant with Small Form Pluggable SFP+ industry agreements for mechanical and low speed electrical specifications. High-speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-7. 

The AFBR-57H5MZ is a multi-rate 850-nm transceiver that ensures compliance with FC-PI-7 64GFC, 32GFC, and 16GFC specifications. Per the requirements of 64GFC, internal clock and data recovery circuits (CDRs) are present on both electrical input and electrical output of this transceiver. These CDRs lock at 57.8-Gb/s PAM4, 28.05-Gb/s NRZ and 14.025-Gb/s NRZ (64GFC, 32GFC, and 16GFC) accomplished by using two Rate Select inputs and I[2] C to configure transmit and receive sides. 

Digital diagnostic monitoring information (DMI) is present in the AFBR-57H5MZ per the requirements of SFF-8472, providing real time monitoring information of transceiver laser, receiver and environment conditions over an SFF-8431 I[2] C interface. 

## **Features** 

- Compliant to RoHS directives with 7c-I exemption 

- Broadcom high-performance 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) and PiN diode 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 75°C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10A) 

- Diagnostic features per SFF-8472, “Diagnostic Monitoring Interface for Optical Transceivers” 

- Enhanced operational features including EWRAP, OWRAP, and adaptive electrical EQ/emphasis settings 

- Integrated PRBS generator and bit error rate checker 

- Real time monitoring of the following: – Transmitter average optical power 

   - Received average optical power 

   - Laser bias current 

   - Temperature 

   - Supply voltage 

   - Power-on hours 

- SFP+ mechanical specifications per SFF-8432 

- SFP+ compliant low-speed interface per SFF-8419 

- Fibre Channel FC-PI-7 compliant high-speed optical and electrical interface 

## **Applications** 

- Fibre Channel switches 

- Fibre Channel host bus adapters 

- Fibre Channel RAID controllers 

- Port-side connections 

- Inter-switch or inter-chassis aggregated links 

AFBR-57H5MZ-DS102 January 31, 2023 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Transceiver Block Diagram** 

## **Figure 1:  Block Diagram** 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER RX LOSS OF SIGNAL<br>PHOTO- TRANS -IMPEDANCE RD+ (RECEIVE DATA)<br>LIGHT FROM FIBER DETECTOR AMPLIFIER RD-  (RECEIVE DATA)<br>DSP<br>TD+ (TRANSMIT DATA)<br>TD-  (TRANSMIT DATA)<br>MOD -DEF2(SDA)<br>MOD -DEF1(SCL)<br>TRANSMITTER MOD -DEF0<br>MCU<br>BIAS & SAFETY<br>LIGHT TO FIBER VCSEL<br>CIRCUITRY TX_FAULT<br>TX RATE SELECT RS(1)<br>RX RATE SELECT RS(0)<br>TX_DISABLE<br>**----- End of picture text -----**<br>


## **Transmitter Section** 

The transmitter section includes a transmitter optical sub-assembly (TOSA), a laser driver circuit, and a digital signal processor (DSP) with input variable equalization. The TOSA contains a Broadcom 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) light source with an integral light monitoring function and imaging optics to ensure efficient optical coupling to the LC connector interface. The TOSA is driven by a laser driver circuit, which uses the differential output from the DSP to modulate and regulate VCSEL optical power. As mandated by FC-PI-7, the integral Tx DSP cleans up any incoming jitter accumulated from the host ASIC, PCB traces, and SFP electrical connector. Between the SFP electrical connector and Tx DSP is an adaptive equalization circuit to optimize SFP performance with nonideal incoming electrical waveforms at all rates. 

## **Receiver Section** 

The receiver section includes a receiver optical sub-assembly (ROSA), a pre-amplification and post-amplification circuit, a DSP circuit with variable emphasis controls, and an integral PRBS generator. The ROSA, containing a high-speed PIN detector, pre-amplifier, and imaging optics efficiently couple light from the LC connector interface and perform an optical-to-electrical conversion. The resulting differential electrical signal passes through a post-amplification circuit and into the DSP for cleaning up accumulated jitter. The resulting signal is passed to a high-speed output line driver stage with variable, I[2] C controlled, emphasis settings that allow the host to optimize signal characteristics between the SFP and the host ASIC. 

## **Digital Diagnostics** 

The AFBR-57H5MZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in document SFF-8472. These features allow the host to access, using I[2] C, real-time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage, and laser operating current. 

AFBR-57H5MZ-DS102 2 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Low-Speed Interfaces** 

Conventional low-speed interface I/Os are available as defined in SFF-8431 to manage coarse and fine functions of the optical transceiver. On the transmit side, a Tx_DISABLE input is provided for the host to turn on and off the outgoing optical signal. A transmitter rate select control input pin, Tx_RATE, and I[2] C controls are provided to configure the transmitter stages for 64GFC, 32GFC, or 16GFC operation (logic HIGH reserved for 64GFC and 32GFC, logic LOW reserved for 16GFC). A transmitter fault indicator output, Tx_FAULT, is available for the SFP to signal the host of a transmitter operational problem. A receiver rate select control input, Rx_RATE, configures receiver stages for 64GFC, 32GFC, or 16GFC operation (logic HIGH reserved for 64GFC and 32GFC, logic LOW reserved for 16GFC). In 64G mode, the Rate_Sel pins are ignored. A received optical power loss of signal indicator, RX_LOS, is available to advise the host of a receiver operational problem. 

## **Special Operation Functions** 

See Table 29 for the I[2] C control registers. 

**Figure 2:  OWRAP Functionality (I[2] C Controlled)** 

**Figure 3:  EWRAP Functionality (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT & PRE POST Rx VOUT &<br>AMP AMP Emphasis AMP AMP Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>LaserDriver EQ LaserDriver EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


Electrical and optical high-speed data “wrap” functions are enabled to assist with local host or remote diagnostic and optimization sequences. Optical data wrap (OWRAP) takes a received optical signal through a CDR and retransmits it optically out. Electrical data wrap (EWRAP) takes an incoming electrical signal through a CDR and retransmits it electrically out. In OWRAP/EWRAP mode the traffic pass-through can be turned on or off, controlled through I[2] C commands. 

**Figure 4:  SFP Tx Input Electrical EQ Is Always Adaptive (No I[2] C Control Needed)** 

**Figure 5:  SFP Rx Variable Output Electrical Emphasis (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT &<br>AMP AMP<br>Emphasis<br>ROSA<br>DSP uController<br>TOSA<br>LaserDriver EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
PRE POST Rx VOUT &<br>AMP AMP<br>Emphasis<br>ROSA<br>DSP uController<br>TOSA<br>LaserDriver EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


AFBR-57H5MZ-DS102 

Broadcom 

3 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

The electrical SFP input stage (TD +/–) has been enhanced with adaptive EQ, which optimizes the transceiver’s input equalization settings without host control. The SFP electrical output stage (RD+/–) has been enhanced with variable output emphasis features to allow host control and optimization of the receiver’s output settings. The host can then select, in situ, the most appropriate SFP setting for a given interconnect scenario. 

**Figure 6:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, Line Side (I[2] C Controlled)** 

**Figure 7:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, System Side (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST PRBS Rx VOUT & PRE POST PRBS Rx VOUT &<br>AMP AMP BER Emphasis AMP AMP Gen Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA<br>TOSA<br>LaserDriver PRBSGen EQ LaserDriver PRBSBER EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


The SFP is equipped with an integrated PRBS generator that self-generates programmable PRBS patterns to either system side (TP4) or line side (TP1) at the speed (16G, 32G, or 64G) and operating mode (NRZ or PAM4) to which the SFP is set. The integrated bit error rate checker can also be enabled to measure bit error ratio for every 5 seconds (fixed). It enables users to know the optical link BER performance between TP2 and TP3 of the two separate SFPs or between the host ASIC transmitter (TP0) and the SFP Tx input (TP1). 

AFBR-57H5MZ-DS102 4 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 1:  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to<br>the Electrical Contacts|JEDEC Human Body Model (HBM)<br>(JESD22-A114-B)|High-speed contacts withstand 1000V. All other<br>contacts withstand 2000 V.|
|ESD to the Optical Connector<br>Receptacle|EN61000-4-2, Criterion B|When installed in a properly grounded housing and<br>chassis, the units are subjected to 15-kV air<br>discharges during operation and 8-kV direct<br>discharges to the case.|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022<br>(CISPR 22A) VCCI Class 1|System margins are dependent on customer board<br>and chassis design.|
|Immunity|EN 55024:2010|Typically shows no measurable effect from a 3 V/m<br>field step from 80 MHz to 1 GHz applied to the module<br>without a chassis enclosure|
|Laser Eye Safety and Equipment<br>Type Testing|CLASS 1 LASER PRODUCT<br>Complies with 21 CFR 1040.10 except for<br>conformance with IEC 60825-1 Ed.3., as<br>described in Laser Notice No. 56, dated<br>May 8, 2019<br><br>(IEC) EN62368-1: 2014<br><br>(IEC) EN60825-1: 2014<br><br>(IEC) EN60825-2: 2004+A1+A2|CDRH Certification 9720151-204|
|Component Recognition|Underwriters Laboratories (UL) and<br>Canadian Standards Association (CSA) Joint<br>Component Recognition for Information<br>Technology Equipment including Electrical<br>Business Equipment|UL File:   E484615|
|RoHS|—|RoHS compliant with 7c-I exemptions.|



AFBR-57H5MZ-DS102 5 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Figure 8:  Typical Application Configuration** 


**----- Start of picture text -----**<br>
Tx Rate Select VCC T<br>RS(1)<br>40k<br>4.7k<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1uF<br>TD +<br>100<br>TD -<br>0.1uF LASER DRIVER<br>4.7k to 10k<br>4.7uH VCCT<br>0.1uF 22 uF 0.1uF<br>3.3V<br>SERDES D S P<br>PROTOCOL IC 4.7uH VCCR<br>0.1uF 22 uF 0.1uF<br>0.1uF<br>RD +<br>100 100<br>RD -<br>LOSS OF  Rx LOS 0.1uF<br>SIGNAL<br>RS(0) POST AMP<br>Rx Rate Select<br>3.3V 40 k<br>GND<br>4.7k to 10k 4.7k to 10k<br>MODULE  4.7k to 10k MOD_ABS MOD_SCL MOD_SDA<br>DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 9:  Recommended Power Supply Filter** 


**NOTE:** Inductors must have less than 0.5Ω series resistance to limit the voltage drop to the SFP module. 

AFBR-57H5MZ-DS102 6 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Table 2:  Pin Description** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground|—|
|2|TX_FAULT|Transmitter Fault Indication - High indicates a fault condition|a|
|3|TX_DISABLE|Transmitter Disable  -  Module optical output disables on high or open|b|
|4|MOD_SDA|Module Definition 2 - Two wire serial ID interface data line (SDA)|c|
|5|MOD_SCL|Module Definition 1 - Two wire serial ID interface clock line (SCL)|c|
|6|MOD_ABS|Module Definition 0 - Grounded in module (module present indicator)|c|
|7|Rx Rate Select, RS(0)|Receiver Rate Select|d|
|8|RX_LOS|Loss of Signal - High indicates loss of received optical signal|e|
|9|Tx Rate Select, RS(1)|Transmitter Rate Select|d|
|10|VeeR|Receiver Ground|—|
|11|VeeR|Receiver Ground|—|
|12|RD-|Inverse Received Data Out|f|
|13|RD+|Received Data Out|f|
|14|VeeR|Receiver Ground|—|
|15|VccR|Receiver Power  + 3.3 V|g|
|16|VccT|Transmitter Power  +  3.3 V|g|
|17|VeeT|Transmitter Ground|—|
|18|TD+|Transmitter Data In|h|
|19|TD-|Inverse Transmitter Data In|h|
|20|VeeT|Transmitter Ground|—|
|a. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7 kΩ to 10 kΩ resistor on the host board. When high, this output<br>indicates a laser fault of some kind. Low indicates normal operation. In the low state, the outputis pulled to < 0.4V.<br>b. TX_DISABLE is an input that shuts down the transmitter optical output. It is internally pulled up (within the transceiver) with a 4.7-kΩ resistor.<br>Low (–0.3V to 0.8V):<br>Transmitter on<br>Between (0.8V and 2.0V):<br>Undefined<br>High (2.0V to Vcc + 0.3) or OPEN:<br>Transmitter Disabled||||



- c. The signals Mod_ABS, SCL, SDA designate the two-wire serial interface pins. They must be pulled up with a 4.7 kΩ to 10 kΩ resistor on the host board. Mod_ABS is grounded by the module to indicate the module is present. Mod_SCL is serial clock line (SCL) of two-wire seiral interface. Mod_SDA is serial data line (SDA) o two wire serial interface. 

- d. The rate select input pin selects the signal rates along with the software rate select bits as shown in Table 16 and Table 17. It is internally pulled down with a 40-kΩ resistor. 

- e. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7-kΩ to 10- kΩ resistor on the host board. When high, this output indicates the received optical power is below the worst case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to < 0.4V. 

- f. RD–/+ designate the differential receiver outputs. They are AC coupled 100 Ω differential lines that should be terminated with 100Ω differential at the host SerDes input. AC coupling is done inside the transceiver and is not required on the host board. 

- g. VccR and VccT are the receiver and transmitter power supplies. Refer to SFF-8419 for details. 

- h. TD–/+ designate the differential transmitter inputs. They are AC coupled differential lines with 100Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. 

Stress in excess of any of the individual absolute maximum ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently. Exposure to any of the absolute maximum ratings for extended periods can adversely affect reliability. 

AFBR-57H5MZ-DS102 7 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 3:  Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Reference**|
|---|---|---|---|---|---|
|Storage Temperature|Ts|–40|85|°C|a|
|Relative Humidity|RH|5|95|%|—|
|Supply Voltage|Vcc|–0.3|3.63|V|—|
|Low Speed Input Voltage|Vi|–0.3|Vcc + 0.5, 3.63|V|—|
|Low Speed Output Current|—|–20|20|mA|—|



- a. Absolute maximum ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. Refer to the reliability data sheet for specific reliability performance. Between the absolute maximum ratings and the Recommended Operating Conditions, functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted. Optical and electrical characteristics are not defined for operation outside the recommended operating conditions, reliability is not implied, and damage to the module may occur for such operation over an extended period of time. 

**Table 4:  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Reference**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tc|0|—|75|°C|a|
|Supply Voltage|Vcc|3.135|3.3|3.465|V|—|
|Data Rate|—|14.025<br>14.025|—<br>—|28.9<br>57.8|GBd<br>Gb/s|b|
|Two-Wire Serial (TWS) Interface<br>Clock Rate|—|—|—|400|kHz|c|



- a. The position of case temperature measurement is shown in Figure 13. Continuous operation at the maximum recommended operating case temperature should be avoided to not degrade reliability. 

- b. 64GFC PAM4 requires FEC RS(544,514) encoding per FC-PI-7. 32GFC NRZ requires FEC RS(528,514) per FC-PI-6 and 16GFC NRZ does not require FEC per FC-PI-5. 

- c. With 500-µs maximum clock stretch per SFF-8419. 

AFBR-57H5MZ-DS102 8 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

The following transceiver electrical characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 5:  Transceiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Reference**|
|---|---|---|---|---|---|---|
|Transceiver Power Consumption|—|—|1.4|1.65<br>2.0|W<br>W|At 3.3V max.<br>At 3.465V max.|
|Power Supply Noise Rejection (peak-peak)|PSNR|—|—|66|mV|a|
|Low Speed Outputs: TX_FAULT, RX_LOS, MOD_SDA|VOL|–0.3|—|0.4|V|b|
||IOH|–50|—|37.5|µA|—|
|Low Speed Inputs: TX_DIS, MOD_SCL, MOD_SDA, RS(0), RS(1)|VIL|–0.3|—|0.8|V|c|
||VIH|2.0|—|VccT +<br>0.3|V|c|



- a. Filter per the SFP specification is required on the host board to remove 10-Hz to 2-MHz content. 

- b. Pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

- c. Mod_SCL and Mod_SDA must be pulled up externally with a4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

The following high speed electrical module input characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 6:  High Speed Electrical Module Input Characteristics[a]** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|64GFC Signaling Rate, Per Lane|B’|—|28.9|—|GBd|± 100 ppm, PAM4 and<br>RS(544,514) FEC<br>encoded|
|32GFC Signaling Rate, Per Lane|B’|—|28.05|—|GBd|± 100 ppm, NRZ and<br>RS(528, 514) FEC<br>encoded|
|16GFC Signaling Rate, Per Lane|B’|—|14.025|—|GBd|± 100 ppm, NRZ|
|Differential pk-pk Input Voltage<br>Tolerance|B’|900|—|—|mV|—|
|Differential Termination Resistance<br>Mismatch|B’|—|—|10|%|—|
|Differential Return Loss, SDD11 min.|B’|—|Eq. 1, Fig. 9|—|dB|IEEE 802.3 Annex 83E|
|Differential Mode to Common Mode<br>Conversion, min.|B’|—|Eq. 2, Fig. 10|—|dB|IEEE 802.3 Annex 83E|
|Common-Mode Output Voltage|B’|—|—|—|V|b|



a. From FC-PI-7, Table 11. 

- b. DC common mode voltage is generated by the host. The specification includes the effects of ground offset voltage. 

**Table 7:  Stressed Input Test Conditions** 

|**Parameter**|**Value**|**Units**|**Notes/Conditions**|
|---|---|---|---|
|Module stressed input test|||a|
|Eye width at 10–5probability EW5|0.23|UI|—|
|Eye height at 10–5probability EH5|34|mV|—|



AFBR-57H5MZ-DS102 

Broadcom 

9 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Table 7:  Stressed Input Test Conditions (Continued)** 

|**Parameter**|**Value**|**Units**|**Notes/Conditions**|
|---|---|---|---|
|Vertical Eye Closure VEC (max.)|12|dB|—|



a. Module stressed input tolerance is measured using the procedure defined in 83E.3.4.1.1. 

## **Table 8:  Reference Points** 

|**Test Point**|**Description**|
|---|---|
|B’|Module electrical input at the input of the module compliance moard. Module return loss specifications are met at this<br>point.|
|C’|Module electrical output at the output of the module compliance board. Module output and module return loss<br>specifications are met at this point.|



**Figure 10:  FC-PI-7 Module Compliance Points** 


AFBR-57H5MZ-DS102 10 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 9:  High Speed Electrical Module Output Characteristics[a]** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|Differential Output Voltage (Enabled)|C’|—|—|900|mV|Measured with<br>PRBS13Q|
|Differential Output Voltage (Disabled)|C’|—|—|35|mV|Measured with<br>PRBS13Q|
|Common Mode Noise, RMS|C’|—|—|17.5|mV|—|
|Differential Termination Mismatch|C’|—|—|10|%|—|
|Differential Output Return Loss SDD22<br>(min.)|C’|—|Eq. 1, Fig. 9|—|dB|FC-PI-7|
|Common to Differential Mode Conversion<br>SDC22, min.|C’|—|Eq 2, Fig. 10|—|dB|FC-PI-7|
|Source Transition Time (20% to 80%)|C’|9.5|—|—|ps|—|
|Common Mode Voltage|C’|—|—|—|V|b|
|Eye width at 10–5Probability EW5|C’|0.265|—|—|UI|—|
|Eye height at 10–5Probability EH5|C’|70|—|—|mV|—|
|Vertical Eye Closure VEC|C’|—|—|12|dB|—|
|Near-End Eye Symmetry Mask Width<br>(ESMW)|C’|—|0.265|—|UI|—|
|Near-end Eye Height, Differential|C’|70|—|—|mV|—|
|Far-end ESMW|C’|—|0.2|—|UI|—|
|Far-end Eye Height, Differential|C’|30|—|—|mV|—|
|Far-end Pre-cursor ISI Ratio|C’|–4.5|—|2.5|%|—|



a. From FC-PI-7, Table 10. 

b. DC common mode voltage is generated by the host. The specification includes the effects of ground offset voltage. 

AFBR-57H5MZ-DS102 11 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 10:  64GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|64GFC Signaling Rate|gamma-T|—|28.9|—|GBd|± 100 ppm, PAM4 and<br>RS(544,514) FEC encoded|
|Center Wavelength Range|gamma-T|840|—|860|nm|—|
|RMS Spectral Width|gamma-T|—|—|0.60|nm|—|
|Transmitter and Dispersion Eye Closure for<br>PAM4 (TDECQ),|gamma-T|—|—|5.5|dB|—|
|TDECQ- 10log10(Ceq)|gamma-T|—|—|5.5|dB|—|
|Optical Modulation Amplitude (OMAouter)|gamma-T|–4.5a|—|+3.0|dBm|—|
|OMAouterExtinction Ratio|gamma-T|3|—|—|dB|—|
|Launch Power in OMAouter minus TDECQ|gamma-T|–5.9|—|—|dBm|—|
|Average Launch Power|gamma-T|–7.5|—|+4.0|dBm|—|
|RIN12OMA|gamma-T|—|—|–128|dB/Hz|—|
|Transmitter Transition Time, 20%-80%|gamma-T|—|—|34|ps|—|
|Average Launch Power of OFF transmitter,|gamma-T|—|—|–30|dBm|—|
|Encircled Flux|gamma-T|—|≥ 86% at 19 µm<br>≤ 30% at 4.5 µm|—|—|Type A1a.2 50-µm Fiber per<br>IEC 61280-1-4|



a. Even if the TDEC < 1.4 dB, the OMA (min.) must exceed this value. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 11:  64GFC Mode Optical Receiver Characteristics (per PC-PI-7)** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/**<br>**Conditions**|
|---|---|---|---|---|---|---|
|Center Wavelength Range|gamma-R|840|—|860|nm|—|
|Damage Threshold|gamma-R|+5.0|—|—|dBm|BER 1.09E–4|
|Average Receive Power|gamma-R|–9.4|—|+4.0|dBm|BER 1.09E–4|
|Receive Power (OMAouter)|gamma-R|—|—|+3.0|dBm|BER 1.09E–4|
|Receiver Return Loss|gamma-R|12|—|—|dB|—|
|Receiver Sensitivity (OMAouter)|gamma-R|—|—|–7.0|dBm|BER 1.09E–4|
|Stressed Receiver Sensitivity OMAouter|gamma-R|—|—|–2.4|dBm|BER 1.09E–4|
|Conditions of Stressed Receiver Sensitivity Test|gamma-R|—|—|—|—|—|
|Stressed Eye Closure for PAM4 (SECQ)|gamma-R|—|—|5.5|dB|BER 1.09E–4|
|SECQ-10log10(Ceq)|gamma-R|—|—|5.5|dB|BER 1.09E–4|
|LOS Assert|gamma-R|–30|—|—|dBm avg|—|
|LOS Deassert|gamma-R|—|—|–7|dBm avg|—|
|LOS Hysteresis|gamma-R|0.5|—|—|dB|—|



AFBR-57H5MZ-DS102 12 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 12:  32GFC Mode Optical Transmitter Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|32GFC Signaling Rate, Per Lane|—|—|28.05|—|GBd|± 100 ppm NRZ, RS(528,514)<br>FEC encoded|
|Modulated Optical Output Power (OMA)<br>(Peak-to-Peak) 28.05 Gb/s|Tx,OMA|479|—|—|µW|—|
|||–3.2|—|—|dBm|—|
|Average Optical Output Power 28.05 Gb/s|Pout|–6.2|—|2|dBm|b|
|Vertical Eye Closure Penalty, 28.05 Gb/s|VECP|—|—|3.13|dB|—|



a. Tc = 0°C to 75°C, VccT, VccR = 3.3V ± 5%. 

- b. Max. Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 13:  32GFC Mode Optical Receiver Characteristic** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power, 28.05 Gb/s|PIN|—|—|+2|dBm,avg|—|
|Input Optical Modulation Amplitude, 28.05 Gb/s<br>(Peak to Peak) (Unstressed Sensitivity)|OMA|—|—|95|µW|a, b|
|||—|—|–10.2|dBm||
|Stressed Receiver Sensitivity (OMA) 28.05 Gb/s|—|—|—|263|µW|b, c|
|||—|—|–5.7|dBm||



- a. Input Optical Modulation Amplitude (commonly known as sensitivity] requires a valid Fibre Channel encoded input. 

- b. 32GFC (28.05 Gb/s) assumes an FEC encoded RS(528, 514) signal and allows a BER of 1E–6 for receiver and transmitter measurements. c. 28.05 Gb/s stressed received vertical eye closure penalty (ISI) min. is 3.1 dB. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 14:  16GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|16GFC Signaling Rate, Per Lane|—|—|14.025|—|GBd|± 100 ppm NRZ,<br>No FEC|
|Modulated Optical Output Power (OMA) (Peak to Peak)<br>14.025 Gb/s|Tx,OMA|331|—|—|µW|—|
|||–4.8|—|—|dBm|—|
|Average Optical Output Power|Pout|–7.8|—|—|dBm|a|
|Vertical Eye Closure Penalty, 14.025 Gb/s|VECP|—|—|2.56|dB|—|
|Transmitter Uncorrelated Jitter, 14.025 Gb/s|UJ|—|—|0.03|UI|—|



a. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 15:  16GFC Mode Optical Receiver Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit.**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power|PIN|—|—|0|dBm,avg|per FC-PI-5|
|Input Optical Modulation Amplitude, 14.025 Gb/s<br>(Peak to Peak) (Unstressed Sensitivity)|OMA|—|—|89|µW|a|
|||—|—|–10.5|dBm||



AFBR-57H5MZ-DS102 

Broadcom 

13 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Table 15:  16GFC Mode Optical Receiver Characteristics (Continued)** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit.**|**Notes**|
|---|---|---|---|---|---|---|
|Stressed Receiver Sensitivity (OMA) 14.025 Gb/s|—|—|—|170|µW|b|
|||—|—|–7.7|dBm||



- a. Input Optical Modulation Amplitude (commonly known as sensitivity) requires a valid Fibre Channel encoded input and allows a BER of 1E–12. 

- b. 14.025-Gb/s stressed received vertical eye closure penalty (ISI) min is 2.5 dB for all fiber types. 

AFBR-57H5MZ-DS102 

Broadcom 

14 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Rate Select Control** 

TX and RX rates and operating modes can be controlled by the hardware input pins and the register control bits as shown in Table 16 and Table 17. All five rate select control inputs must be set to 0 for 16GFC operation. Either A, B, C, or D must be set to 1 while A2.119.2 = 0 to switch to 32GFC operation. TX and RX operate at the same speed and operating mode and cannot be independently controlled. 

**Table 16:  TX and RX Rate Select Control** 

|**Rate Select Control Inputs**|**Rate Select Control Inputs**|**Rate Select Control Inputs**|**Rate Select Control Inputs**|**Rate Select Control Inputs**|**TX and RX Rate and Operating Mode**|**TX and RX Rate and Operating Mode**|
|---|---|---|---|---|---|---|
|**Software A2h**<br>**Byte 110 Bit 3**|**Software A2h**<br>**Byte 118 Bit 3**|**Software A2h**<br>**Byte 119 Bit 2**|**Hardware Pin 7**<br>**RS0**|**Hardware Pin 9**<br>**RS1**|**Rate**|**Operating Mode**|
|0|0|0|0|0|16GFC|TX RX CDR NRZ|
|A|B|0|C|D|32GFC|TX RX CDR NRZ|
|X|X|1|X|X|64GFC|TX RX CDR PAM4|



## **64GFC Rate Select Control/Status Register** 

The host can assert the 64GFC mode of operation by using I[2] C controls located in Address A2h Byte 119. When asserted, bit 2 of byte 119 enables the module 64GFC Mode of operation, ignoring the RS(0) and RS(1) hard pin and register settings. Byte 119 status bits 0–1 and 3–4 verify internal settings are properly configured for PAM operation at 28.9 GBd. 

**Table 17:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 119)** 

|**Address**<br>**A2h Byte**|**Bit**|**Definition**|**Status/Control**|**Behavior**|
|---|---|---|---|---|
|119|5–7|Unallocated|—|—|
|—|4|64GFC Mode Tx Configured|Status|This status bit is a response to the 64GFC mode control bit. The<br>bit indicates the module Tx logic has finished configuring itself<br>to 64GFC mode at 28.9 GBd.|
|—|3|64GFC Mode Rx Configured|Status|This status bit is a response to the 64GFC mode control bit. The<br>bit indicates the module Rx logic has finished configuring itself<br>to 64GFC mode at 28.9 GBd.|
|—|2|64GFC Mode|Control|Writing a 1 to this bit selects 64GFC speed of operation at<br>28.9 GBd. When this bit is set to 1, the rate select settings on<br>the pins or in the registers are ignored. Default at power up for<br>this bit is 0.|
|—|1|Tx CDR Not Locked|Status|A value of 0 indicates that the CDR is locked, whereas a value<br>of 1 indicates loss of lock of the CDR. In 64GFC mode, if bit 4<br>of this byte is set to 1, a value of 0 indicates that the equalizer<br>has finished adaptation and the CDR is locked to the PAM4<br>signal.|
|—|0|Rx CDR Not Locked|Status|A value of 0 indicates that the CDR is locked, whereas a value<br>of 1 indicates loss of lock of the CDR. In 64GFC mode, if bit 3<br>of this byte is set to 1, a value of 0 indicates that the equalizer<br>has finished adaptation and the CDR is locked to the PAM4<br>signal.|



AFBR-57H5MZ-DS102 15 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 18:  Transceiver Timing Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit.**|**Notes**|
|---|---|---|---|---|---|
|Hardware TX_DISABLE Assert Time (Gamma-t/TP2)|t_off|—|100|µs|a|
|Hardware TX_DISABLE Negate Time (Gamma-t/TP2)|t_on|—|2|ms|b|
|Time to initialize, including reset of TX_FAULT|t_init|—|10|s|c|
|Hardware TX_FAULT Assert Time (Gamma-t/TP2)|t_fault|—|1|ms|d|
|Hardware TX_DISABLE to Reset|t_reset|10|—|µs|e|
|Hardware RX_LOS Deassert Time (Gamma-r/TP3)|t_loss_on|—|100|µs|f|
|Hardware RX_LOS Assert Time (Gamma-r/TP3)|t_loss_off|—|100|µs|g|
|Hardware RATE_SELECT Assert Time RS(0), RS(1)|t_rate_high|—|4|ms|h|
|Hardware RATE_SELECT Deassert Time RS(0), RS(1)|t_rate_low|—|4|ms|h|
|Software TX_DISABLE Assert Time (Gamma-t/TP2)|t_off_soft|—|100|ms|i|
|Software TX_DISABLE Negate Time (Gamma-t/TP2)|t_on_soft|—|100|ms|j|
|Software Tx_FAULT Assert Time (Gamma-t/TP2)|t_fault_soft|—|100|ms|k|
|Software Rx_LOS Assert Time (Gamma-r/TP3)|t_loss_on_soft|—|100|ms|l|
|Software Rx_LOS Deassert Time (Gamma-r/TP3)|t_loss_off_soft|—|100|ms|m|
|Software RATE_SELECT Assert Time RS(0), RS(1)|t_rate_soft_high|—|500|ms|n|
|Software RATE_SELECT Deassert Time RS(0), RS(1)|t_rate_soft_low|—|500|ms|o|
|Software NRZ Tx_LOL Assert Time (Delta-t/TP1)|tx_lol_on_nrz|—|100|ms|p|
|Software NRZ Tx_LOL Deassert Time (Delta-t/TP1)|tx_lol_off_nrz|—|100|ms|q|
|Software PAM Tx_LOL Assert Time (Delta-t/TP1)|tx_lol_on_pam|—|100|ms|r|
|Software PAM Tx_LOL DeAssert Time (Delta-t/TP1)|tx_lol_off_pam|—|100|ms|s|
|Software NRZ Rx_LOL Assert Time (Gamma-r/TP3)|rx_lol_on_nrz|—|40|ms|t|
|Software NRZ Rx_LOL Deassert Time (Gamma-r/TP3)|rx_lol_off_nrz|—|40|ms|u|
|Software PAM Rx_LOL Assert Time (Gamma-r/TP3)|rx_lol_on_pam|—|40|ms|v|
|Software PAM Rx_LOL Deassert Time (Gamma-r/TP3)|rx_lol_off_pam|—|40|ms|w|
|Software 64GFC MODE Assert Time|t_rate_64gfc_high|—|2|s|x|
|Software 64GFC MODE Deassert Time|t_rate_64gfc_low|—|2|s|y|
|Diagnostic Data Ready|t_data|—|5|s|z|
|Serial Bus Hardware Ready|t_serial|—|300|ms|aa|
|Serial Bus Buffer Time|t_buf|20|—|µs|ab|
|Write Cycle Time|t_write|—|80|ms|ac|
|Serial Interface Clock Holdoff “Clock Stretching”|T_clock_hold|—|500|µs|ad|
|Serial ID Clock Rate|f_serial_clock|—|400|kHz|ae|



- a. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

- b. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

c. Time from power on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

- d. From occurrence of fault to assertion of Tx_Fault. 

AFBR-57H5MZ-DS102 16 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

- e. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

- f. Time from loss of optical signal to Rx_LOS Assertion. 

- g. Time from valid optical signal to Rx_LOS Deassertion. 

- h. Time from rising or falling edge of Rate_Select input until transceiver is successfully passing traffic as designated by RS(0) and RS(1). For Rate_Select going high, the internal CDR locks on valid 32GFC encoded data within the specified time. For Rate_Select going low, the internal CDR locks on valid 16GFC encoded data within the specified time. 

- i. Time from I[2] C interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

- j. Time from I[2] C interface deassertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output rises above 90% of nominal. 

- k. Time from fault to I[2] C interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

- l. Time for I[2] C interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

- m. Time for I[2] C interface deassertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

- n. Time from I[2] C interface Assertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is engaged at 32GCFC data rate. 

- o. Time from I[2] C interface Deassertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is either engaged at 16GCFC data rate or bypassed for 8GFC operation. 

- p. Time from loss of TX electrical input CDR data lock to Tx_LOL Assertion for data at 16GFC or 32GFC. Address A2h, Byte 119, bit 1. 

- q. Time from valid TX electrical input CDR data lock to Tx_LOL Deassertion for data at 16GFC or 32GFC. Address A2h, Byte 119, bit 1. 

- r. Time from loss of TX electrical input CDR data lock to Tx_LOL Assertion for data at 64GFC. Address A2h, Byte 119, bit 1. 

- s. Time from valid TX electrical input CDR data lock to Tx_LOL Deassertion for data at 64GFC. Address A2h, Byte 119, bit 1. 

- t. Time from loss of RX optical input CDR data lock to Rx_LOL Assertion for data at 16GFC or 32GFC. Address A2h, Byte 119, bit 0. 

- u. Time from valid RX optical input CDR data lock to Rx_LOL Deassertion for data at 16GFC or 32GFC. Address A2h, Byte 119, bit 0. 

- v. Time from loss of RX optical input CDR data lock to Rx_LOL Assertion for data at 64GFC. Address A2h, Byte 119, bit 0. 

- w. Time from valid RX optical input CDR data lock to Rx_LOL Deassertion for data at 64GFC. Address A2h, Byte 119, bit 0. 

- x. Time from I[2] C interface Assertion of 64GFC MODE input until transceiver has finished configuring itself to 64GFC mode. See address A2h, Byte 119, bits 3 and 4 for the status indicators. 

- y. Time from I[2] C interface Deassertion of 64G MODE input until transceiver has finished configuring itself out of 64GFC mode. See address A2h, Byte 119, bits 3 and 4 for the status indicators. 

- z. From power on to data ready bit asserted (address A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. aa.Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). ab.Time between START and STOP commands. 

ac. Time from stop bit to completion of a write command. Write cycle time is 40 ms for 1–4 bytes and 80 ms for 5–8 bytes. 

ad.Maximum time the SFP+ module may hold the SCL line low before continuing with a read or write operation. 

ae.With a maximum clock stretch of 500 µs. A maximum of 100-kHz operation can be supported without a clock stretch. 

AFBR-57H5MZ-DS102 17 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 19:  Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature<br>Accuracy|TINT|± 5.0|°C|Temperature is measured internal to the transceiver. Valid from 0°C<br>to 75°C case temperature.|
|Transceiver Internal Supply Voltage<br>Accuracy|VINT|± 0.1|V|Supply voltage is measured internal to the transceiver and can, with<br>less accuracy, be correlated to voltage at the SFP Vcc pin. Valid<br>over 3.3V ± 5%.|
|Transmitter Laser DC Bias Current<br>Accuracy|IINT|± 10|%|IINTis better than ± 10% of the nominal value.|
|Transmitted Average Optical<br>Output Power Accuracy|PT|± 3.0|dB|Coupled into 50-µm multi-mode fiber. Valid from 100 µW to 500 µW,<br>average.|
|Received Optical Input Power<br>Accuracy|PR|± 3.0|dB|Coupled from 50-µm multi-mode fiber. Valid from 70 µW to 500 µW<br>average.|



a. TC = 0°C to 75°C, VccT, VccR = 3.3V ± 5%. 

AFBR-57H5MZ-DS102 18 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Figure 11:  Transceiver Timing Diagrams (Module Installed Except Where Noted)** 



AFBR-57H5MZ-DS102 19 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 20:  EEPROM Serial ID Memory Contents – Base SFP Memory (Address A0h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|
|---|---|---|---|---|---|
|0|03|SFP physical device|37|00|Hex Byte of Vendor OUIa|
|1|04|SFP function defined by serial ID only|38|17|Hex Byte of Vendor OUIa|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUIa|
|3|00|—|40|41|“A” – Vendor Part Number ASCII character|
|4|00|—|41|46|“F” – Vendor Part Number ASCII character|
|5|00|—|42|42|“B” – Vendor Part Number ASCII character|
|6|00|—|43|52|“R” – Vendor Part Number ASCII character|
|7|60|Short and Intermediate distance (per FC-PI)|44|2D|“-” – Vendor Part Number ASCII character|
|8|40|Shortwave laser without OFC (open fiber<br>control)|45|35|“5” – Vendor Part Number ASCII character|
|9|04|Multi-mode 50-µm optical media|46|37|“7” – Vendor Part Number ASCII character|
|10|2A|32/16G. Refer to Byte 36 for Extended<br>Specification|47|48|“H” – Vendor Part Number ASCII character|
|11|08|PAM4 per SFF-8024, Table 4-2|48|35|“5” – Vendor Part Number ASCII character|
|12|FF|Bit rate is greater than 25Gb/s. See address<br>66/67.|49|4D|“M“ – Vendor Part Number ASCII character|
|13|10|64/32/16G Independent Tx and Rx Rate<br>Selects|50|5A|“Z” – Vendor Part Number ASCII character|
|14|00|—|51|30|“ “ – Vendor Part Number ASCII character|
|15|00|—|52|31|“ “ – Vendor Part Number ASCII character|
|16|00|Unspecified 50/125 µm OM2 at 64GFC|53|20|“ “ – Vendor Part Number ASCII character|
|17|00|Unspecified 62.5/125 µm OM1 at 64GFC|54|20|“ “ – Vendor Part Number ASCII character|
|18|0A|100m of 50/125 µm OM4 at 64GFC|55|20|“ “ – Vendor Part Number ASCII character|
|19|07|70m of 50/125 µm OM3 at 64GFC|56|20|“ “ – Vendor Revision ASCII character|
|20|41|“A” – Vendor Name ASCII character|57|20|“ “ – Vendor Revision ASCII character|
|21|56|“V” – Vendor Name ASCII character|58|20|“ “ – Vendor Revision ASCII character|
|22|41|“A” – Vendor Name ASCII character|59|20|“ “ – Vendor Revision ASCII character|
|23|47|“G” – Vendor Name ASCII character|60|03|Hex Byte of Laser Wavelengthb|
|24|4F|“O” – Vendor Name ASCII character|61|52|Hex Byte of Laser Wavelengthb|
|25|20|“ “ – Vendor Name ASCII character|62|00|Unallocated|
|26|20|“ “ – Vendor Name ASCII character|63|—|Checksum for Bytes 0–62c|
|27|20|“ “ – Vendor Name ASCII character|64|28|CDRs present. 2.0W power class.|
|28|20|“ “ – Vendor Name ASCII character|65|3A|Hardware SFP TX_DISABLE, TX_FAULT,<br>and RX_LOS, RATE_SELECT|
|29|20|“ “ – Vendor Name ASCII character|66|E7|Upper bit rate.  57.8 Gb/s in units of 250 Mb/s|
|30|20|“ “ – Vendor Name ASCII character|67|00|—|
|31|20|“ “ – Vendor Name ASCII character|68–83|—|Vendor Serial Number ASCII charactersd|
|32|20|“ “ – Vendor Name ASCII character|84–91|—|Vendor Date Code ASCII characterse|
|33|20|“ “ – Vendor Name ASCII character|92|68|Digital Diagnostics, Internal Cal, Rx Pwr Avg|



AFBR-57H5MZ-DS102 

Broadcom 

20 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 20:  EEPROM Serial ID Memory Contents – Base SFP Memory (Address A0h) (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|
|---|---|---|---|---|---|
|34|20|“ “ – Vendor Name ASCII character|93|FA|A/W, Soft SFP TX_DISABLE, TX_FAULT,<br>and RX_LOS, RATE_SELECT|
|35|20|“ “ – Vendor Name ASCII character|94|08|SFF-8472 Compliance to revision 12|
|36|80|64GFC FC-PI-7 per SFF-8024, Table 4-4|95|—|Checksum for Bytes 64–94f|
||||96–255|00|Reserved for Broadcom usef|



- a. The IEEE Organizationally Unique Identifier (OUI) assigned to Broadcom is 00-17-6A (3 bytes of hex). 

- b. Laser wavelength is represented in 16 unsigned bits. The hex representation of 850 (nm) is 0352. 

- c. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored prior to product shipment. 

- d. Addresses 68–83 specify the AFBR-57H5MZ ASCII serial number and will vary on a per-unit basis. 

- e. Addresses 84–91 specify the AFBR-57H5MZ ASCII date code and will vary on a per-date-code basis. 

- f. Bytes 128–255 are undefined and filled with 00h. 

**Table 21:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|
|---|---|---|---|---|---|---|---|
|0|50|Temp H Alarm MSBa|80°C|36|62|Rx Power H Warning MSBg|4 dBm|
|1|0|Temp H Alarm LSBa||37|1E|Rx Power H Warning LSBg||
|2|FB|Temp L Alarm MSBa|–5°C|38|3|Rx Power L Warning MSBg|–10.5 dBm|
|3|0|Temp L Alarm LSBa||39|7B|Rx Power L Warning LSBg||
|4|4B|Temp H Warning MSBa|75°C|40–55|—|Reserved|—|
|5|0|Temp H Warning LSBa||56–94|—|External Calibration Constantsb|—|
|6|0|Temp L Warning MSBa|0°C|95|—|Checksum for Bytes 0–94c|—|
|7|0|Temp L Warning LSBa||96|—|Real Time Temperature MSBa|—|
|8|8D|Vcc H Alarm MSBd|3.63V|97|—|Real Time Temperature LSBa|—|
|9|CC|Vcc H Alarm LSBd||98|—|Real Time Vcc MSBd|—|
|10|74|Vcc L Alarm MSBd|2.97V|99|—|Real Time Vcc LSBd|—|
|11|04|Vcc L Alarm LSBd||100|—|Real Time Tx Bias MSBe|—|
|12|87|Vcc H Warning MSBd|3.465V|101|—|Real Time Tx Bias LSBe|—|
|13|5A|Vcc H Warning LSBd||102|—|Real Time Tx Power MSBf|—|
|14|7A|Vcc L Warning MSBd|3.135V|103|—|Real Time Tx Power LSBf|—|
|15|75|Vcc L Warning LSBd||104|—|Real Time Rx Power MSBg|—|
|16|13|Tx Bias H Alarm MSBe|10 mA|105|—|Real Time Rx Power LSBg|—|
|17|88|Tx Bias H Alarm LSBe||106|—|Reserved|—|
|18|3|Tx Bias L Alarm MSBe|2 mA|107|—|Reserved|—|
|19|E8|Tx Bias L Alarm LSBe||108|—|Reserved|—|



AFBR-57H5MZ-DS102 21 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 21:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h) (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|
|---|---|---|---|---|---|---|---|
|20|10|Tx Bias H Warning MSBe|8.5 mA|109|—|Reserved|—|
|21|9A|Tx Bias H Warning LSBe||110|—|Status/Control – SeeTable 22|—|
|22|5|Tx Bias L Warning MSBe|3 mA|111|—|Reserved|—|
|23|DC|Tx Bias L Warning LSBe||112|—|Flag Bits – SeeTable 23|—|
|24|C3|Tx Power H Alarm MSBf|7 dBm|113|—|Flag Bits – SeeTable 23|—|
|25|C6|Tx Power H Alarm LSBf||114|—|TX Input EQ – SeeTable 25and<br>Table 26|—|
|26|3|Tx Power L Alarm MSBf|–10.8 dBm|115|—|RX Output Emphasis – See<br>Table 27andTable 28|—|
|27|3F|Tx Power L Alarm LSBf||116|—|Flag Bits – SeeTable 23|—|
|28|62|Tx Power H Warning MSBf|4 dBm|117|—|Flag Bits – SeeTable 23|—|
|29|1E|Tx Power H Warning LSBf||118|—|Status/Control – SeeTable 24|—|
|30|6|Tx Power L Warning MSBf|–7.8 dBm|119|—|Status/Control – SeeTable 17|—|
|31|7B|Tx Power L Warning LSBf||120–126|—|Reserved|—|
|32|C3|Rx Power H Alarm MSBg|7 dBm|127|—|Page Select|—|
|33|C6|Rx Power H Alarm LSBg||128–247|—|Custom Configuration Bytes –<br>SeeTable 29|—|
|34|1|Rx Power L Alarm MSBg|–13.5 dBm|248–255|—|Vendor Specific|—|
|35|BE|Rx Power L Alarm LSBg||||||



a. Temperature (Temp) is decoded as a 16-bit signed two’s complement integer in increments of 1/256°C. 

b. Bytes 56–94 are not intended for use, but they have been set to default values per SFF-8472. 

c. Byte 95 is a checksum calculated (per SFF-8472) and is stored prior to product shipment. 

d. Supply Voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 µV. 

e. Tx bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 µA. 

f. Transmitted average optical power (Tx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

- g. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

AFBR-57H5MZ-DS102 22 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 22:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|a|
|6|Soft TX_DISABLE Control|Read/write bit for changing digital state of TX_DISABLE function|a, b|
|5|RS(1) State|Digital state of TX Rate_Select Input Pin RS(1) (1 = Rate High asserted)|—|
|4|RS(0) State|Digital state of RX Rate_Select Input Pin RS(0) (1 = Rate High asserted)|—|
|3|Soft RS(0) Control|Read/write bit for changing digital state of Rx Rate_Select RS(0) function|c|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|a|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|a|
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready (0 = Data Ready)|—|
|a. The response time for soft commands of the AFBR-57H5MZ is 100 msec as specified by MSA SFF-8472.<br>b. Bit 6 is logic ORed with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter.<br>c. Bit 3 is logic ORed with the SFP RS(0) RX Rate_Select input pin 7 …. either asserted will set receiver to Rate = High.||||



**Table 23:  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**|**Flag Bit Name**|**Description**|
|---|---|---|---|
|112|7|Temp High Alarm|Set when transceiver internal temperature exceeds high alarm threshold.|
||6|Temp Low Alarm|Set when transceiver internal temperature exceeds low alarm threshold.|
||5|Vcc High Alarm|Set when transceiver internal supply voltage exceeds high alarm threshold.|
||4|Vcc Low Alarm|Set when transceiver internal supply voltage exceeds low alarm threshold.|
||3|Tx Bias High Alarm|Set when transceiver laser bias current exceeds high alarm threshold.|
||2|Tx Bias Low Alarm|Set when transceiver laser bias current exceeds low alarm threshold.|
||1|Tx Power High Alarm|Set when transmitted average optical power exceeds high alarm threshold.|
||0|Tx Power Low Alarm|Set when transmitted average optical power exceeds low alarm threshold.|
|113|7|Rx Power High Alarm|Set when received average optical power exceeds high alarm threshold.|
||6|Rx Power Low Alarm|Set when received average optical power exceeds low alarm threshold.|
||0–5|reserved|—|
|116|7|Temp High Warning|Set when transceiver internal temperature exceeds high warning threshold.|
||6|Temp Low Warning|Set when transceiver internal temperature exceeds low warning threshold.|
||5|Vcc High Warning|Set when transceiver internal supply voltage exceeds high warning threshold.|
||4|Vcc Low Warning|Set when transceiver internal supply voltage exceeds low warning threshold.|
||3|Tx Bias High Warning|Set when transceiver laser bias current exceeds high warning threshold.|
||2|Tx Bias Low Warning|Set when transceiver laser bias current exceeds low warning threshold.|
||1|Tx Power High Warning|Set when transmitted average optical power exceeds high warning threshold.|
||0|Tx Power Low Warning|Set when transmitted average optical power exceeds low warning threshold.|
|117|7|Rx Power High Warning|Set when received average optical power exceeds high warning threshold.|
||6|Rx Power Low Warning|Set when received average optical power exceeds low warning threshold.|
||0–5|reserved|—|



AFBR-57H5MZ-DS102 

Broadcom 

23 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 24:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4–7|Reserved|—|—|
|3|Soft RS(1) Control|Read/write bit for changing digital state of Tx Rate_Select RS(1)<br>function|a|
|2|Reserved|—|—|
|1|Optional Power Level Operation State|Unused.|—|
|0|Optional Power Level Select|Unused.|—|



a. Bit 3 is logic ORed with the SFP RS(1) TX Rate_Select input pin 9 …. either asserted will set transmitter to Rate = High. 

**Table 25:  EEPROM Serial ID Memory Contents – Transmitter Input Electrical Equalization Control (Address A2h, Byte 114)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|TX EQ, RS(1)=HIGH|Not supported|—|
|3–0|TX EQ, RS(1)=LOW|Not supported|—|



Transmitter input equalization control is adaptive. The value written to the register has no effect. 

**Table 26:  Transmitter Input Equalization Control Values (Address A2h, Byte 114)[a]** 

|**Code**|**Transmitter Input Equalization**|**Transmitter Input Equalization**|
|---|---|---|
||**Nominal**|**Units**|
|xxxx|Reserved|—|



a. From SFF-8472, Table 9-13. 

**Table 27:  EEPROM Serial ID Memory Contents – Receiver Output Electrical Emphasis Control (Address A2h, Byte 115)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|RX EMPH, RS(0)=HIGH|Selects an output emphasis value per SFF-8472, Table 9-14 for high<br>rate operation. 64G/32G|—|
|3–0|RX EMPH, RS(0)=LOW|Selects an output emphasis value per SFF-8472, Table 9-14 for low<br>rate operation. 16G|—|



AFBR-57H5MZ-DS102 

Broadcom 

24 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 28:  Receiver Output Emphasis Control Values (Address A2h, Byte 115)[a]** 

|**Code**|**Receiver Output Emphasis At Nominal Output Amplitude**|**Receiver Output Emphasis At Nominal Output Amplitude**|
|---|---|---|
||**Nominal**|**Units**|
|1xxx|Vendor Specific|—|
|0111|7|dB|
|0110|6|dB|
|0101|5|dB|
|0100|4|dB|
|0011|3|dB|
|0010|2|dB|
|0001|1|dB|
|0000|0|No Emphasis|



a. From SFF-8472, Table 9-14. 

**Table 29:  SFP Signal Integrity Feature Configuration Bytes (2-Wire Address A2h)** 

|**Byte**|**Name**|**R/W**|**Default**|**Description**|
|---|---|---|---|---|
|123–126|Reserved|RO|0|Contents 00h|
|127|Page Select|RW|0|—|
|128–129|Reserved|RO|0|—|
|130|TP1 to TP4 EWRAP Control|RW|0|Bit 7:2 Unused<br>Bit 1:0 = 00; EWRAP Disable, Bleed to TP2 Enabled (normal mode)<br>Bit 1:0 = 01; EWRAP Enable, Bleed to TP2 Enabled<br>Bit 1:0 = 10; EWRAP Enable, Bleed to TP2 Disable<br>Bit 1:0 = 11; EWRAP Enable, Bleed to TP2 Enabled|
|131|Reserved|RW|0|Contents 00h|
|132|Reserved|RW|0|Contents 00h|
|133|TP3 to TP2 OWRAP Control|RW|0|Bit 7:2 Unused<br>Bit 1:0 = 00; OWRAP Disable, Bleed to TP4 Enabled (normal mode)<br>Bit 1:0 = 01; OWRAP Enable, Bleed to TP4 Enabled<br>Bit 1:0 = 10; OWRAP Enable, Bleed to TP4 Disable<br>Bit 1:0 = 11; OWRAP Enable, Bleed to TP4 Enabled|
|134|PRBS Checker BER, MSB|RO|0|Bit 15:10 = Exponent<br>Bit 9:0 = Mantissa<br>Clear on read|
|135|PRBS Checker BER, LSB|RO|0||



AFBR-57H5MZ-DS102 25 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 29:  SFP Signal Integrity Feature Configuration Bytes (2-Wire Address A2h) (Continued)** 

|**Byte**|**Name**|**R/W**|**Default**|**Description**|
|---|---|---|---|---|
|136|PRBS Generator Control|RW|0|Bit 7:5 = 000 = N/A<br>Bit 7:5 = 001 = PRBS9/9Q<br>Bit 7:5 = 010 = PRBS11/11Q<br>Bit 7:5 = 011 = PRBS13/13Q<br>Bit 7:5 = 100 = PRBS23/23Q<br>Bit 7:5 = 101 = PRBS31/31Q<br>Bit 7:5 = 110 = PRBS49/49Q<br>Bit 7:5 = 111 = PRBS58/58Q<br>Bit 4:3 = Don’t Care<br>Bit 2: 0 = System Side at TP1, 1 = Line Side at TP3<br>Bit 1: 0 = Disable Checker, 1 = Enable Checker<br>Bit 0: 0 = Disable PRBS, 1 = Enable PRBS|
|137|64G TX_PRE2|RW|0|Output FFE Pre2, Default (64G) = 0|
|138|64G TX_PRE1|RW|0|Output FFE Pre1, Default (64G) = 0|
|139|64G TX_MAIN|RW|75|Output FFE Main, Default (64G) = 117|
|140|64G TX_POST1|RW|FB|Output FFE Post1, Default (64G) = –5|
|141|64G TX_POST2|RW|0|Output FFE Post2, Default (64G) = 0|
|142|64G TX_POST3|RW|0|Output FFE Post3, Default (64G) = 0<br>The host write to byte 142 sets 64G FFE taps. To read back the tap<br>settings, host must write 80h to byte 142, and taps read out are<br>populated in bytes 137 to 142.|
|143|System 64G RX CTLE|RW|0|Input CTLE 64G<br>Bit 7: Rx Bandwidth 0 = high, 1 = low<br>Bit 6: Set this bit to trigger read back setting on bit 5:0 and bandwidth<br>on bit 7<br>Bit 5:0 Estimated channel loss (0 to 31)|
|144–152|Reserved|RW|0|Contents 00h|
|153|TX CDR Status (TP1 System Side)|RO|0|TX CDR Status (TP1 System Side)<br>Bit 7:5 Unused<br>Bit 4: 1 = PRBS pattern Lock (only used for byte 136 PRBS)<br>Bit 3: 1 = CDR Lock<br>Bit 2: 1 = LOS<br>Bit 1: PLL Unlock Sticky Bit<br>0 = PLL did not transition from locked to unlock<br>1 = PLL transitioned from locked to unlock<br>Clear on read<br>Bit 0: 0 = PLL unlocked, 1 = PLL Lock|



AFBR-57H5MZ-DS102 

Broadcom 

26 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

**Table 29:  SFP Signal Integrity Feature Configuration Bytes (2-Wire Address A2h) (Continued)** 

|**Byte**|**Name**|**R/W**|**Default**|**Description**|
|---|---|---|---|---|
|154|RX CDR Status (TP3 Line Side)|RO|0|RX CDR Status (TP3 Line Side)<br>Bit 7:5 Unused<br>Bit 4: 1 = PRBS pattern Lock (only used for byte 136 PRBS)<br>Bit 3: 1 = CDR Lock<br>Bit 2: 1 = LOS<br>Bit 1: PLL Unlock Sticky Bit<br>0 = PLL did not transition from locked to unlock<br>1 = PLL transitioned from locked to unlock<br>Clear on read<br>Bit 0: 0 = PLL unlocked, 1 = PLL Lock|
|155|Reserved|RO|—|—|
|156|Power On Hours MSB|RW|—|Units of hours. Byte 156 resides in nonvolatile memory (that is,<br>contents are retained during power cycle).|
|157|Power On Hours LSB|RW|—|Units of hours. Byte 157 resides in nonvolatile memory (that is,<br>contents are retained during power cycle).|
|158|Reserved|RW|0|Contents 00h|
|159|32G/16G TX_PRE2|RW|0|Output FFE Pre2, Default (32G/16G) = 0|
|160|32G/16G TX_PRE1|RW|0|Output FFE Pre1, Default (32G/16G) = 0|
|161|32G/16G TX_MAIN|RW|58|Output FFE Main, Default (32G/16G) = 88|
|162|32G/16G TX_POST1|RW|FB|Output FFE Post1, Default (32G/16G) = –5|
|163|32G/16G TX_POST2|RW|0|Output FFE Post2, Default (32G/16G) = 0|
|164|32G/16G TX_POST3|RW|0|Output FFE Post3, Default (32G/16G) = 0<br>The host write to byte 164 sets 32G/16G FFE taps. To read back the<br>tap settings, the host must write 80h to byte 164, and taps read out<br>are populated in bytes 159 to 164.|
|165–241|Reserved|RW|—|—|
|242|Fast CDR Adaptation Enable/<br>Disable|RW|0|Bit 0 = 0 enabled<br>Bit 0 = 1 disabled|
|243|16G/32G Pretrain Status|RW|0|Bit 1:0 = 16G pretrain status<br>Bit 3:2 = 32G pretrain status<br>0 = Not trained<br>1 = Training is running<br>2 = Training finished<br>3 = Training failed|
|244|Reserved|RW|0|Contents 00h|
|245|LSN Control|RW|0|LSN Control<br>Bit 7: = 1b Enter LSN Mode; = 0b Exit LSN Mode<br>Bit 6: = 1b Client Rx Adaptation Reset<br>Bit 5: Unused<br>Bit 4: = 1b: Set up TIA parameters in 16G<br>Bit 3: = 1b: DC offset on at 16G, 0b : off<br>Bit 2: = 0b: Fixed speed switch to 64G Disable, 1b: Fixed speed<br>switch to 64G Enable<br>Bit 1: = 1b Train 32G<br>Bit 0: = 1b Train 16G|
|246–255|Reserved|RW|—|—|



AFBR-57H5MZ-DS102 27 

Broadcom 

64GFC SFP56 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850 nm, 64G/32G/16G 

**AFBR-57H5MZ** Data Sheet 

## **Figure 12:  Module Label** 


**Figure 13:  Module Mechanical Drawing** 


AFBR-57H5MZ-DS102 28 

Broadcom 

Broadcom, the pulse logo, Connecting everything, Avago Technologies, Avago, and the A logo are among the trademarks of Broadcom and/or its affiliates in the United States, certain other countries, and/or the EU. 

Copyright © 2021–2023 Broadcom. All Rights Reserved. 

The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, please visit www.broadcom.com. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

