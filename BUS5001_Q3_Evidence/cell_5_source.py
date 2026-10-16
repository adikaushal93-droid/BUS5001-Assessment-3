import time
from datetime import datetime, timezone

run_log = []
parsed_results = []

for item in messages:
    print(f"\nRunning {item['message_id']}...")

    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(item)}
    ]

    text = tokenizer.apply_chat_template(
        conversation,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    started_at = datetime.now(timezone.utc).isoformat()
    torch.cuda.synchronize()
    start = time.perf_counter()

    with torch.inference_mode():
        generated = model.generate(
            **inputs,
            max_new_tokens=700,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start

    new_tokens = generated[0, inputs["input_ids"].shape[1]:]
    raw_output = tokenizer.decode(
        new_tokens, skip_special_tokens=True
    ).strip()

    # Preserve the original response before attempting to parse it.
    (evidence_dir / f"{item['message_id']}_raw_output.txt").write_text(
        raw_output, encoding="utf-8"
    )

    try:
        result = json.loads(raw_output)
        parsed_results.append(result)
        json_valid = True
        parse_error = None
    except json.JSONDecodeError as error:
        json_valid = False
        parse_error = str(error)

    run_log.append({
        "message_id": item["message_id"],
        "model": MODEL_ID,
        "model_revision": getattr(model.config, "_commit_hash", None),
        "transformers_version": transformers.__version__,
        "started_at_utc": started_at,
        "do_sample": False,
        "max_new_tokens": 700,
        "generated_tokens": len(new_tokens),
        "elapsed_seconds": round(elapsed, 2),
        "json_syntax_valid": json_valid,
        "parse_error": parse_error
    })

    (evidence_dir / "run_log.json").write_text(
        json.dumps(run_log, indent=2), encoding="utf-8"
    )

    (evidence_dir / "qwen_parsed_outputs.json").write_text(
        json.dumps({"results": parsed_results}, indent=2),
        encoding="utf-8"
    )

    print(raw_output)
    print("JSON syntax valid:", json_valid)
    print("Elapsed seconds:", round(elapsed, 2))

print("\nAll three model runs completed.")