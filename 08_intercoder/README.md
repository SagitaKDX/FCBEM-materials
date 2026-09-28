# Human↔human inter-coder α (revised-sheet exports)

**Source files**
- Minh: `gold2_chung_minh.csv` (200/200 `xong=1`, Downloads export 2026-09-28)
- Trúc: `data/absa/gold2_truc_nop1.csv` (overlap n = 200 shared IDs)

**Results:** `intercoder_alpha_tableX.csv`

| Label | α | Verdict |
|---|---:|---|
| R_uncanny | 0.265 | fail |
| R_ai_skepticism | 0.363 | fail |
| S_parasocial | −0.093 | fail |
| C_commercial | 0.603 | fail (nearest to 0.67) |
| asp_appearance | 0.211 | fail |
| asp_voice_motion | 0.137 | fail |
| asp_ai_nature | 0.049 | fail |
| asp_persona | −0.003 | fail |

**Mean α ≈ 0.19. 0/8 labels reach 0.67.**

## Critical diagnostic (S_parasocial)
On the 200 shared items:
- Minh positive rate **63.0%** vs Trúc **12.5%**
- Disagreement almost one-sided: Minh=1/Trúc=0 **102**; Minh=0/Trúc=1 **1**
See `S_parasocial_disagreement.csv`.

This pattern resembles the discarded round-1 instrument failure (over-application of `S_parasocial`). **Do not treat these α values as evidence that the revised codebook is reliable** until Minh re-checks familiar-address / social-cue rules and (if needed) re-codes.

## Manuscript use
- You **may** deposit these files for transparency.
- For §3.4, prefer: report the table + explicit caveat that no label cleared 0.67 and S_parasocial remains one-sided; keep point-of-claim caveats for H2/H3/H4.
