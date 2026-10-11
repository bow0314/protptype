"""用 reurl.cc 替 GitHub Pages 頁面產生短網址，記錄在 short-links.json。

GitHub Pages 的網址由檔名決定，內容修改不會改變網址，
所以每頁只在第一次出現時轉一次，之後沿用 short-links.json 的紀錄。

環境變數：
- REURL_API_KEY：reurl.cc API 金鑰（放在 repo secret）
- PAGES_BASE：Pages 網址前綴，例如 https://bow0314.github.io/my-repo/
- SHORTEN_GLOBS：要轉的檔案範圍，多個用逗號分隔，例如 "*.html,pages/*.html"
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
LINKS_FILE = ROOT / "short-links.json"
SHORT_PREFIX = "https://reurl.cc/"


def shorten_url(url, api_key):
    req = urllib.request.Request(
        "https://api.reurl.cc/shorten",
        data=json.dumps({"url": url}).encode(),
        headers={"Content-Type": "application/json", "reurl-api-key": api_key},
        method="POST",
    )
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=15).read().decode())
    except urllib.error.HTTPError as e:
        print(f"  reurl.cc 回應 HTTP {e.code}：{e.read().decode(errors='replace')[:300]}")
        return None
    except Exception as e:
        print(f"  呼叫 reurl.cc 失敗：{e}")
        return None
    if data.get("res") == "success" and str(data.get("short_url", "")).startswith(SHORT_PREFIX):
        return data["short_url"]
    print(f"  reurl.cc 回應：{data}")
    return None


def main():
    api_key = os.environ.get("REURL_API_KEY", "").strip()
    if not api_key:
        sys.exit("找不到 REURL_API_KEY：請到 repo 的 Settings → Secrets and variables → Actions 新增這個 secret。")
    base = os.environ["PAGES_BASE"].rstrip("/") + "/"
    globs = [g.strip() for g in os.environ.get("SHORTEN_GLOBS", "**/*.html").split(",") if g.strip()]

    links = json.loads(LINKS_FILE.read_text(encoding="utf-8")) if LINKS_FILE.exists() else {}
    links = {k: v for k, v in links.items() if v.startswith(SHORT_PREFIX)}
    files = sorted({p for g in globs for p in ROOT.glob(g)
                    if p.is_file() and not any(part.startswith(".") for part in p.relative_to(ROOT).parts)})
    failed = []
    for f in files:
        path = f.relative_to(ROOT).as_posix()
        if path in links:
            continue
        short = shorten_url(base + urllib.parse.quote(path), api_key)
        if short:
            links[path] = short
            print(f"{path} → {short}")
        else:
            failed.append(path)
            print(f"{path} → 轉短網址失敗，下次再試")
    LINKS_FILE.write_text(json.dumps(links, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as s:
            s.write("| 頁面 | 短網址 |\n| --- | --- |\n")
            for k, v in sorted(links.items()):
                s.write(f"| {k} | {v} |\n")
    if failed:
        sys.exit(f"{len(failed)} 頁轉短網址失敗，請看上面的訊息。")


if __name__ == "__main__":
    main()
