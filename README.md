# Determination of Ibuprofen and Biphenyl Solubility from Peng Robinson Equation of State (PR EoS) and  van der Waals (vdW) Mixing Parameters 

## Introduction

Recently, the applications of supercritical fluids (SCF) as a substitution of organic solvents in several conventional reaction, extraction and crystallization processes have gained attention due to the advantages which it may address in the controlability of the system. SCFs exist in a supercritical state, the state where temperature and pressure are above a critical point. Beyond the critical point, SCFs begin to demonstrate properties of a combined liquid and gaseous state which can have diffusion rates close to gases and liquid-like densities allowing applications as reaction and seperation mediums. Furthermore, minor changes in temperatures and pressures around the critical point can provide a great controllability for the processes. Hereby, the properties such as density and solubility can be modulated with small changes in the process conditions and in this manner, a solute which is dissolved in a SCF can be easily precipitated reducing the pressure as the SCF is transitioning to the gas phase. The gas can be conveniently recycled for repeated use [[1]](#1).

One of the applications where SCFs stands forward is the particle design of pharmaceutical compunds. A great proportion of the pharmaceutical compunds in solid form has poor water solubility. So, in order to increase the solubility of the pharmaceutical ingredient for the ease of drug absorbtion, the size of the pharmaceutical compund is usually reduced by several **micronization** techniques such as crushing, milling recrytallization, spray drying etc. Mechanical aproaches like crushing and milling are generally undesirable since they induce the heat formation which may degrade the compounds. Also, in the recrystallization, the use of organic solvents and anti-solvents can be costly and the residues of solvent on the pharmaceutical compunds can be toxic [[2]](#2). Hence, lately, the novel and green techniques, which SCFs are employed, such as **Rapid Expansion of Supercritical Solution (RESS)**, **Supercritical Anti-Solvent (SAS)** and **Gas Anti-Solvent (GAS)** have come to fore (See [[3]](#3) for more detail). These new methods are also favorable since the supercritical solvent can be easily recovered for using repeatedly minor modulation. Moreover, since the solvent can be recovered in differen phase, the risk of toxic residue remaining on the drug compound is avoided.

In most of the processes which include SCFs, CO<sub>2</sub> is preferred as supercritical fluid since its intoxicity and mild critical point conditions which favors processes that contains heat sensitive materials. Hence, in this repo, CO<sub>2</sub> is employed as scf for the solubility calculations as well.

## Dependencies
- sympy
- numpy
- pandas
- scipy
- matplotlib
- openpyxl


## Solubility Calculations

In this repository, solubility of the organic compounds of ibubrofen and biphenyl in the supercritical CO<sub>2</sub> were determined using PR-EoS and vdW mixing rules. 

Solubility of the organic compounds are derived from the equation:


<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}\displaystyle&space;y_{solubility}&space;=&space;\frac{y_{ideal}&space;e^{\frac{v_{sol}&space;\left(P&space;-&space;P_{sub}\right)}{R}}}{\phi_{scf}}" /></p>

In the equation above, T is the equilibrium temperature, P the equilibrium pressure, v<sub>sol</sub> the pure solid molar volume of the solute, Φ<sub>scf</sub> 
the fugacity coefficient of the pure solid in the supercritical phase which can be obtained from the following equation. 


<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}&space;\displaystyle&space;\ln{\left(\phi_{scf}&space;\right)}&space;=&space;-\ln{\left(Z&space;\right)}&space;-\int_{V}^{\infty}&space;\left(&space;\frac{dP}{dn_i}&space;-&space;\frac{1}{V}\right)\,&space;dV&space;" /></p>

The thermodynamic relation of  the Φ<sub>scf</sub> was calculated using the combined PR EoS and vdW mixing rules in `fugacity_coeff.py` and the final form can derived as below.

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}\displaystyle&space;-&space;\ln{\left(-&space;\frac{P&space;b}{R&space;T}&space;&plus;&space;Z_{1}&space;\right)}&space;&plus;&space;\frac{b_{s}&space;\left(Z_{1}&space;-&space;1\right)}{b}&space;-&space;\frac{\sqrt{2}&space;a&space;\left(-&space;\frac{b_{s}}{b}&space;&plus;&space;\frac{a_{s}}{a}\right)&space;\ln{\left(\frac{\frac{P&space;b&space;\left(1&space;&plus;&space;\sqrt{2}\right)}{R&space;T}&space;&plus;&space;Z_{1}}{\frac{P&space;b&space;\left(1&space;-&space;\sqrt{2}\right)}{R&space;T}&space;&plus;&space;Z_{1}}&space;\right)}}{4&space;R&space;T&space;b}" /></p>



In the equation, the parameters, a in the attractive term and the parameter b in the repulsive term coming from PR EoS are replaced by the parameters, a<sub>mix</sub> and b<sub>mix</sub> in vdW mixing rules. All needed functions to calculate these parameters are available in `mixing_parameter.py`.

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}a_{mix}&space;=&space;\displaystyle&space;\sum_{\substack{0&space;\leq&space;j&space;\leq&space;1\\0&space;\leq&space;i&space;\leq&space;1}}&space;{a}_{\left(&space;i,&space;\&space;j\right)}&space;{y}_{i}&space;{y}_{j}" /></p>

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}a_{mix}&space;=&space;&space;\sqrt{a_{i}&space;a_{j}}&space;\left(1&space;-&space;{k}_{i,j}\right)" /></p>

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}{b}_{mix}&space;=&space;\displaystyle&space;\sum_{\substack{0&space;\leq&space;j&space;\leq&space;1\\0&space;\leq&space;i&space;\leq&space;1}}&space;{b}_{\left(&space;i,&space;\&space;j\right)}&space;{y}_{i}&space;{y}_{j}" /></p>

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}{b}_{i,j}&space;=&space;\left(0.5&space;-&space;0.5&space;{l}_{i,j}\right)&space;\left(b_{i}&space;&plus;&space;b_{j}\right)" /></p>

In the equations, a<sub>i</sub>, a<sub>j</sub>, b<sub>i</sub>, b<sub>j</sub> are calculated according to PRK EoS for each component. Also, binary interaction parameters of k and l can be found fitting an experimental equilibrium data to PR EoS. More detailed derivations of these paramaters could be found in the book of "Introduction to Supercritical Fluids A Spreadsheet-based Approach" [[4]](#4). 

In this repo, the binary interaction parameters for ibuprofen and CO<sub>2</sub>, k and l, were calculated by the minimization of Average Absolute Relative Deviation, AARD(%) using the solubility from the study of "Measurement and Correlation of Ibuprofen in Supercritical Carbon Dioxide Using Stryjek and Vera EOS" [[5]](#5). The calculation of the binary parameters interaction parameters by the optimization of AARD(%) can be found in `binary_interaction_parameters_ibuprofen.ipynb`.

<p align="center"><img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\bg{white}\color{Black}{AARD}&space;=&space;\displaystyle&space;\frac{100&space;\sum_{i=1}^{N}&space;\frac{\left|{{y_{cal}}_{i}&space;-&space;{y_{exp}}_{i}}\right|}{{y_{exp}}_{i}}}{N}" /></p>

## Results

- Ibuprofen solubility was studied at 40°C and in a pressure range of 0.1 - 13 MPa in `Ibuprofen_Solubility_in_scCO2.ipynb`

<p align="center"><img src="https://github.com/AnilOz/solubility_in_sc_CO2/blob/master/Figures/y_ibu.png" /></p>
 
- Biphenyl solubility in scCO2 was studied at 40°C and in a pressure range of 0.1 - 20 in  `Biphenyl_Solubility_in_scCO2_with_Cosolvent_Toluene.ipynb`.
<p align="center"><img src="https://github.com/AnilOz/solubility_in_sc_CO2/blob/master/Figures/y_biphenyl_tol.png" /></p>

- Also, the solubility of biphenyl was investigated in the presence of 3% toluene to see the effects of cosolvent in the solubility.
<p align="center"><img src="https://github.com/AnilOz/solubility_in_sc_CO2/blob/master/Figures/y_biphenyl_2.png" /></p>

## References
<a id="1">[1]</a> 
Noor U Din Reshi, Masood Ahmad Rizvi, Syed Kazim Moosvi, Mudasir Ahmad, Adil Gani,
Chapter 16 - Solubility of organic compounds in scCO2,
Editor(s):  Inamuddin, Abdullah M. Asiri, Arun M. Isloor,
Green Sustainable Process for Chemical and Environmental Engineering and Science,
Elsevier,
2020,
Pages 379-411,
ISBN 9780128173886,
https://doi.org/10.1016/B978-0-12-817388-6.00016-7.
(https://www.sciencedirect.com/science/article/pii/B9780128173886000167)
</br></br><a id="2">[2]</a> 
Hamidreza Bagheri, G. Ali Mansoori, Hassan Hashemipour,
A novel approach to predict drugs solubility in supercritical solvents for RESS process using various cubic EoS-mixing rule,
Journal of Molecular Liquids,
Volume 261,
2018,
Pages 174-188,
ISSN 0167-7322,
https://doi.org/10.1016/j.molliq.2018.03.081.
(https://www.sciencedirect.com/science/article/pii/S0167732218311164)
</br></br><a id="3">[3]</a> 
Mojhdeh Baghbanbashi, Naghmeh Hadidi, Gholamreza Pazuki,
Chapter 10 - Solubility of pharmaceutical compounds in supercritical carbon dioxide: Application, experimental, and mathematical modeling,
Editor(s):  Inamuddin, Abdullah M. Asiri, Arun M. Isloor,
Green Sustainable Process for Chemical and Environmental Engineering and Science,
Elsevier,
2020,
Pages 185-254,
ISBN 9780128173886,
https://doi.org/10.1016/B978-0-12-817388-6.00010-6.
(https://www.sciencedirect.com/science/article/pii/B9780128173886000106)
</br></br>
<a id="4">[4]</a> 
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
</br></br>
<a id="5">[5]</a> 
"Measurement and Correlation of Ibuprofen in Supercritical Carbon Dioxide Using Stryjek and Vera EOS". Iranian Journal of Chemical Engineering(IJChE), 7, 4, 2010, 42-49.
