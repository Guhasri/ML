# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:10:32 2024

@author: Admin
"""

P_C = 0.008
P_not_C = 1 - P_C
P_T_pos_given_C = 0.98
P_T_neg_given_not_C = 0.97
P_T_pos_given_not_C = 1 - P_T_neg_given_not_C

P_T_pos = (P_T_pos_given_C * P_C) + (P_T_pos_given_not_C * P_not_C)
P_C_given_T_pos = (P_T_pos_given_C * P_C) / P_T_pos
print(f"(a) P(C | T+) after first positive test: {P_C_given_T_pos:.3f}")

P_C_prior_after_first_test = P_C_given_T_pos
P_not_C_prior_after_first_test = 1 - P_C_prior_after_first_test

P_T_pos_again = (P_T_pos_given_C * P_C_prior_after_first_test) + (P_T_pos_given_not_C * P_not_C_prior_after_first_test)
P_C_given_T_pos_T_pos = (P_T_pos_given_C * P_C_prior_after_first_test) / P_T_pos_again
print(f"(b) P(C | T+, T+) after second positive test: {P_C_given_T_pos_T_pos:.3f}")
