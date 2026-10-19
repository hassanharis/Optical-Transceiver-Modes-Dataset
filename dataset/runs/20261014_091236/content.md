LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **LS-MM8525E-S3C** 

## SFP28 10G/25Gbps 850nm 300m DDMI 

## **Product Features** 

- Up to 10/25.7813Gbps Data Links 

- 850nm VCSEL laser transmitter and PIN receiver 

- Maximum link length of 70m on OM3 

- Multimode Fiber (MMF) and 300m on OM4 MMF 

- Hot-pluggable SFP28 footprint 

- Duplex LC receptacles 

- Low power dissipation 

- RoHS compliant and lead-free 

- Support Digital Diagnostic Monitor interface 

- Single +3.3V power supply 

- 0°C to +70°C case operating temperature 

## **Applications** 

- 25GBASE-SR Ethernet 

- eCPRI 

- Data center 

## **Compliance** 


- SFF-8472 

- SFF-8402 

- SFF-8432 

- SFF-8431 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Pin Diagram** 


Pin out of Connector Block on Host Board 

## **Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|VEET|Module transmitter ground|1|
|2|Fault|Module transmitter Fault|2|
|3|Disable|Transmitter Disable; Turns off transmitter laser output|3|
|4|SDL|2 wire serial interface data input/output (SDA)|4|
|5|SCL|2 wire serial interface clock input (SCL)|4|
|6|MOD-ABS|Module Absent, connect to VeeR or VeeT in the module|2|
|7|RS0|Rate select0: module inputs and are pulled low to VeeT with >30 kΩ resistors<br>in the module.||
|8|LOS|Receiver Loss of Signal Indication||
|9|RS1|Rate select1: module inputs and are pulled low to VeeT with >30 kΩ resistors<br>in the module.||
|10|VeeR|Module receiver ground|1|
|11|VeeR|Module receiver ground|1|
|12|RD-|Receiver inverted data out put||
|13|RD+|Receiver non-inverted data out put||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


|14|VeeR|Module receiver ground|1|
|---|---|---|---|
|15|VccR|Module receiver 3.3V supply||
|16|VccT|Module transmitter 3.3V supply||
|17|VeeT|Module transmitter ground|1|
|18|TD+|Transmitter non-inverted data out put||
|19|TD-|Transmitter inverted data out put||
|20|VeeT|Module transmitter ground|1|



## **Notes:** 

1. The module ground pins shall be isolated from the module case. 

2. This pin is an open collector/drain output pin and shall be pulled up with 4.7K-10Kohms to Host_Vcc on the host board. 

3. This pin shall be pulled up with 4.7K-10Kohms to VccT in the module. 

4. This pin is an open collector/drain output pin and shall be pulled up with 4.7K-10Kohms to Host_Vcc on the host board. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Type**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.5||3.6|V||
|Storage Temperature|TS|-40||85|℃|1|
|Case Operating Temperature|TOP|0||70|℃||
|Relative Humidity|RH|0||85|%|2|



Notes: 

- 1.Limited by the fiber cable jacket, not the active ends. 

- 2.Non-condensing. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Optical Characteristics (TOP = 0°C to 70°C, VCC = 3.3 ± 5% Volts)** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Remark**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Center Wavelength|λc|840|850|860|nm||
|RMS Spectral Width|Pm|||0.6|nm||
|Average Output Power(25.78G)|Pavg|-8.4||2.4|dBm||
|Average Output Power(10.3G)|Pavg|-7||-1|dBm||
|Optical Modulation Amplitude<br>(OMA)（25.78G）|Poma|-6.4||3|dBm||
|Optical Modulation Amplitude<br>(OMA)(10G)|Poma|-5.2||3|dBm||
|Extinction Ratio(25.78G)|ER|2|||dB||
|Extinction Ratio(10.3G)|ER|2|5.5||dB||
|Transmitter Dispersion<br>Penalty(25.78G)|TDEC|||4.3|dB||
|Transmitter Dispersion<br>Penalty(10.3G)|TDP|||3.9|dB||
|Optical Return Loss Tolerance|TOL|||12|dB||
|Transmitter OFF Output Power|POff|||-30|dBm||
|Transmitter eye mask definition<br>{X1, X2, X3, Y1, Y2, Y3}, Hit ratio<br>1.5E-3||{0.3,<br>0.38,<br>0.45,<br>0.35,<br>0.41,<br>0.5}|||||
|**Receiver**|||||||
|Center Wavelength|λc|840|850|860|nm||
|Receiver Stress Sensitivity,OMA||||-5.2|dBm||
|Receiver Sensitivity, Average<br>Power(25.78G)||-10.3||3|dBm||
|Receiver Sensitivity, Average<br>Power(10.3G)||-10||0.5|dBm||
|Receiver Reflectance|Rfl|||-26|dBm||
|Loss of Signal Assert|PA|-30|||dBm||
|Loss of Signal De-assert|PD|||-13|dBm||
|LOS Hysteresis|PD- PA|0.5|||dB||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Electrical Characteristics (TOP = 0°C to 70°C, VCC = 3.3 ± 5% Volts)** 

|**Parameter**|**Symbol**|**Min**|**Type**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.135|3.3|3.465|V||
|Supply Current|Icc|||300|mA||
|**Transmitter**|||||||
|Input differential impedance|Rin||100|||1|
|Differential data input swing|Vin, pp|200||1000|mV||
|Transmit Disable Voltage|VD|2||VCC|V||
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|V||
|**Receiver**|||||||
|Differential data output swing|Vout, pp|200||1000|mV|2|
|LOS Fault|VLOS_fault|2||Vcc|V|3|
|LOS Normal|VLOS_norm|Vee||Vee+0.8|V|3|
|Power Supply Noise Tolerance|VCCT/VCCR|Per SFF-8431 Rev 4.1|||mVpp||



## Notes: 

1. Connected directly to TX data input pins.AC coupling from pins into laser driver IC. 

2. Into 100Ω differential termination. 

3. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s in sequence in the PRBS^9 is an acceptable alternative. SFF-8431 Rev 4.1 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Digital Diagnostic Memory Map** 


## **Digital Diagnostic Monitoring Information** 

|**Parameter**|**Unit**|**Accuracy**|
|---|---|---|
|Case Temperature|℃|±3|
|Supply Voltage|V|±3%|
|Tx Bias Current|mA|±10%|
|Tx Optical Power|dB|±3|
|Rx Optical Power|dB|±3|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Recommended Interface Circuit** 


www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM8525E-S3C Rev1.0- Sep.2021 


## **Mechanical Dimensions** 


SFP wire mechanical drawing (Unit: mm) 

## **Ordering information** 

|**Part Number**|**Description**|
|---|---|
|LS-MM8525E-S3C|SFP28 10G/25Gbps 850nm 300m DDMI<br>0°C to +70°C|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 8 of 8 

