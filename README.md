# Determination of Ibuprofen and Biphenyl Solubility from Peng Robinson Equation of State (PR EoS) and  van der Waals (vdW) Mixing Parameters 

## Introduction

Recently, the applications of supercritical fluids (SCF) as a substitution of organic solvents in several conventional reaction, extraction and crystallization processes have gained attention due to the advantages which it may address in the controlability of the system. SCFs exist in a supercritical state, the state where temperature and pressure are above a critical point. Beyond the critical point, SCFs begin to demonstrate properties of a combined liquid and gaseous state which can have diffusion rates close to gases and liquid-like densities allowing applications as reaction and seperation mediums. Furthermore, minor changes in temperatures and pressures around the critical point can provide a great controllability for the processes. Hereby, the properties such as density and solubility can be modulated with small changes in the process conditions and in this manner, a solute which is dissolved in a SCF can be easily precipitated reducing the pressure as the SCF is transitioning to the gas phase. The gas can be conveniently recycled for repeated use [[1]](#1).

## Solubility Calculations

In this repository, solubility of the organic compounds of ibubrofen and biphenyl in the supercritical CO<sub>2</sub> were determined using PR-EoS and vdW mixing rules. 

Solubility of the organic compunds are derived from the equation:


<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=%5Cdisplaystyle%20y_%7Bsolubility%7D%20%3D%20%5Cfrac%7By_%7Bideal%7D%20e%5E%7B%5Cfrac%7Bv_%7Bsol%7D%20%5Cleft%28P%20-%20P_%7Bsub%7D%5Cright%29%7D%7BR%7D%7D%7D%7B%5Cphi_%7Bscf%7D%7D&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="\displaystyle y_{solubility} = \frac{y_{ideal} e^{\frac{v_{sol} \left(P - P_{sub}\right)}{R}}}{\phi_{scf}}" width="310" height="81" /></p>

In the equation above, T is the equilibrium temperature, P the equilibrium pressure, v<sub>sol</sub> the pure solid molar volume of the solute, Φ<sub>scf</sub> 
the fugacity coefficient of the pure solid in the supercritical phase which can be obtained from the following equation. 


<p align="center"><img src="https://bit.ly/3xlxsbL" align="center" border="0" alt="\displaystyle \ln{\left(\phi_{scf} \right)} = -\ln{\left(Z \right)} -\int_{V}^{\infty} \left( \frac{dP}{dn_i} - \frac{1}{V}\right)\, dV" width="404" height="58" /></p>

The thermodynamic relation of  the Φ<sub>scf</sub> was calculated using the combined PR EoS and vdW mixing rules in `fugacity_coeff.py` and the final form can derived as below.

<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=%5Cdisplaystyle%20-%20%5Cln%7B%5Cleft%28-%20%5Cfrac%7BP%20b%7D%7BR%20T%7D%20%2B%20Z_%7B1%7D%20%5Cright%29%7D%20%2B%20%5Cfrac%7Bb_%7Bs%7D%20%5Cleft%28Z_%7B1%7D%20-%201%5Cright%29%7D%7Bb%7D%20-%20%5Cfrac%7B%5Csqrt%7B2%7D%20a%20%5Cleft%28-%20%5Cfrac%7Bb_%7Bs%7D%7D%7Bb%7D%20%2B%20%5Cfrac%7Ba_%7Bs%7D%7D%7Ba%7D%5Cright%29%20%5Cln%7B%5Cleft%28%5Cfrac%7B%5Cfrac%7BP%20b%20%5Cleft%281%20%2B%20%5Csqrt%7B2%7D%5Cright%29%7D%7BR%20T%7D%20%2B%20Z_%7B1%7D%7D%7B%5Cfrac%7BP%20b%20%5Cleft%281%20-%20%5Csqrt%7B2%7D%5Cright%29%7D%7BR%20T%7D%20%2B%20Z_%7B1%7D%7D%20%5Cright%29%7D%7D%7B4%20R%20T%20b%7D&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="\displaystyle - \ln{\left(- \frac{P b}{R T} + Z_{1} \right)} + \frac{b_{s} \left(Z_{1} - 1\right)}{b} - \frac{\sqrt{2} a \left(- \frac{b_{s}}{b} + \frac{a_{s}}{a}\right) \ln{\left(\frac{\frac{P b \left(1 + \sqrt{2}\right)}{R T} + Z_{1}}{\frac{P b \left(1 - \sqrt{2}\right)}{R T} + Z_{1}} \right)}}{4 R T b}" width="635" height="104" /></p>



In the equation, the parameters, a in the attractive term and the parameter b in the repulsive term coming from PR EoS are replaced by the parameters, a<sub>mix</sub> and b<sub>mix</sub> in vdW mixing rules. All needed functions to calculate these parameters are available in `mixing_parameter.py`.

<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=a_%7Bmix%7D%20%3D%20%5Cdisplaystyle%20%5Csum_%7B%5Csubstack%7B0%20%5Cleq%20j%20%5Cleq%201%5C%5C0%20%5Cleq%20i%20%5Cleq%201%7D%7D%20%7Ba%7D_%7B%5Cleft%28%20i%2C%20%5C%20%20j%5Cright%29%7D%20%7By%7D_%7Bi%7D%20%7By%7D_%7Bj%7D&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="a_{mix} = \displaystyle \sum_{\substack{0 \leq j \leq 1\\0 \leq i \leq 1}} {a}_{\left( i, \  j\right)} {y}_{i} {y}_{j}" width="237" height="69" /></p>

<p align="center"><img src="https://bit.ly/3E52oOM" align="center" border="0" alt="{a}_{i,j} =  \left(\sqrt{a_{i} a_{j}} \left(1 - {k}_{i,j}\right)" width="235" height="35" /></p>

<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=%7Bb%7D_%7Bmix%7D%20%3D%20%20%5Cdisplaystyle%20%5Csum_%7B%5Csubstack%7B0%20%5Cleq%20j%20%5Cleq%201%5C%5C0%20%5Cleq%20i%20%5Cleq%201%7D%7D%20%7Bb%7D_%7B%5Cleft%28%20i%2C%20%5C%20%20j%5Cright%29%7D%20%7By%7D_%7Bi%7D%20%7By%7D_%7Bj%7D&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="{b}_{mix} =  \displaystyle \sum_{\substack{0 \leq j \leq 1\\0 \leq i \leq 1}} {b}_{\left( i, \  j\right)} {y}_{i} {y}_{j}" width="235" height="69" /></p>

<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=%7Bb%7D_%7Bi%2Cj%7D%20%3D%20%20%5Cleft%280.5%20-%200.5%20%7Bl%7D_%7Bi%2Cj%7D%5Cright%29%20%5Cleft%28b_%7Bi%7D%20%2B%20b_%7Bj%7D%5Cright%29&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="{b}_{i,j} =  \left(0.5 - 0.5 {l}_{i,j}\right) \left(b_{i} + b_{j}\right)" width="285" height="33" /></p>

In the equations, a<sub>i</sub>, a<sub>j</sub>, b<sub>i</sub>, b<sub>j</sub> are calculated according to PRK EoS for each component. Also, binary interaction parameters of k and l can be found fitting an experimental equilibrium data to PR EoS. More detailed derivations of these paramaters could be found in the book of "Introduction to Supercritical Fluids A Spreadsheet-based Approach" [[3]](#3). 

In this repo, the binary interaction parameters for ibuprofen and CO<sub>2</sub>, k and l, were calculated by the minimization of Average Absolute Relative Deviation, AARD(%) using the solubility from the study of "Measurement and Correlation of Ibuprofen in Supercritical Carbon Dioxide Using Stryjek and Vera EOS" [[4]](#4). The calculation of the binary parameters interaction parameters by the optimization of AARD(%) can be found in `binary_interaction_parameters_ibuprofen.ipynb`.

<p align="center"><img src="http://www.sciweavers.org/tex2img.php?eq=%7BAARD%7D%20%3D%20%20%5Cdisplaystyle%20%5Cfrac%7B100%20%5Csum_%7Bi%3D1%7D%5E%7BN%7D%20%5Cfrac%7B%5Cleft%7C%7B%7By_%7Bcal%7D%7D_%7Bi%7D%20-%20%7By_%7Bexp%7D%7D_%7Bi%7D%7D%5Cright%7C%7D%7B%7By_%7Bexp%7D%7D_%7Bi%7D%7D%7D%7BN%7D&bc=White&fc=Black&im=jpg&fs=18&ff=fourier&edit=0" align="center" border="0" alt="{AARD} =  \displaystyle \frac{100 \sum_{i=1}^{N} \frac{\left|{{y_{cal}}_{i} - {y_{exp}}_{i}}\right|}{{y_{exp}}_{i}}}{N}" width="302" height="77" /></p>

## References
<a id="3">[3]</a> 
Richard Smith, Hiroshi Inomata, Cor Peters,
Chapter 6 - Equations of State and Formulations for Mixtures,
Editor(s): Richard Smith, Hiroshi Inomata, Cor Peters,
Supercritical Fluid Science and Technology,
Elsevier,
Volume 4,
2013,
Pages 333-480,
ISSN 2212-0505,
ISBN 9780444522153,
https://doi.org/10.1016/B978-0-444-52215-3.00006-4.
(https://www.sciencedirect.com/science/article/pii/B9780444522153000064)
</br></br><a id="4">[4]</a> 
"Measurement and Correlation of Ibuprofen in Supercritical Carbon Dioxide Using Stryjek and Vera EOS". Iranian Journal of Chemical Engineering(IJChE), 7, 4, 2010, 42-49.
