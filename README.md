# FCBEM — Open materials

Supplementary materials for the manuscript:

> Quan, M. T., Le, T. M., & Huynh, A.-V. *From Rejection to Acceptance: Detecting the Normalization Crossover of Virtual Influencers through Longitudinal Social Media Discourse in Vietnam.* FPT University, Greenwich Vietnam.

This repository is the materials deposit referred to in Section 3 of the manuscript. Cite a fixed version via its release tag (see [Releases](https://github.com/SagitaKDX/FCBEM-materials/releases)).

## Contents

| Folder | Contents | Manuscript |
|---|---|---|
| [`01_codebook`](01_codebook) | Discourse coding scheme (four constructs, four aspects) and the machine-readable codebook used by the labelling pipeline | Appendix A, §3.3 |
| [`02_reliability`](02_reliability) | Krippendorff's α by label for DeepSeek↔GLM, DeepSeek↔gold and GLM↔gold (n = 680) | Table 2, Figure 2 |
| [`03_confusion_matrices`](03_confusion_matrices) | Per-label confusion matrices for every model/gold/human pairing, and the α recomputed from them | §3.4 |
| [`04_gold_sampling`](04_gold_sampling) | Gold-set sampling scheme and the 200 shared (dual-coded) item IDs | §3.4 |
| [`05_test_inventory`](05_test_inventory) | Full list of the 718 automated tests guarding the collection and processing pipeline | §3 |
| [`06_figures`](06_figures) | High-resolution Figures 2 and 3 | Figures 2–3 |
| [`07_channel_notes`](07_channel_notes) | Platform, comment-inclusion rules, calendar alignment of observation windows, posting cadence, and dropped post-level controls | §3.1–3.2 |
| [`08_intercoder`](08_intercoder) | Human–human inter-coder α on the revised instrument (n = 200 shared comments) and the underlying codings | §3.4, §5.8 |

## Reliability at a glance

- **Human–model and cross-model α** (Table 2): see `02_reliability/`. Thresholds follow Krippendorff (2004): α ≥ 0.80 reliable; 0.67 ≤ α < 0.80 tentative; α < 0.67 fails for confirmatory claims.
- **Human–human α on the revised instrument** (n = 200): no retained label reaches 0.67 (range −0.09 to 0.60). Disagreement on `S_parasocial` is largely one-sided (102 vs 1 comments). The manuscript therefore relies on human–model and cross-model agreement and flags claims that rest on failing labels at the point of claim. Details: `08_intercoder/`.

## Data and privacy

All comments come from public Facebook pages and profiles of five virtual influencers. Commenter names and profile identifiers are not included. The comment IDs in this deposit are pseudonymous hashes. Items in `04_gold_sampling/` and `08_intercoder/` include the comment text and the public reel URL, because coding decisions cannot be audited without them. The full comment corpus is not redistributed.

## License

Materials: CC BY 4.0 (see `LICENSE.txt`).
