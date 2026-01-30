import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------- config ----------
INPUT_CSV = "outputs/risk_map_input.csv"
OUT_DIR = "figures"
OUT_PNG = os.path.join(OUT_DIR, "clinvar_risk_map.png")
OUT_SVG = os.path.join(OUT_DIR, "clinvar_risk_map.svg")

TITLE = "Mapping Interpretation Stability in ClinVar:\nAge and Consensus Stratify Reclassification Risk"
SUBTITLE = "Evidence age and submission consensus jointly stratify interpretation stability."

RISK_ORDER = ["Low", "Moderate", "High", "Critical"]
RISK_COLORS = {
    "Low": "#2E7D32",
    "Moderate": "#F9A825",
    "High": "#FB8C00",
    "Critical": "#C62828",
}

Y_TICKS = [1, 2, 3]
Y_TICKLABELS = ["Low", "Medium", "High"]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1) Load
    if not os.path.exists(INPUT_CSV):
        raise FileNotFoundError(
            f"Missing {INPUT_CSV}. Run your notebook export cell first. "
            f"Check: ls outputs"
        )

    df = pd.read_csv(INPUT_CSV)

    # 2) Validate columns
    required = {"years_since_last_eval", "confidence_level", "risk_tier"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in {INPUT_CSV}: {missing}")

    # 3) Clean / normalize
    df = df.dropna(subset=list(required)).copy()

    df["risk_tier"] = (
        df["risk_tier"].astype(str).str.strip().str.title().replace({"Med": "Moderate"})
    )
    df = df[df["risk_tier"].isin(RISK_ORDER)].copy()

    df["years_since_last_eval"] = pd.to_numeric(df["years_since_last_eval"], errors="coerce")
    df["confidence_level"] = pd.to_numeric(df["confidence_level"], errors="coerce")

    df = df.dropna(subset=["years_since_last_eval", "confidence_level"]).copy()
    df["years_since_last_eval"] = df["years_since_last_eval"].clip(0, 45)
    df["confidence_level"] = df["confidence_level"].clip(1, 3)

    # 4) Jitter (cloudy look like your mock)
    rng = np.random.default_rng(42)
    df["confidence_jitter"] = df["confidence_level"] + rng.normal(0, 0.12, size=len(df))
    df["years_jitter"] = df["years_since_last_eval"] + rng.normal(0, 0.35, size=len(df))

    # 5) Plot
    plt.figure(figsize=(12, 6.2))
    ax = plt.gca()

    ax.grid(True, which="major", axis="both", linewidth=0.8, alpha=0.15)

    for tier in RISK_ORDER:
        sub = df[df["risk_tier"] == tier]
        ax.scatter(
            sub["years_jitter"],
            sub["confidence_jitter"],
            s=22,
            alpha=0.65,
            edgecolors="none",
            label=tier,
            c=RISK_COLORS[tier],
        )

    ax.set_xlabel("Years Since Last Expert Evaluation", fontsize=12)
    ax.set_ylabel("Interpretation Confidence\n(Review Strength)", fontsize=12)

    ax.set_yticks(Y_TICKS)
    ax.set_yticklabels(Y_TICKLABELS, fontsize=11)
    ax.set_ylim(0.6, 3.4)

    ax.set_xlim(-1, 45)
    ax.tick_params(axis="x", labelsize=11)

    plt.suptitle(TITLE, fontsize=16, fontweight="bold", y=0.98)
    plt.title(SUBTITLE, fontsize=11, style="italic", pad=12)

    leg = ax.legend(
        title="Inferred Reclassification Risk",
        loc="upper right",
        frameon=True,
        borderpad=0.8,
    )
    leg.get_title().set_fontsize(11)
    for t in leg.get_texts():
        t.set_fontsize(11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig(OUT_PNG, dpi=300)
    plt.savefig(OUT_SVG)
    plt.close()

    print(f"Saved:\n- {OUT_PNG}\n- {OUT_SVG}\nRows plotted: {len(df)}")


if __name__ == "__main__":
    main()
