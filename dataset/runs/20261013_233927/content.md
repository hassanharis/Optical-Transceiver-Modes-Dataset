LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


## **LG-SC432G-20IMC1** 

## SFP SC 20km GPON OLT Stick with Mac 2.488Gbps 1490nm TX / 1.244Gbps 1310nm RX 

## **Features** 

- SFP package with SC receptacle 

- Transmitter 1490nm 2.488Gbps with DFB-LD 

- Receiver 1310nm 1.244Gbps with APD-TIA 

- Distance up to 20km 

- Hot pluggable 

- Digital burst RSSI function to monitor the input optical power level 

- Single 3.3V power supply and TTL logic interface 

- Compliant with MSA SFP-8472 

- Compliant with ITU-T G.984.2 

- Compliant with ITU-T G.984.3 

- Maximum support up to 128 subscribers 

- Maximum support up to 1024 TCont 

- Maximum support up to 4096 Gem-Port 

- Support SGMII / HSGMII Uplink with Switch 

- Support IIC / UART configuration for OLT MAC Processing 

- Operating temperature range commercial -40~85°C 

## **Application** 

- Passive Optical Network (PON) 


## **Description** 

The GPON OLT transceiver is packaged of The small form factor pluggable with SC receptacle. digital diagnostic monitoring function is compliant with SFP MSA. 

The module consists of 1490nm DFB Laser, APD detector and WDM filter in a high-integrated optical sub-assembly. It transmits 2.488Gbps at 1490nm, and receives 1.244Gbps at 1310nm in burst mode. 

The Stick OLT PON MAC Processor supports three communication channels, including PLOAM, OMCI and SDU. On the uplink side, the Stick OLT could work in SGMII and HSGMII mode, supporting 2.5Gbps at full duplex. 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 6 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|
|Storage Ambient Temperature|TSTG|-40|85|°C||
|OperatingHumidity|HOPR|5|85|%||
|Power SupplyVoltage|Vcc|-0.5|3.6|V||



## **Recommended Operating Conditioned** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Power Supply Voltage|Vcc|3.135|3.3|3.465|V||
|Power Supply Current|Icc|||800|mA||
|Operating Case Temperature|Tc|-40||85|°C||



## **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Optical Wavelength|λc|1480|1490|1500|nm||
|Data Rate|DR||2.488||Gbps||
|Spectral Width(-20dB)|Δλ|||1|nm||
|Average Output Power|AOP|3|4.5|7|dBm||
|Extinction Ratio|ER|8.2|||dB||
|Average Power of OFF Transmitter||||-39|dBm||
|Transmitter Dispersion Penalty|TDP|||1|dB||
|Optical Eye Diagram|Compliant With ITU-T G984.2||||||
|**Receiver**|||||||
|Receiver Optical wavelength|λc|1260|1310|1360|nm||
|Data Rate|DR||1.244||Gbps||
|Sensitivity|Sen|||-30|dBm|1|
|Overload|Pmax|-12|||dBm|1|
|Burst Mode Dynamic Range||15|||dB||
|Optical Return Loss||||-20|dB||
|LOS De-Asset||||-33|dBm||
|LOS Asset||-45|||dBm||
|LOS Hysteresis||0.5||4|dB||



Note1:Measure with PRBS23, reference bit error ratio 1E-10 . 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 6 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


## **Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|CML Inputs (Differential)|Vin|400||1000|mVpp|AC coupled|
|Input Impedance(Differential)|Zin|90|100|110|ohm||
|Tx_DISABLE Input Voltage High||2||Vcc|V||
|Tx_DISABLE Input Voltage Low||0||0.8|V||
|Tx_FAULT Output Voltage High||2.4||Vcc|V||
|Tx_FAULT Output Voltage Low||0||0.4|V||
|**Receiver**|||||||
|CML Outputs (Differential)|Vout|400||1000|mVpp|AC coupled|
|Output Impedance (Differential)|Zout|90|100|110|ohm||
|Rx LOS Voltage – High||2.4||Vcc|V||
|Rx LOS Voltage – Low||0||0.4|V||



## **Timing Specification** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|TX Disable Assert Time|T_off|||10|us||
|TX Disable Negate Time|T_on|||1|ms||
|Time to initialize, include reset of<br>TX_FAULT|T_int|||300|ms||
|TX_FAULT from fault to assertion|T_fault|||100|us||
|Signal Detect Assert Time||||25.6|ns||
|Signal Detect De-Assert Time||||12.8|ns||
|Guard Time|Tg|25.6|||ns||
|I2C Access Prohibited Time||100||500|us||



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 6 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


## **Digital Diagnostic Monitoring Information** 

|**Parameter**|**Range**|**Accuracy**|**Calibration**|
|---|---|---|---|
|Temperature|0 to 70℃|±3°C|Internal|
||-40 to 85℃|±3°C|Internal|
|Voltage|3.0 to 376V|±3%|Internal|
|Bias Current|0 to 130mA|±10%|Internal|
|TX Power|-10 to 8dBm|±2dB|Internal|
|RX Power|-30 to -8dBm|±2dB|Internal|



## **Digital Diagnostic Memory Map** 


Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 6 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


## **Pin Description** 


|**Pin Num.**|**Name**|**Function**|**Plug seq.**|**Note**|
|---|---|---|---|---|
|1|VeeT|Transmitter Ground|1||
|2|Tx Fault|Transmitter Fault Indication|3|1|
|3|Tx_Burst|Transmitter Disable. Module disables on high or<br>open|3|2|
|4|SDA|2 wire serial ID Interface Data Line|3|1|
|5|SCL|2 wire serial ID Interface Clock|3|1|
|6|MOD_Det|Grounded within the module|3||
|7|TX_SD|Function not available,|3||
|8|LOS|Loss of Signal High: Loss of Signal; Low: Signal<br>Detect|3|3|
|9|VeeR|Receiver Ground|1|1|
|10|VeeR|Receiver Ground|1||
|11|VeeR|Receiver Ground|1||
|12|RD-|Received inverted DATA out. AC Coupled.|3||
|13|RD+|Received DATA out. AC Coupled.|3||
|14|VeeR|Receiver Ground|1||
|15|VccR|Receiver Power. 3.3V±5%.|2||
|16|VccT|Transmitter Power. 3.3V±5%.|2||
|17|VeeT|Transmitter Ground|1||
|18|TD+|Transmit DATA in. AC Coupled.|3||
|19|TD-|Transmit Inverted DATA in. AC Coupled.|3||
|20|VeeT|Transmitter Ground|1||



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 6 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LG-SC432G-20IMC1 Rev1.0- Sep.2016 


Plug Seq.: Pin engagement sequence during hot plugging. 

Note 1: The pin should be pulled up with a 4.7K – 10KΩ resistor on the host board. 

Note 2: The pin is pulled up with a 4.7K – 10KΩ resistor in the module. Note 3: The pin is pulled down with 100KΩ resistor in the module. 

## **Package Outline** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LG-SC341G-20IMB1|GPON ONU,SC,TX1310nm/RX1490nm,TX1.25G/RX2.5G,20km,-40~85℃,with MAC,Class B+|
|LG-SC432G-20IMC1|GPON OLT,SC,TX1490nm/RX1310nm,TX2.5G/RX1.25G,20km,-40~85℃,with MAC,Class C+|



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 6 

www.link-pp.com 

