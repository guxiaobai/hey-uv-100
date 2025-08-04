
* pkg
* apt
* pyenv

---

* 环境: venv、virtualenv
* 安装依赖: pip、pipenv、poetry、pipx
* 检查类型: ruff

---

* 确定版本
* 解决依赖





---
> 临时运行一个脚本

```
uv run -p 3.13 ai.py
uv run -p 3.13 python
```

> 初始化一个项目

```
uv init -p 3.33

# .python-version
# .venv
# pyproject.toml
```

> 在项目内运行脚本

```bash
uv run main.py
```

---

```
uv add ruff --dev
uv remove ruff --dev
```

> 独立安装, 会为每个工具建立自己的虚拟环境

```
uv tool install ruff
which ruff
uv tool list
```

> 打包 whl

```
[project.scripts]
ai = "ai:main"
```



## Ref

 [用uv管理Python的一切！ - YouTube](https://www.youtube.com/watch?v=aVXs8lb7i9U&t=7s)