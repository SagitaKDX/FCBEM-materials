# Gold-set sampling scheme

As described in manuscript §3.4:

1. **Size:** 800 comments.
2. **Design:** Stratified sampling with **rare-class enrichment** for `R_uncanny`, `R_ai_skepticism`, and `C_commercial`, to yield enough positive cases to estimate recall.
3. **Dual-coding subset:** 200 of the 800 are designated for **two independent human coders** (shared items) to support Krippendorff’s α (human↔human).
4. **Single-coding remainder:** 600 items split across coders for single coding.
5. **Calibration:** a 40-item calibration round with self-check on the revised coding sheet precedes main coding.
6. **Instrument:** Revised sheet keeps codebook definitions visible; blocks construct-without-aspect and `S_parasocial` without a social cue.
7. **Use of rates:** Because the gold set is rare-class enriched, **label rates on the gold set are not used to estimate population prevalence**; they score models / agreement only.
8. **Cross-model:** Gold items were also labeled by DeepSeek-V4-Flash and GLM-5.2 under the same codebook (`temperature = 0`); manuscript Table 2 reports α on n = 680 comments comparable across pairings.

## Files

- `gold2_chung_200_shared_ids.csv` — the 200 shared items (comment ID, week, VI, public reel URL, comment text).
- The two human codings of these items and their α are in `../08_intercoder/`.
