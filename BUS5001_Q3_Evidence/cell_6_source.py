import re

cleaned_results = []

for item in messages:
    message_id = item["message_id"]

    raw = (
        evidence_dir / f"{message_id}_raw_output.txt"
    ).read_text(encoding="utf-8")

    cleaned = raw.strip()

    # Remove only an enclosing Markdown code fence.
    match = re.fullmatch(
        r"```(?:json)?\s*\n?(.*?)\n?```",
        cleaned,
        flags=re.DOTALL | re.IGNORECASE
    )

    if match:
        cleaned = match.group(1).strip()

    print(f"\n--- {message_id} ---")

    try:
        result = json.loads(cleaned)
        cleaned_results.append(result)
        print(json.dumps(result, indent=2))
        print("JSON syntax valid after wrapper removal: True")
    except json.JSONDecodeError as error:
        print("JSON parsing failed:", error)
        print("Original output:")
        print(raw)

(evidence_dir / "qwen_cleaned_outputs.json").write_text(
    json.dumps({"results": cleaned_results}, indent=2),
    encoding="utf-8"
)

print("\nOriginal raw outputs remain unchanged.")