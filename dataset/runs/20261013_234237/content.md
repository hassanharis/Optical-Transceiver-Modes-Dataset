LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


## **LO-DM31800-DR8C** 

## 800GBASE-DR8 OSFP 1310nm 500m Dual MPO-12/APC IHS / Closed top with heat sink Transceiver 

## **Features** 

- Compliant with IEEE 802.3cu-2021: 

   - -2x400GBASE-DR4 optical interface 

- Compliant with IEEE P802.3ck D2.2 

   - -2x400GAUI-4 C2M electrical interface 

- Compliant with OSFP MSA HW Rev 4.1 Type 2 housing with Dual MPO-12 connector 

- Compliant with CMIS Rev 5.0 

- Maximum Power Consumption 16w 

- Operating Temperature Range: 0℃ ~ +70 ℃ 

- Two Wire Serial Interface with Digital Diagnostic Monitoring 

- Class 1 Laser Safety 


## **Applications** 

- 800G Ethernet 

- 2x 400GBASE-DR4 

- Data Center 

- Cloud Networks 

## **Description** 

The LO-DM31800-DR8C OSFP transceiver supports up to 500m link lengths over single-mode fiber (SMF) via dual MTP/MPO-12 connectors. This transceiver is compliant with IEE802.3ck, IEEE 802.3cu and OSFP MSA standards. The built-in digital diagnostics monitoring (DDM) allows access to real-time operating parameters. It is suitable for 800G Ethernet, Breakout 2x 400G DR4, Data Center and Cloud Networks. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|StorageTemperature Range|TS|-40||85|ºC||
|SupplyVoltage|VCC|-0.5||3.6|V||
|Relative Humidity(non-condensing)|RH|5||95|%||
|DataInputVoltage Differential|lVDIP-VDI|||1|V||
|ControlInput Voltage|VI|-0.3||VCC+0.5|V||
|ControlOutput Current|IO|-20||20|mA||



## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|OperatingCase Temperature|TOPR|0||70|ºC||
|PowerSupply Voltage|VCC|3.135|3.3|3.465|V||
|MaximumPower Dissipation|PD|||16|W||
|SignallingSpeed perLane|DRL||53.125||GBd||
|ControlInputVoltage High|VIH|VCC*0.7||VCC+0.3|V||
|ControlInput VoltageLow|VIL|-0.3||VCC*0.3|V||
|TwoWire Serial Interface ClockRate||||400|kHz||
|PowerSupply Noise 1 kHz - 1 MHz (p-p)||||66|mVpp||
|Operating Distance||2||500|m||



## **Optical Characteristic** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter(Per Lane)**|||||||
|Wavelength|λ|1304.5|1311|1317.5|nm||
|Side Mode Suppression Ratio|SMSR|30|||dB||
|Average Launch Power, each lane|AOPL|-2.9||4.0|dBm|1|
|OuterOptical Modulation Amplitude<br>(OMAouter), each Lane|TOMA|-0.8||4.2|dBm||
|Launch Powerin OMAouter minus|TOMA-TD|-2.2|||dBm||
|TransmitterandDispersion Eye Closurefor<br>PAM4(TDECQ),each lane|TDECQ|||3.4|dB||
|AverageLaunch Powerof OFF Transmitter,<br>each lane|TOFF|||-15|dBm||
|Extinction Ratio|ER|3.5|||dB||
|Transmittertransition time (max)|Tr|||17|ps||
|RIN21.4OMA (max)|RIN|||-136|dB/Hz||
|OpticalReturn LossTolerance|ORL|||21.4|dB||
|Transmitter Reflectance|TR|||-26|dB|2|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


|**Receiver(Per Lane)**|**Receiver(Per Lane)**|**Receiver(Per Lane)**|**Receiver(Per Lane)**|**Receiver(Per Lane)**|**Receiver(Per Lane)**|**Receiver(Per Lane)**|
|---|---|---|---|---|---|---|
|Wavelength|λ|1304.5|1311|1317.5|nm||
|Damage Threshold, each Lane|AOPD|5|||dBm||
|Average ReceivePower, each Lane|AOPR|-5.9||4|dBm||
|Receive Power(OMAouter), each|OMAR|||4.2|dBm||
|ReceiverReflectance|RR|||-26|dB||
|ReceiverSensitivity(OMAouter), each<br>Lane|SOMA|||Max(–3.9,<br>SECQ – 5.3)|dBm|3|
|Stressed Receiver Sensitivity(OMAouter), each|SRS|||-1.9|dBm|4|
|**Conditions of stressed receiver sensitivity test**|||||||
|Stressedeye closure forPAM4 (SECQ),<br>laneunder test|SECQ||3.4||dB||
|OMAouterofeach aggressorlane|||4.2||||



## **Notes:** 

- 1: Average launch power, each lane (min) is informative and not the principal indicator of signal strength 

- 2: Transmitter reflectance is defined looking into the transmitter 

- 3.Receiver sensitivity (OMAouter), each lane (max) is informative and is defined for a transmitter with a value of SECQ up to 3.4 dB. 

4. Measured with conformance test signal at TP3 for the BER = 2.4x10 -4 

## **Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter(per Lane)**|||||||
|ACcommon-modeoutput Voltage (RMS)||||25|mV||
|Differential peak-to-peak outputvoltage<br>Shortmode<br>Longmode||||600<br>900|mV<br>mV||
|Eye height, differential|EH|15|||mV||
|Verticaleye closure|VEC|||12|dB||
|Common-modeto differentialreturn loss|RLDc|802.3ck120G-1|||dB||
|Effective return loss, ERL|ERL|8.5|||dB||
|Differentialtermination mismatch||||10|%||
|Transitiontime (20% to 80%)||8.5|||ps||
|**Receiver (per Lane)**|||||||
|Differentialpk-pkinputVoltage tolerance||900|||mV||
|AC common-modeRMS voltage tolerance(TP1a)||25|||mV||
|Differentialto common-modereturn loss|RLcd|802.3ck120G-2|||dB||
|Effective return loss, ERL|ERL|8.5|||dB||
|Differentialtermination mismatch||||10|%||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


|Single-ended voltage tolerance range||-0.4||3.3|V||
|---|---|---|---|---|---|---|
|DCcommon-mode Voltage||-0.35||2.85|V||



## **Low Speed Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|
|ModuleoutputSCL andSDA|VOL|0|0.4|V||
|Module InputSCL and SDA|VIL|-0.3|VCC*0.3|V||
||VIH|VCC*0.7|VCC+0.5|V||
|LPMode/TxDis,ResetL and ModSelL|VIL|-0.3|0.8|V||
||VIH|2|VCC+0.3|V||
|IntL/RxLos|VOL|0|0.4|V||
||VOH|VCC-0.5|VCC+0.3|V||



## **Pin Map and Description** 


**Figure 1. MSA Compliant Connector** 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


|**Pin#**|**Symbol**|**Description**|**Logic**|**Direction**|**Plug**|
|---|---|---|---|---|---|
|1|GND||Ground||1|
|2|TX2p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|3|TX2n|Transmitter Data Inverted|CML-I|Input from Host|3|
|4|GND||Ground||1|
|5|TX4p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|6|TX4n|Transmitter Data Inverted|CML-I|Input from Host|3|
|7|GND||Ground||1|
|8|TX6p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|9|TX6n|Transmitter Data Inverted|CML-I|Input from Host|3|
|10|GND||Ground||1|
|11|TX8p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|12|TX8n|Transmitter Data Inverted|CML-I|Input from Host|3|
|13|GND||Ground||1|
|14|SCL|2-wire Serial interface clock|LVCMOS-<br>I/O|Bi-directional|3|
|15|VCC|+3.3V Power||Power from Host|2|
|16|VCC|+3.3V Power||Power from Host|2|
|17|LPWn/PRSn|Low-Power Mode / Module Present|Multi-Level|Bi-directional|3|
|18|GND||Ground||1|
|19|RX7n|Receiver Data Inverted|CML-O|Output to Host|3|
|20|RX7p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|21|GND||Ground||1|
|22|RX5n|Receiver Data Inverted|CML-O|Output to Host|3|
|23|RX5p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|24|GND||Ground||1|
|25|RX3n|Receiver Data Inverted|CML-O|Output to Host|3|
|26|RX3p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|27|GND||Ground||1|
|28|RX1n|Receiver Data Inverted|CML-O|Output to Host|3|
|29|RX1p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|30|GND||Ground||1|
|31|GND||Ground||1|
|32|RX2p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|33|RX2n|Receiver Data Inverted|CML-O|Output to Host|3|
|34|GND||Ground||1|
|35|RX4p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|36|RX4n|Receiver Data Inverted|CML-O|Output to Host|3|
|37|GND||Ground||1|
|38|RX6p|Receiver Data Non-Inverted|CML-O|Output to Host|3|
|39|RX6n|Receiver Data Inverted|CML-O|Output to Host|3|
|40|GND||Ground||1|
|41|RX8p|Receiver Data Non-Inverted|CML-O|Output to Host|3|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


|42|RX8n|Receiver Data Inverted|CML-O|Output to Host|3|
|---|---|---|---|---|---|
|43|GND||Ground||1|
|44|INT/RSTn|Module Interrupt / Module Reset|Multi-Level|Bi-directional|3|
|45|VCC|+3.3V Power||Power from Host|2|
|46|VCC|+3.3V Power||Power from Host|2|
|47|SDA|2-wire Serial interface data|LVCMOS-I/<br>O|Bi-directional|3|
|48|GND||Ground||1|
|49|TX7n|Transmitter Data Inverted|CML-I|Input from Host|3|
|50|TX7p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|51|GND||Ground||1|
|52|TX5n|Transmitter Data Inverted|CML-I|Input from Host|3|
|53|TX5p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|54|GND||Ground||1|
|55|TX3n|Transmitter Data Inverted|CML-I|Input from Host|3|
|56|TX3p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|57|GND||Ground||1|
|58|TX1n|Transmitter Data Inverted|CML-I|Input from Host|3|
|59|TX1p|Transmitter Data Non-Inverted|CML-I|Input from Host|3|
|60|GND||Ground||1|



## **Digital Diagnostics** 

|**Parameter**|**Range**|**Accuracy**|**Unit**|**Calibration**|
|---|---|---|---|---|
|Temperature|0 to 70|±3|ºC|Internal|
|Voltage|0 to VCC|0.1|V|Internal|
|Tx BiasCurrent (EachLane)|0 to 100|10%|mA|Internal|
|Tx OutputPower (EachLane)|-2.8to +5.3|±3|dB|Internal|
|Rx ReceivePower (Each Lane)|-9.1to +5.3|±3|dB|Internal|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


## **Recommended OSFP Host Board Schematic** 


**Figure 2. Recommended OSFP Host Board Schematic** 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LO-DM31800-DR8C Rev1.0- Sep.2026 


## **Mechanical Drawing** 

**Figure 3. Mechanical Outline** 

## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LO-DM31800-DR8C|OSFP,Dual MPO-12/APC interface,1310nm,800G,Closed top,DR8,500m,0~70°C|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2026 LINK-PP AlI Rights Reserved 

Page 8 of 8 

