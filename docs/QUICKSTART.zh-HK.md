# 學生入門：五個 AI 工作流程

先[下載 ZIP](https://github.com/ekcheungAI/super-skills/archive/refs/heads/main.zip) 並解壓。
用你平時嘅 AI coding assistant 打開資料夾，叫佢讀取指定 `SKILL.md` 同相關 references，然後交代任務。
唔熟安裝都可以先用呢個方法。

| 想做咩 | 用邊個 | 可以直接講 |
|---|---|---|
| 諗法太多，唔知由邊度開始 | superadhd | 「讀 skills/superadhd/SKILL.md，幫我理順畢業專題嘅諗法。」 |
| 想由唔同使用者角度檢查設計 | superpersona | 「用 superpersona，3 個模擬角色、1 輪，檢查呢個報名流程。」 |
| 想整網站或改善介面 | superdesign | 「用 superdesign，幫我改善學生會活動頁，同時保留原有品牌。」 |
| 想搵專門角色幫手 | agency-agents | 「用 agency-agents 嘅 code-reviewer，檢查呢份 diff。」 |
| 想有規則咁反覆改好作品 | superloop | 「用 superloop，最多 3 輪改善呢份草稿，保留原意，列出每輪改動。」 |

需要自動載入時，按你使用嘅 assistant 版本確認 skills 資料夾位置，將 `skills/` 入面五個完整資料夾複製過去。
可選安裝工具用法見 [英文 README](../README.md)。安裝工具預設只預覽，唔會覆蓋同名 skill。
呢啲檔案唔係 native agent 設定檔，唔會自動新增工具、帳戶或權限。

練習可以用「虛構學生會活動報名頁」：理順目標 → 模擬角色檢查 → 設計 → 實際測試 → 最多兩輪改善。
使用假資料，唔好放同學個人資料、密碼或 API key。AI 模擬意見唔等於真人訪談；未實測就要寫明未驗證。

套件同安裝工具本身唔需要 API key；你仍然需要自己嘅 AI assistant 帳戶，正常用量限制或收費仍然適用。
唔會附送 Mobbin、Stitch、MiroFish 或其他付費服務。
