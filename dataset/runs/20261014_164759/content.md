DATASHEET 

6.6 

## **QSFP28 100GE SR1.2** 

## QSFP28, 100G Eth, 100GBASE-SR1.2, MM, 850nm / 908nm, 100m, 2.4dB, LC 

## TQ2016-MS2C-SO 

The TQ2016-MS2C-SO is a pluggable QSFP28 transceiver designed for high capacity 100 Gigabit Ethernet (100GbE) Data Center Interconnect (DCI) applications up to 100m over a multimode fiber. The transceiver can also be used for 4x100G aggregation together with the QSFP-DD 400GBASE-SR4.2 transceiver (p/n: TQD022-MS2C-SO). 

TQ2016-MS2C-SO has an optical performance enabling distances of up to 100m over a Multi-Mode (MM) OM4 fiber-pair cable. The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10-4. FEC will render in the required BER of better than 1 x 10-12. 

The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8636 specification. 

## TECHNICAL DATA 

||**Parameter**|**Value**||**Parameter**||||**Value**||
|---|---|---|---|---|---|---|---|---|---|
||Technology|BiDi QSFP28||**Transmitter data:**||||||
||Transmission media|MM (2x LC)||Output power, per lane||||Max: +4.0dBm3)||
||Typical reach|70m @ OM3, 100m @ OM4, 150m @ OM5||||||Min: -6.2dBm3)||
||Nominal wavelengths|λ1: 850nm||Output power, per lane, OMA||||Max: +3.0dBm||
|||λ2: 908nm||||||Min: -4.2dBm||
||Interface standards|100GBASE||Transmit wavelengths||||844 – 863nm||
||Bit rate support|106.25Gbps1)||||||900 – 918nm||
|||26.5625Gbd2)||**Receiver data:**||||||
||Protocol support|100GbE||Receiver sensitivity, OMA||||-6.6dBm5)||
||Power budget|0 – 2.4dB||Minimum input power||||-8.2dBm3) 4)||
||Power consumption|< 4.0W||Overload (max power)||||+4.0dBm3) 5)||
||Operating temperature|0°C to +70°C||Wavelength range||||844 – 863nm||
||Storage temperature|-40°C to +85°C||||||900 – 918nm||
|||||LOS Assert||||-30.0dBm3)||
||1)Aggregated line rate 100GbE with FEC|||LOS De-assert||||-5.9dBm3)||
||2)Line baud rate|||DDM||||Yes||
||3)Average power, per lane.|||MSA compliance||||QSFP28 MSA||
||4)A received power below this value cannot be compliant; however, a value<br>above this does not ensure compliance.|||||||SFF-8636||
||5)Specified at BER 2.4x10^-4|||||||||
||**Safety/regulatory compliance:**|||||||||
||TUV/UL/FDA (contact Smartoptics for latest certification information)|||||||||
||RoHS compliance|||λ1|850nm||T1, R1|||
|||||λ2|908nm||T2, R2|||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.6 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2016-MS2C-SO|QSFP28 100GE-SR1.2 Duplex MM 100m|



## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
||Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally1x 10-12. Some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally1x10-12.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

