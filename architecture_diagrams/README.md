# VLA模型架构图集

本目录包含三个最新VLA模型的专业Draw.io架构图，适用于论文、演讲和教学。

---

## 📁 文件清单

### 架构图文件

| 文件名 | 模型 | 特点 | 尺寸 |
|--------|------|------|------|
| `pi0_star_architecture.drawio` | π₀* 0.6 | RECAP训练循环 | 1600×1200 |
| `smolvla_architecture.drawio` | SmolVLA | 异步推理+社区数据 | 1600×1400 |
| `evo1_architecture.drawio` | Evo-1 | 两阶段训练+语义保留 | 1600×1500 |

### 文档文件

| 文件名 | 说明 |
|--------|------|
| `README_DESIGN_GUIDE.md` | 完整设计指南（配色、布局、连线规范） |
| `README.md` | 本文件（快速开始指南） |

---

## 🚀 快速开始

### 1. 打开架构图

#### 在线编辑（推荐）
```
1. 访问 https://app.diagrams.net/
2. File → Open from → Device
3. 选择对应的 .drawio 文件
4. 开始编辑
```

#### 离线编辑
```
1. 下载 Draw.io 桌面版: https://github.com/jgraph/drawio-desktop/releases
2. 安装后打开软件
3. 打开 .drawio 文件
```

### 2. 导出为图片

**用于论文：**
```
File → Export as → PNG
设置:
- Zoom: 100%
- Border Width: 0
- Transparent Background: ✓
- DPI: 300
```

**用于演示：**
```
File → Export as → PNG/JPEG
设置:
- Zoom: 100%
- DPI: 150-200
- Background: White
```

**矢量图：**
```
File → Export as → SVG
用于可缩放的高质量图片
```

### 3. 编辑技巧

#### 修改文本
- 双击文本框直接编辑
- 字体大小推荐：11-14px（内容），24px（标题）

#### 调整颜色
- 选中组件 → 右侧属性面板
- 填充色、边框色、文字色都可调整

#### 添加模块
- 复制现有模块（Ctrl+C, Ctrl+V）
- 使用对齐工具：Arrange → Align

---

## 🎨 架构图预览

### π₀* 0.6: 强化学习驱动的VLA

**核心特色：**
- ✨ RECAP训练循环（粉色突出显示）
- 🎯 优势条件化机制
- 📊 价值函数引导
- 🔄 专家干预数据

**配色主题：** 蓝绿紫粉四色体系

**主要组件：**
```
Input → VLM (Gemma 3) → Action Expert (860M)
                ↓
        Value Function (670M) ⟷ RECAP Loop
```

**关键指标：**
- 参数量: 4.86B
- 性能提升: 吞吐量2×，失败率降低50%
- 成功率: 90%+ (多数任务)

---

### SmolVLA: 小而美的高效VLA

**核心特色：**
- ⚡ 层跳过技术（使用前50%层）
- 🔀 交替注意力机制
- 🚀 异步推理栈（速度提升29.5%）
- 🌍 社区驱动数据（481个数据集）

**配色主题：** 靛蓝青绿橙黄体系

**主要组件：**
```
Input → VLM (SmolVLM-2) → Flow Matching Action Expert
         ↓
   Async Inference Stack (RobotClient ⟷ PolicyServer)
         ↓
   Community Data (10.6M frames)
```

**关键指标：**
- 参数量: 0.45B (比OpenVLA小15倍)
- LIBERO: 87.3% (超越7B的OpenVLA)
- 训练: 单GPU可训练
- 部署: 消费级GPU或CPU

---

### Evo-1: 语义对齐的轻量SOTA

**核心特色：**
- 🎓 两阶段训练范式（冻结→解冻）
- ✨ 语义保留机制（实验验证）
- 🌟 原生多模态VLM（InternVL3）
- 🎯 纯交叉注意力架构

**配色主题：** 青紫橙蓝粉体系

**主要组件：**
```
Stage 1: Freeze VLM + Train Action Expert
         ↓
Stage 2: Unfreeze All + Joint Fine-tuning
         ↓
Input → VLM (InternVL3-1B) → Integration Module
                              ↓
                    Cross-modulated Diffusion Transformer
```

**关键指标：**
- 参数量: 0.77B (最小SOTA)
- Meta-World: 80.6% (超越前最佳12.4%)
- LIBERO: 94.8% (竞争力表现)
- RoboTwin: 37.8% (超越前最佳6.9%)
- 无需机器人数据预训练！

---

## 🎯 使用场景

### 学术论文
```
导出格式: PNG (300 DPI) 或 SVG
放置位置: 论文的Architecture/Method章节
标注: 可添加图注解释关键组件
```

### 学术演讲
```
导出格式: PNG (150-200 DPI)
使用方式: 嵌入PPT/Keynote
建议: 分步展示，逐个模块讲解
```

### 技术博客
```
导出格式: PNG/JPEG (web优化)
大小: 压缩到<500KB
SEO: 添加alt text描述
```

### 教学材料
```
导出格式: PDF或高清PNG
用途: 课件、讲义、实验指导
互动: 可在Draw.io中添加链接
```

---

## 📊 三模型对比表

| 特性 | π₀* 0.6 | SmolVLA | Evo-1 |
|------|---------|---------|-------|
| **参数量** | 4.86B | 0.45B | **0.77B** |
| **核心创新** | RECAP训练 | 异步推理 | **语义保留** |
| **预训练需求** | 大量机器人数据 | 社区数据 | **仅VLM** |
| **训练成本** | 高 | 中 | **低** |
| **LIBERO** | 86.0% | 87.3% | **94.8%** |
| **Meta-World** | - | 57.3% | **80.6%** |
| **适用场景** | 性能关键型 | 资源受限型 | **平衡最优** |

---

## 🎨 配色方案速览

### π₀* 0.6 配色
```
🟢 Input: #E8F5E9 → #4CAF50 (绿色系)
🔵 VLM: #E3F2FD → #2196F3 (蓝色系)
🟠 Action: #FFF3E0 → #FF9800 (橙色系)
🟣 Value: #F3E5F5 → #9C27B0 (紫色系)
🔴 RECAP: #FCE4EC → #E91E63 (粉色系)
🟡 Tasks: #FFF8E1 → #FFC107 (黄色系)
```

### SmolVLA 配色
```
🔷 Input: #E8EAF6 → #3F51B5 (靛蓝系)
🟦 VLM: #E0F2F1 → #00897B (青色系)
🟠 Action: #FFF3E0 → #EF6C00 (橙色系)
🔴 Async: #FCE4EC → #C2185B (粉红系)
🟢 Data: #E8F5E9 → #388E3C (绿色系)
🟡 Perf: #FFF9C4 → #F57F17 (黄色系)
```

### Evo-1 配色
```
🟢🔵 Stages: #E8F5E9/#E3F2FD (双色)
🟠 Input: #FFF3E0 → #FF6F00 (橙色系)
🟣 VLM: #F3E5F5 → #7B1FA2 (紫色系)
🔵 Integration: #E1F5FE → #0277BD (天蓝系)
🟡 Action: #FFF8E1 → #F57F17 (黄色系)
🔴 Semantic: #FCE4EC → #C2185B (粉红系)
💧 Perf: #E0F7FA → #00838F (水蓝系)
```

---

## 🔧 常见问题

### Q: 如何修改架构图的文字？
**A:** 双击任何文本框即可直接编辑。支持中英文混合输入。

### Q: 可以更改配色方案吗？
**A:** 可以！选中组件后，在右侧属性面板调整fillColor, strokeColor, fontColor。建议参考[设计指南](README_DESIGN_GUIDE.md)中的配色表。

### Q: 如何确保导出的图片清晰？
**A:**
- 论文用途: PNG 300 DPI + 透明背景
- 网页用途: PNG 150 DPI + 白色背景
- 打印用途: PDF矢量格式（最佳）

### Q: 连线如何避免遮挡？
**A:** 编辑连线时，双击连线添加转折点（waypoint），手动调整路径避开其他组件。详见[设计指南](README_DESIGN_GUIDE.md#连线规范)。

### Q: 能否批量导出所有架构图？
**A:** 可以使用Draw.io的批处理功能，或写脚本调用命令行工具：
```bash
drawio --export --format png --output output.png input.drawio
```

### Q: 架构图可以用于商业用途吗？
**A:** 可以，这些架构图基于论文公开内容创建，可用于学术和商业用途。建议注明来源。

---

## 📖 详细文档

### 完整设计指南
查看 [README_DESIGN_GUIDE.md](README_DESIGN_GUIDE.md) 获取：
- ✅ 详细配色方案和色板
- ✅ 布局优化策略
- ✅ 连线规范和技巧
- ✅ 最佳实践和禁忌
- ✅ Draw.io使用技巧

### 论文参考
- π₀* 0.6: [Physical Intelligence Blog](https://www.physicalintelligence.company/blog/pistar06)
- SmolVLA: [arXiv:2506.01844](https://arxiv.org/abs/2506.01844)
- Evo-1: [arXiv:2511.04555](https://arxiv.org/abs/2511.04555)

---

## 🤝 贡献

欢迎贡献改进！你可以：
- 🐛 报告问题
- 💡 提出改进建议
- 🎨 分享你的配色方案
- 📝 完善文档

---

## 📄 许可

本项目基于以下资源：
- Draw.io: Apache License 2.0
- drawio-nn-templates: MIT License
- Material Design: Apache License 2.0

架构图内容基于公开论文，供学术和教育使用。

---

## ✨ 更新历史

### v1.0 (2025-01-20)
- ✅ 创建π₀* 0.6架构图
- ✅ 创建SmolVLA架构图
- ✅ 创建Evo-1架构图
- ✅ 编写设计指南
- ✅ 优化配色和布局

---

## 📧 联系

如有问题或建议，请通过Git仓库提交Issue。

---

**设计原则**: 清晰 > 美观 > 复杂
**目标**: 让每个人都能轻松理解VLA模型！

---

*持续更新中，欢迎Star和Fork！*
