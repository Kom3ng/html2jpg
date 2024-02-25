import os

import imgkit

if __name__ == "__main__":
    path = input("path: ")

    ps = os.walk(path)

    for p, dir_lst, file_lst in ps:
        for file_name in file_lst:
            if not file_name.endswith('.html'):
                continue
            f = os.path.join(p, file_name)
            print(f"处理 {f}")
            imgkit.from_file(f, f + ".jpg")
