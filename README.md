# CorrectHorse

[![alt text](https://imgs.xkcd.com/comics/password_strength.png "Password strength xkcd")](https://xkcd.com/936/)

<s>Random words generator</s> **random secure password generator**.

The file [20k.txt](https://github.com/Shifterovich/CorrectHorse/blob/master/20k.txt) comes from [google-10000-english](https://github.com/first20hours/google-10000-english).

Feel free to use any other list, for example some of the [EFF's ones](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).

Protip: "bad words" are easier to remember. For example, [a list](https://www.cs.cmu.edu/~biglou/resources/bad-words.txt) mentioned on the [EFF page](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) contains 1383 words.

1383 words is not much, but is still *pretty* safe.

Amount of words | Calculation* | Possible combinations
--------------- | ----------- | ---------------------
1 | 1383^1 | 1383
2 | 1383^2 | 1912689
3 | 1383^3 | 2645248887
4 | 1383^4 | 3658379210721
5 | 1383^5 | 5.05953845 \* 10^15
6 | 1383^6 | 6.99734167 \* 10^18
7 | 1383^7 | 9.67732354 \* 10^21
8 | 1383^8 | 1.33837384 \* 10^25
9 | 1383^9 | 1.85097103 \* 10^28
10 | 1383^10 | 2.55989293 \* 10^31

_\* For amount of possible combinations with repetitions (therefore words can be contained more than once)_
