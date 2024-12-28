from PIL import Image
import os

def optimize_images(directory):
    print("画像最適化を開始します...")

    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')) and filename != 'requirements.txt':
            filepath = os.path.join(directory, filename)

            # 元のファイルサイズを取得
            original_size = os.path.getsize(filepath) / 1024  # KBに変換

            try:
                with Image.open(filepath) as img:
                    # 画像の元のサイズを保持
                    width, height = img.size

                    # 100KB以上のファイルのみ最適化
                    if original_size > 100:
                        # より強い最適化設定
                        img.save(
                            filepath, 
                            optimize=True, 
                            quality=75,  # 品質を75%に下げる
                            progressive=True  # プログレッシブJPEGとして保存
                        )

                        # 最適化後のサイズを取得
                        new_size = os.path.getsize(filepath) / 1024

                        print(f"{filename}:")
                        print(f"  元のサイズ: {original_size:.1f}KB")
                        print(f"  最適化後: {new_size:.1f}KB")
                        print(f"  削減率: {((original_size - new_size) / original_size * 100):.1f}%")
                    else:
                        print(f"{filename}: スキップ（{original_size:.1f}KB）")
            except Exception as e:
                print(f"エラー（{filename}）: {str(e)}")

if __name__ == "__main__":
    # static/images内の画像を最適化
    image_dir = 'static/images'
    optimize_images(image_dir)