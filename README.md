# 成都理工大学生存指南

由 determine 发起的学生共建手册，面向成都理工大学，非学校官方文件。整理日期：2026-10-03。

围绕在校学习、发展选择与办理事务提供可执行的清单。内容优先，作者背景仅在个人案例中说明。

## 项目缘起与致谢

本项目受到[上海交通大学生存手册](https://github.com/SurviveSJTU/SurviveSJTUManual)与[上海交通大学飞跃手册](https://github.com/SurviveSJTU/SJTU-Application)的启发，分为成都理工大学生存指南与飞跃手册两个独立仓库，希望持续收录成都理工大学各院系同学不同出路的真实经验。

内容组织参考[南方科技大学飞跃手册](https://github.com/SUSTech-Application/2019-Fall)和[成理工程生存指南 & 飞跃手册](https://github.com/cdutetc-tieba/CDUTETC-Guide)。感谢这些项目的作者与贡献者，也感谢 Codex、Claude Code、DeepSeek Harness 等 AI 开发工具为个人学习与初版探索提供的帮助。本站实际代码与文字整理由 Codex 辅助完成；这项致谢不代表这些工具提供方参与维护或认可本站内容。

早期保留上述项目的**参考样本入口**，供投稿者理解结构与写法；这些入口标明原校与原作者，不计为成理案例。取得转载许可前不复制全文。待成理原创投稿逐步充实后，减少首页样本入口，保留来源与致谢记录。

## 从这里开始

- [新生入学与第一个月](docs/start/arrival.md)
- [培养方案、学分与毕业要求](docs/study/degree-plan.md)
- [选课、绩点与考试复盘](docs/study/courses.md)
- [转专业：申请前到转入后](docs/study/change-major.md)
- [电子信息大类分流与方向选择](docs/study/streaming.md)
- [降级转专业后的毕业规划](docs/study/graduation.md)
- [人工智能学习：基础与可复现项目](docs/study/ai.md)
- [科研、竞赛与团队合作](docs/study/research.md)
- [图书馆、信息检索与数字工具](docs/life/library.md)
- [住宿、通勤、社团与日常生活](docs/life/living.md)
- [预算、资助与求助](docs/life/safety.md)
- [determine：2022 成理到 2026 上交](docs/experience/determine.md)

## 深入阅读

- [数学与编程：怎样把基础学扎实](docs/study/math-programming.md)
- [课程账本与学期计划模板](docs/study/course-ledger.md)
- [校内事务：找谁、带什么、怎样留记录](docs/life/services.md)
- [怎样判断经验帖与政策是否可信](docs/life/information-literacy.md)

## 使用说明
先看适用背景，再用问题清单向学院或目标单位核对。顶部支持全文搜索，侧栏提供完整导航。政策定位见[来源记录](docs/resources/sources.md)，投稿见[贡献说明](docs/contribute/index.md)。

本册通用方法已成文，真实案例目前只有作者一例。未经核实的年份、门槛与案例不编写成事实。

## 参考样本

[查看原项目样本入口](docs/resources/samples.md)

## 另一册
[成都理工大学飞跃手册](https://determine123.github.io/CDUT-Application/) 独立维护，与本册互相链接。


## 在线与本地阅读
[在线阅读](https://determine123.github.io/CDUT-Survival-Guide/) · [另一仓库](https://github.com/determine123/CDUT-Application)

网页编辑无需安装工具。可选本地环境为 Python 3.12：

```sh
python -m venv .venv
# Windows PowerShell: .venv/Scripts/Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python tools/check_links.py
python -m mkdocs serve
```

严格构建：`python -m mkdocs build --strict`。推送 main 后 Actions 构建发布；Pages 来源设置 GitHub Actions。PR 只验证，site/ 不提交。

## 投稿与许可
阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。原创文档 [CC BY 4.0](LICENSE)，参考项目注明来源，未复制其他学校内容。文字与实现使用 AI 辅助，事实来自作者确认及核查来源。
