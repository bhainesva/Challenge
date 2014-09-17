# Challenge Time

## Introduction
Two words are friends if they have a Levenshtein distance of 1. That is, you
can add, remove, or substitute exactly one letter in word X to create word Y.
A word’s social network consists of all of its friends, all of its friends' friends, and all of its friends' friends' friends.

## Problem
Write a program in your favorite dynamic language that efficiently finds the
social network for any given word, using the word list provided.

## Solution / Comments

At its core, my Levenshtein distance calculator is an implementation of the algorithm described by Michael and Fischer in [this paper](http://dl.acm.org/citation.cfm?doid=321796.321811). The problem does not require reconstruction of edits so I also took advantage of the note made [here](http://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_two_matrix_rows) that allows for improved memory use.

### Modification

My first attempt at creating an effective solution was by simplifying the problem. 

Using the Lemma 1and the definition of traces from the paper above it can be shown that the final "tier" of friends can be reached by at most three steps from the input word. Initially I thought this solved the problem. However, simply selecting all words with a Levenshtein distance of three or less includes words that are not necessarily reachable through the nodes in the provided wordlist.

Although not as useful as I had hoped, taking the initial step of eliminating all strings more than three edits away from the target word did prove helpful. The primary time consuming activity in this problem is looping through the wordlist. The naive solution requires one iteration for the input word and additional iterations for each word in friendship tiers one and two. My solution requires the same number of loops, but over a significantly reduced list.

Additionally, I have altered Michael and Fischer's algorithm to better fit its current use. The problem doesn't require us to actually compute Levenshtein distances, just to know whether they are below a certain threshold. Thus, the program stops calculations after this has been determined.

### Potential Improvements
There are some minor changes that could be made to improve performance. For example, after creating the initial pool of words within three edits of the input, there's no longer a need to check the length of these words as we know they must be an acceptable length. I have chosen not to do this because it would increase code complexity while providing performance improvements that are neglible for a wordlist of this size.

Currently some words can be returned in multiple locations. For example, if the input word is 'knell', it will be displayed in Tier 2 and as the input. However, words from any given tier will not be shown in the tier immediately above it. This was an arbitrary decision and could easily be altered if the context of the problem made one format more applicable.

I do not claim that this is the most efficient approach. 


