DATASHEET 

5.0 

## **SO-SFP28-SR3** 

## SFP28, 25G Ethernet, 850nm, MM, DDM, 1.9dB, 200m@OM3, 300m@OM4 

## OVERVIEW 

The SO-SFP28-SR3 is an SFP+ form-factor transceiver for 25 Gbps Ethernet applications. Since the transmission rate can reach up to 28Gbps, the engineering and industry name is SFP28. It is intended for use in inter- and intra-connect applications within data centers between switches, routers, storage equipment etc. The optical performance is in accordance with the IEEE -SR standard, i.e. for optical distances up to 300m over a MultiMode (MM) OM4-grade fiber. 

SO-SFP28-SR3 uses a single 850nm channel @ 25.78 Gbps to transport a 25G Ethernet signal. Digital diagnostics functions are available via an I2C interface, as specified by the MSA. 

As stipulated by the 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The optical parameters below will provide a bit error ratio (BER) of 5 x 10[-5 ] for 25G Ethernet. FEC will provide the required quality for secure service. 

## TECHNICAL DATA 

|**Parameter**<br>**Value**<br>Technology<br>Grey SFP28<br>Transmission media<br>MM (2x LC)<br>Typical reach<br>300m (OM4), 200m (OM3)<br>Nominal wavelength<br>850nm<br>Interface standards<br>25GBASE-SR<br>Bit rate support<br>25.78Gbps<br>Protocol support<br>25GbE<br>Power budget<br>0 – 1.9dB<br>Power consumption<br>< 1.0W<br>Operating temperature<br>0°C to +70°C<br>Storage temperature<br>-40°C to +85°C|**Parameter**|**Value**|
|---|---|---|
||**Transmitter data:**||
||Output power, per lane|Min: -8.4dBm1)|
|||Max: +2.4dBm1)|
||Transmit wavelength|840 – 860nm|
||**Receiver data:**||
||Minimum input power|-10.3dBm1) 2)|
||Overload (max power)|+3.0dBm1) 2)|
||Wavelength range|840 – 860nm|
||LOS Assert|Min -30dBm|
||LOS De-Assert|Max -13dBm|
||LOS Hysteresis|Min 0.5dB|
||DDM|Yes|
||MSA compliance|SFP28 SFF-8402|



1) Average power 

- 2) At BER less than 5x10-5 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 

Note: The 25GbE specification states that a 25GbE interface can operate with or without FEC. The optical data above is defined at a BER of 5x10[-5] , implying that FEC shall be enabled on the host equipment to provide required quality at specified distance. 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.0 

ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-SFP28-SR3|SFP28, 25G Ethernet, 850nm, MM, DDM, 1.9dB, 200m@OM3, 300m@OM4, LC|



The SO-SFP28-SR3 supports high data rates 24.33/25.78G (CPRI options 10 /25GbE) and Low data rates 9.95/10.31G (10GbE-LW/LR). 

|Logic OR of<br>RS0 Pin and<br>Bit110.3 of A2H|Logic OR of<br>RS1 Pin and<br>Bit118.3 of A2H|RX<br>Data Rate|TX<br>Data Rate|Status of<br>RX CDR|Status of<br>TX CDR|
|---|---|---|---|---|---|
|High/1|High/1|24.33/25.78 Gbps|24.33/25.78 Gbps|CDR Engaged|CDR Engaged|
|Low/0|Low/0|9.95/10.31 Gbps|9.95/10.31 Gbps|CDR Bypassed|CDR Bypassed|
|GENERAL DEFINITIONS<br>Technology:<br>Grey; Transceiver type for non-WDM applications. Electrical or optical.<br>CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.<br>DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.<br>DAC: Direct Attach Cable (DAC). Electrical or optical cable with attached connectors.<br>Transmission Media:<br>Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within<br>brackets (e.g. 2x LC, 1x MPO).<br>Typical reach:<br>Nominal distance performance based on dispersion and power budget properties, i.e. w/o<br>dispersion compensation and optical amplification.<br>Bit rate range:<br>Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).<br>Protocols:<br>Protocols within supported bit rate range.<br>Nominal wavelength:<br>Typical wavelength from transmitter.<br>Interface standards:<br>Referenced interface standards e.g. IEEE 802.3 standard for 10GbE services.<br>Power budget:<br>Min and max power budget between Transmitter and Receiver.<br>Dispersion tolerance/penalty:<br>Maximum amount of tolerated dispersion and required reduction of power budget to maintain<br>stipulated Bit Error Rate (BER) and at a given bit rate.<br>Temperature range:<br>Max operating case temperature range.<br>Commercial temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp):  typically -20°C to +75°C (-4°F to +167°F)<br>Industrial temperature range (I-temp): -40°C to +85°C (-40°F to +185°F)<br>Power consumption:<br>Worst case power consumption. Will vary over temperature.<br>Transmitter Output power:<br>Average output power. Provided in min and max values.<br>Receiver minimum input power: Minimum average input power at specified BER, normally 1E-12.<br>Receiver max input power:<br>Maximum average input power giving a BER, normally 1E-12.<br>DDM:<br>Digital Diagnostic Monitoring functionality as defined in SFF-8472 MSA.||||||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

