LINK-PP INT’L TECHNOLOGY CO., LIMITED 

L9-SD312M-20TTC5 Rev1.0- Sep.2016 


## **L9-SD312M-20TTC5** 

## 1×9 2Mbps 1310nm 20km SC Transceiver Module 

## **Product Features** 

- VCSEL/FP Laser Diode Transmitter 

- Up to 2 Km on 62.5/125μm MMF,Up to 40 Km on 9/125μm SMF 

- 3.3V or 5.0V power supply 

- SC/ST/FC duplex optical interface 

- (LV)TTL Inputs / Outputs and ( LV)TTL signal detect 

- Class 1 Laser International Safety Standard IEC 825 Compliant 

- Operating case temperature range (Standard：0 to +70°C) 

   - (Industrial： -40°C to +85°C) 

## **Application** 

- RS232/RS485/RS422 receptacle fiber transmission 

- Fiber System 


## **Product Description** 

LINK-PP’s L9-xxxx2M-xTTx5 series of transceiver modules are the perfect solution for ultra-low speed communication networks. 

These transceiver modules support data rates up to 2Mbps. The module is fully compliant with the Multi-sourced 1x9 protocol. 

These transceiver modules provides the system designer with products to RS232/RS485/RS422 receptacle fiber transmission. 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

L9-SD312M-20TTC5 Rev1.0- Sep.2016 


## **Absolute Maximum Ratings** 

Operating of the transceiver beyond the Absolute Conditions Listed in Table 1 will degrade or damage the product. It’s not implied that the product would function above the recommended operating environment, it’s possible to reduce the reliability and lifetime of device if Recommended Operating Environment is exceeded (Refer to table 2) 

**Table 1-- Absolute Maximum Conditions** 

|**Parameter**|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature||TST|-40|+85|℃|-|
|Relative Humidity||RH|5|95|%|-|
|Supply Voltage|3.3V power|VCC|0|+3.6|V|-|
||5V power||0|+6||-|



**Table 2-- Recommended Operating Environment and Electrical Characteristics** 

|**Parameter**||**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Note**|
|---|---|---|---|---|---|---|---|
|Supply Voltage|3.3Vpower|VCC|+3.1|+3.3|+3.5|V|-|
||5V power||+4.75|+5.0|+5.25||-|
|SupplyCurrent||Icc|-|-|160|mA|-|
|Operating Case Temperature||TOP|0|-|+70|℃|1|
||||-40|-|+85||2|
|Data Rate||B|DC|500K|2000|Kbps|-|



Note1:standard level 2:industrial level 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

L9-SD312M-20TTC5 Rev1.0- Sep.2016 


## **Optical Parameters** 

## **Table 3-- L9-SD312M-20TTC5 Transceiver Optical Characteristics** 

(Ambient Operating Temperature Ta=+25±5°C, VCC = 3.3 or 5±0.2V) 

|**Parameter**|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Note**|
|---|---|---|---|---|---|---|---|
|**Transmitter**||||||||
|Data rate||B|DC|-|2|Mbps|-|
|||||||||
|Output Center Wavelength||λC|1260|1310|136<br>0|nm|-|
|Output Spectral width (RMS)||λ|-||4.0|nm|-|
|Average Optical Output Power||Po|-8|-|-3|dBm|1,2|
|Extinction Ratio||ER|10|-|-|dB|-|
|**Receiver**||||||||
|Receiver Sensitivity||S|-|-|-18|dBm|1,2|
|Maximum Input Power||||-|-|dBm|1,2|
|||PM<br>|-3|||||
|||AX||||||
|Operation Center Wavelength||λc|1260|-|162<br>0|nm|-|
|SD|Deassert|LOSA|-30|-|-|dBm|1,2|
||Assert|LOSD|-|-|-18|dBm|1,2|
|SD Hysteresis||LOSHYS|0.5|-|-|dB|-|



Note1：The optical power is launched into 9/125μm SMF. Note2：With 2Mbps. 

## **Table 4--- Transceiver Electrical Characteristics** 

(Ambient Operating Temperature Ta=+25±5°C, VCC = 3.3 or 5.0±0.2V) 

|**Parameter**||**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Note**|
|---|---|---|---|---|---|---|---|
|Supply Voltage|3.3V power|VCC|+3.1|+3.3|+3.5|V|-|
||5V power||+4.75|+5.0|+5.2<br>5||-|
|Supply Current||ICC|-|-|160|mA|-|
||**Transmitter**|||||||
|Data Input Voltage - Low||VIL|0|-|0.8|V|1|
|Data Input Voltage - High||VIH|2|-|VCC|V|1|
|**Receiver**||||||||
|Data Output Voltage – Low||VOL|0|-|0.4|V|1|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||||||
|---|---|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>L9-SD312M-20TTC5 Rev1.0- Sep.2016||||||||
||Data Output Voltage – High|VOH|2.4|-|VCC|V|1|
||SD Output Voltage-Low|VOL|0|-|0.8|V|1|
||SD Output Voltage-High|VOH|2|-|VCC|V|1|



Note1：(LV)TTL signal detect 

## **Pin Definitions** 


**Table 5—Connector pin assignment** 

|**Pin #**|**Pin Name**|**Description**|**Note**|
|---|---|---|---|
|1|Rx VEE|Receiver Signal Ground|-|
|2|RD+|Receiver Data Out|-|
|3|RD-|NC|-|
|4|SD|Signal Detect. (LV)TTL||
|5|Rx VCC|Receiver Power Supply|-|
|6|Tx VCC|Transmitter Power Supply|-|
|7|TD-|NC|-|
|8|TD+|Transmitter Data In|-|
|9|Tx VEE|Transmitter Ground|-|



Note1：(LV)TTL-Normal optical input levels to the receiver result in logic “1” output,pull-up 10kΩresistor. 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

L9-SD312M-20TTC5 Rev1.0- Sep.2016 


## **Recommended Circuit Schematic** 


**Recommended Circuit Schematic** 

## **Module Outline Drawing** 


**SC receptacleTYPE1(common)** 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

L9-SD312M-20TTC5 Rev1.0- Sep.2016 



**SC receptacleTYPE2** 

## **Order Information** 

|**Type**|**Fiber Type**|**Wave**<br>**length(nm)**|**Fieber**<br>**length(km)**|**Voltage**|**Operating**<br>**temperature**|
|---|---|---|---|---|---|
|L9-SD312M-02TTC5|MM SC duplex|1310(FP)|2|5V|0 to +70℃|
|L9-SD312M-02TTI5|MM SC duplex|1310(FP)|2|5V|-40°C to +85°C|
|L9-SD312M-20TTC5|SM SC duplex|1310(FP)|20|5V|0 to +70℃|
|L9-SD312M-20TTI5|SM SC duplex|1310(FP)|20|5V|-40°C to +85°C|
|L9-SD312M-40TTC5|SM SC duplex|1310(FP)|40|5V|0 to +70℃|
|L9-SD312M-40TTI5|SM SC duplex|1310(FP)|40|5V|-40°C to +85°C|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 6 

