**Data Sheet** 

## **AFBR-57G5MZ** 

**32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver** 


## **Description** 

The Broadcom[®] AFBR-57G5MZ optical transceiver supports high-speed serial links over multimode optical fiber at signaling rates up to 28.05 Gb/s (the serial line rate of 32GFC). The product is compliant with Small Form Pluggable industry agreements SFP and SFP28 for mechanical and low-speed electrical specifications. High-speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-6. 

The AFBR-57G5MZ is a multirate 850-nm transceiver that ensures compliance with FC-PI-6 32GFC, 16GFC, and 8GFC specifications. Per the requirements of 32GFC, internal clock and data recovery (CDR) circuits are present on both electrical input and electrical output of this transceiver. These CDRs lock at 28.05 Gb/s and 14.025 Gb/s (32GFC and 16GFC) but must be bypassed for operation at 8.5 Gb/s (8GFC), accomplished by using two Rate Select inputs to configure transmit and receive sides. The transmitter and receiver can operate at different data rates, as is often seen during Fibre Channel speed negotiation. 

Digital diagnostic monitoring information (DMI) is present in the AFBR-57G5MZ per the requirements of SFF-8472, providing real-time monitoring information of transceiver laser, receiver, and environment conditions over an SFF-8419 two-wire serial interface. 

## **Features** 

- Compliant to RoHS directives 

- 850-nm Vertical Cavity Surface Emitting Laser (VCSEL) 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 70°C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10A) 

- Diagnostic features per SFF-8472 _Diagnostic Monitoring Interface for Optical Transceivers_ 

- Real-time monitoring of the following: 

   - Transmitter average optical power 

   - Received average optical power 

   - Laser bias current 

   - Temperature 

   - Supply voltage 

- SFP28 mechanical specifications per SFF-8432 

- SFP28 compliant low-speed interface per SFF-8419 

- Fibre Channel FC-PI-6 compliant high-speed interface – 3200-M5-SN-S, 1600-M5-SN-S, 800-M5-SN-S 

- – 3200-M5E-SN-I, 1600-M5E-SN-I, 800-M5E-SN-I 

   - 3200-M5F-SN-I, 1600-M5F-SN-I, 800-M5F-SN-I 

- Fibre Channel FC-PI-6 compliant optical link distances 

## **Applications** 

- Fibre Channel switches (director, stand-alone, blade) 

- Fibre Channel host bus adapters 

- Fibre Channel RAID controllers 

- Fibre Channel tape drive 

- Port side connections 

- Inter-switch or inter-chassis aggregated links 

AFBR-57G5MZ-DS101 September 6, 2023 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Related Products** 

- AFCT-57G5MZ: 1310-nm SFP for 32G/16G/8G Fibre Channel 

- AFBR-57F5MZ: 850-nm SFP for 16G/8G/4G Fibre Channel 

- AFCT-57F5AMZ: 1310-nm SFP for 16G/8G/4G Fibre Channel 

- AFBR-57D9AMZ: 850-nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D5ATPZ: 1310-nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D5ANPZ: 1310-nm SFP for 8G/4G/2G Fibre Channel 

- AFBR-57R5APZ: 850-nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5APZ: 1310-nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5ATPZ: 1310-nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5ANPZ: 1310-nm SFP for 4G/2G/1G Fibre Channel 

## **Transmitter Section** 

The transmitter section includes a Transmitter Optical Sub-Assembly (TOSA), laser driver circuit, CDR circuit, and an electrical input stage with variable equalization controls. The TOSA contains an 850-nm VCSEL light source with an integral light-monitoring function and imaging optics to ensure efficient optical coupling to the LC connector interface. The TOSA is driven by a laser driver IC, which uses the differential output from an integral Tx CDR stage to modulate and regulate VCSEL optical power. As mandated by FC-PI-6, the integral CDR cleans up any incoming jitter accumulated from the host ASIC, PCB traces, and SFP electrical connector. Between the SFP electrical connector and Tx CDR is a variable, I[2] C controlled, equalization circuit to optimize SFP performance with nonideal incoming electrical waveforms. Note the Tx CDR is engaged with Tx_RATE = high (32GFC) and autoconfigured (engaged or bypassed) with Tx_RATE = low (16G/8G). 

## **Receiver Section** 

The receiver section includes a Receiver Optical Sub-Assembly (ROSA), pre-amplification and post-amplification circuit, CDR circuit, and an electrical output stage with variable emphasis controls. The ROSA, containing a high-speed PIN detector, preamplifier, and imaging optics, efficiently couples light from the LC connector interface and performs an optical-to-electrical conversion.The resulting differential electrical signal passes through a post-amplification circuit and into a CDR circuit for cleaning up accumulated jitter. 

Note the Rx CDR is engaged with Rx_RATE = high (32GFC) and autoconfigured (engaged or bypassed) with Rx_RATE = low (16G/8G). 

## **Digital Diagnostics** 

The AFBR-57G5MZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in SFF-8472. These features allow the host to access, using two-wire serial, real-time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage, and laser operating current. 

## **Low-Speed Interfaces** 

Conventional low-speed interface I/Os are available as defined in SFF-8419 to manage coarse and fine functions of the optical transceiver. On the transmit side, a Tx_DISABLE input is provided for the host to turn on and turn off the outgoing optical signal. A transmitter rate select control input, Tx_RATE, is provided to configure the transmitter stages for 32GFC, 16GFC, or 8GFC operation (logic HIGH reserved for 32GFC, logic LOW reserved for 16GFC and 8GFC). A transmitter fault indicator output, Tx_FAULT, is available for the SFP to signal a host of a transmitter operational problem. A receiver rate select control input, Rx_RATE, is provided to configure receiver stages for 32GFC, 16GFC, or 8GFC operation (logic HIGH reserved for 32GFC, logic LOW reserved for 16GFC and 8GFC). A received optical power loss of signal indicator, RX_LOS, is available to advise the host of a receiver operational problem. 

AFBR-57G5MZ-DS101 2 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Figure 1:  Transceiver Block Diagram** 


**----- Start of picture text -----**<br>
����������������� �������� ��������������������<br>������������������<br>������������������<br>������������� �� ���������<br>���������������� �������������� �������������� ��� �������� �����������������<br>��������������������<br>��������������<br>����������<br>��������������<br>��������<br>�����������<br>����������<br>����� �������������������<br>�������������� ����� �������������� ����� �������������� �������������������<br>��������� ��������<br>��������������������<br>**----- End of picture text -----**<br>


**Table 1:  Regulatory Compliance Table** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to<br>the Electrical Contacts|JEDEC Human Body Model (HBM)<br>(JESD22-A114-B)|High-speed contacts shall withstand 1000V. All<br>other contacts shall withstand 2000V.|
|Electrostatic Discharge (ESD) to<br>the Optical Connector Receptacle|EN61000-4-2, Criterion B|When installed in a properly grounded housing<br>and chassis the units are subjected to 15-kV air<br>discharges during operation and 8-kV direct<br>discharges to the case.|
|Electromagnetic Interference (EMI)|FCC Part 15 CENELEC EN55022<br>(CISPR 22A)VCCI Class 1|System margins are dependent on customer<br>board and chassis design.|
|Immunity|Variation of IEC 61000-4-3|Typically shows no measurable effect from a<br>10-V/m field swept from 80 MHz to 1 GHz applied<br>to the module without a chassis enclosure.|
|Laser Eye Safety and Equipment<br>Type Testing<br>������<br>�������<br>����<br>��������<br>���<br>���������<br>�������������<br>�<br>�|Class 1 Laser Product<br>US FDA CDRH AEL Class 1<br>US21 CFP, Subchapter J per Paragraphs<br>1002.10 and 1002.12<br>(IEC) EN60825-1:1994 +A11 +A2<br>(IEC) EN60825-2:1994 +A1<br>(IEC) EN60950:1992 +A1 +A2 +A3 +A4 +A11|CDRH Certification 9720151-155<br>TUV File: R72121699|
|Component Recognition|Underwriters Laboratories (UL) and Canadian<br>Standards Association (CSA) Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment|UL File: E173874|
|RoHS Compliance||Less than 1000 ppm of cadmium, lead, mercury,<br>hexavalent chromium, polybrominated biphenyls<br>(PPBs) and polybrominated biphenyl ethers<br>(PBDEs).|



AFBR-57G5MZ-DS101 3 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Figure 2:  Typical Application Configuration** 


**----- Start of picture text -----**<br>
Tx Rate Select  VCC,T<br>RS (1)<br>40 k Ω 10 k Ω<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1 μF<br>TD+<br>100  Ω<br>TD-<br>0.1 μF Tx CDR LASER DRIVER<br>4.7 k to 10 k Ω<br>4.7 μH VCC,T<br>0.1 μF 22 μF 0.1 μF<br>3.3 V<br>PROTOCOL IC SERDES IC 4.7 μH VCC,R VCC,R<br>VCC,R<br>0.1 μF 22 μF 0.1 μF 50  Ω<br>4.7 k to<br>10 k Ω 50  Ω<br>0.1 μF<br>RD+<br>100  Ω<br>RD-<br>0.1 μF<br>Rx LOS<br>LOSS OF SIGNAL<br>RS (0) Rx CDR POST AMPLIFIER<br>Rx Rate Select<br>3.3 V 40 k Ω<br>GND,R<br>4.7 k to 10 k Ω 4.7 k to 10 k Ω<br>4.7 k to 10 k Ω MOD_ABS MOD_SCL MOD_SDA<br>MODULE DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 3:  Recommended Power Supply Filter** 


**----- Start of picture text -----**<br>
4.7 μH<br>VCC T<br>0.1 μF 22 μF 0.1 μF<br>3.3 V<br>4.7 μH<br>VCC R<br>0.1 μF 22 μF 0.1 μF<br>SFP MODULE HOST BOARD<br>**----- End of picture text -----**<br>


**NOTE: INDUCTORS MUST HAVE LESS THAN 0.5** Ω **SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.** 

AFBR-57G5MZ-DS101 4 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Pin Descriptions** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground||
|2|TX_FAULT|Transmitter Fault Indication – High indicates a fault condition|a|
|3|TX_DISABLE|Transmitter Disable – Module optical output disables on high or open|b|
|4|MOD_SDA|Module Definition 2 – Two-wire serial ID interface data line (SDA)|c|
|5|MOD_SCL|Module Definition 1 – Two-wire serial ID interface clock line (SCL)|c|
|6|MOD_ABS|Module Definition 0 – Grounded in module (module present indicator)|c|
|7|Rx Rate Select, RS(0)|Receiver Rate Select. Logic High = 28.05 Gb/s, Logic Low = 14.025 Gb/s and 8.5 Gb/s|d|
|8|RX_LOS|Loss of Signal – High indicates loss of received optical signal|e|
|9|Tx Rate Select, RS(1)|Transmitter Rate Select. Logic High = 28.05 Gb/s, Logic Low = 14.025 Gb/s and 8.5 Gb/s|d|
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
|a. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. When high, this<br>output indicates a laser fault of some kind. Low indicates normal operation. In the low state, the output is pulled to < 0.8V.||||



- b. TX_DISABLE is an input that shuts down the transmitter optical output. It is internally pulled up (within the transceiver) with a 5.6-kΩ resistor. Low (0V to 0.8V): Transmitter on Between (0.8V and 2.0V): Undefined High (2.0V – Vcc max.) or OPEN: Transmitter Disabled 

- c. The signals Mod_ABS, SCL, and SDA designate the two-wire serial interface pins. They must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. 

Mod_ABS is grounded by the module to indicate the module is present. Mod_SCL is serial clock line (SCL) of a two-wire serial interface. Mod_SDA is serial data line (SDA) of a two-wire serial interface. 

d. RATE_SELECT is an input that controls transmitter and receiver compliance among multiple rates. It is internally pulled down with a 40-kΩ resistor. Low (0V to 0.8V) or OPEN: Low Bit Rate Compliance (14.025 Gb/s and 8.5 Gb/s) Between (0.8V and 2.0V): Undefined High (2.0V to Vcc max.): High Bit Rate Compliance (28.05 Gb/s) 

- e. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board. When high, this output indicates the received optical power is below the worst-case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output is pulled to < 0.8V. 

- f. RD–/+ designate the differential receiver outputs. They are AC coupled 100Ω differential lines that should be terminated with 100Ω differential at the host SerDes input. AC coupling is done inside the transceiver and is not required on the host board. The voltage swing on these lines is between 50-mV and 900-mV differential (25-mV to 450-mV single-ended) when properly terminated. 

- g. VccR and VccT are the receiver and transmitter power supplies. Refer to SFF-8419 for details. 

- h. TD–/+ designate the differential transmitter inputs. They are AC-coupled differential lines with 100Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. The inputs accept differential swings of 40 mV to 1200 mV (20-mV to 600-mV single-ended). Use values between 50-mV and 900-mV differential (25-mV to 450-mV single-ended) for best EMI performance. 

AFBR-57G5MZ-DS101 5 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Absolute Maximum Ratings** 

Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently. Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. Refer to the reliability data sheet for specific reliability performance. 

|**Parametera**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|85|°C||
|Case Operating Temperature|TC|–40|85|°C||
|Relative Humidity|RH|5|95|%||
|Supply Voltage|VCC|–0.5|3.6|V||
|Low Speed Input Voltage|VI|–0.5|VCC+ 0.5, 3.63|V||



- a. Absolute Maximum Ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. Between Absolute Maximum Ratings and the Recommended Operating Conditions, functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

## **Recommended Operating Conditions** 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted. Optical and electrical characteristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied, and damage to the module may occur for such operation over an extended period of time. 

**Table 2:  Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|0|—|85|°C|a|
|Supply Voltage|VCC|3.135|3.3|3.465|V||
|Data Rate||8.5|—|28.05|Gb/s|b|
|Two-Wire Serial (TWS) Interface Clock Rate||—|—|400|kHz|c|



- a. The position of case temperature measurement is shown in Figure 7. Continuous operation at the maximum recommended case operating temperature should be avoided so as not to degrade reliability. 

- b. 32GFC requires FEC RS(528,514) encoding per FC-PI-6. 16GFC and 8GFC are not compatible with FEC, per FC-PI-5. 

- c. With 500-µs clock stretch per SFF-8419. 

AFBR-57G5MZ-DS101 6 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Electrical and Optical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

**Table 3:  Transceiver Electrical Characteristics** 

|**Parameter**|**Symbols**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Transceiver Power Consumption||—|—|1.0|W||
|Transceiver Power SupplyCurrent||—|—|319|mA||
|Power Supply Noise Rejection (peak-peak)|PSNR|—|—|66|mVpp|a|
|TX_FAULT, RX_LOS|IOH|–50|—|37.5|µA|b|
||VOL|–0.3|—|0.4|V||
|TX_DIS, RS0, RS1|VIH|2.0|—|VCC+ 0.3|V||
||VIL|–0.3|—|0.8|V||
|MOD_SCL, MOD_SDA|VOH|VCC_Hst – 0.5|—|VCC_Hst + 0.3|V|c|
||VOL|0.0|—|0.4|V||
||VIH|VccT × 0.7|—|VccT + 0.5|V||
||VIL|–0.3|—|VccT × 0.3|V||



- a. Filter per SFF-8419 specification is required on the host board. 

- b. Measured with a 4.7-kΩ load pulled up to the host board to 3.3V. 

- c. Mod_SCL and Mod_SDA must be pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to host VCC (3.14 < VCC_Hst < 3.46V). 

**NOTE:** For Table 4, Table 5, and Table 6, TC = 0°C to 70°C, VccT, VccR = 3.3V ± 5%. 

**Table 4:  Transmitter and Receiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|High-Speed Data Input Transmitter Differential Input<br>Voltage(TD+/–)|VI|50|900|mV|Notea|
|High-Speed Data Output Receiver Differential Output<br>Voltage(RD+/–)|VO|250|900|mV|Noteb|
|Module Electrical Input, Differential Termination Resistance<br>Mismatch||—|10|%||
|Module Electrical Input Differential Return Loss SDD11||—|—||See FC-PI-6 Equation 6-1, Figure 10.|
|Module Electrical Input Common Mode to Differential<br>Conversion, SCD11||—|—||See FC-PI-6 Equation 6-2, Figure 12.|
|Module Electrical Input, Differential Mode to Common<br>Conversion, SDC11||—|—||See FC-PI-6 Equation 6-2, Figure 12.|
|Module Electrical Input, Stressed Input Random Jitter, p-p,<br>10E–6 BER||—|0.09|UI||
|Module Electrical Input, Stressed Input Eye Width at 1E–6<br>ProbabilityEW6||0.46|—|UI||
|Module Electrical Input, Stressed Input Eye Height at 1E–6<br>ProbabilityEH6||50|—|mV||
|Module Electrical Output, Common Mode Noise rms||—|17.5|mV,rms||
|Module Electrical Output, Differential Termination<br>Resistance Mismatch||—|10|%||



AFBR-57G5MZ-DS101 7 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 4:  Transmitter and Receiver Electrical Characteristics (Continued)** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Module Electrical Output, Differential Return Loss SDD22||—|—||See FC-PI-6 Equation 6-1, Figure 10.|
|Module Electrical Output, Common Mode to Differential<br>Conversion, SCD22||—|—||See FC-PI-6 Equation 6-3, Figure 12.|
|Module Electrical Output, Differential Mode to Common<br>Conversion, SDC22||—|—||See FC-PI-6 Equation 6-3, Figure 12.|
|Module Electrical Output, Common Mode Return Loss,<br>SCC22||—|–2|dB||
|Module Electrical Output, Vertical Eye Closure||—|4|dB||
|Module Electrical Output, Eye Width at 1E–6 Probability<br>EW6||0.65|—|UI||
|Module Electrical Output, Eye Height at 1E–6 Probability<br>EH12||250|—|mV||
|Receiver Total Jitter (28.05 Gb/s)|TJ|—|—|UI|Compliance Test. Notesc, d|
|Receiver Total Jitter (14.025 Gb/s)|TJ|—|0.36|UI|Notec|
|Receiver Total Jitter (8.5 Gb/s)|TJ|—|0.71|UI|Notee|
|Receiver Deterministic Jitter (14.025 Gb/s)|DJ|—|0.22|UI|Notec|
|Receiver Deterministic Jitter (8.5 Gb/s)|DJ|—|0.42|UI|Notee|
|Receiver Data Dependent Pulse Width Shrinkage<br>(14.025 Gb/s)|DDPWS|—|0.14|UI|Notec|
|Receiver Data Dependent Pulse Width Shrinkage<br>(8.5 Gb/s)|DDPWS|—|0.36|UI|Notee|



a. Internally AC coupled and terminated (100Ω differential). 

b. Internally AC coupled but requires an external load termination (100Ω differential). 

c. CDR is engaged with 28.05 Gb/s and 14.025 Gb/s. 

d. 32GFC (28.05 Gb/s) assumes an FEC encoded RS(528, 514) signal and allows a BER of 1E–6 for receiver and transmitter measurements. 

e. CDR is not engaged with 8.5 Gb/s. 

AFBR-57G5MZ-DS101 8 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 5:  Transmitter Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Modulated Optical Output Power (OMA) (Peak to<br>Peak)28.05 Gb/s|Tx,OMA|479|—|—|µW||
|Modulated Optical Output Power (OMA) (Peak to<br>Peak)14.025 Gb/s|Tx,OMA|331|—|—|µW||
|Modulated Optical Output Power (OMA) (Peak to<br>Peak)8.5 Gb/s|Tx,OMA|302|—|—|µW||
|Average Optical Output Power 28.05 Gb/s|Pout|–6.2|—|—|dBm|a|
|Average Optical Output Power 14.025 Gb/s|Pout|–7.8|—|—|dBm|a|
|Average Optical Output Power 8.5 Gb/s|Pout|–8.2|—|—|dBm|a|
|Center Wavelength|λc|840|—|860|nm||
|Spectral Width – rms|σrms|—|—|0.57|nm||
|RIN12(OMA)|RIN|—|—|–129|dB/Hz||
|Optical Return Loss Tolerance||—|—|12|dB||
|Vertical Eye Closure Penalty, 28.05 Gb/s|VECP|—|—|3.13|dB|b|
|Vertical Eye Closure Penalty, 14.025 Gb/s|VECP|—|—|2.56|dB|b|
|Transmitter Waveform Distortion Penalty, 8.5 Gb/s|TWDP|—|—|4.3|dB|c|
|Pout Tx_DISABLE Asserted|Poff|—|—|–35|dBm||



- a. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

- b. CDR is engaged with 28.05 Gb/s and 14.025 Gb/s. 

- c. CDR is not engaged with 8.5 Gb/s. 

**Table 6:  Receiver Optical and Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power, 28.05 Gb/s|PIN|—|—|+2|dBm,avg||
|Optical Input Power, 14.025 Gb/s and 8.5 Gb/s|PIN|—|—|0|dBm,avg||
|Input Optical Modulation Amplitude, 28.05 Gb/s (Peak<br>to Peak) (Unstressed Sensitivity)|OMA|95|—|—|µW,OMA|a, b|
|Input Optical Modulation Amplitude, 14.025 Gb/s<br>(Peak to Peak) (Unstressed Sensitivity)|OMA|89|—|—|µW,OMA|a|
|Input Optical Modulation Amplitude, 8.5 Gb/s (Peak to<br>Peak) (Unstressed Sensitivity)|OMA|76|—|—|µW,OMA|a|
|Stressed Receiver Sensitivity (OMA) 28.05 Gb/s||263|—|—|µW,OMA|b, c|
|Stressed Receiver Sensitivity (OMA) 14.025 Gb/s||170|—|—|µW,OMA|d|
|Stressed Receiver Sensitivity (OMA) 8.5 Gb/s||151|—|—|µW,OMA|e|
|Return Loss||12|—|—|dB||
|Loss of Signal – Assert|PA|–30|—|—|dBm,avg||
|Loss of Signal – Deasserted|PD|—|—|–9.1|dBm,avg||
|Loss of Signal – Hysteresis|PA– PD|0.5|—|—|dB||



a. Input optical modulation amplitude (commonly known as sensitivity) requires a valid Fibre Channel encoded input. 

- b. 32GFC (28.05 Gb/s) assumes an FEC-encoded RS(528, 514) signal and allows a BER of 1E–6 for receiver and transmitter measurements. 

- c. 28.05-Gb/s stressed received vertical eye closure penalty (ISI) min is 3.1 dB. 

- d. 14.025-Gb/s stressed received vertical eye closure penalty (ISI) min is 2.5 dB. 

- e. 8.5 Gb/s stressed received vertical eye closure penalty (ISI) min is 3.1 dB. 

AFBR-57G5MZ-DS101 9 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Rate Select Control Inputs** 

## **Table 7  Rate Select Definitions[a]** 

|**Function**|**State**|**Operation**|
|---|---|---|
|Tx Rate Select RS(1)|High<br> <br> <br>|Transmit Rate Select HIGH is defined for 32GFC operation. It configures the Tx CDR to lock on<br>28.05-Gb/s 64b/66b encoded data and sets the Tx optical power and linear bandwidth for 32GFC<br>operation. FEC is expected for 32GFC.|
||Low<br> <br> <br>|Transmit Rate Select LOW autoconfigures the internal Tx CDR for 16GFC (CDR locked) or 8GFC<br>(CDR bypassed) operation. Transmit optical power and linear bandwidth are optimized accordingly.<br>FEC is not expected for 16GFC or 8GFC. This is intended for use onlywith 16GFC and 8GFC traffic.|
|Rx Rate Select RS(0)|High<br> <br> <br>|Receive Rate Select HIGH is defined for 32GFC operation. It configures the Rx CDR to lock on<br>28.05 Gb/s 64b/66b encoded data and sets the Rx optical sensitivity and bandwidth for 32GFC<br>operation. FEC is expected for 32GFC.|
||Low<br> <br> <br> <br>|Receive Rate Select LOW autoconfigures the internal Rx CDR for 16GFC (CDR locked) or 8GFC<br>(CDR bypassed) operation. Receiver optical sensitivity and linear bandwidth are optimized<br>accordingly. FEC is not expected for 16GFC or 8GFC. This is intended for use only with 16GFC and<br>8GFC traffic.|



a. During Fibre Channel link speed negotiation sequences, the host controls the Tx Rate and Rx Rate inputs separately to accomplish link initialization. When speed negotiation is complete, it is expected that both Tx Rate and Rx Rate are placed in the same state by the host. 

Rx and Tx rates can be independently controlled by either hardware input pins or using register writes. Module electrical input pins 7 and 9 are used to select Rx and Tx rates, respectively. The status of each logic level is reflected to register byte 110 bits 4 and 5 on address A2h as shown in the following figures. Rx and Tx rates can also be controlled using register writes to bytes 110 bit 3 and 118 bit 3. The power-on default of these bits is logic low. Hardware and software control inputs are ORed to allow flexible control. 

**Figure 4:  RS0 Rx Rate Select Control Flow** 


**----- Start of picture text -----**<br>
��������� ���������<br>����� �����<br>������������������ �������������<br>����������� �����<br>�����������<br>�������������<br>����� ��<br>�������<br>�������<br>**----- End of picture text -----**<br>


**Figure 5:  RS1 Tx Rate Select Control Flow** 


**----- Start of picture text -----**<br>
��������� ���������<br>����� �����<br>������������������ �������������<br>����������� �����<br>�����������<br>�������������<br>����� ��<br>�������<br>�������<br>**----- End of picture text -----**<br>


|**RS0 Control Input**|**RS0 Control Input**|**Rx Operation**|**Rx Operation**|
|---|---|---|---|
|**Hardware**|**Software**|||
|0|0|16G/8G FC|Rx CDR autodetect|
|0|1|32GFC|Rx CDR engaged|
|1|0|32GFC|Rx CDR engaged|
|1|1|32GFC|Rx CDR engaged|



|**RS1 Control Input**|**RS1 Control Input**|**Tx Operation**|**Tx Operation**|
|---|---|---|---|
|**Hardware**|**Software**|||
|0|0|16G/8G FC|Tx CDR autodetect|
|0|1|32GFC|Tx CDR engaged|
|1|0|32GFC|Tx CDR engaged|
|1|1|32GFC|Tx CDR engaged|



AFBR-57G5MZ-DS101 10 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Transceiver Characteristics** 

For Table 8 and Table 9, TC = –10 °C to 70 °C, VccT, VccR = 3.3V ± 5%. 

**Table 8:  Transceiver SOFT DIAGNOSTIC Timing Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Hardware TX_DISABLE Assert Time|t_off|—|100|µs|a|
|Hardware TX_DISABLE Negate Time|t_on|—|2|ms|b|
|Time to Initialize, including Reset of TX_FAULT|t_init|—|300|ms|c|
|Hardware TX_FAULT Assert Time|t_fault|—|1|ms|d|
|Hardware TX_DISABLE to Reset|t_reset|10|—|µs|e|
|Hardware RX_LOS Deassert Time|t_loss_on|—|100|µs|f|
|Hardware RX_LOS Assert Time|t_loss_off|—|100|µs|g|
|Hardware RATE_SELECT Assert Time|t_rate_high|—|2|ms|h|
|Hardware RATE_SELECT Deassert Time|t_rate_low|—|2|ms|h|
|Software TX_DISABLE Assert Time|t_off_soft|—|100|ms|i|
|Software TX_DISABLE Negate Time|t_on_soft|—|100|ms|j|
|Software Tx_FAULT Assert Time|t_fault_soft|—|100|ms|k|
|Software Rx_LOS Assert Time|t_loss_on_soft|—|100|ms|l|
|Software Rx_LOS Deassert Time|t_loss_off_soft|—|100|ms|m|
|Software RATE_SELECT Assert Time|t_rate_soft_high|—|100|ms|n|
|Software RATE_SELECT Deassert Time|t_rate_soft_low|—|100|ms|o|
|Analog Parameter Data Ready|t_data|—|1000|ms|p|
|Serial Bus Hardware Ready|t_serial|—|300|ms|q|
|Serial Bus Buffer Time|t_buf|20|—|µs|r|
|Complete Single or Sequential Write Up to 4 Bytes|twR|—|40|ms|s|
|Complete Sequential Write of 5 to 8 Bytes|twR|—|80|ms||
|Serial Interface Clock Holdoff_Clock Stretching_|T_clock_hold|—|500|µs|t|
|Serial ID Clock Rate|f_serial_clock|—|400|kHz|u|



- a. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

- b. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

- c. Time from power-on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

- d. From occurrence of fault to assertion of TX_FAULT. 

- e. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

- f. Time from loss of optical signal to Rx_LOS Assertion. 

- g. Time from valid optical signal to Rx_LOS Deassertion. 

- h. Time from rising or falling edge of Rate_Select input until transceiver is successfully passing traffic as designated by RS(0) and RS(1). For Rate_Select going high, the internal CDR locks on valid 32GFC encoded data within the specified time. For Rate_Select going low, the internal CDR attempts to lock on valid 16GFC encoded data for a certain gating period. If valid 16GFC data is not detected in that gating period, the internal CDR is automatically bypassed for use at 8GFC rates. 

- i. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

- j. Time from two-wire interface deassertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output rises above 90% of nominal. 

AFBR-57G5MZ-DS101 11 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

- k. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

- l. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

- m. Time for two-wire interface deassertion of Rx_LOS (A2h, byte 110, bit 1) from presence of a valid optical signal. 

- n. Time from two-wire interface assertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is engaged at 32GCFC data rate. 

- o. Time from two-wire interface deassertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is either engaged at 16GCFC data rate or bypassed for 8GFC operation. 

- p. From power-on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

- q. Time from power-on until the module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). 

- r. Time between START and STOP commands. 

- s. Time from stop bit to completion of a 1- to 8-byte write command. 

- t. Maximum time the SFP+ module may hold the SCL line low before continuing with a read or write operation. 

- u. With a maximum clock stretch of 500 µs. A maximum of 100-kHz operation can be supported without a clock stretch. 

**Table 9:  Transceiver Digital Diagnostic Monitor (Real-Time Sense) Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature<br>Accuracy|TINT|±3.0|°C|Temperature is measured internal to the transceiver. Valid<br>from 0°C to 70°C case temperature.|
|Transceiver Internal Supply Voltage<br>Accuracy|VINT|±0.1|V|Supply voltage is measured internal to the transceiver and<br>can, with less accuracy, be correlated to voltage at the SFP<br>VCCpin. Valid over 3.3V ± 5%.|
|Transmitter Laser DC Bias Current<br>Accuracy|IINT|±10|%|IINTis better than ±10% of the nominal value.|
|Transmitted Average Optical<br>Output Power Accuracy|PT|±3.0|dB|Coupled into 50-µm multimode fiber. Valid from –8.2 dBm<br>to +2 dBm avg.|
|Received Optical Input Power<br>Accuracy|PR|±3.0|dB|Coupled from 50-µm multimode fiber. Valid from<br>–10.3 dBm to +2 dBm avg.|



AFBR-57G5MZ-DS101 

Broadcom 

12 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Figure 6:  Transceiver Timing Diagrams (Module Installed Except Where Noted)** 


**----- Start of picture text -----**<br>
��������������� ���������������<br>�������� ��������<br>���������� ����������<br>������������������ ������������������<br>������ ������<br>�������������������������� ���������������������������<br>��������������� ��������<br>�������� ����������<br>����������<br>������������������<br>������������������<br>����� ����<br>������<br>���������<br>����������������������������������������������� ����������������������������������������������<br>������������������<br>������������������<br>��������<br>��������<br>����������<br>����������<br>������������������<br>������������������<br>������� ����������������������������� ������� �������<br>��������������������������������������<br>��������������������������������������������������� ��������������������������������������������������������������<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
������������������<br>�������� ���������<br>�������������� �������<br>����������<br>������������������ ���<br>�������<br>������� ��������� ����������<br>����������������������������� �������<br>����������������������������������������<br>������������������������������������������������������������������ ����������������������<br>**----- End of picture text -----**<br>


AFBR-57G5MZ-DS101 13 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **EEPROM Serial ID Memory Contents** 

**Table 10:  EEPROM Serial ID Memory Contents – Address A0h** 

|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|
|---|---|---|---|---|---|
|0|03|SFP physical device|37|00|Hex Byte of Vendor OUIa|
|1|04|SFP function defined by serial ID only|38|17|Hex Byte of Vendor OUIa|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUIa|
|3|00||40|41|"A" – Vendor Name ASCII Character|
|4|00||41|46|"F" – Vendor Name ASCII Character|
|5|00||42|42|"B" – Vendor Name ASCII Character|
|6|00||43|52|"R" – Vendor Name ASCII Character|
|7|60|Short and Intermediate link distance (per<br>FC-PI-6)|44|2D|"-" – Vendor Name ASCII Character|
|8|40|Shortwave laser without OFC (open fiber<br>control)|45|35|"5" – Vendor Name ASCII Character|
|9|04|Multimode 50-µm optical media|46|37|"7" – Vendor Name ASCII Character " "|
|10|68|800, 1600, and 3200 MB/s FC-PI-6 speedb|47|47|G" – Vendor Name ASCII Character " "|
|11|06|64B/66B data at 32GFC/16GFC and 8B/10B<br>at 8GFC|48|35|"5" – Vendor Name ASCII Character|
|12|FF|Greater than 25.5 Gb/s(see Address 66)|49|4D|"M" – Vendor Name ASCII Character|
|13|0C|Rate Select (High=32GFC, Low=16GFC,<br>8GFC)|50|5A|"Z" – Vendor Name ASCII Character|
|14|00||51|20|" " – Vendor Name ASCII Character|
|15|00||52|20|" " – Vendor Name ASCII Character|
|16|02|20m of OM2 50/125-µm distance at 32GFCc|53|20|" " – Vendor Name ASCII Character|
|17|00|Unspecified OM1 62.5/125-µm distance at<br>32GFCd|54|20|" " – Vendor Name ASCII Character|
|18|0A|100m of OM4 50/125-µm fiber at 32GFCe|55|20|" " – Vendor Name ASCII Character|
|19|07|70m of OM3 50/125-µm fiber at 32GFCf|56|20|" " – Vendor Name ASCII Character|
|20|41|"A"  – Vendor Name ASCII Character|57|20|" " – Vendor Name ASCII Character|
|21|56|"V" – Vendor Name ASCII Character|58|20|" " – Vendor Name ASCII Character|
|22|41|"A" – Vendor Name ASCII Character|59|20|" " – Vendor Name ASCII Character|
|23|47|"G" – Vendor Name ASCII Character|60|03|Hex Byte of Laser Wavelengthg|
|24|4F|"O" – Vendor Name ASCII Character|61|52|Hex Byte of Laser Wavelengthg|
|25|20|" " – Vendor Name ASCII Character|62|00||
|26|20|" " – Vendor Name ASCII Character|63||Checksum for Bytes 0 to 62h|
|27|20|" " – Vendor Name ASCII Character|64|08|CDRspresent. 1Wpower class|
|28|20|" " – Vendor Name ASCII Character|65|3A|Hardware Tx_Disable, Tx_Fault, Rx_LOS,<br>Rate_Select|
|29|20|" " – Vendor Name ASCII Character|66|70|28.050-Gb/s nominal bit rate(32GFC)|
|30|20|" " – Vendor Name ASCII Character|67|00||
|31|20|" " – Vendor Name ASCII Character|68–83||Vendor Serial Number ASCII charactersi|



AFBR-57G5MZ-DS101 

Broadcom 

14 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 10:  EEPROM Serial ID Memory Contents – Address A0h (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|**Byte**<br>**Number**<br>**Decimal**|**Hex**|**Description**|
|---|---|---|---|---|---|
|32|20|" " – Vendor Name ASCII Character|84–91||Vendor Date Code ASCII charactersj|
|33|20|" " – Vendor Name ASCII Character|92|68|Digital diagnostics, Internal Cal, Rx Pwr Avg|
|34|20|" " – Vendor Name ASCII Character|93|FA|Alarms/Warnings, Software Tx_Disable,<br>Tx-Fault, Rx_LOS, Rate_Select|
|35|20|" " – Vendor Name ASCII Character|94|08|SFF-8472 compliance to revision 12.2|
|36|00||95||Checksum for Bytes 62 to 94h|
||||96–255|00||



- a. The IEEE Organizationally Unique Identified (OUI) assigned to Broadcom is 00-17-6A (3 bytes of hex). 

- b. FC-PI-6 speed 3200 MB/s is a serial bit rate of 28.05 Gb/s using FEC encoded data (RS 528/514). FC-PI-5 speed 1600 MB/s is a serial bit rate of 14.025 Gb/s. 800 MB/s is a serial bit rate of 8.5 Gb/s. 

- c. Link distance with OM2 50/125-µm cable at 16GFC is 35m and at 8GFC is 50m. 

- d. Link distance with OM1 62.5/125-µm cable at 8.5Gb/s is 25m (and is unspecified at 16GFC). 

- e. Link distance with OM4 50/125-µm cable at 16GFC is 125m and at 8GFC is 190m. 

- f. Link distance with OM3 50/125-µm cable at 16GFC is 100m and at 8GFC is 150m. 

- g. Laser wavelength is represented in 16 unsigned buts. The hex representation of 850 nm is 0352. 

- h. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored prior to product shipment. 

- i. Addresses 68 to 83 specify the AFBR-57G5MZ ASCII serial number and vary on a per-unit basis. 

- j. Addresses 84 to 91 specify the AFBR-57G5MZ ASCII data code and vary on a per-date code basis. 

**Table 11:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h)** 

|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|0|TempH Alarm MSBa|26|Tx Power L Alarm MSBg|104|Real Time Rx Power MSBb|
|1|TempH Alarm LSBa|27|Tx Power L Alarm LSBg|105|Real Time Rx Power LSBb|
|2|TempL Alarm MSBa|28|Tx Power H WarningMSBg|106|Reserved|
|3|TempL Alarm LSBa|29|Tx Power H WarningLSBg|107|Reserved|
|4|TempH WarningMSBa|30|Tx Power L WarningMSBg|108|Reserved|
|5|TempH WarningLSBa|31|Tx Power L WarningLSBg|109|Reserved|
|6|TempL WarningMSBa|32|Rx Power H Alarm MSBb|110|Status/Control – SeeTable 12.|
|7|TempL WarningLSBa|33|Rx Power H Alarm LSBb|111|Status/Control – SeeTable 13.|
|8|Vcc H Alarm MSBc|34|Rx Power L Alarm MSBb|112|Flag Bits – SeeTable 14.|
|9|Vcc H Alarm LSBc|35|Rx Power L Alarm LSBb|113|Flag Bits – SeeTable 14.|
|10|Vcc L Alarm MSBc|36|Rx Power H Warning MSBb|114|Tx Input EQ Control – See<br>Table 17,Table 18.|
|11|Vcc L Alarm LSBc|37|Rx Power H Warning LSBb|115|Rx Output Emphasis ControlSee<br>Table 19,Table 20.|
|12|Vcc H WarningMSBc|38|Rx Power L WarningMSBb|116|Flag Bits – SeeTable 14.|
|13|Vcc H WarningLSBc|39|Rx Power L WarningLSBb|117|Flag Bits – SeeTable 14.|



AFBR-57G5MZ-DS101 

Broadcom 

15 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 11:  EEPROM Serial ID Memory Contents – Enhanced SFP Memory (Address A2h) (Continued)** 

|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|**Byte**<br>**Number**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|14|Vcc L WarningMSBc|40–55|Optional Alarm and Warning|118|Status/Control – SeeTable 15.|
|15|Vcc L Warning LSBc|56–94|External Calibration Constantsd|119|CDR Loss of Lock Status – See<br>Table 16.|
|16|Tx Bias H Alarm MSBe|95|Checksum for Bytes 0 to 94f|120–126|Reserved|
|17|Tx Bias H Alarm LSBe|96|Real Time Temperature MSBa|127|Page Select Control|
|18|Tx Bias L Alarm MSBe|97|Real Time Temperature LSBa|128–247|Customer Writable|
|19|Tx Bias L Alarm LSBe|98|Real Time Vcc MSBc|248–255|Vendor Specific|
|20|Tx Bias H WarningMSBe|99|Real Time Vcc LSBc|||
|21|Tx Bias H WarningLSBe|100|Real Time Tx Bias MSBe|||
|22|Tx Bias L WarningMSBe|101|Real Time Tx Bias LSBe|||
|23|Tx Bias L WarningLSBe|102|Real Time Tx Power MSBg|||
|24|Tx Power H Alarm MSBg|103|Real Time Tx Power LSBg|||
|25|Tx Power H Alarm LSBg|||||



a. Temperature (Temp) is decoded as a 16-bit signed two's complement integer in increments of 1/256°C. 

b. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

c. Supply voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 µV. 

d. Bytes 56–94 are not intended for use, but have been set to default values per SFF-8472. 

e. Tx bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 µA. 

f. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment. 

g. Transmitted average optical power (Tx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 µW. 

**Table 12:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|a|
|6|Soft TX_DISABLE Control|Read/write bit for changing digital state of TX_DISABLE function|a, b|
|5|RS(1)State|Digital state of Tx Rate_Select Input Pin RS(1) (1 = Rate High asserted)||
|4|RS(0)State|Digital state of Rx Rate_Select Input Pin RS(0) (1 = Rate High asserted)||
|3|Soft RS(0) Control|Read/write bit for changing digital state of Rx Rate_Select RS(0) function|c|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|a|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|a|
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready (0 = Data<br>Ready)||



a. The response time for soft commands of the AFBR-57G5MZ is 100msec as specified by MSA SFF-8472. 

b. Bit 6 is log ORed with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter. 

c. Bit 3 is log ORed with the SFP RS(0) Rx Rate_Select input pin 7 …. either asserted will set receiver to Rate = High. 

AFBR-57G5MZ-DS101 16 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 13:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 111)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|3–7|Reserved|||
|2|OWRAP Control Bit|Logic Low = OWRAP disabled. Logic High = OWRAP enabled. When<br>enabled, OWRAP routes incoming SFP Rx optical data to the Tx optical<br>output and Rx electrical output. Enablingclears all other bits in byte 111.||
|1|EWRAP FORWARD Control Bit|Logic Low = FORWARD disabled. Logic High = FORWARD enabled. When<br>used in combination with EWRAP enable, FORWARD routes incoming SFP<br>Tx electrical data to both Rx electrical output and Tx optical output. Enabling<br>sets bit 0 and clears all other bits in byte 111.||
|0|EWRAP Control Bit|Logic Low = EWRAP disabled. Logic High = EWRAP enabled. When<br>enabled, EWRAP routes incoming SFP Tx electrical data to the Rx electrical<br>output. Enablingclears all other bits in byte 111.||



**Table 14:  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

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



AFBR-57G5MZ-DS101 17 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

**Table 15:  EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4–7|Reserved|||
|3|Soft RS(1) Control|Read/write bit for changing digital state of Tx Rate_Select RS(1) function.|a|
|2|Reserved|||
|1|Power Level State|Always set to zero. Value of zero indicates Power Level 1 operation(1W max.).||
|0|Power Level Select|Unused. This device supportspower level zero(1W max.)only.||



a. Bit 3 is log ORed with the SFP RS(1) Tx Rate_Select input pin 9 …. either asserted will set transmitter to Rate = High. 

**Table 16:  EEPROM Serial ID Memory Contents – CDR Loss of Lock (LOL) Status Indicators (Address A2h, Byte 119)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–2|Reserved|||
|1|TX CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock.<br>If the CDR is operationally bypassed (that is, for 8.5-Gb/s operation), the value is<br>undefined.||
|0|RX CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock.<br>If the CDR is operationally bypassed (that is, for 8.5-Gb/s operation), the value is<br>undefined.||



**Table 17:  EEPROM Serial ID Memory Contents – Transmitter Input Electrical Equalization Control (Address A2h, Byte 114)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|TX EQ, RS(1)=HIGH|Selects an input equalization value per Table 9-13 of SFF-8472 for high rate<br>operation.||
|3–0|TX EQ, RS(1)=LOW|Selects an input equalization value per Table 9-13 of SFF-8472 for low rate<br>operation.||



AFBR-57G5MZ-DS101 18 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

From Table 9-13 of SFF-8472. 

**Table 18:  Transmitter Input Equalization Control Values (Address A2h, Byte 114)** 

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



**Table 19:  EEPROM Serial ID Memory Contents – Receiver Output Electrical Emphasis Control (Address A2h, Byte 115)** 

|**Bit Number**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7–4|RX EMPH, RS(0)=HIGH|Selects an output emphasis value per Table 9-14 of SFF-8472 for high rate<br>operation.||
|3–0|RX EMPH, RS(0)=LOW|Selects an output emphasis value per Table 9-14 of SFF-8472 for low rate<br>operation.||



From Table 9-14 of SFF-8472. 

**Table 20:  Receiver Output Emphasis Control Values (Address A2h, Byte 115)** 

|**Code**|**Receiver Output Emphasis**<br>**At Nominal Output Amplitude**|**Receiver Output Emphasis**<br>**At Nominal Output Amplitude**|
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



AFBR-57G5MZ-DS101 19 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Figure 7:  Module Drawing** 


**----- Start of picture text -----**<br>
8.99 47.5<br>13.9 13.46<br>13.65<br>0.65 Uncompressed<br>12.5 8.5<br>6.25<br>0.7 Uncompressed<br>14.8 Uncompressed<br>Tcase Reference Point Bottom Label<br>TX RX<br>**----- End of picture text -----**<br>


**Figure 8:  Module Label** 


AFBR-57G5MZ-DS101 20 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Figure 9:  SFP Host Board Mechanical Layout** 


**----- Start of picture text -----**<br>
�<br>�<br>����<br>��<br>��<br>���������������� ��� ���<br>����� � ��������������� ��� �����������<br>���������� � � ������������<br>���<br>��� � � �<br>���� ����<br>���� ����� ��<br>���� ������ ����<br>����� �����<br>�����<br>����� ���<br>����<br>���<br>��<br>��<br>������������<br>��� ��������������<br>��� ������� � ���������������<br>���� �<br>�<br>� ��<br>��<br>����<br>����<br>�<br>���<br>��������������<br>���<br>������������������������<br>����� �� ������<br>����� ����� ����� ����������������������������������<br>���<br>���<br>���� ���������������������������������<br>��<br>�� ��������������������������������<br>�������������������������<br>���������������<br>� ������������������������<br>�������������� ������������������������<br>��������������<br>������������������������<br>� ������������������ �����������������������������<br>��������<br>**----- End of picture text -----**<br>


AFBR-57G5MZ-DS101 21 

Broadcom 

32GFC SFP28 for Multimode Optical Fiber Digital Diagnostic SFP, 850-nm, 32G/16G/8G Low-Voltage (3.3V) Fibre Channel Optical Transceiver 

**AFBR-57G5MZ** Data Sheet 

## **Figure 10:  SFP Assembly Drawing** 


**----- Start of picture text -----**<br>
1.7 ± 0.9<br>3.5 ± 0.3<br>42.08 ± 0.5<br>15 MAX.<br>9.8 MAX.<br>16.25 ± 0.1<br>10<br>15.25 ± 0.1<br>**----- End of picture text -----**<br>


## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

AFBR-57G5MZ-DS101 22 

Broadcom 

Copyright © 2015–2023 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

