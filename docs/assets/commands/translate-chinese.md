# Translate English Tutorial to Chinese

Translate the English tutorial to Chinese (Simplified): $ARGUMENTS

## Phase 1: Read the English Tutorial

1. **Read the English tutorial** at `docs/$ARGUMENTS`

If the file doesn't exist, report the error and stop.

## Phase 2: Check for Existing Chinese Translation

Check if a Chinese translation already exists at `docs/zh/$ARGUMENTS`

- **If it exists:** Ask the user if they want to update the existing translation or start fresh
- **If it doesn't exist:** Proceed to create a new translation

## Phase 3: Translate to Chinese

Create the Chinese translation following these guidelines:

### Translation Rules

**Keep in English (do not translate):**
- Code blocks and commands
- Technical terms: Git, Docker, VS Code, Claude Code, WSL, Terminal, etc.
- File names and paths
- URLs and links
- Brand names and product names

**Translate to Chinese:**
- All instructional text
- Section headings
- Explanations and descriptions
- UI element names ONLY if the software has official Chinese localization
- Troubleshooting descriptions

### Language Guidelines

**Tone and Style:**
- Use Simplified Chinese (简体中文)
- Keep sentences clear and direct
- Use natural Chinese phrasing, not word-for-word translation
- Maintain a friendly but professional tone
- Use "您" for formal address when appropriate

**Common Technical Translations:**
- Click = 点击
- Type = 输入
- Open = 打开
- Close = 关闭
- Save = 保存
- File = 文件
- Folder = 文件夹
- Settings = 设置
- Install = 安装
- Download = 下载
- Run = 运行
- Button = 按钮
- Window = 窗口
- Next Steps = 下一步
- Troubleshooting = 故障排除
- What You'll Need = 您需要准备的内容
- Key Concepts = 核心概念
- Prerequisites = 前提条件
- Getting Started = 入门指南
- Step = 步骤
- Note = 注意
- Tip = 提示
- Warning = 警告

### Formatting Requirements

1. **Home Link** - Change to `[首页](./zh/)` at the top
2. **Preserve structure** - Keep the same sections and order as English
3. **Code blocks** - Copy exactly, do not translate
4. **Bold/backtick formatting** - Preserve all formatting
5. **Links** - Keep URLs unchanged, translate link text if appropriate
6. **Punctuation** - Use Chinese punctuation marks (。，！？：；""''）

## Phase 4: Create the Chinese File

1. Create the `docs/zh/` directory if it doesn't exist
2. Save the translation to `docs/zh/$ARGUMENTS`
3. Update the creation credit at the bottom (keep author name, translate surrounding text):
   - "由 [Author Name](link) 创建于 [date]。"

## Phase 5: Quality Review

Review the translation for:

- [ ] Natural Chinese flow (not literal translation)
- [ ] Consistent terminology throughout
- [ ] Correct Chinese punctuation (。，！？ instead of . , ! ?)
- [ ] No mixing of full-width and half-width characters inappropriately
- [ ] Proper use of Simplified Chinese characters
- [ ] Code blocks unchanged
- [ ] All links working
- [ ] Same structure as English original

## Phase 6: Report

Present to the user:

1. **Translation completed** - Confirm file location
2. **Key decisions made** - Any translation choices worth noting
3. **Recommendations** - Suggestions for improvement if any

## Notes

- English tutorials are in `docs/`
- Chinese translations go in `docs/zh/`
- Both should have the same filename
- When in doubt about a technical term, keep it in English
- Test that the Chinese home link `./zh/` will work in the site structure
