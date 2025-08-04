# 03 Versions

> `managed`、`system`

在大多数 uv 命令中，可以使用 `--python` 标志请求特定的 Python 版本

```bash
uv run --python 3.13 python --version
uv run --python /usr/bin/python3 python --version
```



> `.python-version`

```bash
# current directory
uv python pin 3.13

# global: ~/.config/uv/.python-version
uv python pin 3.13 --global
```



---

## 安装Python 可执行文件


🤔Python 可执行文件安装到 `~/.local/bin` 中。但`uv` 没有安装到默认的 `~/.local/bin`的情况下。

```bash
brew install uv
```

```bash
uv python install 3.12

warning: `/Users/lemon/.local/bin` is not on your PATH. To use installed Python executables, run `fish_add_path "/Users/lemon/.local/bin"` or `uv python update-shell`.
```


```bash
# https://docs.astral.sh/uv/concepts/python-versions/#installing-python-executables
uv tool update-shell

# Updated configuration file: /Users/lemon/.config/fish/config.fish
# Restart your shell to apply changes

# /Users/lemon/.config/fish/config.fish
fish_add_path "/Users/lemon/.local/bin"
```

🤔：思考 `~/.config/fish/conf.d/uv.env.fish` 文件。 理解这个命令存在的意义



## 查找 Python 可执行文件



```bash
# 默认情况下，这将显示第一个可用 Python 可执行文件的路径
uv python find
```



**查找规则**

* `UV_PYTHON_INSTALL_DIR` 中的托管 Python 安装
* 在 macOS 和 Linux 上，`PATH` 上的 Python 解释器为 `python`、`python3` 或 `python3.x`，或 `python.exe` Windows 上的
* **在搜索托管 Python 版本时，uv 会首先选择较新的版本**



## Ref

* <https://docs.astral.sh/uv/concepts/python-versions/>