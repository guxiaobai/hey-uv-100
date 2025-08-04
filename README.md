

# Hey Uv 101


## macOS

```bash
# ls -al /opt/homebrew/share/fish/vendor_completions.d|grep uv
brew install uv

# echo $PATH
# ~/.local/bin
uv tool update-shell
```



## Standalone

```bash
curl -LsSf https://astral.sh/uv/0.8.4/install.sh | sh

# enable shell autocompletion for uv commands
echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish

# enable shell autocompletion for uvx
echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish
```



## 问题

是给全局使用的工具，不是绑定到某个项目的，所以它不能因为你切换了项目目录的 .python-version 就换 Python 版本，这样会导致工具不稳定。

```bash
uv python pin 3.11 --global

# 正确: 3.11.13
uv python find --show-version
# 正确: 3.11.13
uv run python --version

# 错误: 3.13.5
uvx python --version
# 错误: Python 3.13.5
uv tool run python --version
```



## Ref

* <https://docs.astral.sh/uv/>
* [用uv管理Python的一切！ - YouTube](https://www.youtube.com/watch?v=aVXs8lb7i9U)