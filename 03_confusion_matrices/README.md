# Confusion matrices (per label)

Each pairing folder contains one CSV per label. Rows = first coder/model; columns = second.

## Pairings

| Folder | Left | Right | Notes |
|---|---|---|---|
| `DeepSeek_vs_gold_vote` | DeepSeek-V4-Flash | `nhan_nhap_bieu_quyet.csv` | Majority-vote import used in analysis pipeline |
| `GLM_vs_gold_vote` | GLM-5.2 | same gold vote | |
| `DeepSeek_vs_GLM` | DeepSeek | GLM | Cross-model |
| `Truc_human_vs_DeepSeek` | Human coder Trúc (`gold2_truc_nop1.csv`) | DeepSeek | Overlap only |
| `Truc_human_vs_GLM` | Human coder Trúc | GLM | Overlap only |

**Manuscript Table 2** uses n = 680 comparable comments across three pairings; see `../02_reliability/Table2_krippendorff_alpha_n680.csv`. Matrix folders here use whatever ID overlap exists in the deposited raw files (n may differ by pairing).

Binary constructs use `{0,1}`; aspects use `{+1,0,-1,NA}`.
