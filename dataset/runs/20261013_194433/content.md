**Data Sheet** 

# **AFBR-57L1APZ 1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet** 


## **Description** 

The Broadcom[®] AFBR-57L1APZ small form-factor pluggable (SFP) transceiver is a fiber-optic solution for transmission of 1.25-Gbaud data up to 2 km for multimode fibers. This transceiver is compatible with the IEEE 802.3z Gigabit Ethernet and SFF-8472 diagnostic monitoring interface (DMI) standards. The AFBR-57L1APZ provides the system designer with a product to implement 1.25Gigabit Ethernet networks with DMI physical layers. 

Using the 2-wire serial interface defined in the SFF-8472 multisource agreement (MSA), the AFBR-57L1APZ provides real-time information on temperature, FP laser bias current, FP laser average output power, and FP laser receiver average input power. 

## **Transmitter** 

## **Features** 

- RoHS compliant 

- Lead free 

- Industry-standard SFP package 

- LC duplex connector optical interface 

- Operates with OM1 (62.5-μm/125-μm) and OM4 (50-μm/125-μm) multimode fiber 

- Compatible with 1.25-Gigabit Ethernet IEEE 802.3z 

- Diagnostic monitoring interface 

- Class 1 laser product compliant with EN 60825-1 

- Single +3.3V power supply 

- Manufactured in an ISO 9001 certified facility 

- Operating temperature range: –40°C to 85°C 

- Hot-plug capability 

## **Applications** 

- Factory automation 

The transmitter contains a 1310-nm FP laser. This FP laser is packaged in the optical subassembly of the transmitter. It is driven by an integrated circuit that converts differential LVPECL logic signals into an analog FP laser drive current. This current is monitored by the diagnostic monitoring interface. The light optical output power is measured using a monitor diode in the optical subassembly to compensate the optical output for temperature and voltage variations. 

- Gigabit Ethernet networking over multimode fiber 

- Power substation automation 

- Transportation 

## **Receiver** 

The receiver utilizes a PIN photodiode coupled to a transimpedance pre-amplifier IC. It is packaged in the optical subassembly of the receiver. The data output is differential LVPECL. The LOS output is +3.3 V TTL as per SFF-8074i. The PIN photodiode average current is monitored by the diagnostic monitoring interface as a measure for input optical power. 

AFBR-57L1APZ-DS102 July 11, 2025 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Module Package** 

The transceiver package is compliant with the SFP MSA with the LC duplex connector option. The hot-pluggable capability of the SFP package allows the module to be installed at any time, including when the host system is online and operating. This capability permits the system to be configured or maintained without system downtime. The AFBR-57L1APZ requires a 3.3V DC power supply for optimal performance. 

## **Module Diagrams** 

Figure 1 shows the major functional components of the AFBR-57L1APZ, and Figure 2 shows the connection diagram of the module. The dimensions of the module are under construction and will be provided in an updated version of this data sheet. 

**Figure 1:  Transceiver Functional Diagram** 


**----- Start of picture text -----**<br>
O P T IC A L  IN T E R F A C E E L E C T R IC A L  IN T E R F A C E<br>R E C E IV E R<br>A M P L IF IC A T IO N R D +<br>L IG H T  F R O M  F IB E R P H O T O -D E T E C T O R &  Q U A N T IZ A T IO N<br>R D -<br>R X  L O S S  O F  S IG N A L<br>C O N T R O L L E R  &  M E M O R Y S D A<br>S C L<br>M O D -D E F 0<br>T R A N S M IT T E R T X  D IS A B L E<br>T D +<br>L IG H T  T O  F IB E R F P  L A S E R L A S E R  D R IV E R<br>T D -<br>T X _F A U L T<br>**----- End of picture text -----**<br>


## **Installation** 

The AFBR-57L1APZ can be installed in or removed from any MSA-compliant SFP port regardless of whether the host equipment is operating. The module housing makes initial contact with the host-board EMI shield, mitigating potential damage due to ESD. Controlled hot-plugging is ensured by 3-stage pin sequencing at the electrical interface. The 3-stage pin contact sequencing involves (1) ground, (2) power, and then (3) signal pins making contact with the host-board surfacemount connector—in that order. 

**Figure 2:  Connection Diagram of Module PCB** 


**----- Start of picture text -----**<br>
20 VEET 1 VEET<br>2 NU<br>18 TD+ 3 TxDisable<br>17 VEET 4 MOD-DEF(2)<br>16 VCCT 5 MOD-DEF(1)<br>15 VCCR 6 MOD-DEF(0)<br>14 VEER 7 NU<br>13 RD+ 8 LOS<br>9 VEER<br>11 VEER 10 VEER<br>TOP OF BOARD BOTTOM OF BOARD<br>(AS VIEWED THROUGH TOP OF BOARD)<br>**----- End of picture text -----**<br>


AFBR-57L1APZ-DS102 

Broadcom 

2 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD) to the<br>Electrical Pins|JEDEC JESD22-A114|Meets Class 2 (2000V to 3999V). Withstands<br>upto 2000V applied between electricalpins.|
|Electrostatic Discharge (ESD) to the Duplex<br>LC Receptacle|Variation of IEC 61000-4-2|Typically withstands at least 8 kV without<br>damage when the LC-connector receptacle<br>is contacted by a human-body-model probe.<br>Typically withstands a 15-kV air discharge on<br>the LC-connector receptacle.|
|Electromagnetic Interference (EMI)|Emission: EN 55016-2-3, Class B.<br>(Reference is EN 55032:2015 +AC:2016<br>+A1:2020 +A11:2020)<br>Immunity: EN IEC 61000-6-2:2019|System margins are dependent on the<br>customer board and chassis design.|
|Eye Safety|IEC 60825-1:2014|Compliant per Broadcom testing under<br>single-fault conditions.|
|RoHS Compliance|—|Reference to RoHS Directive 2011/65EU<br>Annex II.|



AFBR-57L1APZ-DS102 

Broadcom 

3 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

**Figure 3:  Recommended Connection Circuitry** 


**----- Start of picture text -----**<br>
1 μH<br>3.3V<br>10 μF 0.1 μF 10 μF 0.1 μF<br>1 μH<br>VccT<br>3.3V AFBR-57L1APZ<br>7.6 kΩ<br>Tx Dis<br>TX_GND<br>4.7 kΩ to 10 kΩ<br>0.1 μF<br>50Ω<br>SO+ LASER DRIVER<br>TD+<br>100Ω &<br>50Ω  LASER<br>SO- SAFETY<br>3.3V TD- 0.1 μF CIRCUITRY<br>PROTOCOL<br>IC SerDes 2.7 kΩ 2.7 kΩ VccR<br>10 μF 0.1 μF<br>50Ω 0.1 μF<br>SI+<br>RD+<br>100Ω AMPLIFIER<br>50Ω<br>SI- &<br>RD-  PD<br>4.3 kΩ 4.3 kΩ 0.1 μF QUANTIZATION<br>RX_LOS<br>Rx_LOS<br>RX_GND<br>MOD_DEF2<br>SDA<br>MOD_DEF1 CONTROLLER<br>SCL<br>MOD_DEF0<br>MODULE<br>DETECT<br>4.7 kΩ to  4.7 kΩ to  4.7 kΩ to<br>10 kΩ 10 kΩ 10 kΩ<br>3.3V<br>**----- End of picture text -----**<br>


**NOTE:** Refer to the SerDes supplier’s recommendation regarding the interface between the AFBR-57L1APZ and the SerDes. The proposed termination is a general recommendation for LVPECL AC-coupled signals. Other terminations could also be applicable depending on the SerDes interface. 

**Figure 4:  MSA Required Power Supply Filter** 

**AFBR-57L1APZ** 


**----- Start of picture text -----**<br>
Vcc TX<br>1 uH<br>0.1 uF 10 uF*<br>Vcc RX 3.3V<br>1 uH<br>0.1 uF 10 uF 0.1 uF 10 uF<br>**----- End of picture text -----**<br>


**NOTE:** Inductors should have less than a 1Ω series resistor per MSA. *Optional capacitance but recommended (required for SFP+). 

AFBR-57L1APZ-DS102 

Broadcom 

4 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Pin Description** 

|**Pin**|**Name**|**Function/Description**|**MSA Notes**|
|---|---|---|---|
|1|VEET|Transmitter Ground|a|
|2|TX_Fault|Transmitter Fault|—|
|3|Tx Disable|Transmitter Disable – Module disables on high or open|—|
|4|MOD-DEF2|Module Definition 2 – Two-wire serial ID interface – SDA serial data signal|b|
|5|MOD-DEF1|Module Definition 1 – Two-wire serial ID interface – SCL serial clock signal|b|
|6|MOD-DEF0|Module Definition 0 – Grounded in module|b|
|7|NU|Not Used – Open circuit|—|
|8|LOS|Loss of Signal – High indicates loss of signal|c|
|9|VEER|Receiver Ground|a|
|10|VEER|Receiver Ground|a|
|11|VEER|Receiver Ground|a|
|12|RD-|Inverse Received Data Out|d|
|13|RD+|Received Data Out|d|
|14|VEER|Receiver Ground|a|
|15|VCCR|Receiver Power 3.3V|—|
|16|VCCT|Transmitter Power 3.3V|—|
|17|VEET|Transmitter Ground|a|
|18|TD+|Transmitter Data In|e|
|19|TD-|Inverse Transmitter Data In|e|
|20|VEET|Transmitter Ground|a|



- a. Transmitter and receiver grounds are connected in the transceiver PCB. 

- b. Mod-Def 0, 1, 2 are the module definition pins. They should be pulled up with a 4.7-kΩ to 10-kΩ resistor on the host board to a supply less than VCCT + 0.3V or VCCR + 0.3V. To use this interface, supply 3.3V to VCCT. 

   - Mod-Def 0 is grounded by the module to indicate that the module is present. 

   - Mod-Def 1 is the clock line of the two-wire serial interface. 

   - Mod-Def 2 is the data line of the two-wire serial interface. 

- c. LOS (Loss Of Signal) is an open collector/drain output, which should be pulled up externally with a 4.7-kΩ to 10-kΩ resistor on the host board to a supply less than VCCT,R +0.3V. When high, this output indicates that the received optical power is below the worst-case receiver sensitivity (as defined by the standard in use). In the low state, the output is pulled to a voltage less than 0.8V. LOS is valid only if VCCT and VCCR are powered. 

- d. RD-/+: These are the differential receiver outputs. They are AC-coupled to 100Ω differential lines, which should be terminated with 100Ω differential at the SERDES. AC-coupling is present inside the module and is not required on the host board. 

- e. TD-/+: These are the differential transmitter inputs. They are AC-coupled differential lines with 100Ω differential termination inside the module. AC-coupling is present inside the module and is not required on the host board. 

AFBR-57L1APZ-DS102 

Broadcom 

5 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Package Dimensions** 

**Figure 5:  Module Drawing** 




AFBR-57L1APZ-DS102 6 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Figure 6:  SFP Host-Board Mechanical Layout** 




AFBR-57L1APZ-DS102 7 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Figure 7:  SFP Assembly Drawing** 




AFBR-57L1APZ-DS102 8 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Absolute Maximum Ratings** 

Stresses in excess of the absolute maximum ratings can cause catastrophic damage to the device. Limits apply to each parameter in isolation, all other parameters having values within the recommended operation conditions. It should not be assumed that limiting values of more than one parameter can be applied to the product at the same time. Exposure to the absolute maximum ratings for extended periods can adversely affect device reliability. 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|+85|°C|—|
|Supply Voltage|VCC|–0.4|4|V|—|
|Data Input Voltage|VI|–0.5|VCC|V|—|
|Receiver Optical Input Power|Pin|—|0|dBm|—|



## **Recommended Operating Conditions** 

All the data in this specification refers to the following operating conditions and over lifetime unless otherwise stated. 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TC|–40|—|+85|°C|a, b|
|Supply Voltage|VCC|3.1|3.3|3.5|V|a|
|Data Output Load|RL|—|100|—|Ω|Differential|
|Signaling Rate (1.25-Gigabit Ethernet)|B|—|1.25|—|Gbaud|—|



a. The case temperature is measured at the surface of the topside using a thermocouple connected to the housing. 

b. Electrical and optical specifications of the product are guaranteed across recommended case operating temperature only. 

## **Transmitter Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|63|109|mA|—|
|Power Dissipation|PDISS|—|208|382|mW|—|
|Differential Input Voltage|VDIFF|0.4|—|2|V|a|



a. Tx data inputs are AC-coupled. 

AFBR-57L1APZ-DS102 9 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Receiver Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Current|ICC|—|85|115|mA|a|
|Power Dissipation|PDISS|—|280|402|mW|a|
|Data Output: Receiver Differential Output Voltage<br>(RD+/-)||VOH–VOL||0.5|—|1.2|V|b|
|Data Output Rise Time (20%–80%)|Tr|—|—|0.35|ns|—|
|Data Output Fall Time (80%–20%)|Tf|—|—|0.35|ns|—|
|Loss of Signal Output Voltage – Low|LOSVOL|—|—|0.5|V|c|
|Loss of Signal Output Voltage – High|LOSVOH|2.4|—|Vcc|V|c|



a. Typical values are for room temperature at 3.3V. 

b. The differential output voltage is internally AC-coupled. The low and high voltages are measured using 100Ω differential termination. 

c. The RD+ and RD- outputs are squelched at LOS assert/deassert levels. 

## **Transmitter Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Output Optical Power, 62.5/125 μm|Po|–9|—|–1|dBm|a, b|
|Output Optical Power, 50/125 μm|Po|–9|—|–1|dBm|a, b|
|Extinction Ratio|ER|9|—|—|dB|—|
|Central Wavelength|λ|1270|1310|1355|nm|c|
|Spectral Width – FWHM|Δλ|—|—|3|nm|—|
|Optical Rise Time(20%–80%)|Tr|—|—|260|ps|—|
|Optical Fall Time(80%–20%)|Tf|—|—|260|ps|—|
|Output Eye|Compatible with IEEE 802.3z||||||
|Transmitter Total Jitter|TJ|—|—|227|ps|d|
|Transmitter Disable(High)|Po(off)|—|—|–45|dBm|—|



a. Optical values are measured over the specified operating voltage and temperature ranges. The average power can be converted to a peak value by adding 3 dB. 

b. Average. 

c. Maximum deviation across the full temperature range: –40°C to 85°C. 

d. Characterized with a 1.25-Gbaud PRBS7 pattern. 

AFBR-57L1APZ-DS102 

Broadcom 

10 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **Receiver Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Optical Input Power|PIN|–19|—|–1|dBm|a|
|OperatingWavelength|λ|1260|1310|1380|nm|—|
|Signal Detect – Asserted|PA|—|—|–19.0|dBm|—|
|Signal Detect – Deasserted|PD|–35|—|—|dBm|—|



- a. This specification is intended to indicate the performance of the receiver section of the transceiver when optical input power signal characteristics are present per the following definitions: 

   - Over the specified operating temperature and voltage ranges 

   - Bit error rate (BER) better than or equal to 1 × 10[-12] 

   - Over OM1 and OM4 2-km fiber links 

## **Module Diagnostics** 

|**Parameter**|**Range**|**Typ. Accuracy**|**Unit**|**Notes**|
|---|---|---|---|---|
|Temperature|–40 to 85|±3|°C|a, b|
|Voltage|0 to VCC|±0.1|V|c|
|Bias Current|0 to 120|±5|mA|—|
|TX Power|–11 to +1|±3 dB|dBm|—|
|RX Power|–19 to –3|±3 dB|dBm|—|



- a. After case-to-PCB stabilization. Temperature is measured internal to the transceiver. Valid from a –40°C to a +85°C case temperature with Tx Enabled. 

- b. Measured at 3.3V. 

- c. The supply voltage is measured internal to the transceiver and can, with less accuracy, be correlated to the voltage at the SFP VCC pin. 

AFBR-57L1APZ-DS102 11 

Broadcom 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **EEPROM Memory Maps** 

## **A0 Memory Map** 

|**Addr**|**Hex**|**ASCII**|**INFO**|**Addr**|**Hex**|**ASCII**|**INFO**|**Addr**|**Hex**|**ASCII**|**INFO**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|00|03||SFP|28|20|||56|20|||
|01|04|||29|20|||57|20|||
|02|07||LC|30|20|||58|20|||
|03|00|||31|20|||59|20|||
|04|00|||32|20|||60|05||1310 nm|
|05|00|||33|20|||61|1E||1310 nm|
|06|00|||34|20|||62|00|||
|07|22||Longwave<br>Laser<br>Intermediate<br>Distance|35|20|||63|||Notea|
|08|00|||36|00|||64|00|||
|09|0C||50 μm (MM)<br>62.5 μm (MM)|37|00|||65|12|||
|10|00||100 MB/s|38|17|||66|00|||
|11|01||8b/10b|39|6A|||67|00|||
|12|0D||1250 Mb/s|40|41|A||68-83|||Noteb|
|13|00|||41|46|F||84-91|||Notec|
|14|00|||42|42|B||92|68||Noted|
|15|00|||43|52|R||93|D0||Notee|
|16|00|||44|2D|-||94|06||Notef|
|17|C8||2-km OM1|45|35|5||95|||Notea|
|18|C8||2-km OM4|46|37|7||96-127|00||Noteg|
|19|00|||47|4C|L||128-255|00||Noteh|
|20|42|B||48|31|1||||||
|21|52|R||49|41|A||||||
|22|4F|O||50|50|P||||||
|23|41|A||51|5A|Z||||||
|24|44|D||52|20|||||||
|25|43|C||53|20|||||||
|26|4F|O||54|20|||||||
|27|4D|M||55|20|||||||



a. Addresses 63 and 95 are checksums. Address 63 is the checksum for bytes 0-62, and address 95 is the checksum for bytes 64-94. b. Addresses 68-83 specify a unique identifier for each device. 

c. Addresses 84-89 specify the date code (YYMMDD). Addresses 90-91 specify the vendor-specific lot code. 

d. Digital diagnostics implemented. Internally calibrated. Average RX power. 

e. Alarm warnings, SoftTX_Disable, and Soft RX_LOS implemented. 

f. Includes functionality described in Rev 11.3 of SFF-8472. 

g. Addresses 96-127 are vendor specific. 

h. Addresses 128-255 are reserved and are all set to zero. 

AFBR-57L1APZ-DS102 

Broadcom 

12 

**AFBR-57L1APZ** Data Sheet 

1310-nm Multimode SFP Transceiver with Diagnostic Monitoring for 1.25-Gigabit Ethernet 

## **A2 Memory Map** 

|**Byte No.**<br>**(Decimal)**|**Notes**|**Byte No.**<br>**(Decimal)**|**Notes**|**Byte No.**<br>**(Decimal)**|**Notes**|
|---|---|---|---|---|---|
|0|TempH Alarm MSBa|26|Tx Power L Alarm MSBg|104|Real Time Rx Power MSBb|
|1|TempH Alarm LSBa|27|Tx Power L Alarm LSBg|105|Real Time Rx Power LSBb|
|2|TempL Alarm MSBa|28|Tx Power H WarningMSBg|106|Reserved|
|3|TempL Alarm LSBa|29|Tx Power H WarningLSBg|107|Reserved|
|4|TempH WarningMSBa|30|Tx Power L WarningMSBg|108|Reserved|
|5|TempH WarningLSBa|31|Tx Power L WarningLSBg|109|Reserved|
|6|TempL WarningMSBa|32|Rx Power H Alarm MSBb|110|Status/Control|
|7|TempL WarningLSBa|33|Rx Power H Alarm LSBb|111|Reserved|
|8|Vcc H Alarm MSBc|34|Rx Power L Alarm MSBb|112-113|FlagBitsd|
|9|Vcc H Alarm LSBc|35|Rx Power L Alarm LSBb|114|Reserved|
|10|Vcc L Alarm MSBc|36|Rx Power H WarningMSBb|115|Reserved|
|11|Vcc L Alarm LSBc|37|Rx Power H WarningLSBb|116-117|FlagBitsd|
|12|Vcc H WarningMSBc|38|Rx Power L WarningMSBb|118-127|Reserved|
|13|Vcc H WarningLSBc|39|Rx Power L WarningLSBb|128-247|Customer Writable|
|14|Vcc L WarningMSBc|40-55|Reserved|248-255|Vendor Specific|
|15|Vcc L WarningLSBc|56-91|External Calibration Constants|||
|16|Tx Bias H Alarm MSB e|92-94|Reserved|||
|17|Tx Bias H Alarm LSB e|95|Checksum for Bytes 0-94f|||
|18|Tx Bias L Alarm MSBe|96|Real Time Temperature MSBa|||
|19|Tx Bias L Alarm LSBe|97|Real Time Temperature LSBa|||
|20|Tx Bias H WarningMSB e|98|Real Time Vcc MSBc|||
|21|Tx Bias H WarningLSB e|99|Real Time Vcc LSBc|||
|22|Tx Bias L WarningMSBe|100|Real Time Tx Bias MSBe|||
|23|Tx Bias L WarningLSB e|101|Real Time Tx Bias LSBe|||
|24|Tx Power H Alarm MSBg|102|Real Time Tx Power MSBg|||
|25|Tx Power H Alarm LSBg|103|Real Time Tx Power LSBg|||



a. Temperature (Temp) is decoded as a 16-bit signed two’s-complement integer in increments of 1/256°C. 

b. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 μW. 

c. Supply voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 μV. 

d. Addresses 112-113 and 116-117 are used for the TX/RX Alarm and Warning flags. 

e. Tx bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 μA. 

f. Byte 95 is a checksum that is calculated (per SFF-8472) and stored prior to product shipment. 

g. Transmitted average optical power (Tx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 μW. 

AFBR-57L1APZ-DS102 

Broadcom 

13 

Copyright © 2024–2025 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

**Lead (Pb) Free RoHS 6 fully compliant** RoHS 6 fully compliant options available; -xxxE denotes a lead-free product 

