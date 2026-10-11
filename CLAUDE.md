# protptype

## 短網址

- 短網址一律用 reurl.cc，不要用 TinyURL、is.gd 等其他服務。
- 金鑰放在 repo secret `REURL_API_KEY`，不能寫進程式碼或 commit。
- 短網址由 GitHub Actions（`.github/workflows/short-links.yml`）產生、記在 `short-links.json`，不要手動編造。
- 頁面檔名發布後不要改名（改名會變成新網址）。
- 新頁面合併後，從預設分支的 `short-links.json` 讀出短網址回報。
