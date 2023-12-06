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

.. execute_code::

    a = [1,2,3]
    b = [4,5,6]
    print ('Printing a list: ', a + b)

.. execute_code::
   :hide_code:
   :hide_headers:

   foo = 32
   print ('This will hide the Code and Results text - and foo is %d' % foo)

Running a simulation

.. plot::
   :include-source:

   import tellurium as te
   r = te.loada ('''A -> B; k1*A; k1=0.1; A = 10''')
   m = r.simulate (0, 40, 100)
   r.plot()

