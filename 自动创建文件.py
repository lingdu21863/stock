import os
from datetime import datetime

def generate_markdown_file():
    # 获取当天日期，格式化为YYYYMMDD
    today = datetime.now().strftime('%Y-%m-%d')
    # 拼接文件名
    filename = f"{today}.md"
    
    try:
        # 获取桌面路径
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        # 确保桌面路径存在
        os.makedirs(desktop, exist_ok=True)
        # 拼接完整路径
        full_path = os.path.join(desktop, filename)
        
        # 检查文件是否已存在
        if os.path.exists(full_path):
            print(f"文件 {filename} 已存在于桌面，取消创建")
            return
        
        # 创建并写入文件
        with open(full_path, 'w', encoding='utf-8') as file:
            # 写入简单的markdown标题
            file.write(f"# {today} 笔记\n\n")
            file.write("今天记录的内容...\n")
        
        print(f"文件 {filename} 已成功保存到桌面")
        
    except Exception as e:
        print(f"创建文件时出错: {e}")

if __name__ == "__main__":
    generate_markdown_file()    