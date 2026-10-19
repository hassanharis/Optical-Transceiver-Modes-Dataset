LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC5210-20CN1 Rev1.0- Sep.2016 


## **LS-SC5210-20CN1** 

XGSPON OLT SFP+ Class N1 Transceiver, DOM SC, 9.953G 1577nm TX/ 9.953G 1270nm RX ,SMF 20km Reach 

## **Product Features** 

- SFP+ package with SC receptacle optical interface compliant 

- Single fiber bi-directional data links with 

- 9.953Gbps downstream and 9.953Gbps/2.488Gbps upstream 

- 1577nm continuous-mode transmitter with EML laser 

- 1270nm burst-mode receiver with APD-TIA 

- 2-wire interface for integrated digital diagnostic Monitoring 

- Hot - P l ug ga b le 

- +3.3V power supplies 

- Compliant with RoHS&WEEE, SFP MSA, SFF 8472, ITU-T G.9807.1 

- Excellent EMI and EMC characteristics 

- Operating case temperature: Standard: 0 to +70°C Industrial: -40 to +85°C 

## **Applications** 

- Access Network 

## **Description** 


This product is designed for OLT module based on XGSPON N1 technology. The product is an integrated module containing a micro-optic component and semiconductor material. The module could implement DDM function. It could be used at key locations in optical networks. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC5210-20CN1 Rev1.0- Sep.2016 


## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Operating Case Temperature|Tc|0||70|°C|Standard|
|||-40||85||Industrial|
|Storage Temperature|Ts|-40||85|°C||
|Operating Relative Humidity|Ho|5||85|%||
|Storage Relative Humidity|Hs|5||90|%||
|Power Supply Voltage|Vcc|3.135|3.3|3.465|V||



## **Optical Characteristics** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|**Transmitter(9.953G)**||||||
|Data Rate|-|9953.28|-|Mbps||
|Center Wavelength Range|1575|-|1580|nm||
|Spectral Width(@-20dB)|-|-|1|nm||
|Launch Optical Power|+2|-|+5|dBm||
|Pout @TX-Disable Asserted|||-39|dBm||
|Extinction Ratio|8.2|-|-|dB|1|
|Transmitter dispersion penalty|-|-|1|dB|2|
|Eye Diagram|Compliant with ITU-TG.987.2|||||
|**Receiver(9.953G)**||||||
|Data Rate|-|9953.28|-|Mbps||
|Center Wavelength Range|1260|1270|1280|nm||
|Receiver Sensitivity|-|-|-26|dBm|3|
|Overload Input Optical Power|-5|||dBm||
|LOS Optical Dessert|-|-|-27|dB||
|LOS Optical Assert|-45|-|-|||
|LOS Hysteresis|0.5|-|6|dB||
|**Receiver(2.488G)**||||||
|Data Rate|-|2488.32|-|Mbps||
|Center Wavelength Range|1260|1270|1280|nm||
|Receiver Sensitivity||-|-27.5||4|
|Overload Input Optical Power|-7|||||
|LOS Optical Dessert|-|-|-28.5|||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||||
|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-SC5210-20CN1Rev1.0- Sep.2016||||||
|LOS Optical Assert|-45|-|-|||
|LOS Hysteresis|0.5|-|6|||



Notes: 

1. Measured with PRBS 2^-31-1 test pattern @9.95328Gbps . 

2. Transmit on 20km SMF. 

3 . Measured with PR BS 2 ^ 3 1 - 1 test pattern @ 9 . 9 5 3 Gb ps , BER = 1 0 ^ - 3 . 4 . Measured with PRBS 2 ^ 2 3 - 1 test pattern @ 2 . 4 8 8 3 2 Gbps, BER = 1 0 ^ - 4 . 

## **Electrical Characteristics** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Power Consumption|-|-|2.5|W||
|CML Signal Differential Data Input Swing|100|-|800|mV||
|CML Single Differential Data Output Swing|600||1000|mV||
|Differential Data input impedance|-|100|-|Ω||
|Signal Level (LVTTL)|2.4|-|Vcc|V||
|Signal Level (LVTTL)|0|-|0.8|V||



## **Pin definition** 

|**Pin No**|**Symbol**|**Description**|**Note**|
|---|---|---|---|
|1|GND_T|Transmitter ground||
|2|TX_FAULT|LVTTL Signal detect output internally pull up||
|3|TXDisable|Transmitter Disable|1|
|4|SDA|I2C SerialData（LVTTL）||
|5|SCL|I2C SerialClock（LVTTL）||
|6|MOS_ABS|Internally connected GND||
|7|RESET|RXReset (LVTTL)||
|8|RX_ SD|LVTTL Signal detect output, internally pull up|2|
|9|RSSI TRIG|RSSI TRIG Receiver RSSI trigger input|3|
|10|GND_R|Receiver ground||
|11|10GND_R|Receiver ground||
|12|RD-|CML data output-(DC coupled and internal<br>terminated)||
|13|RD+|8CML data output+(DC coupled and internal<br>terminated)||
|14|GND_R|Receiver ground||
|15|VCC_R|Receiver power supply||
|16|VCC_T|Transmitter power supply||



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LS-SC5210-20CN1 Rev1.0- Sep.2016 

|17|GND_T|Transmitter ground||
|---|---|---|---|
|18|TD+|LVPECL Data input+ (AC coupled and internal<br>terminated)||
|19|TD-|LVPECL Data input- (AC coupled and internal<br>terminated)||
|20|GND_T|Transmitter ground||



Note : 

- 1.TX Disable input is used to shut down both the 10G laser and 1G laser (if module has 1G transmitter) output per the state table below. It is pulled up within the module with a 4.7 – 10K resistor. 

Low (<0.8V):Transmitter on 

High (>2.0 V):Transmitter Disabled 

Open :Transmitter Disabled 

2.SD (signal Detect) is an open collector/drain output which should be pulled up externally with a 4.7 – 10K resistor on the host board to supply <VccT+0.3V or VccR+0.3V. When low, this output indicates the received optical power is below the worst case receiver sensitivity. High indicates normal operation. In the low state, the output will be pulled to <0.8V. 

3. RX_RSSI_TRIG is used to start a RX Power Monitoring. It is pulled high to trigger a A/D sample start. 

## **TypicalApplication circuit** 


www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC5210-20CN1 Rev1.0- Sep.2016 


## **EEPROM Memory Map** 


## **EEPROM Serial ID Memory Contents** 

The optical transceiver contains an EEPROM. It provides access to sophisticated identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. When the serial protocol is activated, the host generates the serial clock signal (SCL, Mod Def 1). The positive edge clocks data into those segments of the EEPROM that are not writing protected within the SFP transceiver. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

The Module provides diagnostic information about the present operating conditions. The transceiver generates this diagnostic data by digitization of internal analog signals. Calibration and alarm/warning threshold data is written during device manufacture. Received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring all are implemented. The diagnostic data are raw A/D values and must be converted to real world units using calibration constants stored in EEPROM locations 56 – 95 at wire serial bus address A2h. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SC5210-20CN1 Rev1.0- Sep.2016 


## **Package Outline** 


Figure 1. Package Outline 

## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LG-SC5210-20CN1|XGSPON OLT SFP+, SC, 1577Tx/1270Rx, 9.953Gbps, SMF 20km, 0°C~+70°C, Class N1|
|LG-SC5210-20IN1|XGSPON OLT SFP+, SC, 1577Tx/1270Rx, 9.953Gbps, SMF 20km, -40°C~+85°C, Class N1|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 6 

