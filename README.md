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

pip install -r requirements.txt
pytest test_cases/ --alluredir=./allure-results
allure serve ./allure-results
