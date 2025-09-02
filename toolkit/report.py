def generate_report(results, output_path):
    with open(output_path, "w") as f:
        f.write("# 🛡️ Compliance Audit Report\n\n")
        for r in results:
            f.write(f"- **{r['id']} - {r['name']}**: {r['status']}\n")
