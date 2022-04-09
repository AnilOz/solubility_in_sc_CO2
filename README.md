## Determination of Ibuprofen and Biphenyl Solubility from Peng Robinson Equation of State (PR EoS) and  van der Waals (vdW) Mixing Parameters  

In this repository, solubility of the organic compounds of ibubrofen and biphenyl in the supercritical CO<sub>2</sub> were determined using PR-EoS and vdW mixing rules. 

Solubility of the organic compunds are derived from the equation:


<p align="center"><img src="https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\bg{white}\displaystyle&space;y_{solubility}&space;=&space;\frac{y_{ideal}&space;e^{\frac{v_{sol}&space;\left(P&space;-&space;P_{sub}\right)}{R}}}{\phi_{scf}}" title="https://latex.codecogs.com/svg.image?\inline \LARGE \bg{white}\displaystyle y_{solubility} = \frac{y_{ideal} e^{\frac{v_{sol} \left(P - P_{sub}\right)}{R}}}{\phi_{scf}}" /></p>

In the equation above, T is the equilibrium temperature, P the equilibrium pressure, v<sub>sol</sub> the pure solid molar volume of the solute, Φ<sub>scf</sub> 
the fugacity coefficient of the pure solid in the supercritical phase which can be obtained from the following equation. 


<p align="center"><img src="https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\bg{white}\displaystyle&space;\ln{\left(\phi_{scf}&space;\right)}&space;=&space;-\ln{\left(Z&space;\right)}&space;-\int_{V}^{\infty}&space;\left(&space;\frac{dP}{dn_i}&space;-&space;\frac{1}{V}\right)\,&space;dV" title="https://latex.codecogs.com/svg.image?\inline \LARGE \bg{white}\displaystyle \ln{\left(\phi_{scf} \right)} = -\ln{\left(Z \right)} -\int_{V}^{\infty} \left( \frac{dP}{dn_i} - \frac{1}{V}\right)\, dV" /></p>

The thermodynamic relation of  the Φ<sub>scf</sub> was calculated using the combined PR EoS and vdW mixing rules and the final form was written below. 

<p align="center"><img src="https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\bg{white}\displaystyle&space;-&space;\ln{\left(-&space;\frac{P&space;b}{R&space;T}&space;&plus;&space;Z_{1}&space;\right)}&space;&plus;&space;\frac{b_{s}&space;\left(Z_{1}&space;-&space;1\right)}{b}&space;-&space;\frac{\sqrt{2}&space;a&space;\left(-&space;\frac{b_{s}}{b}&space;&plus;&space;\frac{a_{s}}{a}\right)&space;\ln{\left(\frac{\frac{P&space;b&space;\left(1&space;&plus;&space;\sqrt{2}\right)}{R&space;T}&space;&plus;&space;Z_{1}}{\frac{P&space;b&space;\left(1&space;-&space;\sqrt{2}\right)}{R&space;T}&space;&plus;&space;Z_{1}}&space;\right)}}{4&space;R&space;T&space;b}" title="https://latex.codecogs.com/svg.image?\inline \LARGE \bg{white}\displaystyle - \ln{\left(- \frac{P b}{R T} + Z_{1} \right)} + \frac{b_{s} \left(Z_{1} - 1\right)}{b} - \frac{\sqrt{2} a \left(- \frac{b_{s}}{b} + \frac{a_{s}}{a}\right) \ln{\left(\frac{\frac{P b \left(1 + \sqrt{2}\right)}{R T} + Z_{1}}{\frac{P b \left(1 - \sqrt{2}\right)}{R T} + Z_{1}} \right)}}{4 R T b}" /></p>


