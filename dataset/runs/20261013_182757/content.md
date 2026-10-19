
**----- Start of picture text -----**<br>
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **10GBASE-SR SFP+ 850nm 300m Transceiver** 

## **P/N: QT-SFP+-SR** 

## **PRODUCT FEATURES** 

- Optical interface compliant to IEEE 802.3ae 10GBASE-SR 

- Electrical interface compliant to SFF-8431 

- Hot Pluggable 

- 850nm VCSEL transmitter, PIN photo-detector 

- Maximum link length of 300m on 2000MHz/km MMF 

- Operating case temperature: Commercial: 0 to 70 °C , Industrial:-40 to 85 °C 

- All-metal housing for superior EMI performance 

- Advanced firmware allow customer system encryption information to be stored in transceiver 

- Cost effective SFP+ solution, enables higher port densities and greater bandwidth 

- Duplex LC receptacle 

- RoHS compliant and lead free 

## **APPLICATIONS** 

- 10GBASE-SR at 10.3125Gbps 

- 10GBASE-SW at 9.953Gbps 

- Other optical links 

sales@qsfptek.com 

1/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1. Absolute maximum rating** 

These values represent the damage threshold of the module.Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. 

|ommended Operating Conditions.|||||
|---|---|---|---|---|
|**Parameters**|**Symbol**|**Min.**|**Max.**|**Unit**|
|Power Supply Voltage|VCC|0|+3.6|V|
|Storage Temperature|Tc|-40|+85|°C|
|Operating Case Temperature|Tc|-5|+75|°C|
|Relative Humidity|RH|5|95|%|
|RX Input Average Power|Pmax|-|0|dBm|



## **2. Optical characteristics** 

The following optical characteristics are defined over the Recommended Operating Environment unless otherwise specified. 

|ified.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max**|**Unit**|**Notes**|
|Transmitter|||||||
|Center Wavelength|λt|840|850|860|nm||
|RMS spectral width|Pm|-|-|Note 1|nm||
|Average Optical Power|Pavg|-6.5|-|-0.5|dBm|2|
|Extinction Ratio|ER|3.5|-|-|dB|3|
|Transmitter Dispersion<br>Penalty|TDP|-|-|3.9|dB||
|Relative Intensity Noise|Rin|-|-|-128|dB/Hz|12dB reflection|
|Optical Return Loss Tolerance||-|-|12|dB||
|**Receiver**|||||||
|Center Wavelength|λr|840|850|860|nm||
|Receiver Sensitivity|Psens|-|-|-11.1|dBm|4|
|Stressed Sensitivity in OMA||-|-|-7.5|dBm|4|
|Los function|Los|-30|-|-12|dBm||
|Overload|Pin|-|-|-1.0|dBm|4|
|Receiver Reflectance||-|-|-12|dB||



## Note 

- 1.Trade-offs are available between spectral width, center wavelength and minimum OMA, as shown in table 6. 

2. The optical power is launched into MMF 

3. Measured with a PRBS 2[31] -1 test pattern @10.3125Gbps 

4. Measured with a PRBS 2[31] -1 test pattern @10.3125Gbps, BER≤10[-12.] 

sales@qsfptek.com 

2/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **3. Electrical characteristics** 

The following electrical characteristics are defined over the Recommended Operating Environment unless otherwise specified. 

|ified.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max**|**Unit**|**Notes**|
|Data Rate||-|10.3125|-|Gbps||
|Power Consumption||-|600|800|mW||
|**Transmitter**|||||||
|Single Ended Output Voltage Tolerance||-0.3|-|4.0|V||
|C common mode voltage tolerance||15|-|-|mV||
|Tx Input Diff Voltage|VI|180||1200|mV||
|Tx Fault|VoL|-0.3||0.4|V|At 0.7mA|
|Data Dependent Input Jitter|DDJ|||0.10|UI||
|Data Input Total Jitter|TJ|||0.28|UI||
|**Receiver**|||||||
|Single Ended Output Voltage Tolerance||-0.3|-|4.0|V||
|Rx Output Diff Voltage|Vo|300||850|mV||
|Rx Output Rise and Fall Time|Tr/Tf|30|||ps|20% to 80%|
|Total Jitter|TJ|||0.70|UI||
|Deterministic Jitter|DJ|||0.42|UI||



Notes : 

- 1.TX data input pins. AC coupling. 

2. Into 100 ohms differential termination. 

sales@qsfptek.com 

3/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **4. Pin definition** 

The SFP+ modules are hot-pluggable. Hot pluggable refers to plugging in or unplugging a module while the host board is powered. The SFP+ host connector is a 0.8 mm pitch 20 position right angle improved connector specified by SFF-8083, or stacked connector with equivalent with equivalent electrical performance. Host PCB contact assignment is shown in Figure 2 and contact definitions are given in Table 2. SFP+ module contacts mates with the host in the order of ground, power, followed by signal as illustrated by Figure 3 and the contact sequence order listed in Table 2. 


Figure 1: Interface to Host PCB 


Figure2: Module Contact Assignment 

sales@qsfptek.com 

4/6 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Description**|**Ref.**|
|---|---|---|---|
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|4|
|5|SCA|2-wire Serial Interface Clock (MOD-DEF1)|4|
|6|MOD_ABS|Module Absent, connected to VEET or VEER|4|
|7|RS0|No connection required||
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|RS1|No connection required||
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
SFP+ 10GASE-SR 850nm 300M Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **5. Mechanical Specifications** 


## **6. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|QT-SFP+-SR|SFP+,10Gbps,850nm,MMF,300M,DDM,LC connector,<br>0 °C ~ 70 °C|
|QT-SFP+-LR|SFP+,10Gbps,1310nm,SMF,10KM,DDM,LC connector,<br>0 °C ~ 70 °C|
|QT-SFP+-ER|SFP+,10Gbps,1550nm,SMF,40KM,DDM,LC connector,<br>-5 °C ~ 70 °C|



sales@qsfptek.com 

6/6 

Rev1.0 

