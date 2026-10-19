LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


## **LS-SM316G-02C** 

## 6.1Gbps SFP+ Transceiver, Single Mode, 2km Reach 

## **Product Features** 

- Supports up to 6.25Gbps bit rates 

- Hot-pluggable SFP+ footprint 

- 1310nm FP laser and PIN photodiode, Up to 2km for SMF transmission 

- Compliant with SFP+ MSA and SFF-8472 with duplex LC receptacle 

- Compatible with RoHS 

- Single +3.3V power supply 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: 

   - Standard: 0 to +70°C 

Industrial: -40 to +85°C 

## **Applications** 

- 6.144Gbps Optical systems 

- LTE systems 

- Other Optical links 

## **Description** 


The SFP+ transceivers are high performance, cost effective modules supporting data rate of 6.1 Gbps and 2km transmission distance with SMF. 

The transceiver consists of three sections: a FP laser transmitter, a PIN photodiode integrated with a transimpedance preamplifier (TIA) and MCU control unit. All modules satisfy class I laser safety requirements. 

The transceivers are compatible with SFP Multi-Source Agreement and SFF-8472 digital diagnostics functions. 

**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 



**----- Start of picture text -----**<br>
TD+/-<br>LD<br>TxFault LD Driver<br>TxDis<br>LOS<br>Post Amp PIN+TIA<br>RD+/-<br>POWER<br>I2C Controller Temp<br>Vcc<br>LD Bias<br>SCL<br>EEPROM ADC/DAC Tx Power<br>SDA<br>Rx Power<br>**----- End of picture text -----**<br>


Transceiver functional diagram 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Supply Voltage|Vcc|-0.5|4.5|V|
|Storage<br>Temperature|Ts|-40|+85|°C|
|Operating Humidity|-|5|85|%|



## **Recommended Operating Conditions** 

|**Parameter**||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Operating Case Temperature|Standard|Tc|0||+70|°C|
||Extended||-20||+85|°C|
||Industrial||-40||+85|°C|
|Power Supply Voltage||Vcc|3.135|3.30|3.465|V|
|Power Supply Current||Icc|||320|mA|
|Data Rate|||1.0|6.144|6.25|Gbps|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


## **Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
||||**Transmitter**||||||
|Centre Wavelength|||λc|1270|1310|1350|nm||
|Spectral Width（-20dB）|||Δλ|||1|nm||
|Side-Mode Suppression Ratio|||SMSR|30|-||dB||
|Average Output Power|||Pout|-6.5||-0.5|dBm|1|
|Extinction Ratio|||ER|3.5|||dB||
|Data Input Swing Differential|||VIN|180||850|mV|2|
|Input Differential Impedance|||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
|TX Fault|Fault|||2.0||Vcc|V||
||Normal|||0||0.8|V||
||||**Receiver**||||||
|Centre Wavelength|||λc|1260||1600|nm||
|Receiver Sensitivity||||||-15|dBm|3|
|Receiver Overload||||0.5|||dBm|3|
|LOS De-Assert|||LOSD|||-15.5|dBm||
|LOS Assert|||LOSA|-30|||dBm||
|LOS Hysteresis||||0.5|||dB||
|Data Output Swing Differential|||Vout|300||900|mV|4|
|LOS|||High|2.0||Vcc|V||
||||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into SMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[31] -1 test pattern @6144Mbps, BER ≤1×10[-12] . 

4. Internally AC-coupled. 

**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


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



## **Diagnostics** 

|**Parameter**|**Range**|**Unit**|**Accuracy**|**Calibration**|
|---|---|---|---|---|
|Temperature|0 to +70|°C|±3°C|Internal|
||-20 to +85||||
||-40 to +85||||
|Voltage|3.0 to 3.6|V|±3%|Internal|
|Bias Current|0 to 100|mA|±10%|Internal|
|TX Power|-6.5 to -0.5|dBm|±3dB|Internal|
|RX Power|-20 to -1|dBm|±3dB|Internal|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


## **Digital Diagnostic Memory Map** 

The transceivers provide serial ID memory contents and diagnostic information about the present operating conditions by the 2-wire serial interface (SCL, SDA). 

The diagnostic information with internal calibration or external calibration all are implemented, including received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring. 

The digital diagnostic memory map specific data field defines as following. 


**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


## **Pin Descriptions** 


|**Pin**|**Signal Name**|**Description**|**Plug Seq.**|**Notes**|
|---|---|---|---|---|
|1|VEET|Transmitter Ground|1||
|2|TX FAULT|Transmitter Fault Indication|3|Note 1|
|3|TX DISABLE|Transmitter Disable|3|Note 2|
|4|SDA|SDA Serial Data Signal|3||
|5|SCL|SCL Serial Clock Signal|3||
|6|MOD_ABS|Module Absent. Grounded within the<br>module|3||
|7|RS0|Not Connected|3||
|8|LOS|Loss of Signal|3|Note 3|
|9|RS1|Not Connected|3||
|10|VEER|Receiver ground|1||
|11|VEER|Receiver ground|1||
|12|RD-|Inv. Received Data Out|3|Note 4|
|13|RD+|Received Data Out|3|Note 4|
|14|VEER|Receiver ground|1||
|15|VCCR|Receiver Power Supply|2||



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


|16|VCCT|Transmitter Power Supply|2||
|---|---|---|---|---|
|17|VEET|Transmitter Ground|1||
|18|TD+|Transmit Data In|3|Note 5|
|19|TD-|Inv. Transmit Data In|3|Note 5|
|20|VEET|Transmitter Ground|1||



Notes: 

Plug Seq.: Pin engagement sequence during hot plugging. 

1. TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

2. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3. LOS is open collector output. Should be pulled up with 4.7k~10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss ofsignal. 

4. RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

5. TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

## **Recommended Interface Circuit** 

**ww** www.link-pp.com w.l-p.comw.l-p.com Copyright © 2016 LINK-PP AlI Rights Reserved 


**----- Start of picture text -----**<br>
Page 7 of 8<br>**----- End of picture text -----**<br>


LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM316G-02C Rev1.0- Sep.2016 


## **Mechanical Dimensions** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LS-SM316G-02C|1310nm,<br>6.144Gbps,<br>LC,<br>2km,<br>0°C~+70°C,<br>with DDM|
|LS-SM316G-02I|1310nm,<br>6.144Gbps,<br>LC,<br>2km,<br>-40°C~+85°C,<br>with DDM|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 8 of 8 

