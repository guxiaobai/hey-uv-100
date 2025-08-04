```bash
brew install python@3.12 python-tk@3.12
fish_add_path /opt/homebrew/opt/python@3.12/libexec/bin
```



## 方案一

> `~/.config/pip/pip.conf`



```ini
[global]
break-system-packages = true
user = true
```



```bash
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```



## 方案二Pipx()



```bash
# dependencies for pipx: python@3.13
brew install pipx
pipx ensurepath  # 确保 ~/.local/bin 加入 PATH
```

## 📦 pipx 的原理和组成

### 1. 自动管理虚拟环境

每个安装的工具都有独立的虚拟环境，存放在 `~/.local/pipx/venvs/` 中。

### 2. 自动把 CLI 命令暴露到全局

把 CLI 工具（比如 `ansible`）的可执行文件软链接到 `~/.local/bin/`，只要这个目录在你的 `PATH` 中，你就可以在任何地方调用。

### 3. 不污染全局环境

因为每个工具都有自己的依赖环境，多个 CLI 工具之间也不会互相冲突。



## 🧪 举个例子（底层行为）

当你运行：

```bash
pipx install ansible
```

pipx 执行的大致相当于：

```bash
python3 -m venv ~/.local/pipx/venvs/ansible
~/.local/pipx/venvs/ansible/bin/pip install ansible
ln -s ~/.local/pipx/venvs/ansible/bin/ansible ~/.local/bin/ansible
```



## Ref



* <https://github.com/pypa/pipx>

* <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible>
* <https://pip.pypa.io/en/stable/topics/configuration/>