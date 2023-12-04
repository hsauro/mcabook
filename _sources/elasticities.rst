.. default-role:: math 

Elasticities
============

.. math::

   \varepsilon^v_x = \frac{\partial v}{\partial x} \frac{x}{v}

Here is some inline math :math:`\psi(r) = \exp(-2r)`

Here is some inline math `\psi(r) = \exp(-2r)`

Display math

.. math:: \psi(r) = e^{-2r}

A more complex version:

.. math::
   :name: Fourier transform

   (\mathcal{F}f)(y)
    = \frac{1}{\sqrt{2\pi}^{\ n}}
      \int_{\mathbb{R}^n} f(x)\,
      e^{-\mathrm{i} y \cdot x} \,\mathrm{d} x.

.. tikz:: An Example Directive with Caption
   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);
