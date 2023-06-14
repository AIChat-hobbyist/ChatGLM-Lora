# 创建一个空列表来存储问题和答案
qa_list = []
# 用一个循环来输入问题和答案，直到输入"q"为止
while True:
    # 输入问题
    question = input("请输入问题，或输入'q'退出：")
    # 如果输入"q"，则退出循环
    if question == "q":
        break
    # 输入答案
    answer = input("请输入答案：")
    # 创建一个字典来存储问题和答案
    qa_dict = {"q": question, "o": answer}
    # 把字典添加到列表中
    qa_list.append(qa_dict)
    # 导入json模块
    import json
    # 把列表转换成json格式的字符串
    json_str = json.dumps(qa_list, ensure_ascii=False, indent=4)
    # 打开一个文件，如果不存在则创建，如果存在则覆盖
    with open("ayaka.json", "w", encoding="utf-8") as f:
        # 把json字符串写入文件中
        f.write(json_str)
        # 关闭文件
        f.close()
        # 打印提示信息
        print("已保存到ayaka.json文件中")

# 打印提示信息
print("程序结束")
