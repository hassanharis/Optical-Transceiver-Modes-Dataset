LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


## **LX-MM8510-S3C** 

## 10Gbps XFP Transceiver, Multi Mode, 300m Reach 

## **Product Features** 

- Supports 8.0Gb/s to 11.1Gb/s bit rates 

- Hot-pluggable XFP footprint, Built-in digital diagnos 

- Maximum link length of 300m with MMF-OM3 

- 850nm VCSEL laser and PIN photodiode 

- XFP MSA package with duplex LC connector 

- No reference clock required 

- Single +3.3V power supply 

- Power dissipation <1.5W 

- Compatible with RoHS 

- Temperature range：0 to +70°C 


## **Applications** 

- SONET OC-192&SDH STM-64 at 9.953Gbps 

- 10GBASE-SR/SW 10G Ethernet 

- 1200-MX-SN-I 10Gigabit Fiber Channel 

- 10GE over G.709 at 11.09Gbps 

- OC192 over FEC at 10.709Gbps 

- Other optical links, up to 11.3Gbps 

## **Description** 

The XFP module is compliant with the 10G Small Form-Factor Pluggable (XFP) Multi-Source Agreement (MSA), supporting data-rate of 8.0~11.1Gbps, and transmission distance up to 300m with OM3 MMF. 

The transceiver module comprises a transmitter with 850nm VCSEL laser and a receiver with a PIN photodiode. Transmitter and receiver are separate within a wide temperature range and offers optimum heat dissipation 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


and excellent electromagnetic shielding thus enabling high port densities for 10 GbE systems. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Supply Voltage|Vcc|-0.5|4.5|V|
|Storage Temperature|Ts|-40|+85|°C|
|Operating Humidity|-|5|85|%|



Any stress beyond the maximum ratings can result in permanent damage. The device specifications are guaranteed only under the recommended operating conditions. 

## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Operating Case Temperature|Tc|0||+70|°C|
|Power Supply Voltage @3.3V|Vcc|3.135|3.30|3.465|V|
|Power Supply Current|Icc|||500|mA|
|Data Rate||8.0||11.1|Gbps|



## **Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
|**Transmitter**|||||||||
|Centre Wavelength|||λc|840|850|860|nm||
|Spectral Width（RMS）|||Δλ|||0.45|nm||
|Side-Mode Suppression Ratio|||SMSR|-|-|-|dB||
|Average Output Power|||Pout|-6.5||-0.5|dBm|1|
|Extinction Ratio|||ER|3.0|||dB||
|Data Input Swing Differential|||VIN|180||950|mV|2|
|Input Differential Impedance|||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
||**Receiver**||||||||
|Centre Wavelength|||λc|840||860|nm||
|Receiver Sensitivity||||||-11.1|dBm|3|



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LX-MM8510-S3C Rev1.0- Sep.2016 

|Receiver Overload||0.5|||dBm|3|
|---|---|---|---|---|---|---|
|LOS De-Assert|LOSD|||-12|dBm||
|LOS Assert|LOSA|-26|||dBm||
|LOS Hysteresis||0.5||4|dB||
|Data Output Swing Differential|Vout|400|600|800|mV|2|
|LOS|High|2.0||Vcc|V||
||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into MMF. 

2. Internally AC-coupled. 

3. Measured with a PRBS 2[31] -1 test pattern @9953Mbps, BER ≤1×10[-12] . 

## **Pin Descriptions** 

|**Pin**|**Logic**|**Symbol**|**Name/Description**|**Ref**|
|---|---|---|---|---|
|1||GND|Module Ground|1|
|2||VEE5|Optional –5.2 Power Supply –**Not required**||
|3|LVTTL-I|Mod-Dese l|Module De-select; When held low allows the module to, respond to 2-wire serial<br>interface commands||
|4|LVTTL-O|Interrupt|Interrupt (bar); Indicates presence of an important condition which can be read over<br>the serial 2-wire interface|2|
|5|LVTTL-I|TX_DIS|Transmitter Disable; Transmitter laser source turned off||
|6||VCC5|+5 Power Supply –**Not required**||
|7||GND|Module Ground|1|
|8||VCC3|+3.3V Power Supply||
|9||VCC3|+3.3V Power Supply||
|10|LVTTL-I|SCL|Serial 2-wire interface clock|2|
|11|LVTTL-<br>I/O|SDA|Serial 2-wire interface data line|2|
|12|LVTTL-O|Mod_Abs|Module Absent; Indicates module is not present. Grounded in the module.|2|
|13|LVTTL-O|Mod_NR|Module Not Ready;|2|
|14|LVTTL-O|RX_LOS|Receiver Loss of Signal indicator|2|
|15||GND|Module Ground|1|
|16||GND|Module Ground|1|
|17|CML-O|RD-|Receiver inverted data output||
|18|CML-O|RD+|Receiver non-inverted data output||
|19||GND|Module Ground|1|
|20||VCC2|+1.8V Power Supply –**Not required**||



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


|21|LVTTL-I|P_Down/R<br>ST|Power Down; When high, places the module in the low power stand-by mode and on the<br>falling edge of P_Down initiates a module reset||
|---|---|---|---|---|
||||Reset; The falling edge initiates a complete reset of the module including the 2-<br>wire serial interface,equivalent to apower cycle.||
|22||VCC2|+1.8V Power Supply –**Not required**||
|23||GND|Module Ground|1|
|24|PECL-I|RefCLK+|Reference Clock non-inverted input, AC coupled on the host board –**Not**<br>**required**|3|
|25|PECL-I|RefCLK-|Reference Clock inverted input, AC coupled on the host board –**Not required**|3|
|26||GND|Module Ground|1|
|27||GND|Module Ground|1|
|28|CML-I|TD-|Transmitter inverted data input||
|29|CML-I|TD+|Transmitter non-inverted data input||
|30||GND|Module Ground|1|



## **Notes:** 

1. Module circuit ground is isolated from module chassis ground within themodule. 

2. Open collector, should be pulled up with 4.7k – 10k ohms on host board to a voltage between 3.15Vand3.6V. 

3. A Reference Clock input is not required. 


Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


## **Management Interface** 

The transceivers provide serial ID memory contents and diagnostic information about the present operating conditions by the 2-wire serial interface (SCL, SDA). 

The Module provides diagnostic information about the present operating conditions. The transceiver generates this diagnostic data by digitization of internal analog signals. Alarm/warning threshold data is written during device manufacture. Received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring all are implemented. 

The digital diagnostic memory map specific data field defines as following. 


Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


## **Recommended Host Board Power Supply Circuit** 


## **Recommended High-speed Interface Circuit** 


Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 7 

www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LX-MM8510-S3C Rev1.0- Sep.2016 


## **Mechanical Specifications** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LX-MM8510-S3C|8.0~11.1Gbps, 850nm, OM3 MMF, 300m, 0ºC ~ +70ºC|



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 7 of 7 

www.link-pp.com 

