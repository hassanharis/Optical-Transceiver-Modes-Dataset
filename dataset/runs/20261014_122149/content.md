DATASHEET 

5.5 

## **SO-QSFP28-LR4-20L** 

## QSFP28, 100G Ethernet eLR4, SM, 1296/1300/1305/1309nm, 20km, 11.2dB, LC 

## OVERVIEW 

The SO-QSFP28-LR4-20L is a QSFP28 form-factor transceiver for 100G Ethernet applications. It is intended for use in inter- and intra-connect applications within and between data centers between switches, routers, storage equipment etc. The optical performance supports optical distances up to 20km over a SingleMode (SM) fiber. 

Forward Error Correction (FEC) is required in the host equipment in order to ensure reliable system operation at the specified distance. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The below optical parameters will provide a bit error ratio (BER) of 5 x 10[-5] . FEC will render in the required BER of better than 1 x 10[-12] . 

SO-QSFP28-LR4-20L uses four optical channels/lanes @ 25.78Gbps to transport the Ethernet signal. Digital diagnostics functions are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

||**Parameter**|**Value**|
|---|---|---|
||**Transmitter data:**||
||Output power, total|Max +8.3dBm3)|
||Output power, per lane|Min: -4.3dBm3)|
|||Max: +4.5dBm3)|
||Output power, per lane, OMA|Min: -1.3dBm3)|
|||Max: +4.5dBm3)|
||Transmit wavelength|1294.53 – 1296.59nm|
|||1299.02 – 1301.09nm|
|||1303.54 – 1305.63nm|
|||1308.09 – 1310.19nm|
||**Receiver data:**||
||Receiver sensitivity, per lane, OMA|-12.5dBm4)|
||Minimum input power, per lane|-14.5dBm3)|
||Overload (max power), per lane|+4.5dBm3) 4)|
||Wavelength range|1294.53 – 1296.59nm|
|||1299.02 – 1301.09nm|
|||1303.54 – 1305.63nm|
|||1308.09 – 1310.19nm|
||LOS Assert|Min -24dBm|
||LOS De-assert|Max -15dBm|
||LOS Hysteresis|Min 0.5dB|
||DDM|Yes|
||MSA compliance|QSFP28 MSA, SFF-8636|
||||
||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.5 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-LR4-20L|QSFP28, 100G Ethernet eLR4, SM, 1296/1300/1305/1309nm, 20km, 11.2dB, LC|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and as receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

