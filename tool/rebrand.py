#!/usr/bin/env python3
"""One-shot rebrand: PrivateAgent -> Smoker-Agent.

Applies the rename across the Flutter/Dart sources, the Android module and the
CI workflow, removes the two YouTube promo links from Settings, rewrites the
README (with proper credit to the original authors) and generates the new
"Smoker-Agent" app logo.

Idempotent: running it twice is a no-op.
"""

import os
import re
import shutil
import sys
import tempfile
import urllib.request

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (old, new) applied in order across all text sources.
REPLACEMENTS = [
    ("com.orailnoor.privateagent", "com.smoke"),
    ("com.privateagent", "com.smoke"),
    ("PrivateAgentApp", "SmokerAgentApp"),
    ("PrivateAgentKotlin", "SmokerAgentKotlin"),
    ("PrivateAgentDart", "SmokerAgentDart"),
    ("PrivateAgent", "Smoker-Agent"),
    ("private_agent", "smoker_agent"),
    ("private-agent-android", "smoker-agent-android"),
    ('description: "AI agent for Android"', 'description: "Smoker-Agent - AI agent for Android"'),
    ("version: 1.0.2+2021", "version: 1.1.0+2022"),
]

SOURCE_DIRS = ["lib", "android/app", "test", ".github"]
SOURCE_FILES = ["pubspec.yaml", "test_parse.dart"]
SOURCE_SUFFIXES = {".dart", ".yaml", ".yml", ".xml", ".kts", ".kt", ".md"}

KOTLIN_SRC = ROOT / "android/app/src/main/kotlin/com/orailnoor/privateagent"
KOTLIN_DST = ROOT / "android/app/src/main/kotlin/com/smoke"


# Old slate/indigo palette -> new ember/bone palette (cosmetic only).
COLOR_REMAP = [
    ("0xFF4F46E5", "0xFFEA580C"),  # primary indigo-600 -> ember-600
    ("0xFF6366F1", "0xFFFB923C"),  # indigo-500 -> ember-400
    ("0xFF0EA5E9", "0xFFF59E0B"),  # sky-500 -> amber-500
    ("0xFF38BDF8", "0xFFFBBF24"),  # sky-400 -> amber-400
    ("0xFFF8FAFC", "0xFFFAF6F1"),  # slate-50 -> bone
    ("0xFFF1F5F9", "0xFFF4EDE4"),  # slate-100 -> warm sand
    ("0xFFE2E8F0", "0xFFEDE2D4"),  # slate-200 -> warm border
    ("0xFF94A3B8", "0xFFA89684"),  # slate-400 -> warm taupe
    ("0xFF64748B", "0xFF8A7566"),  # slate-500
    ("0xFF475569", "0xFF5C4B3D"),  # slate-600 -> warm bark
    ("0xFF334155", "0xFF3D322A"),  # slate-700
    ("0xFF1E293B", "0xFF2A211A"),  # slate-800 -> smoked charcoal
    ("0xFF0F172A", "0xFF1C1512"),  # slate-900
    ("0xFF243049", "0xFF35291E"),  # dark border -> warm border
    ("0xFF151D30", "0xFF1E1811"),  # dark surface -> warm charcoal
    ("0xFF0B0F19", "0xFF120D0A"),  # dark bg -> deep smoke black
    ("0xFF161329", "0xFF1A120D"),  # dark purple-black -> warm black
    ("0xFF0C0A15", "0xFF0F0A07"),  # dark purple-black -> warm black
    ("0xFFF2F2F2", "0xFFF4EFE7"),  # overlay grey -> warm grey
    ("0xFFF2F2F5", "0xFFF4EFEA"),  # overlay grey -> warm grey
    ("0xFFEAEAEA", "0xFFEBE3D8"),  # overlay grey -> warm grey
    ("0xFF9E9BAC", "0xFFA79A8C"),  # muted text -> warm muted
    ("0xFF6C6A7C", "0xFF7A6C5E"),  # muted text -> warm muted
    ("Colors.indigoAccent", "Colors.orangeAccent"),
]


def text_files():
    for d in SOURCE_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.suffix in SOURCE_SUFFIXES and "build" not in p.parts:
                yield p
    for f in SOURCE_FILES:
        p = ROOT / f
        if p.exists():
            yield p


def apply_replacements():
    hits = 0
    for path in text_files():
        original = path.read_text(encoding="utf-8")
        updated = original
        for old, new in REPLACEMENTS:
            updated = updated.replace(old, new)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            hits += 1
            print(f"  updated {path.relative_to(ROOT)}")
    print(f"replacements applied to {hits} file(s)")


def apply_palette():
    hits = 0
    for path in sorted((ROOT / "lib").rglob("*.dart")):
        original = path.read_text(encoding="utf-8")
        updated = original
        for old, new in COLOR_REMAP:
            updated = updated.replace(old, new)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            hits += 1
    print(f"palette remap applied to {hits} file(s)")


def move_kotlin_package():
    if not KOTLIN_SRC.exists():
        print("kotlin sources already moved")
        return
    KOTLIN_DST.parent.mkdir(parents=True, exist_ok=True)
    os.renames(KOTLIN_SRC, KOTLIN_DST)
    print(f"moved kotlin package dir -> {KOTLIN_DST.relative_to(ROOT)}")


def strip_youtube_promos():
    path = ROOT / "lib/screens/settings_screen.dart"
    text = path.read_text(encoding="utf-8")
    for who in ("Orailnoor", "Tech Jarves"):
        pattern = re.compile(
            r"              ListTile\(\n"
            r"                contentPadding: EdgeInsets\.zero,\n"
            r"                title: const Text\('" + re.escape(who) + r" on YouTube'\),"
            r".*?\n              \),\n",
            re.DOTALL,
        )
        text, n = pattern.subn("", text)
        if n != 1:
            print(f"WARNING: expected 1 '{who}' tile, removed {n}", file=sys.stderr)
    text = text.replace(
        "subtitle: 'Resources and repository access',",
        "subtitle: 'Based on the original project by orailnoor & Tech Jarves',",
    )
    text = text.replace(
        "subtitle: const Text('View source code on GitHub'),",
        "subtitle: const Text('Original project by orailnoor & Tech Jarves'),",
    )
    path.write_text(text, encoding="utf-8")
    print("settings_screen.dart: YouTube promo links removed, credits kept")


MAIN_DART = r'''
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter_overlay_window/flutter_overlay_window.dart';
import 'dart:developer';
import 'config/feature_flags.dart';
import 'screens/home_screen.dart';
import 'screens/onboarding_screen.dart';
import 'overlay_main.dart';

@pragma("vm:entry-point")
void overlayMain() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        canvasColor: Colors.transparent,
        scaffoldBackgroundColor: Colors.transparent,
        cardColor: Colors.white,
        dialogBackgroundColor: Colors.transparent,
        primaryColor: const Color(0xFFEA580C),
        useMaterial3: true,
        colorScheme: const ColorScheme.light(
          background: Colors.transparent,
          primary: Color(0xFFEA580C),
          surface: Colors.white,
          onSurface: Color(0xFF2A211A),
          onPrimary: Colors.white,
        ),
      ),
      builder: (context, child) {
        return Container(color: Colors.transparent, child: child);
      },
      home: const OverlayApp(),
    ),
  );
}

final ValueNotifier<ThemeMode> themeNotifier = ValueNotifier(ThemeMode.system);

void Function(String task)? onOverlayTask;

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  if (FeatureFlags.floatingOverlayEnabled) {
    FlutterOverlayWindow.overlayListener.listen((event) {
      log("Main app received from overlay: $event");
      if (event is String && event.trim().isNotEmpty) {
        if (onOverlayTask != null) {
          onOverlayTask!(event.trim());
        } else {
          log("Warning: overlay task received but no handler registered yet");
        }
      }
    });
  }

  final prefs = await SharedPreferences.getInstance();
  final themeStr = prefs.getString('themeMode');
  if (themeStr == 'dark') {
    themeNotifier.value = ThemeMode.dark;
  } else {
    themeNotifier.value = ThemeMode.light;
  }

  final onboardingCompleted = prefs.getBool('onboarding_completed') ?? false;

  runApp(SmokerAgentApp(onboardingCompleted: onboardingCompleted));
}

class SmokerAgentApp extends StatelessWidget {
  final bool onboardingCompleted;
  const SmokerAgentApp({super.key, required this.onboardingCompleted});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<ThemeMode>(
      valueListenable: themeNotifier,
      builder: (context, ThemeMode currentMode, child) {
        return MaterialApp(
          title: 'Smoker-Agent',
          debugShowCheckedModeBanner: false,
          themeMode: currentMode,
          theme: ThemeData(
            brightness: Brightness.light,
            primaryColor: const Color(0xFFEA580C), // Ember-600
            scaffoldBackgroundColor: const Color(
              0xFFFAF6F1,
            ), // Warm bone background
            colorScheme: const ColorScheme.light(
              primary: Color(0xFFEA580C), // Ember-600
              secondary: Color(0xFFF59E0B), // Amber-500
              surface: Color(0xFFFFFFFF),
              onSurface: Color(0xFF2A211A), // Smoked charcoal
              surfaceContainerHighest: Color(0xFFF4EDE4), // Warm sand
              error: Colors.redAccent,
            ),
            useMaterial3: true,
            appBarTheme: const AppBarTheme(
              centerTitle: true,
              elevation: 0,
              scrolledUnderElevation: 0,
              backgroundColor: Colors.transparent,
              foregroundColor: Color(0xFF2A211A),
              iconTheme: IconThemeData(color: Color(0xFF2A211A)),
              systemOverlayStyle: SystemUiOverlayStyle(
                statusBarColor: Colors.transparent,
                statusBarIconBrightness: Brightness.dark,
                statusBarBrightness: Brightness.light,
              ),
            ),
            cardTheme: CardThemeData(
              elevation: 0,
              color: const Color(0xFFFFFFFF),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: const BorderSide(
                  color: Color(0xFFEDE2D4),
                  width: 1.2,
                ), // Warm border
              ),
            ),
          ),
          darkTheme: ThemeData(
            brightness: Brightness.dark,
            primaryColor: const Color(0xFFFB923C), // Ember-400
            scaffoldBackgroundColor: const Color(
              0xFF120D0A,
            ), // Deep smoke black
            colorScheme: const ColorScheme.dark(
              primary: Color(0xFFFB923C), // Ember-400
              secondary: Color(0xFFFBBF24), // Amber-400
              surface: Color(0xFF1E1811), // Warm charcoal card background
              onSurface: Color(0xFFF5EDE4), // Bone white text
              surfaceContainerHighest: Color(0xFF2A211A), // Smoked charcoal
              error: Colors.redAccent,
            ),
            useMaterial3: true,
            appBarTheme: const AppBarTheme(
              centerTitle: true,
              elevation: 0,
              scrolledUnderElevation: 0,
              backgroundColor: Colors.transparent,
              foregroundColor: Color(0xFFF5EDE4),
              iconTheme: IconThemeData(color: Color(0xFFF5EDE4)),
              systemOverlayStyle: SystemUiOverlayStyle(
                statusBarColor: Colors.transparent,
                statusBarIconBrightness: Brightness.light,
                statusBarBrightness: Brightness.dark,
              ),
            ),
            cardTheme: CardThemeData(
              elevation: 0,
              color: const Color(0xFF1E1811),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(24),
                side: BorderSide(
                  color: const Color(0xFF35291E).withOpacity(0.4),
                  width: 1.2,
                ),
              ),
            ),
          ),
          home: onboardingCompleted
              ? const HomeScreen()
              : const OnboardingScreen(),
        );
      },
    );
  }
}
'''

README_MD = r'''# Smoker-Agent

Smoker-Agent is an AI agent for Android built with Flutter. It connects to an OpenAI-compatible AI provider and uses native Android Accessibility Services to interpret screen layouts and execute multi-step tasks across any installed application via natural language commands.

## Architecture

The system operates on a continuous feedback loop:

1. The user issues a command (via voice, text, or Telegram remote access).
2. The agent captures the current screen hierarchy, calculating the exact spatial coordinates of all interactive elements.
3. The layout data is transmitted to the AI provider alongside the current task context and the result of the previous action.
4. The AI determines the next optimal action (e.g., clicking specific coordinates, inputting text, scrolling).
5. The native Android layer executes the action.
6. The loop repeats until the task is marked as complete.

## Capabilities

- **Screen Reading:** Parses the Android UI tree to map clickable, scrollable, and editable elements.
- **Coordinate-Based Interaction:** Simulates physical screen taps based on coordinate geometry, mitigating issues with missing text labels or inaccessible icons.
- **Remote Access:** Integrates with the Telegram Bot API via background polling, allowing users to issue commands and monitor task execution progress remotely.
- **Voice Control:** Native speech-to-text integration for hands-free operation.

## Installation

Download the latest APK from the [Releases Page](https://github.com/mobiclawtest-cell/private-agent/releases).

Choose `app-universal-release.apk` when it is available. It supports ARM64, 32-bit ARM, and x86_64 devices in one package. If a release only provides split APKs, most modern Android phones must use `app-arm64-v8a-release.apk`.

Smoker-Agent supports Android 8.0 (API 26) and newer. Release builds are also checked for Android 15/16's 16 KB native-library alignment requirement.

## Setup Instructions

This app requires an AI brain to operate. You can use it for free by using OpenRouter's free models.

1. Install the APK on your Android device (API 30+ recommended).
2. Go to [OpenRouter.ai](https://openrouter.ai/) and create a free account.
3. Generate a free API Key.
4. Launch Smoker-Agent and go to the **Settings** screen.
5. Tap the **"OpenRouter"** quick-select chip under Base URL.
6. Paste your API Key.
7. Type `openai/gpt-oss-120b:free` (or any other free model) into the Model field.
8. Enable the **"Smoker-Agent Screen Control"** service in your Android Accessibility Settings.

### "Restricted setting" when enabling Screen Control

Android may block accessibility access for apps installed from an APK. This is an operating-system safety restriction:

1. Open **Settings -> Apps -> Smoker-Agent**.
2. Open the three-dot menu in the top-right corner.
3. Tap **Allow restricted settings** and confirm.
4. Return to Smoker-Agent and open **Accessibility Settings** again.
5. Enable **Smoker-Agent Screen Control**.

Smoker-Agent now shows these instructions and provides shortcuts to both App Info and Accessibility Settings during onboarding.

## Telegram Integration

To enable remote access:

1. Acquire a bot token from BotFather on Telegram.
2. Input the token in the Smoker-Agent Settings screen and enable the integration toggle.
3. The application will maintain a background polling connection to the Telegram API to receive commands.

## Credits

Smoker-Agent is a rebranded build of **PrivateAgent**, originally created by **orailnoor** and **Tech Jarves**. All credit for the original design and implementation goes to them.

- Upstream project: https://github.com/orailnoor/private-agent

This project also bundles a local copy of `flutter_overlay_window`, copyright (c) 2022 Iheb Briki, released under the MIT license (see `local_plugins/flutter_overlay_window/LICENSE`).

## License

This project is open-source and available for modification.
'''


def write_files():
    (ROOT / "lib/main.dart").write_text(MAIN_DART.lstrip("\n"), encoding="utf-8")
    (ROOT / "README.md").write_text(README_MD.lstrip("\n"), encoding="utf-8")
    print("rewrote lib/main.dart (Smoker-Agent ember theme) and README.md")


FONT_URL = (
    "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/"
    "Montserrat%5Bwght%5D.ttf"
)
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(size):
    from PIL import ImageFont

    cache = Path(tempfile.gettempdir()) / "smoker-agent-montserrat.ttf"
    paths = [str(cache)] if cache.exists() else []
    if not cache.exists():
        try:
            urllib.request.urlretrieve(FONT_URL, cache)
            paths.insert(0, str(cache))
        except Exception as exc:  # network optional
            print(f"font download skipped: {exc}", file=sys.stderr)
    paths += FONT_CANDIDATES
    for candidate in paths:
        if os.path.exists(candidate):
            try:
                font = ImageFont.truetype(candidate, size)
                try:
                    font.set_variation_by_axes([800])
                except Exception:
                    pass
                return font
            except Exception:
                continue
    return ImageFont.load_default(size)


def gradient(size, top, bottom):
    from PIL import Image

    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        t = y / max(size - 1, 1)
        row = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        for x in range(size):
            px[x, y] = row
    return img


def rounded_mask(size, radius):
    from PIL import Image, ImageDraw

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return mask


def generate_logo():
    try:
        from PIL import Image, ImageDraw, ImageFilter
    except ImportError:
        print("Pillow not available; skipping logo generation", file=sys.stderr)
        return

    S = 1024
    # Smoky charcoal tile with a warm ember glow.
    base = gradient(S, (43, 33, 25), (16, 13, 11))
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([S * 0.16, S * 0.34, S * 0.84, S * 1.02], fill=(234, 88, 12, 96))
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    base = Image.alpha_composite(base.convert("RGBA"), glow)

    # Bold "S" monogram filled with an ember gradient.
    s_font = load_font(560)
    s_mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(s_mask).text((S // 2, int(S * 0.44)), "S", font=s_font, fill=255, anchor="mm")
    ember = gradient(S, (251, 191, 36), (226, 87, 12)).convert("RGBA")
    base.paste(ember, (0, 0), s_mask)

    # Letter-spaced wordmark.
    wm_font = load_font(58)
    word = "SMOKER-AGENT"
    draw = ImageDraw.Draw(base)
    spacing = 14
    widths = [draw.textlength(ch, font=wm_font) for ch in word]
    total = sum(widths) + spacing * (len(word) - 1)
    x = (S - total) / 2
    y = int(S * 0.845)
    for ch, w in zip(word, widths):
        draw.text((x, y), ch, font=wm_font, fill=(240, 226, 208, 255), anchor="lm")
        x += w + spacing

    final = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    final.paste(base, (0, 0), rounded_mask(S, 220))
    out = ROOT / "assets/app-logo.png"
    final.convert("RGB").save(out, "PNG")
    print(f"logo written -> {out.relative_to(ROOT)}")

    # Regenerate the Android launcher icons from the new mark.
    densities = {
        "mdpi": 48,
        "hdpi": 72,
        "xhdpi": 96,
        "xxhdpi": 144,
        "xxxhdpi": 192,
    }
    for density, size in densities.items():
        icon = final.resize((size, size), Image.LANCZOS)
        target = ROOT / f"android/app/src/main/res/mipmap-{density}/ic_launcher.png"
        icon.convert("RGB").save(target, "PNG")
        print(f"launcher icon -> {target.relative_to(ROOT)}")


def drop_build_report():
    stray = ROOT / "android/build"
    if stray.exists():
        shutil.rmtree(stray)
        print("removed committed gradle build output (android/build)")


def main():
    gradle = (ROOT / "android/app/build.gradle.kts").read_text(encoding="utf-8")
    if 'applicationId = "com.smoke"' in gradle:
        print("rebrand already applied; nothing to do")
        return
    drop_build_report()
    apply_replacements()
    apply_palette()
    move_kotlin_package()
    strip_youtube_promos()
    write_files()
    generate_logo()
    print("rebrand complete")


if __name__ == "__main__":
    main()
