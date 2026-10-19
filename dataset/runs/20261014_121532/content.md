DATASHEET 

5.3 

## **SO-QSFP28-Dxx** 

## QSFP28, 100GBASE, PAM4, DWDM, 100GHz, DDM, D9200-D9590 (40ch) 

## OVERVIEW 

The SO-QSFP28-Dxx is a pluggable QSFP28 DWDM transceiver designed for high capacity 100 Gigabit Ethernet (100GbE) Data Center Interconnect (DCI) optical communication applications up to 80km[1)] over a singlemode fiber. 

The transceiver utilizes two PAM4-modulated 56 Gbps wavelengths that are grouped within a 100GHz channel, enabling up to 40 channels over a 100GHz DWDM grid system as specified in the ITU-T 694.1 standard. Integrated, high-gain FEC (Forward Error Correction) and advanced ADC/DSP technology enable optical reaches up to 80km over an amplified DWDM line system. 

The electrical signals are transmitted and received from the host via a standard 38 pin connector described in the QSFP28 MSA (SFF-8679). The electrical interface is compliant to CAUI-4 (IEEE P802.3bm Annex 83E), splitting the 100Gbps signal in to four parallel 25 Gbps NRZ streams. 

## TECHNICAL DATA 

|**Parameter**|**Value**||
|---|---|---|
|Technology|DWDM QSFP28 100GHz||
|Transmission media|SM (2x LC)||
|Typical reach|80km1)||
|Nominal wavelength|192.00 - 195.90THz (40ch)||
|Bit rate support|103.12Gbps||
|Protocol support|100GbE2)||
|Dispersion tolerance|± 100ps/nm3)||
|Power consumption|< 5W||
|Operating temperature|-20°C to +70°C||
|Storage temperature|-40°C to +85°C||



- 1) requires a DWDM line system with amplification and dispersion management 

- 2) aggregated line rate 100GbE 

|**Parameter**|**Value**|
|---|---|
|**Transmitter data:**||
|Output power per lane|Min: -11.0dBm5)|
||Max: -8.0dBm5)|
|Transmit wavelength|192.00 - 195.90THz (G.694.1)6)|
|**Receiver data:**||
|Minimum input power per lane|-2.0dBm5)|
|Overload (max power) per lane|+6.0dBm5)|
|Wavelength range|1529.55 – 1560.61|
|LOS assert|Min -10dBm|
|LOS de-assert|Max -3dBm|
|LOS Hysteresis|Typ 1.0dB|
|DDM|Yes|
|MSA compliance|SFF-8665, -8636, -8661, -8679|



- 3) residual dispersion after dispersion compensation (DCM) 

- 4) per 56.25 Gbps lane 

- 5) average power 

- 6) Each transceiver uses two wavelengths within the grid, located +25GHz and -25GHz from the ITU-T center channel. 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.3 

## ORDERING INFORMATION 

|**Part number**<br>SO-QSFP28-D20|**Center Freq. THz**<br>192.00|**Part number**<br>SO-QSFP28-D40|**Center Freq. THz**<br>194.00|
|---|---|---|---|
|SO-QSFP28-D21|192.10|SO-QSFP28-D41|194.10|
|SO-QSFP28-D22|192.20|SO-QSFP28-D42|194.20|
|SO-QSFP28-D23|192.30|SO-QSFP28-D43|194.30|
|SO-QSFP28-D24|192.40|SO-QSFP28-D44|194.40|
|SO-QSFP28-D25|192.50|SO-QSFP28-D45|194.50|
|SO-QSFP28-D26|192.60|SO-QSFP28-D46|194.60|
|SO-QSFP28-D27|192.70|SO-QSFP28-D47|194.70|
|SO-QSFP28-D28|192.80|SO-QSFP28-D48|194.80|
|SO-QSFP28-D29|192.90|SO-QSFP28-D49|194.90|
|SO-QSFP28-D30|193.00|SO-QSFP28-D50|195.00|
|SO-QSFP28-D31|193.10|SO-QSFP28-D51|195.10|
|SO-QSFP28-D32|193.20|SO-QSFP28-D52|195.20|
|SO-QSFP28-D33|193.30|SO-QSFP28-D53|195.30|
|SO-QSFP28-D34|193.40|SO-QSFP28-D54|195.40|
|SO-QSFP28-D35|193.50|SO-QSFP28-D55|195.50|
|SO-QSFP28-D36|193.60|SO-QSFP28-D56|195.60|
|SO-QSFP28-D37|193.70|SO-QSFP28-D57|195.70|
|SO-QSFP28-D38|193.80|SO-QSFP28-D58|195.80|
|SO-QSFP28-D39|193.90|SO-QSFP28-D59|195.90|



Note: The above represents the center channels of the ITU-T G.694.1 grid. Each transceiver uses two wavelengths within the grid, located +25GHz and -25GHz from the center channel. 

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

5.3 

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

