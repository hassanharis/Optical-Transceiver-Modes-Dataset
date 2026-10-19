
**----- Start of picture text -----**<br>
25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver** 

## **P/N: CWDM-SFP28-LR-XX** 

## **Product Features** 

- Supports up to 25.78Gbps bit rates 

- Hot-pluggable SFP+ footprint 

- CWDM DFB laser and PIN photodiode, Up to 10km for SMF transmission 

- Compliant with SFP+ MSA and SFF-8472 with duplex LC receptacle 

- Compatible with RoHS 

- Single +3.3V power supply 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: Standard: 0 to +70°C 

## **Applications** 

- 25GBASE-LR 

## **1. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|SupplyVoltage|Vcc|-0.5|4.5|V|
|Storage Temperature|Ts|-40|+85|°C|
|OperatingHumidity|-|5|85|%|



sales@qsfptek.com 

1/5 

Rev1.0 


**----- Start of picture text -----**<br>
25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **2. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|OperatingCase Temperature|Tc|0||+70|°C|
|Power SupplyVoltage|Vcc|3.135|3.30|3.465|V|
|Power SupplyCurrent|Icc|||400|mA|
|Data Rate|||25.78||Gbps|



## **3. Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|||**Transmitter**||||||
|Centre Wavelength||λc|λc-6.5|λc|λc+6.5|nm||
|Spectral Width（-20dB）||Δλ|||1|nm||
|Side-Mode Suppression Ratio||SMSR|30|-||dB||
|Average Output Power||Pout|-4||4|dBm|1|
|Extinction Ratio||ER|3.5|||dB||
|Data Input SwingDifferential||VIN|180||850|mV|2|
|Input Differential Impedance||ZIN|90|100|110|Ω||
|TX Disable|Disable||2.0||Vcc|V||
||Enable||0||0.8|V||
|TX Fault|Fault||2.0||Vcc|V||
||Normal||0||0.8|V||
|||**Receiver**||||||
|Centre|Wavelength|λc|1260||1620|nm||
|Receiver Sensitivity|||||-13.3|dBm|3|
|Receiver Overload|||||2|dBm|3|
|LOS De-Assert||LOSD|||-15|dBm||
|LOS Assert||LOSA|-30|||dBm||
|LOS Hysteresis|||0.5|||dB||
|Data Output SwingDifferential||Vout|300||900|mV|4|
|LOS||High|2.0||Vcc|V||
|||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into SMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[31] -1 test pattern @25.78Gps, BER ≤5×10[-5] . 

4. Internally AC-coupled. 

sales@qsfptek.com 

2/5 

Rev1.0 


**----- Start of picture text -----**<br>
25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **4. Timing and Electrical** 

|**Timing and Electrical**||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|Tx Disable Negate Time|t_on|||2|ms|
|Tx Disable Assert Time|t_off|||100|µs|
|Time To Initialize, including Reset of<br>Tx Fault|t_init|||300|ms|
|Tx Fault Assert Time|t_fault|||100|µs|
|Tx Disable To Reset|t_reset|10|||µs|
|LOS Assert Time|t_loss_on|||100|µs|
|LOS De-assert Time|t_loss_off|||100|µs|
|Serial ID Clock Rate|f_serial_clock||100|400|KHz|
|MOD_DEF(0:2)-High|VH|2||Vcc|V|
|MOD_DEF(0:2)-Low|VL|||0.8|V|



## **5. Diagnostics** 

|**iagnostics**|||||
|---|---|---|---|---|
|**Parameter**|**Range**|**Unit**|**Accuracy**|**Calibration**|
|Temperature|0 to +70|°C|±3°C|Internal|
|Voltage|3.0 to 3.6|V|±3%|Internal|
|Bias Current|0 to 100|mA|±10%|Internal|
|TX Power|-4 to 4|dBm|±3dB|Internal|
|RX Power|-14 to +2|dBm|±3dB|Internal|



## **6. Pin Descriptions** 


sales@qsfptek.com 

3/5 

Rev1.0 


**----- Start of picture text -----**<br>
25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


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
|10|VEER|Receiverground|1||
|11|VEER|Receiverground|1||
|12|RD-|Inv. Received Data Out|3|Note 4|
|13|RD+|Received Data Out|3|Note 4|
|14|VEER|Receiverground|1||
|15|VCCR|Receiver Power Supply|2||
|16|VCCT|Transmitter Power Supply|2||
|17|VEET|Transmitter Ground|1||
|18|TD+|Transmit Data In|3|Note 5|
|19|TD-|Inv. Transmit Data In|3|Note 5|
|20|VEET|Transmitter Ground|1||



## **Notes:** 

Plug Seq.: Pin engagement sequence during hot plugging. 1) TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than0.8V. 

2) Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3) LOS is open collector output. Should be pulled up with 4.7k~10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

4) RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

5) TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

sales@qsfptek.com 

4/5 

Rev1.0 


**----- Start of picture text -----**<br>
25G CWDM SFP28 1270-1610nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **7. Mechanical Dimensions** 


## **8. Ordering Information** 

|**rdering Information**||
|---|---|
|**Part Number**|**Product Description**|
|CWDM-SFP28-LR-XX|1270~1610nm CWDM, 25.78Gbps, LC, 10km, 0°C~+70°C, with DDM|



sales@qsfptek.com 

5/5 

Rev1.0 

