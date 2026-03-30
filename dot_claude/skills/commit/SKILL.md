---
name: commit
description: Conventional Commits形式でgitコミットを作成する。git commitを行う時に呼び出す。
---

# commit

ステージ済みの差分を元に、Conventional Commits形式でコミットを作成する。

## コンテキスト

- ステージ済み差分: !`git diff --staged`
- ステージ済みファイル一覧: !`git diff --staged --name-only`
- 未ステージのファイル一覧: !`git diff --name-only && git ls-files --others --exclude-standard`

## 手順

1. 未ステージのファイルがある場合、`AskUserQuestion` ツールを使ってユーザーに確認する：
   - `question` に対象ファイルの一覧を列挙したうえで「ステージしますか？」と記載する
   - `options` は「ステージして続行」「中断する」の2択にする
   - 「ステージして続行」ならステージしてから続行
   - 「中断する」なら処理を止める
2. ステージ済みの差分を読んで、変更内容を把握する
3. 以下のルールに従ってコミットメッセージを決定する
4. `git commit` を実行する

## Conventional Commits ルール

### フォーマット

```
<type>[optional scope]: <description>

[optional body]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### タイプ一覧

| タイプ | 使いどころ |
|---|---|
| `feat` | 新機能の追加 |
| `fix` | バグ修正 |
| `docs` | ドキュメントのみの変更 |
| `style` | コードの動作に影響しない変更（フォーマット等） |
| `refactor` | バグ修正でも機能追加でもないコードの変更 |
| `test` | テストの追加・修正 |
| `chore` | ビルドプロセスや補助ツールの変更 |
| `ci` | CI設定の変更 |
| `perf` | パフォーマンス改善 |
| `revert` | 以前のコミットの取り消し |

### ルール

- **descriptionは日本語で書く**（明示的に英語を指定された場合のみ英語にする）
- 命令形・現在形で書く（「追加する」「修正する」等）
- 1行目は72文字以内
- `Co-Authored-By` は必ず末尾に付与する

## コミット実行

以下の形式で実行する：

```bash
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```
