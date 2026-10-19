DATASHEET 

6.3 

**QSFP-DD 400G SR4.2 MPO, CMIS5.1** QSFP-DD SR4.2 400G Ethernet, PAM4 CMIS5.1, 4x 100G-SR1.2 100m 2.1dB MPO 

## TQD022-MS2C-SO 

The TQD022-MS2C-SO is a QSFP-DD form-factor transceivers for 400Gbps Ethernet applications. The intended use is intra-data center interconnect between switches, routers, storage equipment etc. for optical distances up to 100m over a MultiMode (MM) ribbon fiber cable. 

The electrical interface consists of eight 53.125G signals (400GAUI-8) that are converted to eight BiDi PAM4-modulated channels/lanes to transport the Ethernet signal. The channels are transported as 8lanes of 100G SR1.2 signals with wavelengths of 850 and 908nm. The transceiver can also be used in 4x100GAUI-2 mode to enable 400G to 4x 100G break-out configurations together with the 100G SR1.2 transceiver TQ2016-MS2C-SO. 

Digital diagnostics functions are available via an I2C interface, as specified by the QSFP-DD MSA. The optical interface to the transceiver is an MPO12 connector. 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio  (BER) of 2.4 x 10-4. 

The TQD022-MS2C-SO is compliant with Common Management Interface Specification CMIS5.1. 

## TECHNICAL DATA 

|**Parameter**|**Value**<br>Grey QSFP-DD<br>MM (MPO-12 UPC)<br>100m @ OM4<br>850/908nm<br>100G SR4.2<br>400GAUI-8 or 4x100GAUI-2<br>425Gbps1)<br>26.56Gbd2)<br>400GbE, 4x100GbE<br>0 – 2.1dB<br>< 12W<br>0°C to +70°C<br>-40°C to +85°C<br>mative and not the principal<br>power below this value cannot<br>this does not ensure|**Parameter**|**Value**|
|---|---|---|---|
|Technology||**Transmitter data:**||
|Transmission media||Output power, per lane|Min: -6.5dBm3)|
|Typical reach|||Max: +4.0dBm|
|Nominal wavelength||Output power, OMA, per lane|Min: -4.5dBm|
|Interface standards|||Max: +3.0dBm|
|Electrical interfaces||ER|Min: 3dB|
|Bit rate support||Transmit wavelength|840 – 868nm, 900-918nm|
|||**Receiver data:**||
|Protocol support||Receiver sensitivity, OMA, per lane|-6.6dBm4)|
|Power budget||Minimum input power, per lane|-8.5dBm3)|
|Power consumption||Overload (max power), per lane|+4.5dBm|
|Operating temperature||Wavelength range|840 – 868nm, 900-918nm|
|Storage temperature||LOS Assert|Min -24.6dBm|
|1)Aggregated line rate 400GbE<br>2)Line baud rate<br>3)Average receive power, (min) is infor<br>indicator of signal strength. A received<br>be compliant; however, a value above<br>compliance.<br>4)Specified at BER 2.4x10-4||LOS De-assert|Max -8.6dBm|
|||LOS Hysteresis|Min 0.5dB|
|||DDM|Yes|
|||MSA compliance|QSFP-DD MSA|
||||CMIS5.1|



4) Specified at BER 2.4x10-4 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.3 

## APPLICATION CODE LIST 

||**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**||
|---|---|---|---|---|---|---|---|
||1|8 x 50GBASE-R|8x 50GAUI-1 (8x 50G)1)|400G|RS-FEC1)|<br>8x 50GBASE-SR||
||2|4 x 100GBASE-R|4x 100GAUI-2 (2x 50G)2)|400G|RS-FEC2)|4x 100G SR1.2||
||3|4x 100GBASE-R|4x 100GAUI-2 (2x 50G)2)|400G|P-FEC2)|4x 100G, with P-FEC||
||4|4x 100GBASE-R|4x 100GAUI-2 (2x 50G)1)|400G|RS-FEC1)|4x 100G SR1.2||
||5|1x 400GBASE-R|1x 400GAUI-8 (8x50G)1)|400G|RS-FEC1)|400G SR4.2||



- 1) Transceiver will not add FEC. Host shall apply FEC 

- 2) On-board FEC, host shall not provide FEC 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQD022-MS2C-SO|QSFP-DD 400G-SR4.2 850/908nm C5.1 MPO|



## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
||Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual opticalpath loss and dispersionproperties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>agiven bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range(I-temp): -40°C to +85°C(-40°F to +185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
||Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured usingan ordinaryopticalpower meter.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any port ion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

