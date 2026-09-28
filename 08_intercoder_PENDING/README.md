# PENDING — human↔human inter-coder α (revised instrument)

**Status:** Not yet available in this package.

**Required before filling Table X in the manuscript:**
1. Coder Minh completes the 200 shared items on the revised sheet (`site/cham/chung_minh.html`) after calibration.
2. Export CSV → place here as `gold2_chung_minh_revised.csv`.
3. Run: `venv/bin/python tools/absa_eval.py --nguoi1 08_intercoder_PENDING/gold2_chung_minh_revised.csv --nguoi2 <truc_shared_export.csv>`
4. Save `intercoder_alpha_tableX.csv` here and update manuscript §3.4 / §5.8.

Do **not** report B8 round-1 Minh–Trúc α (old sheet) as Table X.
