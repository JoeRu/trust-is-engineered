#!/usr/bin/env python3
"""Generate the English figures of "Trust is Engineered".

Usage:
    python3 make_figures.py [OUTPUT_DIR]

OUTPUT_DIR defaults to $FIGURES_OUT, else docs/figures/ (the parent of this
script's folder), so a plain run regenerates the figures in place.

Requires matplotlib only. All curves and values are computed from the
formulas in the paper (Sections 2.2, 4.3, 4.7, 7.9, 10.4, 12.4); all parameter
values are the illustrative values stated there.

Layout is done on a fixed pixel canvas: every figure is 1344 px wide
(672 px at 2x scale), coordinates below are output pixels with y downward.
"""

import math
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Polygon, FancyArrowPatch, Rectangle  # noqa: E402
from matplotlib import font_manager  # noqa: E402

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------

WIDTH = 1344
DPI = 200
PT = 72.0 / DPI  # points per output pixel

_installed = {f.name for f in font_manager.fontManager.ttflist}
FONTS = [f for f in ("Inter", "DejaVu Sans") if f in _installed] or ["sans-serif"]
plt.rcParams["font.family"] = FONTS
plt.rcParams["svg.fonttype"] = "none"

INK = "#111111"
MUTED = "#555555"
GRID = "#E6E6E3"
BOX_EDGE = "#C9C8BE"
LINE = "#C2C1B5"
BLUE = "#2B78D8"
BLUE_FILL = "#E5EEF9"
BAR_BLUE = "#A0C2EC"
BAR_RED = "#EAB1B0"
BAR_GREY = "#E9E9E5"
BAR_NEUTRAL = "#D6D5CE"
DARK_LINE = "#6E6D66"

F_TITLE = 23
F_SUB = 17.5
F_BOX_TITLE = 20
F_TEXT = 18
F_SMALL = 16


def num(x, digits=2):
    """Format a number with a decimal point and a typographic minus."""
    s = f"{x:.{digits}f}"
    return s.replace("-", "−")


def canvas(height):
    fig = plt.figure(figsize=(WIDTH / DPI, height / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(height, 0)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    return fig, ax


def text(ax, x, y, s, size=F_TEXT, color=INK, weight="normal", ha="left", va="center", **kw):
    return ax.text(x, y, s, fontsize=size * PT, color=color, fontweight=weight,
                   ha=ha, va=va, **kw)


def title(ax, s, subtitle=None, y=48):
    text(ax, 43, y, s, size=F_TITLE, weight="bold")
    if subtitle:
        text(ax, 43, y + 30, subtitle, size=F_SUB, color=MUTED)


def box(ax, x0, y0, x1, y1, head, sub=None, highlight=False, head_size=F_BOX_TITLE,
        sub_size=F_SMALL + 1):
    edge = BLUE if highlight else BOX_EDGE
    face = BLUE_FILL if highlight else "white"
    lw = 3.0 if highlight else 2.0
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0,rounding_size=12",
                                linewidth=lw * PT, edgecolor=edge, facecolor=face,
                                zorder=2))
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    if sub is None:
        text(ax, cx, cy, head, size=head_size, weight="bold", ha="center", zorder=3)
        return
    n_sub = sub.count("\n") + 1
    line_h = 29
    total = 34 + n_sub * line_h
    top = cy - total / 2
    text(ax, cx, top + 15, head, size=head_size, weight="bold", ha="center", zorder=3)
    text(ax, cx, top + 34 + (n_sub * line_h) / 2 + 2, sub, size=sub_size, color=MUTED,
         ha="center", linespacing=1.45, zorder=3)


def polyline(ax, pts, color=LINE, lw=2.2, arrow=True, dashed=False, z=1):
    """Draw a polyline; the last segment ends in a filled arrow head."""
    ls = (0, (4, 4)) if dashed else "-"
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw * PT, ls=ls,
                solid_capstyle="butt", zorder=z)
    hl, hw = (4.5 * lw + 4) * PT, (2.2 * lw + 2) * PT
    style = f"-|>,head_length={hl:.3f},head_width={hw:.3f}" if arrow else "-"
    ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle=style,
                                 mutation_scale=1,
                                 color=color, lw=lw * PT, linestyle=ls,
                                 shrinkA=0, shrinkB=0, zorder=z))


class Chart:
    """Map data coordinates onto a pixel rectangle of the canvas."""

    def __init__(self, ax, x0, x1, y0, y1, xmin, xmax, ymin, ymax):
        self.ax = ax
        self.px = (x0, x1)
        self.py = (y0, y1)  # y0 = pixel of ymin (bottom), y1 = pixel of ymax (top)
        self.xr = (xmin, xmax)
        self.yr = (ymin, ymax)

    def X(self, v):
        (a, b), (lo, hi) = self.px, self.xr
        return a + (v - lo) / (hi - lo) * (b - a)

    def Y(self, v):
        (a, b), (lo, hi) = self.py, self.yr
        return a + (v - lo) / (hi - lo) * (b - a)

    def grid(self, yticks, ylabels, xticks, xlabels, xlabel):
        ax = self.ax
        for v, lab in zip(yticks, ylabels):
            if v != self.yr[0]:
                ax.plot([self.px[0], self.px[1]], [self.Y(v)] * 2, color=GRID,
                        lw=1.6 * PT, zorder=0)
            text(ax, self.px[0] - 15, self.Y(v), lab, size=F_TEXT, color=MUTED, ha="right")
        ax.plot([self.px[0], self.px[1]], [self.py[0]] * 2, color="#9A9A94",
                lw=1.6 * PT, zorder=1)
        for v, lab in zip(xticks, xlabels):
            text(ax, self.X(v), self.py[0] + 27, lab, size=F_TEXT, color=MUTED, ha="center")
        text(ax, (self.px[0] + self.px[1]) / 2, self.py[0] + 60, xlabel, size=F_TEXT,
             color=MUTED, ha="center")

    def line(self, xs, ys, color, lw=4.0, z=3, **kw):
        self.ax.plot([self.X(v) for v in xs], [self.Y(v) for v in ys], color=color,
                     lw=lw * PT, solid_capstyle="round", zorder=z, **kw)


def save(fig, outdir, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=DPI, facecolor="white")
    plt.close(fig)
    print("wrote", path)


# ---------------------------------------------------------------------------
# Figure 1: three states (Section 2.2)
# ---------------------------------------------------------------------------

def fig01(outdir):
    a = 0.5  # base rate
    states = [  # (label, b, d, u)
        ("Ignorance", 0.05, 0.05, 0.90),
        ("Ambivalence", 0.45, 0.45, 0.10),
        ("Justified trust", 0.85, 0.05, 0.10),
    ]
    fig, ax = canvas(456)
    title(ax, "Ignorance and ambivalence have the same expected value, but a different position",
          "Shares of trust, distrust and uncertainty per state (illustrative values)", y=42)

    x0, x1 = 353, 1060
    ly = 127
    for lx, col, lab in ((353, BAR_BLUE, "Trust b"), (556, BAR_RED, "Distrust d"),
                         (777, BAR_GREY, "Uncertainty u")):
        ax.add_patch(Rectangle((lx, ly - 10), 21, 21, color=col, lw=0))
        text(ax, lx + 33, ly, lab, size=F_TEXT, color=MUTED)
    text(ax, 1097, ly, "Expectation E = b + a·u", size=F_TEXT, color=MUTED)

    for i, (lab, b, d, u) in enumerate(states):
        cy = 193 + 85 * i
        text(ax, 43, cy, lab, size=F_BOX_TITLE + 1)
        pos = x0
        for val, col in ((b, BAR_BLUE), (d, BAR_RED), (u, BAR_GREY)):
            w = val * (x1 - x0)
            ax.add_patch(Rectangle((pos, cy - 24), w, 48, color=col, lw=0))
            if val >= 0.1:
                text(ax, pos + w / 2, cy, num(val), size=F_TEXT)
            pos += w
        e = b + a * u
        text(ax, 1097, cy, f"E = {num(e)}", size=F_BOX_TITLE + 1, weight="bold")
    save(fig, outdir, "fig-01-states.png")


# ---------------------------------------------------------------------------
# Figure 2: example graph (Chapter 3)
# ---------------------------------------------------------------------------

def fig02(outdir):
    fig, ax = canvas(596)
    title(ax, "Trust is directed and holds per context", y=50)
    box(ax, 70, 113, 335, 331, "Person A", "rates B")
    box(ax, 1007, 113, 1273, 331, "Person B", "rates A")
    box(ax, 70, 442, 335, 540, "AI agent", "technical entity")
    box(ax, 1007, 442, 1273, 540, "Team", "group as a node")

    polyline(ax, [(337, 162), (1005, 162)], color=BLUE, lw=2.6, z=3)
    text(ax, 671, 141, "Professional judgment: high trust", size=F_TEXT, ha="center")
    polyline(ax, [(337, 230), (1005, 230)], color=BLUE, lw=2.6, z=3)
    text(ax, 671, 209, "Lending money: low trust", size=F_TEXT, ha="center")
    polyline(ax, [(1005, 296), (337, 296)], color=LINE, lw=2.2)
    text(ax, 671, 275, "Reverse direction, professional judgment: medium trust",
         size=F_TEXT, color=MUTED, ha="center")

    polyline(ax, [(203, 333), (203, 440)], color=LINE, lw=2.2)
    text(ax, 225, 386, "Code execution: still unknown (u high)", size=F_TEXT, color=MUTED)
    ax.plot([1140, 1140], [333, 440], color=LINE, lw=2.2 * PT, ls=(0, (3, 3)), zorder=1)
    text(ax, 1118, 386, "Membership, no trust judgment", size=F_TEXT, color=MUTED, ha="right")
    save(fig, outdir, "fig-02-graph.png")


# ---------------------------------------------------------------------------
# Figure 3: temporal decay (Section 4.3)
# ---------------------------------------------------------------------------

def fig03(outdir):
    W, a, lam = 2.0, 0.5, 0.9
    r0, s0 = 40.0, 0.0  # amount of evidence 40, all positive
    days = [i / 10 for i in range(0, 601)]
    E, U = [], []
    for t in days:
        r, s = r0 * lam ** t, s0 * lam ** t
        n = r + s + W
        E.append((r + a * W) / n)
        U.append(W / n)

    fig, ax = canvas(596)
    title(ax, "Without new evidence, trust returns to the base rate and uncertainty rises",
          "Example: prior strength W = 2, amount of evidence 40, forgetting factor "
          "λ = 0.9 per day (illustrative values)", y=42)
    c = Chart(ax, 113, 1032, 494, 158, 0, 60, 0, 1)
    c.grid([0, 0.25, 0.5, 0.75, 1], ["0", "0.25", "0.5", "0.75", "1"],
           range(0, 61, 10), [str(v) for v in range(0, 61, 10)], "Days without new evidence")
    ax.plot([c.X(0), c.X(60)], [c.Y(a)] * 2, color="#8A8A85", lw=1.2 * PT,
            ls=(0, (4, 3)), zorder=2)
    text(ax, 127, c.Y(a) + 23, f"Base rate a = {num(a, 1)}", size=F_TEXT, color=MUTED)
    c.line(days, U, LINE)
    c.line(days, E, BLUE)
    text(ax, 1047, c.Y(U[-1]), "Uncertainty u", size=F_TEXT, color=MUTED)
    text(ax, 1047, c.Y(E[-1]), "Trust E", size=F_TEXT, weight="bold")
    save(fig, outdir, "fig-03-temporal-decay.png")


# ---------------------------------------------------------------------------
# Figure 4: effective sample (Section 4.7)
# ---------------------------------------------------------------------------

def fig04(outdir):
    def n_eff(n, D):
        return n / (1 + (n - 1) * D)

    ns = list(range(1, 11))
    fig, ax = canvas(596)
    title(ax, "At D = 0.5, any number of repetitions counts at most as two sources",
          "Effective number of independent sources depending on the dependence D "
          "of the sources", y=42)
    c = Chart(ax, 113, 961, 494, 158, 1, 10, 0, 10)
    c.grid(range(0, 11, 2), [str(v) for v in range(0, 11, 2)], ns, [str(v) for v in ns],
           "Number of perceived repetitions n")
    D_lim = 0.5
    ax.plot([c.X(1), c.X(10)], [c.Y(1 / D_lim)] * 2, color="#8A8A85", lw=1.2 * PT,
            ls=(0, (4, 3)), zorder=2)
    text(ax, 955, c.Y(1 / D_lim) - 18, f"Limit 1/D = {1 / D_lim:g}", size=F_TEXT,
         color=MUTED, ha="right")
    labels = {0.0: "D = 0 (independent)", 0.2: "D = 0.2", 0.5: "D = 0.5",
              1.0: "D = 1 (one source)"}
    for D in (0.0, 0.2, 1.0, 0.5):
        ys = [n_eff(n, D) for n in ns]
        hi = D == 0.5
        c.line(ns, ys, BLUE if hi else LINE, z=4 if hi else 3)
        text(ax, 980, c.Y(ys[-1]), labels[D], size=F_TEXT,
             color=INK if hi else MUTED, weight="bold" if hi else "normal")
    save(fig, outdir, "fig-04-source-dependence.png")


# ---------------------------------------------------------------------------
# Figure 5: learning trap (Section 5.4)
# ---------------------------------------------------------------------------

def fig05(outdir):
    fig, ax = canvas(502)
    title(ax, "Distrust stabilizes itself: without interaction no evidence arises", y=50)
    box(ax, 42, 113, 307, 211, "Belief", "prior a, strength W")
    box(ax, 364, 113, 629, 211, "Interpretation", "valence v")
    box(ax, 686, 113, 951, 211, "Trust", "E and uncertainty u")
    box(ax, 1007, 113, 1301, 211, "Above the threshold?", "interaction is worthwhile")
    box(ax, 364, 325, 629, 423, "New experience", "evidence r and s")
    box(ax, 1007, 311, 1301, 444, "No interaction",
        "no new evidence,\nonly temporal decay acts", highlight=True)

    polyline(ax, [(309, 160), (362, 160)])
    polyline(ax, [(631, 160), (684, 160)])
    polyline(ax, [(953, 160), (1005, 160)])
    polyline(ax, [(1078, 213), (1078, 264), (562, 264), (562, 323)])
    text(ax, 1060, 242, "yes", size=F_TEXT, color=MUTED, ha="right")
    polyline(ax, [(1237, 213), (1237, 309)])
    text(ax, 1255, 262, "no", size=F_TEXT, color=MUTED)
    polyline(ax, [(431, 323), (431, 213)])
    text(ax, 413, 272, "is interpreted", size=F_TEXT, color=MUTED, ha="right")
    save(fig, outdir, "fig-05-learning-trap.png")


# ---------------------------------------------------------------------------
# Figure 6: architecture (Chapter 8)
# ---------------------------------------------------------------------------

def fig06(outdir):
    fig, ax = canvas(484)
    title(ax, "The gap between felt and justified trust is the attack surface", y=50)
    box(ax, 42, 211, 290, 339, "Event", "request, message\nor observation")
    box(ax, 346, 211, 629, 339, "Assess source", "independence D\ndiagnosticity q")
    box(ax, 700, 124, 1018, 250, "Normative account", "counts only independent,\ncostly evidence")
    box(ax, 700, 300, 1018, 427, "Descriptive account",
        "additionally counts\nrepetition, interpretation")
    box(ax, 1075, 124, 1301, 250, "Decision", "threshold per\naction class")
    box(ax, 1075, 300, 1301, 427, "Gap Γ", "attack surface,\ntraining target",
        highlight=True)

    polyline(ax, [(292, 273), (344, 273)])
    polyline(ax, [(631, 254), (664, 254), (664, 186), (698, 186)])
    polyline(ax, [(631, 297), (664, 297), (664, 364), (698, 364)])
    polyline(ax, [(1020, 167), (1073, 167)])
    polyline(ax, [(1020, 218), (1045, 218), (1045, 336), (1073, 336)])
    polyline(ax, [(1020, 364), (1073, 364)])
    save(fig, outdir, "fig-06-architecture.png")


# ---------------------------------------------------------------------------
# Figure 7: quick procedure (Section 9.3)
# ---------------------------------------------------------------------------

def diamond(ax, cx, cy, hw, hh, label, highlight=False):
    edge = BLUE if highlight else BOX_EDGE
    face = BLUE_FILL if highlight else "white"
    lw = 3.0 if highlight else 2.0
    ax.add_patch(Polygon([(cx - hw, cy), (cx, cy - hh), (cx + hw, cy), (cx, cy + hh)],
                         closed=True, edgecolor=edge, facecolor=face, lw=lw * PT,
                         joinstyle="round", zorder=2))
    text(ax, cx, cy, label, size=F_BOX_TITLE, weight="bold", ha="center",
         linespacing=1.4, zorder=3)


def fig07(outdir):
    fig, ax = canvas(530)
    title(ax, "The action triggers the verification, not the gut feeling", y=50)
    box(ax, 42, 146, 190, 243, "Request", "comes in")
    diamond(ax, 374, 194, 143, 78, "Risky\naction?", highlight=True)
    box(ax, 558, 146, 800, 243, "Verify", "via a second channel")
    diamond(ax, 933, 194, 98, 71, "Confirmed?")
    box(ax, 1075, 146, 1301, 243, "Execute", "limit scope")
    box(ax, 233, 371, 516, 470, "Process normally", "without additional verification")
    box(ax, 792, 371, 1075, 470, "Defer", "and report")

    polyline(ax, [(192, 194), (229, 194)])
    polyline(ax, [(519, 194), (556, 194)])
    text(ax, 536, 172, "yes", size=F_TEXT, color=MUTED, ha="center")
    polyline(ax, [(802, 194), (833, 194)])
    polyline(ax, [(1033, 194), (1073, 194)])
    text(ax, 1053, 172, "yes", size=F_TEXT, color=MUTED, ha="center")
    polyline(ax, [(374, 274), (374, 369)])
    text(ax, 390, 322, "no", size=F_TEXT, color=MUTED)
    polyline(ax, [(933, 267), (933, 369)])
    text(ax, 949, 318, "no", size=F_TEXT, color=MUTED)
    save(fig, outdir, "fig-07-quick-procedure.png")


# ---------------------------------------------------------------------------
# Figure 8: re-verification interval (Section 10.4)
# ---------------------------------------------------------------------------

def fig08(outdir):
    W, n0, lam = 2.0, 40.0, 0.9

    def u(t):
        return W / (W + n0 * lam ** t)

    def t_star(u_max):
        return math.log(W * (1 - u_max) / (u_max * n0)) / math.log(lam)

    ts = [i / 10 for i in range(0, 251)]
    fig, ax = canvas(596)
    title(ax, "Risky rights must be re-verified about twice as often",
          "Uncertainty since the last verification: W = 2, amount of evidence 40, "
          "λ = 0.9 per day (illustrative values)", y=42)
    c = Chart(ax, 113, 997, 494, 158, 0, 25, 0, 0.5)
    yt = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    c.grid(yt, ["0"] + [num(v, 1) for v in yt[1:]], range(0, 26, 5),
           [str(v) for v in range(0, 26, 5)], "Days since the last verification")
    c.line(ts, [u(t) for t in ts], LINE)
    text(ax, 1012, c.Y(u(25)), "Uncertainty u", size=F_TEXT, color=MUTED)

    classes = [(0.1, BLUE, "High risk", True), (0.2, "#8A8A85", "Low risk", False)]
    for k, (umax, col, name, hi) in enumerate(classes):
        ts_ = t_star(umax)
        x, y = c.X(ts_), c.Y(umax)
        ax.plot([c.X(0), x], [y, y], color=col, lw=2.4 * PT, ls=(0, (4, 3)), zorder=2)
        ax.plot([x, x], [y, c.Y(0)], color=col, lw=2.4 * PT, ls=(0, (4, 3)), zorder=2)
        ax.plot([x], [y], "o", ms=16 * PT, color=col, zorder=5)
        ly = 170 + 35 * k
        ax.plot([135], [ly], "o", ms=14 * PT, color=col, zorder=5)
        text(ax, 155, ly, f"{name} (u at most {num(umax, 1)}): re-verify after about "
             f"{round(ts_)} days", size=F_TEXT, color=INK if hi else MUTED,
             weight="bold" if hi else "normal")
    save(fig, outdir, "fig-08-reverification-interval.png")


# ---------------------------------------------------------------------------
# Figure 9: global shock (Section 12.4)
# ---------------------------------------------------------------------------

def fig09(outdir):
    delta_a = -0.3
    edges = [
        ("Long-standing supplier", 0.05),
        ("Colleague, daily contact", 0.15),
        ("Acquaintance, rare contact", 0.50),
        ("New business contact", 0.90),
        ("Unknown sender", 1.00),
    ]
    fig, ax = canvas(476)
    title(ax, "A global shock hits weakly evidenced relationships twenty times more strongly",
          "Change in expected trust when the base rate drops by 0.3 (illustrative values)",
          y=42)
    x0, scale = 417, 530 / 0.3
    ax.plot([x0, x0], [117, 440], color="#BDBCB4", lw=1.2 * PT, zorder=3)
    for i, (lab, u) in enumerate(edges):
        cy = 149 + 63.75 * i
        dE = u * delta_a  # Delta E = u * Delta a
        last = i == len(edges) - 1
        w = abs(dE) * scale
        ax.add_patch(Rectangle((x0, cy - 19), w, 38, lw=0,
                               color="#4A8CDC" if last else BAR_NEUTRAL, zorder=2))
        text(ax, 43, cy, lab, size=F_BOX_TITLE + 1)
        text(ax, x0 + w + 15, cy, f"{num(dE, 3)} (u = {num(u)})", size=F_TEXT,
             color=INK if last else MUTED, weight="bold" if last else "normal")
    save(fig, outdir, "fig-09-global-shock.png")


# ---------------------------------------------------------------------------
# Figure 10: trust dimensions and security objectives (Sections 13.3-13.6)
# ---------------------------------------------------------------------------

def fig10(outdir):
    fig, ax = canvas(720)
    title(ax, "Three dimensions have a security objective, competence needs a fourth", y=46)
    text(ax, 190, 119, "Trust dimensions · actor B", size=F_SMALL, color=MUTED,
         ha="center")
    text(ax, 1020, 119, "Security objectives · asset", size=F_SMALL, color=MUTED,
         ha="center")
    rows = [138, 243, 348, 453]
    left = [("Competence", "Can B do it?"), ("Benevolence", "Does B wish me well?"),
            ("Integrity", "Rules and truth?"),
            ("Predictability", "Does B behave consistently?")]
    right = [("Utility", "result fit for the purpose", True),
             ("Confidentiality", "no unauthorized outflow", False),
             ("Integrity (data)", "nothing falsified", False),
             ("Availability", "there when needed", False)]
    for y, (h, s) in zip(rows, left):
        box(ax, 40, y, 340, y + 81, h, s)
    for y, (h, s, hl) in zip(rows, right):
        box(ax, 870, y, 1170, y + 81, h, s, highlight=hl)
    box(ax, 40, 593, 340, 675, "Authenticity", "Is B really B?", highlight=True)

    # strong mappings: the diagonal
    for y in rows:
        polyline(ax, [(342, y + 41), (867, y + 41)], color=DARK_LINE, lw=2.4, z=2)
    # weak mappings: competence -> confidentiality, data integrity, availability;
    # integrity -> confidentiality
    weak = [((342, 197), (866, 272)), ((342, 205), (866, 377)), ((342, 213), (866, 482)),
            ((342, 369), (866, 296))]
    for p, q in weak:
        polyline(ax, [p, q], color="#A9A8A0", lw=1.5, dashed=True, z=1)
    # authenticity anchors all four dimensions
    polyline(ax, [(190, 591), (190, 543)], color=BLUE, lw=2.6, z=3)
    text(ax, 366, 635, "Anchor beneath all four dimensions:\n"
         "whoever takes over the identity inherits the whole profile",
         size=F_SMALL, color=MUTED, linespacing=1.4)
    ax.plot([875, 937], [626, 626], color=DARK_LINE, lw=2.4 * PT)
    ax.plot([875, 937], [664, 664], color="#A9A8A0", lw=1.5 * PT, ls=(0, (4, 4)))
    text(ax, 950, 626, "strong mapping", size=F_SMALL, color=MUTED)
    text(ax, 950, 664, "weak mapping", size=F_SMALL, color=MUTED)
    save(fig, outdir, "fig-10-security-objectives.png")


# ---------------------------------------------------------------------------
# Figure 11: verification coverage against the number of possible verifiers
# (Section 7.9): C = 1 - rho^(n/(n-1)), rho = K / (tau (1 - E) L)
# ---------------------------------------------------------------------------

def fig11(outdir):
    def coverage(rho, n):
        return 1.0 if n == 1 else 1 - rho ** (n / (n - 1))

    ns = list(range(1, 9))
    fig, ax = canvas(640)
    title(ax, "More possible verifiers, less coverage",
          "Verification coverage C when every verifier presumes the same of the others; "
          "ρ = K / (τ (1 − E) L) (illustrative values)", y=42)
    c = Chart(ax, 113, 997, 494, 158, 1, 8, 0, 1.0)
    yt = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    c.grid(yt, ["0"] + [num(v, 1) for v in yt[1:]], ns, [str(n) for n in ns],
           "Number of possible verifiers n (no role assigned)")
    c.line([1, 8], [1, 1], BLUE, lw=3.0, ls=(0, (4, 3)))
    text(ax, 1012, c.Y(1.0), "Named role: C = 1", size=F_TEXT, color=BLUE, weight="bold")
    curves = [(0.1, INK, "High visible loss (ρ = 0.1)"),
              (0.3, DARK_LINE, "Medium (ρ = 0.3)"),
              (0.6, "#B04A48", "Looks harmless (ρ = 0.6)")]
    for rho, col, name in curves:
        ys = [coverage(rho, n) for n in ns]
        c.line(ns, ys, col)
        for n, y in zip(ns, ys):
            ax.plot([c.X(n)], [c.Y(y)], "o", ms=12 * PT, color=col, zorder=5)
        text(ax, 1012, c.Y(ys[-1]), name, size=F_TEXT, color=col)
    text(ax, 113, 598, "n = 1: the single verifier always verifies (ρ < 1). "
         "From n = 2 on, coverage falls with every further unassigned verifier "
         "and falls faster the smaller the loss.", size=F_SMALL, color=MUTED)
    save(fig, outdir, "fig-11-verification-coverage.png")


# ---------------------------------------------------------------------------
# Figure F1.1 of Case Study 1: attack chain on the macro level (Section F1.5)
# ---------------------------------------------------------------------------

def fig_f1_1(outdir):
    fig, ax = canvas(500)
    title(ax, "Attack chain on the macro level",
          "Feedback loop via dependent sources", y=48)
    top, bot = (130, 250), (330, 450)
    cols = [(42, 410), (488, 856), (934, 1302)]
    box(ax, cols[0][0], top[0], cols[0][1], top[1], "Silent majority",
        "group boundary,\na for S rises")
    box(ax, cols[1][0], top[0], cols[1][1], top[1], "Straw man",
        "s on edges to F rises (π < 1)")
    box(ax, cols[2][0], top[0], cols[2][1], top[1], "False dilemma", "u becomes d")
    box(ax, cols[2][0], bot[0], cols[2][1], bot[1], "Motte-and-bailey", "no counter-evidence")
    box(ax, cols[1][0], bot[0], cols[1][1], bot[1], "Edges to F",
        "below the interaction\nthreshold")
    box(ax, cols[0][0], bot[0], cols[0][1], bot[1], "Learning trap",
        "no correction, Σ stays high", highlight=True)
    mid_top, mid_bot = sum(top) / 2, sum(bot) / 2
    polyline(ax, [(cols[0][1] + 2, mid_top), (cols[1][0] - 2, mid_top)])
    polyline(ax, [(cols[1][1] + 2, mid_top), (cols[2][0] - 2, mid_top)])
    xc = sum(cols[2]) / 2
    polyline(ax, [(xc, top[1] + 2), (xc, bot[0] - 2)])
    polyline(ax, [(cols[2][0] - 2, mid_bot), (cols[1][1] + 2, mid_bot)])
    polyline(ax, [(cols[1][0] - 2, mid_bot), (cols[0][1] + 2, mid_bot)])
    xa = sum(cols[0]) / 2
    polyline(ax, [(xa, bot[0] - 2), (xa, top[1] + 2)], color=BLUE, dashed=True)
    text(ax, xa + 14, (top[1] + bot[0]) / 2, "internal repetition, D close to 1",
         size=F_SMALL, color=BLUE, ha="left")
    save(fig, outdir, "fig-f1-1-attack-chain.png")


DEFAULT_OUT = os.environ.get(
    "FIGURES_OUT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT
    os.makedirs(outdir, exist_ok=True)
    for f in (fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09, fig10, fig11, fig_f1_1):
        f(outdir)


if __name__ == "__main__":
    main()
