
**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver** 

## **P/N: DWDM-SFP+-ZR-XX** 

## **PRODUCT FEATURES** 

- Compliant with SFF-8413 and IEE802.3ae 

- Suitable for use in 100GHz channel spacing DWDM systems 

- Data rate selectable ≤4.25Gbps or 9.95Gbps to 10.3Gbps bit rates 

- Cooled EML transmitter and PIN receiver 

- link length up to 80km 

- Low Power Dissipation 1.5W Maximum 

- -5ºC to 70ºC Operating Case Temperature 

- Single 3.3V power supply 

- Diagnostic Performance Monitoring of module temperature, supply 

- Voltages, laser bias current, transmit optical power, receive optical power 

- RoHS compliant and lead free 

## **APPLICATIONS** 

- 10G Ethernet 

- 10G Fiber Channel (with/without FEC) 

sales@qsfptek.com 

1/6 

Rev1.0 


**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|SupplyVoltage|Vcc|-0.5|3.8|V|
|Storage Temperature|Tst|-40|85|ºC|
|Relative Humidity|Rh|0|85|%|



## **2. Operating Conditions** 

|**Operating Conditions**||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|SupplyVoltage|Vcc|3.13|3.3|3.47|V|
|Supplycurrent|Icc||420|610|mA|
|OperatingCase temperature|Tca|-5|-|70|ºC|
|Module Power Dissipation|Pm|-|1.4|2|W|



## Notes: 

[1] Supply current is shared between VCCTX and VCCRX. 

[2] In-rush is defined as current level above steady state current requirements. 

## **3. Transmitter Specification-Optical** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Center Wavelength(SOL)△|c|c-25|c|c+25|pm|
|Center Wavelength(EOL)▲|c|c-100|c|c+100|pm|
|OpticalOMAPower|Pom|-1|||dBm|
|Side Mode Suppression Ratio|SMSR|30|-|-|dB|
|Optical Transmit Power(disabled)|PTX_DISABLE|-|-|-30|dBm|
|Extinction Ratio|ER|9||-|dB|
|RIN21OMA [1]||||-128|dB/Hz|
|Optical Return Loss Tolerance||||21|dB|



## Notes: 

[1] RIN measurement is made with a return loss at 21 dB. 

▲Laser- Start of Life 

▲Laser End of life 

## **4. Transmitter Specification-Electrical** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Data Rate|Mra|-|10.3|11.3|Gbps|
|Input differential impedance|Rim|-|100|-|Ω|
|Differential data Input|VtxDIFF|120|-|850|mV|
|Transmit Disable Voltage|VD|2.0|-|Vcc3+0.3|V|
|Transmit Enable Voltage|Ven|0|-|+0.8|V|
|Transmit Disable Assert<br>Time|Vn|-|-|100|us|



sales@qsfptek.com 

2/6 

Rev1.0 


**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **5. Receiver Specification-Optical** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Input OperatingWavelength|λ|1260|-|1620|nm|
|Receiver sensitivity[1]||-|-|-24|dBm|
|Maximum Input Power|RX-overload|-|-|-8|dBm|
|Loss of Signal Asserted||-34|-|-|dBm|
|LOS De-Asserted||-|-|-24|dBm|
|LOS Hysteresis||0.5|-|-|dB|



Notes: 

- [1] Measured with conformance test signal for BER = 10[–12] . The stressed sensitivity values in the table are for system level BER measurements which include the effects of CDR circuits. It is recommended that at least 0.4 dB additional margin be allocated if component level measurements are made without the effects of CDR circuits. 

## **6. Receiver Specification-Electrical** 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Data Rate|Mra|-|10.3|11.3|Gbps|
|Differential Output<br>Swing|Vout P-P|350|-|850|mV|
|Rise/Fall Time|Tr / Tf|24|-|-|ps|
|Loss of Signal –<br>Asserted|VOH|2|-|Vcc3+0.3-|V|
|Loss of Signal –<br>Negated|VOL|0|-|+0.4|V|



## **7. Pin Description** 


sales@qsfptek.com 

3/6 

Rev1.0 


**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|**Pin**|**Symbol**|**Name/Description**|
|---|---|---|
|1|VEET[1]|Transmitter Ground|
|2|Tx_FAULT[2]|Transmitter Fault|
|3|Tx_DIS<br>[3]|Transmitter Disable. Laser output disabled on high or open|
|4|SDA[2]|2-wire Serial Interface Data Line|
|5|SCL[2]|2-wire Serial Interface Clock Line|
|6|MOD_ABS[4]|Module Absent. Grounded within the module|
|7|RS0 [5]|RS0 for Rate Select: Open or Low = Module supports ≤4.25Gbps<br>High=Module supports 9.95 Gb/s to 10.3125 Gb/s|
|8|RX_LOS[2]|Loss of Signal indication. Logic 0 indicates normal operation|
|9|RS1[5]|No connection required|
|10|VEER[1]|Receiver Ground|
|11|VEER[1]|Receiver Ground|
|12|RD-|Receiver Inverted DATA out. AC Coupled|
|13|RD+|Receiver DATA out. AC Coupled|
|14|VEER[1]|Receiver Ground|
|15|VCCR|Receiver Power Supply|
|16|VCCT|Transmitter Power Supply|
|17|VEET[1]|Transmitter Ground|
|18|TD+|Transmitter DATA in. AC Coupled|
|19|TD-|Transmitter Inverted DATA in. AC Coupled|
|20|VEET[1]|Transmitter Ground|



## Notes: 

[1] Module circuit ground is isolated from module chassis ground within the module. [2].should be pulled up with 4.7k – 10k ohms on host board to a voltage between 3.15Vand 3.6V. 

[3]Tx_Disable is an input contact with a 4.7 kΩ to 10 kΩ pullup to VccT inside the module. 

[4]Mod_ABS is connected to VeeT or VeeR in the SFP+ module. The host may pull this contact up to Vcc_Host with a resistor in the range 4.7 kΩ to10 kΩ.Mod_ABS is asserted “High” when the SFP+ module is physically absent from a host slot. 

[5] RS0 and RS1 are module inputs and are pulled low to VeeT with > 30 kΩ resistors in the module. 

## **8. C-band λc Wavelength Guide** 

|**ITU Channel**<br>**Product Code**|**Frequency(THz)**|**Wavelength**|**ITU Channel**<br>**Product Code**|**Frequency(THz)**|**Wavelength**|
|---|---|---|---|---|---|
|17|191.7|1563.86|40|194.0|1545.32|
|18|191.8|1563.05|41|194.1|1544.53|
|19|191.9|1562.23|42|194.2|1543.73|
|20|192.0|1561.42|43|194.3|1542.94|
|21|192.1|1560.61|44|194.4|1542.14|
|22|192.2|1559.79|45|194.5|1541.35|
|23|192.3|1558.98|46|194.6|1540.56|
|24|192.4|1558.17|47|194.7|1539.77|
|25|192.5|1557.36|48|194.8|1538.98|



sales@qsfptek.com 

4/6 

Rev1.0 


**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|26|192.6|1556.55|49|194.9|1538.19|
|---|---|---|---|---|---|
|27|192.7|1555.75|50|195.0|1537.40|
|28|192.8|1554.94|51|195.1|1536.61|
|29|192.9|1554.13|52|195.2|1535.82|
|30|193.0|1553.33|53|195.3|1535.04|
|31|193.1|1552.52|54|195.4|1534.25|
|32|193.2|1551.72|55|195.5|1533.47|
|33|193.3|1550.92|56|195.6|1532.68|
|34|193.4|1550.12|57|195.7|1531.90|
|35|193.5|1549.32|58|195.8|1531.12|
|36|193.6|1548.51|59|195.9|1530.33|
|37|193.7|1547.72|60|196.0|1529.55|
|38|193.8|1546.92|61|196.1|1528.77|
|39|193.9|1546.12||||



## **9. Mechanical Specifications** 


sales@qsfptek.com 

5/6 

Rev1.0 


**----- Start of picture text -----**<br>
DWDM SFP+ CH17~CH61 80km DDM LC SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **10. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|DWDM-SFP+-ZR-XX|SFP+,10Gbps ,SMF,80KM, DDM,LC connector, -5℃~ +70℃，XX= ITU Grid<br>17~61,|



sales@qsfptek.com 

6/6 

Rev1.0 

