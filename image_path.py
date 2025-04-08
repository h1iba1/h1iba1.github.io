
import re
from pathlib import Path
import sys

def batch_convert(root_path):
    """递归遍历目录处理所有Markdown文件"""
    success_count = 0
    failure_count = 0

    for md_file in Path(root_path).rglob('*.md'):
        print(f"\n处理文件中: {md_file}")
        try:
            if convert_image_paths(md_file):
                success_count += 1
                print(f"[✓] 成功处理：{md_file.name}")
            else:
                failure_count += 1
        except Exception as e:
            print(f"[×] 处理失败：{str(e)}")
            failure_count += 1

    print(f"\n处理完成：成功 {success_count} 个，失败 {failure_count} 个")

def convert_image_paths(md_file_path):
    """核心转换函数"""
    try:
        full_path = md_file_path.resolve()
        parts = full_path.parts

        # 定位_posts目录索引
        posts_index = parts.index('_posts')
        relative_path = Path(*parts[posts_index+1:-1])  # 提取中间目录

        # 构建GitHub前缀
        github_prefix = f"https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/{relative_path}/images/"

        # 读取并转换内容
        with open(full_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            # 增强正则匹配规则
            pattern = re.compile(
                r'!\[(.*?)\]\((?:images/)?(.*?)\)',
                flags=re.IGNORECASE
            )
            new_content = pattern.sub(
                lambda m: f'![{m.group(1)}]({github_prefix}{m.group(2)})',
                content
            )
            # 回写文件
            f.seek(0)
            f.write(new_content)
            f.truncate()
        return True
    except ValueError:
        print(f"[路径错误] 文件路径必须包含_posts目录: {md_file_path}")
        return False
    except Exception as e:
        print(f"[处理异常] {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "/blog/h1iba1.github.io/_posts/社会工程学"  # 默认处理目录

    if not Path(target_path).exists():
        print(f"错误：路径不存在 {target_path}")
        sys.exit(1)

    print(f"开始批量处理目录: {target_path}")
    batch_convert(target_path)
