
**----- Start of picture text -----**<br>
BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver** 

## **P/N: QT- WDM-0220BD** 

## **FEATURES** 

- Dual data-rate of 1.25Gbps/1.063Gbps operation 

- 1550nm DFB laser and PIN photodetector for 20km transmission 

- Compliant with SFP MSA and SFF-8472 with duplex LC receptacle 

- Digital Diagnostic Monitoring: Internal Calibration or External Calibration 

- Compatible with SONET OC-24-LR-1 

- Compatible with RoHS 

- +3.3V single power supply 

- Operating case temperature: Standard: 0 to +70°C, Extended: -40 to +85°C 

## **APPLICATIONS** 

- Gigabit Ethernet 

- Fiber Channel 

- Switch to Switch interface 

- Switched backplane applications 

- Router/Server interface 

- Other optical transmission systems 

sales@qsfptek.com 

1/5 

Rev1.0 


**----- Start of picture text -----**<br>
BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1. Absolute Maximum Ratings** 

|**Parameter**<br>SupplyVoltage<br>Storage Temperature<br>OperatingHumidity|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Vcc|-0.5|4.5|V|
||Ts|-40|+85|°C|
||-|5|85|%|



## **2. Recommended Operating Conditions** 

|||**ons**|||||
|---|---|---|---|---|---|---|
|||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
||Standard|Tc|0||+70|°C|
|||Vcc|3.13|3.3|3.47|V|
|||Icc|||300|mA|
|Gigabit Ethernet||||1.25||Gbps|
|Fiber Channel||||1.063|||



## **3. Optical and Electrical Characteristics** 

|**Parameter**|**Parameter**||**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|
||||**Transmitter**||||||
|Centre Wavelength|||λc|1480|1550|1580|nm||
|Spectral Width (RMS)|||∆λ|||4|nm||
|Average Output Power|||Pout|-9||-3|dBm|1|
|Extinction Ratio|||ER|9|||dB||
|Optical Rise/Fall Time<br>(20%~80%)|||tr/tf|||0.26|ns||
|Data Input Swing Differential|||VIN|400||1800|mV|2|
|Input Differential Impedance|||ZIN|90|100|110|Ω||
|TX Disable|Disable|||2.0||Vcc|V||
||Enable|||0||0.8|V||
|TX Fault|Fault|||2.0||Vcc|V||
||Normal|||0||0.8|V||
||||**Receiver**||||||
|Centre Wavelength|||λc|1260|1310|1360|nm||
|Receiver Sensitivity||||||-22|dBm|3|
|Receiver Overload||||-3|||dBm|3|
|LOS De-Assert|||LOSD|||-24|dBm||
|LOS Assert|||LOSA|-30|||dBm||
|LOS Hysteresis||||1||4|dB||
|Data Output Swing Differential|||Vout|400||1800|mV|4|
|LOS|||High|2.0||Vcc|V||
||||Low|||0.8|V||



## **Notes:** 

1. The optical power is launched into SMF. 

2. PECL input, internally AC-coupled and terminated. 

3. Measured with a PRBS 2[7] -1 test pattern @1250Mbps, BER ≤1×10[-12] . 

4. Internally AC-coupled. 

sales@qsfptek.com 

2/5 

Rev1.0 


**----- Start of picture text -----**<br>
BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **4. Timing and Electrical** 

|**iming and Electrical**||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|Tx Disable Negate Time|t_on|||1|ms|
|Tx Disable Assert Time|t_off|||10|µs|
|Time To Initialize,includingReset of Tx Fault|t_init|||300|ms|
|Tx Fault Assert Time|t_fault|||100|µs|
|Tx Disable To Reset|t_reset|10|||µs|
|LOS Assert Time|t_loss_on|||100|µs|
|LOS De-assert Time|t_loss_off|||100|µs|
|Serial ID Clock Rate|f_serial_clock|||400|KHz|
|MOD_DEF(0:2)-High|VH|2||Vcc|V|
|MOD_DEF(0:2)-Low|VL|||0.8|V|



## **5. Pin Definitions** 


sales@qsfptek.com 

3/5 

Rev1.0 


**----- Start of picture text -----**<br>
BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


**Pin Descriptions** 

|**Descriptions**|||||
|---|---|---|---|---|
|<br>**Pin**|**Signal Name**|**Description**|**Plug Seq.**|**Notes**|
|1|VEET|Transmitter Ground|1||
|2|TX FAULT|Transmitter Fault Indication|3|Note 1|
|3|TX DISABLE|Transmitter Disable|3|Note 2|
|4|MOD_DEF(2)|SDA Serial Data Signal|3|Note 3|
|5|MOD_DEF(1)|SCL Serial Clock Signal|3|Note 3|
|6|MOD_DEF(0)|TTL Low|3|Note 3|
|7|Rate Select|Not Connected|3||
|8|LOS|Loss of Signal|3|Note 4|
|9|VEER|Receiverground|1||
|10|VEER|Receiverground|1||
|11|VEER|Receiverground|1||
|12|RD-|Inv. Received Data Out|3|Note 5|
|13|RD+|Received Data Out|3|Note 5|
|14|VEER|Receiverground|1||
|15|VCCR|Receiver Power Supply|2||
|16|VCCT|Transmitter Power Supply|2||
|17|VEET|Transmitter Ground|1||
|18|TD+|Transmit Data In|3|Note 6|
|19|TD-|Inv. Transmit Data In|3|Note 6|
|20|VEET|Transmitter Ground|1||



## **Notes:** 

## Plug Seq.: Pin engagement sequence during hot plugging. 

- 1) TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; Logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

- 2) TX Disable is an input that is used to shut down the transmitter optical output. It is pulled up within the module with a 4.7k~10kΩ resistor. Its states are: 

Low (0 to 0.8V): Transmitter on (>0.8V, < 2.0V): Undefined High (2.0 to 3.465V): Transmitter Disabled Open: Transmitter Disabled 

- 3) Mod-Def 0,1,2. These are the module definition pins. They should be pulled up with a 4.7k~10kΩ resistor on the host board. The pull-up voltage shall be VccT or VccR. 

   - Mod-Def 0 is grounded by the module to indicate that the module is present Mod-Def 1 is the clock line of two wire serial interface for serial ID 

   - Mod-Def 2 is the data line of two wire serial interface for serial ID 

- 4) LOS is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor. Pull up voltage between 2.0V and Vcc+0.3V. Logic 1 indicates loss of signal; Logic 0 indicates normal operation. In the low state, the output will be pulled to less than 0.8V. 

- 5) RD-/+: These are the differential receiver outputs. They are internally AC-coupled 100 differential lines which should be terminated with 100Ω (differential) at the user SERDES. 

- 6) TD-/+: These are the differential transmitter inputs. They are internally AC-coupled, differential lines with 100Ω differential termination inside the module. 

sales@qsfptek.com 

4/5 

Rev1.0 


**----- Start of picture text -----**<br>
BIDI SFP 1550nm-TX/1310nm-RX 20KM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **6. Mechanical Dimensions** 


## **7. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|QT-WDM-0220BD|BIDI SFP,1.25 Gb/s,1550nm,SMF,20km,DDM,LC connector,0°C to +70°C|
|QT-WDM-0220BID|BIDI SFP,1.25 Gb/s,1550nm,SMF,20km,DDM,LC connector,-40°C to +85°C|



sales@qsfptek.com 

5/5 

Rev1.0 

