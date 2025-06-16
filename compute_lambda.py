"""
Last update: 16 June 2025

This script calculates the time-window circularity in [1] 
for a fixed set of parameters. The main parameters are the
percentage success (i.e., s), the disassembly time 
(i.e., T_d), and the criticality of the materials 
beta_1 and beta_2 (i.e., c_fb1 and c_fb2) [1].

References:
[1] Zocco, F. and Malvezzi, M., 2025. CIRO7.2: A material 
    network with circularity of -7.2 and
    reinforcement-learning-controlled robotic disassembler.
    arXiv preprint arXiv:2506.11748
[2] Zocco, F., Corti, A. and Malvezzi, M., 2025. CiRL: 
    Open-source environments for reinforcement learning in 
    circular economy and net zero. arXiv 
    preprint arXiv:2505.21536.
[3] Potting, J., Hekkert, M.P., Worrell, E. and Hanemaaijer, 
    A., 2017. Circular economy: Measuring innovation in the 
    product chain. Planbureau voor de Leefomgeving, (2544).
[4] CRM Alliance, 2024, webpage: https://www.crmalliance.eu/
    critical-raw-materials; last access: 16 June 2025.
"""

## Variables:
s = 0.0 # percentage success
T_d = 86400 # disassembly time in seconds
m0_fb1 = 5 # kg
m0_fb2 = 2 # kg

## Parameters:
c_fb1 = 0.1 # between 0 and 1 
c_fb2 = 0.95 # between 0 and 1
m0_bar = c_fb1*m0_fb1 + c_fb2*m0_fb2 
T_t = 3600 # seconds, 1 h
T_r = 2592000 # 1 month, must be T_r > T_t
T_i = 86400 # 1 day
t_2in4 = T_r 
t_f = t_2in4 + T_d + T_r + T_i   


lambda_ = - (2/t_f)*(m0_bar*(t_2in4+T_d+T_t) \
                     + (m0_bar+m0_bar*(1-s/100))*(T_r-T_t) \
                     + 2*m0_bar*T_i)

    

    