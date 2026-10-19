LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **LS-MM858G-S3I** 8Gbps SFP+ Transceiver, Multi Mode, 300m Reach 

## **Product Features** 

- Supports up to 8.5Gbps bit rates 

- Hot-pluggable SFP+ footprint 

- 850nm VCSEL laser and PIN photodiode, Up to 300m for OM3-MMF transmission 

- Compliant with SFP+ MSA and SFF-8472 with duplex LC receptacle 

- Compatible with RoHS 

- Single +3.3V power supply 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: 

Standard: 0 to +70°C 

Industrial: -40 to +85°C 

## **Applications** 

- Tri-Rate 2.125/4.25/8.5Gbps Fiber Channel 

- Wireless – CPRI and OBSAI 

- Other Optical links 

## **Description** 


The SFP+ transceivers are high performance, cost effective modules supporting data rate of 8.5Gbps. The transceiver consists of three sections: a VCSEL laser transmitter, a PIN photodiode integrated with a transimpedance preamplifier (TIA) and MCU control unit. All modules satisfy class I laser safety requirements. The transceivers are compatible with SFP Multi-Source Agreement and SFF-8472 digital diagnostics functions. 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 




**----- Start of picture text -----**<br>
TD+/-<br>LD<br>TxFault LD Driver<br>TxDis<br>LOS<br>Post Amp PIN+TIA<br>RD+/-<br>POWER<br>I2C Controller Temp<br>Vcc<br>LD Bias<br>SCL<br>EEPROM ADC/DAC Tx Power<br>SDA<br>Rx Power<br>**----- End of picture text -----**<br>


Transceiver functional diagram 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Supply Voltage|Vcc|-0.5|4.5|V|
|Storage Temperature|Ts|-40|+85|°C|
|Operating Humidity|-|5|85|%|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **Recommended Operating Conditions** 

|**Parameter**||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Operating Case Temperature|Standard|Tc|0||+70|°C|
||Extended||-20||+85|°C|
||Industrial||-40||+85|°C|
|Power Supply Voltage||Vcc|3.135|3.30|3.465|V|
|Power Supply Current||Icc|||260|mA|
|Data Rate|||1.0|10.3|10.7|bps|



## **Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
|**Transmitter**|||||||||
|Centre Wavelength|||λc|840|850|860|nm||
|Spectral Width（RMS）|||Δλ|||0.45|nm||
|Side-Mode Suppression Ratio|||SMSR|-|-|-|dB||
|Average Output Power|||Pout|-6.0||-0.5|dBm|1|
|Extinction Ratio|||ER|3.0|||dB||
|Data Input Swing|Differential||VIN|180||950|mV|2|
|Input Differential|Impedance||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
|TX Fault|Fault|||2.0||Vcc|V||
||Normal|||0||0.8|V||
|**Receiver**|||||||||
|Centre Wavelength|||λc|840|850|860|nm||
|Receiver Sensitivity||||||-10.5|dBm|3|
|Receiver Overload||||0.5|||dBm|3|
|LOS De-Assert|||LOSD|||-12|dBm||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


|LOS Assert|LOSA|-22|||dBm||
|---|---|---|---|---|---|---|
|LOS Hysteresis||0.5||4|dB||
|Data Output Swing Differential|Vout|500|700|900|mV|4|
|LOS|High|2.0||Vcc|V||
||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into MMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[31] -1 test pattern @10312Mbps, BER ≤1×10[-12] . 

4. Internally AC-coupled. 

## **Timing and Electrical** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Tx Disable Negate Time|t_on|||1|ms|
|Tx Disable Assert Time|t_off|||10|µs|
|Time To Initialize, including Reset of Tx Fault|t_init|||300|ms|
|Tx Fault Assert Time|t_fault|||100|µs|
|Tx Disable To Reset|t_reset|10|||µs|
|LOS Assert Time|t_loss_on|||100|µs|
|LOS De-assert Time|t_loss_off|||100|µs|
|Serial ID Clock Rate|f_serial_clock||100|400|KHz|
|MOD_DEF (0:2)-High|VH|2||Vcc|V|
|MOD_DEF (0:2)-Low|VL|||0.8|V|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **Diagnostics** 

|**Parameter**|**Range**|**Unit**|**Accuracy**|**Calibration**|
|---|---|---|---|---|
|Temperature|0 to +70|°C|±3°C|Internal|
||-20 to +85||||
||-40 to +85||||
|Voltage|3.0 to 3.6|V|±3%|Internal|
|Bias<br>Current|0 to 15|mA|±10%|Internal|
|TX Power|-6.0 to -0.5|dBm|±3dB|Internal|
|RX Power|-16 to -1|dBm|±3dB|Internal|



## **Digital Diagnostic Memory Map** 

The transceivers provide serial ID memory contents and diagnostic information about the present operating conditions by the 2-wire serial interface (SCL, SDA). 

The diagnostic information with internal calibration or external calibration all are implemented, including received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring. 

The digital diagnostic memory map specific data field defines as following. 


**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **Pin Descriptions** 


|**Pin**|**Signal Name**|**Description**|**Plug Seq.**|**Notes**|
|---|---|---|---|---|
|1|VEET|Transmitter Ground|1||
|2|TX FAULT|Transmitter Fault Indication|3|Note 1|
|3|TX DISABLE|Transmitter Disable|3|Note 2|
|4|SDA|SDA Serial Data Signal|3||
|5|SCL|SCL Serial Clock Signal|3||
|6|MOD_ABS|Module Absent. Grounded within the module|3||
|7|RS0|Not Connected|3||
|8|LOS|Loss of Signal|3|Note 3|
|9|RS1|Not Connected|3||
|10|VEER|Receiver ground|1||
|11|VEER|Receiver ground|1||
|12|RD-|Inv. Received Data Out|3|Note 4|
|13|RD+|Received Data Out|3|Note 4|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 9 


## LINK-PP INT’L TECHNOLOGY CO., LIMITED 

||||||||
|---|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-MM858G-S3I Rev1.0- Sep.2016|||||||
||14|VEER|Receiver ground|1|||
||15|VCCR|Receiver Power Supply|2|||
||16|VCCT|Transmitter Power Supply|2|||
||17|VEET|Transmitter Ground|1|||
||18|TD+|Transmit Data In|3|Note 5||
||19|TD-|Inv. Transmit Data In|3|Note 5||
||20|VEET|Transmitter Ground|1|||



Notes: 

Plug Seq.: Pin engagement sequence during hot plugging. 

1. TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

2. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3. LOS is open collector output. Should be pulled up with 4.7k~10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss ofsignal. 

4. RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

5. TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 7 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **Recommended Interface Circuit** 


**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 8 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-MM858G-S3I Rev1.0- Sep.2016 


## **Mechanical Dimensions** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LS-MM858G-S3C|850nm,<br>8.5Gbps, Multi Mode, LC, 300m, 0°C~+70°C|
|LS-MM858G-S3I|850nm,<br>8.5Gbps, Multi Mode, LC, 300m, -40°C~+85°C|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 9 of 9 

