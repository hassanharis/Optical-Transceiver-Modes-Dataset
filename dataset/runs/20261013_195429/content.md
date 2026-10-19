## **Data Sheet** 

**AFCT-57H5MZ 64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km** 


## **Description** 

The Broadcom[®] AFCT-57H5MZ optical transceiver supports high-speed serial links over singe-mode optical fiber at signaling rates up to 57.8 Gb/s PAM4 (the serial line rate of 64GFC). The product is compliant with Small Form Pluggable SFP+ industry agreements for mechanical and low-speed electrical specifications. High-speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-7. 

The AFCT-57H5MZ is a multirate 1310-nm transceiver that ensures compliance with FC-PI-7 64GFC, 32GFC, and 16GFC specifications. Per the requirements of 64GFC, internal clock and data recovery circuits (CDRs) are present on both electrical input and electrical output of this transceiver. These CDRs lock at 57.8-Gb/s PAM4, 28.05-Gb/s NRZ, and 14.025-Gb/s NRZ (64GFC, 32GFC, and 16GFC) accomplished by using two Rate Select inputs and I[2] C to configure transmit and receive sides. 

Digital diagnostic monitoring information (DMI) is present in the AFCT-57H5MZ per the requirements of SFF-8472, providing real-time monitoring information of transceiver laser, receiver, and environment conditions over an SFF-8431 I[2] C interface. 

## **Features** 

- Compliant to RoHS with 7c-I exemption 

- Broadcom’s high-performance 1310-nm DFB Laser and PiN diode 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 80°C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10B) 

- Diagnostic features per SFF-8472, rev 12.3 “Diagnostic Monitoring Interface for Optical Transceivers” 

- Enhanced operational features including EWRAP, OWRAP, and adaptive electrical EQ/emphasis settings 

- Integrated PRBS generator and bit error rate checker 

- Real-time monitoring of the following: – Transmitter average optical power 

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

- Interswitch or inter-chassis aggregated links 

AFCT-57H5MZ-DS100 February 6, 2023 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

## **Transceiver Block Diagram** 

## **Figure 1:  Block Diagram** 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER RX LOSS OF  SIGNAL<br>PHOTO - TRANS -IMPEDANCE  RD+ (RECEIVE DATA)<br>LIGHT FROM FIBER DETECTOR AMPLIFIER RD-  (RECEIVE DATA)<br>DSP<br>TD+ (TRANSMIT DATA)<br>TD-  (TRANSMIT DATA)<br>MOD -DEF2(SDA)<br>MOD -DEF1(SCL)<br>TRANSMITTER MOD -DEF0<br>MCU<br>BIAS & SAFETY<br>LIGHT TO FIBER DFB Laser<br>CIRCUITRY TX_FAULT<br>TX RATE SELECT RS(1)<br>RX RATE SELECT RS(0)<br>TX_DISABLE<br>**----- End of picture text -----**<br>


## **Transmitter Section** 

The transmitter section includes a transmitter optical sub-assembly (TOSA), a laser driver circuit, and a digital signal processor (DSP) with input variable equalization. The TOSA contains a Broadcom 1310-nm DFB laser light source with an integral light monitoring function and imaging optics to ensure efficient optical coupling to the LC connector interface. The TOSA is driven by a laser driver circuit, which uses the differential output from the DSP to modulate and regulate laser optical power. As mandated by FC-PI-7, the integral TX DSP cleans up any incoming jitter accumulated from the host ASIC, PCB traces, and SFP electrical connector. Between the SFP electrical connector and TX DSP is an adaptive equalization circuit to optimize SFP performance with nonideal incoming electrical waveforms at all rates. 

## **Receiver Section** 

The receiver section includes a receiver optical sub-assembly (ROSA), a preamplification and post-amplification circuit, a DSP circuit with variable emphasis controls, and an integral PRBS generator. The ROSA, containing a high-speed PIN detector, preamplifier, and imaging optics, efficiently couples light from the LC connector interface and performs an optical-to-electrical conversion. The resulting differential electrical signal passes through a post-amplification circuit and into the DSP for cleaning up accumulated jitter. The resulting signal is passed to a high-speed output line driver stage with variable, I[2] C controlled, emphasis settings that allow the host to optimize signal characteristics between the SFP and the host ASIC. 

## **Digital Diagnostics** 

The AFCT-57H5MZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in document SFF-8472. These features allow the host to access, using I[2] C, real-time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage, and laser operating current. 

AFCT-57H5MZ-DS100 2 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

## **Low-Speed Interfaces** 

Conventional low-speed interface I/Os are available as defined in SFF-8431 to manage coarse and fine functions of the optical transceiver. On the transmit side, a Tx_DISABLE input is provided for the host to turn on and off the outgoing optical signal. A transmitter rate select control input pin, Tx_RATE, and I[2] C controls are provided to configure the transmitter stages for 64GFC, 32GFC, or 16GFC operation (logic HIGH reserved for 64GFC and 32GFC, logic LOW reserved for 16GFC). A transmitter fault indicator output, Tx_FAULT, is available for the SFP to signal the host of a transmitter operational problem. A receiver rate select control input, Rx_RATE, configures receiver stages for 64GFC, 32GFC, or 16GFC operation (logic HIGH reserved for 64GFC and 32GFC, logic LOW reserved for 16GFC). In 64G mode, the Rate_Sel pins are ignored. A received optical power loss of signal indicator, RX_LOS, is available to advise the host of a receiver operational problem. 

## **Special Operation Functions** 

See Table 29 for the I[2] C control registers. 

**Figure 2:  OWRAP Functionality (I[2] C Controlled)** 

**Figure 3:  EWRAP Functionality (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT & PRE POST Rx VOUT &<br>AMP AMP Emphasis AMP AMP Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>Laser Laser EQ<br>Driver EQ Driver<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


Electrical and optical high-speed data _wrap_ functions are enabled to assist with local host or remote diagnostic and optimization sequences. Optical data wrap (OWRAP) takes a received optical signal through a CDR and retransmits it optically out. Electrical data wrap (EWRAP) takes an incoming electrical signal through a CDR and retransmits it electrically out. In OWRAP/EWRAP mode, the traffic pass-through can be turned on or off, controlled through I[2] C commands. 

**Figure 4:  SFP TX Input Electrical EQ Is Always Adaptive (No I[2] C Control Needed)** 

**Figure 5:  SFP RX Variable Output Electrical Emphasis (I[2] C controlled))** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT & PRE POST Rx VOUT &<br>AMP AMP Emphasis AMP AMP<br>Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>LaserDriver EQ LaserDriver EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


AFCT-57H5MZ-DS100 3 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

The electrical SFP input stage (TD +/–) has been enhanced with adaptive EQ, which optimizes the transceiver’s input equalization settings without host control. The SFP electrical output stage (RD+/–) has been enhanced with variable output emphasis features to allow host control and optimization of the receiver’s output settings. The host can then select, in situ, the most appropriate SFP setting for a given interconnect scenario. 

**Figure 6:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, Line Side (I[2] C Controlled)** 

**Figure 7:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, System Side (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST PRBS Rx VOUT & PRE POST PRBS Rx VOUT &<br>AMP AMP BER Emphasis AMP AMP Gen Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>LaserDriver PRBSGen EQ LaserDriver PRBSBER EQ<br>r r<br>o o<br>t t<br>c c<br>e e<br>n n<br>n n<br>o o<br>C C<br>P P<br>F F<br>S S<br>**----- End of picture text -----**<br>


The SFP is equipped with an integrated PRBS generator that self-generates programmable PRBS patterns to either system side (TP4) or line side (TP2) at the speed (16G, 32G, or 64G) and operating mode (NRZ or PAM4) to which the SFP is set. The integrated bit error rate checker can also be enabled to measure bit error ratio for every 5 seconds (fixed). It enables users to know the optical link BER performance between TP2 and TP3 of the two separate SFPs or between the host ASIC transmitter (TP0) and the SFP TX input (TP1). 

AFCT-57H5MZ-DS100 4 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 1:  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to<br>the Electrical Contacts|JEDEC Human Body Model (HBM)<br>(JESD22-A114-B)|High-speed contacts withstand 1000V. All other<br>contacts withstand 2000V.|
|ESD to the Optical Connector<br>Receptacle|EN61000-4-2, Criterion B|When installed in a properly grounded housing and<br>chassis, the units are subjected to 15-kV air<br>discharges during operation and 8-kV direct<br>discharges to the case.|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022<br>(CISPR 22A)VCCI Class 1|System margins are dependent on customer board<br>and chassis design.|
|Immunity|EN 55024:2010|Typically shows no measurable effect from a 3-V/m<br>field step from 80 MHz to 1 GHz applied to the module<br>without a chassis enclosure.|
|Laser Eye Safety and Equipment<br>Type Testing|CLASS 1 LASER PRODUCT<br>Complies with 21 CFR 1040.10 except for<br>conformance with IEC 60825-1 Ed.3., as<br>described in Laser Notice No. 56, dated<br>May 8, 2019<br><br>(IEC) EN62368-1: 2014<br><br>(IEC) EN60825-1: 2014<br><br>(IEC) EN60825-2: 2004+A1+A2|CDRH Certification 2111452-000.|
|Component Recognition|Underwriters Laboratories (UL) and<br>Canadian Standards Association (CSA) Joint<br>Component Recognition for Information<br>Technology Equipment including Electrical<br>Business Equipment|UL File: E484615.|
|RoHS Compliance||With 7c-I exemption.|



AFCT-57H5MZ-DS100 5 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Figure 8:  Typical Application Configuration** 


**----- Start of picture text -----**<br>
Tx Rate Select VCC T<br>RS(1)<br>40k 4.7k<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1uF<br>TD +<br>100<br>TD -<br>0.1uF LASER DRIVER<br>4.7k to 10k<br>4.7uH VCCT<br>0.1uF 22 uF 0.1uF<br>3.3V<br>SERDES D S P<br>PROTOCOL IC 4.7uH VCCR<br>0.1uF 22 uF 0.1uF<br>0.1uF<br>RD +<br>100 100<br>RD -<br>LOSS OF  Rx LOS 0.1uF<br>SIGNAL<br>Rx Rate Select RS(0) POST AMP<br>3.3V 40 k<br>GND<br>4.7k to 10k 4.7k to 10k<br>MODULE  4.7k to 10k MOD_ABS MOD_SCL MOD_SDA<br>DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 9:  Recommended Power Supply Filter** 


**NOTE:** Inductors must have less than 0.5Ω series resistance to limit the voltage drop to the SFP module. 

AFCT-57H5MZ-DS100 6 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

## **Table 2:  Pin Description** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground||
|2|TX_FAULT|Transmitter Fault Indication - High indicates a fault condition|a|
|3|TX_DISABLE|Transmitter Disable - Module optical output disables on high or open|b|
|4|MOD_SDA|Module Definition 2 - Two-wire serial ID interface data line (SDA)|c|
|5|MOD_SCL|Module Definition 1 - Two-wire serial ID interface clock line (SCL)|c|
|6|MOD_ABS|Module Definition 0 - Grounded in module (module present indicator)|c|
|7|Rx Rate Select, RS(0)|Receiver Rate Select|d|
|8|RX_LOS|Loss of Signal - High indicates loss of received optical signal|e|
|9|Tx Rate Select, RS(1)|Transmitter Rate Select|d|
|10|VeeR|Receiver Ground||
|11|VeeR|Receiver Ground||
|12|RD-|Inverse Received Data Out|f|
|13|RD+|Received Data Out|f|
|14|VeeR|Receiver Ground||
|15|VccR|Receiver Power +3.3V|g|
|16|VccT|Transmitter Power +3.3V|g|
|17|VeeT|Transmitter Ground||
|18|TD+|Transmitter Data In|h|
|19|TD-|Inverse Transmitter Data In|h|
|20|VeeT|Transmitter Ground||



- a. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7 kΩ to 10 kΩ resistor on the host board. When high, this output indicates a laser fault of some kind. Low indicates normal operation. In the low state, the output is pulled to < 0.4V. 

|b.|TX_DISABLE is an input that shuts|down the transmitter optical output. It is internally pulled up (within the transceiver) with a 4.7-kΩ resistor.|
|---|---|---|
||Low (–0.3V to 0.8V):|Transmitter on|
||Between (0.8V and 2.0V):|Undefined|
||High (2.0V to Vcc + 0.3) or OPEN:|Transmitter Disabled|



- c. The signals Mod_ABS, SCL, SDA designate the two-wire serial interface pins. They must be pulled up with a 4.7 kΩ to 10 kΩ resistor on the host board. Mod_ABS is grounded by the module to indicate the module is present. Mod_SCL is serial clock line (SCL) of two-wire serial interface. Mod_SDA is serial data line (SDA) o two-wire serial interface. 

- d. The rate select input pin selects the signal rates along with the software rate select bits as shown in Table 16 and Table 17. It is internally pulled down with a 40-kΩ resistor. 

- e. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7-kΩ to 10- kΩ resistor on the host board. When high, this output indicates the received optical power is below the worst-case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to < 0.4V. 

- f. RD–/+ designate the differential receiver outputs. They are AC-coupled 100Ω differential lines that should be terminated with 100Ω differential at the host SerDes input. AC-coupling is done inside the transceiver and is not required on the host board. 

- g. VccR and VccT are the receiver and transmitter power supplies. Refer to SFF-8419 for details. 

- h. TD–/+ designate the differential transmitter inputs. They are AC coupled differential lines with 100Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. 

AFCT-57H5MZ-DS100 7 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

Stress in excess of any of the individual absolute maximum ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently. Exposure to any of the absolute maximum ratings for extended periods can adversely affect reliability. 

**Table 3:  Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|
|Storage Temperature|Ts|–40|85|°C|a|
|Relative Humidity|RH|5|95|%||
|SupplyVoltage|Vcc|–0.3|3.63|V||
|Low Speed Input Voltage|Vi|–0.3|Vcc + 0.5, 3.63|V||
|Low Speed Output Current||–20|20|mA||



- a. Absolute maximum ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. Refer to the reliability data sheet for specific reliability performance. Between the absolute maximum ratings and the Recommended Operating Conditions, functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted. Optical and electrical characteristics are not defined for operation outside the recommended operating conditions, reliability is not implied, and damage to the module may occur for such operation over an extended period of time. 

**Table 4:  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tc|0|—|80|°C|a|
|SupplyVoltage|Vcc|3.135|3.3|3.465|V||
|Data Rate||14.025<br>14.025|—<br>—|28.9<br>57.8|GBd<br>Gb/s|b|
|Two-Wire Serial (TWS) Interface<br>Clock Rate||—|—|400|kHz|c|



- a. The position of case temperature measurement is shown in Figure 13. Continuous operation at the maximum recommended operating case temperature should be avoided to not degrade reliability. 

- b. 64GFC PAM4 requires FEC RS(544,514) encoding per FC-PI-7. 32GFC NRZ requires FEC RS(528,514) per FC-PI-6, and 16GFC NRZ does not require FEC per FC-PI-5. 

- c. With 500-µs maximum clock stretch per SFF-8419. 

AFCT-57H5MZ-DS100 8 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

The following transceiver electrical characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 5:  Transceiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|---|
|Transceiver Power Consumption||—|—|2.0|W|a|
|||—|—|2.1|W||
|Power Supply Noise Rejection (peak-peak)|PSNR|—|—|66|mV|b|
|Low Speed Outputs<br>TX_FAULT, RX_LOS, MOD_SDA|VOL|–0.3|—|0.4|V|c|
||IOH|–50|—|37.5|μA||
|Low Speed Inputs<br>TX_DIS, MOD_SCL, MOD_SDA, RS(0), RS(1)|VIL|–0.3|—|0.8|V|d|
||VIH|2.0|—|VccT + 0.3|V||



a. Power consumption at 3.3V ± 5% is 2.0W max. Power consumption at 3.3V +0/–5% over 70°C is 2.1W max. 

b. Filter per the SFP specification is required on the host board to remove 10-Hz to 2-MHz content. 

c. Pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

d. Mod_SCL and Mod_SDA must be pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

The following high-speed electrical module input characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 6:  High-Speed Electrical Module Input Characteristics[a]** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|64GFC Signaling Rate, Per Lane|B’|—|28.9|—|GBd|±100 ppm, PAM4 and<br>RS(544,514)<br>FEC encoded|
|32GFC Signaling Rate, Per Lane|B’|—|28.05|—|GBd|±100 ppm, NRZ and<br>RS(528, 514)<br>FEC encoded|
|16GFC SignalingRate, Per Lane|B’|—|14.025|—|GBd|±100ppm, NRZ|
|Differential pk-pk Input Voltage<br>Tolerance|B’|900|—|—|mV||
|Differential Termination Resistance<br>Mismatch|B’|—|—|10|%||
|Differential Return Loss, SDD11 min.|B’|—|Eq. 1, Fig. 9|—|dB|IEEE 802.3 Annex 83E|
|Differential Mode to Common-Mode<br>Conversion, min.|B’|—|Eq. 2, Fig. 10|—|dB|IEEE 802.3 Annex 83E|
|Common-Mode Output Voltage|B’|—|—|—|V|b|



a. From FC-PI-7, Table 11. 

b. DC common mode voltage is generated by the host. The specification includes the effects of ground offset voltage. 

AFCT-57H5MZ-DS100 9 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 7:  Stressed Input Test Conditions** 

|**Parameter**|**Value**|**Unit**|**Notes/Conditions**|
|---|---|---|---|
|Module Stressed Input Test|||a|
|Eye Width at 10–5ProbabilityEW5|0.23|UI||
|Eye Height at 10–5ProbabilityEH5|34|mV||
|Vertical Eye Closure VEC(max.)|12|dB||



a. Module stressed input tolerance is measured using the procedure defined in 83E.3.4.1.1. 

## **Table 8:  Reference Points** 

|**Test Point**|**Description**|
|---|---|
|B’|Module electrical input at the input of the module compliance board. Module return loss specifications are met at this<br>point.|
|C’|Module electrical output at the output of the module compliance board. Module output and module return loss<br>specifications are met at thispoint.|



**Figure 10:  FC-PI-7 Module Compliance Points** 


AFCT-57H5MZ-DS100 10 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 9:  High-Speed Electrical Module Output Characteristics[a]** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|Differential Output Voltage (Enabled)|C’|—|—|900|mV|Measured with<br>PRBS13Q|
|Differential Output Voltage (Disabled)|C’|—|—|35|mV|Measured with<br>PRBS13Q|
|Common Mode Noise, RMS|C’|—|—|17.5|mV||
|Differential Termination Mismatch|C’|—|—|10|%||
|Differential Output Return Loss SDD22<br>(min.)|C’|—|Eq. 1, Fig. 9|—|dB|FC-PI-7|
|Common to Differential Mode Conversion<br>SDC22, min.|C’|—|Eq 2, Fig. 10|—|dB|FC-PI-7|
|Source Transition Time(20% to 80%)|C’|9.5|—|—|ps||
|Common-Mode Voltage|C’|—|—|—|V|b|
|Eye Width at 10–5ProbabilityEW5|C’|0.265|—|—|UI||
|Eye Height at 10–5ProbabilityEH5|C’|70|—|—|mV||
|Vertical Eye Closure(VEC)|C’|—|—|12|dB||
|Near-End Eye Symmetry Mask Width<br>(ESMW)|C’|—|0.265|—|UI||
|Near-end Eye Height, Differential|C’|70|—|—|mV||
|Far-end ESMW|C’|—|0.2|—|UI||
|Far-end Eye Height, Differential|C’|30|—|—|mV||
|Far-end Pre-cursor ISI Ratio|C’|–4.5|—|2.5|%||



a. From FC-PI-7, Table 10. 

b. DC common-mode voltage is generated by the host. The specification includes the effects of ground offset voltage. 

AFCT-57H5MZ-DS100 11 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 10:  64GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|64GFC Signaling Rate|gamma-T|—|28.9|—|GBd|±100 ppm, PAM4 and<br>RS(544,514)FEC encoded|
|Center Wavelength Range|gamma-T|1304.5|—|1317.5|nm||
|Side-Mode Suppression Ratio|gamma-T|30|—|—|dB||
|Transmitter and Dispersion Eye Closure for<br>PAM4(TDECQ)|gamma-T|—|—|4|dB||
|TDECQ 10log10(Ceq)|gamma-T|—|—|4|dB||
|Optical Modulation Amplitude (OMAouter)|gamma-T|–1.5a|—|+4.0|dBm||
|OMAouterExtinction Ratio|gamma-T|3.5|—|—|dB||
|Launch Power in OMAouter minus TDECQ|gamma-T|–2.9|—|—|dBm||
|Average Launch Power|gamma-T|–4.5|—|+4.2|dBm||
|Average Launch Power to OFF Transmitter|gamma-T|—|—|–16|||
|RIN12OMA|gamma-T|—|—|–134|dB/Hz||
|Transmitter Transition Time, 20% to 80%|gamma-T|—|—|34|ps||
|Optical Return Loss Tolerance|gamma-T|—|—|15.6|dB||
|Transmitter Reflectance|gamma-T|—|—|–26|dB||



a. Even if the TDEC < 1.4 dB, the OMA (min.) must exceed this value. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 11:  64GFC Mode Optical Receiver Characteristics (per PC-PI-7)** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/**<br>**Conditions**|
|---|---|---|---|---|---|---|
|Center Wavelength Range|gamma-R|1304.5|—|1317.5|nm||
|Damage Threshold|gamma-R|+5.2|—|—|dBm|BER 1.09E–4|
|Average Receive Power|gamma-R|–10.8|—|+4.2|dBm|BER 1.09E–4|
|Receive Power (OMAouter)|gamma-R|—|—|+4.0|dBm|BER 1.09E–4|
|Receiver Reflectance|gamma-R|—|—|–26|dB||
|Receiver Sensitivity (OMAouter)|gamma-R|—|—|–8.9|dBm|BER 1.09E–4|
|Stressed Receiver Sensitivity OMAouter|gamma-R|—|—|–5.8|dBm|BER 1.09E–4|
|Conditions of Stressed Receiver SensitivityTest|gamma-R|—|—|—|||
|Stressed Eye Closure for PAM4(SECQ)|gamma-R|—|—|4|dB|BER 1.09E–4|
|SECQ 10log10(Ceq)|gamma-R|—|—|4|dB|BER 1.09E–4|
|LOS Assert|gamma-R|–30|—|—|dBm avg||
|LOS Deassert|gamma-R|—|—|–10|dBm avg||
|LOS Hysteresis|gamma-R|0.5|—|—|dB||



AFCT-57H5MZ-DS100 12 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 12:  32GFC Mode Optical Transmitter Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|32GFC Signaling Rate, Per Lane||—|28.05|—|GBd|±100 ppm NRZ, RS(528,514)<br>FEC encoded|
|Modulated Optical Output Power (OMA)<br>(Peak-to-Peak) 28.05 Gb/s|TX,OMA|631|—|—|µW||
|||–2.0|—|—|dBm||
|Average Optical Output Power 28.05 Gb/s|Pout|–5.0|—|+3|dBm|b|
|Transmitter Distortion Penalty, 28.05 Gb/s|TDP|—|—|2.7|dB||



a. Tc = 0°C to 80°C, VccT, VccR = 3.3V ± 5%. 

- b. Max. Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 13:  32GFC Mode Optical Receiver Characteristic** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power, 28.05 Gb/s|PIN|—|—|+3|dBm,avg||
|Unstressed Receiver Sensitivity|OMA|–11.4|—|—|dBm|a, b|
|Optical Return Loss||26|—|—|dB||
|Center Wavelength Range||1304.5|—|1317.5|nm||
|LOS Assert||–30|—|—|dBm,avg||
|LOS Deassert||—|—|–12.5|dBm,avg||
|LOS Hysteresis||0.5|—|—|dB||



a. Input Optical Modulation Amplitude (commonly known as sensitivity] requires a valid Fibre Channel encoded input. 

- b. 32GFC (28.05 Gb/s) assumes an FEC encoded RS(528, 514) signal and allows a BER of 1E–6 for receiver and transmitter measurements. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 14:  16GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|16GFC Signaling Rate, Per Lane||—|14.025|—|GBd|±100 ppm NRZ,<br>No FEC|
|Modulated Optical Output Power (OMA) (Peak to Peak)<br>14.025 Gb/s|TX,OMA|631|—|—|µW||
|||–2.0|—|—|dBm||
|Average Optical Output Power|Pout|–5.0|—|2.0|dBm|a|
|Transmitter Distortion Penalty, 14.025 Gb/s|TDP|—|—|4.4|dB||
|Extinction Ratio||3.5|—|—|dB||



a. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 15:  16GFC Mode Optical Receiver Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power|PIN|—|—|2.0|dBm,avg|Per FC-PI-5|
|Unstressed Receiver Sensitivity|OMA|–12.0|—|—|dBm|a|



a. Input Optical Modulation Amplitude (commonly known as sensitivity) requires a valid Fibre Channel encoded input and allows a BER of 1E–12. 

AFCT-57H5MZ-DS100 13 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

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

The host can assert the 64GFC mode of operation by using I[2] C controls located in Address A2h Byte 119. When asserted, bit 2 of byte 119 enables the module 64GFC mode of operation, ignoring the RS(0) and RS(1) hard pin and register settings. Byte 119 status bits 0–1 and 3–4 verify that internal settings are properly configured for PAM operation at 28.9 GBd. 

**Table 17:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 119)** 

|**Address**<br>**A2h Byte**|**Bit**|**Definition**|**Status/Control**|**Behavior**|
|---|---|---|---|---|
|119|5–7|Unallocated|||
||4|64GFC Mode TX Configured|Status|This status bit is a response to the 64GFC mode control bit. The<br>bit indicates the module TX logic has finished configuring itself<br>to 64GFC mode at 28.9 GBd.|
||3|64GFC Mode RX Configured|Status|This status bit is a response to the 64GFC mode control bit. The<br>bit indicates the module RX logic has finished configuring itself<br>to 64GFC mode at 28.9 GBd.|
||2|64GFC Mode|Control|Writing a 1 to this bit selects 64GFC speed of operation at<br>28.9 GBd. When this bit is set to 1, the rate select settings on<br>the pins or in the registers are ignored. Default at power up for<br>this bit is 0.|
||1|TX CDR Not Locked|Status|A value of 0 indicates that the CDR is locked, whereas a value<br>of 1 indicates loss of lock of the CDR. In 64GFC mode, if bit 4<br>of this byte is set to 1, a value of 0 indicates that the equalizer<br>has finished adaptation and the CDR is locked to the PAM4<br>signal.|
||0|RX CDR Not Locked|Status|A value of 0 indicates that the CDR is locked, whereas a value<br>of 1 indicates loss of lock of the CDR. In 64GFC mode, if bit 3<br>of this byte is set to 1, a value of 0 indicates that the equalizer<br>has finished adaptation and the CDR is locked to the PAM4<br>signal.|



AFCT-57H5MZ-DS100 14 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 18:  Transceiver Timing Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit.**|**Notes**|
|---|---|---|---|---|---|
|Hardware TX_DISABLE Assert Time (Gamma-t/TP2)|t_off|—|100|µs|a|
|Hardware TX_DISABLE Negate Time (Gamma-t/TP2)|t_on|—|2|ms|b|
|Time to Initialize, Including Reset of TX_FAULT|t_init|—|10|s|c|
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
|Software 64GFC MODE Assert Time|t_rate_64gfc_high|—|2000|ms|x|
|Software 64GFC MODE Deassert Time|t_rate_64gfc_low|—|500|ms|y|
|Diagnostic Data Ready|t_data|—|5|s|z|
|Serial Bus Hardware Ready|t_serial|—|300|ms|aa|
|Serial Bus Buffer Time|t_buf|20|—|µs|ab|
|Write Cycle Time|t_write|—|80|ms|ac|
|Serial Interface Clock Holdoff “Clock Stretching”|T_clock_hold|—|500|µs|ad|
|Serial ID Clock Rate|f_serial_clock|—|400|kHz|ae|



a. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

b. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

c. Time from power on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

d. From occurrence of fault to assertion of Tx_Fault. 

AFCT-57H5MZ-DS100 15 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

- e. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

- f. Time from loss of optical signal to Rx_LOS Assertion. 

- g. Time from valid optical signal to Rx_LOS Deassertion. 

- h. Time from rising or falling edge of Rate_Select input until transceiver is successfully passing traffic as designated by RS(0) and RS(1). For Rate_Select going high, the internal CDR locks on valid 32GFC encoded data within the specified time. For Rate_Select going low, the internal CDR locks on valid 16GFC encoded data within the specified time. 

- i. Time from I[2] C interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

- j. Time from I[2] C interface deassertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output rises above 90% of nominal. k. Time from fault to I[2] C interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

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

- z. From power on to data ready bit asserted (address A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

- aa.Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). ab.Time between START and STOP commands. 

ac. Time from stop bit to completion of a write command. Write cycle time is 40 ms for 1–4 bytes and 80 ms for 5–8 bytes. 

ad.Maximum time the SFP+ module may hold the SCL line low before continuing with a read or write operation. 

ae.With a maximum clock stretch of 500 µs. A maximum of 100-kHz operation can be supported without a clock stretch. 

AFCT-57H5MZ-DS100 16 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 19:  Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Unit**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature<br>Accuracy|TINT|±5.0|°C|Temperature is measured internal to the transceiver. Valid from 0°C<br>to 80°C case temperature.|
|Transceiver Internal Supply Voltage<br>Accuracy|VINT|±0.1|V|Supply voltage is measured internal to the transceiver and can, with<br>less accuracy, be correlated to voltage at the SFP Vcc pin. Valid<br>over 3.3V ± 5%.|
|Transmitter Laser DC Bias Current<br>Accuracy|IINT|±10|%|IINTis better than ±10% of the nominal value.|
|Transmitted Average Optical<br>Output Power Accuracy|PT|±3.0|dB|Coupled into 9-µm single-mode fiber. Valid from –5 dBm to 4.2 dBm,<br>average.|
|Received Optical Input Power<br>Accuracy|PR|±3.0|dB|Coupled from 9-µm single-mode fiber. Valid from –12 dBm to<br>4.2 dBm, average.|



a. TC = 0°C to 80°C, VccT, VccR = 3.3V ± 5%. 

**Figure 11:  Transceiver Timing Diagrams (Module Installed Except Where Noted)** 



AFCT-57H5MZ-DS100 17 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 20:  EEPROM Serial ID Memory Contents – Base SFP Memory (Address A0h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|
|---|---|---|---|---|---|
|0|03|SFP physical device|37|00|Hex Byte of Vendor OUIa|
|1|04|SFP function defined by serial ID only|38|17|Hex Byte of Vendor OUIa|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUIa|
|3|00||40|41|“A” – Vendor Part Number ASCII character|
|4|00||41|46|“F” – Vendor Part Number ASCII character|
|5|00||42|42|“C” – Vendor Part Number ASCII character|
|6|00||43|52|“T” – Vendor Part Number ASCII character|
|7|12|Longdistance, longwave laser(per FC-PI)|44|20|“-” – Vendor Part Number ASCII character|
|8|00||45|35|“5” – Vendor Part Number ASCII character|
|9|01|Single-mode optical media|46|37|“7” – Vendor Part Number ASCII character|
|10|2A|32/16G. See Byte 36 for extended specification.|47|48|“H” – Vendor Part Number ASCII character|
|11|08|PAM4per SFF-8024, Table 4-2|48|35|“5” – Vendor Part Number ASCII character|
|12|FF|Bit rate isgreater than 25 Gb/s. See address 66/67.|49|4D|“M“ – Vendor Part Number ASCII character|
|13|10|64/32/16G independent TX and RX rate selects|50|5A|“Z” – Vendor Part Number ASCII character|
|14|0A|10-km single-mode length, in units of km|51|20|“ “ – Vendor Part Number ASCII character|
|15|64|10-km single-mode length, in units of 100 meters|52|20|“ “ – Vendor Part Number ASCII character|
|16|00|Unspecified 50/125µm OM2 at 64GFC|53|20|“ “ – Vendor Part Number ASCII character|
|17|00|Unspecified 62.5/125µm OM1 at 64GFC|54|20|“ “ – Vendor Part Number ASCII character|
|18|00|Unspecified 50/125µm OM4 at 64GFC|55|20|“ “ – Vendor Part Number ASCII character|
|19|00|Unspecified 50/125µm OM3 at 64GFC|56|20|“ “ – Vendor Revision ASCII character|
|20|41|“A” – Vendor Name ASCII character|57|20|“ “ – Vendor Revision ASCII character|
|21|56|“V” – Vendor Name ASCII character|58|20|“ “ – Vendor Revision ASCII character|
|22|41|“A” – Vendor Name ASCII character|59|20|“ “ – Vendor Revision ASCII character|
|23|47|“G” – Vendor Name ASCII character|60|05|Hex Byte of Laser Wavelengthb|
|24|4F|“O” – Vendor Name ASCII character|61|1E|Hex Byte of Laser Wavelengthb|
|25|20|“ “ – Vendor Name ASCII character|62|00|Unallocated|
|26|20|“ “ – Vendor Name ASCII character|63||Checksum for Bytes 0–62c|
|27|20|“ “ – Vendor Name ASCII character|64|28|CDRspresent. 2.0Wpower class.|
|28|20|“ “ – Vendor Name ASCII character|65|3A|Hardware SFP TX_DISABLE, TX_FAULT, and<br>RX_LOS, RATE_SELECT|
|29|20|“ “ – Vendor Name ASCII character|66|E7|Upper bit rate. 57.8 Gb/s in units of 250 Mb/s|
|30|20|“ “ – Vendor Name ASCII character|67|00||
|31|20|“ “ – Vendor Name ASCII character|68–83||Vendor Serial Number ASCII charactersd|
|32|20|“ “ – Vendor Name ASCII character|84–91||Vendor Date Code ASCII characterse|
|33|20|“ “ – Vendor Name ASCII character|92|68|Digital Diagnostics, Internal Cal, RX Pwr Avg|
|34|20|“ “ – Vendor Name ASCII character|93|FA|A/W, Soft SFP TX_DISABLE, TX_FAULT, and<br>RX_LOS, RATE_SELECT|
|35|20|“ “ – Vendor Name ASCII character|94|08|SFF-8472 Compliance to revision 12.3|
|36|80|64GFC per SFF-8024, Table 4-4|95||Checksum for Bytes 64–94f|
||||96–255|00|Reserved for Broadcom usef|



a. The IEEE Organizationally Unique Identifier (OUI) assigned to Broadcom is 00-17-6A (3 bytes of hex). 

AFCT-57H5MZ-DS100 18 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

- b. Laser wavelength is represented in 16 unsigned bits. The hex representation of 1310 (nm) is 051E. 

- c. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored prior to product shipment. 

- d. Addresses 68–83 specify the AFCT-57H5MZ ASCII serial number and will vary on a per-unit basis. 

- e. Addresses 84–91 specify the AFCT-57H5MZ ASCII date code and will vary on a per-date-code basis. 

- f. Bytes 128–255 are undefined and filled with 00h. 

**Table 21:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|
|---|---|---|---|---|---|---|---|
|0|55|TempH Alarm MSBa|85°C|36|66|RX Power H WarningMSBg|4.2 dBm|
|1|0|TempH Alarm LSBa||37|BE|RX Power H WarningLSBg||
|2|FB|TempL Alarm MSBa|–5°C|38|03|RX Power L WarningMSBg|–10.8 dBm|
|3|0|TempL Alarm LSBa||39|3F|RX Power L WarningLSBg||
|4|50|TempH WarningMSBa|80°C|40–55||Reserved||
|5|0|TempH WarningLSBa||56–94||External Calibration Constantsb||
|6|0|TempL WarningMSBa|0°C|95||Checksum for Bytes 0–94c||
|7|0|TempL WarningLSBa||96||Real Time Temperature MSBa||
|8|8D|Vcc H Alarm MSBd|3.63V|97||Real Time Temperature LSBa||
|9|CC|Vcc H Alarm LSBd||98||Real Time Vcc MSBd||
|10|74|Vcc L Alarm MSBd|2.97V|99||Real Time Vcc LSBd||
|11|04|Vcc L Alarm LSBd||100||Real Time TX Bias MSBe||
|12|87|Vcc H WarningMSBd|3.465V|101||Real Time TX Bias LSBe||
|13|5A|Vcc H WarningLSBd||102||Real Time TX Power MSBf||
|14|7A|Vcc L WarningMSBd|3.135V|103||Real Time TX Power LSBf||
|15|75|Vcc L WarningLSBd||104||Real Time RX Power MSBg||
|16|AF|TX Bias H Alarm MSBe|90 mA|105||Real Time RX Power LSBg||
|17|C8|TX Bias H Alarm LSBe||106||Reserved||
|18|0B|TX Bias L Alarm MSBe|6 mA|107||Reserved||
|19|B8|TX Bias L Alarm LSBe||108||Reserved||
|20|9C|TX Bias H WarningMSBe|80 mA|109||Reserved||
|21|40|TX Bias H WarningLSBe||110||Status/Control – SeeTable 22||
|22|0F|TX Bias L WarningMSBe|8 mA|111||Reserved||
|23|A0|TX Bias L WarningLSBe||112||Flag Bits – SeeTable 23||
|24|CD|TX Power H Alarm MSBf|7.2 dBm|113||Flag Bits – SeeTable 23||
|25|00|TX Power H Alarm LSBf||114||TX Input EQ – SeeTable 25andTable 26||
|26|06|TX Power L Alarm MSBf|–7.5 dBm|115||RX Output Emphasis – SeeTable 27and<br>Table 28||
|27|F2|TX Power L Alarm LSBf||116||Flag Bits – SeeTable 23||



AFCT-57H5MZ-DS100 19 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 21:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h) (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|**Byte**<br>**Number**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Values**|
|---|---|---|---|---|---|---|---|
|28|66|TX Power H WarningMSBf|4.2 dBm|117||Flag Bits – SeeTable 23||
|29|BE|TX Power H WarningLSBf||118||Status/Control – SeeTable 24||
|30|0D|TX Power L WarningMSBf|–4.5 dBm|119||Status/Control – SeeTable 17||
|31|DC|TX Power L WarningLSBf||120–126||Reserved||
|32|CD|RX Power H Alarm MSBg|7.2 dBm|127||Page Select||
|33|0|RX Power H Alarm LSBg||128–247||Custom Configuration Bytes – SeeTable 29||
|34|1|RX Power L Alarm MSBg|–13.8 dBm|248–255||Vendor Specific||
|35|A0|RX Power L Alarm LSBg||||||



- a. Temperature (Temp) is decoded as a 16-bit signed two’s complement integer in increments of 1/256°C. 

b. Bytes 56–94 are not intended for use, but they have been set to default values per SFF-8472. 

- c. Byte 95 is a checksum calculated (per SFF-8472) and is stored prior to product shipment. 

d. Supply Voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 µV. 

- e. TX bias current (TX Bias) is decoded as a 16-bit unsigned integer in increments of 2 µA. 

- f. Transmitted average optical power (TX Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

- g. Received average optical power (RX Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

**Table 22:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|a|
|6|Soft TX_DISABLE Control|Read/write bit for changing digital state of TX_DISABLE function|a, b|
|5|RS(1)State|Digital state of TX Rate_Select Input Pin RS(1) (1 = Rate High asserted)||
|4|RS(0)State|Digital state of RX Rate_Select Input Pin RS(0) (1 = Rate High asserted)||
|3|Soft RS(0) Control|Read/write bit for changing digital state of RX Rate_Select RS(0) function|c|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|a|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|a|
|0|Data Ready (Bar)|Indicates transceiver ispowered and real-time sense data is ready (0 = Data Ready)||



a. The response time for soft commands of the AFCT-57H5MZ is 100 ms as specified by MSA SFF-8472. 

b. Bit 6 is logic ORed with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter. 

- c. Bit 3 is logic ORed with the SFP RS(0) RX Rate_Select input pin 7 …. either asserted will set receiver to Rate = High. 

AFCT-57H5MZ-DS100 20 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 23:  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)[a]** 

|**Byte**|**Bit**|**Flag Bit Name**|**Description**|
|---|---|---|---|
|112|7|TempHigh Alarm|Set when transceiver internal temperature exceeds high alarm threshold.|
||6|TempLow Alarm|Set when transceiver internal temperature exceeds low alarm threshold.|
||5|Vcc High Alarm|Set when transceiver internal supplyvoltage exceeds high alarm threshold.|
||4|Vcc Low Alarm|Set when transceiver internal supplyvoltage exceeds low alarm threshold.|
||3|Tx Bias High Alarm|Set when transceiver laser bias current exceeds high alarm threshold.|
||2|Tx Bias Low Alarm|Set when transceiver laser bias current exceeds low alarm threshold.|
||1|Tx Power High Alarm|Set when transmitted average opticalpower exceeds high alarm threshold.|
||0|Tx Power Low Alarm|Set when transmitted average opticalpower exceeds low alarm threshold.|
|113|7|Rx Power High Alarm|Set when received average opticalpower exceeds high alarm threshold.|
||6|Rx Power Low Alarm|Set when received average opticalpower exceeds low alarm threshold.|
||0–5|Reserved||
|116|7|TempHigh Warning|Set when transceiver internal temperature exceeds high warningthreshold.|
||6|TempLow Warning|Set when transceiver internal temperature exceeds low warningthreshold.|
||5|Vcc High Warning|Set when transceiver internal supplyvoltage exceeds high warningthreshold.|
||4|Vcc Low Warning|Set when transceiver internal supplyvoltage exceeds low warningthreshold.|
||3|Tx Bias High Warning|Set when transceiver laser bias current exceeds high warningthreshold.|
||2|Tx Bias Low Warning|Set when transceiver laser bias current exceeds low warningthreshold.|
||1|Tx Power High Warning|Set when transmitted average opticalpower exceeds high warningthreshold.|
||0|Tx Power Low Warning|Set when transmitted average opticalpower exceeds low warningthreshold.|
|117|7|Rx Power High Warning|Set when received average opticalpower exceeds high warningthreshold.|
||6|Rx Power Low Warning|Set when received average opticalpower exceeds low warningthreshold.|
||0–5|Reserved||



a. Flags are latched, read on clear. 

AFCT-57H5MZ-DS100 21 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 24:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4–7|Reserved|||
|3|Soft RS(1) Control|Read/write bit for changing digital state of TX Rate_Select RS(1)<br>function|a|
|2|Reserved|||
|1|Optional Power Level Operation State|Unused.||
|0|Optional Power Level Select|Unused.||



a. Bit 3 is logic ORed with the SFP RS(1) TX Rate_Select input pin 9. Either bit 3 or pin 9 asserted will set transmitter to Rate = High. 

**Table 25:  EEPROM Serial ID Memory Contents – Transmitter Input Electrical Equalization Control (Address A2h, Byte 114)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|TX EQ, RS(1)= HIGH|Not supported||
|3–0|TX EQ, RS(1)= LOW|Not supported||



Transmitter input equalization control is adaptive. The value written to the register has no effect. 

**Table 26:  Transmitter Input Equalization Control Values (Address A2h, Byte 114)[a]** 

|**Code**|**Transmitter Input Equalization**|**Transmitter Input Equalization**|
|---|---|---|
||**Nominal**|**Unit**|
|xxxx|Reserved||



a. From SFF-8472, Table 9-13. 

**Table 27:  EEPROM Serial ID Memory Contents – Receiver Output Electrical Emphasis Control (Address A2h, Byte 115)** 

|**Bit**<br>**Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|RX EMPH, RS(0) = HIGH|Selects an output emphasis value per SFF-8472, Table 9-14 for high<br>rate operation. 64G/32G||
|3–0|RX EMPH, RS(0) = LOW|Selects an output emphasis value per SFF-8472, Table 9-14 for low<br>rate operation. 16G||



AFCT-57H5MZ-DS100 22 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 28:  Receiver Output Emphasis Control Values (Address A2h, Byte 115)[a]** 

|**Code**|**Receiver Output Emphasis at Nominal Output Amplitude**|**Receiver Output Emphasis at Nominal Output Amplitude**|
|---|---|---|
||**Nominal**|**Unit**|
|1xxx|Vendor Specific||
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
|123-126|Reserved|RO|0|Contents 00h.|
|127|Page Select|RW|0||
|128-129|Reserved|RO|0||
|130|TP1 to TP4 EWRAP Control|RW|0|<br>Bit 7:2: Unused.<br><br>Bit 1:0:<br>–<br>00: EWRAP disabled, Bleed to TP2 enabled (normal mode).<br>–<br>01: EWRAP enabled, Bleed to TP2 enabled.<br>–<br>10: EWRAP enabled, Bleed to TP2 disable.<br>–<br>11: EWRAP enabled, Bleed to TP2 enabled.|
|131-132|Reserved|RW|0||
|133|TP3 to TP2 OWRAP Control|RW|0|<br>Bit 7:2: Unused.<br><br>Bit 1:0:<br>–<br>00: OWRAP disabled, Bleed to TP4 enabled (normal mode).<br>–<br>01: OWRAP enabled, Bleed to TP4 enabled.<br>–<br>10: OWRAP enabled, Bleed to TP4 disable.<br>–<br>11: OWRAP enabled, Bleed to TP4 enabled.|
|134|PRBS Checker BER, MSB|RO|0|<br>Bit 15:10 = Exponent.<br><br>Bit 9:0 = Mantissa clear on read.|
|135|PRBS Checker BER, LSB|RO|0||



AFCT-57H5MZ-DS100 23 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 29:  SFP Signal Integrity Feature Configuration Bytes (2-Wire Address A2h) (Continued)** 

|**Byte**|**Name**|**R/W**|**Default**|**Description**|
|---|---|---|---|---|
|136|PRBS Generator Control|RW|0|<br>Bit 7:5:<br>–<br>000: N/A.<br>–<br>001: PRBS9/9Q.<br>–<br>010: PRBS11/11Q.<br>–<br>011: PRBS13/13Q.<br>–<br>100: PRBS23/23Q.<br>–<br>101: PRBS31/31Q.<br>–<br>110: PRBS49/49Q.<br>–<br>111: PRBS58/58Q.<br><br>Bit 4:3 = Don't care.<br><br>Bit 2: 0 = System side at TP1; 1 = Line side at TP3.<br><br>Bit 1: 0 = Disable checker; 1 = Enable checker.<br><br>Bit 0: 0 = Disable PRBS; 1 = Enable PRBS.|
|137|64G TX_PRE2|RW|0|Output FFE Pre2, Default(64G)= 0.|
|138|64G TX_PRE1|RW|0|Output FFE Pre1, Default(64G)= 0.|
|139|64G TX_MAIN|RW|75|Output FFE Main, Default(64G)= 117.|
|140|64G TX_POST1|RW|FB|Output FFE Post1, Default(64G)= –5.|
|141|64G TX_POST2|RW|0|Output FFE Post2, Default(64G)= 0.|
|142|64G TX_POST3|RW|0|Output FFE Post3, Default (64G) = 0.<br>The host write to byte 142 sets 64G FFE taps. To read back the tap<br>settings, the host needs to write 80h to byte 142, and taps read out<br>will bepopulated in bytes 137 to 142.|
|143|System 64G RX CTLE|RW|0|Input CTLE 64G.<br><br>Bit 7: Rx Bandwidth 0 = high, 1 = low.<br><br>Bit 6: Set this bit will trigger read back setting on bit 5:0 and<br>bandwidth on bit 7.<br><br>Bit 5:0: Estimated channel loss(0 to 31).|
|144-152|Reserved|RW|0|Contents 00h.|
|153|TX CDR Status (TP1 System<br>Side)|RO|0|TX CDR Status (TP1 System Side)<br><br>Bit 7:5: Unused.<br><br>Bit 4: 1 = PRBS pattern lock (only used for byte 136 PRBS).<br><br>Bit 3: 1 = CDR lock.<br><br>Bit 2: 1 = LOS.<br><br>Bit 1: PLL unlock sticky bit.<br>–<br>0 = PLL did not transition from locked to unlock.<br>–<br>1 = PLL transitioned from locked to unlock clear on read.<br><br>Bit 0: 0 = PLL unlocked; 1 = PLL lock.|
|154|RX CDR Status (TP3 Line Side)|RO|0|RX CDR Status (TP3 Line Side)<br><br>Bit 7:5: Unused.<br><br>Bit 4: 1 = PRBS pattern lock (only used for byte 136 PRBS).<br><br>Bit 3: 1 = CDR lock.<br><br>Bit 2: 1 = LOS.<br><br>Bit 1: PLL unlock sticky bit.<br>–<br>0 = PLL did not transition from locked to unlock.<br>–<br>1 = PLL transitioned from locked to unlock clear on read.<br><br>Bit 0: 0 = PLL unlocked; 1 = PLL lock.|
|155|Reserved|RO|||



AFCT-57H5MZ-DS100 24 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

**Table 29:  SFP Signal Integrity Feature Configuration Bytes (2-Wire Address A2h) (Continued)** 

|**Byte**|**Name**|**R/W**|**Default**|**Description**|
|---|---|---|---|---|
|156|Power On Hours<br>MSB|RW||Units of hours. Byte 156 resides in nonvolatile memory (that is,<br>contents are retained during power cycle).|
|157|Power On Hours<br>LSB|RW||Units of hours. Byte 157 resides in nonvolatile memory (that is,<br>contents are retained during power cycle).|
|158|Reserved|RW|0|Contents 00h.|
|159|32G/16G TX_PRE2|RW|0|Output FFE Pre2, Default(32G/16G)= 0.|
|160|32G/16G TX_PRE1|RW|0|Output FFE Pre1, Default(32G/16G)= 0.|
|161|32G/16G TX_MAIN|RW|58|Output FFE Main, Default(32G/16G)= 88.|
|162|32G/16G TX_POST1|RW|FB|Output FFE Post1, Default(32G/16G)= –5.|
|163|32G/16G TX_POST2|RW|0|Output FFE Post2, Default(32G/16G)= 0.|
|164|32G/16G TX_POST3|RW|0|Output FFE Post3, Default (32G/16G) = 0.<br>The host write to byte 164 sets 32G/16G FFE taps. To read back the<br>tap settings, the host needs to write 80h to byte 142, and taps read out<br>will bepopulated in bytes 159 to 164.|
|165-241|Reserved|RW|0||
|242|Fast CDR adaptation<br>enable/disable|RW|0|<br>Bit 0 = 0: Enabled.<br><br>Bit 0 = 1: Disabled.|
|243|16G/32G pretrain status|RW||Bit 1:0 = 16G pretrain status; Bit 3:2 = 32G pretrain status.<br><br>0 = Not trained.<br><br>1 = Training is running.<br><br>2 = Training finished.<br><br>3 = Trainingfailed.|
|244|Reserved|RW|0|Contents 00h.|
|245|LSN Control|RW|0|LSN Control.<br><br>Bit 7:<br>–<br>1 = Enter LSN mode.<br>–<br>0 = Exit LSN mode.<br><br>Bit 6 = 1: Client RX adaptation reset.<br><br>Bit 5:3: Unused.<br><br>Bit 2:<br>–<br>0b = Fixed speed switch to 64G disable.<br>–<br>1b = Fixed speed switch to 64G enable.<br><br>Bit 1 = 1: Train 32G.<br><br>Bit 0 = 1: Train 16G.|
|246-255|Reserved|RW|||



AFCT-57H5MZ-DS100 25 

Broadcom 

64GFC for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310-nm, 64G/32G/16G, 10 km 

**AFCT-57H5MZ** Data Sheet 

## **Figure 12:  Module Label** 


**Figure 13:  Module Mechanical Drawing** 


AFCT-57H5MZ-DS100 26 

Broadcom 

Copyright © 2023 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

