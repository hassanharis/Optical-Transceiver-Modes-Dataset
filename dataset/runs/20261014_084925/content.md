LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


## **LS-DWxx10-40C** 

## 10.3Gbps SFP+ DWDM Transceiver, Single Mode, 40km Reach 

## **Product Features** 

- Supports up to 10.7Gbps bit rates 

- Hot-pluggable SFP+ footprint 

- 100GHz ITU, C Band DWDM Cooled EML laser and PIN photodiode, Up to 40km for SMF transmission 

- Compliant with SFP+ MSA and SFF-8472 with duplex LC receptacle 

- Compatible with RoHS 

- Single +3.3V power supply 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: Standard:0 to +70°C 

## **Applications** 

- 10Gbps DWDM Optical systems 

- 10GBASE-ZR at 10.3125Gbps 

- 10GBASE-ZW at 9.953Gbps 

- LTE systems 

- Other Optical links 


## **Description** 

The SFP+ transceivers are high performance, cost effective modules supporting data rate of 10Gbps and 40km transmission distance with SMF. 

The transceiver consists of three sections: a Cooled EML laser transmitter, a PIN photodiode integrated with a trans-impedance preamplifier (TIA) and MCU control unit. All modules satisfy class I laser safety requirements. 

The transceivers are compatible with SFP Multi-Source Agreement and SFF-8472 digital diagnostics functions. 

www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 



**----- Start of picture text -----**<br>
TD+/-<br>LD<br>TxFault LD Driver<br>TxDis<br>LOS<br>Post Amp PIN+TIA<br>RD+/-<br>POWER<br>I2C Controller Temp<br>Vcc<br>LD Bias<br>SCL<br>EEPROM ADC/DAC Tx Power<br>SDA<br>Rx Power<br>**----- End of picture text -----**<br>


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
|Power Supply Current|Icc|||550|mA|
|Data Rate||8.0|10.3|10.7|Gbps|



www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


## **Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
||||**Transmitter**||||||
|Centre Wavelength|||λc|1528.77||1563.05|nm||
|Spectral Width（-20dB）|||Δλ|||1|nm||
|Side-Mode Suppression Ratio|||SMSR|30|-||dB||
|Average Output Power|||Pout|-1||+2|dBm|1|
|Extinction Ratio|||ER|6.0|||dB||
|Data Input Swing Differential|||VIN|180||850|mV|2|
|Input Differential Impedance|||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
|TX Fault|Fault|||2.0||Vcc|V||
||Normal|||0||0.8|V||
||||**Receiver**||||||
|Centre Wavelength|||λc|1450||1620|nm||
|Receiver Sensitivity||||||-15.5|dBm|3|
|Receiver Overload||||0.5|||dBm|3|
|LOS De-Assert|||LOSD|||-17|dBm||
|LOS Assert|||LOSA|-28|||dBm||
|LOS Hysteresis||||0.5|||dB||
|Data Output Swing Differential|||Vout|300||900|mV|4|
|LOS|||High|2.0||Vcc|V||
||||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into SMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[31] -1 test pattern @10312Mbps, BER ≤1×10[-12] . 

4. Internally AC-coupled. 

www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


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
|Serial ID Clock Rate|f_serial_cloc<br>k||100|400|KHz|
|MOD_DEF (0:2)-High|VH|2||Vcc|V|
|MOD_DEF (0:2)-Low|VL|||0.8|V|



## **Diagnostics** 

|**Parameter**|**Range**|**Unit**|**Accuracy**|**Calibration**|
|---|---|---|---|---|
|Temperature|0 to +70|°C|±3°C|Internal|
|Voltage|3.0 to 3.6|V|±3%|Internal|
|Bias Current|0 to 100|mA|±10%|Internal|
|TX Power|-1 to +2|dBm|±3dB|Internal|
|RX Power|-16 to -1|dBm|±3dB|Internal|



www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


## **Digital Diagnostic Memory Map** 

The transceivers provide serial ID memory contents and diagnostic information about the present operating conditions by the 2-wire serial interface (SCL, SDA). 

The diagnostic information with internal calibration or external calibration all are implemented, including received power monitoring, transmitted power monitoring, bias current monitoring, supply voltage monitoring and temperature monitoring. 

The digital diagnostic memory map specific data field defines as following. 


www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


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



www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


|||||||
|---|---|---|---|---|---|
|LINK-PP INT’L TECHNOLOGY CO.,LIMITED<br>LS-DWxx10-40CRev1.0- Sep.2016||||||
||17<br>VEET<br>Transmitter Ground<br>1<br>18<br>TD+<br>Transmit Data In<br>3<br>Note 5<br>19<br>TD-<br>Inv. Transmit Data In<br>3<br>Note 5<br>20<br>VEET<br>Transmitter Ground<br>1|||||
||17|VEET|Transmitter Ground|1||
||18|TD+|Transmit Data In|3|Note 5|
||19|TD-|Inv. Transmit Data In|3|Note 5|
||20|VEET|Transmitter Ground|1||



Notes: 

## Plug Seq.: Pin engagement sequence during hot plugging. 

1. TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

2. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3. LOS is open collector output. Should be pulled up with 4.7k~10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss ofsignal. 

4. RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

5. TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

## **Recommended Interface Circuit** 


www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 7 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


## **Mechanical Dimensions** 


www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 8 of 9 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LS-DWxx10-40C Rev1.0- Sep.2016 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LS-DWxx10-40C|1528.77~1563.05nm DWDM, 10Gbps, LC, 40km, 0°C~+70°C, with DDM,<br>xx: Channel code|



|**λC Wavelength Guide**|**λC Wavelength Guide**|**λC Wavelength Guide**|**λC Wavelength Guide**|**λC Wavelength Guide**|**λC Wavelength Guide**|
|---|---|---|---|---|---|
|**ITU Channel**<br>**Product Code**|**Frequency(THz)**|**Wavelength**|**ITU Channel**<br>**Product**<br>**Code**|**Frequency(THz)**|**Wavelength**|
|17|191.7|1563.86|40|194.0|1545.32|
|18|191.8|1563.04|41|194.1|1544.52|
|19|191.9|1562.23|42|194.2|1543.73|
|20|192.0|1561.41|43|194.3|1542.93|
|21|192.1|1560.60|44|194.4|1542.14|
|22|192.2|1559.79|45|194.5|1541.34|
|23|192.3|1558.98|46|194.6|1540.55|
|24|192.4|1558.17|47|194.7|1539.76|
|25|192.5|1557.36|48|194.8|1538.97|
|26|192.6|1556.55|49|194.9|1538.19|
|27|192.7|1555.74|50|195.0|1537.40|
|28|192.8|1554.94|51|195.1|1536.61|
|29|192.9|1554.13|52|195.2|1535.82|
|30|193.0|1553.32|53|195.3|1535.04|
|31|193.1|1552.52|54|195.4|1534.25|
|32|193.2|1551.72|55|195.5|1533.46|
|33|193.3|1550.92|56|195.6|1532.68|
|34|193.4|1550.11|57|195.7|1531.89|
|35|193.5|1549.32|58|195.8|1531.12|
|36|193.6|1548.51|59|195.9|1530.33|
|37|193.7|1547.71|60|196.0|1529.55|
|38|193.8|1546.92|61|196.1|1528.77|
|39|193.9|1546.12|-|-|-|



www.link-pp.com **www.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 9 of 9 

