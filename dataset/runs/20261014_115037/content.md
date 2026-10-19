DATASHEET 

5.0 

## **SO-QSFP-Dxx** 

## QSFP+, 40GBASE, PAM4, DWDM, 100GHz, DDM, D9200-D9590 (40ch) 

## OVERVIEW 

The SO-QSFP-Dxx is a pluggable QSFP+ DWDM transceiver designed for high capacity 40 Gigabit Ethernet (40GbE) Data Center Interconnect (DCI) optical communication applications up to 80km[1)] over a single mode fiber. 

The transceiver utilizes one PAM4-modulated 20Gbd wavelength within a 100GHz channel, enabling up to 40 channels over a 100GHz DWDM grid system as specified in the ITU-T 694.1 standard. Integrated, high-gain FEC (Forward Error Correction) and advanced ADC/DSP technology enable optical reaches up to 80km over an amplified DWDM line system. 

The electrical signals are transmitted and received from the host via a standard 38 pin connector described in the QSFP MSA (SFF-8679). The electrical 40Gbps signal consists of four parallel 10Gbps NRZ streams. 

## TECHNICAL DATA 

|**Parameter**<br>**Value**<br>Technology<br>DWDM QSFP+ 40GHz<br>Transmission media<br>SM (2x LC)<br>Typical reach<br>80km1)<br>Nominal wavelength<br>192.00 - 195.90THz (40ch)<br>Bit rate support<br>41.25Gbps<br>Protocol support<br>40GbE<br>Dispersion tolerance<br>± 100ps/nm2)<br>Power consumption<br>< 5W<br>Operating temperature<br>-20°C to +70°C<br>Storage temperature<br>-40°C to +85°C<br>1)requires a DWDM line system with amplification and dispersion management<br>2)residual dispersion after dispersion compensation (DCM)|**Parameter**|**Value**|
|---|---|---|
||**Transmitter data:**||
||Output power per lane|Min: -11.0dBm3)|
|||Max: -8.0dBm3)|
||Transmit wavelength|192.00 - 195.90THz (G.694.1)4)|
||**Receiver data:**||
||Minimum input power per lane|-2.0dBm3)|
||Overload (max power) per lane|+6.0dBm3)|
||Wavelength range|1529.55 – 1560.61|
||LOS assert|Min -10dBm|
||LOS de-assert|Max -3dBm|
||LOS Hysteresis|Typ 1.0dB|
||DDM|Yes|
||MSA compliance|SFF-8665, -8636, -8661, -8679|



3) average power 

6) Each transceiver uses two wavelengths within the grid, with a 25GHz offset from the ITU-T center channel. 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.0 

## ORDERING INFORMATION 

|**Part number**<br>SO-QSFP-D20|**Center Freq. THz**<br>192.00|**Part number**<br>SO-QSFP-D40|**Center Freq. THz**<br>194.00|
|---|---|---|---|
|SO-QSFP-D21|192.10|SO-QSFP-D41|194.10|
|SO-QSFP-D22|192.20|SO-QSFP-D42|194.20|
|SO-QSFP-D23|192.30|SO-QSFP-D43|194.30|
|SO-QSFP-D24|192.40|SO-QSFP-D44|194.40|
|SO-QSFP-D25|192.50|SO-QSFP-D45|194.50|
|SO-QSFP-D26|192.60|SO-QSFP-D46|194.60|
|SO-QSFP-D27|192.70|SO-QSFP-D47|194.70|
|SO-QSFP-D28|192.80|SO-QSFP-D48|194.80|
|SO-QSFP-D29|192.90|SO-QSFP-D49|194.90|
|SO-QSFP-D30|193.00|SO-QSFP-D50|195.00|
|SO-QSFP-D31|193.10|SO-QSFP-D51|195.10|
|SO-QSFP-D32|193.20|SO-QSFP-D52|195.20|
|SO-QSFP-D33|193.30|SO-QSFP-D53|195.30|
|SO-QSFP-D34|193.40|SO-QSFP-D54|195.40|
|SO-QSFP-D35|193.50|SO-QSFP-D55|195.50|
|SO-QSFP-D36|193.60|SO-QSFP-D56|195.60|
|SO-QSFP-D37|193.70|SO-QSFP-D57|195.70|
|SO-QSFP-D38|193.80|SO-QSFP-D58|195.80|
|SO-QSFP-D39|193.90|SO-QSFP-D59|195.90|



Note: The above represents the center channels of the ITU-T G.694.1 grid. Each transceiver uses two wavelengths within the grid, with a 25GHz offset from the center channel. 

## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
|Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
||AOC: Active Optical Cable. Optical cable with attached connectors.||
|Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
|Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
|Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
|Protocols|Protocols within supported bit rate range.||
|Nominal wavelength|Typical wavelength(s) from transmitter.||
|Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
|Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
|Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
||Max operating case temperature range.||
|Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.0 

## APPLICATION: EMBEDDED 0-80KM 100G DWDM DCI: PAM4 AND OPEN LINE SYSTEM 

The QSFP28 PAM4 transceiver utilizes advanced PAM4 signaling and delivers up to 4Tb/s of bandwidth over a single fiber, allowing multiple data centers located up to 80km of each other to be connected and act like a single data center. The transceiver can be used in data switches with QSFP28 transceiver interfaces. The result is 100G networking with the smallest footprint, lowest power consumption and lowest capex/opex. Perfect for web scale data centers and Internet Exchanges looking to keep costs, inventory and rack space down. The transceiver requires a line system with amplification and dispersion compensation and Smartoptics DCP-M is the perfect accompaniment, enabling true open-line embedded 100G networking. 

## DCP-M40, 1U TRUE OPEN LINE SYSTEM 

Form factor and appearance 



Generic DCP-M40-xxxx schematic diagram 

## DCP-M AND PAM4 ADVANTAGES: 

- The only 1U true plug and play PAM4 connectivity solutions on the market 

- No transponders required; fewer transceivers and electrical points of failure. Reduced cost, complexity and time to service • New 100G interconnects added in the same way as a DWDM transceiver is added to an embedded DWDM network 

- Simple provisioning and management 

- New high capacity DCs and services brought on line as integrated elements of a larger infrastructure 

- Flexible expansion to new lower cost locations with no change in architecture 

- Standardization for geographically distributed topologies 

- Lower opex. No incremental software or support services needed 

- No transport platform training or services are needed beyond basic CLI skills 

- Removes the transport issue from all metro builds. Only access to fiber is needed 

   - 0-80km ptp connectivity with different power budget performance. - DCP-M40-PAM4-ER 0-14dB - DCP-M40-PAM4-ER+ 0-14dB - DCP-M40-PAM4-ZR 0-18dB - DCP-M8-PAM4 0-20d 

DCP-M – True Open Line System 

- 40 channel DWDM Mux/Demux 

PAM4 QSFP28 DWDM transceiver embedded in a 100G router/switch or in a Smartoptics DCP-108 Transponder 

- Integrated amplification, Dispersion management, Optical Monitoring & Control • Any DWDM modulation format: PAM4, NRZ (16/10/8G), Coherent (QPSK/8QSM/16QAM) 


Subject to change without notice. For more information visit smartoptics.com. 

