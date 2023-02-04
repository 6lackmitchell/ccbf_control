import matplotlib

matplotlib.use("Qt5Agg")

import os
import glob
import pickle
import traceback
from sys import platform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from .timing_params import dt, tf
from .initial_conditions import xg

matplotlib.rcParams.update({"figure.autolayout": True})

if platform == "linux" or platform == "linux2":
    # linux
    pre_path = "/home/6lackmitchell/"
elif platform == "darwin":
    # OS X
    pre_path = "/Users/mblack/"
elif platform == "win32":
    # Windows...
    pass

# Specify files
filepath = pre_path + "Documents/git/ccbf-control/data/nonlinear_1d/default/academic_example/paper/"
fname1 = filepath + "alpha_0p1_pos.pkl"
fname2 = filepath + "alpha_0p5_pos.pkl"
fname3 = filepath + "alpha_1_pos.pkl"
fname4 = filepath + "alpha_5_pos.pkl"
fname5 = filepath + "alpha_10_pos.pkl"

# ### Define Recording Variables ###
t = np.linspace(dt, tf, int(tf / dt))

# Load Simulation Data
with open(fname1, "rb") as f:
    data = pickle.load(f)

    x1 = np.array([data[a]["x"] for a in data.keys()])
    u1 = np.array([data[a]["u"] for a in data.keys()])
    u01 = np.array([data[a]["u0"] for a in data.keys()])
    czero11 = np.array([data[a]["czero1"] for a in data.keys()])
    czero21 = np.array([data[a]["czero2"] for a in data.keys()])
    k1 = np.array([data[a]["kgains"] if a < 1 else None for a in data.keys()][:1])
    kdot1 = np.array([data[a]["kdot"] if a < 1 else None for a in data.keys()][:1])
    kdotf1 = np.array([data[a]["kdotf"] if a < 1 else None for a in data.keys()][:1])
    ii = int(data[0]["ii"] / dt)
with open(fname2, "rb") as f:
    data = pickle.load(f)

    x2 = np.array([data[a]["x"] for a in data.keys()])
    u2 = np.array([data[a]["u"] for a in data.keys()])
    u02 = np.array([data[a]["u0"] for a in data.keys()])
    czero12 = np.array([data[a]["czero1"] for a in data.keys()])
    czero22 = np.array([data[a]["czero2"] for a in data.keys()])
    k2 = np.array([data[a]["kgains"] if a < 1 else None for a in data.keys()][:1])
    kdot2 = np.array([data[a]["kdot"] if a < 1 else None for a in data.keys()][:1])
    kdotf2 = np.array([data[a]["kdotf"] if a < 1 else None for a in data.keys()][:1])
with open(fname3, "rb") as f:
    data = pickle.load(f)

    x3 = np.array([data[a]["x"] for a in data.keys()])
    u3 = np.array([data[a]["u"] for a in data.keys()])
    u03 = np.array([data[a]["u0"] for a in data.keys()])
    czero13 = np.array([data[a]["czero1"] for a in data.keys()])
    czero23 = np.array([data[a]["czero2"] for a in data.keys()])
    k3 = np.array([data[a]["kgains"] if a < 1 else None for a in data.keys()][:1])
    kdot3 = np.array([data[a]["kdot"] if a < 1 else None for a in data.keys()][:1])
    kdotf3 = np.array([data[a]["kdotf"] if a < 1 else None for a in data.keys()][:1])
with open(fname4, "rb") as f:
    data = pickle.load(f)

    x4 = np.array([data[a]["x"] for a in data.keys()])
    u4 = np.array([data[a]["u"] for a in data.keys()])
    u04 = np.array([data[a]["u0"] for a in data.keys()])
    czero14 = np.array([data[a]["czero1"] for a in data.keys()])
    czero24 = np.array([data[a]["czero2"] for a in data.keys()])
    k4 = np.array([data[a]["kgains"] if a < 1 else None for a in data.keys()][:1])
    kdot4 = np.array([data[a]["kdot"] if a < 1 else None for a in data.keys()][:1])
    kdotf4 = np.array([data[a]["kdotf"] if a < 1 else None for a in data.keys()][:1])
with open(fname5, "rb") as f:
    data = pickle.load(f)

    x5 = np.array([data[a]["x"] for a in data.keys()])
    u5 = np.array([data[a]["u"] for a in data.keys()])
    u05 = np.array([data[a]["u0"] for a in data.keys()])
    czero15 = np.array([data[a]["czero1"] for a in data.keys()])
    czero25 = np.array([data[a]["czero2"] for a in data.keys()])
    k5 = np.array([data[a]["kgains"] if a < 1 else None for a in data.keys()][:1])
    kdot5 = np.array([data[a]["kdot"] if a < 1 else None for a in data.keys()][:1])
    kdotf5 = np.array([data[a]["kdotf"] if a < 1 else None for a in data.keys()][:1])


x = np.concatenate(
    [
        x1[np.newaxis, 0],
        x2[np.newaxis, 0],
        x3[np.newaxis, 0],
        x4[np.newaxis, 0],
        x5[np.newaxis, 0],
    ]
)
u = np.concatenate(
    [
        u1[np.newaxis, 0],
        u2[np.newaxis, 0],
        u3[np.newaxis, 0],
        u4[np.newaxis, 0],
        u5[np.newaxis, 0],
    ]
)
u0 = np.concatenate(
    [
        u01[np.newaxis, 0],
        u02[np.newaxis, 0],
        u03[np.newaxis, 0],
        u04[np.newaxis, 0],
        u05[np.newaxis, 0],
    ]
)
czero = np.concatenate(
    [
        czero11[np.newaxis, 0],
        czero12[np.newaxis, 0],
        czero13[np.newaxis, 0],
        czero14[np.newaxis, 0],
        czero15[np.newaxis, 0],
    ]
)
k = np.concatenate(
    [
        k1[np.newaxis, 0],
        k2[np.newaxis, 0],
        k3[np.newaxis, 0],
        k4[np.newaxis, 0],
        k5[np.newaxis, 0],
    ]
)
# x = np.concatenate(
#     [
#         x1[np.newaxis, 0],
#         x2[np.newaxis, 0],
#         x3[np.newaxis, 0],
#         x4[np.newaxis, 0],
#         x5[np.newaxis, 0],
#     ]
# )
# x = np.concatenate(
#     [
#         x1[np.newaxis, 0],
#         x2[np.newaxis, 0],
#         x3[np.newaxis, 0],
#         x4[np.newaxis, 0],
#         x5[np.newaxis, 0],
#     ]
# )
# x = np.concatenate(
#     [
#         x1[np.newaxis, 0],
#         x2[np.newaxis, 0],
#         x3[np.newaxis, 0],
#         x4[np.newaxis, 0],
#         x5[np.newaxis, 0],
#     ]
# )

names = [
    r"$\alpha = 0.1$",
    r"$\alpha = 0.5$",
    r"$\alpha = 1.0$",
    r"$\alpha = 2.0$",
    r"$\alpha = 5.0$",
]

# Plot Settings
nAgents = 5
plt.style.use(["ggplot"])
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.plasma(np.linspace(0, 1, nAgents)))
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
# colors[0] = colors[1]
colors[-1] = np.array([0.0, 0.98, 0.2, 1])
colors.reverse()
lwidth = 4
dash = [3, 2]


def set_edges_black(ax):
    ax.spines["bottom"].set_color("#000000")
    ax.spines["top"].set_color("#000000")
    ax.spines["right"].set_color("#000000")
    ax.spines["left"].set_color("#000000")


plt.close("all")


############################################
### Control Trajectories ###
fig_control = plt.figure(figsize=(12, 8))
ax_cont = fig_control.add_subplot(111)
set_edges_black(ax_cont)
set_edges_black(ax_cont)

ii_u = ii

# Angular Control Inputs
ax_cont.plot(t[1:ii_u], 1 * np.ones(t[1:ii_u].shape), linewidth=lwidth + 1, color="k")
ax_cont.plot(t[1:ii_u], -1 * np.ones(t[1:ii_u].shape), linewidth=lwidth + 1, color="k")
for aa in [0]:
    ax_cont.plot(
        t[:ii_u],
        u0[aa, :ii_u, 0],
        label=r"$u_0$",
        linewidth=lwidth,
        color=colors[aa],
        dashes=dash,
    )
for aa in [0, 1, 2, 3, 4]:
    ax_cont.plot(
        t[:ii_u],
        u[aa, :ii_u, 0],
        label=rf"$u$: {names[aa]}",
        linewidth=lwidth,
        color=colors[aa],
    )

# ax_cont.plot(
#     t[:ii_u], u[0, :ii_u, 0], label=names[0], linewidth=lwidth, color=colors[0], dashes=dash
# )
# ax_cont.plot(t[:ii_u], u0[0, :ii_u, 0], label=names[1], linewidth=lwidth, color=colors[1])
ax_cont.set(
    xlabel=r"$t$",
    ylabel=r"$u$",
    # ylim=[np.min(u[:ii_u, :, 0]) - 0.1, np.max(u[:ii_u, :, 0]) + 0.1],
    # xlim=[-0.1, 13.2],
    # title="Control Inputs",
)

for item in (
    [ax_cont.title, ax_cont.xaxis.label, ax_cont.yaxis.label]
    + ax_cont.get_xticklabels()
    + ax_cont.get_yticklabels()
):
    item.set_fontsize(25)

ax_cont.set_xticks([])
ax_cont.set_yticks([-1, 0, 1])
ax_cont.legend(fancybox=True, fontsize=20)
ax_cont.grid(True, linestyle="dotted", color="white")
# ax_cont.set_xticks([0, 2, 4, 6, 8, 10])

plt.tight_layout(pad=2.0)

############################################
### Gain Trajectories ###
fig_k = plt.figure(figsize=(8, 8))
ax_k = fig_k.add_subplot(111)
set_edges_black(ax_k)

# Angular Control Inputs
lbl = [
    [r"$w_1: \alpha = 0.1$", r"$w_2: \alpha = 0.1$"],
    [r"$w_1: \alpha = 0.5$", r"$w_2: \alpha = 0.5$"],
    [r"$w_1: \alpha = 1.0$", r"$w_2: \alpha = 1.0$"],
    [r"$w_1: \alpha = 2.0$", r"$w_2: \alpha = 2.0$"],
    [r"$w_1: \alpha = 5.0$", r"$w_2: \alpha = 5.0$"],
]
clr = plt.rcParams["axes.prop_cycle"].by_key()["color"]
clr.reverse()
for aa in [0, 1, 2, 3, 4]:
    ax_k.plot(t[1:ii], k[aa, 1:ii, 0], linewidth=lwidth, color=clr[aa], label=lbl[aa][0])
    ax_k.plot(t[1:ii], k[aa, 1:ii, 1], linewidth=lwidth, color=clr[aa], label=lbl[aa][1])
ax_k.set(ylabel=r"$w$", title="C-CBF Weights")

# Plot Settings
for item in (
    [ax_k.title, ax_k.xaxis.label, ax_k.yaxis.label]
    + ax_k.get_xticklabels()
    + ax_k.get_yticklabels()
):
    item.set_fontsize(25)
ax_k.legend(fancybox=True)
ax_k.grid(True, linestyle="dotted", color="white")

plt.tight_layout(pad=2.0)


# ############################################
# ### Kdot Trajectories ###
# fig_kdot = plt.figure(figsize=(8, 8))
# ax_kdot = fig_kdot.add_subplot(111)
# set_edges_black(ax_kdot)

# for cbf in range(k.shape[2]):
#     ax_kdot.plot(t[1:ii], kdot[0, 1:ii, cbf], linewidth=lwidth, color=clr[cbf], label=lbl[cbf])
#     ax_kdot.plot(
#         t[1:ii],
#         kdotf[0, 1:ii, cbf],
#         "-.",
#         linewidth=lwidth,
#         color=clr[cbf],
#         label=lbl[cbf],
#     )
# ax_kdot.set(ylabel=r"$\dot{w}$", title="Weight Derivatives")

# # Plot Settings
# for item in (
#     [ax_kdot.title, ax_kdot.xaxis.label, ax_kdot.yaxis.label]
#     + ax_kdot.get_xticklabels()
#     + ax_kdot.get_yticklabels()
# ):
#     item.set_fontsize(25)
# ax_kdot.legend(fancybox=True)
# ax_kdot.grid(True, linestyle="dotted", color="white")

# plt.tight_layout(pad=2.0)

# ############################################
# ### CZero Trajectories ###
# fig_cz = plt.figure(figsize=(8, 8))
# ax_cz = fig_cz.add_subplot(111)
# set_edges_black(ax_cz)

# ax_cz.plot(t[1:ii], czero1[0, 1:ii], linewidth=lwidth, color=colors[1], label="C_01")
# ax_cz.plot(t[1:ii], czero2[0, 1:ii], linewidth=lwidth, color=colors[2], label="C_02")
# ax_cz.set(ylabel=r"$b_{c+1}$", title="Sufficient Control Authority")

# # Plot Settings
# for item in (
#     [ax_cz.title, ax_cz.xaxis.label, ax_cz.yaxis.label]
#     + ax_cz.get_xticklabels()
#     + ax_cz.get_yticklabels()
# ):
#     item.set_fontsize(25)
# ax_cz.legend(fancybox=True)
# ax_cz.grid(True, linestyle="dotted", color="white")

# plt.tight_layout(pad=2.0)


# ############################################
# ### CBF Trajectories ###
# fig_cbf = plt.figure(figsize=(10, 6))
# ax_cbf = fig_cbf.add_subplot(111)
# set_edges_black(ax_cbf)

# gain1 = 2.0
# gain2 = 2.0
# gain3 = 2.0
# R1 = 0.5
# cx1 = 1.0
# cy1 = 1.0
# R2 = 0.5
# cx2 = 1.5
# cy2 = 2.25
# R3 = 0.5
# cx3 = 2.4
# cy3 = 1.5
# gain4 = 5.0
# gain5 = 5.0
# gain6 = 10.0

# ii_h6 = int(8 / 0.01)
# h1 = gain1 * ((x_ccbf[0, 1:ii_u, 0] - cx1) ** 2 + (x_ccbf[0, 1:ii_u, 1] - cy1) ** 2 - R1**2)
# h2 = gain2 * ((x_ccbf[0, 1:ii_u, 0] - cx2) ** 2 + (x_ccbf[0, 1:ii_u, 1] - cy2) ** 2 - R2**2)
# h3 = gain3 * ((x_ccbf[0, 1:ii_u, 0] - cx3) ** 2 + (x_ccbf[0, 1:ii_u, 1] - cy3) ** 2 - R2**2)
# h4 = gain4 * (1 - x_ccbf[0, 1:ii_u, 2] ** 2)
# h5 = gain5 * (1 - x_ccbf[0, 1:ii_u, 3] ** 2)
# # h6_a = gain6 * (
# #     (((2) ** 2) / 4 + (10 - t[1:ii_h6]) ** 2) / 4
# #     - (x_ccbf[0, 1:ii_h6, 0] - 2) ** 2
# #     - (x_ccbf[0, 1:ii_h6, 1] - 2) ** 2
# # )
# # h6_b = gain6 * (
# #     ((2) ** 2) / 4 - (x_ccbf[0, ii_h6:ii_u, 0] - 2) ** 2 - (x_ccbf[0, ii_h6:ii_u, 1] - 2) ** 2
# # )
# h6 = gain6 * (
#     (1 + (10 - t[1:ii_u]) ** 2) / 4
#     - (x_ccbf[0, 1:ii_u, 0] - 2) ** 2
#     - (x_ccbf[0, 1:ii_u, 1] - 2) ** 2
# )
# # h6 = np.concatenate([h6_a, h6_b])
# hh = np.array([h1, h2, h3, h4, h5, h6])
# summer = np.array([np.exp(-k[0, 1:ii_u, cc] * hh[cc]) for cc in range(6)])
# H_ccbf = 1 - np.sum(summer, axis=0)


# ax_cbf.plot(t[1:ii_u], np.zeros((ii_u - 1,)), ":", linewidth=lwidth, color="k", label="Barrier")
# ax_cbf.plot(t[1:ii_u], h1, linewidth=lwidth, color=colors[1], label=r"$h_1$")
# ax_cbf.plot(t[1:ii_u], h2, linewidth=lwidth, color=colors[2], label=r"$h_2$")
# ax_cbf.plot(t[1:ii_u], h3, linewidth=lwidth, color=colors[3], label=r"$h_3$")
# ax_cbf.plot(t[1:ii_u], h4, linewidth=lwidth, color=colors[4], label=r"$h_4$")
# ax_cbf.plot(t[1:ii_u], h5, linewidth=lwidth, color=colors[5], label=r"$h_5$")
# ax_cbf.plot(t[1:ii_u], h6, linewidth=lwidth, color=colors[6], label=r"$h_6$")
# ax_cbf.plot(t[1:ii_u], H_ccbf, linewidth=lwidth, color=colors[0], dashes=dash, label=r"$H$")
# ax_cbf.set(
#     ylabel="Constraint Function Value", xlabel=r"$t$ (sec)", xlim=[-0.25, 13.25], ylim=[-0.1, 5.25]
# )

# # Plot Settings
# for item in (
#     [ax_cbf.title, ax_cbf.xaxis.label, ax_cbf.yaxis.label]
#     + ax_cbf.get_xticklabels()
#     + ax_cbf.get_yticklabels()
# ):
#     item.set_fontsize(25)
# ax_cbf.legend(fancybox=True, fontsize=20)
# ax_cbf.grid(True, linestyle="dotted", color="white")

# plt.tight_layout(pad=2.0)


############################################
### State Trajectories ###
# plt.style.use(['dark_background'])
fig_state = plt.figure(figsize=(10, 7.5))
ax_state = fig_state.add_subplot(111)
set_edges_black(ax_state)

for aa in [0, 1, 2, 3, 4]:
    ax_state.plot(
        t[1:ii],
        x[aa, 1:ii, 0],
        label=names[aa],
        color=colors[aa],
        linewidth=lwidth,
    )
# ax_state.plot(xi[0], yi[0], "o", markersize=10, label=r"$z_0$", color="r")
ax_state.plot(t[1:ii], xg[0] * np.ones((len(t[1:ii]),)), label="Goal", color="g")

ax_state.set(
    # ylim=[-0.75, 2.25],
    # xlim=[-0.5, 3.5],
    xlabel=r"$t$ (sec)",
    ylabel=r"$x$",
)

# Plot Settings
for item in (
    [ax_state.title, ax_state.xaxis.label, ax_state.yaxis.label]
    + ax_state.get_xticklabels()
    + ax_state.get_yticklabels()
):
    item.set_fontsize(25)
# Hide X and Y axes label marks
# ax_map.xaxis.set_tick_params(labelbottom=False)
# ax_map.yaxis.set_tick_params(labelleft=False)
# Hide X and Y axes tick marks
# ax_map.set_xticks([])
# ax_map.set_yticks([])
ax_state.legend(fancybox=True, fontsize=15)
ax_state.grid(False)

plt.tight_layout(pad=2.0)
plt.show()
