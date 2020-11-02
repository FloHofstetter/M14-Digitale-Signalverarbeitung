#!/usr/bin/env python
# coding: utf-8

# # M14 - Digitale Signalverarbeitung
# ## Aufgabe 2 - Diskrete Faltung von Signalen

# # 0. Einrichten der Umgebung
# ## 0.1 Import der Bibelioteken

# In[1]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# plt.style.use('ggplot')


# # 2. Das System
# Es handelt sich um einen Tiefpass 1. Ordnung, also ein LTI-System.
# ![LTI-System](Images/02_Faltung/System.png)

# # 2. Eingangssignale
# ## 2.1 Konstante Parameter des Systems und der diskreten Signale

# In[2]:


# Time credentials
START_TIME = 0.0
STOP_TIME = 10.0
SAMPLE_RATE = 0.5

# System credentials
TAU_LOWPASS = 1


# ## 2.2 Erzeugung der Signale

# In[3]:


# Zeitachse
t = np.arange(start=START_TIME, stop=STOP_TIME + SAMPLE_RATE, step=SAMPLE_RATE)
total_sampels = len(t)

# Eingangsfunktionen
y_sin = np.sin(t)
y_rec = np.array([1. if 1 < x < 3 else 0. for x in t])
y_dir = np.array([1 if x == 1. else 0 for x in t])


# ## 2.3 Plot der Eingangssignale

# In[4]:


fig, axs = plt.subplots(ncols=3, nrows=1, figsize=[15, 4])
X_LABEL = "t in s"
Y_LABEL = "y(t)"


# In[5]:


ax0 = fig.add_subplot(axs[0])
ax1 = fig.add_subplot(axs[1])
ax2 = fig.add_subplot(axs[2])


# In[6]:


def setup_axis0():
    ax0.set_xlim(0.0, 10.0)
    ax0.set_ylim(-1.10, 1.10)

    ax0.set_title("Sinus")
    ax0.set_xlabel(X_LABEL)
    ax0.set_ylabel(Y_LABEL)

    ax0.grid(True)
    ax0.minorticks_on()


# In[7]:


def setup_axis1():
    ax1.set_xlim(0.0, 10.0)
    ax1.set_ylim(-1.10, 1.10)

    ax1.set_title("Rechteck")
    ax1.set_xlabel(X_LABEL)
    ax1.set_ylabel(Y_LABEL)

    ax1.grid(True)
    ax1.minorticks_on()


# In[8]:


def setup_axis2():
    ax2.set_xlim(0.0, 10.0)
    ax2.set_ylim(-1.10, 1.10)

    ax2.set_title("Dirac")
    ax2.set_xlabel(X_LABEL)
    ax2.set_ylabel(Y_LABEL)

    ax2.grid(True)
    ax2.minorticks_on()


# In[9]:


def animate(i):
    fig.suptitle("Input signal on Timestep: {:02d}".format(i))
    ax0.clear()
    ax1.clear()
    ax2.clear()
    setup_axis0()
    setup_axis1()
    setup_axis2()
    ax0.stem(t[:i+1], y_sin[:i+1])
    ax1.stem(t[:i+1], y_rec[:i+1])
    ax2.stem(t[:i+1], y_dir[:i+1])
    # ax.clear()
    # setup_ax()
    # markerline, stemlines, baseline = ax.stem(t[:i+1], y_sin[:i+1])


# In[10]:


# https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib
left  = None # 0.125  # the left side of the subplots of the figure
right = None # 0.9    # the right side of the subplots of the figure
bottom = None # 0.1   # the bottom of the subplots of the figure
top = None  # 0.9      # the top of the subplots of the figure
wspace = 0.5   # the amount of width reserved for blank space between subplots
hspace = None  # 0.2   # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
plt.draw()
# plt.tight_layout()
# plt.show()


anim = FuncAnimation(fig, animate, interval=250, frames=len(t))


# In[11]:


# anim.save('filename.mp4')


# In[12]:


# anim.save('filename.gif', writer='imagemagick')


# In[13]:




# ## 2.4 Definition der Impulsanwort auf das System

# In[14]:


def impuls_response_lowpass(t, tau):
    """
    Berechnung der Impulsantwort eines Tiefpasses 1. Ordnung.
    """
    h = 1./tau * np.exp(-t/tau)
    return h


# In[15]:


y_impulse_response = np.array([impuls_response_lowpass(x, TAU_LOWPASS) for x in t])


# Löschen des Alten Plot Objekts:

# In[16]:


fig.clear()
del fig


# ## 2.5 Plot der Impulsantwort

# In[17]:


# Zeitverschiebung Eingangssignal
t_shift = np.array([x - (total_sampels - 1) * SAMPLE_RATE for x in t])

# Eingangsfunktionen gespiegelt
y_sin_flip = np.flip(y_sin)
y_rec_flip = np.flip(y_rec)
y_dir_flip = np.flip(y_dir)


# In[18]:


fig, axs = plt.subplots(ncols=3, nrows=2, figsize=[25, 8])
X_LABEL = "t in s"
Y_LABEL = "y(t)"


# In[19]:


ax0 = fig.add_subplot(axs[0, 0])
ax1 = fig.add_subplot(axs[0, 1])
ax2 = fig.add_subplot(axs[0, 2])
ax3 = fig.add_subplot(axs[1, 0])
ax4 = fig.add_subplot(axs[1, 1])
ax5 = fig.add_subplot(axs[1, 2])


# In[20]:


def setup_axis0():
    ax0.set_xlim(-10.0, 10.0)
    ax0.set_ylim(-1.10, 1.10)

    ax0.set_title("Sinus")
    ax0.set_xlabel(X_LABEL)
    ax0.set_ylabel(Y_LABEL)

    ax0.grid(True)
    ax0.minorticks_on()


# In[21]:


def setup_axis1():
    ax1.set_xlim(-10.0, 10.0)
    ax1.set_ylim(-1.10, 1.10)

    ax1.set_title("Rechteck")
    ax1.set_xlabel(X_LABEL)
    ax1.set_ylabel(Y_LABEL)

    ax1.grid(True)
    ax1.minorticks_on()


# In[22]:


def setup_axis2():
    ax2.set_xlim(-10.0, 10.0)
    ax2.set_ylim(-1.10, 1.10)

    ax2.set_title("Dirac")
    ax2.set_xlabel(X_LABEL)
    ax2.set_ylabel(Y_LABEL)

    ax2.grid(True)
    ax2.minorticks_on()


# In[23]:


def setup_axis3():
    ax3.set_xlim(-10.0, 10.0)
    ax3.set_ylim(-2.10, 2.10)

    ax3.set_title("Dirac")
    ax3.set_xlabel(X_LABEL)
    ax3.set_ylabel(Y_LABEL)

    ax3.grid(True)
    ax3.minorticks_on()


# In[24]:


def setup_axis4():
    ax4.set_xlim(-10.0, 10.0)
    ax4.set_ylim(-2.10, 2.10)

    ax4.set_title("Dirac")
    ax4.set_xlabel(X_LABEL)
    ax4.set_ylabel(Y_LABEL)

    ax4.grid(True)
    ax4.minorticks_on()


# In[25]:


def setup_axis5():
    ax5.set_xlim(-10.0, 10.0)
    ax5.set_ylim(-2.10, 2.10)

    ax5.set_title("Dirac")
    ax5.set_xlabel(X_LABEL)
    ax5.set_ylabel(Y_LABEL)

    ax5.grid(True)
    ax5.minorticks_on()


# In[26]:


def convolve(x0, y0, x1, y1):
    y = []
    for a, b in zip(x0, y0):
        for c, d in zip(list(x1), list(y1)):
            if a == c:
                y.append(b * d * SAMPLE_RATE)
    return sum(y)
                


# In[27]:


a3 = []
a4 = []
a5 = []
def animate(i):
    a3.append(convolve(t_shift + i * SAMPLE_RATE, y_sin_flip, t, y_impulse_response))
    a3_ = np.array(a3)
    a3_.resize(t.shape)
    a4.append(convolve(t_shift + i * SAMPLE_RATE, y_rec_flip, t, y_impulse_response))
    a4_ = np.array(a4)
    a4_.resize(t.shape)
    a5.append(convolve(t_shift + i * SAMPLE_RATE, y_dir_flip, t, y_impulse_response))
    a5_ = np.array(a5)
    a5_.resize(t.shape)
    fig.suptitle("Input signal on Timestep: {:02d}".format(i))
    ax0.clear()
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    setup_axis0()
    setup_axis1()
    setup_axis2()
    setup_axis3()
    setup_axis4()
    setup_axis5()
    ax0.stem(t, y_impulse_response, linefmt="C1-", markerfmt="C1o")
    ax0.stem(t_shift + i * SAMPLE_RATE, y_sin_flip)
    ax1.stem(t, y_impulse_response, linefmt="C1-", markerfmt="C1o")
    ax1.stem(t_shift + i * SAMPLE_RATE, y_rec_flip)
    ax2.stem(t, y_impulse_response, linefmt="C1-", markerfmt="C1o")
    ax2.stem(t_shift + i * SAMPLE_RATE, y_dir_flip)
    ax3.stem(t, a3_)
    ax4.stem(t, a4_)
    ax5.stem(t, a5_)
    
    
    # ax.clear()
    # setup_ax()
    # markerline, stemlines, baseline = ax.stem(t[:i+1], y_sin[:i+1])


# In[28]:


# https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib
left  = None # 0.125  # the left side of the subplots of the figure
right = None # 0.9    # the right side of the subplots of the figure
bottom = None # 0.1   # the bottom of the subplots of the figure
top = None  # 0.9      # the top of the subplots of the figure
wspace = 0.25   # the amount of width reserved for blank space between subplots
hspace = 0.30  # 0.2   # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
plt.draw()
# plt.tight_layout()
plt.show()


anim = FuncAnimation(fig, animate, interval=250, frames=2 * len(t))


# In[29]:




# In[30]:


# anim.save('Faltung.mp4')


# In[31]:


# anim.save('Faltung.gif', writer="pillow")

