# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:41:33 2024

@author: TANMAY
"""


def is_vowel(ch):
    return ch in 'aeiouAEIOU'

def edit_distance_bottom_up(seqA, seqB, gap_penalty, low_mismatch_cost, high_mismatch_cost, regular_mismatch_cost):
    n = len(seqA)
    m = len(seqB)

    # Create a DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # DP table of size (n+1) x (m+1)

    # Initialize the first row and column
    for i in range(1, n + 1):
        dp[i][0] = i * gap_penalty  # Cost of deleting all characters from seqA
    for j in range(1, m + 1):
        dp[0][j] = j * gap_penalty  # Cost of inserting all characters into seqA

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Determine the mismatch cost based on whether the characters are vowels or consonants
            if seqA[i - 1] == seqB[j - 1]:
                substitution = 0  # No cost for matching
            else:
                # If one is a vowel and the other is a consonant
                if is_vowel(seqA[i - 1]) and is_vowel(seqB[j - 1]):
                    substitution = low_mismatch_cost  # Vowel to Vowel mismatch
                elif is_vowel(seqA[i - 1]) != is_vowel(seqB[j - 1]):
                    substitution = high_mismatch_cost  # Vowel to Consonant or Consonant to Vowel mismatch
                else:
                    substitution = regular_mismatch_cost  # Consonant to Consonant mismatch

            dp[i][j] = min(
                dp[i - 1][j] + gap_penalty,         # Deletion
                dp[i][j - 1] + gap_penalty,         # Insertion
                dp[i - 1][j - 1] + substitution     # Substitution
            )

    return dp, dp[n][m]

def print_dp_table(dp):
    """Function to print the DP table."""
    for row in dp:
        print("\t".join(map(str, row)))


# Taking user input for sequences and penalties
seqA = input("Enter the first sequence (string): ")
seqB = input("Enter the second sequence (string): ")
gap_penalty = int(input("Enter the gap penalty: "))
low_mismatch_cost = int(input("Enter the low mismatch cost (vowel-to-vowel): "))
high_mismatch_cost = int(input("Enter the high mismatch cost (vowel-to-consonant or consonant-to-vowel): "))
regular_mismatch_cost = int(input("Enter the regular mismatch cost (consonant-to-consonant): "))

# Performing edit distance calculation using Bottom-Up approach
dp_table_bottom_up, optimal_score_bottom_up = edit_distance_bottom_up(
    seqA, seqB, gap_penalty, low_mismatch_cost, high_mismatch_cost, regular_mismatch_cost
)

# Printing the results
print("\nDynamic Programming Table (Bottom-Up Approach):")
print_dp_table(dp_table_bottom_up)
print("\nOptimal Edit Distance (Bottom-Up Approach):", optimal_score_bottom_up)



# def edit_distance_bottom_up(seqA, seqB, gap_penalty, substitution_cost):
#     n = len(seqA)
#     m = len(seqB)

#     # Create a DP table
#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     # Initialize the first row and column
#     for i in range(1, n + 1):
#         dp[i][0] = i * gap_penalty  # Cost of deleting all characters from seqA
#     for j in range(1, m + 1):
#         dp[0][j] = j * gap_penalty  # Cost of inserting all characters into seqA

#     # Fill the DP table
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if seqA[i - 1] == seqB[j - 1]:
#                 substitution = 0  # No cost for matching
#             else:
#                 substitution = substitution_cost  # Cost for substitution

#             dp[i][j] = min(
#                 dp[i - 1][j] + gap_penalty,
#                 dp[i][j - 1] + gap_penalty,         
#                 dp[i - 1][j - 1] + substitution      
#             )

#     return dp, dp[n][m]

# # def edit_distance_top_down(seqA, seqB, gap_penalty, substitution_cost):
# #     n = len(seqA)
# #     m = len(seqB)
# #     dp = [[-1] * (m + 1) for _ in range(n + 1)]  # Memoization table

# #     def top_down(i, j):
# #         if dp[i][j] != -1:  # Return cached value if it exists
# #             return dp[i][j]
# #         if i == 0:  # Only seqB remains
# #             dp[i][j] = j * gap_penalty
# #         elif j == 0:  # Only seqA remains
# #             dp[i][j] = i * gap_penalty
# #         else:
# #             if seqA[i - 1] == seqB[j - 1]:
# #                 substitution = 0  # No cost for matching
# #             else:
# #                 substitution = substitution_cost

# #             dp[i][j] = min(
# #                 top_down(i - 1, j) + gap_penalty,         # Deletion
# #                 top_down(i, j - 1) + gap_penalty,         # Insertion
# #                 top_down(i - 1, j - 1) + substitution      # Substitution
# #             )
# #         return dp[i][j]

# #     optimal_score = top_down(n, m)
# #     return dp, optimal_score

# def print_dp_table(dp):
#     for row in dp:
#         print("\t".join(map(str, row)))

# # Taking user input for sequences and penalties
# seqA = input("Enter the first sequence (string): ")
# seqB = input("Enter the second sequence (string): ")
# gap_penalty = int(input("Enter the gap penalty: "))
# substitution_cost = int(input("Enter the mismatch cost: "))

# # Performing edit distance calculation using Bottom-Up approach
# dp_table_bottom_up, optimal_score_bottom_up = edit_distance_bottom_up(seqA, seqB, gap_penalty, substitution_cost)

# # Performing edit distance calculation using Top-Down approach
# #dp_table_top_down, optimal_score_top_down = edit_distance_top_down(seqA, seqB, gap_penalty, substitution_cost)

# # Printing the results for Bottom-Up approach
# print("\nDynamic Programming Table (Bottom-Up Approach):")
# print_dp_table(dp_table_bottom_up)
# print("\nOptimal Edit Distance (Bottom-Up Approach):", optimal_score_bottom_up)

# # # Printing the results for Top-Down approach
# # print("\nDynamic Programming Table (Top-Down Approach):")
# # print_dp_table(dp_table_top_down)
# # print("\nOptimal Edit Distance (Top-Down Approach):", optimal_score_top_down)
