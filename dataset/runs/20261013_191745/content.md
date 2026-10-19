
**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **10GBASE-ZR SFP+ 1550nm 80km Transceiver** 

## **P/N: QT-SFP+-ZR** 

## **PRODUCT FEATURES** 

- Compliant with SFF-8413 and IEE802.3ae 

- Data rate selectable ≤4.25Gbps or 9.95Gbps to 10.3Gbps bit rates 

- Cooled EML transmitter and PIN receiver 

- link length up to 80km 

- Low Power Dissipation 1.5W Maximum 

- -5ºC to 70ºC Operating Case Temperature 

- Single 3.3V power supply 

- Diagnostic Performance Monitoring of module temperature, supply 

- Voltages, laser bias current, transmit optical power, receive optical power 

- RoHS compliant and lead free 

- Duplex LC receptacle 

- RoHS compliant and lead free 

## **APPLICATIONS** 

- 10GBASE-ER/EW (with/without FEC) 

- 10G Fiber Channel (with/without FEC) 

- Other optical links 

sales@qsfptek.com 

1/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1. Absolute maximum rating** 

These values represent the damage threshold of the module.Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. 

|rating Conditions.||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max.**|**Unit**|
|Storage Temperature|TS|-40||+85|°C|
|Case OperatingTemperature|TA|0||70|°C|
|Maximum SupplyVoltage|Vcc|-0.5||4|V|
|Relative Humidity|RH|0||85|%|



## **2. Optical characteristics** 

The following optical characteristics are defined over the Recommended Operating Environment unless otherwise specified. 

|ified.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max.**|**Unit**|**Note**|
|**Transmitter Section:**|||||||
|Center Wavelength|λt|1530|1550|1565|nm||
|spectral width|△λ|||0.3|nm||
|Average Optical Power|Pavg|0||+5|dBm|1|
|Optical Power OMA|Poma|-2.1|||dBm||
|Laser Off Power|Poff|||-30|dBm||
|Extinction Ratio|ER|8.2|||dB||
|Transmitter Dispersion Penalty|TDP|||3.0|dB|2|
|Relative IntensityNoise|Rin|||-128|dB/Hz|3|
|Optical Return Loss Tolerance||21|||dB||
|**Receiver Section:**|||||||
|Center Wavelength|λr|1260||1600|nm||
|Receiver Sensitivity|Sen|||-24|dBm|4|
|Los Assert|LOSA|-34||-|dBm||
|Los Dessert|LOSD|||-25|dBm||
|Los Hysteresis|LOSH|0.5|||dB||
|Overload|Sat|-7|||dBm|5|
|Receiver Reflectance|Rrx|||-26|dB||



## Notes : 

- 1.Trade-offs are available between spectral width, center wavelength and minimum OMA. 

2. The optical power is launched into MMF 

3. Measured with a PRBS 2[31] -1 test pattern @10.3125Gbps 

4. Measured with a PRBS 2[31] -1 test pattern @10.3125Gbps, BER≤10[-12.] 

sales@qsfptek.com 

2/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **3. Electrical characteristics** 

The following electrical characteristics are defined over the Recommended Operating Environment unless otherwise specified. 

|ified.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max.**|**Unit**|**Note**|
|Supply Voltage|Vcc|3.135||3.465|V||
|Supply Current|Icc|||500|mA||
|Power Consumption|P|||1.8|W||
|**Transmitter Section**|||||||
|Input differential impedance|Rin||100||Ω|1|
|Tx Input Single Ended DC Voltage<br>Tolerance (Ref VeeT)|V|-0.3||4|V||
|Differential input voltage swing|Vin,pp|180||700|mV|2|
|Transmit Disable Voltage|VD|2||Vcc|V|3|
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|V||
|**Receiver Section**|||||||
|Single Ended Output Voltage Tolerance|V|-0.3||4|V||
|Rx Output Diff Voltage|Vo|300||850|mV||
|Rx Output Rise and Fall Time|Tr/Tf|30|||ps|4|
|LOS Fault|VLOS<br>fault|2||VccHOST|V|5|
|LOS Normal|VLOS<br>norm|Vee||Vee+0.8|V|5|



Notes : 

- 1.TX data input pins. AC coupling. 

2. Into 100 ohms differential termination. 

sales@qsfptek.com 

3/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **4. Pin definition** 

The SFP+ modules are hot-pluggable. Hot pluggable refers to plugging in or unplugging a module while the host board is powered. The SFP+ host connector is a 0.8 mm pitch 20 position right angle improved connector specified by SFF-8083, or stacked connector with equivalent with equivalent electrical performance. Host PCB contact assignment is shown in Figure 2 and contact definitions are given in Table 2. SFP+ module contacts mates with the host in the order of ground, power, followed by signal as illustrated by Figure 3 and the contact sequence order listed in Table 2. 


Figure 1: Interface to Host PCB 


Figure2: Module Contact Assignment 

sales@qsfptek.com 

4/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **Pin Descriptions** 

|**Pin**|**Symbol**|**Description**|**Ref.**|
|---|---|---|---|
|1|VEET|Transmitter Ground(Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line(MOD-DEF2)|4|
|5|SCA|2-wire Serial Interface Clock(MOD-DEF1)|4|
|6|MOD_ABS|Module Absent,connected to VEET or VEER|4|
|7|RS0|No connection required||
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|RS1|No connection required||
|10|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled||
|14|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground(Common with Receiver Ground)|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground(Common with Receiver Ground)|1|



Notes: 

1. Circuit ground is internally isolated from chassis ground. 

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 

5. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

sales@qsfptek.com 

5/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-ZR 1550nm 80km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **5. Mechanical Specifications** 


## **6. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|QT-SFP+-ZR|SFP+,10Gbps,1550nm,SMF,80KM,DDM,LC connector,<br>-5 °C ~ 70 °C|
|QT-SFP+-SR|SFP+,10Gbps,850nm,MMF,300M,DDM,LC connector,<br>0 °C ~ 70 °C|
|QT-SFP+-LR|SFP+,10Gbps,1310nm,SMF,10KM, DDM,LC connector,<br>0 °C ~ 70 °C|
|QT-SFP+-ER|SFP+,10Gbps,1550nm,SMF,40KM, DDM,LC connector,<br>-5 °C ~ 70 °C|



sales@qsfptek.com 

6/6 

Rev1.0 

