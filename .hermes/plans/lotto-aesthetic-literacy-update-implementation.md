# Lotto Aesthetic Literacy Realistic Scratcher Update Plan

Goal: strengthen the lotto dictionary entry and knowledge profile so they describe real scratch-off ticket language instead of a generic digital promo card.

Architecture: This is a docs/knowledge update guarded by repository regression tests. Add focused test assertions for the lotto files, then update only the lotto entry/profile to satisfy the scratcher realism acceptance criteria while preserving fictional/non-redeemable framing and the casino distinction.

Tasks:
1. Add tests in `tests/test_aesthetic_entries.py` that require lotto dictionary/profile text to include drag/brush partial reveal, grey latex debris/residue, validation/serial/void markers, dense grid hierarchy, price/lottery badge, foil/security/paper texture, casino distinction, and fictional/non-redeemable safety language.
2. Run the targeted tests and confirm they fail against the current baseline.
3. Update `skills/aesthetic-literacy/aesthetics/lotto.md` with stronger seven-dimension guidance and non-negotiables grounded in the supplied scratcher references.
4. Update `knowledge/aesthetics/lotto.md` with a 2026-06-26 research update that records the reference-specific corrections and implementation guidance.
5. Run `make test` and `make check`, inspect `git diff`, then commit, push, and open a PR.
