**Draft 1.0** 

## _**www.amphenol-cs.com/optics.html**_ 

## **1.6T 2xDR4 OSFP (Retimer)** 

## **OP13PI8-005D** 

## **PRODUCT FEATURES** 

- Support 212.5 Gb/s Data rate per channel 

- Electrically hot-pluggable 

- Single 3.3V power supply 

- Digital Diagnostics Monitoring Interface 

- DUAL MPO-12 

- Case operating temperature range:0°C to 70°C 

- Power dissipation < 30W 


- Integrated 1310nm DFB laser and Silicon photonics modulator chip / PIN receiver 

- Be compliant to ROHS 

## **REFERENCE STANDARD** 

- Refer to OSFP MSA rev5.0 

- Refer to OIF-CMIS rev5.1 

- Refer to IEEE 802.3dj-2024 

## **APPLICATIONS** 

##  1.6T Ethernet 

OP13PI8-005D 2x800G-DR4 OSFP modules are designed for use in 1.6T Ethernet links on up to 500m of single mode fiber. Forward error correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. They are compliant with the OSFP MSA, IEEE802.3dj, OIF-CMIS. 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

**Draft 1.0** 

## _**www.amphenol-cs.com/optics.html**_ 

## **PRODUCT SPECIFICATION** 

## I. **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|85|%||
|Power Supply Voltage|VCC|-0.5|-|3.6|V||
|Optical Receiver Damage<br>Thresholdinput, each lane|Pdmg|5.0|||dBm||



## II. **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0||70|ºC||
|Power Supply Voltage|VCC|3.135|3.3|3.465|V||
|Power Supply Current|ICC|||9090|mA|When Vcc is 3.3V|
|Data Rate|BR||106.25@PAM4||GBd|Each channel-<br>Optical|
|Transmission Distance|TD|-|-|500|m||



## III. **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Signaling Speed per Lane|||106.25<br>± 50 ppm||GBd||
|Modulation format|||PAM4||||
|Wavelength Assignment|λ|1304.5||1317.5|nm|3|
|Average Launch Power Per lane||-2.8||4.0|dBm||
|Transmit OMA per Lane(max)||||4.2|dBm||
|Transmit OMA per Lane(min)<br>for max(TECQ,TDECQ)<0.9dB<br>for 0.9dB≤max(TECQ,TDECQ)≤<br>3.4dB||-0.3<br>-1.2+max(TECQ,<br>TDECQ)|||dBm||
|Transmitter and Dispersion eye<br>closure for PAM4(TDECQ) each<br>lane|TDECQ|||3.4|dB||
|TECQ(max)||||3.4|dB||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

## _**www.amphenol-cs.com/optics.html**_ 

## **Draft 1.0** 

|│TDECQ-TECQ│(max)||||2.5|dB||
|---|---|---|---|---|---|---|
|Transmitter overshoot and<br>undershoot(max)||||22|%||
|SMSR||30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Average launch Power off per lane|Poff|||-15|dBm||
|RIN21.4OMA (max)|RIN|||-139|dB/Hz||
|Optical return loss tolerance(max)||||21.4|dB||
|Transmitter Reflectance|Tr|||-26|dB||
|**Receiver**|||||||
|Signaling Speed per Lane|||106.25<br>± 50ppm||GBd||
|Modulation format|||PAM4||||
|Wavelength Assignment|λ|1304.5||1317.5|nm|3|
|Damage Threshold per Lane||5.0|||dBm|1|
|Receive Power (OMA) per Lane|ROMA|||4.2|dBm||
|Average Input Power per Channel|RXPx|-5.8||4.0|dBm||
|Receiver Sensitivity (OMA) per<br>Lane<br>for TECQ<0.9 dB<br>for 0.9dB≤TECQ≤SECQ|RXsens|||-3.4<br>-4.3+TECQ|dBm|2|
|Stressed receiver<br>sensitivity(OMAouter),each lane||||-0.9|dBm|3|
|Stressed eye closure receiver<br>sensitivity test||||3.4|dB|4|
|OMAouter of each aggressor lane|||2.9||dBm||
|Receiver Reflectance|Rr||-26||dB||



## **Notes:** 

1. The receiver shall be able to tolerate, without damage, continuous exposure to an optical input signal having this average power level. 

2. Measured with a PRBS31Q test pattern, BER@2.4*10-4. 

3. The wavelength assignment is suitable for all channels. 

## IV. **Link Power Budget** 

|IV. **Link Power Budget**||||
|---|---|---|---|
|**Parameter**|**Typ**|**Unit**|**NOTE**|
|Power budget(for maximum TDECQ)|6.5|dB||
|Operating distance|500|m||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

## _**www.amphenol-cs.com/optics.html**_ 

**Draft 1.0** 

|Channel insertion loss|4|dB||
|---|---|---|---|
|Allocation for penalties(for maximum TDECQ)|TBD|dB||



## V. **Pin Assignment** 


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

## _**www.amphenol-cs.com/optics.html**_ 

## **Draft 1.0** 

|10|GND|Ground|1|
|---|---|---|---|
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
|49|TX7n|Transmitter Data Inverted||



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

## _**www.amphenol-cs.com/optics.html**_ 

**Draft 1.0** 

|50|TX7p|Transmitter Data Non-Inverted||
|---|---|---|---|
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

## VI. **Host - Transceiver Interface Block Diagram** 


Figure2--- Host - Transceiver Interface Block Diagram 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

**Draft 1.0** 

## _**www.amphenol-cs.com/optics.html**_ 

## VII. **Mechanical Specifications** 

Figure3--- Mechanical Specifications 

## VIII. **Regulatory Compliance** 

|**Feature**|**Reference**|**Performance**|
|---|---|---|
|Electrostatic discharge（ESD）|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic Interference (EMI)|FCC Part 15 Class B /EN 55022 Class B<br>(CISPR 22A)|Compatible with standards|
|Laser Eye Safety|FDA 21CFR 1040.10, 1040.11 IEC/EN<br>60825-1, 2|Class 1 laser product|
|Component Recognition|IEC/EN 62368-1, UL62368-1|Compatible with standards|
|ROHS|2011/65/EU and 2015/863/EU|Compatible with standards|
|REACH|Regulation(EC) No.1907/2006|Compatible with standards|



## **Warnings** 

Handling Precautions: This device is susceptible to damage as a result of electrostatic discharge (ESD). A static free environment is highly recommended. Follow guidelines according to proper ESD procedures. Laser Safety: Radiation emitted by laser devices can be dangerous to human eyes. Avoid eye exposure to direct or indirect radiation. 

**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

**Draft 1.0** 

## _**www.amphenol-cs.com/optics.html**_ 

## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|1.0|2024-8-20|Draft version|



**XGIGA Communication Technology Co.,ltd                      https://www.amphenol-cs.com/optics.html** 

