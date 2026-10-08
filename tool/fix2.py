#!/usr/bin/env python3
"""Phase-2 branding fixes for Smoker-Agent.

Patches the leaks that survived the first rebrand pass:

  * the chat app-bar title is built from two TextSpans ('Private' + 'Agent'),
    so the combined "PrivateAgent" replacement never matched it;
  * the overlay welcome text and bubble header spelled it "Private Agent"
    (with a space);
  * the Settings "About" tile now links to the project YouTube video instead
    of the source repository. The upstream credit line on that card is kept.

Idempotent: running it twice is a no-op.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (path, old, new) applied in order; plain string replacements.
REPLACEMENTS = [
    (
        "lib/screens/home_screen.dart",
        "text: 'Private',",
        "text: 'Smoker-',",
    ),
    (
        "lib/overlay_main.dart",
        "'Hi! I am your Private Agent. Ask me to perform any task on your screen.'",
        "'Hi! I am your Smoker-Agent. Ask me to perform any task on your screen.'",
    ),
    (
        "lib/overlay_main.dart",
        "                        'Private Agent',",
        "                        'Smoker-Agent',",
    ),
    (
        "pubspec.yaml",
        "version: 1.1.0+2022",
        "version: 1.1.1+2023",
    ),
]

OLD_TILE = """              ListTile(
                contentPadding: EdgeInsets.zero,
                title: const Text('Project Repository'),
                subtitle: const Text('Original project by orailnoor & Tech Jarves'),
                leading: const Icon(Icons.code_rounded),
                onTap: () {
                  launchUrl(
                    Uri.parse('https://github.com/orailnoor/private-agent'),
                    mode: LaunchMode.externalApplication,
                  );
                },
              ),"""

NEW_TILE = """              ListTile(
                contentPadding: EdgeInsets.zero,
                title: const Text('Watch on YouTube'),
                subtitle: const Text('Demo video and tutorials'),
                leading: const Icon(
                  Icons.play_circle_fill_rounded,
                  color: Colors.red,
                ),
                onTap: () {
                  launchUrl(
                    Uri.parse('https://youtube.com/shorts/TgBEnZhTSVs?si=NBb_Niws_htZY1XN'),
                    mode: LaunchMode.externalApplication,
                  );
                },
              ),"""


def main():
    applied = 0
    for rel, old, new in REPLACEMENTS:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if new in text:
            print(f"already applied: {rel}")
            continue
        if old not in text:
            print(f"WARNING: pattern not found in {rel}: {old[:60]!r}", file=sys.stderr)
            continue
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        applied += 1
        print(f"updated {rel}")

    settings = ROOT / "lib/screens/settings_screen.dart"
    text = settings.read_text(encoding="utf-8")
    if NEW_TILE in text:
        print("already applied: settings About tile")
    elif OLD_TILE in text:
        settings.write_text(text.replace(OLD_TILE, NEW_TILE, 1), encoding="utf-8")
        applied += 1
        print("updated lib/screens/settings_screen.dart (About tile -> YouTube)")
    else:
        print("WARNING: About tile block not found", file=sys.stderr)

    print(f"phase-2 fixes applied to {applied} spot(s)")


if __name__ == "__main__":
    main()
