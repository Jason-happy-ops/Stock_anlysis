# AI STOCK Analysis Assistant



本项目基于Python SQL 和数据分析技术构建的股票项目



### 项目目标



学习并实践：

* Python数据分析
* SQL数据库
* Git版本控制
* 软件工程开发流程



最终实现



AKshare股票数据获取————数据库存储————数据分析————可视化————生成AI报告的完整过程



进而对后续硬件传感器接入数据库分析进行标准开发流程的训练



### 项目结构

AK\_analysis/



├── src/

├── data/

├── sql/

├── venv/

├── requirements.txt

├── .gitignore

└── README.md





### 技术栈

* Python
* Pandas
* Matplotlib
* XAMPP
* SQL
* Git





## 开发日志

2026-06-03

* ###### Situation

拟定计划书

* ###### Task

通过AI生成报告帮助老妈找到更好的进退场时机

* ###### Action

在bash里面做好venv后在IDE里面使用ctrl+shift+p选择解释器！！



2026-06-04

* ###### Situation

AKshare获取股票数据，请求容易超时

* ###### Task

需要获取三只股票行情信息

* ###### Action

尝试github中adata借口，和yfinance均失败，最后上request直接请求

* ###### Result

成功获取三只股票

* ###### Reflection

爬虫其实很不稳定，特别很多网站加强了对爬虫的管理request库只有第一次请求成功

后续如果需要稳定可以购买特定数据库的API



###### 

###### 2026-06-05

* ###### Situation

已经获取csv文件需要转移到数据库中取数

* ###### Task

设计数据库

* ###### Action

设计数据库，观察发现三张csv文件拥有相同的列名列数行数。那么是化为一张表还是两张表呢？

股票名称、股票代码属于静态信息，而每日开盘价、收盘价属于动态信息。

* ###### Result

分析后得出这里其实可以划分出两个实体：股票自身信息，股票行情他们都是1对N的表格。

在这样的方式下我们用stock\_code作为稳定的主字段，因为在后续意外情况下可以更改最少的单元





##### 2026-06-08

* ##### Situation

已了解两张表成分，着手创建两张数据库

* ##### Task

\## 数据库设计



\### stock\_price 表字段说明



| 字段名          | 类型           | 含义           | 示例         | 计算方式                                              |

|-----------------|----------------|----------------|--------------|----------------------------------------|

| `stock\_code`    | VARCHAR(10)    | 股票代码       | 601288       |                     -                     |

| `trade\_date`    | DATE           | 交易日期       | 2024-01-02   |                         -                     |

| `open\_price`    | DECIMAL(10,2)  | 开盘价（元）   | 2.92         | 早盘第一笔成交价                  |

| `close\_price`   | DECIMAL(10,2)  | 收盘价（元）   | 2.94         | 尾盘最后一笔成交价                |

| `high\_price`    | DECIMAL(10,2)  | 最高价（元）   | 2.96         | 盘中最高成交价                       |

| `low\_price`     | DECIMAL(10,2)  | 最低价（元）   | 2.91         | 盘中最低成交价                       |

| `volume`        | INT(20)        | 成交量（股）   | 3479088      | 当日总成交股数                         |

| `amount`        | DECIMAL(15,2)  | 成交额（元）   | 1274151353   | 当日总成交金额                 |

| `amplitude`     | DECIMAL(5,2)   | 振幅（%）      | 1.71         | `(high\_price - low\_price) / close\_price \* 100`|

| `pct\_change`    | DECIMAL(5,2)   | 涨跌幅（%）    | 0.68         | `(close - 昨日close) / 昨日close \* 100`      |

| `change\_amount` | DECIMAL(10,2)  | 涨跌额（元）   | 0.02         | `close\_price - 昨日close\_price`              |

| `turnover`      | DECIMAL(5,2)   | 换手率（%）    | 0.11         | `volume / 总股本 \* 100`                      |



\*\*主键\*\*：`(stock\_code, trade\_date)` 联合主键  

\*\*外键\*\*：`stock\_code` → `stock\_info(stock\_code)`  

\*\*级联\*\*：`ON DELETE CASCADE ON UPDATE CASCADE`



\*\*主键\*\*：`(stock\_code, trade\_date)` 联合主键

\*\*外键\*\*：`stock\_code` → `stock\_info(stock\_code)`



* ##### Action

明确两张数据库后，将stock\_price中的stock\_code作为外键和info表关联起来，同时使用CASCADE语法建立关联

实时更新。这样是为了保持数据一致性，自动更新清理行情数据，避免孤儿记录



* ##### Result

建造出两张数据库，接下来的任务是将三份CSV文件导入两个数据库之中，方便后续CRUD操作



* ##### Reflection

熟悉了数据库中的最基本操作，但是第一个项目能不能完整做下去也是挺考验我的……以后面对真实业务场景

要提前熟悉好字段意思，对应公式可以事半功倍

