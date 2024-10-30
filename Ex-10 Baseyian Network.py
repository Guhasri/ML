# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:11:15 2024

@author: Admin
"""


P_Alarm1 = 0.1
P_Alarm2 = 0.2
P_Burglary_given_Alarm1_Alarm2 = 0.8
P_Burglary_given_Alarm1_not_Alarm2 = 0.7
P_Burglary_given_not_Alarm1_Alarm2 = 0.6
P_Burglary_given_not_Alarm1_not_Alarm2 = 0.5


P_Burglary_given_Alarm1 = (P_Burglary_given_Alarm1_Alarm2 * P_Alarm2) + \
                          (P_Burglary_given_Alarm1_not_Alarm2 * (1 - P_Alarm2))

    
P_Burglary_given_Alarm1 = (P_Burglary_given_Alarm1_Alarm2 * P_Alarm2) + (P_Burglary_given_Alarm1_not_Alarm2 * (1 - P_Alarm2))


P_Alarm2_given_Burglary_Alarm1 = (P_Burglary_given_Alarm1_Alarm2 * P_Alarm2) / P_Burglary_given_Alarm1

# Print the result
print(f"P(Alarm2 | Burglary, Alarm1) = {P_Alarm2_given_Burglary_Alarm1:.4f}")