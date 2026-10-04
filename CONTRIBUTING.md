# 贡献指南

请阅读 [投稿说明](docs/contribute/index.md) 与 [模板](docs/contribute/templates.md)。

本地运行 `python tools/check_links.py` 与 `python -m mkdocs build --strict`。新增页面加入 mkdocs.yml，主分支 main。不上传隐私或生成的 site/。

## 本地检查：从仓库根目录开始

网页投稿无需安装工具。需要本地预览或排查构建问题时，使用 Python 3.12，在含有 `mkdocs.yml` 和 `requirements.txt` 的仓库根目录执行以下步骤。不要把命令运行在 `docs/` 子目录中。

Windows PowerShell（直接使用虚拟环境中的 Python，无需修改脚本执行策略）：

```powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements.txt
& ./.venv/Scripts/python.exe -m unittest discover -s tests
& ./.venv/Scripts/python.exe tools/check_links.py
& ./.venv/Scripts/python.exe -m mkdocs build --strict
& ./.venv/Scripts/python.exe -m mkdocs serve
```

macOS / Linux：

```sh
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m unittest discover -s tests
./.venv/bin/python tools/check_links.py
./.venv/bin/python -m mkdocs build --strict
./.venv/bin/python -m mkdocs serve
```

每一步成功后再继续。最后的 `serve` 用于本地预览，会持续运行；按终端提示打开本地地址，结束时按 Ctrl+C。测试、链接检查和严格构建分别检查不同内容，网页能打开不代表三项检查都通过。

出现 `No module named markdown` 或 `No module named mkdocs` 时，先确认依赖已安装成功，而且后续命令使用同一个虚拟环境 Python。链接检查报错时，根据输出核对文件路径、大小写和导航条目；不要通过删除检查步骤绕过错误。

提交前查看改动，只提交本次内容及必要导航修改。`.venv/`、`site/`、本地资料和私人材料不提交；新增页面的构建结果由 PR 检查确认，合并后的发布结果由 Pages 工作流确认。
