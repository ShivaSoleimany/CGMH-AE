from pathlib import Path
import pickle
from .pathsetup import run_path_setup
run_path_setup()

import os
from hope.probabilistic_nlg.snli.vae import gl
gl.isTrain = False

from .model_config import model_argparse
config = model_argparse()

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = config['device']

import tensorflow as tf

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True
sess = tf.Session(config=tf_config)

import numpy as np
import hope.probabilistic_nlg.utils as utils

from hope.probabilistic_nlg.snli.vae.vae import VAEModel
from sklearn.model_selection import train_test_split


np.random.seed(1337)

absolute_path = '/mnt/hope/hope/probabilistic_nlg/snli/vae'

if Path(absolute_path, 'tokenizer.pickle').exists():
    print('[INFO] Loading tokenizer and word_index from pickle file...')
    with Path(absolute_path, 'tokenizer.pickle').open('rb') as handle:
        tokenizer = pickle.load(handle)
    with Path(absolute_path, 'word_index.pickle').open('rb') as handle:
        word_index = pickle.load(handle)
    # with Path(absolute_path, 'x_test.pickle').open('rb') as handle:
    #     x_test = pickle.load(handle)
else:
    snli_data = utils.get_sentences(file_path = config['data'])

    print('[INFO] Number of sentences = {}'.format(len(snli_data)))

    sentences = [s.strip() for s in snli_data]

    np.random.shuffle(sentences)

    print('[INFO] Tokenizing input and output sequences')
    filters = '!"#$%&()*+/:;<=>@[\\]^`{|}~\t\n'
    x, word_index, tokenizer = utils.tokenize_sequence(sentences,
                                                filters,
                                                config['num_tokens'],
                                                config['vocab_size'])

    print('[INFO] Split data into train-validation-test sets')
    x_train, _x_val_test = train_test_split(x, test_size = 0.1, random_state = 10)
    x_val, x_test = train_test_split(_x_val_test, test_size = 0.5, random_state = 10)

    # # dump x_test for next run
    with Path(absolute_path, 'word_index.pickle').open('wb') as handle:
        pickle.dump(word_index, handle)
    with Path(absolute_path, 'tokenizer.pickle').open('wb') as handle:
        pickle.dump(tokenizer, handle)
    with Path(absolute_path, 'x_test.pickle').open('wb') as handle:
        pickle.dump(x_test, handle)

w2v = config['w2v_file']
embeddings_matrix = utils.create_embedding_matrix(word_index,
                                                  config['embedding_size'],
                                                  w2v)

# Re-calculate the vocab size based on the word_idx dictionary
config['vocab_size'] = len(word_index)

#----------------------------------------------------------------#

model = VAEModel(config, 
                    embeddings_matrix,
                    word_index)
#----------------------------------------------------------------#
config['ckpt'] = '/mnt/hope/hope/probabilistic_nlg/snli/vae/models/full_snli_anneal_type_tanh_anneal_till_3000_lambda_0.0_batch_128_optimizer_adam_wdkeepAnnealTill_0.5_num_tokens_20/20.ckpt'
checkpoint = config['ckpt']

session = tf.Session()
session.run(tf.global_variables_initializer())
saver = tf.train.Saver()
saver.restore(session, checkpoint)

# #---------------------Reconstruction-----------------------------#
# print("[INFO] Restoring model parameters ...")

# preds = model.predict(checkpoint, x_test)
# print('-'*100)

# #----------------------------------------------------------------#

# print("[INFO] Generate with test set input ...")
# generated = ''
# for pred in preds[:10]:
#     generated += '\t\t' + ' '.join([model.idx_word[i] for i in pred if i not in [model.pad, model.eos]]) + '\n'
# print(generated)

# print('-'*100)
# #----------------------------------------------------------------#

# print("[INFO] Generate samples from the latent space ...")
# model.random_sample(checkpoint)
# model.random_sample_save(checkpoint, num_batches=782)

# print('-'*100)
# #----------------------------------------------------------------#

# print("[INFO] Interpolate samples from the latent space ...")
# model.linear_interpolate(checkpoint, num_samples=8)

# print('-'*100)
# #----------------------------------------------------------------#
