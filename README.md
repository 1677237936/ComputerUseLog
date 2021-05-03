# 基于Python的电脑使用情况统计系统
___
## 大学期间课程设计
*提示：项目中不自带主程序，须自行安装第三方库后可以运行，如需打包可自行打包，项目文件中Chart.exe是使用.net编写的用于显示统计图的程序，须与主程序联合使用，单独打开无效*

#### 需要使用的第三方库
*pygame,pywin32*

#### 主要功能
+ 前台/后台收集电脑各进程/窗口的运行时间**(窗口消息钩子ShellHook)**
+ 表格形式显示数据汇总
+ 表格形式显示今日数据及操作日志
+ 绘制柱形图/饼图，支持筛选指定日期/周/月/全部**(使用Echarts库)**
+ 对指定的进程限制使用时间，时间到时可进行窗口抖动/结束进程/锁屏/关机操作

#### 部分截图
文件说明
![文件说明](https://www.starlwr.com/Images/1.png)
UI
![UI](https://www.starlwr.com/Images/2.png)
数据汇总
![数据汇总](https://www.starlwr.com/Images/3.png)
今日数据
![今日数据](https://www.starlwr.com/Images/4.png)
柱形图
![柱形图](https://www.starlwr.com/Images/5.png)
饼图
![饼图](https://www.starlwr.com/Images/6.png)