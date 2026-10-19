DATASHEET 

6.3 

## **OSFP112 800G 2xLR4, CMIS5.0** 

OSFP112, 800G Ethernet, 2x400G-LR4, PAM4 CMIS5.0, 13xxnm 10km 7.1dB Dual-LC 

## TOC004-SC4C-SO 

The TOC004-SC4C-SO is an OSFP112 form-factor transceiver for 800Gbps or 2x400G Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 10km over single-mode fiber. The optical interface consists of two duplex LC connectors, allowing aggregation of two 400G-LR4-10 transceivers. 

The electrical interface consists of eight 106.25G signals (800GAUI-8) that are converted to eight PAM4-modulated channels/lanes to transport the optical signal over CWDM wavelengths. The transceiver can also be set in 2x400GAUI-4 mode to enable 2x 400G break-out configurations. Digital diagnostics functions are available via an I[2] C interface, as specified by the CMIS revision 5.0. 

The optical interface to the transceiver is two duplex LC connectors (UPC). 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . 

## TECHNICAL DATA 

||**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|---|
||Technology|Grey, OSFP112 800G||**Transmitter data:**|||
||Transmission media|SM (2x Duplex LC)||Output power, Average, per lane|Min: -2.7dBm||
||Typical reach|10km|||Max: +5.1dBm||
||Nominal wavelengths|1271nm||Output power, OMA, per lane|Min: +0.3dBm||
|||1291nm|||Max: +4.4dBm||
|||1311nm||Transmit wavelength|1264.5 – 1277.5nm||
|||1331nm|||1284.5 – 1297.5nm||
||Interface standards|2x 400G-LR4-10|||1304.5 – 1317.5nm||
||Electrical interfaces|800GAUI-4 or 2x400GAUI-4|||1324.5 – 1337.5nm||
||Bit rate support|850Gbps1)||**Receiver data:**|||
|||53.125Gbd2)||Minimum input power, Average, per lane|-9.8dBm||
||Protocol support|800GbE||Overload, Average, per lane|+4.1dBm||
||Power budget|0 – 7.1dB||Minimum input power, OMA per lane|-6.8dBm||
||Power consumption|< 14W||Wavelength range|1264.5 – 1277.5nm||
||Operating temperature|0°C to +70°C|||1284.5 – 1297.5nm||
||Storage temperature|-40°C to +85°C|||1304.5 – 1317.5nm||
||1)Aggregated line rate 800GbE||||1324.5 – 1337.5nm||
||2)Line baud rate per lane|||LOS Assert|Min -16dBm||
||**Safety/regulatory compliance:**|||LOS De-assert|Max -10dBm||
||TUV/UL/FDA (contact Smartoptics for latest certification information)|||LOS Hysteresis|Min 0.5dB||
||RoHS compliance|||DDM|Yes||
|||||MSA compliance|OSFP MSA, CMIS5.0||






Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.3 

## APPLICATION CODE LIST 

||**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**Media ID**|**MSA**||
|---|---|---|---|---|---|---|---|---|
||1|2 x 400GBASE-R|2x 400GAUI-4-L C2M|2x 400G|RS-FEC|0xC0|400G-LR4-10 MSA||
||2|2 x 400GBASE-R|2x 400GAUI-4-S C2M|2x 400G|RS-FEC|0xC0|400G-LR4-10 MSA||
||3|800GBASE-R|1x 800GAUI-8 L C2M|800G|RS-FEC|0xC1|800G 2xLR4* (Undefined)||
||4|800GBASE-R|1x 800GAUI-8 S C2M|800G|RS-FEC|0xC1|800G 2xLR4* (Undefined)||
||5|4 x 200GBASE-R|4x 200GAUI-2-L C2M|4x 200G|RS-FEC|0xC2|200G-LR2* (Undefined)||
||6|4 x 200GBASE-R|4x 200GAUI-2-S C2M|4x 200G|RS-FEC|0xC2|200G-LR2* (Undefined)||
||7|8 x100GBASE-R|8 x 100GAUI-1-L C2M|8x 100G|RS-FEC|0xC0|100G-LR1* (Undefined)||
||8|8 x100GBASE-R|8 x 100GAUI-1-S C2M|8x 100G|RS-FEC|0xC0|100G-LR1* (Undefined)||



*) The media ID for the application code is missing in the MSA SFF-8024 and uses a Vendor specific/Custom code. 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TOC004-SC4C-SO|OSFP112 800G-2xLR4 Ethernet, PAM4 CMIS5.0, 1271nm/1291nm/1311nm/1331nm 10km 7.1dB dual-LC|



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

