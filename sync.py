"""
sync.py — Pull content from the trading system into the wiki.
Run via cron daily, or manually: python3 sync.py
"""

import json
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

TRADING_ROOT = Path("/home/ojas/Documents/Ai-memory/Financial assistant")
WIKI_ROOT    = Path(__file__).resolve().parent
DOCS         = WIKI_ROOT / "docs"
KNOWLEDGE    = TRADING_ROOT / "knowledge"
DB_FILE      = TRADING_ROOT / "trades.db"
STATE_FILE   = TRADING_ROOT / "trader_state.json"


# ---------------------------------------------------------------------------
# Research notes
# ---------------------------------------------------------------------------

def sync_research():
    out = DOCS / "research"
    out.mkdir(exist_ok=True)
    copied = 0
    index_lines = ["# Research\n\n| Topic | Date | Model |\n|-------|------|-------|"]

    for src in sorted(KNOWLEDGE.glob("*.md")):
        if src.name.startswith("_") or src.name == "HOME.md":
            continue
        dest = out / src.name
        shutil.copy2(src, dest)
        copied += 1

        # Pull frontmatter for index
        text = src.read_text()
        topic = date = model = ""
        in_fm = False
        for line in text.splitlines():
            if line.strip() == "---":
                in_fm = not in_fm
                continue
            if in_fm:
                if line.startswith("topic:"):
                    topic = line.split(":", 1)[1].strip().strip('"')
                elif line.startswith("date:"):
                    date = line.split(":", 1)[1].strip()
                elif line.startswith("model:"):
                    model = line.split(":", 1)[1].strip()
        if topic:
            index_lines.append(f"| [{topic}]({src.name}) | {date} | {model} |")

    (out / "index.md").write_text("\n".join(index_lines) + "\n")
    print(f"  research: {copied} notes synced")


# ---------------------------------------------------------------------------
# Trade log from SQLite
# ---------------------------------------------------------------------------

def sync_trades():
    out = DOCS / "trades"
    out.mkdir(exist_ok=True)

    if not DB_FILE.exists():
        (out / "index.md").write_text("# Trade Log\n\nNo trades recorded yet.\n")
        return

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT * FROM trades ORDER BY timestamp DESC LIMIT 100"
    ).fetchall()
    conn.close()

    lines = ["# Trade Log\n", f"_Last synced: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n",
             "\n| Time | Strategy | Symbol | Side | Qty | Price | PnL |",
             "|------|----------|--------|------|-----|-------|-----|"]
    for r in rows:
        pnl = f"${float(r['pnl']):.2f}" if r['pnl'] is not None else "—"
        lines.append(
            f"| {r['timestamp'][:16]} | {r['strategy']} | {r['symbol']} "
            f"| {r['side']} | {r['qty']} | ${float(r['price']):.2f} | {pnl} |"
        )

    (out / "index.md").write_text("\n".join(lines) + "\n")
    print(f"  trades: {len(rows)} rows synced")


# ---------------------------------------------------------------------------
# Performance report from state JSON
# ---------------------------------------------------------------------------

def sync_report():
    out = DOCS / "reports"
    out.mkdir(exist_ok=True)

    if not STATE_FILE.exists():
        (out / "index.md").write_text("# Reports\n\nNo state file found yet.\n")
        return

    state = json.loads(STATE_FILE.read_text())
    lines = ["# Performance Report\n",
             f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n",
             f"\n**Account equity:** ${state.get('peak_equity', 0):.2f} (peak)\n",
             "\n## Strategy Summary\n",
             "| Strategy | Balance | Wins | Losses | Status |",
             "|----------|---------|------|--------|--------|"]

    for name, s in state.get("strategies", {}).items():
        status = "🔴 killed" if s.get("killed") else "🟢 active"
        lines.append(
            f"| {name} | ${s.get('balance', 0):.2f} | {s.get('wins', 0)} "
            f"| {s.get('losses', 0)} | {status} |"
        )

    today = datetime.now().strftime("%Y-%m-%d")
    report_file = out / f"{today}.md"
    content = "\n".join(lines) + "\n"
    report_file.write_text(content)
    (out / "index.md").write_text(content)
    print(f"  report: {today} written")


# ---------------------------------------------------------------------------
# Nav rebuild
# ---------------------------------------------------------------------------

def rebuild_nav():
    research_files = sorted((DOCS / "research").glob("*.md"))
    research_nav = ["  - Overview: research/index.md"] + [
        f"  - {f.stem.replace('_', ' ').title()}: research/{f.name}"
        for f in research_files if f.name != "index.md"
    ]

    report_files = sorted((DOCS / "reports").glob("[0-9]*.md"), reverse=True)
    reports_nav = ["  - Latest: reports/index.md"] + [
        f"  - {f.stem}: reports/{f.name}"
        for f in report_files[:10]
    ]

    mkdocs = WIKI_ROOT / "mkdocs.yml"
    text = mkdocs.read_text()
    nav_block = "\nnav:\n  - Home: index.md\n  - Research:\n"
    nav_block += "\n".join(research_nav) + "\n"
    nav_block += "  - Strategies:\n    - Overview: strategies/index.md\n"
    nav_block += "  - Trades:\n    - Overview: trades/index.md\n"
    nav_block += "  - Reports:\n"
    nav_block += "\n".join(reports_nav) + "\n"

    # Replace nav section
    import re
    text = re.sub(r"\nnav:.*", nav_block, text, flags=re.DOTALL)
    mkdocs.write_text(text)
    print("  nav: rebuilt")


if __name__ == "__main__":
    print(f"Syncing wiki — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    sync_research()
    sync_trades()
    sync_report()
    rebuild_nav()
    print("Done.")
