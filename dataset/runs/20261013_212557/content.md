DATASHEET 

6.2 

## **QSFP-DD800 800G 2xPLR4, CMIS5.0** 

QSFP-DD800, 800G Ethernet, 2xPLR4, PAM4 CMIS5.0, 8x1311nm 10km 6.3dB 2xMPO 

## TD8007-S31C-SO 

The TD8007-S31C-SO is an QSFP-DD800 form-factor transceiver for 8x 100G Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 10km over single-mode fiber. The optical interface consists of two MPO-12 connectors, allowing aggregation of eight 100G-LR or transceivers. 

The electrical interface consists of eight 106.25G signals (800GAUI-8) that are converted to eight PAM4-modulated channels/lanes to transport the optical signal over 1311 wavelengths. The transceiver can also be set in 2x400GAUI-4 and 8x100GAUI-1 mode to enable 2x 400G or 8x 100G break-out configurations. Digital diagnostics functions are available via an I[2] C interface, as specified by the CMIS revision 5.0. 

The optical interface to the transceiver is two MPO-12 connectors (APC). 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . 

## TECHNICAL DATA 

||**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|---|
||Technology|Grey, QSFP-DD800||**Transmitter data:**|||
||Transmission media|SM (2x MPO-12, APC)||Output power, Average, per lane|Min: -1.9dBm||
||Typical reach|10km|||Max: +4.8dBm||
||Nominal wavelengths|8x1311nm||Output power, OMA, per lane|Min: +1.1dBm||
||Interface standards|8x 100GBASE-LR|||Max: +5.0dBm||
||Electrical interfaces|800GAUI-8||Transmit wavelength|1304.5 – 1317.5nm||
|||2x 400GAUI-4||**Receiver data:**|||
|||8x 100GAUI-1||Minimum input power, Average, per lane|-9.1dBm||
||Bit rate support|850Gbps1)||Overload, Average, per lane|+4.8dBm||
|||53.125Gbd2)||Minimum input power, OMA per lane|-6.1dBm||
||Protocol support|800GbE, 2x400GbE, 8x100GbE||Wavelength range|1304.5 – 1317.5nm||
||Power budget|0 – 6.3dB||LOS Assert|Min -18dBm||
||Power consumption|< 14W||LOS De-assert|Max -10dBm||
||Operating temperature|0°C to +70°C||LOS Hysteresis|Min 0.5dB||
||Storage temperature|-40°C to +85°C||DDM|Yes||
||1)Aggregated line rate 800GbE|||MSA compliance|QSFP-DD MSA, CMIS5.0||
||2)Line baud rate per lane||||||
||**Safety/regulatory compliance:**||||||
||TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
||RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.2 

## APPLICATION CODE LIST 

||**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**Media ID**|<br>**MSA**||
|---|---|---|---|---|---|---|---|---|
||1|2 x 400GBASE-R|2x 400GAUI-4-L C2M|2x 400G|RS-FEC|0x1C|400GBASE-PLR4* (Undefined)||
||2|2 x 400GBASE-R|2x 400GAUI-4-S C2M|2x 400G|RS-FEC|0x1C|400GBASE-PLR4* (Undefined)||
||3|800GBASE-R|1x 800GAUI-8 L C2M|800G|RS-FEC|0x56|800GBASE-PLR8* (Undefined)||
||4|800GBASE-R|1x 800GAUI-8 S C2M|800G|RS-FEC|0x56|800GBASE-PLR8* (Undefined)||
||5|4 x 200GBASE-R|4x 200GAUI-2-L C2M|4x 200G|RS-FEC|0xC0|200G-PLR2* (Undefined)||
||6|4 x 200GBASE-R|4x 200GAUI-2-S C2M|4x 200G|RS-FEC|0xC0|200G-PLR2* (Undefined)||
||7|8 x100GBASE-R|8 x 100GAUI-1-L C2M|8x 100G|RS-FEC|0x14|100G-LR/100GBASE-LR1 (Clause 140)||
||8|8 x100GBASE-R|8 x 100GAUI-1-S C2M|8x 100G|RS-FEC|0x14|100G-LR/100GBASE-LR1 (Clause 140)||



*) The media ID for the application code is missing in the MSA SFF-8024 and uses a Vendor specific/Custom code. 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TD8007-S31C-SO|QSFP-DD 800G-2xPLR4 Ethernet, PAM4, CMIS5.0, 8x 1311nm 10km 6.3dB 2xMPO12|



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
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any port ion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof.  The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

