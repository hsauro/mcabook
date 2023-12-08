.. default-role:: math 

Control Coefficients
====================

A control coefficient measures the influcence a change in an enzyme has on the steady-state flux or metabolite concentrations.

Imagine a simple metabolite pathway such as the one below is at ateady-state:

.. math:: X_o \stackrel{e_1}{\longrightarrow} S_1 \stackrel{e_2}{\longrightarrow} S_2 \stackrel{e_3}{\longrightarrow} S_3 \stackrel{e_4}{\longrightarrow} X_1

We will assume that the boundary species `X_o` and `X_1` are fixed n order to sustain sa steady-state. At steady-state there 
will be a pathway flux, `J` and steady-state level of metabolites. 

Let us now imgine we increase the level of enzyme `e_2` by an amount `\delta e_2`. This wil cause the steady-state to change resulting in changes in `J` 
and metabolites `S_1, S_2`, and `S_3`. If we assume these changde by `\delta J`, `\delta S_1, \delta S_2`, and `\delta S_3`.

We can assess the influence by the pertubtion in `e_2` had by looking at the ratio. For example the effect on the flux can be written as:

.. math:: \frac{\delta J}{\delta e_2} 

This ratio has units. For convenince we can eliminate the units by multiplying and dividing by `e_2` and `J` to give us a unit-less measure of influence:
 
.. math:: \frac{\delta J}{\delta e_2} \frac{e_2}{J} 

This can be reexpressed in the following form:

.. math:: \frac{\delta J}{J} / \frac{\delta e_2}{e_2}

This can now be seen as a ratio of relative changes. In general, the relationship between changes in enzyme and say a flux is non-linear. This means that the ratio will
depend on the size of the perturbation in `\delta e_2`. To remidie this, we can reduce the size of perturbation such that in the limit, we obtain a ratio of differentials
independent of the size of the perturbation. We call this ratio the flux control coefficient, `C^J_{e_2}`:

.. math :: C^J_{e_2} = \frac{d J}{d e_2} \frac{e_2}{J}

A similar kind of measurement can be made with respect to the metabolite levels such that we can define concentraton control coefficients, one for each metabolite:

.. math:: C^{s_1}_{e_2} = \frac{d s_1}{d e_2} \frac{e_2}{s_1},\quad  C^{s_2}_{e_2} = \frac{d s_2}{d e_2} \frac{e_2}{s_2},\quad  C^{s_2}_{e_2} = \frac{d s_2}{d e_2} \frac{e_2}{s_2}

Given that there are four enzymes there will in total be twelve concentraton control coeffiicients.

However since there thereis only a single flux since all step carries the same flux, there will only be four flux control coefficients. 



.. math::

   C^s_e = \frac{\partial s}{\partial e} \frac{e}{s}

.. note::

   This function is not suitable for sending spam e-mails.

.. warning::

   This function is not suitable for sending spam e-mails.



