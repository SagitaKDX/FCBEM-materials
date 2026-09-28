# FCBEM — Open materials deposit package

**Paper:** From Rejection to Acceptance: Detecting the Normalization Crossover of Virtual Influencers…  
**Package built:** 2026-09-28  
**Purpose:** Upload this folder (or the zip) to OSF / Zenodo and paste the persistent URL into §3 of the manuscript.

## Contents

| Folder | Contents |
|---|---|
| `01_codebook` | Appendix A + `codebook.py` |
| `02_reliability` | Table 2 α CSV (n = 680) |
| `03_confusion_matrices` | Per-label confusion matrices + α summary |
| `04_gold_sampling` | Sampling scheme + shared-ID list |
| `05_test_inventory` | Pytest collect-only (**718 tests**) |
| `06_figures` | Hi-res Figure 2–3 PNGs |
| `07_channel_notes` | Platform, calendar windows, cadence, dropped controls |
| `08_intercoder` | Human↔human α Table X (n=200); **0/8 pass 0.67 — see folder README** |

## How to deposit (you do this on osf.io)

1. Create account / log in at https://osf.io  
2. **Create project** → title e.g. `FCBEM virtual-influencer discourse materials`  
3. **Files** → Upload (or upload `osf_fcbem.zip`)  
4. Optional: add license (CC-BY recommended for materials)  
5. Make project **Public** (or create a view-only link if journal allows)  
6. Copy the project URL (or component DOI if registered)  
7. In the manuscript, replace the “pending OSF/Zenodo” sentence with that URL  

## Manuscript sentence (after you have the URL)

```
Materials (codebook, per-label confusion matrices, gold-set sampling scheme, automated test inventory, and figures) are deposited at [PASTE OSF/Zenodo URL]. Human↔human inter-coder α (n=200) is in `08_intercoder/`; **no label reached α ≥ 0.67** — see diagnostic notes there.
```

## License note

Confirm you have rights to deposit public Facebook comment **IDs/text** under your ethics protocol. If needed, deposit **matrices + codebook + sampling description only** and keep raw text private.
