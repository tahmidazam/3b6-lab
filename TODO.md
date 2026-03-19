# 3B6 Semiconductor lasers — Lab report todo list

## Part I: CD laser characterisation

### Data and plots

- [ ] Include raw data table: voltage monitor reading, current monitor voltage (across 20 Ω resistor), and photodiode output for each measurement point (0 to $I_{\max}$)
- [ ] Correct each laser voltage reading by subtracting the voltage drop across the 20 Ω current-sense resistor ($V_{\text{laser}} = V_{\text{monitor}} - I \times 20\;\Omega$)
- [ ] Plot L–I curve (photodiode signal vs. laser current) with error bars
- [ ] Plot V–I curve (corrected laser voltage vs. laser current) with error bars
- [ ] Identify and label the threshold current $I_{\text{th}}$ on the L–I curve (point where optical output rises sharply, typically 40–55 mA)

### Analysis of operating regimes

- [ ] Explain the sub-threshold regime: spontaneous emission dominates, light output increases slowly with current
- [ ] Explain the above-threshold regime: stimulated emission dominates, light output increases linearly and steeply with current
- [ ] Relate both regimes to the underlying radiative recombination processes (spontaneous vs. stimulated emission)

### Series resistance and diode voltage

- [ ] Extract the stray series resistance $R_s$ from the slope of the V–I curve above threshold ($\Delta V / \Delta I$ in the linear region)
- [ ] Estimate the error on $R_s$ (note: expect poor accuracy due to small voltage range and measurement uncertainty)
- [ ] Calculate the voltage across the ideal diode at threshold: $V_{\text{diode}} = V_{\text{measured}}(I_{\text{th}}) - I_{\text{th}} \cdot R_s$
- [ ] Discuss whether $V_{\text{diode}}$ should change above threshold (it should remain approximately clamped)

### Wavelength calculation

- [ ] Calculate wavelength from the photon energy relation: $\lambda = hc \,/\, eV_{\text{diode}}$
- [ ] Propagate errors using $\delta\lambda / \lambda = \delta V_{\text{diode}} / V_{\text{diode}}$
- [ ] Include systematic error sources: $R_s$ uncertainty, resistor tolerance (20 Ω and 26 Ω), oscilloscope reading precision
- [ ] Compare calculated $\lambda$ with the expected ~780 nm for a CD laser and comment on agreement

### Temperature effects

- [ ] Record the lab temperature and any significant fluctuations during the experiment
- [ ] Comment on how temperature variations affect threshold current and emission wavelength

## Part II: Telecom laser spectrum analysis

### Spectral sketches

- [ ] Sketch the broad-span (~100 nm) spectrum below threshold (14 mA) — broad spontaneous emission envelope
- [ ] Sketch the broad-span spectrum above threshold (17 mA) — narrowed spectrum with dominant mode(s)
- [ ] Sketch the narrow-span (~5–10 nm) spectrum below threshold — showing Fabry–Pérot cavity mode ripples on a broad envelope
- [ ] Sketch the narrow-span spectrum above threshold — showing sharp longitudinal modes with one or few dominant peaks

### Measured parameters

- [ ] Record centre wavelength $\lambda_0$ for both operating conditions
- [ ] Record peak output power $P_0$ for both conditions
- [ ] Record 3 dB spectral width for both conditions
- [ ] Note OSA settings used: resolution bandwidth, sensitivity, span

### Spectral interpretation

- [ ] Explain why below-threshold spectrum is broad (spontaneous emission with weak mode selectivity)
- [ ] Explain why above-threshold spectrum narrows (gain clamping, mode competition, stimulated emission into cavity modes)
- [ ] Relate spectral differences to the transition from spontaneous to stimulated emission dominance

### Mode spacing and refractive index

- [ ] Measure the longitudinal mode spacing $\Delta\lambda$ — average over as many mode pairs as possible to reduce random error
- [ ] Record the cavity length $L$ from the laser box label
- [ ] Calculate the effective refractive index: $n = \lambda_0^2 \,/\, (2L \cdot \Delta\lambda)$
- [ ] Propagate errors: $\delta n / n = \sqrt{(2\,\delta\lambda_0 / \lambda_0)^2 + (\delta L / L)^2 + (\delta\Delta\lambda / \Delta\lambda)^2}$
- [ ] Compare $n$ with expected values for InGaAsP (~3.2–3.6) and comment
- [ ] Verify that mode spacing is consistent above and below threshold (it should be, since $n$ and $L$ are approximately constant)

## General write-up

- [ ] Ensure all error bars and uncertainties are quoted to 1–2 significant figures with results rounded accordingly
- [ ] Distinguish between random errors (oscilloscope jitter, detector noise) and systematic errors (resistor tolerance, OSA calibration)
- [ ] Add random errors in quadrature; add systematic errors linearly
