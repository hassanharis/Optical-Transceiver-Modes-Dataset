LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


## **LQD-M31400-DR4C** 400G QSFP-DD DR4 Transceiver 

## **Product Features** 

- Compliant with IEEE Std 802.3bs 

- Compliant with 400G-DR4 optical specifications 

- Compliant with QSFP-DD MSA 

- Compliant with CMIS4.0 Management interface specifications 

- 8x53.125Gb/s electrical interface (400GAUI-8) 

- Up to 0.5km transmission on single mode fiber (SMF) with FEC 

- Single +3.3V power supply 

- Case temperature range: 0 ~ +70℃ 

- Maximum power consumption 9.5W 

- RoHS complaint 

## **Applications** 

- 400G Ethernet 

- Data Center Interconnect 

- Infiniband Interconnect 

- Enterprise Networking 

## **Standards** 

- IEEE 802.3cd 

- QSFP-DD MSA 

- CMIS4.0 

## **Descriptions** 

LQD-M31400-DR4C is a transceiver module designed for 500m optical communication applications, and it is compliant to 100G Lambda MSA standard. This module can convert 8-channel 53.125Gb/s electrical data to 4- channel 106.25Gb/s optical signals, and multiplex them into a single channel for 425Gb/s optical transmission. Similarly, it optically de-multiplexes a 425Gb/s input into 4-channel signals, and converts them to 8-channel output electrical data on the receiver side. It has been designed to meet the harshest external operating conditions including temperature, humidity and EMI interference. The module offers very high functionality and feature integration, accessible via a two-wire serial interface. 

> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 1 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


## **Absolute Maximum Ratings** 

It has to be noted that the operation in excess of any individual absolute maximum ratings might cause permanent damage to this module. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|Storage Temperature Range|TSTG|-40|+85|⁰C|
|SupplyVoltage|VCC|0|4|V|
|Relative Humidity|RH|10% to 90% non-condensing|||



## **Recommended Operating Conditions** 

Electrical and optical characteristics below are defined under this operating environment, unless otherwise specified. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|Case Temperature- Operating|TCASE|0|70|⁰C|
|SupplyVoltage|Vcc|3.14|3.46|V|
|Pre-FEC Bit Error Ratio|||2.4x10-4||
|Post-FEC Bit Error Ratio|||1x10-12||
|Link Distance||2|500|M|
|Instantaneous peak current at hot plug|ICC_IP||4000|mA|
|Sustained peak current at hot plug|ICC_SP||3300|mA|
|Power Consumption|PDISS||10|W|
|Maximum Power Dissipation, Low Power<br>Mode|PDLP||1.5|W|



## **Transmitter Optical Specifications** 

||**Transmitter Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Units**||
|---|---|---|---|---|---|---|---|
||Lane Wavelength Range|λC|1290||1320|nm||
||Modulation Format||PAM4|||||
||Average Optical Power per lane|AOPL|-3.2||4.4|dBm||
||Outer Optical Modulation<br>Amplitude(OMAouter), each lane|TOMA|||3.7|dBm||
||Outer Optical Modulation Amplitude (OMAouter)<br>each lane:for TDECQ <1.4dB<br>for 1.4≤TDECQ≤3.4dB|TOMA|-0.2<br>-1.6+TDECQ|||||
||Difference in launch power between any two lanes<br>(OMAouter)|DP|||3.9|dB||
||Transmitter and Dispersion Eye Closure for PAM4|TDECQ|||3.4|dB||



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2021 LINK-PP AlI Rights Reserved Page 2 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||||||
|---|---|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LQD-M31400-DR4C Rev1.0- Sep.2021||||||||
||(TDECQ), each lane|||||||
||Transmitter eye closure for PAM4(TECQ)|TECQ|||3.4|dB||
||| TDECQ - TECQ |||||2.5|dB||
||Over/under-shoot||||22|%||
||Transmitter power excursion||||1.8|dBm||
||Average Launch Power of OFF Transmitter, each lane|TOFF|||-16|dBm||
||Extinction Ratio, each lane|ER|3.5|||dB||
||Transmitter transition time||||17|ps||
||Optical Return Loss Tolerance|ORL|||17.1|dB||
||Transmitter Reflectance|TR|||-26|dB||



|**Receiver Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|
|Lane Wavelength Range|λC|1290||1320|nm|
|Damage Threshold, each lane|AOPD|5.4|||dBm|
|Average Receive Power, each lane|AOPR|-7.2||4.4|dBm|
|Receive Power (OMAouter), each lane|OMAR|||3.7|dBm|
|Difference in receive power between any two lanes<br>(OMAouter)|DR|||4.1|dB|
|Receiver Reflectance|RR|||-26|dB|
|Receiver Sensitivity (OMAouter), each lane<br>for TECQ<1.4dB for 1.4≤TECQ≤3.4dB|SOMA|||-4.6<br>-6+TECQ|dBm|
|Stressed Receiver Sensitivity (OMAouter), each lane|SRS|||-2.6|dBm|
|Conditions of stressed receiver sensitivity test||||||
|Stressed eye closure for PAM4 (SECQ)|||3.4||dB|
|OMAouter of each aggressor lane|||1.4||dBm|



## **High Speed Electrical Specifications** 

|**Parameter**|**Min**|**Typical**|**Max**|**Units**|**Notes**|
|---|---|---|---|---|---|
|**Receiver electrical output characteristics at TP4**||||||
|Signalingrateper lane||26.5625||GBd||
|AC common-mode output voltage(RMS)||-|17.5|mV||
|Differentialpeak-to-peak output voltage|||900|mV||
|Near-end ESMW(Eye symmetrymask width)||0.265||UI||
|Near-end Eye height,differential|70|||mV||
|Far-end ESMW(Eye symmetrymask width)||0.2||UI||
|Far-end Eye height,differential|30|||mV||
|Far-endpre-cursor ISI ratio|-4.5||2.5|%||



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 3 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


|Differential termination mismatch|||10|%||
|---|---|---|---|---|---|
|Transition time(min,20% to 80%)|9.5|||ps||
|DC common mode voltage|-350||2850|mV||
|**Transmitter electrical input characteristics at TP1**||||||
|Signalingrate, per lane||26.5625||GBd||
|Differentialpk-pk input voltage tolerance|900|||mV||
|Differential termination mismatch|||10|%||
|Module stressed input test|Per Section<br>120E.3.4.1,IEEE80<br>2.3bs|||||
|Single-ended voltage tolerance range|-0.4||3.3|V||
|Common-mode voltage|-350||2850|mV||



## **Receiver Output Power Thresholds for Loss of Signal (LOS)** 

|**Parameter**|**Min**|**Typical**<br>**Max**|**Typical**<br>**Max**|**Units**|
|---|---|---|---|---|
|RX_LOS_Assert Min/Max|-15.0|||dBm|
|RX_LOS_De-Assert Min/Max|||-8.9|dBm|
|RX_LOS_Hysteresis||1.5||dB|



## **Digital Diagnostic Monitoring Specifications** 

|**Parameter**|**Unit**|**Specification**|
|---|---|---|
|Temperature Monitor absolute error|degC|± 3|
|Voltage Monitor absolute error|%|± 5|
|I_bias Monitor absolute error|%|± 10|
|TransmitPower(Tx)Monitorabsoluteerror|dB|± 3.0|
|ReceivedPower(Rx)Monitorabsoluteerror|dB|± 3.0|



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 4 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


## **QSFP-DD Edge Connector and Pinout Description** 

The electrical pinout of the QSFP-DD module is shown in Figure 2 below. 



Figure 1. Host PCB QSFP-DD pad assignment top view 

||**Pin No.**|**Symbol**|**Description**|**Note**||
|---|---|---|---|---|---|
||1|GND|Ground|1||
||2|Tx2n|Transmitter Inverted Data Input|||
||3|Tx2p|Transmitter Non-Inverted Data output|||



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 5 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQD-M31400-DR4C Rev1.0- Sep.2021 

||4|GND|Ground|1||
|---|---|---|---|---|---|
||5|Tx4n|Transmitter Inverted Data Input|||
||6|Tx4p|Transmitter Non-Inverted Data output|||
||7|GND|Ground|1||
||8|ModSelL|Module Select|||
||9|ResetL|Module Reset|||
||10|VccRx|3.3V Power SupplyReceiver|2||
||11|SCL|2-Wire serial Interface Clock|||
||12|SDA|2-Wire serial Interface Data|||
||13|GND|Ground|1||
||14|Rx3p|Receiver Non-Inverted Data Output|||
||15|Rx3n|Receiver Inverted Data Output|||
||16|GND|Ground|1||
||17|Rx1p|Receiver Non-Inverted Data Output|||
||18|Rx1n|Receiver Inverted Data Output|||
||19|GND|Ground|1||
||20|GND|Ground|1||
||21|Rx2n|Receiver Inverted Data Output|||
||22|Rx2p|Receiver Non-Inverted Data Output|||
||23|GND|Ground|1||
||24|Rx4n|Receiver Inverted Data Output|||
||25|Rx4p|Receiver Non-Inverted Data Output|||
||26|GND|Ground|1||
||27|ModPrsL|Module Present|||
||28|IntL|Interrupt|||
||29|VccTx|3.3Vpower supplytransmitter|2||
||30|Vcc1|3.3Vpower supply|2||
||31|Init Mode|Initialization mode|||
||32|GND|Ground|1||
||33|Tx3p|Transmitter Non-Inverted Data Input|||
||34|Tx3n|Transmitter Inverted Data Output|||
||35|GND|Ground|1||
||36|Tx1p|Transmitter Non-Inverted Data Input|||
||37|Tx1n|Transmitter Inverted Data Output|||
||38|GND|Ground|1||
||39|GND|Ground|1||
||40|Tx6n|Transmitter Inverted Data Input|||
||41|Tx6p|Transmitter Non-Inverted Data output|||
||42|GND|Ground|1||
||43|Tx8n|Transmitter Inverted Data Input|||



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 6 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||||
|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LQD-M31400-DR4C Rev1.0- Sep.2021||||||
||44|Tx8p|Transmitter Non-Inverted Data output|||
||45|GND|Ground|1||
||46|Reserved|For Future Use|3||
||47|VS1|Module Vendor Specific 1|3||
||48|VccRx1|3.3V Power Supply|2||
||49|VS2|Module Vendor Specific 2|3||
||50|VS3|Module Vendor Specific 3|3||
||51|GND|Ground|1||
||52|Rx7p|Receiver Non-Inverted Data Output|||
||53|Rx7n|Receiver Inverted Data Output|||
||54|GND|Ground|1||
||55|Rx5p|Receiver Non-Inverted Data Output|||
||56|Rx5n|Receiver Inverted Data Output|||
||57|GND|Ground|1||
||58|GND|Ground|1||
||59|Rx6n|Receiver Inverted Data Output|||
||60|Rx6p|Receiver Non-Inverted Data Output|||
||61|GND|Ground|1||
||62|Rx8n|Receiver Inverted Data Output|||
||63|Rx8p|Receiver Non-Inverted Data Output|||
||64|GND|Ground|1||
||65|NC|No Connect|3||
||66|Reserved|For Future Use|3||
||67|VccTx1|3.3Vpower supply|2||
||68|Vcc2|3.3Vpower supply|2||
||69|Reserved|For Future Use|3||
||70|GND|Ground|1||
||71|Tx7p|Transmitter Non-Inverted Data Input|||
||72|Tx7n|Transmitter Inverted Data Output|||
||73|GND|Ground|1||
||74|Tx5p|Transmitter Non-Inverted Data Input|||
||75|Tx5n|Transmitter Inverted Data Output|||
||76|GND|Ground|1||



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 7 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


## **Module Block Diagram** 


Figure 2. Module Block Diagram 

> **ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 8 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-M31400-DR4C Rev1.0- Sep.2021 


## **Mechanical Specifications** 

Pull tab color: Blue Panon:30 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LQ4-M31400-DR4C|400Gbps，QSFP56-DD，DR4，500m，0°C~+70°C，with DDM,MPO-12 connector|



> **ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 9 of 9 

