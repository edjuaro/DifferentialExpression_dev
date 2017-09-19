print("Uno, dos, probando.")
# import matplotlib as mpl
# mpl.use('Agg')
import sys
import os
tasklib_path = os.path.dirname(os.path.realpath(sys.argv[0]))
# sys.path.append(tasklib_path)
sys.path.append(tasklib_path + "/ccal")
import ccal as ccal
from modalities import differential_gene_expression
import pandas as pd

from ccal.mathematics.information import information_coefficient
# print(information_coefficient)
# print(os.listdir(tasklib_path + "/ccal/ccal/match"))
from ccal.match.match.make_match_panel import make_match_panel
# from match.make_match_panel import make_match_panel
# from ccal.match.match.make_summary_match_panel import make_summary_match_panel
# from ccal.match.match.support.support.df import simulate_df
# from ccal.match.match.support.support.s import simulate_s

# n=10
# target = simulate_s(n, index_prefix='Sample ')
# features_continuous = simulate_df(n * 2, n, index_prefix='Feature ', column_prefix='Sample ')
# print(features_continuous)
# match_scores_for_continuous = make_match_panel(
    # target, features_continuous, n_features=3, n_samplings=3, n_permutations=3)

gene_expression = pd.read_table('data/kras_isogenic_vs_imortalized.gct', index_col='Name', skiprows=[0, 1]).drop('Description', 1)
gene_expression = gene_expression.iloc[0:2000]

phenotypes = pd.Series(data=[1, 1, 1, 1, 1, 1, -1, -1, -1, -1])
phenotypes.index = gene_expression.columns
#differential_gene_expression
# phenotypes,
# gene_expression,
# output_filename,
# max_number_of_genes_to_show=20,
# number_of_permutations=10,
# title=None,
# random_seed=RANDOM_SEED

differential_gene_expression(phenotypes=phenotypes, gene_expression=gene_expression, output_filename='test',
                             title="Test")


