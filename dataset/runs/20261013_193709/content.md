## **Data Sheet** 

## **AFBR-52H5PZ 64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G** 


## **Description** 

The Broadcom[®] AFBR-52H5PZ optical transceiver supports high-speed serial links over multimode optical fiber at signaling rates up to 57.8 Gb/s PAM4 (the serial line rate of 64GFC). The product is compliant with SFP-DD MSA agreements for mechanical and low-speed electrical specifications. High-speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-7. 

## **Features** 

- Compliant to SFP-DD MSA Rev 4.2 

- Compliant to SFP-DD MIS Rev 2.0 

- SN connector optical interface conforming to SN-60092019 specifications 

- Compliant to RoHS 3 directives with 7c-I exemption 

- Broadcom’s high-performance 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) and PiN diode 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 75°C) 

The AFBR-52H5PZ is a multirate 850-nm transceiver that ensures compliance with FC-PI-7 64GFC, 32GFC, and 16GFC specifications. Per the requirements of 64GFC, internal clock and data recovery circuits (CDRs) are present on both electrical input and electrical output of this transceiver. These CDRs lock at 57.8 Gb/s PAM4, 28.05 Gb/s NRZ, and 14.025Gb/s NRZ (64GFC, 32GFC, and 16GFC) accomplished by using two Rate Select inputs and I[2] C to configure transmit and receive sides. 

Digital diagnostic monitoring information (DMI) is present in the AFBR-52H5PZ per the requirements of SFF-8472, providing real-time monitoring information of transceiver laser, receiver, and environment conditions over an SFF-8431 I[2] C interface. 

## **Related Products** 

- AFCT-57G5PZ: 1310-nm SFP for 32G/16G/8G Fibre Channel 

- AFBR-57G5PZ: 850-nm SFP for 32G/16G/8G Fibre Channel 

- AFBR-57F5PZ: 850-nm SFP for 16G/8G/4G Fibre Channel 

- AFCT-57F5APZ: 1310-nm SFP for 16G/8G/4G Fibre Channel 

- Diagnostic features per SFF-8472 "Diagnostic Monitoring Interface for Optical Transceivers" 

- Enhanced operational features including EWRAP, OWRAP, and adaptive electrical EQ/emphasis settings 

- Integrated PRBS generator and bit error rate checker 

- Real-time monitoring of the following: 

   - Transmitter average optical power 

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

AFBR-52H5PZ-DS100 February 8, 2023 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

## **Transceiver Block Diagram** 

**Figure 1:  Block Diagram** 


## **Transmitter Section** 

The transmitter section includes a transmitter optical sub-assembly (TOSA), laser driver circuit, and a digital signal processor (DSP) with input adaptive equalization. The TOSA contains a Broadcom 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) light source with an integral light monitoring function and imaging optics to assure efficient optical coupling to the SN connector interface. The TOSA is driven by a laser driver circuit, which uses the differential output from the DSP to modulate and regulate VCSEL optical power. As mandated by FC-PI-7, the integral TX DSP cleans up any incoming jitter accumulated from the host ASIC, PCB traces, and SFP electrical connector. Between the SFP electrical connector and TX DSP is an adaptive equalization circuit to optimize SFP performance with nonideal incoming electrical waveforms at all rates. 

## **Receiver Section** 

The receiver section includes a receiver optical sub-assembly (ROSA), preamplification and post-amplification circuit, DSP circuit with variable emphasis controls, and an integral PRBS generator. The ROSA, containing a high-speed PIN detector, preamplifier, and imaging optics, efficiently couples light from the SN connector interface and performs an optical-toelectrical conversion. The resulting differential electrical signal passes through a post-amplification circuit and into the DSP for cleaning up accumulated jitter. The resulting signal is passed to a high-speed output line driver stage with variable, I[2] C controlled, emphasis settings allowing the host to optimize signal characteristics between the SFP and the host ASIC. 

## **Digital Diagnostics** 

The AFBR-52H5PZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in document SFF-8472. These features allow the host to access, via I[2] C, real-time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage, and laser operating current. 

AFBR-52H5PZ-DS100 2 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

## **Low-Speed Interfaces** 

Conventional low-speed interface I/Os are available as defined in document SFF-8431 to manage coarse and fine functions of the optical transceiver. On the transmit side, Tx_DISABLE and TxDisableDD inputs are provided for the host to turn on and off the outgoing optical signal. Rate select control hardware input pins and I[2] C controls are provided to configure both the transmitter and receiver stages for 64GFC, 32GFC, or 16GFC operation. A transmitter fault indicator outputs, Tx_FAULT and TxFAULTDD, are available for the SFP to signal a host of a transmitter operational problem. Received optical power loss of signal indicators, RX_LOS and RxLOSDD, are available to advise the host of a receiver operational problem. 

## **Special Operation Functions** 

**Figure 2:  OWRAP Functionality (I[2] C Controlled)** 

**Figure 3:  EWRAP Functionality (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT & PRE POST Rx VOUT &<br>AMP AMP Emphasis AMP AMP Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>Laser Laser EQ<br>Driver EQ Driver<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


Electrical and optical high-speed data _wrap_ functions are enabled to assist with local host or remote diagnostic and optimization sequences. Optical data wrap (OWRAP) takes a received optical signal through a CDR and retransmits it optically out. Electrical data wrap (EWRAP) takes an incoming electrical signal through a CDR and retransmits it electrically out. In OWRAP/EWRAP mode, the traffic pass-through can be turned on or off, controlled through I[2] C commands. 

**Figure 4:  SFP TX Input Electrical EQ Is Always Adaptive (No I[2] C Control Needed)** 

**Figure 5:  SFP RX Variable Output Electrical Emphasis (I[2] C Controlled))** 


**----- Start of picture text -----**<br>
PRE POST Rx VOUT & PRE POST Rx VOUT &<br>AMP AMP Emphasis AMP AMP Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>LaserDriver EQ LaserDriver EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


The electrical SFP input stage (TD +/–) has been enhanced with adaptive EQ, which optimizes the transceiver’s input equalization settings without host control. The SFP electrical output stage (RD+/–) has been enhanced with variable output emphasis features to allow host control and optimization of the receiver’s output settings. The host can then select, in situ, the most appropriate SFP setting for a given interconnect scenario. 

AFBR-52H5PZ-DS100 3 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Figure 6:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, Line Side (I[2] C Controlled)** 

**Figure 7:  Programmable PRBS Pattern Generator and Bit Error Rate Checker, System Side (I[2] C Controlled)** 


**----- Start of picture text -----**<br>
PRE POST PRBS Rx VOUT & PRE POST PRBS Rx VOUT &<br>AMP AMP BER Emphasis AMP AMP Gen Emphasis<br>ROSA ROSA<br>DSP uController DSP uController<br>TOSA TOSA<br>LaserDriver PRBSGen EQ LaserDriver PRBSBER EQ<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>r<br>o<br>t<br>c<br>e<br>n<br>n<br>o<br>C<br>P<br>F<br>S<br>**----- End of picture text -----**<br>


The SFP is equipped with an integrated PRBS generator that self-generates programmable PRBS patterns to either system side (TP4) or line side (TP2) at the speed (16G, 32G, or 64G) and operating mode (NRZ or PAM4) to which the SFP is set. The integrated bit error rate checker can also be enabled to measure bit error ratio for every 5 seconds (fixed). It enables users to know the optical link BER performance between TP2 and TP3 of the two separate SFPs or between the host ASIC transmitter (TP0) and the SFP TX input (TP1). 

**Table 1:  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to<br>the Electrical Contacts|JEDEC Human Body Model (HBM)<br>(JESD22-A114-B)|High-speed contacts withstand 1000V. All other<br>contacts withstand 2000V.|
|ESD to the Optical Connector<br>Receptacle|EN61000-4-2, Criterion B|When installed in a properly grounded housing and<br>chassis, the units are subjected to 15-kV air<br>discharges during operation and 8-kV direct<br>discharges to the case.|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022<br>(CISPR 22A)VCCI Class 1|System margins are dependent on customer board<br>and chassis design.|
|Immunity|Variation of IEC 61000-4-3|Typically shows no measurable effect from a 10-V/m<br>field step from 80 MHz to 1 GHz applied to the module<br>without a chassis enclosure.|
|Laser Eye Safety and Equipment<br>Type Testing|CLASS 1 LASER PRODUCT<br>Complies with 21 CFR 1040.10 except for<br>conformance with IEC 60825-1 Ed.3., as<br>described in Laser Notice No. 56, dated<br>May 8, 2019<br><br>(IEC) EN62368-1: 2014<br><br>(IEC) EN60825-1: 2014<br><br>(IEC) EN60825-2: 2004+A1+A2|CDRH Certification 9720151-205.|
|Component Recognition|Underwriters Laboratories (UL) and<br>Canadian Standards Association (CSA) Joint<br>Component Recognition for Information<br>Technology Equipment including Electrical<br>Business Equipment|UL File: E176896.|
|RoHS Compliance||With 7c-I exemption.|



AFBR-52H5PZ-DS100 4 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Figure 8:  Typical Application Configuration** 


**Figure 9:  Recommended Power Supply Filter** 


AFBR-52H5PZ-DS100 5 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

## **Table 2:  Pin Descriptions** 

|**Pin**|**Name**|**Function/Description**|**Plug**<br>**Sequencea**|**Notes**|
|---|---|---|---|---|
|0|Case|Module Case|||
|1|GND|Ground|1B|b|
|2|TX_FAULT|Module Fault Indication – High indicates a fault condition|3B||
|3|TX_DISABLE|Transmitter Disable for legacySFP channel|3B||
|4|SDA|Management I/F data line|3B||
|5|SCL|Management I/F clock|3B||
|6|MOD_ABS|Module Absent|3B||
|7|Speed1|RX Rate Select for legacySFP channel|3B||
|8|RX_LOS|RX Loss of Signal for legacySFP channel|3B||
|9|Speed2|TX Rate Select for legacySFP channel|3B||
|10|GND|Ground|1B|b|
|11|GND|Ground|1B|b|
|12|RD0-|Inverse Received Data Out for legacySFP+ channel|3B||
|13|RD0+|Received Data Out for legacySFP+ channel|3B||
|14|GND|Ground|1B|b|
|15|VccR|Receiver power|3B|c|
|16|VccT|Transmitter power|3B|c|
|17|GND|Ground|1B|b|
|18|TD0+|Transmit Data In for legacySFP channel|3B||
|19|TD0-|Inverse Transmit Data In for legacySFP channel|3B||
|20|GND|Ground|1B|b|
|21|GND|Ground|1A|b|
|22|IntL/TxFaultDD|Interrupt; optionally configured as TxFaultDD via TWI as described in the<br>SFP-DD MIS|3A||
|23|TxDisableDD|Transmitter Disable for DD channel|3A||
|24|ePPS|Precision Time Protocol (PTP) reference clock input|3A|d|
|25|LPMode|Low Power Mode control|3A||
|26|ResetL|Module Reset|3A||
|27|Speed1DD|RX Rate Select for DD channel|3A||
|28|RxLOSDD|Loss of Signal for DD channel|3A||
|29|Speed2DD|TX Rate Select for DD channel|3A||
|30|GND|Ground|1A|b|
|31|GND|Ground|1A|b|
|32|RD1-|Inverse Received Data Out for DD channel|3A||
|33|RD1+|Received Data Out for DD channel|3A||
|34|GND|Ground|1A|b|
|35|VccR1|Receiver power for DD channel|2A|c|
|36|VccT1|Transmitter power for DD channel|2A|c|
|37|GND|Ground|1A|b|



AFBR-52H5PZ-DS100 6 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Table 2:  Pin Descriptions (Continued)** 

|**Pin**|**Name**|**Function/Description**|**Plug**<br>**Sequencea**|**Notes**|
|---|---|---|---|---|
|38|TD1+|Transmit Data In for DD Channel|3A||
|39|TD1-|Inverse Transmit Data In for DD Channel|3A||
|40|GND|Ground|1A|b|



- a. Plug Sequence specifies the mating sequence of the host connector and module. The sequence is 1A, 2A, 3A, 1B, 2B, 3B. 

- b. SFP-DD uses common ground (GND) for all signals and supply (power). All are common within the SFP-DD module, and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal-common ground plane 

- c. VccR, VccT must be applied concurrently, and VccR1, VccT1 must be applied concurrently. VccR, VccT, VccR1, VccT1 are internally connected within the module. 

- d. The ePPS pins (if not used) may be terminated with 50Ω to ground on the host. 

Stress in excess of any of the individual absolute maximum ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently. Exposure to any of the absolute maximum ratings for extended periods can adversely affect reliability. 

**Table 3:  Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|
|Storage Temperature|Ts|–40|85|°C|a|
|Relative Humidity|RH|5|95|%||
|SupplyVoltage|Vcc|–0.5|3.63|V||
|Low Speed Input Voltage|Vi|–0.5|Vcc + 0.5, 3.63|V||



- a. Absolute maximum ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. Refer to the reliability data sheet for specific reliability performance. Between the absolute maximum ratings and the Recommended Operating Conditions, functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted. Optical and electrical characteristics are not defined for operation outside the recommended operating conditions, reliability is not implied, and damage to the module may occur for such operation over an extended period of time. 

**Table 4:  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|0|—|75|°C|a|
|SupplyVoltage|Vcc|3.135|3.3|3.465|V||
|Data Rate||14.025<br>14.025|—<br>—|28.9<br>57.8|GBd<br>Gb/s|b|
|Two-Wire Serial (TWS) Interface<br>Clock Rate||—|—|400|kHz|c|



- a. The position of case temperature measurement is shown in Figure 12. Continuous operation at the maximum recommended operating case temperature should be avoided to not degrade reliability. 

- b. 64GFC PAM4 requires FEC RS(544,514) encoding per FC-PI-7. 32GFC NRZ requires FEC RS(528,514) per FC-PI-6, and 16GFC NRZ does not require FEC per FC-PI-5. 

- c. With 500-µs maximum clock stretch per SFF-8419. 

AFBR-52H5PZ-DS100 7 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

The following transceiver electrical characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 5:  Transceiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Reference**|
|---|---|---|---|---|---|---|
|Transceiver Power Consumption||—|—|3.2|W||
|Power Supply Noise Rejection (peak-peak)|PSNR|—|—|66|mV|a|
|Low Speed Outputs<br>TX_FAULT, RX_LOS, MOD_SDA|VOL|–0.3|—|0.4|V|b|
||IOH|–50|—|37.5|μA||
|Low Speed Inputs<br>TX_DIS, MOD_SCL, MOD_SDA, RS(0), RS(1)|VIL|–0.3|—|0.8|V|c|
||VIH|2.0|—|VccT + 0.3|V||



a. Filter per the SFP specification is required on the host board to remove 10-Hz to 2-MHz content. 

b. Pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

- c. Mod_SCL and Mod_SDA must be pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to 3.3V. 

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

b. DC common-mode voltage is generated by the host. The specification includes the effects of ground offset voltage. 

**Table 7:  Stressed Input Test Conditions** 

|**Parameter**|**Value**|**Unit**|**Notes/Conditions**|
|---|---|---|---|
|Module Stressed Input Test<br>Eye Width at 10–5Probability EW5<br>Eye Height at 10–5Probability EH5<br>Vertical Eye Closure VEC(max.)|||a|
||0.23|UI||
||34|mV||
||12|dB||



a. Module stressed input tolerance is measured using the procedure defined in 83E.3.4.1.1. 

AFBR-52H5PZ-DS100 8 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Table 8:  Reference Points** 

|**Test Point**|**Description**|
|---|---|
|B’|Module electrical input at the input of the module compliance board. Module return loss specifications are met at this<br>point.|
|C’|Module electrical output at the output of the module compliance board. Module output and module return loss<br>specifications are met at thispoint.|



**Figure 10:  FC-PI-7 Module Compliance Points** 


The characteristics in Table 9 through Table 15 are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 9:  High-Speed Electrical Module Output Characteristics[a]** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|Differential Output Voltage (Enabled)|C’|—|—|900|mV|Measured with<br>PRBS13Q|
|Differential Output Voltage (Disabled)|C’|—|—|35|mV|Measured with<br>PRBS13Q|
|Common-Mode Noise, RMS|C’|—|—|17.5|mV||
|Differential Termination Mismatch|C’|—|—|10|%||
|Differential Output Return Loss SDD22<br>(min.)|C’|—|Eq. 1, Fig. 9|—|dB|FC-PI-7|
|Common to Differential Mode Conversion<br>SDC22, min.|C’|—|Eq 2, Fig. 10|—|dB|FC-PI-7|
|Source Transition Time(20% to 80%)|C’|9.5|—|—|ps||
|Common-Mode Voltage|C’|—|—|—|V|b|
|Vertical Eye Closure(VEC)|C’|—|—|12|dB||
|Near-End Eye Symmetry Mask Width<br>(ESMW)|C’|0.265|—|—|UI||
|Near-End Eye Height, Differential|C’|70|—|—|mV||
|Far-End ESMW|C’|—|0.2|—|UI||
|Far-End Eye Height, Differential|C’|30|—|—|mV||
|Far-End Pre-Cursor ISI Ratio|C’|–4.5|—|2.5|%||



- a. From FC-PI-7, Table 10. 

b. Referred to host ground. Common-mode voltage is generated by the host. 

AFBR-52H5PZ-DS100 9 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Table 10:  64GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|64GFC Signaling Rate|gamma-T|—|28.9|—|GBd|±100 ppm, PAM4 and<br>RS(544,514)FEC encoded|
|Center Wavelength Range|gamma-T|840|—|860|nm||
|RMS Spectral Widtha|gamma-T|—|—|0.60|nm||
|Transmitter and Dispersion Eye Closure for<br>PAM4(TDECQ)|gamma-T|—|—|5.5|dB||
|TDECQ 10log10(Ceq)|gamma-T|—|—|5.5|dB||
|Optical Modulation Amplitude (OMAouter)|gamma-T|–4.5b|—|+3.0|dBm||
|OMAouterExtinction Ratio|gamma-T|3|—|—|dB||
|Launch Power in OMAouterminus TDECQ|gamma-T|–5.9|—|—|dBm||
|Average Launch Power|gamma-T|–7.5|—|+4.0|dBm||
|RIN12OMA|gamma-T|—|—|–128|dB/Hz||
|Transmitter Transition Time, 20% to 80%|gamma-T|—|—|34|ps||
|Average Launch Power to OFF Transmitter|gamma-T|—|—|–30|dBm||
|Optical Return Loss Tolerance|gamma-T|—|—|12|dB||
|Encircled Fluxc|gamma-T|≥86% at 19 μm<br>≤30% at 4.5μm||||Type A1a.2 50-μm Fiber per<br>IEC 61280-1-4|



- a. RMS spectral width is the standard deviation of the spectrum. 

b. Even if the TDEC < 1.4 dB, the OMA (min.) must exceed this value. 

c. If measured into type A1a.2 50-μm fiber in accordance with IEC 61280-1-4. 

**Table 11:  64GFC Mode Optical Receiver Characteristics (per PC-PI-7)** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|Center Wavelength Range|gamma-R|840||860|nm||
|Damage Thresholda|gamma-R|+5.0|||dBm||
|Average Receive Powerb|gamma-R|–9.4||+4.0|dBm|BER 1.09E-4|
|Receive Power (OMAouter)|gamma-R|||+3.0|dBm|BER 1.09E-4|
|Receiver Return Loss|gamma-R|12|||dB||
|Receiver Sensitivity (OMAouter)|gamma-R|||–7.0|dBm|BER 1.09E-4|
|Stressed Receiver Sensitivity (OMAouter)c|gamma-R|||–2.4|dBm|BER 1.09E-4|
|Conditions of Stressed Receiver SensitivityTestd|gamma-R||||||
|Stressed Eye Closure for PAM4(SECQ)|gamma-R|||5.5|dB|BER 1.09E-4|
|SECQ-10log10(Ceq),|gamma-R|||5.5|dB|BER 1.09E-4|
|LOS Assert|gamma-R|–30|||dBm avg||
|LOS Deassert|gamma-R|||–7|dBm avg||
|LOS Hysteresis|gamma-R|0.5|||dB||



- a. The receiver must be able to tolerate, without damage, continuous exposure to a modulated optical input signal having this power level on one lane. The receiver does not have to operate correctly at this input power 

- b. Average receive power, each lane (min.) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

c. Measured with conformance test signal at TP3 (refer to 802.3cd, section 138.8.10) for BER specified in 802.3cd, section 138.1.1. 

- d. These test conditions are for measuring stressed receiver sensitivity. They are not characteristics of the receiver. 

AFBR-52H5PZ-DS100 10 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Table 12:  32GFC Mode Optical Transmitter Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|32GFC Signaling Rate, Per Lane||—|28.05|—|GBd|±100 ppm NRZ, RS(528,514)<br>FEC encoded|
|Modulated Optical Output Power (OMA)<br>(Peak to Peak) 28.05 Gb/s|Tx,OMA|479<br>–3.2|—<br>—|—<br>—|μW<br>dBm||
|Average Optical Output Power 28.05 Gb/s|POUT|–6.2|—|2|dBm|b|
|Vertical Eye Closure Penalty, 28.05 Gb/s|VECP||—|3.13|dB||



- a. TC = 0°C to 75°C, VccT, VccR = 3.3V ± 5%. 

b. Max. POUT is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

**Table 13:  32GFC Mode Optical Receiver Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power, 28.05 Gb/s|PIN|—|—|+2|dBm,avg||
|Input Optical Modulation Amplitude, 28.05 Gb/s (Peak to Peak)<br>(Unstressed Sensitivity)|OMA|—<br>—|—<br>—|95<br>–10.2|μW<br>dBm|a, b|
|Stressed Receiver Sensitivity (OMA), 28.05 Gb/s||—<br>—|—<br>—|263<br>–5.8|μW<br>dBm|c|



a. Input Optical Modulation Amplitude (commonly known as sensitivity) requires a valid Fibre Channel encoded input. 

b. 32GFC (28.05 Gb/s) assumes an FEC encoded RS(528, 514) signal and allows a BER of 1E–6 for receiver and transmitter measurements. 

c. 28.05 Gb/s stressed received vertical eye closure penalty (ISI) minimum is 3.1 dB. 

**Table 14:  16GFC Mode Optical Transmitter Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|16GFC Signaling Rate, Per Lane|—||14.025|—|GBd|±100 ppm NRZ,<br>No FEC|
|Modulated Optical Output Power (OMA)<br>(Peak to Peak), 14.025 Gb/s|Tx,OMA|331<br>–4.8|—<br>—|—<br>—|μW<br>dBm||
|Average Optical Output Power|POUT|–7.8|—|—|dBm|a|
|Vertical Eye Closure Penalty, 14.025 Gb/s|VECP|—|—|2.56|dB||
|Transmitter Uncorrelated Jitter, 14.025 Gb/s|UJ|—|—|0.03|UI||



a. Max. POUT is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

**Table 15:  16GFC Mode Optical Receiver Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power|PIN|—|—|0|dBm,avg|Per FC-PI-5|
|Input Optical Modulation Amplitude, 14.025Gb/s<br>(Peak to Peak) (Unstressed Sensitivity)|OMA|—<br>—|—<br>—|89<br>–10.5|μW<br>dBm|a|
|Stressed Receiver Sensitivity (OMA), 14.025Gb/s||—<br>—|—<br>—|170<br>–7.7|μW<br>dBm|b|



a. Input Optical Modulation Amplitude (commonly known as sensitivity) requires a valid Fibre Channel encoded input and allows a BER of 1E–12. 

- b. 14.025 Gb/s stressed received vertical eye closure penalty (ISI) minimum is 2.5 dB for all fiber types. 

AFBR-52H5PZ-DS100 11 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

## **SFP-DD Speed Change Control** 

Refer to SFP-DD MIS Rev 2.0 specifications to change the SFP-DD speed. The following table identifies the supported applications advertised through the advertising registers. 

**Table 16:  Application Advertising Registers** 

|**A0 Address/**<br>**Page (Dec)**|**ApSel**<br>**Code**|**Name**|**Value (Hex)**|**Supported**<br>**Application**|
|---|---|---|---|---|
|86|0001b|Host Electrical Interface ID|0x27|16GFC<br>(power up<br>default)|
|87||Module Media Interface ID|0x15||
|88||Host Lane Count, Bits 7:4|0x11||
|||Media Lane Count, Bits 3:0|||
|89||Host Lane Assignment Options|0x03||
|169/01U||Media Lane Assignment Options|0x03||
|90|0010b|Host Electrical Interface ID|0x28|32GFC|
|91||Module Media Interface ID|0x16||
|92||Host Lane Count, Bits 7:4|0x11||
|||Media Lane Count, Bits 3:0|||
|93||Host Lane Assignment Options|0x03||
|170/01U||Media Lane Assignment Options|0x03||
|94|0011b|Host Electrical Interface ID|0x29|64GFC|
|95||Module Media Interface ID|0x17||
|96||Host Lane Count, Bits 7:4|0x11||
|||Media Lane Count, Bits 3:0|||
|97||Host Lane Assignment Options|0x03||
|171/01U||Media Lane Assignment Options|0x03||



The following examples show the steps to change the speed through staged control set 0. 

**Example 1** . To change data path 0 (channel 0) speed to 16G: 

1. Set page to 01h: I[2] C W 7Fh 01h. 

2. Set application select control: I[2] C W EEh 11h (for FC16, FC32 = 21h, FC64 = 31h). 

3. Set staged set 0 apply control: I[2] C W EDh 01h. 

**Example 2** . To change data path 1 speed to 16G: 

1. Set page to 01h: I[2] C W 7Fh 01h. 

2. Set application select control: I[2] C W EFh 13h (for FC16, FC32 = 23h, FC64 = 33h). 

3. Set staged set 0 apply control: I[2] C W EDh 02h. 

**Example 3** . To set data path 0 to FC32 speed and data path 1 to FC64 speed: 

1. Set page to 01h: I[2] C W 7Fh 01h. 

2. Set application select control: I[2] C W EEh 21h (data path 0 speed FC32). 

3. Set application select control: I[2] C W EFh 33h (data path 1 speed FC64). 

4. Set staged set 0 apply control: I[2] C W EDh 03h. 

AFBR-52H5PZ-DS100 12 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Example 4** . To check if the data path is set up correctly, check the following bytes: 

1. Configuration error report on byte 74d. 

2. Active control set on byte 75d (data path 0) and 76d (data path 1). 

**NOTE:** Examples 1 through 4 use staged control set 0 apply immediate (A0U01h byte EDh bits 1:0). You can also use staged control set 0 apply init (A0U01h byte EDh bits 5:4). Staged control set 1 is available for use as well. 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 17:  Timing for Soft Control and Status Functions** 

|**Parameters**|**Symbol**|**Min.**|**Max.**|**Unit**|**Conditions**|
|---|---|---|---|---|---|
|Module Initialization Time|t_init|—|4|s|Time from module power onauntil the<br>configuration of the datapath is completed.|
|MgmtInitDuration|Max MgmtInit<br>Duration|—|2000|ms|Time from power onato hot plug or rising edge of<br>reset until completion of the MgmtInit state.|
|ResetL Assert Time|t_reset_init|10|—|µs|Minimum pulse time on the ResetL signal to initiate<br>a module reset.|
|IntL Assert Time|ton_IntL|—|200|ms|Time from the occurrence of condition triggering<br>IntL until Vout:IntL = Vol.|
|IntL Deassert Time|toff_IntL|—|500|µs|Time from the clear on readboperation of the<br>associated flag until Vout:IntL = Voh. This includes<br>deassert times for RX LOS, TXFault, and other flag<br>bits.|
|RX LOS Assert Time|ton_los|—|200|ms|Time from RX LOS conditioncpresent to RX LOS<br>bit set (value = 1b), LOS signal asserted, and IntL<br>asserted.|
|TXFault Assert Time|ton_TxFault|—|600|ms|Time from TXFault state to TXFault bit set (value =<br>1b)and IntL asserted.|
|Flag Assert Time|ton_flag|—|200|ms|Time from the occurrence of condition triggering<br>flag to the associated flag bit set (value = 1b) and<br>IntL asserted.|
|Mask Assert Time|ton_mask|—|100|ms|Time from mask bit set (value = 1b)duntil the<br>associated IntL assertion is inhibited.|
|Mask Deassert Time|toff_mask|—|100|ms|Time from mask bit cleared (value = 0b)duntil<br>associated IntL operation resumes.|
|DataPathDeinit Max. Duration|0101b|100|500|ms||
|DataPathInit Max. Duration|0111b|1|5|s||
|ModulePwrDn Max. Duration|0100b|50|100|ms||
|ModulePwrUpMax. Duration|0111b|1|5|s||
|Data Path TX Turn Off Max. Duration|0110b|500|1000|ms||
|Data Path TX Turn On Max. Duration|0110b|500|1000|ms||



a. Power on is defined as the instant when supply voltages reach and remain at or above the minimum level specified in Table 8 of SFP-DD Hardware Rev 4.2 specifications. 

b. Measured from low to high SDA edge of the Stop condition of the read transaction. 

c. RX LOS condition is defined at the optical input by the relevant standard. 

d. Measured from low to high SDA edge of the Stop condition of the write transaction. 

AFBR-52H5PZ-DS100 13 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Table 18:  I/O Timing for Squelch and Disable** 

|**Parameters**|**Symbol**|**Max.**|**Unit**|**Conditions**|
|---|---|---|---|---|
|RX Squelch Assert Time|ton_Rxsq|100|ms|Time from loss of RX input signal until the<br>squelched output condition is reached.|
|RX Squelch Deassert Time|toff_Rxsq|10|s|Time from resumption of RX input signals until the<br>normal RX output condition is reached.|
|TX Squelch Assert Time|ton_Txsq|400|ms|Time from loss of TX input signal until the<br>squelched output condition is reached.|
|TX Squelch Deassert Time|toff_Txsq|10|s|Time from the resumption of TX input signals until<br>the normal TX output condition is reached.|
|TX Disable Assert Time|ton_txdis|100|ms|Time from the stop condition of the TX Disable<br>write sequence 1 until optical output falls below<br>10% of nominal.|
|TX Disable Deassert Time|toff_txdis|400|ms|Time from TX Disable bit cleared (value = 0b)auntil<br>the optical output rises above 90% of nominal.|
|RX Output Disable Assert Time|ton_rxdis|100|ms|Time from RX Output Disable bit set (value = 1b)a<br>until RX output falls below 10% of nominal.|
|RX Output Disable Deassert Time|toff_rxdis|100|ms|Time from RX Output Disable bit cleared (value =<br>0b)1 until RX output rises above 90% of nominal.|



- a. Measured from low to high SDA signal transition of the Stop condition of the write transaction. 

**Table 19:  Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics[a]** 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature<br>Accuracy|TINT|±5.0|°C|Temperature is measured internal to the<br>transceiver. Valid from = 0°C to 75°C case<br>temperature.|
|Transceiver Internal Supply Voltage<br>Accuracy|VINT|±0.1|V|Supply voltage is measured internal to the<br>transceiver and can, with less accuracy, be<br>correlated to voltage at the SFP Vcc pin. Valid<br>over 3.3V ± 5%.|
|Transmitter Laser DC Bias Current<br>Accuracy|IINT|±10|%|IINTis better than ±10% of the nominal value.|
|Transmitted Average Optical Output<br>Power Accuracy|PT|±3.0|dB|Coupled into 50-μm multimode fiber. Valid from<br>–7.5 dBm to +4.0 dBm avg.|
|Received Optical Input Power Accuracy|PR|±3.0|dB|Coupled from 50um multimode fiber. Valid from<br>–9.4 dBm to +4.0 dBm avg.|



a. TC = 0°C to 75°C, VccT, VccR = 3.3V ± 5%. 

AFBR-52H5PZ-DS100 14 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

**Figure 11:  Module Label** 


**Figure 12:  Module Mechanical Drawing** 


AFBR-52H5PZ-DS100 15 

Broadcom 

**AFBR-52H5PZ** Data Sheet 

64GFC SFP-DD Digital Diagnostic SFP, 850-nm, 2x64G/32G/16G 

## **Memory Map** 

The memory is structured as a single-address, multiple-page approach. The 7-bit device address on the two-wire interface is 1010000b. Figure 13 shows the structure of the memory. The memory space is arranged into a lower, single-page address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, for example, Interrupt Flags and Monitors. Less time-critical entries, for example, serial ID information and threshold settings, are available with the Page Select function. For a more detailed description of the SFP-DD memory map, see the SFP-DD MIS Rev 2.0 Specification. 

## **Figure 13:  Memory Structure** 


**----- Start of picture text -----**<br>
Lower Page<br>00h<br>Module<br>Dynamic<br>Information<br>(VRs)<br>7Eh<br>7Fh Page Select<br>Page 00h Page 01h Page 03h Bank 0 Bank 0 Bank 0 Bank 0 Bank 0<br>80h Revision Page 13h Page 14h Page B0h Page B1h Page B2h<br>Codes, User<br>System ID, Advertising, EEPROM<br>Advertising Monitor (NVRs) Diagnostic Diagnostic Custom Custom Custom<br>(NVRs) Thresholds, Advertising Status and  Status and Status and Status and<br>Channel and control counters control control control<br>FFh Controls<br>**----- End of picture text -----**<br>


AFBR-52H5PZ-DS100 16 

Broadcom 

Copyright © 2023 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

