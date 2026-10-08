#!/usr/bin/env python3
"""Phase-3 fixes for Smoker-Agent.

- Remove the upstream-author line from the Settings About card entirely (the
  repository keeps its README credits + LICENSE; the app no longer shows the
  name). Nothing is added in its place -- the YouTube tile remains.
- Point the API request `HTTP-Referer` at this fork so no upstream owner name
  ships inside the app.
- Preconfigure the default AI backend: OpenRouter endpoint, NVIDIA Nemotron
  model, and a default API key injected at build time so the app is
  preconfigured on first run.
- Bump the app version.

Idempotent: running it twice is a no-op.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (path, old, new) applied in order; plain string replacements.
REPLACEMENTS = [
    # 1. About card: drop the upstream-author subtitle entirely (add nothing).
    (
        "lib/screens/settings_screen.dart",
        "            title: 'About Smoker-Agent',\n"
        "            subtitle: 'Based on the original project by orailnoor & Tech Jarves',\n"
        "            isDark: isDark,\n",
        "            title: 'About Smoker-Agent',\n"
        "            isDark: isDark,\n",
    ),
    # 2. API request attribution -> this fork (removes upstream owner from app).
    (
        "lib/services/ai_service.dart",
        "https://github.com/orailnoor/private-agent",
        "https://github.com/mobiclawtest-cell/private-agent",
    ),
    # 3. Default backend -> OpenRouter + Nemotron; key read from a build define.
    (
        "lib/services/ai_service.dart",
        "  static const String _defaultBaseUrl = 'https://api.deepseek.com';\n"
        "  static const String _defaultModel = 'deepseek-chat';\n",
        "  static const String _defaultBaseUrl = 'https://openrouter.ai/api/v1';\n"
        "  static const String _defaultModel =\n"
        "      'nvidia/nemotron-3-super-120b-a12b:free';\n"
        "\n"
        "  /// Default API key, injected at build time via\n"
        "  /// `--dart-define=OPENROUTER_API_KEY=...` (kept out of public source).\n"
        "  /// The released APK is therefore preconfigured out of the box. Falls\n"
        "  /// back to empty when the define is absent (API then shows unconfigured).\n"
        "  static const String _defaultApiKey =\n"
        "      String.fromEnvironment('OPENROUTER_API_KEY');\n",
    ),
    # 4. Fall back to the default key when the user has not saved one.
    (
        "lib/services/ai_service.dart",
        "    _apiKey = prefs.getString('api_key');\n",
        "    _apiKey = prefs.getString('api_key') ?? _defaultApiKey;\n",
    ),
    # 5. Version bump.
    (
        "pubspec.yaml",
        "version: 1.1.1+2023",
        "version: 1.1.2+2024",
    ),
]


def main():
    applied = 0
    for rel, old, new in REPLACEMENTS:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        # "old not present" means already applied. Do NOT gate on `new in text`,
        # because a multi-occurrence replacement can be partially applied and
        # that check would then wrongly skip the remaining occurrences.
        if old not in text:
            print(f"already applied: {rel} ({old[:48]!r})")
            continue
        path.write_text(text.replace(old, new), encoding="utf-8")
        applied += 1
        print(f"updated {rel} ({old[:48]!r})")

    print(f"phase-3 fixes applied to {applied} spot(s)")


if __name__ == "__main__":
    main()
