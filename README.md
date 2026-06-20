# API自动化测试演示项目

## 项目简介
本项目用于展示API自动化测试的基础能力。使用公开的测试API（JSONPlaceholder）作为被测对象，覆盖了常见的HTTP方法（GET/POST/PUT/DELETE），并集成了Allure测试报告。

## 技术栈
- Python 3.9+
- pytest - 测试框架
- requests - HTTP客户端
- allure-pytest - 测试报告

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/Ningyu24/api_test_project.git
cd test_cases
2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 运行所有测试

```bash
pytest test_cases/ -v --alluredir=./allure-results
```

（test_cases/ 是存放测试用例的目录，如果你将测试文件放在根目录，则直接执行 pytest 即可）

4. 查看 Allure 报告

```bash
allure serve ./allure-results
```

浏览器会自动打开报告页面。

测试用例覆盖说明

用例 ID 测试点 请求方式 输入数据 预期结果
TC-01 获取所有帖子 GET /posts 200，返回列表且长度大于 0
TC-02 获取单个存在的帖子 GET /posts/1 200，返回数据的 id 为 1
TC-03 获取不存在的帖子 GET /posts/99999 404
TC-04 创建帖子（完整数据） POST 包含 title, body, userId 201，返回数据包含发送的所有字段，并自动生成 id
TC-05 创建帖子（缺少字段） POST 仅含 title 201（JSONPlaceholder 不校验，但真实项目应返回 400/422）
TC-06 创建帖子（空数据） POST {} 201（同上，仅为模拟）

说明：由于 JSONPlaceholder 是模拟 API，不会严格校验请求体，因此 TC-05 和 TC-06 实际返回 201。但在简历或面试中可补充说明：“我意识到 Mock API 的限制，真实项目中我会预期 400/422，并在代码中注释了这一点。”

项目目录结构

```
.
├── test_cases/
│   └── test_posts.py          # 所有 /posts 相关的测试用例
├── requirements.txt           # 依赖清单
├── README.md                  # 项目说明
└── .gitignore                 # 忽略 allure-results 等临时文件（可选）
```

运行结果示例

<img width="1891" height="959" alt="image" src="https://github.com/user-attachments/assets/1722f407-70fb-43da-a4f4-ad1f49981464" />


后续计划

· 增加更多资源（如 /comments、/users）的测试
· 集成 GitHub Actions，实现每次提交自动运行测试
· 引入参数化测试，减少重复代码
· 增加日志记录，便于调试

联系方式

如有问题，欢迎通过 GitHub Issues 交流。

```

---
