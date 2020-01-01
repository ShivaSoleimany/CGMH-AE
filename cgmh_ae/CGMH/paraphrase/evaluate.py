from hope.probabilistic_nlg.utils import calculate_bleu_scores, calculate_ngram_diversity, calculate_entropy
from hope.probabilistic_nlg.evaluate_latent_space import get_avg_sent_lengths

from pathlib import Path

files = {
    "ref": './output/ref.txt',
    "par": './output/par.txt',
    "cgmh": './output/CGMH/output.txt100',
    "vae": './output/VAE/output.txt100',
    "wae_det": './output/WAE-DET/output.txt100',
    "wae_st": './output/WAE-ST/output.txt100',
}

for filename in files:
    files[filename] = open(files[filename]).read()