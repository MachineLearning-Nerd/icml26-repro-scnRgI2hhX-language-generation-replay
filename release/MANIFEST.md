# Release metadata

`upload-allowlist.txt` is the exact set of paths sent through the text-only Hugging Face API. `candidate-manifest.sha256` covers every candidate file except itself; self-exclusion avoids a circular hash. The manifest includes the allowlist and all protected historical files, including unchanged binary assets that remain in place and are not re-uploaded.
