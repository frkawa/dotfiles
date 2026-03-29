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

## ツール・環境

- シェル: zsh
- プラグインマネージャ: [Zimfw](https://zimfw.sh/)
- プロンプト: [Starship](https://starship.rs/)
- ランタイム管理: [mise](https://mise.jdx.dev/)
