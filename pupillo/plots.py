
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.patches import Patch

def ygb_colormap():
    return LinearSegmentedColormap.from_list("yellow_green_blue",
        ["#ffff66", "#33cc33", "#0066cc"], N=256)

def heatmap_with_isobars(OCC, USE, Z, title, xlabel, ylabel, outfile,
                         vmin=0.0, vmax=None, levels=None, hlines=None):
    plt.figure(figsize=(6,6))
    im = plt.imshow(Z, origin="lower", cmap=ygb_colormap(),
                    extent=[OCC.min(), OCC.max(), USE.min(), USE.max()],
                    vmin=vmin, vmax=vmax,
                    aspect=(OCC.max()-OCC.min())/(USE.max()-USE.min()))
    if levels is None:
        max_val = Z.max() if vmax is None else vmax
        levels = np.arange(2, max(4, int(max_val)+2), 2)
    cs = plt.contour(OCC, USE, Z, colors='white', linewidths=1, levels=levels)
    plt.clabel(cs, inline=True, fontsize=8, fmt="%.0f")
    if hlines:
        for y, style in hlines:
            plt.axhline(y, color='black', linestyle=style, linewidth=1.4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, pad=25, fontsize=11)
    cbar = plt.colorbar(im, orientation="horizontal", pad=0.15)
    cbar.set_label("CO₂e savings per bed-year (kg)")
    plt.tight_layout()
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close()

def comparison_barchart(names, mids, lows, highs, outfile, proposed_labels=None):
    idx = np.argsort(mids)[::-1]
    names = [names[i] for i in idx]
    mids  = np.array(mids)[idx]
    lows  = np.array(lows)[idx]
    highs = np.array(highs)[idx]
    err_lower = mids - lows
    err_upper = highs - mids

    colors = []
    edges = []
    for n in names:
        if proposed_labels and n in proposed_labels:
            colors.append("#444444")
        else:
            colors.append("white")
        edges.append("black")

    fig, ax = plt.subplots(figsize=(7,4.5))
    y = np.arange(len(names))
    ax.barh(y, mids, xerr=[err_lower, err_upper], color=colors, edgecolor=edges,
            linewidth=1.5, alpha=0.9, capsize=4)
    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.invert_yaxis()
    ax.set_xlabel("Estimated CO₂e savings per ICU bed-year (kg)")
    ax.set_title("Comparison of ICU Sustainability Interventions", pad=20)
    legend_elements = [
        Patch(facecolor="#444444", edgecolor="black", label="Proposed interventions (this study)"),
        Patch(facecolor="white", edgecolor="black", label="Other published LCAs"),
    ]
    ax.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, -0.3), ncol=2, frameon=False)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close()
