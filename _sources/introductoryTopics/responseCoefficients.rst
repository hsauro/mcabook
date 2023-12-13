.. default-role:: math 

Response Coefficients
=====================

In any system we choose to study there will be qunatities which we can measure and other quantities which we can change.

In a metabolite pathway the kinds of qunatiies we can measure include the pathwy flux and the pathwya metabolite concentations. 
If the pathwya understudy is sigaling network or a gen resulatory network we migth instead meaure the
levels of transcription factor or the levels of certian phosporylatde proteins. 

We will call these measurable quantities **variables** or the **dependent variables**.  

In constrast there are also **independent variables** which we will call **parameters** which expermentalist can directly control. 

Examples of parameters include any environmental condition, this includes externally applied 
inhibitors or drug molecules, and parmaeters internal to a cell such as the levels of enzyme expression. 

One of the core ideas in MCA is meauring how much a variable such as a flux, metabolite or 
protein (if its a signaling network) is influenced by a parmaeter such as an inhibitor.

Measuring Influence
-------------------

When we talk about influence we are primarly going to consider how a given parameter
influences the steady-state. Therefore, in all subsequent discussions we will be assuming our pathway
is at steady-state.

Imagine a simple metabolite pathway such as the one below is at ateady-state:

.. math:: X_o \stackrel{e_1}{\longrightarrow} S_1 \stackrel{e_2}{\longrightarrow} S_2 \stackrel{e_3}{\longrightarrow} S_3 \stackrel{e_4}{\longrightarrow} X_1

We will assume that the boundary species `X_o` and `X_1` are fixed n order to sustain a steady-state. At steady-state there 
will be a pathway flux, `J` and steady-state level of three metabolites, `S_1, S_2` and `S_3`. We will also asusme ther is an inhibitor
called `I` that inhibites the second enzymes `E_2`. To guage how much influence the inhibior has on the pathwya, we can pick a dependent
variable to measure, for example `S_3`.

With the pathway at steady-state, let us make a small change to the inhibitor by an amount `\delta I`.
As a rsult the system is no longer in steady-state and will start to change and move to a new 
steady-state with a new flux and new concentsations for the metabolites. 

Let's say the concentation of `S_3` has changed by `\delta s_3`. We could estimate the influence the inhiitor has on `S_3` 
by taking the ratio:

.. math:: \frac{\delta s_3}{\delta I}

This ratio however has units. For convenince we can eliminate the units by multiplying and dividing by 
`I` and `s_3` to give us a unit-less measure of influence:
 
.. math:: \frac{\delta s_3}{\delta I} \frac{I}{s_3} 

This can be reexpressed in the following form:

.. math:: \frac{\delta s_3}{s_3} / \frac{\delta I}{I}

This can now be seen as a ratio of relative changes. In general, the relationship between changes in enzyme and say a flux is non-linear. 
This means that the ratio will depend on the size of the perturbation in `\delta I`. To remidie this, we can 
reduce the size of perturbation such that in the limit, we obtain a ratio of differentials
independent of the size of the perturbation. We call this ratio the response coefficient, `R^{s_3}_{I}`:

.. math :: R^{s_3}_{I} = \frac{d s_3}{d I} \frac{I}{J}

This form can still be interpreted, at least aproximately, as a ratio of percentage changes.

.. admonition:: Definition

   The Flux Response Coefficient:
   
   .. math:: R^J_I = \frac{dJ}{dI} \frac{I}{J} \approx \frac{J\%}{I\%}

.. admonition:: Definition

  The Concentration Response Coefficient:
   
  .. math:: R^s_I = \frac{ds}{dI} \frac{I}{s}  \approx \frac{J\%}{I\%}

**Example**

When the concentration of a drug is increased from 2 mM to 2.5 mM, the cocentration
of a given metabolite changes its steady-state level from 15 mM to 18 mM. Estimate
the response cofficient. 

Since the percentage change in the metabolite is (18-15)/18 and the percntage change in drug is 
(2.5-2.0)/2, then the response coefficient is estimated to be:

.. math:: R = ((18-15)/18)/(2.5-2.0)/2 = 0.66667

This means that a 1\% change in the drug concentration will lead to a 0.66667\% change in the metabolite.

If a given pathway has `m` metabolites then it means there will be `m` response coefficients 
with respect to a given external factor.




