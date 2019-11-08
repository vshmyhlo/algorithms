import os
import pickle
import random
import string
import sys
import time

from tqdm import tqdm

# TODO: remove short and long words (outliers)


chars = set(string.ascii_lowercase)

if not os.path.exists('./vocab.pkl'):
    vocab = set()
    with open('./wiki-news-300d-1M.vec') as f:
        for line in tqdm(f, desc='building vocab'):
            word, _ = line.split(maxsplit=1)
            word = word.lower()

            if len(word) > 16:
                continue

            diff = set(word) - chars
            if len(diff) > 0:
                continue

            vocab.add(word)

    with open('./vocab.pkl', 'wb') as f:
        pickle.dump(vocab, f)

with open('./vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)

print('vocab size: {}'.format(len(vocab)))


# def is_tokenizable(text, vocab):
#     max_len = max(map(len, vocab))
#
#     @lru_cache(len(text))
#     def aux(start):
#         if len(text) - start == 0:
#             return True
#
#         # for l in range(1, min(max_len, len(text) - start) + 1):
#         #     if text[start:start + l] in vocab:
#         #         if aux(start + l):
#         #             return True
#
#         for l in range(min(max_len, len(text) - start), 0, -1):
#             if text[start:start + l] in vocab:
#                 if aux(start + l):
#                     return True
#
#         return False
#
#     return aux(0)


def is_tokenizable(text, vocab):
    max_len = max(map(len, vocab))
    cache = [None] * len(text)

    def aux(start):
        if len(text) - start == 0:
            return True

        if cache[start] is not None:
            return cache[start]

        # for l in range(1, min(max_len, len(text) - start) + 1):
        #     if text[start:start + l] in vocab:
        #         if aux(start + l):
        #             return True

        for l in range(min(max_len, len(text) - start), 0, -1):
            if text[start:start + l] in vocab:
                if aux(start + l):
                    cache[start] = True
                    return cache[start]

        cache[start] = False
        return cache[start]

    return aux(0)


# def is_tokenizable(text, vocab):
#     max_len = max(map(len, vocab))
#     # cache = [None] * len(text)
#     stack = [0]
#     while len(stack) > 0:
#         start = stack.pop()
#
#         # if cache[start] is not None:
#         #     return cache[start]
#
#         if len(text) - start == 0:
#             return True
#
#         for l in range(min(max_len, len(text) - start), 0, -1):
#             if text[start:start + l] in vocab:
#                 stack.append(start + l)
#
#     return False


random.seed(42)
vocab_list = sorted(vocab)
print(sys.getrecursionlimit())

text = ''.join(random.choice(vocab_list) for _ in range(900))

t = time.time()
print(is_tokenizable(text, vocab))
print(time.time() - t)

text += 'X'

t = time.time()
print(is_tokenizable(text, vocab))
print(time.time() - t)

# trie = RWayTrie()
# for word in tqdm(vocab, desc='building trie'):
#     trie[word] = True
