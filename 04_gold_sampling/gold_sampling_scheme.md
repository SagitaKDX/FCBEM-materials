# Gold-set sampling scheme

As described in the manuscript (§3 Annotation / reliability):

1. **Size:** 800 comments.
2. **Design:** Stratified sampling with **rare-class enrichment** for `R_uncanny`, `R_ai_skepticism`, and `C_commercial`, to yield enough positive cases to estimate recall.
3. **Dual-coding subset:** 200 of the 800 are designated for **two independent human coders** (shared items) to support Krippendorff’s α (human↔human).
4. **Single-coding remainder:** 600 items split across coders for single coding.
5. **Calibration:** 40-item calibration round with self-check on the revised browser sheet (`site/cham/hieu_chuan.html`) precedes main coding.
6. **Instrument:** Revised sheet keeps codebook definitions visible; blocks construct-without-aspect and `S_parasocial` without a social cue.
7. **Use of rates:** Because the gold set is rare-class enriched, **label rates on the gold set are not used to estimate population prevalence**; they score models / agreement only.
8. **Cross-model:** Gold items were also labeled by DeepSeek-V4-Flash and GLM-5.2 under the same codebook (`temperature = 0`); manuscript Table 2 reports α on n = 680 comments comparable across pairings.

## Files in this deposit related to gold IDs

- Shared-item sheet data: `site/cham/data/phieu_chung_*.js` (in repository; not all re-copied here).
- Human coder Trúc (revised sheet export): source path `data/absa/gold2_truc_nop1.csv` (500 rows including shared + private).
- Pipeline gold vote import: `data/absa/nhan_nhap_bieu_quyet.csv` (800 rows).

Human↔human α on the **revised** instrument for the 200 shared items will be deposited in `08_intercoder_PENDING/` once the second coder completes re-coding.
