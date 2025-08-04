
* PEP517, PEP518

## conda

> <https://www.anaconda.com/docs/getting-started/miniconda/main>
> 深度学习框架

* miniconda
* pixi
* nvdia(cuda)、intel(mlk)、amd(rocm)

## 官方体系

* 项目管理: pip、uv、poetry
* 打包: setuptools、hatchling

```
pip3 show flask
```


**虚拟环境**

```
python3 -m venv .venv
source .venv/bin/active
```

```
sys.path
```

早期处理方式

```
# 问题是分不清直接依赖、间接依赖
pip freeze > requirements.txt
pip install -r requirements.txt
```

> `pyproject.toml`


```
pip install -e .
```

## Uv

```
uv add flask
uv sync
uv run main.py
```

## Ref

* [从pip到uv：一口气梳理现代Python项目管理全流程！ - YouTube](https://www.youtube.com/watch?v=jd1aRE5pJWc&t=4s)