
**----- Start of picture text -----**<br>
25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver** 

# **P/N: QT-SFP28-LR** 

## **PRODUCT FEATURES** 

- Up to 28Gbps Data Links 

- Up to 10km transmission on SMF 

- DFB Laser and PIN receiver 

- Metal enclosure, for lower EMI 

- 2-wire interface with integrated Digital Diagnostic monitoring 

- Specifications compliant with SFF 8472 

- Compliant with SFP+ MSA with LC connector 

- Single 3.3V power supply 

- Power dissipation < 1.0 W 

- Case operating temperature range: 0°C to +70°C 

- Compliant to SFF-8431 

- RoHS Compliant 

## **APPLICATIONS** 

- 25G Ethernet 

- Data center and Fiber channel 

sales@qsfptek.com 

1/5 

Rev1.0 


**----- Start of picture text -----**<br>
25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1 Absolute Maximum Ratings** 

|**Absolute Maximum Ratings**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power SupplyVoltage|VCC|-0.3|-|4|V||



## **2. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Tcase|0|-|70|ºC|Commercial|
|Power SupplyVoltage|VCC|3.14|3.3|3.47|V||
|Power SupplyCurrent|ICC|-||300|mA||
|Data Rate|BR||25.78||Gbps||
|Transmission Distance|TD||-|10|km||
|Coupled fiber|Single mode fiber|||9/125um SMF|||



## **3. Optical Characteristics** 

|**. Optical Characteristics**|||||||
|---|---|---|---|---|---|---|
|<br>**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|Transmitter|||||||
|Output Opt. Power|POUT|-7||2|dBm|1|
|Optical Wavelength|λ|1260|1310|1355|nm||
|Spectral Width(-20dB)|σ|||1|nm||
|Optical Extinction Ratio|ER|3.5|||dB||
|Receiver|||||||
|Rx Sensitivity|RSENS|||-11|dBm|2|
|Input Saturation Power (Overload)|Psat|0.5|||dBm||
|Wavelength Range|λ<br>C|1270||1610|nm||
|LOS De -Assert|LOSD|||-13|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|1.0||dB||



## **Notes:** 

1. Class 1 Laser Safety per FDA/CDRH and IEC-825-1 regulations. 2. Measured with a PRBS 2[31] -1 test pattern, @25.78Gb/s, BER<10[-][12] . 

## **4. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|SupplyVoltage|Vcc|3.14|3.3|3.46|V||
|SupplyCurrent|Icc|||300|mA||
|Transmitter|||||||



sales@qsfptek.com 

2/5 

Rev1.0 


**----- Start of picture text -----**<br>
25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|Input differential impedance|Rin||100||Ω|1|
|---|---|---|---|---|---|---|
|Single ended data input swing|Vin,pp|180||700|mV||
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
|Transmit Disable Assert Time||||10|us||
|Receiver|||||||
|Differential data output swing|Vout,pp|300||850|mV|3|
|Data output rise time|tr|28|||ps|4|
|Data output fall time|tf|28|||ps|4|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|5|
|LOS Normal|VLOS<br>norm|Vee||Vee+0.8|V|5|
|Power SupplyRejection|PSR|100|||mVpp|6|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupled thereafter. 

2. Or open circuit. 

3. Into 100 ohms differential termination. 

4. 20 – 80 %. 

5. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

6. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specifiedvalue applied through the recommended power supply filtering network. 

## **5. Pin Assignment** 


**Pin out of Connector Block on Host Board** 

sales@qsfptek.com 

3/5 

Rev1.0 


**----- Start of picture text -----**<br>
25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **Pin Definition** 

|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|VEET|Transmitter Ground(Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|4|
|5|SCL|2-wire Serial Interface Clock Line|4|
|6|MOD_ABS|Module Absent. Grounded within the module|4|
|7|RS0|Rate Select 0|5|
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
|9|RS1|No connection required|1|
|10|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled||
|14|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground (Common with Receiver Ground)|1|



## **Notes:** 

1. Circuit ground is internally isolated from chassis ground. 

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V.A high output indicates atransmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarmthreshold. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabledonTDIS>2.0V or open, enabled on TDIS<0.8V. 

4. Should be pulled up with 4.7kΩ- 10kΩhost board to a voltage between 2.0V and 3.6V. MOD_ABS pulls linelow to indicate module is plugged in. 

5. Internally pulled down per SFF-8431 Rev 4.1. 

6. LOS is open collector output. It should be pulled up with 4.7kΩ– 10kΩon host board to a voltage between 2.0Vand 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

sales@qsfptek.com 

4/5 

Rev1.0 


**----- Start of picture text -----**<br>
25GBASE-LR SFP28 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **6. Outline Dimensions** 



## **7. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|QT-SFP28-LR|SFP28,28Gb/s,1310nm,SMF,10KM,LC connector,0°C to +70°C|
|QT-SFP28-SR|SFP28,28Gb/s,850nm,MMF,100M,LC connector,0°C to +70°C|
|QT-SFP28-ER|SFP28,28Gb/s,1310nm,SMF,40KM,LC connector,0°C to +70°C|



sales@qsfptek.com 

5/5 

Rev1.0 

