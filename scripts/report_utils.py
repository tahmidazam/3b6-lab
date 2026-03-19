from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt


def init_mpl():
    matplotlib.use("pgf")
    matplotlib.rcParams.update(
        {
            "pgf.preamble": r"\usepackage{siunitx}\usepackage{amsmath}\usepackage[OT1]{fontenc}\renewcommand*\familydefault{\sfdefault}\usepackage{sansmathfonts}\usepackage{gensymb}\usepackage{mhchem}",
            "pgf.texsystem": "pdflatex",
            "text.usetex": True,
            "pgf.rcfonts": False,
        }
    )


def save_fig(id: str):
    directory = Path("../report/figures")
    directory.mkdir(parents=True, exist_ok=True)
    filepath = directory / f"{id}.pgf"
    fig = plt.gcf()
    axes = fig.get_axes()
    for ax in axes:
        ax.minorticks_on()
        ax.grid(which="minor", alpha=0.2)
        ax.grid(which="major", alpha=0.5)
        ax.tick_params(axis="both", which="major", labelsize="small")

        title = ax.get_title()
        ax.set_title("")
        ax.set_title(title, loc="left", fontweight="bold", fontsize="small")

        ax.tick_params(axis="both", which="major", labelsize="small")
        ax.tick_params(axis="both", which="minor", labelsize="small")

        xlabel = ax.get_xlabel()
        ylabel = ax.get_ylabel()
        ax.set_xlabel(xlabel, fontsize="small")
        ax.set_ylabel(ylabel, fontsize="small")
    plt.tight_layout()
    plt.savefig(filepath)


MARGIN_IN_INCHES = 1
A4_PAGE_WIDTH_IN_INCHES = 8.2677165354
CONTENT_WIDTH_IN_INCHES = A4_PAGE_WIDTH_IN_INCHES - 2 * MARGIN_IN_INCHES
