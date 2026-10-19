LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **LS-BL302925-60C** 

## 25.78Gbps SFP28 LC BIDI Tx1309nm/Rx1295nm 60km Transceiver 

## **Product Feature** 

- All metal housing for superior EMI performance 

- Support 25GE and CPRI, data rate up to 25.78125Gbps 

- Link distance up to 40km single mode fiber without FEC Link 

- Distance up to 60km single mode fiber with FEC 

- 1295nm EML Transmitter and APD receiver for LS-BL293025-60x 1309nm EML Transmitter and APD receiver for LS-BL302925-60x 

- Low DC power consumption : 

- Commercial : <1.6W Industrial : <1.8W 

- High speed I/O electrical interface 

- I2C interface with integrated Digital Diagnostic monitoring 

- RoHS 6 compliance 

- Compliant to IEEE 802.3cc, SFF-8402 and SFF-8419 

- Complies with EU Directive 2015/863/EU 

- Case Operating temperature ranges: 

- Commercial : 0 °C to 70 °C 

- Industrial : -40 °C to 85 °C 

## **Applications** 

- 25G Ethernet 

- Data center 

## **Standard** 

- Compliant to SFP28 MSA 

- Compliant with IEEE 802.3cc 


- Compliant with SFF-8432,SFF-8472 

- RoHS complaint 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Product Description** 

The SFP28 BIDI optical Transceiver integrates receiver and transmitter path on one module. In the transmit side, one of serial data streams are recovered, retimed, and passed to laser driver. In the receive side, the optical data streams is recovered by a APD and trans-impedance amplifier, retimed. This module features a hot-pluggable electrical interface, low power consumption. 

The product is designed with form factor, optical/electrical connection and digital diagnostic interface according to the SFP28 and compliant to IEEE 802.3cc. 

## **Pin Assignment** 


Diagram of Host Board Connector Block Pin Numbers and Names 

## **Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Description**|**Note**|
|---|---|---|---|
|1|VeeT|Transmitter Ground|1|
|2|Tx_Fault|Transmitter Fault - High indicates a fault condition|2|
|3|Tx_Disable|Transmitter Disable – High or open disables the transmitter||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||
|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-BL302925-60C Rev1.0- Sep.2025||||
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|3|
|5|SCL|2-wire Serial Interface Clock (MOD-DEF1)|3|
|6|MOD_ABS|Module Absent, connected to VeeT or VeeR in the module||
|7|RS0|Rate Select 0|5|
|8|RX_LOS|Receiver Loss of Signal(LVTTL-O). Logic 0 indicates normal operation|4|
|9|RS1|Rate Select 1|5|
|10|VeeR|Receiver Ground|1|
|11|VeeR|Receiver Ground|1|
|12|RD-|Inverse Received Data out (CML-O), AC Coupled||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled||
|14|VeeR|Receiver Ground|1|
|15|VccR|Receiver Power Supply||
|16|VccT|Transmitter Power Supply||
|17|VeeT|Transmitter Ground|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VeeT|Transmitter Ground|1|



Notes: 

1. Module ground pins GND are isolated from the module case. 

2. Tx_Fault is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on Host board. 

3. Should be pulled up with 4.7k–10kohms on host board to a voltage between 2.0V and 3.6V. 

4. LOS is open collector output. Should be pulled up with 4.7k–10kohms on host board to a voltage between 2.0V and 3.6V. 

5. RS0 and RS1 pins are pulled low to GND with a resistor > 30KΩ in module. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40||+85|°C||
|Relative Humidity|RH|0||95|%||
|Power Supply Voltage|VCC|0||+3.6|V||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|TA|0||70|°C|Commercial|
|||-40||85|°C|Industrial|
|Power Supply Voltage|VCC|3.15|3.3|3.46|V||
|Power Supply Current|ICC|||480|mA|Commercial|
|||||540|mA|Industrial|



## **Electrical Characteristics** 

High-Speed Signal: Compliant to CEI-28G-VSR 

## Low-Speed Signal: Compliant to SFF-8419 

|**Parameter**|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|---|
|**Transmitter**||||||||
|Differential Data Input Amplitude||VIN,P-P|||900|mVpp||
|Differential Impedance|||90|100|110|Ω||
|Tx_Disable|Normal<br>Operation|VIL|-0.3||0.8|V||
||Laser Disable|VIH|2.0||VCC+0.3|V||
|**Receiver**||||||||
|Differential Data Output Amplitude||VOUT,P-P|||900|mVpp||
|Differential Termination<br>Mismatch(1MHZ）|||||10|%||
|Differential Impedance|||90|100|110|Ω||
|Rx_LOS|Normal<br>Operation|VOL|-0.3||0.4|V||
||Loss Signal|VOH|2||VCCHOST|V||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|||**Transmitter**|||||
|Optical<br>Modulation<br>Amplitude(OMA)|POMA|2||6|dBm||
|Average Output Power|POUT|1||6|dBm||
|Average Output Power(Laser<br>Off)|POFF|||-30|dBm||
|Center Wavelength|λc|1281|1295|1297|nm|LS-BL293025-60x|
|||1306|1309|1322|nm|LS-BL302925-60x|
|SpectrumBandwidth @ -20dB|Δλ|||1|nm||
|Side<br>mode<br>suppression<br>ratio(SMSR)|SMSR|30|||dB||
|Extinction ratio|ER|4|||dB||
|Transmitter<br>and<br>dispersion<br>penalty(TDP)||||2.7|dB||
|RIN20OMA|RIN|||-130|dB/Hz||
|Transmitter Reflectance (max)|TFL|||-26|dB||
|||**Receiver**|||||
|Input Optical Wavelength|λC|1306|1309|1322|nm|LS-BL293025-60x|
|||1281|1295|1297|nm|LS-BL302925-60x|
|Receiver sensitivity<br>(OMA)(40km)|RSEN-OMA|||-19|dBm|40km NO FEC|
|Receiver sensitivity<br>(OMA)(60km)|RSEN-OMA|||-21|dBm|60km With FEC|
|Optical Power Overload|PIN(SAT)|-4|||dBm||
|Rx_LOS of Signal Assert|PA|-35|||dBm||
|Rx_LOS of Signal De-assert|PD|||-21|dBm||
|Rx_LOS of Signal Hysteresis|PHy|0.5||5|dB||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Digital Diagnostic Monitoring Interface** 

Five transceiver parameter values are monitored. The following table defines the monitored parameter’s accuracy. 

|**Parameter**|**Range**|**Accuracy**|**Calibratiom**|
|---|---|---|---|
|Temperature|0 to +70°C (C)|±3°C|Internal|
||-40 to +85°C (I)|||
|Voltage|3.13 to 3.47V|±5%|Internal|
|Bias Current|0 to 100mA|±10%|Internal|
|TX Power|0 to +6dBm|±3dBm|Internal|
|RX Power|-21 to -4dBm|±3dBm|Internal|



## **EEPROM Information** 

EEPROM memory map specific data field description is as below: 


www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Recommend Circuit Schematic** 


www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-BL302925-60C Rev1.0- Sep.2025 


## **Mechanical Specifications** 


## **Ordering information** 

|**PN**|**Description**|
|---|---|
|LS-BL293025-60C|SFP28, 25.78G, Tx1295nm/Rx1309nm, 60km, 0℃-70℃|
|LS-BL293025-60I|SFP28, 25.78G, Tx1295nm/Rx1309nm, 60km, -40℃-85℃|
|LS-BL302925-60C|SFP28, 25.78G, Tx1309nm/Rx1295nm, 60km, 0℃-70℃|
|LS-BL302925-60I|SFP28, 25.78G, Tx1309nm/Rx1295nm, 60km, -40℃-85℃|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 8 of 8 

