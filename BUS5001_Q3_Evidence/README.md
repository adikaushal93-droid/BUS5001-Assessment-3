# BUS5001 Q3 ESG message triage evidence

Recovered from the uploaded Colab notebook and its saved cell outputs. No model was rerun and no predictions were corrected.

## Contents
- Original notebook, unchanged, including saved outputs.
- Revised prompt and three simulated messages extracted from notebook source using static parsing.
- M1/M2/M3 raw responses recovered from the generation cell, including Markdown fences. Console separators and trailing console newline are excluded; original full console output is retained separately.
- qwen_cleaned_outputs.json: only enclosing Markdown fences removed. All prediction values remain unchanged.
- baseline_outputs.json and comparison.csv: actual saved keyword-baseline results and side-by-side comparison.
- run_log_recovered.json: observed timings and parsing outcomes, plus settings from source.
- Cell source and output text files for traceability.

## Recovery limitations
The original runtime files were unavailable. The original run_log.json was not printed in the notebook, so its complete contents cannot be recovered. Exact run timestamps, resolved model revision, generated token counts and original parser-error strings are unavailable and are not invented. The recovered log is explicitly named run_log_recovered.json.

Transformers version 4.57.6 and Tesla T4 are visible in saved outputs. Model ID and generation settings are retained in notebook source. Timings are 6.65, 4.49 and 4.44 seconds for M1, M2 and M3 respectively.

All three raw responses failed strict JSON parsing because of Markdown fences; all three parsed after fence removal. Parsing success does not establish classification correctness. Recorded errors include M1 emergency routing, M2 urgency, and M3 urgency/follow-up. This three-example comparison uses a baseline designed after the messages were inspected; it is not a general performance estimate. There is no paired prompt-injection control test in this package.

ChatGPT preliminary outputs and external screenshots are not included in this notebook recovery package.
