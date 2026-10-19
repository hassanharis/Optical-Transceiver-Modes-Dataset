DATASHEET 

5.2 

## **SO-CFP-LPC-DWDM** 

CFP-DCO Low Tx Power, 100G Eth, DWDM 6,25/50GHz Coh, 191.25-196.10THz, 2400km, 25dB, LC 

## OVERVIEW 

The SO-CFP-LPC-DWDM is a high performance DWDM transceiver that utilizes DP-QPSK coherent modulation and an advanced dispersion compensation technique that provides equal or better chromatic and polarization mode (CM/PMD) tolerance as a 10Gbps channel. The 100Gbps wavelength can thus be injected into an existing 10Gbps DWDM link without any changes to the optical network. The SO-CFP-LPC-DWDM is used on the line side of the Smartoptics DCP-101 Transponder module. See separate datasheet for further information. 

The module includes a high-performance DSP (Digital Signal Processor) to code and decode the coherent signal and an OTU4 framer/deframer into which the 100G Ethernet signal is mapped to provide the necessary long-haul transmission performance via FEC (Forward Error Correction). 

The optical performance provides a bridgeable distance of up to 2400km (without in-line dispersion compensation) for 100GbE. The unit is tunable and supports 50GHz or 6.25GHz ITU-T grid between 191.25 - 196.10THz and later also in flex-grid channel configurations in the DCP-Series. 

SO-CFP-LPC-DWDM includes mechanical characteristics are compliant with the CFP MSA specifications. 

- Compliant with CAUI-10 100G Ethernet signaling 

- Low latency Soft-Decision Forward Error Correction (SD-FEC) without post-FEC error floor 

- Compliant to CFP MSA Hardware Specification 1.0 with modifications 

- Compliant to CFP MSA Management Interface Specification 2.4 with modifications 

## TECHNICAL DATA 

|TECHNICAL DATA|||
|---|---|---|
|**Parameter**<br>**Value**<br>Technology<br>DWDM 12.5/50GHz CFP<br>Transmission media<br>SM (2x LC)<br>Typical reach<br>2400km<br>Nominal wavelength<br>191.25 - 196.10THz<br>Bit rate support<br>103.125Gbps<br>Protocol support<br>100GbE<br>Power budget<br>0 – 25dB<br>Dispersion tolerance<br>40 000ps/nm4)<br>Power consumption<br>< 20W<br>Operating temperature<br>-5°C to +70°C<br>Storage temperature<br>-40°C to +85°C|**Parameter**|**Value**|
||**Transmitter data:**||
||Output power|Min: -5.0dBm|
|||Max: -1.0dBm|
||Transmit wavelength|191.25 - 196.10THz @ 12.5/50GHz steps|
||OSNR @ Tx|40dB/0.1nm|
||Tuning speed|< 60s from any to any1)|
||**Receiver data:**||
||Minimum input power|0 to -18dBm2)|
|||Min -30dBm3)|
||OSNR sensitivity|14dB/0.1nm|
||Overload (max power)|0dBm|
||Wavelength range|191.25 - 196.10THz|
||DDM|Yes|
||MSA compliance|CFP MSA’s|



- 1) Maximum switching time from one wavelength to any other wavelength, including modulator bias optimization time 

- 2) Optimum Input power range. Signal power of the selected channel. The input power range gets optimum OSNR performance. 

- 3) Minimum input power needed to achieve post FEC BER < 10-15 when OSNR > 35dB and SDFEC is enabled. 

4) CD tolerance with less than 0.3dB OSNR penalty at SD-FEC 

For further technical details, please contact Smartoptics **Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.2 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-CFP-LPC-DWDM|CFP-DCO Low Tx Power, 100G Eth, DWDM 6,25/50GHz Coh, 191.25-196.10THz, 2400km, 25dB, LC|



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

