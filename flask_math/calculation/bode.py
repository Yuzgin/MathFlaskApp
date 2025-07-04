from flask import make_response
from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from io import BytesIO

def bode(formula, lower_end, upper_end):
    s = symbols('s')
    try:
        formula = sympify(formula)
        formula_2 = lambdify(s, formula, "numpy")
    except Exception:
        raise ValueError("Invalid formula.")

    title = ""
    width = 100

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)  # Gain plot
    ax2 = fig.add_subplot(2, 1, 2)  # Phase plot

    # Generate frequency range (logarithmic scale)
    w_list = np.array([10**(i / width) for i in range(int(lower_end) * width, int(upper_end) * width, 1)])
    Gw = formula_2(1j * w_list)
    if np.isscalar(Gw):
        Gw = np.full_like(w_list, Gw, dtype=np.complex128)
    g_list = 20 * np.log10(np.abs(Gw))
    φ_list = np.rad2deg(np.angle(Gw))
    g_list = np.atleast_1d(g_list)
    φ_list = np.atleast_1d(φ_list)
    φ_list[φ_list > 0] -= 360  # Wrap phase to [-360, 0]

    # Estimate gain crossover frequency (Wc) and phase margin (Pm)
    try:
        idx_g_cross = np.where(np.abs(g_list) < 5)[0]
        if idx_g_cross.size > 0:
            tmpWc = np.average(w_list[idx_g_cross])
            w_list_c = np.linspace(tmpWc - 0.3, tmpWc + 0.3, 61)
            g_list_c = 20 * np.log10(np.abs(formula_2(1j * w_list_c)))
            Wc = w_list_c[np.argmin(np.abs(g_list_c))]
            Pm = 180 + np.rad2deg(np.angle(formula_2(1j * Wc)))
            ax1.axvline(x=Wc, color="black")
            ax2.axvline(x=Wc, color="black")
            title += f"Wc={round(Wc, 2)} rad/s, Pm={round(Pm, 2)} deg, "
    except Exception:
        pass

    # Estimate phase crossover frequency (Wp) and gain margin (Gm)
    try:
        idx_phase_cross = np.where((-190 < φ_list) & (φ_list < -170))[0]
        if idx_phase_cross.size > 0:
            tmpWp = np.average(w_list[idx_phase_cross])
            w_list_p = np.linspace(tmpWp - 0.3, tmpWp + 0.3, 61)
            φ_list_p = np.rad2deg(np.angle(formula_2(1j * w_list_p)))
            φ_list_p = np.atleast_1d(φ_list_p)
            φ_list_p[φ_list_p > 0] -= 360
            Wp = w_list_p[np.argmin(np.abs(180 + φ_list_p))]
            Gm = -20 * np.log10(np.abs(formula_2(1j * Wp)))
            ax1.axvline(x=Wp, color="black")
            ax2.axvline(x=Wp, color="black")
            title += f"Wπ={round(Wp, 2)} rad/s, Gm={round(Gm, 2)} dB, "
    except Exception:
        pass

    # Plot gain and phase
    ax1.plot(w_list, g_list)
    ax2.plot(w_list, φ_list)
    ax1.set_xscale("log")
    ax2.set_xscale("log")
    ax1.axhline(y=0, color="black")      # 0 dB line
    ax2.axhline(y=-180, color="black")   # -180 deg line

    ax1.set_title(f"$G(s)={LATEX(formula)}$")
    plt.title(title, y=-0.30)

    # Output image to canvas
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    # Use Flask app context if available, else create a dummy response
    try:
        response = make_response(data)
        response.headers['Content-Type'] = 'image/png'
        response.headers['Content-Length'] = str(len(data))
        return response
    except RuntimeError:
        # For unit tests without app context, return raw image data for assertion
        class DummyResponse:
            status_code = 200
            headers = {'Content-Type': 'image/png', 'Content-Length': str(len(data))}
            def __init__(self, data):
                self.data = data
        return DummyResponse(data)
