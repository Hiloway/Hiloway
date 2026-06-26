Hiloway

中国矿业大学 地理信息科学专业 本科

[GitHub](https://github.com/Hiloway) · [Email](xccg0010014@gmail.com)


研究兴趣集中在自动驾驶中的三维视觉感知，特别是激光雷达点云理解、三维目标检测与稀疏表示学习。
---

## 研究方向

- **三维计算机视觉**：激光雷达点云处理、3D目标检测、稀疏点云表示学习。
- **自动驾驶环境感知**：长距离与遮挡条件下的鲁棒感知、多模态融合感知。
- **空间智能**：具身智能与三维场景理解、不确定性感知方法。

---

## 技术能力

**编程语言**  
Python, C++, SQL, JavaScript

**深度学习与框架**  
PyTorch, CUDA, TensorBoard

**三维感知与视觉**  
[OpenPCDet](https://github.com/open-mmlab/OpenPCDet), OpenCV, NumPy, SciPy

**GIS 与空间计算**  
QGIS, ArcGIS, WebGIS开发 (OpenLayers / Leaflet)

**开发环境与工具**  
Linux, Git, Docker

---

## 主要项目

### DUD-Net

针对激光雷达点云在远距离和遮挡条件下的稀疏性，设计的一种即插即用的前端特征编码增强框架。

- 基于密度的体素特征自适应增强机制
- 点云特征的不确定性估计模型
- 稀疏场景下的点云特征扩散优化
- 在 KITTI 与 Waymo Open Dataset 上完成全量实验验证

当前状态：源码将随之开源。

### GeoPlan - 智能选址决策 WebGIS 平台

独立设计并实现的轻量化 WebGIS 系统，集成时空数据渲染、交互式沙盒选址与多方案比选面板。全链路使用标准 GeoJSON 与 EPSG:4326 进行前后端数据交互。

### 车道优 - WebGIS 车道健康度监测与养护管理平台

[![Repository](https://img.shields.io/badge/GitHub-chedaoyou-blue?logo=github)](https://github.com/Hiloway/chedaoyou)

基于 WebGIS 的车道病害智能检测与维护调度系统，集成 AI 视觉诊断与空间热点分析。

- **实时路网**：天地图底图 + OpenStreetMap Overpass API 拉取真实路网，支持框选区域补全
- **AI 病害诊断**：通义千问 VL 视觉识别病害类型与严重度，输出维修材料/工艺/通行管控方案；DeepSeek 文本分析路段养护建议
- **空间分析**：Getis-Ord Gi* 热点分析 + 核密度估计，区域健康度评分与可视化
- **工作流引擎**：上报 → 指派 → 维修 → 验收 → 完成，五状态流转 + 历史记录回溯
- **多角色协同**：管理员 / 维修方 / 普通用户三角色权限，JWT 鉴权
- **坐标系适配**：GCJ02 / WGS84 互转，支持百度街景联动

技术栈：React 19 + TypeScript + Vite + Leaflet ｜ Express 5 + MySQL + JWT ｜ DeepSeek + 通义千问 VL（后端代理）

---

## 统计

![GitHub 统计](https://github-readme-stats.vercel.app/api?username=Hiloway&show_icons=false&theme=graywhite&hide_border=true&rank_icon=github)
![连续贡献](https://streak-stats.demolab.com/?user=Hiloway&theme=graywhite&hide_border=true)

---

## 联系方式

- GitHub: [Hiloway](https://github.com/Hiloway)
- Email: `xccg0010014@gmail.com` 
