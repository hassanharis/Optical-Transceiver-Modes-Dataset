_**www.amphenol-cs.com/optics.html**_ **Draft 1.1** 

## **800G OSFP 2xDR4+ Transceiver** 

# **OP13LD8-02D** 

## **PRODUCT FEATURES** 

- Support 106.25 Gb/s Data rate per channel 

- Electrically hot-pluggable 

- Single 3.3V power supply 

- Integrated Silicon photonics modulator chip 


   - 1310nm High-power DFB Laser / 1310nm PIN Array for up to 2km reach over SMF 

- Digital Diagnostics Monitoring Interface 

- Dual Duplex MPO-12 optical receptacle 

- Case operating temperature range:0°C to 70°C 

- Power dissipation < 8.5 W（Typical 8W） 

- Be compliant to ROHS 

## **REFERENCE STANDARD** 

- Compliant to OSFP MSA rev5.0 

## **APPLICATIONS** 

- Compliant to OIF-CMIS rev5.0 

   - 800G Ethernet 

- Compliant to IEEE 802.3cu-2021 

OP13LD8-02D 800G OSFP 2xDR4+ transceiver modules are designed for use in 800G Ethernet links on up to 2km of single mode fiber. Forward error correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. They are compliant with the OSFP MSA, IEEE802.3cu, OIFCMIS. 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

## **PRODUCT SPECIFICATION** 

## I. **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power Supply Voltage|VCC|-0.5|-|3.6|V||
|Optical Receiver Damage<br>Thresholdinput|Pdmg|5.4|||dBm||



## II. **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0||70|ºC|Without air flow|
|Power Supply Voltage|VCC|3.135|3.3|3.465|V||
|Power Supply Current|ICC|||3030|mA|When Vcc is 3.3V|
|Data Rate|BR||53.125@PAM4||GBd|Each channel-<br>Optical|
|Transmission Distance|TD||-|2|km||
|Coupled fiber|Single mode fiber|||||9/125um SMF|



## III. **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Signaling Speed per Lane|||53.125 ± 100 ppm||GBd||
|Modulation format|||PAM4||||
|Wavelength Assignment|λ|1304.5||1317.5|nm|3|
|Total Output Average Launch Power|POUT|||10.4|dBm||
|Average Launch Power Per lane||-3.2||4.4|dBm||
|Transmit OMA per Lane(max)||||3.7|dBm||
|Transmit OMA per Lane(min)<br>for TDECQ<1.4dB<br>for 1.4dB≤TDECQ≤3.4dB||-0.2<br>-1.6+TDECQ|||dBm||
|Transmitter and Dispersion eye closure<br>for PAM4(TDECQ) each lane|TDECQ|||3.4|dB||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|
|---|---|---|---|---|---|---|
||||||||
|SMSR||30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Average launch Power off per lane|Poff|||-16|dBm||
|RIN17.1OMA (max)|RIN|||-136|dB/Hz||
|Transmitter Reflectance|Tr|||-26|dB||
|**Receiver**|||||||
|Signaling Speed per Lane|||53.125 ± 100 ppm||GBd||
|Modulation format|||PAM4||||
|Wavelength Assignment|λ|1304.5||1317.5|nm|3|
|Damage Threshold per Lane||5.4|||dBm|1|
|Receive Power (OMA) per Lane|ROMA|||3.7|dBm||
|Average Input Power per Channel|RXPx|-7.2||4.4|dBm||
|Receiver Sensitivity (OMA) per Lane<br>for TECQ<1.4 dB<br>for 1.4dB≤TECQ≤3.4dB|RXsens|||-4.6<br>-6+TECQ|dBm|2|
|Receiver Reflectance|Rr|||-26|dB||



## **Notes:** 

1：The receiver shall be able to tolerate, without damage, continuous exposure to an optical input signal having this average power level. 

-4 2：Measured with a PRBS31Q test pattern, BER@2.4*10 . 

3：The wavelength assignment is suitable for all channels. 

## **IV.Link Power Budget** 

|**IV. Link Power Budget**||||
|---|---|---|---|
|**Parameter**|**Typ**|**Unit**|**NOTE**|
|Power budget(for maximum TDECQ)|7.8|dB||
|Operating distance|2|km||
|Channel insertion loss|4|dB||
|Allocation for penalties(for maximum TDECQ)|3.8|dB||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

## **V. Pin Assignment** 


Figure1---Pin out of Connector Block on Host Board 

|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|GND|Ground|1|
|2|TX2p|Transmitter Data Non-Inverted||
|3|TX2n|Transmitter Data Inverted||
|4|GND|Ground|1|
|5|TX4p|Transmitter Data Non-Inverted||
|6|TX4n|Transmitter Data Inverted||
|7|GND|Ground|1|
|8|TX6p|Transmitter Data Non-Inverted||
|9|TX6n|Transmitter Data Inverted||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|
|---|---|---|---|
|||||
|10|GND|Ground|1|
|11|TX8p|Transmitter Data Non-Inverted||
|12|TX8n|Transmitter Data Inverted||
|13|GND|Ground|1|
|14|SCL|2-wire Serial interface clock|2|
|15|VCC|+3.3V Power||
|16|VCC|+3.3V Power||
|17|LPWn/PRSn|Low-Power Mode / Module Present||
|18|GND|Ground|1|
|19|RX7n|Receiver Data Inverted||
|20|RX7p|Receiver Data Non-Inverted||
|21|GND|Ground|1|
|22|RX5n|Receiver Data Inverted||
|23|RX5p|Receiver Data Non-Inverted||
|24|GND|Ground|1|
|25|RX3n|Receiver Data Inverted||
|26|RX3p|Receiver Data Non-Inverted||
|27|GND|Ground|1|
|28|RX1n|Receiver Data Inverted||
|29|RX1p|Receiver Data Non-Inverted||
|30|GND|Ground|1|
|31|GND|Ground|1|
|32|RX2p|Receiver Data Non-Inverted||
|33|RX2n|Receiver Data Inverted||
|34|GND|Ground|1|
|35|RX4p|Receiver Data Non-Inverted||
|36|RX4n|Receiver Data Inverted||
|37|GND|Ground|1|
|38|RX6p|Receiver Data Non-Inverted||
|39|RX6n|Receiver Data Inverted||
|40|GND|Ground|1|
|41|RX8p|Receiver Data Non-Inverted||
|42|RX8n|Receiver Data Inverted||
|43|GND|Ground|1|
|44|INT/RSTn|Module Interrupt / Module Reset||
|45|VCC|+3.3V Power||
|46|VCC|+3.3V Power||
|47|SDA|2-wire Serial interface data|2|
|48|GND|Ground|1|



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|**Rev 1.1**|
|---|---|---|---|
|||||
|49|TX7n|Transmitter Data Inverted||
|50|TX7p|Transmitter Data Non-Inverted||
|51|GND|Ground|1|
|52|TX5n|Transmitter Data Inverted||
|53|TX5p|Transmitter Data Non-Inverted||
|54|GND|Ground|1|
|55|TX3n|Transmitter Data Inverted||
|56|TX3p|Transmitter Data Non-Inverted||
|57|GND|Ground|1|
|58|TX1n|Transmitter Data Inverted||
|59|TX1p|Transmitter Data Non-Inverted||
|60|GND|Ground|1|



## **Notes:** 

1. OSFP uses common ground (GND) for all signals and supply (power). All are common within the OSFP module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signalcommon ground plane. 

2. Open-Drain with pull-up resistor on Host. 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

## **VI. Host - Transceiver Interface Block Diagram** 


**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


Figure2--- Host - Transceiver Interface Block Diagram 

## **Notes:** 

1. LPO module does not have a CDR 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

## **VII. Mechanical Specifications** 


Figure3--- Mechanical Specifications 

## **VIII. Regulatory Compliance** 

|**Feature**|**Reference**|**Performance**|
|---|---|---|
|Electrostatic discharge（ESD）|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic Interference (EMI)|FCC Part 15 Class B EN 55022 Class B<br>(CISPR 22A)|Compatible with standards|
|Laser Eye Safety|FDA 21CFR 1040.10, 1040.11 IEC/EN<br>60825-1, 2|Class 1 laser product|
|Component Recognition|IEC/EN 60950, UL|Compatible with standards|
|ROHS|2011/65/EU and 2015/863/EU|Compatible with standards|
|REACH|Regulation(EC) No.1907/2006|Compatible with standards|
|EMC|EN61000-3|Compatible with standards|



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

_**www.amphenol-cs.com/optics.html**_ 

**Rev 1.1** 

## **Warnings** 

Handling Precautions: This device is susceptible to damage as a result of electrostatic discharge (ESD). A static free environment is highly recommended. Follow guidelines according to proper ESD procedures. Laser Safety: Radiation emitted by laser devices can be dangerous to human eyes. Avoid eye exposure to direct or indirect radiation. 

## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|1.0|2023-12-05|Draft version|
|1.1|2023-12-11|Modify product features|



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

