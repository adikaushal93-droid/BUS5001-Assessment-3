def rule_based_triage(item):
    text = item["message"].lower()

    # Simple keyword baseline, applied in the stated order.
    if "water leak" in text:
        category = "WATER_LEAK"
        urgency = "CRITICAL" if "electrical" in text else "MEDIUM"
        team = (
            "Emergency/Security"
            if urgency == "CRITICAL"
            else "Facilities"
        )
    elif "air conditioning" in text and "overnight" in text:
        category = "ENERGY_WASTE"
        urgency = "MEDIUM"
        team = "Facilities"
    elif "accessible entrance" in text and "blocked" in text:
        category = "ACCESSIBILITY"
        urgency = "HIGH"
        team = "Accessibility Support"
    else:
        category = "OTHER"
        urgency = "LOW"
        team = "Human Triage"

    return {
        "message_id": item["message_id"],
        "issue_category": category,
        "urgency": urgency,
        "recommended_team": team,
        "followup_required": "N" if category == "OTHER" else "Y"
    }

baseline_results = [rule_based_triage(item) for item in messages]

(evidence_dir / "baseline_outputs.json").write_text(
    json.dumps(baseline_results, indent=2),
    encoding="utf-8"
)

print(json.dumps(baseline_results, indent=2))
print("\nRule-based baseline completed and saved.")