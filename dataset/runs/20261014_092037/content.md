LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC2510-20IN2 Rev1.0- Sep.2016 


## **LS-SC2510-20IN2** 

XGSPON ONU SFP+ Class N2 Transceiver, DOM SC, 9.953G nm 1270TX/ 9.953G 1577nm RX ,SMF 20km Reach 

## **Product Features** 

- Integrated Single fiber bi-directional optical subassembly 

- Symmetric 9.95328Gb/s upstream and downstream bit rate 

- SFP+ metallic package, SC/UPC connector 

- +3.3V single power supply 

- Low power consumption 

- Burst enable :H-active 

- Class 1 Laser eye safety 

- Excellent EMI and EMC characteristics 

- Compliant with RoHS&WEEE 

- Operating case temperature: Standard: 0 to +70°C Industrial: -40 to +85°C 

## **Applications** 

- Asymmetric 10-Gigabit capable passive optical network(XG-PON) system 

## **Description** 

This product is designed for XGSPON transmission. The module incorporates 10Gb/s 1270nm burst-mode transmitter and 10Gb/s 1577nm continuous-mode receiver. An integrated WDM coupler can separate 1577nm input light and 1270nm output light. The metallic package guarantees excellent EMI and EMC characteristics, which totally comply with international relevant standards. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC2510-20IN2 Rev1.0- Sep.2016 


## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Operating Case Temperature|Tc|0||70|°C|Standard|
|||-40||85||Industrial|
|Storage Temperature|Ts|-40||85|°C||
|Operating Relative Humidity|Ho|5||85|%||
|Storage Relative Humidity|Hs|5||95|%||
|Power Supply Voltage|Vcc|3.135|3.3|3.465|V||



## **Optical Characteristics** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|**Transmitter**||||||
|Data Rate||9.953||Gbps||
|Center Wavelength Range|1260||1280|nm||
|Spectral Width(@-20dB)|||1|nm||
|Side Mode Suppression Ratio|30|||dB||
|Launch Optical Power|+4.0||+9.0|dBm||
|Off level light|||-45|dBm||
|Burst turn on/off time|||128|bit||
|TXSD delay time|||1000|ns|1|
|Extinction Ratio|6|||dB|2|
|Transmitter Dispersion Penalty|||1.5|dB|3|
|Transmitter tolerance to reflected<br>optical power|-15|||dB||
|Eye Diagram|Compliant with ITU-T G.987.1|||||
|**Receiver**||||||
|Data Rate||9.953||Gbps||
|Center Wavelength Range|1575||1580|nm||
|Receiver Sensitivity|||-28.0|dBm|3|
|WDM filter isolation|35|||dB||
|Overload Input Optical Power|-8.0|||dBm||
|LOS Optical Dessert|||-29|dB||
|LOS Optical Assert|-44|||dB||
|LOS Hysteresis|0.5||6|dB||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC2510-20IN2 Rev1.0- Sep.2016 


Note: 

1..Measured with PRBS 223-1 test pattern @9.953Gbps. 

2.Transmit on 20km SMF. 

- 3.Measured with PRBS 223-1 test pattern @9.953Gbps with Tx on ER=8.2dB, BER= 10-3 

## **Electrical Characteristics** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Power Consumption|||1.5|W||
|LVPECL Single Ended Data<br>Input Swing|100||800|mV||
|CML Single Ended Data Output Swing|300||500|mV||
|Differential Data input impedance||100||Ω||
|Signal Level(LVTTL)|2.4||Vcc|V||
||0||0.8|V||



## **Pin definition** 

|**Pin No**|**Symbol**|**Description**|**Note**|
|---|---|---|---|
|1|GND_T|Transmitter ground||
|2|TX_FAULT|LVTTL Signal detect output internally pull up||
|3|TX_BRST|LVTTL ransmitter burst mode control, “L”: Tx ON||
|4|SDA|I2C SerialData（LVTTL）||
|5|SCL|I2C SerialClock（LVTTL）||
|6|MOS_ABS|Internally connected GND||
|7|TX-SD|LVTTL Signal detect output, internally pull up||
|8|RX_ LOS|LVTTL Signal detect output, internally pull up||
|9|NC|Not Connected||
|10|GND_R|Receiver ground||
|11|GND_R|Receiver ground||
|12|RD-|CML data output-(AC coupled internally)||
|13|RD+|CML data output+(AC coupled internally)||
|14|GND_R|Receiver ground||
|15|VCC_R|Receiver power supply||
|16|VCC_T|Transmitter power supply||
|17|GND_T|Transmitter ground||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 6 


|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-SC2510-20IN2Rev1.0- Sep.2016|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-SC2510-20IN2Rev1.0- Sep.2016|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-SC2510-20IN2Rev1.0- Sep.2016|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-SC2510-20IN2Rev1.0- Sep.2016|
|---|---|---|---|
|18|TD+|LVPECL Data input+(AC coupled and internal<br>terminated)||
|19|TD-|LVPECL Data input-(AC coupled and internal<br>terminated)||
|20|GND_T|Transmitter ground||



## **TypicalApplication circuit** 


www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC2510-20IN2 Rev1.0- Sep.2016 


## **EEPROM Memory Map** 


## **EEPROM Serial ID Memory Contents** 

The optical transceiver contains an EEPROM. It provides access to sophisticated identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. When the serial protocol is activated, the host generates the serial clock signal (SCL, Mod Def 1). The positive edge clocks data into those segments of the EEPROM that are not writing protected within the SFP transceiver. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

The Module provides diagnostic information about the present operating conditions. The transceiver generates this diagnostic data by digitization of internal analog signals. Calibration and alarm/warning threshold data is written during device manufacture. Received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring all are implemented. The diagnostic data are raw A/D values and must be converted to real world units using calibration constants stored in EEPROM locations 56 – 95 at wire serial bus address A2h. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC2510-20IN2 Rev1.0- Sep.2016 


## **Package Outline** 


Figure 1. Package Outline 

## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LS-SC2510-20CN2|XGSPON ONU SFP+, SC/UPC, 1270Tx/ 1577Rx, 9.953Gbps, SMF 20km, 0°C~+70°C, Class N2|
|LS-SC2510-20IN2|XGSPON ONU SFP+, SC/UPC, 1270Tx/ 1577Rx, 9.953Gbps, SMF 20km, -40°C~+85°C, Class N2|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 6 

