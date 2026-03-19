import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from report_utils import CONTENT_WIDTH_IN_INCHES, init_mpl, save_fig
from scipy.constants import c, e, h
from scipy.stats import linregress

DATA_PATH = "../data/cd.csv"
I_TH = 0.05125  # Threshold current (mA)


def calculate_wavelength(result):
    V_0 = result.intercept
    delta_V0 = result.intercept_stderr

    wavelength_nm = (h * c) / (e * V_0) * 1e9
    delta_wavelength_nm = wavelength_nm * (delta_V0 / V_0)

    print(f"V_0 = {V_0:.3f} ± {delta_V0:.3f} V")
    print(f"lambda = {wavelength_nm:.1f} ± {delta_wavelength_nm:.1f} nm")


def main():
    init_mpl()

    df = pd.read_csv(DATA_PATH)
    df["current_A"] = df["current_monitor"] / 20
    df["laser_voltage"] = df["voltage_monitor"] - df["current_monitor"]
    df["photodiode_output"] = df["photodiode_output"] * 1e-3
    above = df[df["current_A"] > I_TH]

    vi_result = linregress(above["current_A"], above["laser_voltage"])
    vi_fit_x = np.linspace(above["current_A"].min(), above["current_A"].max(), 100)
    vi_fit_y = vi_result.slope * vi_fit_x + vi_result.intercept

    li_result = linregress(above["current_A"], above["photodiode_output"])
    li_fit_x = np.linspace(above["current_A"].min(), above["current_A"].max(), 100)
    li_fit_y = li_result.slope * li_fit_x + li_result.intercept
    fig, (li_ax, vi_ax) = plt.subplots(1, 2, figsize=(CONTENT_WIDTH_IN_INCHES, 4))

    li_ax.plot(
        df["current_A"], df["photodiode_output"], ls="none", marker="x", color="black"
    )
    li_ax.plot(
        li_fit_x,
        li_fit_y,
        label=rf"$L=({li_result.slope:.2g} \pm {li_result.stderr:.1g}) I + ({li_result.intercept:.2g} \pm {li_result.intercept_stderr:.1g})$",
        lw=1,
        color="black",
    )
    li_ax.set_xlabel("current, $I$ (mA)")
    li_ax.set_ylabel("photodiode output, $L$ (V)")
    li_ax.axvline(I_TH, color="black", ls="--", lw=1, label=r"$I_\mathrm{th}$")
    li_ax.legend(fontsize="x-small")
    li_ax.set_xlim(left=0)

    vi_ax.plot(
        df["current_A"], df["laser_voltage"], ls="none", marker="x", color="black"
    )
    vi_ax.plot(
        vi_fit_x,
        vi_fit_y,
        label=rf"$V=({vi_result.slope:.2g} \pm {vi_result.stderr:.1g}) I + ({vi_result.intercept:.2g} \pm {vi_result.intercept_stderr:.1g})$",
        lw=1,
        color="black",
    )
    vi_ax.set_xlabel("current, $I$ (mA)")
    vi_ax.set_ylabel(r"laser voltage, $V$ (V)")
    vi_ax.axvline(I_TH, color="black", ls="--", lw=1, label=r"$I_\mathrm{th}$")
    vi_ax.legend(fontsize="x-small")
    vi_ax.set_xlim(left=0)

    Rs = vi_result.slope
    Rs_err = vi_result.stderr
    print(f"Series resistance: Rs = {Rs:.1f} ± {Rs_err:.1f} Ω")
    calculate_wavelength(vi_result)

    eta_s = li_result.slope
    eta_s_err = li_result.stderr
    print(f"Slope efficiency: eta_s = {eta_s:.4f} ± {eta_s_err:.4f} V/mA")

    save_fig("cd")


if __name__ == "__main__":
    main()
