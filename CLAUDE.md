# CLAUDE.md

このリポジトリは [chezmoi](https://www.chezmoi.io/) で管理する dotfiles プロジェクトです。

## リポジトリ構造

chezmoi の規則に従い、ファイル名をプレフィックスでエンコードして管理します。

- `dot_*` → `.*`（例: `dot_zshrc` → `~/.zshrc`）

## 管理しているファイル

| chezmoi パス | 展開先 |
|---|---|
| `dot_zshrc` | `~/.zshrc` |
| `dot_zimrc` | `~/.zimrc` |
| `private_dot_config/starship.toml` | `~/.config/starship.toml` |
| `private_dot_config/mise/config.toml` | `~/.config/mise/config.toml` |
| `private_dot_config/private_karabiner/private_karabiner.json` | `~/.config/karabiner/karabiner.json` |
| `private_Library/private_Application Support/private_Code/User/settings.json` | `~/Library/Application Support/Code/User/settings.json` |
| `private_Library/private_Application Support/com.mitchellh.ghostty/config.ghostty` | `~/Library/Application Support/com.mitchellh.ghostty/config.ghostty` |
| `dot_claude/settings.json` | `~/.claude/settings.json` |
| `dot_claude/scripts/status_line/executable_statusline.py` | `~/.claude/scripts/status_line/statusline.py` |
| `dot_claude/skills/commit/SKILL.md` | `~/.claude/skills/commit/SKILL.md` |

## chezmoi 運用方針

設定ファイルを変更する場合は **sourceディレクトリを正（source of truth）** とする。

### 変更フロー

1. `chezmoi edit <ターゲットパス>` でsourceファイルを編集
2. `chezmoi apply` でターゲットに反映
3. commitスキルで変更を記録

### `chezmoi add` の用途

新規ファイルをchezmoi管理に追加する場合のみ使用する。
ターゲットを直接編集してsourceに逆反映する用途では使わない。

### ファイルの追加・削除時

`chezmoi add` で管理対象を追加、または管理対象からファイルを削除した場合は、上記「管理しているファイル」の一覧を必ず更新する。

## ツール・環境

- シェル: zsh
- プラグインマネージャ: [Zimfw](https://zimfw.sh/)
- プロンプト: [Starship](https://starship.rs/)
- ランタイム管理: [mise](https://mise.jdx.dev/)
