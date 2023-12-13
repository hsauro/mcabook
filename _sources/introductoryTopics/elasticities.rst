.. default-role:: math 

Elasticities
============

Another way to study a biochemical pathway is to look at the individual steps. This
has often been the domain of enzyme kineticists. For example, give the pathway shown 
below:

.. math:: X_o \stackrel{v_1}{\longrightarrow} S_1 \stackrel{v_2}{\longrightarrow} S_2 \stackrel{v_3}{\longrightarrow} X_1

we could extract the second step and study it in isolation away from the rest of the pathway:

.. math:: S_1 \stackrel{v_2}{\longrightarrow} S_2

One way to study this reaction is to look at how the reaction rate `v_2` changes
as a function of the substrate `S_1` and product `S_2`. For example, we could change
the substrate by an amount `\delta s_1` and observe the change rate `v_2`. This
would given us an indication how how much `S_1` influences the reaction rate. As
before we can examine the relative change in reaction rate given a relative change
in substrate. We can express this as follows:

.. math::

   \varepsilon^v_s = \frac{\partial v_2}{\partial s_1} \frac{s_1}{v_2}

We call this measure the **elasticity** coefficient. However changes in the 
product can also affect the reaction rate. This means there will also an elastciity
for the product `S_2`:

.. math::

   \varepsilon^v_s = \frac{\partial v_2}{\partial s_2} \frac{s_2}{v_2}
   
In fact, a chemical reaction will have as many elasticities as there are factors
as might infuence the reaction rate. For an enzyme catalyzed reaction, there are 
a number of elasticities to consider other than the substrate(s) and product(s) elasticities.

For example, the reaction rate of an enzyme catlayzed reaction is also affected
by the concentration of enzyme and any regulators of the enzyme.


.. note::

   This function is not suitable for sending spam e-mails.

.. warning::

   This function is not suitable for sending spam e-mails.



