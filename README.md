# MinEnglish

**"Uat u spic is uat u spel."**

MinEnglish is a formal simplification and clarification of Modern English. Its
aim is to **remove** the inconsistencies, redundancies, and irregularities that
burden English — not to replace it with something foreign.

The result is a leaner, fully regular version of English: same vocabulary, same
phonemes, same word order — but with predictable spelling, explicit quantities,
and precise time operators.

## Key Design Principles

1. **Phonetic Spelling**: Every letter has one sound, every sound one letter.
   (`knight` → `nait`, `enough` → `inuf`)
2. **Explicit Quantities**: Plurals are explicitly numbered to prevent noisy
   channel errors. Singular is the default. (`3cat` instead of `cats`)
3. **Regular Time**: Tenses are simplified into algebraic operators (`-1d`,
   `1d`, `:5Y`) instead of irregular verbs.
4. **Symbolic Operators**: Adopts familiar logical syntax (`&`, `|`, `^`, `>`,
   `<`) to compress compound constructs.
5. **Zero Exceptions**: Irregular verbs, irregular plurals, and silent letters
   are completely abolished.

## Performance

Across a 35-sentence corpus comparing American English against MinEnglish, the
protocol achieves an average **~35.0% byte-length density reduction** by
applying Information Theory principles to eliminate Claude Shannon redundancy.

## Documentation

- The full specifications and ruleset can be found in `MinEnglish.md` or
  compiled into `MinEnglish.pdf`.
- An Academic Review of the system architecture can be found in
  `academic_review.md`.

## License

MIT (See `MinEnglish.md` Appendix B)
