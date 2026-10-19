**Data Sheet** 


## **AFBR-735SMZ** 

**25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver** 

## **Description** 

The Broadcom[®] AFBR-735SMZ optical transceiver supports high-speed serial links over multi-mode optical fiber at 25.78 Gb/s (the serial line rate of 25GbE). The product is compliant with Small Form Pluggable industry agreements SFP and SFP28 for mechanical and low-speed electrical specifications. High-speed electrical and optical specifications are compliant with IEEE 802.3 for 25GBASE-SR and 10GBASE-SR. 

The AFBR-735SMZ is a 850-nm transceiver that ensures compliance with 25GBASE-SR specifications. Per the requirements of 25GbE, internal clock and data recovery (CDR) circuits are present on both electrical input and electrical output of this transceiver. These CDRs lock at 25.78 Gb/s but must be bypassed for 10GBASE-SR operation using two Rate Select inputs. 

Digital diagnostic monitoring information (DMI) is present in the AFBR-735SMZ per the requirements of SFF-8472, providing real-time monitoring information of transceiver laser, receiver, and environment conditions over an SFF-8419 two-wire serial interface. 

## **Related Products** 

- AFBR-89CDDZ: 850-nm QSFP28 for 100GBASE-SR4 

- AFBR-79EQDZ: 850-nm QSFP+ for 40GBASE-SR4, 100m 

- AFBR-79E3PZ: 850-nm QSFP+ for 40GBASE-SR4, 300m 

## **Features** 

- Compliant to RoHS directives 

- 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 70°C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10A) 

- Diagnostic features per SFF-8472 “Diagnostic Monitoring Interface for Optical Transceivers” 

- Enhanced operational features including variable electrical EQ/emphasis settings 

- Real-time monitoring of the following: – Transmitter average optical power 

   - Received average optical power 

   - Laser bias current 

   - Temperature 

   - Supply voltage 

- SFP28 mechanical specifications per SFF-8432 

- SFP28 compliant low-speed interface per SFF-8419 

- 25GBASE-SR and 10GBASE-SR compliant optical link distances 

## **Applications** 

   - Ethernet switches (director, stand-alone, blade) 

   - Ethernet NIC cards and adapters 

   - Port side connections 

   - Inter-switch or inter-chassis aggregated links 

- AFBR-709ISMZ: 850-nm SFP+ for 10GBASE-SR/SW, –40°C/85°C 

- AFBR-709SMZ: 850-nm SFP+ for 10GBASE-SR/SW, 0°C/70°C 

- AFCT-709SM: 1310-nm SFP+ for 10GBASE-LR, 0°C/ 70°C 

AFBR-735SMZ-DS100 June 7, 2021 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

## **Transmitter Section** 

The transmitter section includes a Transmitter Optical Sub-Assembly (TOSA), laser driver circuit, CDR circuit, and an electrical input stage with variable equalization controls. The TOSA contains a 850-nm VCSEL light source with integral light monitoring function and imaging optics to ensure efficient optical coupling to the LC connector interface. The TOSA is driven by a laser driver IC, which uses the differential output from an integral Tx CDR stage to modulate and regulate VCSEL optical power. As mandated by IEEE 802.3, the integral CDR cleans up any incoming jitter accumulated from the host ASIC, PCB traces, and SFP electrical connector. Between the SFP electrical connector and Tx CDR is a variable, two-wire serial controlled, equalization circuit to optimize SFP performance with nonideal incoming electrical waveforms. 

## **Receiver Section** 

The receiver section includes a Receiver Optical Sub-Assembly (ROSA), pre-amplification and post-amplification circuit, CDR circuit, and an electrical output stage with variable emphasis controls. The ROSA, containing a high-speed PIN detector, pre-amplifier, and imaging optics efficiently couple light from the LC connector interface and perform an optical-to-electrical conversion. The resulting differential electrical signal passes through a 

post-amplification circuit and into a CDR circuit for cleaning up accumulated jitter. 

Note the Tx and Rx CDR is engaged with TX/RX Rate Select = high (25GbE) and disengaged (bypassed) with RATE Select = low (other data rates, such as 10GbE). 

## **Digital Diagnostics** 

The AFBR-735SMZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in document SFF-472. These features allow the host to access, using two-wire serial, real-time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage, and laser operating current. 

## **Low-Speed Interfaces** 

Conventional low-speed interface I/Os are available as defined in SFF-8419 to manage coarse and fine functions of the optical transceiver. On the transmit side, a Tx_DISABLE input is provided for the host to turn on and off the outgoing optical signal. A transmitter fault indicator output, Tx_FAULT, is available for the SFP to signal a host of a transmitter operational problem. A received optical power loss of signal indicator, RX_LOS, is available to advise the host of a receiver operational problem, such as a low optical input condition. 

**Figure 1:  Transceiver Functional Diagram** 


AFBR-735SMZ-DS100 2 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

## **Rate Select Control** 

RX and TX rates can be independently controlled by either hardware input pins or using register writes. Module electrical input pins 7 and 9 are used to select RX and TX rates, respectively. Status of each logic level is reflected to register byte 110 bit 4 and 5 on address A2h as shown in Figure 2. RX and TX rates can also be controlled by register writes to byte 110 bit 3 and 118 bit 3. The power-on default of these bits is logic low. Hardware and software control inputs are ORed to allow flexible control. 

## **Figure 2:  Rate Select Control Flow RS0 RX Rate Select Control Flow** 

## **RS1 TX Rate Select Control Flow** 


**----- Start of picture text -----**<br>
Hardware Software Hardware Software<br>Input Input Input Input<br>RS0 (PIN7) Voltage A2h, byte 110 RS1 (PIN9) Voltage A2h, byte 118<br>"1"...V>2.0 Bit 3 "1"...V>2.0 Bit 3<br>"0"...V<0.8 "0"...V<0.8<br>A2h, byte 110 A2h, byte 110<br>Bit 4 OR Bit 5 OR<br>RX Rate TX Rate<br>Control Control<br>**----- End of picture text -----**<br>


**Table 1:  Rate Control Input** 

|**RS0 Control Input**|**RS0 Control Input**|**RX Operation**|**RX Operation**||**RS1 Control Input**|**RS1 Control Input**|**TX Operation**|**TX Operation**|
|---|---|---|---|---|---|---|---|---|
|**Hardware**<br>**Pin 7**|**A2h Byte**<br>**110 Bit 3**||||**Hardware**<br>**Pin 9**|**A2h Byte**<br>**118 Bit 3**|||
|**0a**|**0a**|**10Ga**|**RX CDR bypasseda**||**0a**|**0a**|**10Ga**|**TX CDR bypasseda**|
|0|1|25G|RX CDR enabled||0|1|25G|TX CDR enabled|
|1|0|25G|||1|0|25G||
|1|1|25G|||1|1|25G||



a. Factory default condition per MSA SFF-8472 is 10G mode. Module software rate select registers set to 0 and hardware pins 7, 9 are internally pulled to GND using 40 kΩ. **The host board must actively change hardware, software, or both logic levels for 25G operation.** 

AFBR-735SMZ-DS100 3 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 2:  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to the<br>Electrical Contacts|JEDEC Human Body Model (HBM)<br>(JESD22-A114- B)|High speed contacts shall withstand 1000V.<br>All other contacts shall withstand 2000V.|
|Electrostatic Discharge (ESD) to the<br>Optical Connector Receptacle|EN61000-4-2, Criterion B|When installed in a properly grounded<br>housing and chassis the units are subjected<br>to 15-kV air discharges during operation and<br>8-kV direct discharges to the case.|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022 (CISPR 22A)<br>VCCI Class 1|System margins are dependent on customer<br>board and chassis design.|
|Immunity|Variation of IEC 61000-4-3|Typically shows no measurable effect from a<br>10-V/m field set from 80 MHz to 1 GHz<br>applied to the module without a chassis<br>enclosure|
|Laser Eye Safety and Equipment Type<br>Testing|US FDA CDRH AEL Class 1<br>US21 CFP, Subchapter J per Paragraphs<br>1002.10 and 1002.12<br>(IEC) EN60825-1:1994 +A11 +A2<br>(IEC) EN60825-2:1994 +A1<br>(IEC) EN60950:1992 +A1 +A2 +A3 +A4 +A11|CDRH Certification 9720151-155 TUV File:<br>R72121699|
|Component Recognition|Underwriters Laboratories (UL) and Canadian<br>Standards Association (CSA) Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment|UL File: E173874|
|RoHS Compliance||Less than 1000 ppm of cadmium, lead,<br>mercury, hexavalent chromium,<br>polybrominated biphenyls (PPBs) and<br>polybrominated biphenyl ethers(PBDEs).|



AFBR-735SMZ-DS100 4 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Figure 3:  Typical Application Configuration** 


**Figure 4:  Recommended Power Supply Filter** 


**NOTE: INDUCTORS MUST HAVE LESS THAN 0.5� SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.** 

AFBR-735SMZ-DS100 5 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

## **Table 3:  Pin Description** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground||
|2|TX_FAULT|Transmitter Fault Indication – High indicates a fault condition|a|
|3|TX_DISABLE|Transmitter Disable – Module optical output disables on high or open|b|
|4|MOD_SDA|Module Definition 2 – Two-wire serial ID interface data line (SDA)|c|
|5|MOD_SCL|Module Definition 1 – Two wire serial ID interface clock line (SCL)|c|
|6|MOD_ABS|Module Definition 0 – Grounded in module (module present indicator)|c|
|7|Rx Rate Select, RS(0)|0 for 10GbE, 1 for 25GbE operation|d|
|8|RX_LOS|Loss of Signal – High indicates loss of received optical signal|e|
|9|Tx Rate Select, RS(1)|0 for 10GbE, 1 for 25GbE operation|d|
|10|VeeR|Receiver Ground||
|11|VeeR|Receiver Ground||
|12|RD–|Inverse Received Data Out|f|
|13|RD+|Received Data Out|f|
|14|VeeR|Receiver Ground||
|15|VccR|Receiver Power + 3.3V|g|
|16|VccT|Transmitter Power + 3.3V|g|
|17|VeeT|Transmitter Ground||
|18|TD+|Transmitter Data In|h|
|19|TD–|Inverse Transmitter Data In|h|
|20|VeeT|Transmitter Ground||



- a. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. When high, this output indicates a laser fault of some kind. Low indicates normal operation. In the low state, the output will be pulled to < 0.8V. 

- b. TX_DISABLE is an input that shuts down the transmitter optical output. It is internally pulled up (within the transceiver) with a 5.6-kΩ resistor. Low (0V to 0.8V): Transmitter on Between (0.8V and 2.0V): Undefined High (2.0 to Vcc max.) or OPEN: Transmitter Disabled 

- c. The signals Mod_ABS, SCL, SDA designate the two wire-serial interface pins. They must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. 

Mod_ABS is grounded by the module to indicate the module is present. Mod_SCL is serial clock line (SCL) of two-wire serial interface. Mod_SDA is serial data line (SDA) of two-wire serial interface. 

- d. Rate select input is used to control CDR. It is internally pulled down with a 40-kΩ resistor. See Table 4. 

- e. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. When high, this output indicates the received optical power is below the worst case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to < 0.8V. 

- f. RD–/+ designate the differential receiver outputs. They are AC coupled 100Ω differential lines that should be terminated with 100Ω differential at the host SerDes input. AC coupling is done inside the transceiver and is not required on the host board. The voltage swing on these lines is between 50 mV and 900 mV differential (25-mV to 450-mV single-ended) when properly terminated. 

- g. VccR and VccT are the receiver and transmitter power supplies. Refer to SFF-8419 for the details. 

- h. TD–/+ designate the differential transmitter inputs. They are AC coupled differential lines with 100Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. The inputs accept differential swings of 40 mV to 1200 mV (20-mV to 600-mV single-ended), although use values between 50 mV and 900 mV differential (25-mV and 450-mV single-ended) for best EMI performance. 

AFBR-735SMZ-DS100 6 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 4:  Rate Select Control** 

|**Table 4:  Rate Select Control**|**Table 4:  Rate Select Control**||||||
|---|---|---|---|---|---|---|
|**RS(0) RX Rate Select Control**||**RX CDR Operation**||**RS(1) TX Rate Select Control**||**TX CDR Operation**|
|**Hardware**<br>**Pin 7**|**Software A2h**<br>**Byte 110 Bit 3**|||**Hardware**<br>**Pin 9**|**Software A2h**<br>**Byte 118 Bit 3**||
|0|0|RX CDR Bypassed, 10GbE||0|0|TX CDR Bypassed, 10GbE|
|0|1|RX CDR On, 25GbE||0|1|TX CDR On, 25GbE|
|1|0|||1|0||
|1|1|||1|1||



Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently. Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. 

**Table 5:  Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|85|°C|a|
|Case Operating Temperature|TC|–40|85|°C||
|Relative Humidity|RH|5|95|%||
|Supply Voltage|VCC|–0.5|3.63|V||
|Low Speed Input Voltage|VI|–0.5|VCC+ 0.5, 3.63|V||



- a. Absolute Maximum Ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. Refer to the reliability data sheet for specific reliability performance. Between Absolute Maximum Ratings and the Recommended Operating Conditions functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted. Optical and electrical characteristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied and damage to the module may occur for such operation over an extended period of time. 

**Table 6:  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|0|—|70|°C|a|
|Supply Voltage|VCC|3.135|3.3|3.465|V||
|Data Rate||10.3125|—|25.78125|Gb/s|b|
|Two-Wire Serial (TWS) Interface Clock Rate||—|—|400|kHz|c|



- a. The position of case temperature measurement is shown in Figure 8. Continuous operation at the maximum recommended case operating temperature should be avoided not to degrade reliability. 

- b. 25GbE requires FEC RS(528,514) encoding per IEEE 802.3. 

- c. With 500-µs clock stretch per SFF-8419. 

AFBR-735SMZ-DS100 7 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 7:  Transceiver Electrical Characteristics** 

|**Parameter**|**Symbols**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Transceiver Power Consumption||—|—|1.0|W||
|Transceiver Power SupplyCurrent||—|—|319|mA||
|Power Supply Noise Rejection (peak-peak)|PSNR|—|—|66|mV|a|
|TX_FAULT, RX_LOS|IOH|–50|—|37.5|µA|b|
||VOL|–0.3|—|0.4|V||
|TX_DIS, RS(0), RS(1)|VIH|2.0|—|VCC+ 0.3|V||
||VIL|–0.3|—|0.8|V||
|MOD_SCL, MOD_SDA|VOH|VCC_Host – 0.5|—|VCC_Host + 0.3|V|c|
||VOL|0.0|—|0.4|V||
||VIH|VCCT × 0.7|—|VCCT + 0.5|V||
||VIL|–0.3|—|VCCT × 0.3|V||



- a. Filter per SFP specification is required on the host board to remove 10-Hz to 2-MHz content. 

- b. Measured with a 4.7-kΩ load pulled up to the host board to 3.3V. 

- c. Mod_SCL and Mod_SDA must be pulled up externally with a 4.7-kΩ to10-kΩ resistor on the host board to host VCC (3.14 < VCC_Hst < 3.46V). 

From 25G AUI C2M Clause 109B. The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 8:  High-Speed Electrical Module Input Characteristics** 

|**Parameter**|**Test Point**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate|TP1|—|25.78125|—|Gbaud|± 100ppm|
|Differential Pk-Pk Input Voltage Tolerance|TP1a|900|—|—|mV||
|Differential Input Return Loss, Min.|TP1|—|Eq83E-5|—|dB|IEEE 802.3bm|
|Common Mode to Differential Input Return<br>Loss, Min.|TP1|—|Eq 83E-6|—|dB|IEEE 802.3bm|
|Differential Termination Mismatch|TP1|—|—|10|%||
|Module Stressed Input Test|TP1a|—|83E.3.4.2|—||IEEE 802.3bm, below|
|Single-Ended Voltage Tolerance Range|TP1a|–0.4|—|3.3|V||
|DC Common Mode Output Voltage|TP1a|–0.350|—|2.85|V|Notea|
|LOS Hysteresis||0.5|—|4|dB|Noteb|
||||||||
|**Parameter**|**Value**||||**Units**|**Notes/Conditions**|
|Module Stressed Input Test|—|||||Notec|
|Eye Width|0.46||||UI||
|Applied Pk-Pk Sinusoidal Jitter|Table 88-13||||||
|Eye Height|95||||mV||



- a. DC common mode voltage generated by the host. The specification includes effects of ground offset voltage. 

- b. LOS hysteresis is defined as 20 × Log(LOS Deassert Level / LOS Assert Level). 

- c. Module stressed input tolerance is measured using the procedure defined in 83E.3.4.1.1. 

AFBR-735SMZ-DS100 8 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 9:  Reference Points** 

|**Test Point**|**Description**|
|---|---|
|TP0|Host ASIC transmitter output at the ASICpackagepin on a DUT board.|
|TP1|Input to the module compliance board through the mated module compliance board and the module connector. Used<br>to test module input.|
|TP1A|Host ASIC transmitter output across the host board and the host edge card connector at the output of the host<br>compliance board.|
|TP2|Optical transmitter output as measured at the end of a 2m to 5mpatch cord mated to the optical module.|
|TP3|Optical testpoint as measured at the end of an optical fiber cable; closestpoint to thepresumed optical receiver input.|
|TP4|Module output through the mated module and the host edge card connector through the module compliance board.|
|TP4A|Input to the host compliance board through the mated host compliance board and the host edge card connector. Used<br>to test host input.|
|TP5|Input to the host ASIC.|



**Figure 5:  IEEE 802.3bm CAUI-4 Compliance Points TP1a, TP4a** 


**Figure 83E–4—Host CAUI-4 Compliance Points** 

Note a reference receiver is used to measure host eye width and eye height at TP1a. The reference receiver includes a selectable continuous time linear equalizer (CTLE), which is described by Equation (83E-4) with coefficients given in Table 83E-2 – Reference CTLE Coefficients. 

## **Equation (83E-4)** 

_H(f) = (G × P1 × P2) / Z1_ 

where: 

_H(f)_ is the CTLE transfer function, _f_ is the frequency in GHz 

_G_ is the CTLE gain 

_P1_ , _P2_ are the CTLE poles in Grad/s 

_Z1_ is the CTLE zero in Grad/s 

AFBR-735SMZ-DS100 9 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 83E-2 – Reference CTLE Coefficients** 

|**Peaking (dB)**|**G**|**P1/2**|**P2/2**|**Z1/2**|
|---|---|---|---|---|
|1|0.89125|18.6|14.1|8.364|
|2|0.79433|18.6|14.1|7.099|
|3|0.70795|15.6|14.1|5.676|
|4|0.63096|15.6|14.1|4.9601|
|5|0.56234|15.6|14.1|4.358|
|6|0.50119|15.6|14.1|3.844|
|7|0.44668|15.6|14.1|3.399|
|8|0.39811|15.6|14.1|3.012|
|9|0.35481|15.6|14.1|2.672|



From 25G AUI C2M Clause 109B. The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 10:  High-Speed Electrical Module Output Characteristics** 

|**Parameter**|**TestPoint**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate|TP4|—|25.78125|—|Gbaud|± 100ppm|
|Common Mode AC Output Voltage, RMS|TP4|—|—|17.5|mV, rms||
|Differential Output Voltage|TP4|—|—|900|mV||
|Eye Width|TP4|0.57|—|—|UI||
|Eye Height, Differential|TP4|228|—|—|mV||
|Vertical Eye Closure|TP4|—|—|5.5|dB||
|Differential Output Return Loss, Min.|TP4|—|Eq83E-2|—|dB|IEEE 802.3bm|
|Common to Differential Mode Conversion, Min.|TP4|—|Eq83E-3|—|dB|IEEE 802.3bm|
|Differential Termination Mismatch|TP4|—|—|10|%||
|Transition Time(20% to 80%)|TP4|12|—|—|ps||
|DC Common Mode Voltage|TP4|–0.35|—|2.85|V|Notea|



a. DC common mode voltage is generated by the host. The specification includes effects of ground offset voltage. 

**Figure 6:  IEEE 802.3bm CAUI-4 Compliance Points TP1, TP4** 


**Figure 83E–5—Module CAUI-4 Compliance Points** 

AFBR-735SMZ-DS100 10 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

From 25GBASE-SR, 802.3by Clause 112. The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 11:  High-Speed Optical Transmitter Characteristics** 

|**Parameter**|**Test Point***|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate||—|25.78125|—|Gbaud|± 100ppm|
|Center Wavelength Range|TP2|840|—|860|nm||
|RMS Spectral Width|TP2|—|—|0.60|nm|Notea|
|Average Launch Oower|TP2|–8.4|—|+2.4|dBm||
|Optical Modulation Amplitude (OMA)|TP2|–6.4|—|+3.0|dBm|Noteb|
|Launch Power in OMA Minus TDEC|TP2|–7.3|—|—|dBm||
|Transmitter and Dispersion Eye Closure(TDEC)|TP2|—|—|4.3|dB||
|Average Launch Power of OFF Transmitter|TP2|—|—|–30|dBm||
|Extinction Ratio|TP2|2|—|—|dB||
|Optical Return Loss Tolerance|TP2|—|—|12|dB||
|Encircled Flux|TP2|≥ 86% at 19 µm<br>≤ 30% at 4.5µm||||Notec|
|Transmitter Eye Mask Definition:<br>{X1, X2, X3, Y1, Y2, Y3}|TP2|Specification Values<br>{0.3, 0.38, 0.45, 0.35, 0.41, 0.5}||||Hit ratio 1.5 × 10–3<br>hitsper sample|



a. RMS spectral width is the standard deviation of the spectrum. 

b. Even if the TDEC < 0.9 dB, the OMA (min.) must exceed this value. 

c. If measured into type A1a.2 50-µm fiber in accordance with IEC 61280-1-4. 

**Figure 7:  Transmitter Eye Mask Definitions** 


AFBR-735SMZ-DS100 11 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 12:  High-Speed Optical Transmitter Characteristics, TX Rate Select = Low** 

|**Parameter**|**Test Point***|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate||—|10.3125|—|Gbaud|± 100ppm|
|Laser OMA Output Power|TP2|–4.3|—|—|dBm|Notea|
|Laser Mean Output Power|TP2|—|—|0|dBm||
|Laser Off Power|TP2|—|—|–30|dBm||
|Extinction Ratio|TP2|3.0|—|—|dBm||
|Transmitter and Dispersion Penalty (TDP)|TP2|—|—|3.9|dB||
|Center Wavelength|TP2|840|—|860|nm|Notea|
|RMS Spectral Width, Standard Deviation|TP2|—|—|–30|dBm|Notea|
|RIN12OMA|TP2|3|—|–128|dB/Hz||
|Optical Return Loss Tolerance|TP2|—|—|12|dB||



a. Trade-offs are available among spectral width, center wavelength and minimum optical modulation amplitude per IEEE 802.3. 

From 25GBASE-SR, 802.3by Clause 112. The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 13:  High-Speed Optical Receiver Characteristics** 

|**Parameter**|**Test Point***|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate||—|25.78125|—|Gbaud|± 100ppm|
|Center Wavelength Range|TP3|840|—|860|nm||
|Damage Threshold|TP3|+3.4|—|—|dBm|Notea|
|Average Receive Power|TP3|–10.3|—|+2.4|dBm|Noteb|
|Receive Power(OMA)|TP3|—|—|+3,0|dBm||
|Receiver Reflectance|TP3|—|—|–12|dB||
|Stressed Receiver Sensitivity OMA|TP3|—|—|–5.2|dBm|Notec|
|Conditions of Stressed Receiver Sensitivity<br>Test||—|—|—||Noted|
|Stressed Eye Closure(SEC)||—|4.3|—|dB||
|Stressed Eye J2 Jitter||—|0.39|—|UI||
|Stressed Eye J4 Jitter||—|0.53|—|UI||
|Stressed Receiver Eye Mask Definition:<br>X1, X2, X3, Y1,Y2, Y3||Specification Values<br>{0.28, 0.50, 0.50, 0.33, 0.33, 0.40}||||Hit ratio 5 × 10–5hits<br>per sample|
||||||||
|**Parameter**|**Test Point***|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|LOS Assert|TP3|–30|—|—|dBm,avg||
|LOS De-Assert|TP3|—|—|–9.1|dBm,avg||
|LOS Hysteresis|TP3|0.5|—|—|dB||



a. The receiver is able to tolerate, without damage, continuous exposure to a modulated optical input signal having this power level. The receiver does not have to operate correctly at this input power. 

- b. Average receive power (min.) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

c. Measured with conformance test signal at TP3 (refer to IEEE 802.3bm Section 95.8.8) for BER specified in IEEE 802.3bm Section 95.1.1. 

d. These test conditions are for measuring stressed receiver sensitivity. They are not characteristics of the receiver. 

AFBR-735SMZ-DS100 12 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 14:  High-Speed Optical Receiver Characteristics, RX Rate Select = Low** 

|**Parameter**|**Test Point***|**Min.**|**Typ.**|**Max.**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|---|
|SignalingRate||—|10.3125|—|Gbaud|± 100ppm|
|Stressed Sensitivity (OMA)||—|—|–7.5|dBm||
|Receive Sensitivity (OMA)|TP3|—|—|–11.1|dBm||
|Receive Power Overload|TP3|–1.0|—|—|dBm||
|Receiver Reflectance|TP3|—|—|–12|dB||
|Center Wavelength|TP3|840|—|860|nm||
|RX_LOS Assert|TP3|–30|—|—|dBm,avg||
|RX_LOS Deassert|TP3|—|—|–9.1|dBm,avg||
|RX_LOS Hysteresis||0.5|—|—|dB||
|Verfical Eye Closure Penalty||3.5|—|—|dB||
|Stressed Eye Jitter||–0.3|—|—|UIp-p||



AFBR-735SMZ-DS100 13 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 15:  Transceiver Soft Diagnostic Timing Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Hardware TX_DISABLE Assert Time|t_off|—|10|µs|a|
|Hardware TX_DISABLE Negate Time|t_on|—|1|ms|b|
|Time to Initialize, Including Reset of TX_FAULT|t_init|—|300|ms|c|
|Hardware TX_FAULT Assert Time|t_fault|—|100|µs|d|
|Hardware TX_DISABLE to Reset|t_reset|10|—|µs|e|
|Hardware RX_LOS Deassert Time|t_loss_on|—|100|µs|f|
|Hardware RX_LOS Assert Time|t_loss_off|—|100|µs|g|
|Hardware RATE_SELECT Change Time|t_ratesel|—|10|µs||
|Software TX_DISABLE Assert Time|t_off_soft|—|100|ms|h|
|Software TX_DISABLE Negate Time|t_on_soft|—|100|ms|i|
|Software Tx_FAULT Assert Time|t_fault_soft|—|100|ms|j|
|Software Rx_LOS Assert Time|t_loss_on_soft|—|100|ms|k|
|Software Rx_LOS Deassert Time|t_loss_off_soft|—|100|ms|l|
|Serial Bus Diagnostic Data Ready|t_data|—|1000|ms|m|
|Serial Bus Hardware Ready|t_serial|—|300|ms|n|
|Serial Bus Buffer Time|t_buf|20|—|µs|o|
|Complete Single or Sequential Write Up to 4 Bytes|twR|—|40|ms|p|
|Complete Sequential Write of 5 to 8 Bytes|twR|—|80|ms||
|Serial Interface Clock Holdoff “Clock Stretching”|T_clock_hold|—|500|µs|q|
|Serial ID Clock Rate|f_serial_clock|—|400|kHz|r|



- a. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

- b. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

- c. Time from power on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

- d. From occurrence of fault to assertion of TX_FAULT. 

- e. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

- f. Time from loss of optical signal to Rx_LOS Assertion. 

- g. Time from valid optical signal to Rx_LOS Deassertion. 

- h. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

- i. Time from two-wire interface de-assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output rises above 90% of nominal. 

- j. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

- k. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

- l. Time for two-wire interface deassertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

- m. From power on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

- n. Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). 

- o. Time between START and STOP commands. 

- p. Time from stop bit to completion of a 1 to 8 byte write command. 

- q. Maximum time the SFP+ module may hold the SCL line low before continuing with a read or write operation. 

- r. With a maximum clock stretch of 500 µs. A maximum of100-kHz operation can be supported without a clock stretch. 

AFBR-735SMZ-DS100 

Broadcom 

14 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 16:  Transceiver Digital Diagnostic Monitor (Real-Time Sense) Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature<br>Accuracy|TINT|± 3.0|°C|Temperature is measured internal to the transceiver. Valid from =<br>0°C to 70 °C case temperature.|
|Transceiver Internal Supply Voltage<br>Accuracy|VINT|± 0.1|V|Supply voltage is measured internal to the transceiver and can, with<br>less accuracy, be correlated to voltage at the SFP Vcc pin. Valid<br>over 3.3V ± 5%.|
|Transmitter Laser DC Bias Current<br>Accuracy|IINT|± 10|%|IINTis better than ± 10% of the nominal value.|
|Transmitted Average Optical<br>Output Power Accuracy|PT|± 3.0|dB|Coupled into 50-µm multi-mode fiber. Valid from –8.4 dBm to<br>+2.4 dBm avg.|
|Received Optical Input Power<br>Accuracy|PR|± 3.0|dB|Coupled from 50-µm multi-mode fiber. Valid from –10.3 dBm to<br>+2.4 dBm avg.|



**Table 17:  EEPROM Serial ID Memory Contents – Address A0h** 

|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|
|---|---|---|---|---|---|
|0|03|SFP physical device|37|00|Hex Byte of Vendor OUIa|
|1|04|SFP function defined by serial ID only|38|17|Hex Byte of Vendor OUIa|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUIa|
|3|00||40|41|"A" – Vendor Part Number ASCII Character|
|4|00||41|46|"F" – Vendor Part Number ASCII Character|
|5|00||42|42|"B" – Vendor Part Number ASCII Character|
|6|00||43|52|"R" – Vendor Part Number ASCII Character|
|7|00||44|2D|"-" – Vendor Part Number ASCII Character|
|8|00||45|37|"7" – Vendor Part Number ASCII Character|
|9|00||46|33|"3" – Vendor Part Number ASCII Character|
|10|00||47|35|"5" – Vendor Part Number ASCII Character|
|11|07|256B/257B(transcoded FEC-enabled data)|48|53|"S" – Vendor Part Number ASCII Character|
|12|FF|Greater than 25.5 Gb/s(see Address 66)|49|4D|"M" – Vendor Part Number ASCII Character|
|13|00||50|5A|"Z" – Vendor Part Number ASCII Character|
|14|00||51|20|" " – Vendor Part Number ASCII Character|
|15|00||52|20|" " – Vendor Part Number ASCII Character|
|16|00||53|20|" " – Vendor Part Number ASCII Character|
|17|00||54|20|" " – Vendor Part Number ASCII Character|
|18|0A|100m of OM4 50/125-µm fiber at 25GbE|55|20|" " – Vendor Part Number ASCII Character|
|19|07|70m of OM3 50/125-µm fiber at 25GbE|56|20|" " – Vendor Revision ASCII Character|
|20|41|"A" – Vendor Name ASCII Character|57|20|" " – Vendor Revision ASCII Character|
|21|56|"V" – Vendor Name ASCII Character|58|20|" " – Vendor Revision ASCII Character|
|22|41|"A" – Vendor Name ASCII Character|59|20|" " – Vendor Revision ASCII Character|
|23|47|"G" – Vendor Name ASCII Character|60|03|Hex Byte of Laser Wavelengthb|
|24|4F|"O" – Vendor Name ASCII Character|61|52|Hex Byte of Laser Wavelengthb|
|25|20|" " – Vendor Name ASCII Character|62|00||



AFBR-735SMZ-DS100 15 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 17:  EEPROM Serial ID Memory Contents – Address A0h (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|
|---|---|---|---|---|---|
|26|20|" " – Vendor Name ASCII Character|63||Checksum for Bytes 0 to 62c|
|27|20|" " – Vendor Name ASCII Character|64|08|CDRspresent. 1Wpower class|
|28|20|" " – Vendor Name ASCII Character|65|3A|Hardware Tx_Disable, Tx_Fault, Rx_LOS,<br>Rate_Select|
|29|20|" " – Vendor Name ASCII Character|66|67|25.78 Gb/s nominal bit rate(25GbE)|
|30|20|" " – Vendor Name ASCII Character|67|00||
|31|20|" " – Vendor Name ASCII Character|68–83||Vendor Serial Number ASCII charactersd|
|32|20|" " – Vendor Name ASCII Character|84–91||Vendor Date Code ASCII characterse|
|33|20|" " – Vendor Name ASCII Character|92|68|Digital diagnostics, Internal Cal, Rx Pwr Avg|
|34|20|" " – Vendor Name ASCII Character|93|FA|Alarms/Warnings, Software Tx_Disable,<br>Tx-Fault, Rx_LOS, Rate_Select|
|35|20|" " – Vendor Name ASCII Character|94|08|SFF-8472 compliance to revision 12.2|
|36|02|25GBASE-SR|95||Checksum for Bytes 62 to 94c|
||||96–255|00||



a. The IEEE Organizationally Unique Identified OUI) assigned to Broadcom is 00-17-6A (3 bytes of hex). 

b. Laser wavelength is represented in 16 unsigned buts. The hex representation of 850 nm is 0352. 

c. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored prior to product shipment. 

d. Addresses 68–83 specify the AFBR-735SMZ ASCII serial number and vary on a per-unit basis. 

e. Addresses 84–91 specify the AFBR-735SMZ ASCII data code and vary on a per-date code basis. 

AFBR-735SMZ-DS100 16 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 18:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|0|TempH Alarm MSBa|26|Tx Power L Alarm MSBg|104|Real Time Rx Power MSBb|
|1|TempH Alarm LSBa|27|Tx Power L Alarm LSBg|105|Real Time Rx Power LSBb|
|2|TempL Alarm MSBa|28|Tx Power H WarningMSBg|106|Reserved|
|3|TempL Alarm LSBa|29|Tx Power H WarningLSBg|107|Reserved|
|4|TempH WarningMSBa|30|Tx Power L WarningMSBg|108|Reserved|
|5|TempH WarningLSBa|31|Tx Power L WarningLSBg|109|Reserved|
|6|TempL WarningMSBa|32|Rx Power H Alarm MSBb|110|Status/Control – SeeTable 19|
|7|TempL WarningLSBa|33|Rx Power H Alarm LSBb|111|Reserved|
|8|Vcc H Alarm MSBc|34|Rx Power L Alarm MSBb|112|Flag Bits – SeeTable 20|
|9|Vcc H Alarm LSBc|35|Rx Power L Alarm LSBb|113|Flag Bits – SeeTable 20|
|10|Vcc L Alarm MSBc|36|Rx Power H Warning MSBb|114|Tx Input EQ Control – See<br>Table 23,Table 24|
|11|Vcc L Alarm LSBc|37|Rx Power H Warning LSBb|115|Rx Output Emphasis Control –<br>SeeTable 25,Table 26|
|12|Vcc H WarningMSBc|38|Rx Power L WarningMSBb|116|Flag Bits – SeeTable 20|
|13|Vcc H WarningLSBc|39|Rx Power L WarningLSBb|117|Flag Bits – SeeTable 20|
|14|Vcc L WarningMSBc|40–55|Optional Alarm and Warning|118|Status/Control – SeeTable 21|
|15|Vcc L Warning LSBc|56–94|External Calibration Constantsd|119|CDR Loss of Lock Status –<br>SeeTable 22|
|16|Tx Bias H Alarm MSBe|95|Checksum for Bytes 0 to 94f|120–127|Reserved|
|17|Tx Bias H Alarm LSBe|96|Real Time Temperature MSBa|128–247|Customer Writable|
|18|Tx Bias L Alarm MSBe|97|Real Time Temperature LSBa|248–255|Vendor Specific|
|19|Tx Bias L Alarm LSBe|98|Real Time Vcc MSBc|||
|20|Tx Bias H WarningMSBe|99|Real Time Vcc LSBc|||
|21|Tx Bias H WarningLSBe|100|Real Time Tx Bias MSBe|||
|22|Tx Bias L WarningMSBe|101|Real Time Tx Bias LSBe|||
|23|Tx Bias L WarningLSBg|102|Real Time Tx Power MSBg|||
|24|Tx Power H Alarm MSBg|103|Real Time Tx Power LSBg|||
|25|Tx Power H Alarm LSBg|||||



a. Temperature (Temp) is decoded as a 16-bit signed two's complement integer in increments of 1/256°C. 

b. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

c. Supply voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 mV. 

d. Bytes 56–94 are not intended for use, but have been set to default values per SFF-8472. 

- e. Tx bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 µA. 

f. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment. 

g. Transmitted average optical power (Tx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

AFBR-735SMZ-DS100 17 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 19:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|a|
|6|Soft TX_DISABLE Control|Read/write bit for changing digital state of TX_DISABLE function|a, b|
|5|RS(1)State|Digital state of TX Rate_Select Input Pin(1 = RS(1)asserted)||
|4|RS(0)State|Digital state of RX Rate_Select Input Pin(1 = RS(0)asserted)||
|3|RS(0) RX_RATE_SELECT Control|Read/write bit for changing digital state of Rx Rate_Select RS(0)|c|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|a|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|a|
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready<br>(0 = Data Ready)||



a. The response time for soft commands of the AFBR-735SMZ is 100 ms as specified by MSA. 

b. Bit 6 is logic ORed with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter. 

c. Bit 3 is logic ORed with the SFP RS(0) RX Rate_Select input pin 7 …. either asserted will set receiver to Rate = High. The power-on default is logic zero/low. 

**Table 20:  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

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
||0–5|reserved||
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
||0–5|reserved||



AFBR-735SMZ-DS100 

Broadcom 

18 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 21:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4–7|Reserved|||
|3|RS(1) TX_RATE_SELECT Control|Read/write bit for changing digital state of Tx Rate_Select RS(1) function|a|
|2|Reserved|||
|1|Power Level State|Always set to zero. A value of zero indicates Power Level 1 operation<br>(1W max.).||
|0|Power Level Select|Unused. This device supportspower level zero(1W max.)only.||



a. Bit 3 is logic ORed with the SFP RS(1) TX Rate_Select input pin 9….either asserted will set transmitter to Rate = High. The power-on default is logic zero/low. 

**Table 22:  EEPROM Serial ID Memory Contents – CDR Loss of Lock (LOL) Status Indicators (Address A2h, Byte 119)** 

|**Bit Number**|**Status/Control Name**|**Description**|
|---|---|---|
|7–2|Reserved||
|1|Tx CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock.|
|0|Rx CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock.|



**Table 23:  EEPROM Serial ID Memory Contents – Transmitter Input Electrical Equalization Control (Address A2h, Byte 114)** 

|**Bit Number**|**Status/Control Name**|**Description**|
|---|---|---|
|7–4|TX EQ|Selects an input equalization valueper Table 9-13 of SFF-8472, RS1 = High|
|3–0|Reserved||



From Table 9-13 of SFF-8472. 

**Table 24:  Transmitter Input Equalization Control Values (Address A2h, Byte 114)** 

|**Code**|**Transmitter Input Equalization**|**Transmitter Input Equalization**|
|---|---|---|
||**Nominal**|**Units**|
|11xx|Reserved||
|1011|Reserved||
|1010|10|dB|
|1001|9|dB|
|1000|8|dB|
|0111|7|dB|
|0110|6|dB|
|0101|5|dB|
|0100|4|dB|
|0011|3|dB|
|0010|2|dB|
|0001|1|dB|
|0000|0|No Equalization|



AFBR-735SMZ-DS100 

Broadcom 

19 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

**Table 25:  EEPROM Serial ID Memory Contents – Receiver Output Electrical Emphasis Control (Address A2h, Byte 115)** 

|**Bit Number**|**Status/Control Name**|**Description**|
|---|---|---|
|7–4|RX EMPH|Selects an output emphasis valueper Table 9-14 of SFF-8472, RS0 = High|
|3–0|Reserved||



From Table 9-14 of SFF-8472. 

**Table 26:  Receiver Output Emphasis Control Values (Address A2h, Byte 115)** 

|**Code**|**Receiver Output Emphasis At Nominal Output Amplitude**|**Receiver Output Emphasis At Nominal Output Amplitude**|
|---|---|---|
||**Nominal**|**Units**|
|1xxx|Vendor Specific||
|0111|7|dB|
|0110|6|dB|
|0101|5|dB|
|0100|4|dB|
|0011|3|dB|
|0010|2|dB|
|0001|1|dB|
|0000|0|No Emphasis|



**Figure 8:  Module Drawing** 


AFBR-735SMZ-DS100 20 

Broadcom 

25GbE SFP28 for Multi-Mode Optical Fiber Digital Diagnostic SFP, 850-nm, Low Voltage (3.3V) 25GBASE-SR, 10GBASE-SR Ethernet Optical Transceiver 

**AFBR-735SMZ** Data Sheet 

## **Figure 9:  Module Label** 


## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

AFBR-735SMZ-DS100 21 

Broadcom 

Broadcom, the pulse logo, Connecting everything, Avago Technologies, Avago, and the A logo are among the trademarks of Broadcom and/or its affiliates in the United States, certain other countries, and/or the EU. 

Copyright © 2015–2021 Broadcom. All Rights Reserved. 

The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, please visit www.broadcom.com. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

