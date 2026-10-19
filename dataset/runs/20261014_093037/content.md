LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


## **LS-SM3116-10C** 

## 14.025Gbps SFP+ Transceiver, Single Mode, 10km Reach 

## **Product Features** 

- Supports up to 14.025Gbps bit rates 

- Hot-pluggable SFP+ footprint 

- 1310nm DFB laser and PIN photodiode, Up to 10km for SMF transmission 

- Compliant with SFP+ MSA and SFF-8472 with duplex LC receptacle 

- Compatible with RoHS 

- Single +3.3V power supply 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: 

   - Standard: 0 to +70°C 

## **Applications** 

- Tri-Rate 4.25/8.5/14.025 Gb/s Fibre Channel 


## **Description** 

The SFP+ transceivers are high performance, cost effective modules supporting data rate of 14.025Gbps and 10km transmission distance with SMF. 

The transceiver consists of three sections: a DFB laser transmitter, a PIN photodiode integrated with a trans-impedance preamplifier (TIA) and MCU control unit. All modules satisfy class I laser safety requirements. 

The transceivers are compatible with SFP Multi-Source Agreement and SFF-8472 digital diagnostics functions. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 



Transceiver functional diagram 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Supply Voltage|Vcc|-0.5|4.5|V|
|Storage Temperature|Ts|-40|+85|°C|
|Operating Humidity|-|5|85|%|



## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Operating Case Temperature|Tc|0||+70|°C|
|Power Supply Voltage|Vcc|3.135|3.30|3.465|V|
|Power Supply Current|Icc|||300|mA|
|Data Rate|||14.025||Gbps|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


## **Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
||||**Transmitter**||||||
|Centre Wavelength|||λc|1270|1310|1350|nm||
|Spectral Width（-20dB）|||Δλ|||1|nm||
|Side-Mode Suppression Ratio|||SMSR|30|-||dB||
|Average Output Power|||Pout|-5||-0.5|dBm|1|
|Extinction Ratio|||ER|3.5|||dB||
|Data Input Swing Differential|||VIN|180||850|mV|2|
|Input Differential Impedance|||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
|TX Fault|Fault|||2.0||Vcc|V||
||Normal|||0||0.8|V||
||||**Receiver**||||||
|Centre Wavelength|||λc|1260||1600|nm||
|Receiver Sensitivity||||||-12|dBm|3|
|Receiver Overload||||0.5|||dBm|3|
|LOS De-Assert|||LOSD|||-13|dBm||
|LOS Assert|||LOSA|-30|||dBm||
|LOS Hysteresis||||0.5|||dB||
|Data Output Swing Differential|||Vout|300||900|mV|4|
|LOS|||High|2.0||Vcc|V||
||||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into MMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[31] -1 test pattern @14025Mbps, BER ≤1×10[-12] . 

4. Internally AC-coupled. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


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
|Voltage|3.0 to 3.6|V|±3%|Internal|
|Bias Current|0 to 15|mA|±10%|Internal|
|TX Power|-7.8 to -0.5|dBm|±3dB|Internal|
|RX Power|-16 to -0.5|dBm|±3dB|Internal|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


## **Digital Diagnostic Memory Map** 

The transceivers provide serial ID memory contents and diagnostic information about the present operating conditions by the 2-wire serial interface (SCL, SDA). 

The diagnostic information with internal calibration or external calibration all are implemented, including received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring. 

The digital diagnostic memory map specific data field defines as following. 


www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


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
|14|VEER|Receiver ground|1||
|15|VCCR|Receiver Power Supply|2||
|16|VCCT|Transmitter Power Supply|2||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LS-SM3116-10C Rev1.0- Sep.2020 

|17|VEET|Transmitter Ground|1||
|---|---|---|---|---|
|18|TD+|Transmit Data In|3|Note 5|
|19|TD-|Inv. Transmit Data In|3|Note 5|
|20|VEET|Transmitter Ground|1||



Notes: 

## Plug Seq.: Pin engagement sequence during hot plugging. 

- 1) TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

- 2) Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

- 3) LOS is open collector output. Should be pulled up with 4.7k~10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

- 4) RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

- 5) TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

## **Recommended Interface Circuit** 


www.link-pp.com **ww** w.l-p.comw.l-p.com Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-SM3116-10C Rev1.0- Sep.2020 


## **Mechanical Dimensions** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LS-SM3116-10C|1310nm<br>14.025Gbps<br>LC<br>10km<br>0°C~+70°C<br>with DDM|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 8 of 8 

